"""
generate_sop60_audit_pdf.py — Body PDF generator for the Well Spring Intervention
SOP Manual v2.24 / CARF Plans v1.2 Operational Audit Report (Task SOP-60).

Audit scope: Full operational audit of (1) service-code citation accuracy,
(2) staffing-ratio compliance with 10A NCAC 27G .1704 codified minimums,
(3) facility-capacity limit per .1706(a), (4) Alliance Health Tailored Plan
nomenclature, (5) WakeMed out-of-network status effective July 1, 2026, and
(6) policy completeness across the SOP Manual + CARF Conformance Plans portfolio.

Pipeline:
  1. Build body PDF via ReportLab (TOC + 8 content sections)
  2. Merge with cover PDF (scripts/audit_cover.pdf) via pypdf
  3. Output: /home/z/my-project/download/WSI_SOP_v2.24_Operational_Audit_Report.pdf
"""

import os
import sys
import hashlib
import subprocess
from pathlib import Path

# Make sop60_findings importable
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sop60_findings import FINDINGS, summary_stats, SEVERITY_LEGEND, STATUS_LEGEND

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch, mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle,
    KeepTogether, CondPageBreak, Image, HRFlowable,
)
from reportlab.platypus.tableofcontents import TableOfContents
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFontFamily

# ─── Font registration (reuse existing fonts) ──────────────────────────────
FONT_DIR = '/usr/share/fonts'
pdfmetrics.registerFont(TTFont('FreeSerif',          f'{FONT_DIR}/truetype/freefont/FreeSerif.ttf'))
pdfmetrics.registerFont(TTFont('FreeSerif-Bold',     f'{FONT_DIR}/truetype/freefont/FreeSerifBold.ttf'))
pdfmetrics.registerFont(TTFont('FreeSerif-Italic',   f'{FONT_DIR}/truetype/freefont/FreeSerifItalic.ttf'))
pdfmetrics.registerFont(TTFont('FreeSerif-BoldItalic', f'{FONT_DIR}/truetype/freefont/FreeSerifBoldItalic.ttf'))
pdfmetrics.registerFont(TTFont('NotoSerifSC',        f'{FONT_DIR}/truetype/noto-serif-sc/NotoSerifSC-Regular.ttf'))
pdfmetrics.registerFont(TTFont('NotoSerifSC-Bold',   f'{FONT_DIR}/truetype/noto-serif-sc/NotoSerifSC-Bold.ttf'))
pdfmetrics.registerFont(TTFont('DejaVuSans',         f'{FONT_DIR}/truetype/dejavu/DejaVuSansMono.ttf'))
registerFontFamily('FreeSerif', normal='FreeSerif', bold='FreeSerif-Bold',
                   italic='FreeSerif-Italic', boldItalic='FreeSerif-BoldItalic')
registerFontFamily('NotoSerifSC', normal='NotoSerifSC', bold='NotoSerifSC-Bold')

# ─── Brand palette (matching v2.22 audit) ─────────────────────────────────
PAGE_BG       = colors.HexColor('#FAF6EE')   # warm cream parchment
SECTION_BG    = colors.HexColor('#F1ECE0')
CARD_BG       = colors.HexColor('#FFFFFF')
TABLE_STRIPE  = colors.HexColor('#F5F0E2')
HEADER_FILL   = colors.HexColor('#7C2D12')   # deep terracotta
COVER_BLOCK   = colors.HexColor('#5C4A2E')
BORDER        = colors.HexColor('#D6CFC0')
ICON          = colors.HexColor('#7C2D12')
ACCENT        = colors.HexColor('#7C2D12')
ACCENT_2      = colors.HexColor('#3B6E8F')
TEXT_PRIMARY  = colors.HexColor('#1F2937')
TEXT_MUTED    = colors.HexColor('#6B6457')

# Severity colors
SEV_CRITICAL  = colors.HexColor('#7F1D1D')
SEV_HIGH      = colors.HexColor('#991B1B')
SEV_MEDIUM    = colors.HexColor('#B45309')
SEV_LOW       = colors.HexColor('#4D7C0F')
SEV_INFO      = colors.HexColor('#1E40AF')

STATUS_COLORS = {
    'Met':         colors.HexColor('#166534'),
    'Met-Exceeds': colors.HexColor('#166534'),
    'Partial':     colors.HexColor('#B45309'),
    'Gap':         colors.HexColor('#991B1B'),
    'Contradicts': colors.HexColor('#7F1D1D'),
    'N/A':         colors.HexColor('#6B6457'),
}

# ─── Styles ────────────────────────────────────────────────────────────────
STY = {}
STY['title'] = ParagraphStyle('title', fontName='FreeSerif-Bold', fontSize=24,
                              textColor=HEADER_FILL, alignment=TA_LEFT,
                              spaceBefore=0, spaceAfter=8, leading=30)
STY['h1'] = ParagraphStyle('h1', fontName='FreeSerif-Bold', fontSize=18,
                           textColor=HEADER_FILL, alignment=TA_LEFT,
                           spaceBefore=20, spaceAfter=10, leading=24)
STY['h2'] = ParagraphStyle('h2', fontName='FreeSerif-Bold', fontSize=14,
                           textColor=TEXT_PRIMARY, alignment=TA_LEFT,
                           spaceBefore=14, spaceAfter=6, leading=20)
STY['h3'] = ParagraphStyle('h3', fontName='FreeSerif-Bold', fontSize=12,
                           textColor=TEXT_PRIMARY, alignment=TA_LEFT,
                           spaceBefore=10, spaceAfter=4, leading=16)
STY['body'] = ParagraphStyle('body', fontName='FreeSerif', fontSize=10.5,
                             textColor=TEXT_PRIMARY, alignment=TA_JUSTIFY,
                             spaceBefore=0, spaceAfter=8, leading=15.5)
STY['body_left'] = ParagraphStyle('body_left', fontName='FreeSerif', fontSize=10.5,
                                  textColor=TEXT_PRIMARY, alignment=TA_LEFT,
                                  spaceBefore=0, spaceAfter=8, leading=15.5)
STY['quote'] = ParagraphStyle('quote', fontName='FreeSerif-Italic', fontSize=10,
                              textColor=TEXT_MUTED, alignment=TA_LEFT,
                              leftIndent=18, rightIndent=18,
                              spaceBefore=4, spaceAfter=8, leading=14.5,
                              borderColor=BORDER, borderWidth=0,
                              borderPadding=(6, 10, 6, 10),
                              backColor=TABLE_STRIPE)
STY['rule_text'] = ParagraphStyle('rule_text', fontName='FreeSerif', fontSize=9.5,
                                  textColor=TEXT_PRIMARY, alignment=TA_LEFT,
                                  leftIndent=12, rightIndent=12,
                                  spaceBefore=2, spaceAfter=6, leading=13.5,
                                  borderColor=BORDER, borderWidth=0.5,
                                  borderPadding=(6, 10, 6, 10),
                                  backColor=SECTION_BG)
STY['meta'] = ParagraphStyle('meta', fontName='FreeSerif', fontSize=9,
                             textColor=TEXT_MUTED, alignment=TA_LEFT,
                             spaceBefore=0, spaceAfter=3, leading=12.5)
STY['finding_meta'] = ParagraphStyle('finding_meta', fontName='FreeSerif-Bold', fontSize=10,
                                     textColor=HEADER_FILL, alignment=TA_LEFT,
                                     spaceBefore=12, spaceAfter=4, leading=14)
STY['table_header'] = ParagraphStyle('table_header', fontName='FreeSerif-Bold', fontSize=9.5,
                                     textColor=colors.white, alignment=TA_CENTER, leading=12)
STY['table_cell'] = ParagraphStyle('table_cell', fontName='FreeSerif', fontSize=9,
                                   textColor=TEXT_PRIMARY, alignment=TA_LEFT, leading=12)
STY['table_cell_center'] = ParagraphStyle('table_cell_center', fontName='FreeSerif', fontSize=9,
                                          textColor=TEXT_PRIMARY, alignment=TA_CENTER, leading=12)
STY['toc_h1'] = ParagraphStyle('toc_h1', fontName='FreeSerif-Bold', fontSize=12,
                               textColor=TEXT_PRIMARY, leftIndent=10, leading=20)
STY['toc_h2'] = ParagraphStyle('toc_h2', fontName='FreeSerif', fontSize=10.5,
                               textColor=TEXT_MUTED, leftIndent=30, leading=16)

# ─── TocDocTemplate with header/footer ────────────────────────────────────
class TocDocTemplate(SimpleDocTemplate):
    def afterFlowable(self, flowable):
        if hasattr(flowable, 'bookmark_name'):
            level = getattr(flowable, 'bookmark_level', 0)
            text = getattr(flowable, 'bookmark_text', '')
            key = getattr(flowable, 'bookmark_key', '')
            self.notify('TOCEntry', (level, text, self.page, key))

def add_heading(text, style, level=0):
    key = 'h_%s' % hashlib.md5(text.encode()).hexdigest()[:8]
    p = Paragraph('<a name="%s"/>%s' % (key, text), style)
    p.bookmark_name = text
    p.bookmark_level = level
    p.bookmark_text = text
    p.bookmark_key = key
    return p

def header_footer(canvas, doc):
    canvas.saveState()
    page_w, page_h = A4
    # Header
    canvas.setFont('FreeSerif', 8)
    canvas.setFillColor(TEXT_MUTED)
    canvas.drawString(0.85 * inch, page_h - 0.45 * inch,
                      'Well Spring Intervention LLC — SOP v2.24 / CARF Plans v1.2 Operational Audit')
    canvas.drawRightString(page_w - 0.85 * inch, page_h - 0.45 * inch,
                           'Doc. WSI-SOP60-AUDIT-001 · Rev. 1.0')
    canvas.setStrokeColor(BORDER)
    canvas.setLineWidth(0.5)
    canvas.line(0.85 * inch, page_h - 0.55 * inch,
                page_w - 0.85 * inch, page_h - 0.55 * inch)
    # Footer
    canvas.drawString(0.85 * inch, 0.45 * inch, 'Confidential — Internal Compliance Use')
    canvas.drawRightString(page_w - 0.85 * inch, 0.45 * inch, 'Page %d' % doc.page)
    canvas.line(0.85 * inch, 0.6 * inch,
                page_w - 0.85 * inch, 0.6 * inch)
    canvas.restoreState()

# ─── Helper: build a single finding block ──────────────────────────────────
def finding_block(f, level=2):
    sev = f['severity']
    sev_color = {'Critical': SEV_CRITICAL, 'High': SEV_HIGH, 'Medium': SEV_MEDIUM,
                 'Low': SEV_LOW, 'Info': SEV_INFO}[sev]
    status_color = STATUS_COLORS.get(f['status'], TEXT_PRIMARY)

    out = []
    header_text = (
        f"<b>{f['id']}</b> &nbsp;&nbsp; "
        f"<font color='{sev_color.hexval()}'>[{sev}]</font> &nbsp;&nbsp; "
        f"<font color='{status_color.hexval()}'>[{f['status']}]</font> &nbsp;&nbsp; "
        f"<b>{f['rule']}</b> — {f['rule_title']}"
    )
    out.append(Paragraph(header_text, STY['finding_meta']))
    out.append(HRFlowable(width='100%', thickness=0.5, color=BORDER,
                          spaceBefore=2, spaceAfter=6))

    meta_rows = [
        [Paragraph('<b>Rule text</b>', STY['table_cell']),
         Paragraph(f['rule_text'], STY['table_cell'])],
        [Paragraph('<b>Source location</b>', STY['table_cell']),
         Paragraph(f['sop_loc'], STY['table_cell'])],
        [Paragraph('<b>Source quote / paraphrase</b>', STY['table_cell']),
         Paragraph(f['sop_quote'], STY['table_cell'])],
        [Paragraph('<b>Strip flag</b>', STY['table_cell']),
         Paragraph(f"<b>{f['strip_flag']}</b> — {f['strip_note']}", STY['table_cell'])],
    ]
    avail = A4[0] - 1.7 * inch
    meta_tbl = Table(meta_rows, colWidths=[1.4 * inch, avail - 1.4 * inch], hAlign='CENTER')
    meta_tbl.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), TABLE_STRIPE),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('LINEABOVE', (0, 0), (-1, 0), 0.4, BORDER),
        ('LINEBELOW', (0, -1), (-1, -1), 0.4, BORDER),
        ('LINEBETWEEN', (0, 0), (-1, -1), 0.3, BORDER),
    ]))
    out.append(meta_tbl)
    out.append(Spacer(1, 6))

    out.append(Paragraph('<b>Finding.</b> ' + f['finding'], STY['body']))
    out.append(Paragraph('<b>Remediation.</b> ' + f['remediation'], STY['body']))
    out.append(Spacer(1, 8))
    return out


# ─── Main builder ──────────────────────────────────────────────────────────
def build_body_pdf(output_path):
    doc = TocDocTemplate(
        output_path, pagesize=A4,
        leftMargin=0.85 * inch, rightMargin=0.85 * inch,
        topMargin=0.85 * inch, bottomMargin=0.85 * inch,
        title='Well Spring Intervention SOP v2.24 / CARF Plans v1.2 Operational Audit Report',
        author='Z.ai', creator='Z.ai',
        subject='Operational audit of SOP Manual v2.24 and CARF Plans v1.2 — service code, staffing, capacity, Alliance Health Tailored Plan, WakeMed OON, policy completeness',
    )

    story = []
    stats = summary_stats()

    # ─── TOC ───────────────────────────────────────────────────────────────
    story.append(Paragraph('<b>Table of Contents</b>', STY['title']))
    story.append(HRFlowable(width='100%', thickness=1.5, color=HEADER_FILL,
                            spaceBefore=4, spaceAfter=14))
    toc = TableOfContents()
    toc.levelStyles = [STY['toc_h1'], STY['toc_h2']]
    story.append(toc)
    story.append(PageBreak())

    # ─── 1. Executive Summary ─────────────────────────────────────────────
    story.append(add_heading('1. Executive Summary', STY['h1'], level=0))
    story.append(Paragraph(
        "This report documents a full operational audit of two interrelated Well Spring "
        "Intervention LLC deliverables — the <b>Standard Operating Procedure &amp; Operational "
        "Manual, Revision 2.24 (August 2026, Legislation-Free Public Edition)</b> and the "
        "<b>CARF CYS 2026 Conformance Plans Portfolio, Revision 1.2 (August 2026)</b> — "
        "triggered by the user's directive to verify the staffing ratios against the correct "
        "NC service code, audit the SOP for any errors, confirm Wake County NC operational "
        "readiness, and confirm policy completeness in preparation for the CARF CYS 2026 "
        "Inaugural Accreditation survey.",
        STY['body']))
    story.append(Paragraph(
        "The audit identifies <b>%d total findings</b>: %d Critical severity (license-"
        "blocking or survey-blocking), %d High severity (direct rule violation with "
        "regulatory or billing impact), %d Medium severity (partial compliance or "
        "documentation gap), and %d informational findings confirming compliance." % (
            stats['total_findings'],
            stats['by_severity'].get('Critical', 0),
            stats['by_severity'].get('High', 0),
            stats['by_severity'].get('Medium', 0),
            stats['by_severity'].get('Info', 0),
        ),
        STY['body']))
    story.append(Paragraph(
        "Of the %d findings, %d confirm full compliance (Met or Met-Exceeds), %d identify "
        "partial compliance gaps, %d identify complete gaps where the source documents do "
        "not address a rule requirement, and %d identify internal contradictions requiring "
        "resolution. The Critical findings cluster around a single root cause: the CARF Plans "
        "v1.2 was over-corrected in SOP-59 when the user clarified the program is a 'staff "
        "secure group home' rather than a hardware-secure Level III RTF, and the corrective "
        "action stripped out the .1700 citation entirely. Verified research confirms that "
        "'staff secure' IS the .1701(b) sub-category within the .1700 Residential Treatment "
        "Facilities series in NC 10A NCAC 27G; there is no separate 'Staff Secure Group "
        "Home' license category in NC. The CARF Plans v1.2 therefore contradicts the SOP "
        "Manual v2.24 (which correctly cites .1700/.1701(b)) and must be re-aligned." % (
            stats['total_findings'],
            stats['by_status'].get('Met', 0) + stats['by_status'].get('Met-Exceeds', 0),
            stats['by_status'].get('Partial', 0),
            stats['by_status'].get('Gap', 0),
            stats['by_status'].get('Contradicts', 0),
        ),
        STY['body']))

    story.append(add_heading('1.1 Critical Findings (License-Blocking)', STY['h2'], level=1))
    story.append(Paragraph(
        "Three Critical findings require remediation before the CARF Inaugural Accreditation "
        "survey submission. Each is summarized below; full deep-dive analysis appears in "
        "Sections A, B, and F.",
        STY['body']))
    critical_findings = [f for f in stats['critical_high_findings'] if f['severity'] == 'Critical']
    for f in critical_findings:
        story.append(Paragraph(
            f"<b>{f['id']} — {f['rule']} {f['rule_title']}.</b> {f['finding'][:400]}…",
            STY['body']))

    story.append(add_heading('1.2 High Findings (Direct Rule Violation)', STY['h2'], level=1))
    story.append(Paragraph(
        "Three High findings require remediation in the v2.25 SOP Manual and v1.3 CARF Plans "
        "revisions. Each is summarized below; full deep-dive analysis appears in Sections C, "
        "E, and F.",
        STY['body']))
    high_findings = [f for f in stats['critical_high_findings'] if f['severity'] == 'High']
    for f in high_findings:
        story.append(Paragraph(
            f"<b>{f['id']} — {f['rule']} {f['rule_title']}.</b> {f['finding'][:400]}…",
            STY['body']))

    story.append(add_heading('1.3 Compliance Strengths Confirmed', STY['h2'], level=1))
    story.append(Paragraph(
        "The audit confirmed that the SOP Manual v2.24 demonstrates strong compliance "
        "across the .1700 series rules. Key strengths confirmed by this audit: (1) §2.1 "
        "staffing ratio 2:4 minimum with both overnight staff awake exceeds .1704(c)(1)'s "
        "minimum of 'two present, one awake' — a stricter, defensible best-practice "
        "standard (F-S60-003); (2) §4.6 Licensed Professional Face-to-Face Clinical "
        "Consultation at 4 hrs/week minimum fully implements .1705(a)-(b) (F-S60-009); "
        "(3) §3.6 18th-Birthday Continuation Policy fully implements .1706(e) (F-S60-010); "
        "(4) §5.5 Activities Program at 14 hrs/week of planned group activities fully "
        "implements .1701(e) (F-S60-011); (5) §3.4(c) Post-Emergency Service-Planning "
        "Meeting within 5 business days fully implements .1708(e) (F-S60-012); "
        "(6) §1.2(g) NC Medicaid RTS Taxonomy comprehensively documents CCP 8D-2 §1.0(c) "
        "with verbatim quotes (F-S60-013); (7) §1.2(a) Accreditation Prerequisite "
        "comprehensively covers COA/TJC/CARF/CQL per NC DHHS 10A NCAC 70I (F-S60-014); "
        "(8) §1.9 Medicaid Enrollment correctly identifies NCTracks + Type 2 NPI + NUCC "
        "taxonomy 320800000X (F-S60-015). Full strengths analysis appears in Section G.",
        STY['body']))

    story.append(PageBreak())

    # ─── 2. Audit Scope, Methodology & Sources ────────────────────────────
    story.append(add_heading('2. Audit Scope, Methodology &amp; Sources', STY['h1'], level=0))
    story.append(add_heading('2.1 Scope', STY['h2'], level=1))
    story.append(Paragraph(
        "This audit covers six operational dimensions of the Well Spring Intervention LLC "
        "compliance portfolio, all of which bear directly on the CARF CYS 2026 Inaugural "
        "Accreditation survey readiness and the NC DHSR MHLC initial-licensure application: "
        "<b>(A) Service Code Citation Accuracy</b> — verify that the CARF Plans v1.2 and SOP "
        "Manual v2.24 cite the correct NC service code sub-section for the program's "
        "license category; <b>(B) Staffing Ratio Compliance</b> — verify that the documented "
        "staffing ratios meet the codified minimums in 10A NCAC 27G .1704; <b>(C) Facility "
        "Capacity Limit</b> — verify the documented maximum capacity against 10A NCAC 27G "
        ".1706(a); <b>(D) Alliance Health Tailored Plan Nomenclature</b> — verify that all "
        "references to the LME/MCO use the post-July 2024 'Tailored Plan' designation; "
        "<b>(E) WakeMed Out-of-Network Status</b> — verify that emergency hospital "
        "coordination references account for the WakeMed out-of-network termination "
        "effective July 1, 2026; and <b>(F) Policy Completeness</b> — confirm that the SOP "
        "Manual v2.24 (11 SOPs + 21 protocols + 9 forms) and CARF Plans v1.2 (15 written "
        "plans) comprehensively address the CARF CYS 2026 Inaugural Accreditation standards.",
        STY['body']))

    story.append(add_heading('2.2 Sources Audited', STY['h2'], level=1))
    story.append(Paragraph(
        "<b>Source 1.</b> Well Spring Intervention LLC SOP &amp; Operational Manual, Doc. "
        "WSI-SOP-001, Rev. 2.24, August 2026 — Legislation-Free Public Edition. "
        "Source script: /home/z/my-project/scripts/sop_content_v3.py (Part 1, ~2,705 lines) + "
        "sop_content_v3_part2.py (Part 2, Protocols) + sop_content_v3_part3.py (Part 3, Forms + "
        "Version History). Final deliverable: /home/z/my-project/download/Well_Spring_Intervention_SOP_Manual_v2.24_Public-Edition.pdf.",
        STY['body']))
    story.append(Paragraph(
        "<b>Source 2.</b> WSI CARF CYS 2026 Conformance Plans Portfolio, Doc. "
        "WSI-CARF-PLANS-001, Rev. 1.2, August 2026. Source script: "
        "/home/z/my-project/scripts/carf_plans_content.py (15 plan sections, ~2,219 lines) + "
        "generate_carf_plans.py (body PDF generator) + carf_plans_cover.html (cover) + "
        "merge_carf_plans.py (cover+body merge). Final deliverable: "
        "/home/z/my-project/download/WSI_CARF_CYS_2026_Conformance_Plans.pdf (49 pages, 5.19 MB).",
        STY['body']))
    story.append(Paragraph(
        "<b>Source 3.</b> Codified NC rule text — 10A NCAC 27G Subchapter G (Mental Health, "
        "Community Facilities and Services), Sections .1700-.1708 (Residential Treatment "
        "Staff Secure for Children or Adolescents). Verified via Cornell Law Institute Legal "
        "Information Repository (Cornell LII) codified rule text retrievals for .1701, .1702, "
        ".1703, .1704, .1705, .1706, .1901. Saved to /home/z/my-project/research_sop60/p01_1704_cornell.json "
        "through p25_*.json. Also cross-referenced against NC OAH (Office of Administrative "
        "Hearings) official publication and the Alliance Health Tailored Plan provider-network "
        "documentation.",
        STY['body']))
    story.append(Paragraph(
        "<b>Source 4.</b> Wake County NC operational requirements — Alliance Health Tailored "
        "Plan provider network status; WakeMed out-of-network termination notice effective "
        "July 1, 2026; Alliance Health in-network hospital alternatives (UNC Rex Hospital, "
        "Duke Raleigh Hospital, UNC Medical Center, Duke University Hospital). Verified via "
        "Alliance Health provider-network documentation and NC Medicaid Tailored Plan "
        "transition guidance (effective July 1, 2024 per NC S.L. 2021-135).",
        STY['body']))

    story.append(add_heading('2.3 Methodology', STY['h2'], level=1))
    story.append(Paragraph(
        "The audit followed a four-step methodology: <b>(1) Source document identification "
        "and version control</b> — the SOP Manual v2.24 and CARF Plans v1.2 source scripts "
        "were read directly (sop_content_v3*.py, carf_plans_content.py, generate_carf_plans.py, "
        "carf_plans_cover.html, merge_carf_plans.py). <b>(2) Regulatory verification</b> — "
        "the correct NC service code, staffing ratios, and capacity limit for a 'staff secure "
        "group home' were verified via web research against Cornell LII codified rule text "
        "(research_sop60/ folder contains 25 fetched web pages and 53 web search results). "
        "<b>(3) Cross-document consistency check</b> — the SOP Manual v2.24 and CARF Plans "
        "v1.2 were cross-checked for consistent terminology, citations, and cross-references. "
        "<b>(4) Wake County operational readiness check</b> — Alliance Health Tailored Plan "
        "nomenclature and WakeMed out-of-network status were verified against current "
        "(2024-2026) regulatory and provider-network publications.",
        STY['body']))

    story.append(PageBreak())

    # ─── 3. Findings Summary Matrix ──────────────────────────────────────
    story.append(add_heading('3. Findings Summary Matrix', STY['h1'], level=0))
    story.append(Paragraph(
        "The table below summarizes all %d findings. Detailed analysis for each finding "
        "appears in Sections A through G." % stats['total_findings'],
        STY['body']))

    avail_w = A4[0] - 1.7 * inch
    col_ratios = [0.07, 0.10, 0.10, 0.08, 0.08, 0.07, 0.50]
    col_widths = [r * avail_w for r in col_ratios]

    header_row = [
        Paragraph('<b>ID</b>', STY['table_header']),
        Paragraph('<b>Rule</b>', STY['table_header']),
        Paragraph('<b>Status</b>', STY['table_header']),
        Paragraph('<b>Severity</b>', STY['table_header']),
        Paragraph('<b>Strip</b>', STY['table_header']),
        Paragraph('<b>Source §</b>', STY['table_header']),
        Paragraph('<b>Finding</b>', STY['table_header']),
    ]
    data = [header_row]
    for f in FINDINGS:
        sop_short = f['sop_loc'].split(';')[0].strip()[:40]
        finding_short = f['rule_title'][:90] + ('…' if len(f['rule_title']) > 90 else '')
        sev = f['severity']
        sev_color = {'Critical': SEV_CRITICAL, 'High': SEV_HIGH, 'Medium': SEV_MEDIUM,
                     'Low': SEV_LOW, 'Info': SEV_INFO}[sev]
        status_color = STATUS_COLORS.get(f['status'], TEXT_PRIMARY)
        data.append([
            Paragraph(f"<b>{f['id']}</b>", STY['table_cell_center']),
            Paragraph(f['rule'], STY['table_cell_center']),
            Paragraph(f"<font color='{status_color.hexval()}'><b>{f['status']}</b></font>", STY['table_cell_center']),
            Paragraph(f"<font color='{sev_color.hexval()}'><b>{sev}</b></font>", STY['table_cell_center']),
            Paragraph(f['strip_flag'], STY['table_cell_center']),
            Paragraph(sop_short, STY['table_cell']),
            Paragraph(finding_short, STY['table_cell']),
        ])

    summary_tbl = Table(data, colWidths=col_widths, hAlign='CENTER', repeatRows=1)
    summary_tbl.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), HEADER_FILL),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 4),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('GRID', (0, 0), (-1, -1), 0.3, BORDER),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, TABLE_STRIPE]),
    ]))
    story.append(summary_tbl)
    story.append(Spacer(1, 10))
    story.append(Paragraph(
        f"<b>Legend.</b> Severity: Critical = license-blocking/survey-blocking; High = direct rule "
        f"violation; Medium = partial/gap; Low = clarification; Info = confirmed compliance. "
        f"Status: Met = full compliance; Met-Exceeds = stricter than rule (defensible); "
        f"Partial = missing elements; Gap = not addressed; Contradicts = inconsistent with rule. "
        f"Strip flag: Y = statutory citation to remove from public edition; N = no citation to strip.",
        STY['meta']))
    story.append(PageBreak())

    # ─── 4. SECTION A — Service Code Citation ────────────────────────────
    story.append(add_heading('4. Section A — Service Code Citation Accuracy', STY['h1'], level=0))
    story.append(Paragraph(
        "This section presents the detailed finding for the service code citation discrepancy "
        "between the SOP Manual v2.24 (correct) and the CARF Plans v1.2 (over-corrected). "
        "The root cause is documented, the regulatory framework is verified, and the "
        "remediation pathway is specified.",
        STY['body']))
    section_a = [f for f in FINDINGS if f['id'] == 'F-S60-001']
    for f in section_a:
        story.extend(finding_block(f))
    story.append(PageBreak())

    # ─── 5. SECTION B — Staffing Ratios ──────────────────────────────────
    story.append(add_heading('5. Section B — Staffing Ratio Compliance', STY['h1'], level=0))
    story.append(Paragraph(
        "This section presents the detailed findings for the staffing-ratio compliance check. "
        "Two findings are documented: F-S60-002 (CARF Plans v1.2 ratios are NON-COMPLIANT "
        "with .1704 codified minimums — Critical) and F-S60-003 (SOP Manual v2.24 ratios "
        "EXCEED .1704(c)(1) minimums — Met-Exceeds, Info).",
        STY['body']))
    section_b = [f for f in FINDINGS if f['id'] in ('F-S60-002', 'F-S60-003')]
    for f in section_b:
        story.extend(finding_block(f))
    story.append(PageBreak())

    # ─── 6. SECTION C — Facility Capacity ────────────────────────────────
    story.append(add_heading('6. Section C — Facility Capacity Limit', STY['h1'], level=0))
    story.append(Paragraph(
        "This section presents the detailed finding for the facility-capacity discrepancy. "
        "The SOP Manual v2.24 §2.1 cap of 9 children is incorrect per the codified rule; "
        "the correct maximum capacity is 12 per 10A NCAC 27G .1706(a).",
        STY['body']))
    section_c = [f for f in FINDINGS if f['id'] == 'F-S60-004']
    for f in section_c:
        story.extend(finding_block(f))
    story.append(PageBreak())

    # ─── 7. SECTION D — Alliance Health Tailored Plan Nomenclature ───────
    story.append(add_heading('7. Section D — Alliance Health Tailored Plan Nomenclature', STY['h1'], level=0))
    story.append(Paragraph(
        "This section presents the detailed finding for the Alliance Health Tailored Plan "
        "nomenclature update. Effective July 1, 2024, NC S.L. 2021-135 transitioned the "
        "LME/MCOs to 'Tailored Plan' status under NC Medicaid Managed Care. The SOP Manual "
        "v2.24 should consistently use 'Alliance Health Tailored Plan' as the first-reference "
        "designation in each section.",
        STY['body']))
    section_d = [f for f in FINDINGS if f['id'] == 'F-S60-005']
    for f in section_d:
        story.extend(finding_block(f))
    story.append(PageBreak())

    # ─── 8. SECTION E — WakeMed Out-of-Network ───────────────────────────
    story.append(add_heading('8. Section E — WakeMed Out-of-Network (Effective July 1, 2026)', STY['h1'], level=0))
    story.append(Paragraph(
        "This section presents the detailed finding for the WakeMed out-of-network status. "
        "Alliance Health Tailored Plan has notified NC Medicaid that the WakeMed Health &amp; "
        "Hospitals system will be OUT-OF-NETWORK effective July 1, 2026 — concurrent with "
        "the facility's planned CARF Inaugural Accreditation survey window. Any emergency "
        "psychiatric or medical admissions to WakeMed on or after July 1, 2026 would be "
        "treated as out-of-network, resulting in denied Medicaid reimbursement and "
        "continuity-of-care gaps.",
        STY['body']))
    section_e = [f for f in FINDINGS if f['id'] == 'F-S60-006']
    for f in section_e:
        story.extend(finding_block(f))
    story.append(PageBreak())

    # ─── 9. SECTION F — CARF/SOP Cross-Reference Consistency ─────────────
    story.append(add_heading('9. Section F — CARF Plans / SOP Manual Cross-Reference Consistency', STY['h1'], level=0))
    story.append(Paragraph(
        "This section presents the detailed findings for the cross-reference consistency "
        "between the CARF Plans v1.2 and the SOP Manual v2.24. The CARF Plans contain 30+ "
        "cross-references to the SOP Manual that are now inconsistent because the CARF "
        "Plans were re-calibrated to 'Staff Secure Group Home' in SOP-59 while the SOP "
        "Manual retained its .1700 Level III RTF Staff-Secure calibration. Two findings "
        "are documented: F-S60-007 (cross-reference consistency — Critical) and F-S60-008 "
        "(Plan 1 §1.4 service-array reference consistency — High).",
        STY['body']))
    section_f = [f for f in FINDINGS if f['id'] in ('F-S60-007', 'F-S60-008')]
    for f in section_f:
        story.extend(finding_block(f))
    story.append(PageBreak())

    # ─── 10. SECTION G — Policy Completeness Check ──────────────────────
    story.append(add_heading('10. Section G — Policy Completeness Check (Confirmed Compliance)', STY['h1'], level=0))
    story.append(Paragraph(
        "This section presents the policy-completeness findings confirming that the SOP "
        "Manual v2.24 and CARF Plans v1.2 comprehensively address the relevant .1700 series "
        "rules and the CARF CYS 2026 Inaugural Accreditation standards. Each finding below "
        "is informational only — no corrective action is required. The findings are "
        "documented to provide the CARF surveyor with a complete crosswalk of the policy "
        "framework at the time of the Inaugural Accreditation survey.",
        STY['body']))
    section_g = [f for f in FINDINGS if f['id'].startswith('M-S60')]
    for f in section_g:
        story.extend(finding_block(f))
    story.append(PageBreak())

    # ─── 11. SECTION H — Remediation Plan / Patch Script Summary ────────
    story.append(add_heading('11. Section H — Remediation Plan &amp; Patch Script', STY['h1'], level=0))
    story.append(Paragraph(
        "This section documents the remediation plan that will be executed immediately "
        "following this audit. The remediation is implemented via a single patch script "
        "(<b>patch_sop_v225.py</b>) that applies 17 surgical edits across 7 source files "
        "in one pass, regenerates the affected PDFs, and produces the final v2.25 SOP "
        "Manual and v1.3 CARF Plans.",
        STY['body']))

    story.append(add_heading('11.1 Patch Script Architecture', STY['h2'], level=1))
    story.append(Paragraph(
        "The patch script applies edits in three groups: <b>(Group 1) CARF Plans v1.2 → v1.3 "
        "restoration</b> — 8 patches to carf_plans_content.py restoring the .1700 Level III "
        "RTF Staff-Secure calibration; 6 patches to generate_carf_plans.py updating the "
        "About-page Service Type/Service Intensity lines and bumping Rev 1.2 → 1.3; 2 patches "
        "to carf_plans_cover.html updating the scope-pill and Rev 1.2 → 1.3; 2 patches to "
        "merge_carf_plans.py updating the Subject metadata and print message. <b>(Group 2) "
        "SOP Manual v2.24 → v2.25 corrections</b> — 1 patch to sop_content_v3.py §2.1 "
        "capacity note (9 → 12 per .1706(a)); 6 patches updating 'Alliance Health' → "
        "'Alliance Health Tailored Plan' first-reference designation in sop_content_v3.py; "
        "1 new subsection §8.X Emergency Hospital Coordination added to sop_content_v3.py "
        "with in-network hospital list (UNC Rex primary, Duke Raleigh secondary, UNC Medical "
        "tertiary, Duke University quaternary). <b>(Group 3) Version History updates</b> — "
        "new v2.25 entry appended to Version History table in sop_content_v3_part3.py with "
        "summary of all corrections applied.",
        STY['body']))

    story.append(add_heading('11.2 Patch Targets &amp; Expected File Outputs', STY['h2'], level=1))
    patch_rows = [
        [Paragraph('<b>#</b>', STY['table_header']),
         Paragraph('<b>Target File</b>', STY['table_header']),
         Paragraph('<b>Surgical Edit</b>', STY['table_header']),
         Paragraph('<b>Finding Addressed</b>', STY['table_header'])],
        [Paragraph('1', STY['table_cell_center']),
         Paragraph('carf_plans_content.py (Plan 1 §1.4)', STY['table_cell']),
         Paragraph('Restore Level III RTF Staff-Secure service array (individual therapy 2x/wk, daily group therapy, weekly family therapy, on-site psychiatric coverage, 24/7 on-call)', STY['table_cell']),
         Paragraph('F-S60-001, F-S60-008', STY['table_cell_center'])],
        [Paragraph('2-4', STY['table_cell_center']),
         Paragraph('carf_plans_content.py (Plan 3 §3.4)', STY['table_cell']),
         Paragraph('Restore .1700/.1701(b) Licensure bullet citation', STY['table_cell']),
         Paragraph('F-S60-001', STY['table_cell_center'])],
        [Paragraph('5', STY['table_cell_center']),
         Paragraph('carf_plans_content.py (Plan 5 §5.4)', STY['table_cell']),
         Paragraph('Restore Level III RTF elopement risk row language', STY['table_cell']),
         Paragraph('F-S60-001', STY['table_cell_center'])],
        [Paragraph('6', STY['table_cell_center']),
         Paragraph('carf_plans_content.py (Plan 11 §11.5)', STY['table_cell']),
         Paragraph('Restore .1704 codified staffing ratios (2 staff waking per 1-4 youth; 2 staff overnight with 1 awake per .1704(c)(1))', STY['table_cell']),
         Paragraph('F-S60-002', STY['table_cell_center'])],
        [Paragraph('7', STY['table_cell_center']),
         Paragraph('carf_plans_content.py (Plan 11 §11.6)', STY['table_cell']),
         Paragraph('Restore .1700 staff-secure physical plant features', STY['table_cell']),
         Paragraph('F-S60-001', STY['table_cell_center'])],
        [Paragraph('8', STY['table_cell_center']),
         Paragraph('carf_plans_content.py (Plan 12 §12.4)', STY['table_cell']),
         Paragraph('Restore Level III RTF Staff-Secure screening-criteria language', STY['table_cell']),
         Paragraph('F-S60-001', STY['table_cell_center'])],
        [Paragraph('9-10', STY['table_cell_center']),
         Paragraph('generate_carf_plans.py', STY['table_cell']),
         Paragraph('About-page Service Type + Service Intensity lines (Rev 1.2 → 1.3)', STY['table_cell']),
         Paragraph('F-S60-001, F-S60-007', STY['table_cell_center'])],
        [Paragraph('11-13', STY['table_cell_center']),
         Paragraph('generate_carf_plans.py (Rev 1.2 → 1.3)', STY['table_cell']),
         Paragraph('DOC_TITLE_SHORT, TOC intro, PDF subject metadata, About-page intro', STY['table_cell']),
         Paragraph('F-S60-007', STY['table_cell_center'])],
        [Paragraph('14-15', STY['table_cell_center']),
         Paragraph('carf_plans_cover.html', STY['table_cell']),
         Paragraph('scope-pill: Staff Secure Group Home → Level III RTF Staff-Secure; Rev 1.2 → 1.3', STY['table_cell']),
         Paragraph('F-S60-007', STY['table_cell_center'])],
        [Paragraph('16-17', STY['table_cell_center']),
         Paragraph('merge_carf_plans.py', STY['table_cell']),
         Paragraph('PDF Subject metadata Rev 1.3; print message Rev 1.3', STY['table_cell']),
         Paragraph('F-S60-007', STY['table_cell_center'])],
        [Paragraph('18', STY['table_cell_center']),
         Paragraph('sop_content_v3.py §2.1 capacity note', STY['table_cell']),
         Paragraph('Capacity max 9 → 12 per .1706(a)', STY['table_cell']),
         Paragraph('F-S60-004', STY['table_cell_center'])],
        [Paragraph('19-24', STY['table_cell_center']),
         Paragraph('sop_content_v3.py (Alliance Health references)', STY['table_cell']),
         Paragraph('"Alliance Health" → "Alliance Health Tailored Plan" first-reference update', STY['table_cell']),
         Paragraph('F-S60-005', STY['table_cell_center'])],
        [Paragraph('25', STY['table_cell_center']),
         Paragraph('sop_content_v3.py (new §8.X Emergency Hospital Coordination)', STY['table_cell']),
         Paragraph('Add UNC Rex primary, Duke Raleigh secondary, UNC Medical tertiary, Duke University quaternary', STY['table_cell']),
         Paragraph('F-S60-006', STY['table_cell_center'])],
        [Paragraph('26', STY['table_cell_center']),
         Paragraph('sop_content_v3_part3.py (Version History)', STY['table_cell']),
         Paragraph('New v2.25 entry documenting all corrections', STY['table_cell']),
         Paragraph('All', STY['table_cell_center'])],
    ]
    avail_w = A4[0] - 1.7 * inch
    patch_widths = [0.05 * avail_w, 0.30 * avail_w, 0.45 * avail_w, 0.20 * avail_w]
    patch_tbl = Table(patch_rows, colWidths=patch_widths, hAlign='CENTER', repeatRows=1)
    patch_tbl.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), HEADER_FILL),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 4),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('GRID', (0, 0), (-1, -1), 0.3, BORDER),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, TABLE_STRIPE]),
    ]))
    story.append(patch_tbl)
    story.append(Spacer(1, 10))

    story.append(add_heading('11.3 Expected Final Deliverables After Patch Execution', STY['h2'], level=1))
    story.append(Paragraph(
        "Upon successful execution of patch_sop_v225.py, the following updated deliverables "
        "will be regenerated: (1) <b>SOP Manual v2.25 Public Edition</b> — "
        "/home/z/my-project/download/Well_Spring_Intervention_SOP_Manual_v2.25_Public-Edition.pdf "
        "(estimated 70+ pages); (2) <b>CARF Plans v1.3</b> — "
        "/home/z/my-project/download/WSI_CARF_CYS_2026_Conformance_Plans.pdf (overwrites v1.2; "
        "estimated 49+ pages, 5.19 MB); (3) <b>This audit report PDF</b> — "
        "/home/z/my-project/download/WSI_SOP_v2.24_Operational_Audit_Report.pdf. The persistent "
        "LATEST pointer (Well_Spring_Intervention_SOP_Manual_LATEST.pdf) will be updated to "
        "point to v2.25.",
        STY['body']))

    story.append(add_heading('11.4 Verification Steps After Patch Execution', STY['h2'], level=1))
    story.append(Paragraph(
        "After patch execution, the QP shall perform the following verification steps: "
        "<b>(1)</b> Run pdf_qa.py on both regenerated PDFs to verify 13/13 checks pass; "
        "<b>(2)</b> Run pdftotext + grep on the CARF Plans v1.3 to verify 0 stale 'Staff "
        "Secure Group Home' references remain (excluding intentional contrast mentions); "
        "<b>(3)</b> Run pdftotext + grep on the SOP Manual v2.25 to verify the capacity "
        "note now reads 'twelve (12) children per 10A NCAC 27G .1706(a)'; <b>(4)</b> Run "
        "pdftotext + grep on the SOP Manual v2.25 to verify 'Alliance Health Tailored Plan' "
        "appears as the first-reference designation in §1.2, §1.2(b), §1.2(d), §1.7, §1.8, "
        "and §8; <b>(5)</b> Verify the new §8.X Emergency Hospital Coordination subsection "
        "appears in the SOP Manual v2.25 with UNC Rex Hospital listed as primary in-network "
        "destination; <b>(6)</b> Update the Version History table in Part 3 of the SOP Manual "
        "to reflect the v2.25 entry; <b>(7)</b> Distribute v2.25 SOP Manual and v1.3 CARF "
        "Plans to the Executive Director, Clinical Director, QP, and Compliance Officer for "
        "review and signature; <b>(8)</b> Following approval, post the signed documents in "
        "the compliance binder and submit the CARF Inaugural Accreditation survey application.",
        STY['body']))

    story.append(add_heading('11.5 Recommended Next Steps', STY['h2'], level=1))
    story.append(Paragraph(
        "Following successful execution of the patch script and verification of the "
        "regenerated PDFs, the following next steps are recommended: <b>(1)</b> Confirm "
        "with the NC DHSR Mental Health Licensure &amp; Certification Section (MHLC) "
        "Licensure &amp; Training Consultant that the .1700 Level III RTF Staff-Secure "
        "designation is the correct license category for the program at the first in-person "
        "meeting per §1.2(e); <b>(2)</b> Order the full 2026 CYS Standards Manual from "
        "carf.org/catalog to complete the Section 3-5 crosswalk per Plan 15; <b>(3)</b> "
        "Coordinate with the CARF resource specialist to schedule the Inaugural Accreditation "
        "survey (target window: late 2026 or early 2027, per the §1.2(a) accreditation-"
        "maintenance calendar); <b>(4)</b> Confirm with Alliance Health Tailored Plan "
        "Provider Relations that the WakeMed out-of-network status is current as of the "
        "survey date and that UNC Rex Hospital is in-network for emergency psychiatric "
        "admissions; <b>(5)</b> Following CARF accreditation, post the certificate in the "
        "compliance binder and submit a license-renewal application to NC DHSR MHLC with "
        "the accreditation certificate attached.",
        STY['body']))

    story.append(PageBreak())

    # ─── 12. Sign-off ───────────────────────────────────────────────────
    story.append(add_heading('12. Audit Sign-Off', STY['h1'], level=0))
    story.append(Paragraph(
        "This operational audit was conducted by the Z.ai compliance-assistance agent on "
        "behalf of Well Spring Intervention LLC. The findings and remediation plan documented "
        "herein are submitted for review and approval by the Executive Director, Clinical "
        "Director, Qualified Professional (QP), and Compliance Officer. Following approval, "
        "the patch script (patch_sop_v225.py) shall be executed and the regenerated "
        "deliverables (SOP Manual v2.25, CARF Plans v1.3) shall be distributed for "
        "signature.",
        STY['body']))
    story.append(Spacer(1, 30))
    signoff_rows = [
        [Paragraph('<b>Role</b>', STY['table_header']),
         Paragraph('<b>Name</b>', STY['table_header']),
         Paragraph('<b>Signature</b>', STY['table_header']),
         Paragraph('<b>Date</b>', STY['table_header'])],
        [Paragraph('Executive Director', STY['table_cell']),
         Paragraph('______________________', STY['table_cell']),
         Paragraph('______________________', STY['table_cell']),
         Paragraph('__________', STY['table_cell'])],
        [Paragraph('Clinical Director', STY['table_cell']),
         Paragraph('______________________', STY['table_cell']),
         Paragraph('______________________', STY['table_cell']),
         Paragraph('__________', STY['table_cell'])],
        [Paragraph('Qualified Professional (QP)', STY['table_cell']),
         Paragraph('______________________', STY['table_cell']),
         Paragraph('______________________', STY['table_cell']),
         Paragraph('__________', STY['table_cell'])],
        [Paragraph('Compliance Officer', STY['table_cell']),
         Paragraph('______________________', STY['table_cell']),
         Paragraph('______________________', STY['table_cell']),
         Paragraph('__________', STY['table_cell'])],
    ]
    signoff_avail = A4[0] - 1.7 * inch
    signoff_widths = [0.30 * signoff_avail, 0.28 * signoff_avail, 0.28 * signoff_avail, 0.14 * signoff_avail]
    signoff_tbl = Table(signoff_rows, colWidths=signoff_widths, hAlign='CENTER', repeatRows=1)
    signoff_tbl.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), HEADER_FILL),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 0.3, BORDER),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, TABLE_STRIPE]),
    ]))
    story.append(signoff_tbl)

    # Build the PDF
    doc.multiBuild(story, onFirstPage=header_footer, onLaterPages=header_footer)
    print(f"  Body PDF generated: {output_path}")


# ─── Main entry point ──────────────────────────────────────────────────────
if __name__ == '__main__':
    output = '/home/z/my-project/scripts/sop60_audit_body.pdf'
    build_body_pdf(output)

    # Verify file exists and report size
    if os.path.exists(output):
        size_kb = os.path.getsize(output) / 1024
        print(f"  File size: {size_kb:.1f} KB")
    else:
        print(f"  ERROR: Output file not created: {output}")
        sys.exit(1)
