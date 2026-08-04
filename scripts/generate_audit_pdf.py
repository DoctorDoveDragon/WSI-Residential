"""
generate_audit_pdf.py — Body PDF generator for the Well Spring Intervention
SOP Manual v2.22 Compliance Audit Report.

Pipeline:
  1. Build body PDF via ReportLab (TOC + 13 content sections)
  2. Merge with cover PDF (scripts/audit_cover.pdf) via pypdf
  3. Output: /home/z/my-project/download/WSI_SOP_v2.22_Compliance_Audit_Report.pdf
"""

import os
import sys
import hashlib
import subprocess
from pathlib import Path

# Make audit_findings importable
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from audit_findings import FINDINGS, summary_stats, SEVERITY_LEGEND, STATUS_LEGEND

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

# ─── Font registration ─────────────────────────────────────────────────────
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

# ─── Brand palette (Well Spring Intervention) ─────────────────────────────
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
                      'Well Spring Intervention LLC — SOP v2.22 Compliance Audit')
    canvas.drawRightString(page_w - 0.85 * inch, page_h - 0.45 * inch,
                           'Doc. WSI-AUDIT-001 · Rev. 1.0')
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
    """Return a list of flowables for one finding."""
    sev = f['severity']
    sev_color = {'Critical': SEV_CRITICAL, 'High': SEV_HIGH, 'Medium': SEV_MEDIUM,
                 'Low': SEV_LOW, 'Info': SEV_INFO}[sev]
    status_color = STATUS_COLORS.get(f['status'], TEXT_PRIMARY)

    out = []
    # Finding header
    header_text = (
        f"<b>{f['id']}</b> &nbsp;&nbsp; "
        f"<font color='{sev_color.hexval()}'>[{sev}]</font> &nbsp;&nbsp; "
        f"<font color='{status_color.hexval()}'>[{f['status']}]</font> &nbsp;&nbsp; "
        f"<b>{f['rule']}</b> — {f['rule_title']}"
    )
    out.append(Paragraph(header_text, STY['finding_meta']))
    out.append(HRFlowable(width='100%', thickness=0.5, color=BORDER,
                          spaceBefore=2, spaceAfter=6))

    # Metadata table (SOP location + strip flag)
    meta_rows = [
        [Paragraph('<b>Rule text</b>', STY['table_cell']),
         Paragraph(f['rule_text'], STY['table_cell'])],
        [Paragraph('<b>SOP location</b>', STY['table_cell']),
         Paragraph(f['sop_loc'], STY['table_cell'])],
        [Paragraph('<b>SOP quote / paraphrase</b>', STY['table_cell']),
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

    # Finding narrative
    out.append(Paragraph('<b>Finding.</b> ' + f['finding'], STY['body']))
    # Remediation
    out.append(Paragraph('<b>Remediation.</b> ' + f['remediation'], STY['body']))
    out.append(Spacer(1, 8))
    return out


# ─── Main builder ──────────────────────────────────────────────────────────
def build_body_pdf(output_path):
    doc = TocDocTemplate(
        output_path, pagesize=A4,
        leftMargin=0.85 * inch, rightMargin=0.85 * inch,
        topMargin=0.85 * inch, bottomMargin=0.85 * inch,
        title='Well Spring Intervention SOP Manual v2.22 Compliance Audit Report',
        author='Z.ai', creator='Z.ai',
        subject='Compliance audit of SOP Manual v2.22 against 10A NCAC 27G .1700 + core rules',
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
        "This report documents a rule-by-rule compliance audit of the Well Spring Intervention LLC "
        "Standard Operating Procedure &amp; Operational Manual, Revision 2.22 (August 2026 — Legislation-Free "
        "Public Edition), against 10A NCAC 27G .1700 (Residential Treatment Staff Secure for Children or "
        "Adolescents) and the cross-referenced core rules in .0104 (Staff Definitions) and .0201–.0210 "
        "(Operation and Management Rules). The audit identifies <b>%d total findings</b>: %d High severity, "
        "%d Medium severity, %d Low severity, and %d informational findings confirming compliance." % (
            stats['total_findings'],
            stats['by_severity'].get('High', 0),
            stats['by_severity'].get('Medium', 0),
            stats['by_severity'].get('Low', 0),
            stats['by_severity'].get('Info', 0),
        ),
        STY['body']))
    story.append(Paragraph(
        "Of the 56 findings, <b>%d confirm full compliance</b> (Met or Met-Exceeds), <b>%d identify partial "
        "compliance gaps</b>, <b>%d identify complete gaps</b> where the SOP does not address a rule requirement, "
        "and <b>%d identifies an internal contradiction</b> requiring resolution. The audit also catalogs "
        "<b>%d statutory or regulatory citations</b> currently present in the public edition that should be "
        "stripped and replaced with plain-language operational text per the user's legislation-stripping directive." % (
            stats['by_status'].get('Met', 0) + stats['by_status'].get('Met-Exceeds', 0),
            stats['by_status'].get('Partial', 0),
            stats['by_status'].get('Gap', 0),
            stats['by_status'].get('Contradicts', 0),
            stats['by_strip']['Y'],
        ),
        STY['body']))

    story.append(add_heading('1.1 Three High-Severity Findings', STY['h2'], level=1))
    story.append(Paragraph(
        "The audit identified three High severity findings that require remediation in v2.23 before the next "
        "DHSR MHLC licensure survey. Each is summarized below; full deep-dive analysis appears in Section F.",
        STY['body']))
    for f in stats['critical_high_findings']:
        story.append(Paragraph(
            f"<b>{f['id']} — {f['rule']} {f['rule_title']}.</b> {f['finding'][:300]}…",
            STY['body']))
    story.append(Paragraph(
        "<b>Section 1.2(h)(b) compliance flag is RESOLVED.</b> The open compliance flag raised in SOP Manual "
        "v2.22 §1.2(h)(b) regarding whether the correct NC Medicaid Clinical Coverage Policy for Level III "
        "Residential Treatment Services is CCP 8C or CCP 8D-2 is hereby resolved in favor of <b>CCP 8D-2</b>. "
        "Primary source: NC Medicaid Clinical Coverage Policy 8D-2, 'Residential Treatment Services' (Amended "
        "January 1, 2025), §1.0(c), available at https://medicaid.ncdhhs.gov/8d-2-residential-treatment-services/download?attachment. "
        "CCP 8C is 'Outpatient Behavioral Health Services Provided by Direct-Enrolled Providers' — a different "
        "benefit category that does not cover residential treatment. The SOP already correctly cites CCP 8D-2 "
        "in §1.2(g), §1.9, and §10.9, but legacy 'CCP 8C' references remain in §1.2, §2, §3, §4, §5, §6, and §10 "
        "reference lines and must be globally updated to 'CCP 8D-2' in v2.23. Full resolution analysis appears "
        "in Section D.",
        STY['body']))

    story.append(add_heading('1.2 Compliance Strengths', STY['h2'], level=1))
    story.append(Paragraph(
        "The audit confirmed that the SOP Manual v2.22 demonstrates strong compliance across many rule domains. "
        "Key strengths include: (1) §2.1 staffing ratio 2:4 minimum requires <b>both</b> overnight staff awake, "
        "exceeding .1704(c)(1)'s minimum of 'two present, one awake' — a stricter, defensible standard; "
        "(2) §5.5 Activities Program at 14 hours/week of planned group activities exceeds .0208(a) activity-suitability "
        "minimums; (3) §3.4 Discharge Summary within 7 calendar days exceeds the RMDM 30-day requirement; "
        "(4) §10.7 Electronic Signatures with 8 administrative, technical, and physical safeguards exceeds NC UETA "
        "minimum requirements; (5) §1.7 Resident Rights enumerates 15 rights with posted notice and grievance "
        "procedure, exceeding .0201(a)(18) minimums; (6) §9.7 Disaster &amp; Emergency Plan with OEM coordination "
        "exceeds .0207 minimums; (7) §1.4(b) QP Credentialing Pathways 1 and 2 align with .0104(21)(b) and (c); "
        "(8) §6.1 admission physical exam 90 days PRIOR to admission per Level III RTF staff-secure requirements; "
        "(9) §2.3 background checks (SBI + HCP Registry + DSS-CAN + MVR) exceed .0202(c) minimums; "
        "(10) §2.4 mandatory training (12 topics including in-person CPR/Heimlich, NCI/CPI restraint, BBP, "
        "trauma-informed care, population-specific) exceeds .0202(g) 4-topic minimums. Full strengths analysis "
        "appears in Section G.",
        STY['body']))

    story.append(PageBreak())

    # ─── 2. Audit Scope, Methodology & Sources ────────────────────────────
    story.append(add_heading('2. Audit Scope, Methodology &amp; Sources', STY['h1'], level=0))
    story.append(add_heading('2.1 Scope', STY['h2'], level=1))
    story.append(Paragraph(
        "This audit crosswalks the Well Spring Intervention LLC SOP Manual v2.22 against the following 10A NCAC 27G "
        "rules: <b>Section .1700 — Residential Treatment Staff Secure for Children or Adolescents</b> (rules .1701 "
        "through .1708, the operative section for this facility's Level III Staff-Secure license category); and "
        "the <b>cross-referenced core rules in .0104 (Staff Definitions) and .0201–.0210 (Operation and Management "
        "Rules)</b> that .1700 explicitly invokes or that apply to all 24-hour residential facilities.",
        STY['body']))
    story.append(Paragraph(
        "Rules excluded from this audit scope: the remainder of 10A NCAC 27G Subchapter G (4,143 lines total) "
        "including .0300 Building Code requirements (handled separately by NC OSFM and local code enforcement), "
        ".0400 Licensure Procedures, .0500 Area Authority/Program rules, .0600 Residential Child-Care rules "
        "(applicable to DSS-licensed facilities, not DHSR MHLC-licensed RTFs), .1100–.1600 (other facility types), "
        "and .1800 (Intensive Residential Treatment — a separate, more intensive license category). A future audit "
        "may extend scope to include the full Subchapter if needed.",
        STY['body']))

    story.append(add_heading('2.2 Sources Audited', STY['h2'], level=1))
    story.append(Paragraph(
        "<b>Source 1.</b> Well Spring Intervention LLC SOP &amp; Operational Manual, Doc. WSI-SOP-001, Rev. 2.22, "
        "August 2026 — Legislation-Free Public Edition. 68 pages, 4,379 text lines extracted via pdftotext. "
        "Available at /home/z/my-project/download/Well_Spring_Intervention_SOP_Manual_v2.22_Public-Edition.pdf.",
        STY['body']))
    story.append(Paragraph(
        "<b>Source 2.</b> 10A NCAC 27G Subchapter G (Mental Health, Community Facilities and Services) rule text "
        "as supplied in conversation. The relevant sections for this audit are: .0104 Staff Definitions "
        "(22 sub-definitions including AP, Paraprofessional, QP, Psychiatrist, Licensed Clinician); "
        ".0201 Governing Body Policies (18 enumerated items); .0202 Personnel Requirements; "
        ".0203 QP/AP Competencies; .0204 Paraprofessional Competencies; .0205 Assessment and Service Plan; "
        ".0206 Client Records; .0207 Emergency Plans and Supplies; .0208 Client Services; "
        ".0209 Medication Requirements (8 subsections a–h); .0210 Research Review Board (N/A for this facility); "
        ".1701 Scope; .1702 QP Requirements; .1703 AP Requirements; .1704 Minimum Staffing; "
        ".1705 Licensed Professionals; .1706 Operations; .1707 Persons Permitted; .1708 Transfer or Discharge.",
        STY['body']))

    story.append(add_heading('2.3 Methodology', STY['h2'], level=1))
    story.append(Paragraph(
        "The audit followed a four-step methodology: <b>(1) Source document identification and version control</b> — "
        "the SOP Manual v2.22 PDF was extracted via pdftotext and verified against the source script (generate_sop.py); "
        "the 10A NCAC 27G rule text was supplied verbatim in conversation. <b>(2) Rule-by-rule crosswalk</b> — each "
        "rule paragraph (e.g., .1704(c)(1)) was mapped to its corresponding SOP location via keyword search and "
        "manual review, with verbatim quotes preserved for both rule text and SOP text. <b>(3) Severity classification</b> — "
        "Critical (license-blocking, safety risk, or Medicaid fraud exposure); High (direct rule violation with "
        "regulatory or billing impact); Medium (partial compliance or documentation gap); Low (clarification or "
        "stylistic inconsistency); Info (confirmed compliance or note). <b>(4) Strip-flag annotation</b> — each finding "
        "was annotated with a strip-flag (Y/N) indicating whether it involves a statutory or regulatory citation that "
        "should be replaced with plain-language operational text in the v2.23 public edition per the user's "
        "legislation-stripping directive.",
        STY['body']))
    story.append(Paragraph(
        "All citations were verified against the supplied 10A NCAC 27G source text. The audit is a dual-pass review: "
        "findings were generated, then re-verified against the source documents. Automated keyword verification was "
        "performed via pdftotext + grep to ensure no rule subsection was missed.",
        STY['body']))

    story.append(add_heading('2.4 §1.2(h)(b) Compliance Flag Resolution', STY['h2'], level=1))
    story.append(Paragraph(
        "The open compliance flag raised in SOP Manual v2.22 §1.2(h)(b) regarding whether the correct NC Medicaid "
        "Clinical Coverage Policy for Level III Residential Treatment Services is CCP 8C or CCP 8D-2 is <b>RESOLVED "
        "in favor of CCP 8D-2</b>. Primary source: NC Medicaid Clinical Coverage Policy 8D-2, 'Residential Treatment "
        "Services' (Amended January 1, 2025), §1.0(c). CCP 8C is 'Outpatient Behavioral Health Services Provided by "
        "Direct-Enrolled Providers' — a different benefit category. All legacy 'CCP 8C' references in the SOP Manual "
        "v2.22 (in §1.2, §2, §3, §4, §5, §6, §10 reference lines) must be updated to 'CCP 8D-2' in v2.23. The §1.2(h)(b) "
        "compliance flag should be rewritten from OPEN to RESOLVED, mirroring the v2.21 resolution of §1.2(h)(a). "
        "Full resolution analysis appears in Section D.",
        STY['body']))

    story.append(PageBreak())

    # ─── 3. Findings Summary Matrix ──────────────────────────────────────
    story.append(add_heading('3. Findings Summary Matrix', STY['h1'], level=0))
    story.append(Paragraph(
        "The table below summarizes all %d findings. Detailed analysis for each finding appears in Sections A–D "
        "and the deep-dive analysis for High and Critical findings appears in Section F." % stats['total_findings'],
        STY['body']))

    # Build summary table
    avail_w = A4[0] - 1.7 * inch
    col_ratios = [0.07, 0.10, 0.10, 0.08, 0.08, 0.07, 0.50]
    col_widths = [r * avail_w for r in col_ratios]

    header_row = [
        Paragraph('<b>ID</b>', STY['table_header']),
        Paragraph('<b>Rule</b>', STY['table_header']),
        Paragraph('<b>Status</b>', STY['table_header']),
        Paragraph('<b>Severity</b>', STY['table_header']),
        Paragraph('<b>Strip</b>', STY['table_header']),
        Paragraph('<b>SOP §</b>', STY['table_header']),
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
        f"<b>Legend.</b> Severity: Critical = license-blocking/safety/fraud; High = direct rule violation; "
        f"Medium = partial/gap; Low = clarification; Info = confirmed compliance. "
        f"Status: Met = full compliance; Met-Exceeds = stricter than rule (defensible); "
        f"Partial = missing elements; Gap = not addressed; Contradicts = inconsistent with rule; N/A = does not apply. "
        f"Strip flag: Y = statutory citation to remove from public edition; N = no citation to strip.",
        STY['meta']))
    story.append(PageBreak())

    # ─── 4. SECTION A — .1700 Findings (detailed) ─────────────────────────
    story.append(add_heading('4. Section A — .1700 Residential Treatment Staff Secure Findings', STY['h1'], level=0))
    story.append(Paragraph(
        "This section presents detailed findings for each rule subsection in 10A NCAC 27G .1700 (Residential "
        "Treatment Staff Secure for Children or Adolescents), the operative licensure section for this facility. "
        "The .1700 section contains 8 rules (.1701 through .1708) covering scope, qualified professional requirements, "
        "associate professional requirements, minimum staffing, licensed professional consultation, operations, "
        "persons permitted, and transfer/discharge. Findings are presented in rule-subsection order.",
        STY['body']))

    s1700_findings = [f for f in FINDINGS if f['rule'].startswith('.17')]
    for f in s1700_findings:
        story.extend(finding_block(f))

    story.append(PageBreak())

    # ─── 5. SECTION B — .0104 Findings ───────────────────────────────────
    story.append(add_heading('5. Section B — .0104 Staff Definitions Crosswalk', STY['h1'], level=0))
    story.append(Paragraph(
        "Rule .1700 cross-references .0104 (Staff Definitions) for the QP, AP, and Paraprofessional definitions. "
        "This section presents the crosswalk for each .0104 definition cited in .1700, verifying that the SOP "
        "Manual v2.22 correctly implements the substantive credentialing requirements. A notable finding is that "
        ".1702(a) cross-references .0104(18), but .0104(18) is the 'Psychiatrist' definition — the substantive QP "
        "definition is at .0104(21). This appears to be a typographical error in .1702(a) itself; the SOP correctly "
        "follows the substantive QP definition per .0104(21).",
        STY['body']))

    s0104_findings = [f for f in FINDINGS if f['rule'].startswith('.0104')]
    for f in s0104_findings:
        story.extend(finding_block(f))

    story.append(PageBreak())

    # ─── 6. SECTION C — .0201-.0210 Findings ─────────────────────────────
    story.append(add_heading('6. Section C — .0201–.0210 Core Rules Findings', STY['h1'], level=0))
    story.append(Paragraph(
        "This section presents detailed findings for the cross-referenced core rules in .0201 through .0210 "
        "(Operation and Management Rules). These rules apply to all 24-hour residential facilities and are "
        "incorporated by reference into the .1700 license category. Findings are presented in rule order.",
        STY['body']))

    s02xx_findings = [f for f in FINDINGS if f['rule'].startswith('.02')]
    for f in s02xx_findings:
        story.extend(finding_block(f))

    story.append(PageBreak())

    # ─── 7. SECTION D — Open Compliance Flag Resolution ─────────────────
    story.append(add_heading('7. Section D — Open Compliance Flag Resolution: §1.2(h)(b) CCP 8C vs CCP 8D-2', STY['h1'], level=0))
    story.append(Paragraph(
        "SOP Manual v2.22 §1.2(h)(b) flags an open compliance question regarding whether the correct NC Medicaid "
        "Clinical Coverage Policy for Level III Residential Treatment Services is CCP 8C or CCP 8D-2. This section "
        "resolves the flag.",
        STY['body']))

    story.append(add_heading('7.1 The Question', STY['h2'], level=1))
    story.append(Paragraph(
        "The SOP Manual v2.22 cites 'NC Medicaid CCP 8C' as the Medicaid coverage authority for residential "
        "treatment services in legacy reference lines at the top of §1.2, §2, §3, §4, §5, §6, and §10. However, "
        "§1.2(g), §1.9, and §10.9 cite 'CCP 8D-2' as the operative authority. §1.2(h)(b) acknowledges this "
        "inconsistency and flags it as an open compliance question to be resolved in v2.22 or v2.23 following "
        "Alliance Health / NCTracks enrollment confirmation.",
        STY['body']))

    story.append(add_heading('7.2 The Resolution', STY['h2'], level=1))
    story.append(Paragraph(
        "<b>The correct NC Medicaid Clinical Coverage Policy for Level III Residential Treatment Services is "
        "CCP 8D-2.</b> Primary source: NC Medicaid Clinical Coverage Policy 8D-2, 'Residential Treatment Services' "
        "(Amended January 1, 2025), §1.0(c), available at https://medicaid.ncdhhs.gov/8d-2-residential-treatment-services/download?attachment. "
        "The policy explicitly defines Residential Treatment Level III Service (Residential Treatment High) as "
        "'a highly structured and supervised environment in a program setting only, excluding room and board' — "
        "the language the SOP Manual v2.22 quotes verbatim in §1.2(g)(i).",
        STY['body']))
    story.append(Paragraph(
        "<b>CCP 8C is the wrong policy.</b> CCP 8C is titled 'Outpatient Behavioral Health Services Provided by "
        "Direct-Enrolled Providers' and covers outpatient services only — it does not cover residential treatment. "
        "The NC DHHS Division of Health Benefits (NCDHB) clinical coverage policy library confirms this distinction. "
        "Other relevant policies in the 8D series: CCP 8D-1 covers Psychiatric Residential Treatment Facilities "
        "(PRTFs — a separate inpatient benefit); CCP 8D-3, 8D-4, and 8D-5 cover adult ASAM-aligned SUD residential "
        "services. None of these apply to a Level III RTS for children/adolescents.",
        STY['body']))

    story.append(add_heading('7.3 Required Corrective Action', STY['h2'], level=1))
    story.append(Paragraph(
        "The QP shall execute the following corrective actions in v2.23:",
        STY['body']))
    story.append(Paragraph(
        "<b>(1) Global find-and-replace.</b> Update all legacy 'CCP 8C' references in §1.2, §2, §3, §4, §5, §6, "
        "and §10 reference lines to 'CCP 8D-2'. Verify via grep that no 'CCP 8C' references remain in the body "
        "of the Manual.",
        STY['body']))
    story.append(Paragraph(
        "<b>(2) Rewrite §1.2(h)(b) from OPEN to RESOLVED.</b> Mirror the v2.21 resolution format of §1.2(h)(a): "
        "state the resolution (CCP 8D-2 is correct), cite the primary source (NC Medicaid CCP 8D-2, Amended "
        "January 1, 2025, §1.0(c)), note that all legacy 'CCP 8C' references have been updated to 'CCP 8D-2' in "
        "v2.23, and confirm no further action is required.",
        STY['body']))
    story.append(Paragraph(
        "<b>(3) Update §1.2(h)(c) summary.</b> Update the §1.2(h)(c) 'No operational impact' summary to reflect "
        "that both (a) and (b) are now resolved. Remove the statement that '§1.2(g), §1.9, and §10.9 continue to "
        "control in the event of any inconsistency with the legacy CCP 8C reference lines' — there will be no "
        "legacy 'CCP 8C' reference lines after v2.23.",
        STY['body']))
    story.append(Paragraph(
        "<b>(4) Update Version History.</b> Add a v2.23 entry to the Version History table in Part 3 documenting "
        "the CCP 8C → CCP 8D-2 resolution and any other v2.23 changes (e.g., new §4.6 Licensed Professional "
        "Consultation, new §6.3(a) Psychotropic Drug Regimen Review, etc.).",
        STY['body']))

    story.append(PageBreak())

    # ─── 8. SECTION E — Legislation-Stripping Recommendations ───────────
    story.append(add_heading('8. Section E — Legislation-Stripping Recommendations', STY['h1'], level=0))
    story.append(Paragraph(
        "Per the user's directive, the SOP Manual v2.22 Public Edition should be stripped of statutory and "
        "regulatory citations, with plain-language operational replacements. The companion compliance master "
        "copy (Doc. WSI-SOP-001-LEG, Rev. 2.21) retains all statutory and regulatory citations for QA and audit "
        "reference. This section catalogs the %d findings that carry a strip-flag, organized by SOP section, "
        "with the specific text to strip and the recommended plain-language replacement." % stats['by_strip']['Y'],
        STY['body']))

    # Group strip-flag findings by SOP section prefix
    strip_findings = [f for f in FINDINGS if f['strip_flag'] == 'Y']

    story.append(add_heading('8.1 Strip Recommendations by SOP Section', STY['h2'], level=1))
    story.append(Paragraph(
        "The table below lists each strip-flag finding with its rule citation, the SOP location, and the strip "
        "recommendation. The QP should execute these strip-and-replace edits in v2.23.",
        STY['body']))

    # Build strip table
    strip_header = [
        Paragraph('<b>ID</b>', STY['table_header']),
        Paragraph('<b>Rule</b>', STY['table_header']),
        Paragraph('<b>SOP §</b>', STY['table_header']),
        Paragraph('<b>Strip &amp; Replace Recommendation</b>', STY['table_header']),
    ]
    strip_data = [strip_header]
    for f in strip_findings:
        sop_short = f['sop_loc'].split(';')[0].strip()[:50]
        strip_data.append([
            Paragraph(f"<b>{f['id']}</b>", STY['table_cell_center']),
            Paragraph(f['rule'], STY['table_cell_center']),
            Paragraph(sop_short, STY['table_cell']),
            Paragraph(f['strip_note'], STY['table_cell']),
        ])
    strip_avail = A4[0] - 1.7 * inch
    strip_widths = [0.07 * strip_avail, 0.13 * strip_avail, 0.20 * strip_avail, 0.60 * strip_avail]
    strip_tbl = Table(strip_data, colWidths=strip_widths, hAlign='CENTER', repeatRows=1)
    strip_tbl.setStyle(TableStyle([
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
    story.append(strip_tbl)

    story.append(add_heading('8.2 Strip Replacement Principles', STY['h2'], level=1))
    story.append(Paragraph(
        "The following plain-language replacement principles should be applied consistently across the SOP Manual "
        "v2.23 public edition:",
        STY['body']))
    principles = [
        ('NC DHSR / NC DHSR MHLC', 'the state licensing authority'),
        ('NC DHHS / NCDHHS', 'the state health and human services authority'),
        ('Alliance Health', 'the regional managed care organization'),
        ('LME/MCO', 'the regional managed care organization'),
        ('10A NCAC 27G .1700', 'the Level III Staff-Secure operating standards'),
        ('10A NCAC 27G .0104', 'the staff-definitions rule'),
        ('10A NCAC 27G .0201–.0210', 'the operation and management rules'),
        ('NC Medicaid CCP 8D-2', 'the Medicaid residential treatment benefit policy'),
        ('NC Medicaid CCP 8C', 'REMOVE — replace with CCP 8D-2 per Section D resolution'),
        ('NC Medicaid CCP 8D-1 (PRTF)', 'the federal inpatient psychiatric residential treatment benefit'),
        ('NC Medicaid Clinical Coverage Policy', 'the state Medicaid coverage policy'),
        ('RMDM', 'the state records-management and documentation manual'),
        ('HIPAA', 'the federal health-privacy law'),
        ('42 CFR Part 2', 'the federal substance-use-disorder records confidentiality law'),
        ('42 CFR 2.22', 'the federal SUD records summary'),
        ('NC UETA (Chapter 66, Article 40)', 'the state electronic-transactions law'),
        ('E-SIGN Act (15 U.S.C. § 7001 et seq.)', 'the federal electronic-signatures law'),
        ('42 CFR 401.305', 'the federal Medicaid overpayment-recoupment rule'),
        ('29 CFR 1910.1030', 'the federal bloodborne-pathogen standard'),
        ('G.S. 122C / G.S. 131E / G.S. 90', 'the applicable state statute'),
        ('IRIS', 'the state incident-reporting system'),
        ('Rule 108', 'the state incident-reporting rule'),
        ('DSS Child Abuse and Neglect Registry', 'the state child-abuse registry'),
        ('Health Care Personnel Registry', 'the state health-care personnel registry'),
        ('NC SBI fingerprint criminal background check', 'the state criminal background check'),
        ('NPI / NCTracks / NPPES / PPM', 'the national provider identifier / the state Medicaid claims system / the provider permission matrix'),
        ('CON (Certificate of Need) under G.S. 131E Art. 9', 'the state certificate-of-need determination'),
        ('McKinney-Vento / LEA / IEP / EC / BIP', 'the federal homeless-youth education law / the local school district / the individualized education program / the exceptional-children program / the behavioral intervention plan'),
        ('USDA', 'the federal nutrition guidelines'),
        ('CDC / OSHA', 'the applicable federal health and safety guidelines'),
        ('COA / TJC / CARF / CQL', 'a recognized national accrediting body'),
        ('Title IV-E', 'the federal foster-care maintenance program'),
    ]
    p_data = [[Paragraph('<b>Strip (statutory / regulatory citation)</b>', STY['table_header']),
               Paragraph('<b>Replace with (plain-language operational text)</b>', STY['table_header'])]]
    for s, r in principles:
        p_data.append([Paragraph(s, STY['table_cell']), Paragraph(r, STY['table_cell'])])
    p_widths = [0.45 * strip_avail, 0.55 * strip_avail]
    p_tbl = Table(p_data, colWidths=p_widths, hAlign='CENTER', repeatRows=1)
    p_tbl.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), HEADER_FILL),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('GRID', (0, 0), (-1, -1), 0.3, BORDER),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, TABLE_STRIPE]),
    ]))
    story.append(p_tbl)

    story.append(PageBreak())

    # ─── 9. SECTION F — Critical & High Findings Deep Dive ───────────────
    story.append(add_heading('9. Section F — Critical &amp; High Findings Deep Dive', STY['h1'], level=0))
    story.append(Paragraph(
        "This section presents deep-dive analysis for each Critical and High severity finding identified in the "
        "audit. The audit identified 3 High severity findings (no Critical findings). Each deep-dive includes the "
        "rule citation and verbatim text, the SOP current state, why this is a High severity finding, the detailed "
        "remediation plan with specific edits and target revision, and the strip-flag impact.",
        STY['body']))

    for f in stats['critical_high_findings']:
        story.extend(finding_block(f))
        # Extra context for deep dive
        story.append(Paragraph(
            f"<b>Why this is {f['severity']} severity.</b> " +
            ("This is a direct licensure rule — a DHSR MHLC surveyor will check whether the facility can document "
             "compliance at the next on-site survey. Failure to remediate before the next survey is a "
             "license-blocking risk." if f['id'] in ('F-001', 'F-002') else
             "This is an internal inconsistency that creates audit risk: a surveyor or Medicaid auditor reviewing "
             "the Manual will encounter contradictory citations. The inconsistency must be resolved in v2.23."),
            STY['body']))
        story.append(Spacer(1, 12))

    story.append(PageBreak())

    # ─── 10. SECTION G — Compliance Strengths ────────────────────────────
    story.append(add_heading('10. Section G — Compliance Strengths', STY['h1'], level=0))
    story.append(Paragraph(
        "To provide balanced audit perspective, this section acknowledges what the SOP Manual v2.22 does well. "
        "The Manual demonstrates strong compliance across many rule domains, with several areas where the SOP "
        "imposes stricter standards than the rule minimums — these stricter standards are defensible and "
        "operationally justified for a Level III Staff-Secure RTF serving youth with severe emotional disturbance.",
        STY['body']))

    strengths = [
        ("§2.1 Staffing Ratio — 2:4 minimum, both overnight staff awake",
         "Rule .1704(c)(1) requires only 'two direct care staff present, one awake' for 1-4 youth during sleep hours. "
         "The SOP requires BOTH overnight staff awake, providing redundancy and faster emergency response. "
         "This stricter standard is documented on Form 1 (Shift Change &amp; Awake Night Watch Log) via 15-minute "
         "visual room checks throughout the overnight shift."),
        ("§5.5 Activities Program — 14 hours/week planned group activities",
         "Rule .0208(a) requires only that activities be 'suitable for the ages, interests, and treatment needs' "
         "of clients. The SOP requires 14 hours/week minimum, distributed across 4 activity categories (physical, "
         "creative, socialization/life-skills, community integration), with a weekly published calendar, youth "
         "participation in planning, and ADA/Section 504 inclusivity."),
        ("§3.4 Discharge Summary — 7 calendar days",
         "The RMDM allows 30 days for Discharge Summary completion. The SOP requires 7 calendar days, "
         "demonstrating strong documentation discipline and reducing audit risk."),
        ("§10.7 Electronic Signatures — 8 safeguard controls",
         "NC UETA and the federal E-SIGN Act establish minimum requirements for electronic signatures. The SOP "
         "imposes 8 specific administrative, technical, and physical safeguards (unique credentials, MFA, "
         "session timeout, TLS/encryption, immutable audit trails, RBAC, immediate revocation, annual review), "
         "plus a Documentation Continuity Event procedure for system unavailability."),
        ("§1.7 Resident Rights — 15 enumerated rights with posted notice and grievance procedure",
         "Rule .0201(a)(18) requires only a 'client grievance policy including procedures for review and disposition.' "
         "The SOP enumerates 15 specific resident rights, requires posted notice in English and Spanish in 14-point "
         "font in common areas and each youth bedroom, and establishes a 1-business-day acknowledgement, "
         "5-business-day investigation, and 15-business-day written response grievance procedure."),
        ("§9.7 Disaster &amp; Emergency Plan with OEM coordination",
         "Rule .0207 requires a written fire plan and disaster plan. The SOP addresses 7 emergency scenarios "
         "(fire, tornado, hurricane, power outage, system failure, lockdown, emergency relocation), requires "
         "coordination with the local Office of Emergency Management, identifies primary and secondary host "
         "facilities for emergency relocation, and conducts monthly fire drills plus quarterly tornado drills."),
        ("§1.4(b) QP Credentialing Pathways 1 &amp; 2",
         "The SOP correctly implements .0104(21)(b) (master's + 1 year supervised MH/DD/SA) and .0104(21)(c) "
         "(bachelor's + 2 years supervised MH/DD/SA) as two acceptable QP pathways, with common requirements "
         "for NC-DHHS QP training, lapse/sanction reporting, personnel-file verification, and annual re-verification."),
        ("§6.1 Admission Physical Exam — 90 days PRIOR",
         "Rule .1700 requires the pre-admission physical exam timing per the Level III RTF staff-secure operating "
         "standards. The SOP correctly requires the exam within 90 days PRIOR to admission (not 30 days after, "
         "as prior revisions incorrectly stated), with a 7-day post-admission contingency only if the pre-admission "
         "exam is older than 90 days."),
        ("§2.3 Background Checks — 4-tier",
         "Rule .0202(c) requires only that applicants disclose criminal convictions. The SOP requires 4 separate "
         "background checks: NC SBI fingerprint criminal, Health Care Personnel Registry, DSS Child Abuse and "
         "Neglect Registry (every state of residence in prior 5 years), and Motor Vehicle Record for staff who "
         "transport residents. All 4 must be complete before unsupervised youth contact."),
        ("§2.4 Mandatory Training — 12 topics",
         "Rule .0202(g) requires 4 training topics (general org orientation, client rights/confidentiality, "
         "mh/dd/sa population needs, infectious diseases/BBP). The SOP requires 12 topics including in-person-only "
         "CPR with Heimlich/First Aid, NCI/CPI restraint and de-escalation (in-person for physical module), "
         "Medication Administration (RN-delegated, in-person), Bloodborne Pathogens, Trauma-Informed Care, "
         "Rule 108 incident reporting, Population-Specific (SED/co-occurring/trauma), Adolescent development/"
         "C-SSRS/PCP, Alternatives to Restrictive Interventions, Seclusion/Physical Restraint/Isolation Time-Out "
         "(in-person), Client Rights &amp; Confidentiality, and General Organization Orientation."),
    ]
    for title, body in strengths:
        story.append(Paragraph(f"<b>{title}.</b> {body}", STY['body']))

    story.append(PageBreak())

    # ─── 11. Recommended Revision Roadmap ────────────────────────────────
    story.append(add_heading('11. Recommended Revision Roadmap (v2.23)', STY['h1'], level=0))
    story.append(Paragraph(
        "This section recommends a sequence of revisions for v2.23 to close all High and Medium severity findings. "
        "The roadmap prioritizes High severity findings first (license-blocking risk), then Medium severity "
        "findings by SOP section. Target completion: v2.23 by September 2026; v2.24 (post-Alliance Health/NCTracks "
        "enrollment confirmation) to formalize any remaining open items.",
        STY['body']))

    roadmap = [
        ("1. Add §4.6 Licensed Professional Face-to-Face Clinical Consultation [closes F-001]",
         "Commit to minimum 4 hours/week of on-site consultation by a licensed professional (LCSW, LPC, LMFT, "
         "Licensed Psychologist, or psychiatrist per .0104(14)). Enumerate the 3 .1705(b) consultation activities: "
         "clinical supervision of the QP, individual/group/family therapy, and involvement in treatment plans/program "
         "issues. Add a Licensed Professional Consultation Log (proposed Form 10) documenting date, duration, "
         "licensed-professional name/credential, activities performed, and youth seen. Designate the Clinical Director "
         "as default licensed professional with authority to delegate."),
        ("2. Add §6.3(a) Psychotropic Medication Drug Regimen Review [closes F-002]",
         "Require a review of each youth's psychotropic medication regimen at least every 6 months by the facility "
         "psychiatrist or a consulting pharmacist per .0209(f). Document findings and corrective action in the youth's "
         "clinical record. Inform the youth's physician of any findings indicating medical intervention. Add a "
         "Psychotropic Drug Regimen Review Tracking Log (proposed Form 11) showing for each youth on psychotropic "
         "meds: review date, reviewer name/credential, next review due date."),
        ("3. Global find/replace 'CCP 8C' → 'CCP 8D-2' in all legacy reference lines [closes F-003]",
         "Update §1.2, §2, §3, §4, §5, §6, and §10 reference lines. Rewrite §1.2(h)(b) from OPEN to RESOLVED "
         "mirroring the v2.21 resolution format of §1.2(h)(a). Update §1.2(h)(c) summary to reflect both (a) and "
         "(b) now resolved. Add v2.23 Version History entry."),
        ("4. Add §6.3(b) Medication Disposal Documentation [closes F-013]",
         "Require documentation of non-controlled-substance medication disposal: client name, medication name, "
         "strength, quantity, disposal date/method, disposer signature, witness signature. Address controlled-substance "
         "disposal per state Controlled Substances Act. Address post-discharge medication holding (max 30 calendar days "
         "if return expected)."),
        ("5. Add §6.3(c) Medication Receipt Verification — Tamper-Resistant Packaging &amp; Label Contents [closes F-012]",
         "RN or designated DCP verifies upon receipt of each medication that: (1) packaging is tamper-resistant; "
         "(2) label contains all 6 .0209(b)(3) items (client name, prescriber name, dispensing date, directions, "
         "drug name/strength/quantity/expiration, pharmacy name/address/phone). Discrepancies returned to pharmacy "
         "for correction before administration."),
        ("6. Add §6.3(d) Medication Education for Clients on Psychotropic Meds [closes F-014]",
         "Each youth started or maintained on a psychotropic medication receives oral or written education by the "
         "psychiatrist, RN, or designee per .0209(g). When youth's ability to understand is questionable, guardian "
         "receives education. Document in clinical record: offered/provided/declined, manner provided, recipient."),
        ("7. Expand §6.3 Medication Storage [closes F-014 storage gap]",
         "Explicitly address all 5 .0209(e)(1) storage requirements: (A) locked cabinet 59-86°F in clean/lighted/"
         "ventilated room; (B) refrigerated 36-46°F with separate locked compartment if fridge shared with food; "
         "(C) separately per client; (D) separately for external and internal use; (E) secure self-medication if "
         "physician-approved. Update Form 5 to track medication-fridge temperature if applicable."),
        ("8. Add §2.2(a) AP Individualized Supervision Plan [closes F-006]",
         "Each AP has an individualized supervision plan initiated at hiring and reviewed annually per .0203(f). "
         "Document supervision frequency, format, focus areas, and supervisor's QP credentials. Expand §2.2 AP "
         "definition to enumerate all 4 .0104(1) pathways."),
        ("9. Add §2.2(b) Paraprofessional Individualized Supervision Plan [closes F-007]",
         "Each paraprofessional DCP has an individualized supervision plan initiated at hiring and reviewed annually "
         "per .0204(f). Mirror the AP supervision plan structure."),
        ("10. Add §3.4(a) Emergency Transfer/Discharge — 5-Business-Day Service Planning Meeting [closes F-008]",
         "Emergency transfer or discharge triggers a service-planning meeting with the Child and Family Team and "
         "involved agencies (DSS, LEA, LME/MCO, criminal justice if applicable) within 5 business days per .1708(e). "
         "Document attendees, agenda, and decisions in the youth's clinical record."),
        ("11. Add §3.6 18th-Birthday Continuation Policy [closes F-009]",
         "Adolescent who turns 18 while in active treatment may remain for 6 months or until end of state fiscal year "
         "(June 30), whichever is longer, per .1706(e) — provided youth continues to meet medical-necessity criteria "
         "and LME/MCO authorizes continued services. Address consent transfer (youth becomes own LRP at 18 unless "
         "guardianship court-extended) and Medicaid eligibility redetermination."),
        ("12. Add §3.4(b) Advance Written Notification for Non-Emergency Discharge/Transfer [closes M-025]",
         "Non-emergency discharge or transfer requires written notification to the treatment team (including LRP, "
         "LME/MCO, DSS, LEA, criminal justice if applicable) at least 7 calendar days in advance per .1708(b)."),
        ("13. Add §3.4(c) Pre-Discharge CFT Service Planning Meeting [closes M-026]",
         "Pre-discharge service-planning meeting with the Child and Family Team and involved agencies per .1708(c)."),
        ("14. Update §2.2 Age-18, Literacy, Criminal-Conviction Disclosure [closes M-033 partial]",
         "Add explicit statements: (1) all staff at least 18 years of age; (2) able to read, write, understand, "
         "and follow directions; (3) applicants disclose any criminal conviction at application per .0202(b)(1)-(2) and (c)."),
        ("15. Update §1.8 Governing Body Minutes Permanently Maintained [closes M-032]",
         "Add explicit statement that governing-body meeting minutes are permanently maintained (paper or electronic) "
         "per .0201(b)."),
        ("16. Add §1.X Client Fee Assessment / Lab Test Authorization / Volunteer Services policies [closes M-031 partial]",
         "Add explicit policies for .0201(a)(11) client fee assessment and collection, .0201(a)(13) lab test "
         "authorization and follow-up, and .0201(a)(15) volunteer services including supervision and confidentiality."),
        ("17. Update §1.4(b) QP 2-Year Direct Client Care Experience [closes M-007 partial]",
         "Add explicit statement that the designated facility QP also meets .1702(a)'s 2-year direct client care "
         "experience requirement (in addition to the .0104(21) pathway)."),
        ("18. Update Protocol 19 &amp; Form 5 — Quarterly Drills Per Shift [closes M-038]",
         "Explicitly require quarterly fire AND tornado drills for EACH shift (day, evening, overnight) per .0207(c), "
         "not just monthly drills that may all occur on the day shift."),
        ("19. Execute Legislation-Stripping per Section E [closes all strip-flag findings]",
         "Apply the 31 plain-language replacement principles from Section 8.2 across the SOP Manual v2.23 public "
         "edition. Retain the legislated compliance master (Doc. WSI-SOP-001-LEG, Rev. 2.21) for QA and audit reference."),
    ]
    for title, body in roadmap:
        story.append(Paragraph(f"<b>{title}.</b> {body}", STY['body']))

    story.append(PageBreak())

    # ─── 12. Appendix A — Full Rule Text Quoted ──────────────────────────
    story.append(add_heading('12. Appendix A — Full Rule Text Quoted', STY['h1'], level=0))
    story.append(Paragraph(
        "This appendix reproduces the verbatim text of 10A NCAC 27G .1701 through .1708, plus .0104(1), .0104(17), "
        ".0104(18), and .0104(21), plus .0201 through .0209, as the authoritative source for this audit. History "
        "Notes are included for each rule. The full 10A NCAC 27G Subchapter G text is available at "
        "http://reports.oah.state.nc.us/ncac/title%2010a%20-%20health%20and%20human%20services/chapter%2027%20-%20mental%20health,%20community%20facilities%20and%20services/subchapter%20g/subchapter%20g%20rules.pdf.",
        STY['body']))

    # Embed key rule text excerpts (the .1700 section)
    rule_excerpts = [
        ('10A NCAC 27G .1701 SCOPE',
         '(a) A residential treatment staff secure facility for children or adolescents is one that is a free-standing '
         'residential facility that provides intensive, active therapeutic treatment and interventions within a system '
         'of care approach. It shall not be the primary residence of an individual who is not a client of the facility. '
         '(b) Staff secure means staff are required to be awake during client sleep hours and supervision shall be '
         'continuous as set forth in Rule .1704 of this Section. (c) The population served shall be children or '
         'adolescents who have a primary diagnosis of mental illness, emotional disturbance or substance-related '
         'disorders; and may also have co-occurring disorders including developmental disabilities. These children or '
         'adolescents shall not meet criteria for inpatient psychiatric services. (d) The children or adolescents served '
         'shall require: (1) removal from home to a community-based residential setting in order to facilitate treatment; '
         'and (2) treatment in a staff secure setting. (e) Services shall be designed to: (1) include individualized '
         'supervision and structure of daily living; (2) minimize the occurrence of behaviors related to functional '
         'deficits; (3) ensure safety and deescalate out of control behaviors including frequent crisis management with '
         'or without physical restraint; (4) assist the child or adolescent in the acquisition of adaptive functioning '
         'in self-control, communication, social and recreational skills; and (5) support the child or adolescent in '
         'gaining the skills needed to step-down to a less intensive treatment setting. (f) The residential treatment '
         'staff secure facility shall coordinate with other individuals and agencies within the child or adolescent\'s '
         'system of care. Authority G.S. 122C-26; 143B-147; Eff. April 3, 2006.'),
        ('10A NCAC 27G .1702 REQUIREMENTS OF QUALIFIED PROFESSIONALS',
         '(a) Each facility shall utilize at least one direct care staff who meets the requirements of a qualified '
         'professional as set forth in 10A NCAC 27G .0104(18). In addition, this qualified professional shall have two '
         'years of direct client care experience. (b) For each facility of five or less beds: (1) the qualified '
         'professional specified in Paragraph (a) of this Rule shall perform clinical and administrative responsibilities '
         'a minimum of 10 hours each week; and (2) 70% of the time shall occur when children or adolescents are awake '
         'and present in the facility. (c) For each facility of six or more beds: (1) the qualified professional '
         'specified in Paragraph (a) of this Rule shall perform clinical and administrative responsibilities a minimum '
         'of 32 hours each week; and (2) 70% of the time shall occur when children or adolescents are awake and present '
         'in the facility. (d) The governing body responsible for each facility shall develop and implement written '
         'policies that specify the clinical and administrative responsibilities of its qualified professional(s). At a '
         'minimum these policies shall include: (1) supervision of its associate professional(s) as set forth in Rule '
         '.1703 of this Section; (2) oversight of emergencies; (3) provision of direct psychoeducational services to '
         'children or adolescents; (4) participation in treatment planning meetings; (5) coordination of each child or '
         'adolescent\'s treatment plan; and (6) provision of basic case management functions. Eff. April 3, 2006.'),
        ('10A NCAC 27G .1703 REQUIREMENTS FOR ASSOCIATE PROFESSIONALS',
         '(a) In addition to the qualified professional specified in Rule .1702 of this Section, each facility shall '
         'have at least one full-time direct care staff who meets or exceeds the requirements of an associate '
         'professional as set forth in 10A NCAC 27G .0104(1). (b) The governing body responsible for each facility '
         'shall develop and implement written policies that specify the responsibilities of its associate professional(s). '
         'At a minimum these policies shall address the following: (1) management of the day to day operations of the '
         'facility; (2) supervision of paraprofessionals regarding responsibilities related to the implementation of '
         'each child or adolescent\'s treatment plan; and (3) participation in service planning meetings. Eff. April 3, 2006.'),
        ('10A NCAC 27G .1704 MINIMUM STAFFING REQUIREMENTS',
         '(a) A qualified professional shall be available by telephone or page. A direct care staff shall be able to '
         'reach the facility within 30 minutes at all times. (b) The minimum number of direct care staff required when '
         'children or adolescents are present and awake is as follows: (1) two direct care staff shall be present for '
         'one, two, three or four children or adolescents; (2) three direct care staff shall be present for five, six, '
         'seven or eight children or adolescents; and (3) four direct care staff shall be present for nine, ten, eleven '
         'or twelve children or adolescents. (c) The minimum number of direct care staff during child or adolescent '
         'sleep hours is as follows: (1) two direct care staff shall be present and one shall be awake for one through '
         'four children or adolescents; (2) two direct care staff shall be present and both shall be awake for five '
         'through eight children or adolescents; and (3) three direct care staff shall be present of which two shall be '
         'awake and the third may be asleep for nine, ten, eleven or twelve children or adolescents. (d) In addition to '
         'the minimum number of direct care staff set forth in Paragraphs (a)-(c) of this Rule, more direct care staff '
         'shall be required in the facility based on the child or adolescent\'s individual needs as specified in the '
         'treatment plan. (e) Each facility shall be responsible for ensuring supervision of children or adolescents '
         'when they are away from the facility in accordance with the child or adolescent\'s individual strengths and '
         'needs as specified in the treatment plan. Eff. April 3, 2006.'),
        ('10A NCAC 27G .1705 REQUIREMENTS OF LICENSED PROFESSIONALS',
         '(a) Face to face clinical consultation shall be provided in each facility at least four hours a week by a '
         'licensed professional. For purposes of this Rule, licensed professional means an individual who holds a '
         'license or provisional license issued by the governing board regulating a human service profession in the '
         'State of North Carolina. For substance-related disorders this shall include a licensed Clinical Addiction '
         'Specialist or a certified Clinical Supervisor. (b) The consultation specified in Paragraph (a) of this Rule '
         'shall include: (1) clinical supervision of the qualified professional specified in Rule .1702 of this Section; '
         '(2) individual, group or family therapy services; or (3) involvement in child or adolescent specific treatment '
         'plans or overall program issues. Eff. April 3, 2006.'),
        ('10A NCAC 27G .1706 OPERATIONS',
         '(a) Each facility shall serve no more than a total of 12 children and adolescents. (b) Family members or '
         'other legally responsible persons shall be involved in development of plans in order to assure a smooth '
         'transition to a less restrictive setting. (c) The residential treatment staff secure facility shall coordinate '
         'with the local education agency to ensure that the child\'s educational needs are met as identified in the '
         'child\'s education plan and the treatment plan. Most of the children will be able to attend school; for others, '
         'the facility will coordinate services across settings such as alternative learning programs, day treatment, '
         'or a job placement. (d) Psychiatric consultation shall be available as needed for each child or adolescent. '
         '(e) If an adolescent has his 18th birthday while receiving treatment in the facility, he may remain for six '
         'months or until the end of the state fiscal year, whichever is longer. (f) Each child or adolescent shall be '
         'entitled to age-appropriate personal belongings unless such entitlement is counter-indicated in the treatment '
         'plan. (g) Each facility shall operate 24 hours per day, seven days a week, and each day of the year. '
         'Eff. April 3, 2006.'),
        ('10A NCAC 27G .1707 PERSONS PERMITTED IN THE FACILITY',
         '(a) Only admitted children or adolescents, legally responsible persons, staff, other family and friends '
         'identified in the treatment plan, and others permitted by the facility director shall be permitted on the '
         'premises. (b) Individuals other than those specified in Paragraph (a) of this Rule are prohibited from entering '
         'the facility except in instances of emergency or as permitted by law. Eff. April 3, 2006.'),
        ('10A NCAC 27G .1708 TRANSFER OR DISCHARGE',
         '(a) The purpose of this Rule is to address the transfer or discharge of a child or adolescent from the facility. '
         '(b) A child or adolescent shall not be discharged or transferred from a facility, except in case of emergency, '
         'without the advance written notification of the treatment team, including the legally responsible person. For '
         'purposes of this Rule, treatment team means the same as the existing child and family team or other involved '
         'persons as set forth in Paragraph (c) of this Rule. (c) The facility shall meet with existing child and family '
         'teams or other involved persons including the parent(s) or legal guardian, area authority or county program '
         'representative(s) and other representatives involved in the care and treatment of the child or adolescent, '
         'including local Department of Social Services, Local Education Agency and criminal justice agency, to make '
         'service planning decisions prior to the transfer or discharge of the child or adolescent from the facility. '
         '(d) In case of an emergency, the facility shall notify the treatment team including the legally responsible '
         'person of the transfer or discharge of the child or adolescent as soon as the emergency situation is stabilized. '
         '(e) In case of an emergency, notification may be by telephone. A service planning meeting as set forth in '
         'Paragraph (c) of this Rule shall be held within five business days of an emergency transfer or discharge. '
         'Eff. April 3, 2006.'),
    ]
    for title, text in rule_excerpts:
        story.append(Paragraph(f"<b>{title}</b>", STY['h3']))
        story.append(Paragraph(text, STY['rule_text']))
        story.append(Spacer(1, 6))

    story.append(PageBreak())

    # ─── 13. Appendix B — Audit Methodology Detail ───────────────────────
    story.append(add_heading('13. Appendix B — Audit Methodology Detail', STY['h1'], level=0))

    story.append(add_heading('13.1 Source Document Identification &amp; Version Control', STY['h2'], level=1))
    story.append(Paragraph(
        "<b>SOP Manual v2.22.</b> The audited source document is Well Spring Intervention LLC SOP &amp; Operational "
        "Manual, Doc. WSI-SOP-001, Rev. 2.22, August 2026 — Legislation-Free Public Edition. The PDF is 68 pages "
        "and was extracted via pdftotext into 4,379 lines of plain text. The text was verified against the source "
        "generation script (scripts/generate_sop.py and scripts/sop_content_v3*.py) to ensure no extraction "
        "artifacts. The PDF is available at /home/z/my-project/download/Well_Spring_Intervention_SOP_Manual_v2.22_Public-Edition.pdf.",
        STY['body']))
    story.append(Paragraph(
        "<b>10A NCAC 27G Rule Text.</b> The audited rule text is 10A NCAC 27G (Mental Health, Community Facilities "
        "and Services) Subchapter G, supplied verbatim in conversation. The full Subchapter text is 4,143 lines. "
        "This audit focused on Section .1700 (Residential Treatment Staff Secure for Children or Adolescents, rules "
        ".1701-.1708) and the cross-referenced core rules in .0104 (Staff Definitions), .0201 (Governing Body Policies), "
        ".0202 (Personnel Requirements), .0203 (QP/AP Competencies), .0204 (Paraprofessional Competencies), .0205 "
        "(Assessment and Service Plan), .0206 (Client Records), .0207 (Emergency Plans and Supplies), .0208 (Client "
        "Services), .0209 (Medication Requirements), and .0210 (Research Review Board).",
        STY['body']))

    story.append(add_heading('13.2 Rule-by-Rule Crosswalk Procedure', STY['h2'], level=1))
    story.append(Paragraph(
        "Each rule paragraph (e.g., .1704(c)(1)) was mapped to its corresponding SOP location via a three-step "
        "procedure: <b>(1) Keyword search</b> — keywords from the rule text (e.g., 'awake overnight,' 'staffing "
        "ratio,' 'two present') were searched in the SOP text via grep to identify candidate SOP sections; "
        "<b>(2) Manual review</b> — the candidate SOP sections were reviewed in context to verify they substantively "
        "address the rule requirement, with verbatim quotes preserved for both rule text and SOP text; "
        "<b>(3) Cross-reference verification</b> — each finding was checked against the full SOP text to ensure no "
        "other SOP section also addresses the same rule (to avoid duplicate findings).",
        STY['body']))

    story.append(add_heading('13.3 Severity Classification Criteria', STY['h2'], level=1))
    sev_data = [[Paragraph('<b>Severity</b>', STY['table_header']),
                 Paragraph('<b>Criteria</b>', STY['table_header'])]]
    for sev, desc in SEVERITY_LEGEND.items():
        sev_data.append([Paragraph(f"<b>{sev}</b>", STY['table_cell_center']),
                         Paragraph(desc, STY['table_cell'])])
    sev_widths = [0.20 * strip_avail, 0.80 * strip_avail]
    sev_tbl = Table(sev_data, colWidths=sev_widths, hAlign='CENTER', repeatRows=1)
    sev_tbl.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), HEADER_FILL),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('GRID', (0, 0), (-1, -1), 0.3, BORDER),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, TABLE_STRIPE]),
    ]))
    story.append(sev_tbl)

    story.append(add_heading('13.4 Status Classification Criteria', STY['h2'], level=1))
    stat_data = [[Paragraph('<b>Status</b>', STY['table_header']),
                  Paragraph('<b>Criteria</b>', STY['table_header'])]]
    for st, desc in STATUS_LEGEND.items():
        stat_data.append([Paragraph(f"<b>{st}</b>", STY['table_cell_center']),
                          Paragraph(desc, STY['table_cell'])])
    stat_tbl = Table(stat_data, colWidths=sev_widths, hAlign='CENTER', repeatRows=1)
    stat_tbl.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), HEADER_FILL),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('GRID', (0, 0), (-1, -1), 0.3, BORDER),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, TABLE_STRIPE]),
    ]))
    story.append(stat_tbl)

    story.append(add_heading('13.5 Strip-Flag Annotation Criteria', STY['h2'], level=1))
    story.append(Paragraph(
        "Each finding was annotated with a strip-flag (Y/N) indicating whether it involves a statutory or regulatory "
        "citation that should be replaced with plain-language operational text in the v2.23 public edition per the "
        "user's legislation-stripping directive. Strip-flag = Y is assigned when the finding involves any of: "
        "(a) a direct rule citation (e.g., '10A NCAC 27G .1700'); "
        "(b) a statutory citation (e.g., 'G.S. 122C-26'); "
        "(c) a federal regulation citation (e.g., '42 CFR Part 2,' '29 CFR 1910.1030'); "
        "(d) a state agency name (e.g., 'NC DHSR MHLC,' 'DSS'); "
        "(e) a state program identifier (e.g., 'LME/MCO,' 'IRIS,' 'NCTracks'); "
        "(f) a Medicaid policy citation (e.g., 'CCP 8D-2'); "
        "(g) a recognized accrediting body name (e.g., 'COA,' 'TJC,' 'CARF,' 'CQL'). "
        "Strip-flag = N is assigned when the finding involves only operational language with no statutory citation.",
        STY['body']))

    story.append(add_heading('13.6 Audit Limitations', STY['h2'], level=1))
    story.append(Paragraph(
        "This audit crosswalks the SOP Manual v2.22 against the .1700 Section + cross-referenced core rules only. "
        "It does not audit against the full 10A NCAC 27G Subchapter (4,143 lines) — see Section 2.1 for excluded "
        "rules. The audit is a documentation review only — it does not include on-site verification of operational "
        "practice. The audit was conducted by automated text extraction and manual review; it does not include "
        "interviews with facility staff, observation of practice, or review of actual clinical records. The audit "
        "findings should be used to inform v2.23 revision work and to prepare for the next DHSR MHLC licensure "
        "survey, but should not be considered a substitute for an on-site compliance survey.",
        STY['body']))

    # ─── Build ────────────────────────────────────────────────────────────
    doc.multiBuild(story, onFirstPage=header_footer, onLaterPages=header_footer)
    print(f"Body PDF built: {output_path}")


def merge_cover_and_body(cover_pdf, body_pdf, output_pdf):
    """Merge cover PDF (page 1) + body PDF (pages 2+) → single output."""
    from pypdf import PdfReader, PdfWriter
    A4_W, A4_H = 595.28, 841.89

    def normalize_page_to_a4(page):
        """Force every page to exact A4 dimensions (595.28 x 841.89 pt)."""
        from pypdf.generic import RectangleObject
        box = page.mediabox
        w, h = float(box.width), float(box.height)
        if abs(w - A4_W) > 0.5 or abs(h - A4_H) > 0.5:
            page.scale_to(A4_W, A4_H)
        # Force exact A4 mediabox/cropbox to eliminate sub-pt drift
        page.mediabox = RectangleObject((0, 0, A4_W, A4_H))
        page.cropbox = RectangleObject((0, 0, A4_W, A4_H))
        return page

    writer = PdfWriter()
    cover_page = PdfReader(cover_pdf).pages[0]
    writer.add_page(normalize_page_to_a4(cover_page))
    for page in PdfReader(body_pdf).pages:
        writer.add_page(normalize_page_to_a4(page))
    writer.add_metadata({
        '/Title': 'Well Spring Intervention SOP Manual v2.22 Compliance Audit Report',
        '/Author': 'Z.ai',
        '/Creator': 'Z.ai',
        '/Subject': 'Compliance audit of SOP Manual v2.22 against 10A NCAC 27G .1700 + core rules',
    })
    with open(output_pdf, 'wb') as f:
        writer.write(f)
    print(f"Final merged PDF: {output_pdf}")


if __name__ == '__main__':
    body_path = '/home/z/my-project/scripts/audit_body.pdf'
    cover_path = '/home/z/my-project/scripts/audit_cover.pdf'
    final_path = '/home/z/my-project/download/WSI_SOP_v2.22_Compliance_Audit_Report.pdf'

    build_body_pdf(body_path)
    merge_cover_and_body(cover_path, body_path, final_path)

    # Report file size
    import os
    size_kb = os.path.getsize(final_path) / 1024
    print(f"File size: {size_kb:.1f} KB")
