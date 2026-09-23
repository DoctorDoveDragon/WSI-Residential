#!/usr/bin/env python3
"""
generate_carf_plans.py — Generate the WSI CARF CYS 2026 Conformance Plan
Portfolio PDF.

Imports helpers/styles from generate_sop.py to maintain visual consistency
with the SOP Manual v2.24. Uses TocDocTemplate.multiBuild for auto-TOC.

Output: /home/z/my-project/scripts/carf_plans_body.pdf (body only)
Final merge with cover via merge_carf_plans.py.
"""

import os
import sys
import platform

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch, mm
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle,
    KeepTogether, CondPageBreak, HRFlowable, Flowable,
)
from reportlab.platypus.tableofcontents import TableOfContents
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFontFamily

# ─── Font registration (same as SOP) ──────────────────────────────────────
_IS_MAC = platform.system() == 'Darwin'
FONT_DIR = os.path.expanduser('~/.openclaw/workspace/fonts') if _IS_MAC else '/usr/share/fonts'

pdfmetrics.registerFont(TTFont('NotoSerifSC',      f'{FONT_DIR}/truetype/noto-serif-sc/NotoSerifSC-Regular.ttf'))
pdfmetrics.registerFont(TTFont('NotoSerifSC-Bold', f'{FONT_DIR}/truetype/noto-serif-sc/NotoSerifSC-Bold.ttf'))
pdfmetrics.registerFont(TTFont('FreeSerif',           f'{FONT_DIR}/truetype/freefont/FreeSerif.ttf'))
pdfmetrics.registerFont(TTFont('FreeSerif-Bold',      f'{FONT_DIR}/truetype/freefont/FreeSerifBold.ttf'))
pdfmetrics.registerFont(TTFont('FreeSerif-Italic',    f'{FONT_DIR}/truetype/freefont/FreeSerifItalic.ttf'))
pdfmetrics.registerFont(TTFont('FreeSerif-BoldItalic',f'{FONT_DIR}/truetype/freefont/FreeSerifBoldItalic.ttf'))
pdfmetrics.registerFont(TTFont('DejaVuSans', f'{FONT_DIR}/truetype/dejavu/DejaVuSansMono.ttf'))

registerFontFamily('NotoSerifSC',  normal='NotoSerifSC',  bold='NotoSerifSC-Bold')
registerFontFamily('FreeSerif',    normal='FreeSerif', bold='FreeSerif-Bold',
                   italic='FreeSerif-Italic', boldItalic='FreeSerif-BoldItalic')
registerFontFamily('DejaVuSans',   normal='DejaVuSans', bold='DejaVuSans')

sys.path.insert(0, '/home/z/my-project/skills/pdf/scripts')
from pdf import install_font_fallback
install_font_fallback()

# ─── Import everything from generate_sop (palette, styles, helpers) ───────
from generate_sop import (
    PAGE_W, PAGE_H, LEFT_M, RIGHT_M, TOP_M, BOTTOM_M, AVAIL_W,
    PAGE_BG, SECTION_BG, CARD_BG, TABLE_STRIPE, HEADER_FILL, COVER_BLOCK,
    BORDER, ICON, ACCENT, ACCENT_2, TEXT_PRIMARY, TEXT_MUTED,
    SEM_SUCCESS, SEM_WARNING, SEM_ERROR, SEM_INFO,
    BODY_FONT, BODY_BOLD, BODY_ITAL,
    s_part, s_part_kicker, s_part_intro, s_h1, s_h2, s_body, s_body_just,
    s_ref, s_bullet, s_callout, s_callout_label,
    s_form_title, s_form_meta, s_form_instr, s_form_section,
    s_th, s_th_left, s_td, s_td_c, s_td_b, s_td_sm,
    s_toc_title, s_toc_kicker, s_toc_intro, s_toc_l0, s_toc_l1,
    TocDocTemplate, draw_header_footer,
)

# ─── Override title for headers/footers ───────────────────────────────────
DOC_TITLE_SHORT = 'CARF CYS 2026 Conformance Plans — Rev. 1.3 (Aug 2026)'
DOC_ORG = 'Well Spring Intervention LLC'


# Custom header/footer (overrides generate_sop's)
def draw_carf_header_footer(canvas, doc):
    canvas.saveState()
    # Header (kicker line)
    canvas.setFont(BODY_BOLD, 8)
    canvas.setFillColor(TEXT_MUTED)
    canvas.drawString(LEFT_M, PAGE_H - TOP_M * 0.55, DOC_TITLE_SHORT)
    canvas.drawRightString(PAGE_W - RIGHT_M, PAGE_H - TOP_M * 0.55, DOC_ORG)
    canvas.setStrokeColor(BORDER)
    canvas.setLineWidth(0.5)
    canvas.line(LEFT_M, PAGE_H - TOP_M * 0.6, PAGE_W - RIGHT_M, PAGE_H - TOP_M * 0.6)

    # Footer (page number + confidentiality)
    canvas.setFont(BODY_ITAL, 8)
    canvas.setFillColor(TEXT_MUTED)
    canvas.drawString(LEFT_M, BOTTOM_M * 0.55,
                      'Confidential — Internal Use Only')
    page_num = canvas.getPageNumber() + 1  # +1 for cover
    canvas.drawRightString(PAGE_W - RIGHT_M, BOTTOM_M * 0.55, f'Page {page_num}')
    canvas.restoreState()


# ─── Main ────────────────────────────────────────────────────────────────
OUTPUT_BODY = '/home/z/my-project/scripts/carf_plans_body.pdf'

SELF_REF = (
    'Well Spring Intervention LLC CARF CYS 2026 Conformance Plan Portfolio '
    '(Doc. WSI-CARF-PLANS-001, Rev. 1.3, Aug 2026)'
)


def build():
    from carf_plans_content import build_part1

    doc = TocDocTemplate(
        OUTPUT_BODY,
        pagesize=A4,
        leftMargin=LEFT_M, rightMargin=RIGHT_M,
        topMargin=TOP_M, bottomMargin=BOTTOM_M,
        title='Well Spring Intervention LLC — CARF CYS 2026 Conformance Plans',
        author='Well Spring Intervention LLC',
        creator='Z.ai',
        subject='CARF CYS 2026 Inaugural Accreditation Conformance Plan Portfolio (Rev. 1.3)',
        keywords='CARF, CYS, 2026, Inaugural Accreditation, Conformance Plans, Strategic Plan, '
                 'Stakeholder Input, Legal Compliance, Financial, ERM, Workforce, Accessibility, '
                 'Performance Measurement, Telehealth, Quality Records',
    )

    story = []

    # ── About This Manual ─────────────────────────────────────────────
    story.append(Paragraph('ABOUT THIS PORTFOLIO', s_toc_kicker))
    story.append(Paragraph('Document Overview', s_toc_title))
    story.append(HRFlowable(width=80, color=ACCENT, thickness=2, spaceBefore=2, spaceAfter=14))

    story.append(Paragraph(
        'This portfolio (Rev. 1.3, August 2026) contains the fifteen written '
        'plans, policies, and procedures referenced in §12.1–§12.19 of the '
        '<b>Well Spring Intervention LLC SOP Manual (Rev. 2.24)</b> required to '
        'demonstrate conformance to the 2026 CARF Child and Youth Services '
        '(CYS) Standards Manual at the time of an <b>Inaugural One-Year '
        'Accreditation survey</b>, per the <b>2026 CYS Inaugural Accreditation '
        'Guidelines</b> (effective July 1, 2026 – June 30, 2027). Each plan is '
        'a self-contained written policy with purpose, scope, policy statement, '
        'procedure, responsible parties, review schedule, and approval '
        'signature block. The QP maintains the signed originals in the facility '
        'compliance binder and presents this portfolio to CARF surveyors as '
        'the primary evidence of organizational readiness.',
        s_body
    ))
    story.append(Spacer(1, 6))

    story.append(Paragraph('<b>Document ID.</b> Doc. WSI-CARF-PLANS-001, Rev. 1.3 (August 2026).', s_body))
    story.append(Paragraph('<b>Population Served.</b> Children &amp; Adolescents — Mental Health / Behavioral Challenges.', s_body))
    story.append(Paragraph('<b>Service Type.</b> Level III Residential Treatment Facility (Staff-Secure for Children and Adolescents) \u2014 10A NCAC 27G .1700 (specifically .1701(b) governing the staff-secure subcategory and .1704 governing continuous supervision).', s_body))
    story.append(Paragraph('<b>Service Intensity.</b> The Level III RTF (Staff-Secure) provides 24-hour intensive residential treatment for children and adolescents with a primary diagnosis of mental illness, emotional disturbance, or substance-related disorder who do not meet inpatient psychiatric criteria but require removal from the home and treatment in a staff-secure setting. Features include continuous awake overnight supervision per .1704 (2 staff for 1-4 youth, both awake per the SOP §2.1 conservative standard that exceeds the .1704(c)(1) minimum of 1 awake + 1 may-sleep; 3 staff for 5-8 youth; 4 staff for 9-12 youth), Licensed Professional on-site during business hours with minimum 4 hours/week face-to-face clinical consultation per .1705(a)-(b) and SOP §4.6, on-call 24/7 for clinical emergencies, on-site psychiatric coverage per the medication-management schedule with 24/7 on-call psychiatric consultation, Registered Nurse on-site or on-call 24/7 for medical and medication-related needs, individual therapy minimum 2 sessions/week, daily group therapy, weekly family therapy, 14 hours/week of planned group activities per .1701(e) and SOP §5.5, and Person-Centered Plan reviews at minimum every 90 days or as clinically indicated. Maximum capacity is 12 children per .1706(a).', s_body))
    story.append(Paragraph('<b>Document Owner.</b> Executive Director &amp; Qualified Professional (QP).', s_body))
    story.append(Paragraph('<b>Companion Documents.</b> SOP Manual v2.24 (Doc. WSI-SOP-001, Rev. 2.24); Resident Handbook (Doc. WSI-RH-001); CARF CYS 2026 Compliance Audit Crosswalk (Doc. WSI-CARF-XW-001).', s_body))
    story.append(Spacer(1, 10))

    story.append(Paragraph('<b>Plan Portfolio Contents.</b>', s_h2))
    story.append(Paragraph(
        'This portfolio contains fifteen plans, organized in the order '
        'referenced in SOP §12. Each plan is numbered consistently with the '
        'SOP §12 subsection that references it:',
        s_body
    ))
    plans_list = [
        '<b>Plan 1 — Strategic Plan</b> (§12.1) — three-year strategic goals, mission/vision/values, environmental analysis, succession planning',
        '<b>Plan 2 — Stakeholder Input Plan</b> (§12.2) — quarterly surveys, advisory convening, "You Said / We Did" feedback loop, non-retaliation',
        '<b>Plan 3 — Legal Compliance Plan</b> (§12.3) — Compliance Officer, Legal Compliance Register, annual legal-compliance review',
        '<b>Plan 4 — Financial Plan</b> (§12.4) — annual budget, capital reserve, internal controls, audit, resident trust funds',
        '<b>Plan 5 — Enterprise Risk Management Plan</b> (§12.5) — Enterprise Risk Register, business-continuity plan, incident integration',
        '<b>Plan 6 — Health &amp; Safety Committee Charter</b> (§12.6) — standing committee, monthly meetings, written health-and-safety policies',
        '<b>Plan 7 — Workforce Development Plan</b> (§12.7) — recruiting, orientation curriculum, annual training, position descriptions, performance evaluation',
        '<b>Plan 8 — Resident Rights Policy Compilation</b> (§12.8) — eleven rights, grievance procedure, audit and trend reporting',
        '<b>Plan 9 — Accessibility &amp; Nondiscrimination Plan</b> (§12.9) — nondiscrimination, language access, reasonable accommodation, physical accessibility',
        '<b>Plan 10 — Performance Measurement Plan</b> (§12.10) — 25 KPIs across seven domains, data aggregation, quarterly Governing Body reporting',
        '<b>Plan 11 — Program Description</b> (§12.11) — populations served, service array, program philosophy, staffing, physical environment',
        '<b>Plan 12 — Screening and Access Policy</b> (§12.12) — referral intake, screening criteria, admission decision, waitlist, denial appeals',
        '<b>Plan 13 — Quality Records Review Procedure</b> (§12.17) — quarterly Form 8 audits, trend analysis, corrective action',
        '<b>Plan 14 — Telehealth &amp; ICT Service Delivery Policy</b> (§12.18) — eligible services, technology platforms, informed consent, emergency procedures',
        '<b>Plan 15 — CARF CYS 2026 Sections 3–5 Standards Crosswalk</b> (§12.19) — 38-item crosswalk mapping standards to written policies',
    ]
    for item in plans_list:
        story.append(Paragraph(f'• {item}', s_bullet))
    story.append(Spacer(1, 10))

    story.append(Paragraph('<b>Approval &amp; Implementation.</b>', s_h2))
    story.append(Paragraph(
        'Each plan includes an Approval signature block requiring signatures '
        'from the Executive Director, Clinical Director, Qualified Professional '
        '(QP), and Compliance Officer. Upon approval, each plan becomes a '
        'written policy of Well Spring Intervention LLC, effective upon the '
        'date of the last signature. Plans are reviewed at minimum annually '
        'and updated as needed to reflect changes in CARF standards, '
        'regulatory requirements, organizational structure, or program design.',
        s_body
    ))
    story.append(PageBreak())

    # ── TOC page ──────────────────────────────────────────────────────
    story.append(Paragraph('CONTENTS', s_toc_kicker))
    story.append(Paragraph('Table of Contents', s_toc_title))
    story.append(HRFlowable(width=80, color=ACCENT, thickness=2, spaceBefore=2, spaceAfter=12))
    story.append(Paragraph(
        'This portfolio is organized into fifteen plans, each addressing a '
        'specific CARF CYS 2026 standard area referenced in SOP §12.1–§12.19. '
        'Each plan is self-contained and may be reviewed, approved, and '
        'implemented independently. The QP maintains the master copy of all '
        'fifteen plans in the compliance binder, with signed originals of '
        'each. A complete revision history appears at the end of this '
        'portfolio.',
        s_toc_intro
    ))

    toc = TableOfContents()
    toc.levelStyles = [s_toc_l0, s_toc_l1]
    story.append(toc)
    story.append(PageBreak())

    # ── Plans content ─────────────────────────────────────────────────
    story.extend(build_part1())

    doc.multiBuild(story, onFirstPage=draw_carf_header_footer, onLaterPages=draw_carf_header_footer)
    print(f'Body PDF written: {OUTPUT_BODY}')


if __name__ == '__main__':
    build()
