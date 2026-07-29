#!/usr/bin/env python3
"""
Generate standalone fillable PDF versions of all 9 forms from the
Well Spring Intervention LLC SOP Manual. Each form is a separate PDF
file with interactive AcroForm fields, saved to:
    /home/z/my-project/download/forms/

Each standalone form includes:
  - A header with the form number, title, and Form Properties banner
  - All fillable fields (text fields + checkboxes) from the parent manual
  - A footer noting the source manual (Rev. 2.13) and the form's purpose

The standalone forms are designed for use OUTSIDE the manual — for
printing, copying, sharing, editing, and filling by staff during daily
operations. They use the same AcroForm helpers as the parent manual so
the interactive behavior is identical.
"""

import os
import sys

# Make the SOP scripts importable
sys.path.insert(0, '/home/z/my-project/scripts')

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable,
    PageBreak,
)

from generate_sop import (
    BODY_FONT, BODY_BOLD, BODY_ITAL,
    HEADER_FILL, BORDER, ACCENT, TEXT_PRIMARY, TEXT_MUTED, CARD_BG,
    AVAIL_W, s_form_meta, s_form_instr, s_form_section, s_body, s_h1, s_h2,
    form_usage_banner,
    AcroTextField, AcroCheckbox,
    fillable_meta_row, fillable_check_row, fillable_signature_row,
)
from sop_content_v2_part3 import _form_banner_and_heading, _fillable_data_cells
from reportlab.platypus.flowables import Flowable

OUTPUT_DIR = '/home/z/my-project/download/forms'
PAGE_W, PAGE_H = A4
LEFT_M = 0.85 * inch
RIGHT_M = 0.85 * inch
TOP_M = 0.95 * inch
BOTTOM_M = 0.85 * inch


def _draw_header_footer(canvas, doc):
    """Draw a minimal header/footer for standalone forms."""
    canvas.saveState()
    # Header
    canvas.setFont('FreeSerif-Italic', 8)
    canvas.setFillColor(TEXT_MUTED)
    canvas.drawString(LEFT_M, PAGE_H - TOP_M * 0.55,
                      'Well Spring Intervention LLC — Standalone Fillable Form')
    canvas.drawRightString(PAGE_W - RIGHT_M, PAGE_H - TOP_M * 0.55,
                           'Rev. 2.13 (RMDM-Compliant)')
    canvas.setStrokeColor(BORDER)
    canvas.setLineWidth(0.5)
    canvas.line(LEFT_M, PAGE_H - TOP_M * 0.55 - 4,
                PAGE_W - RIGHT_M, PAGE_H - TOP_M * 0.55 - 4)
    # Footer
    canvas.line(LEFT_M, BOTTOM_M * 0.55 + 14,
                PAGE_W - RIGHT_M, BOTTOM_M * 0.55 + 14)
    canvas.setFont('FreeSerif-Italic', 8)
    canvas.setFillColor(TEXT_MUTED)
    canvas.drawString(LEFT_M, BOTTOM_M * 0.55,
                      'Confidential — Internal Use Only')
    canvas.drawRightString(PAGE_W - RIGHT_M, BOTTOM_M * 0.55,
                           f'Page {canvas.getPageNumber()}')
    canvas.restoreState()


def _standalone_form_doc(filepath, title):
    """Create a SimpleDocTemplate configured for a standalone fillable form."""
    return SimpleDocTemplate(
        filepath,
        pagesize=A4,
        leftMargin=LEFT_M, rightMargin=RIGHT_M,
        topMargin=TOP_M, bottomMargin=BOTTOM_M,
        title=title,
        author='Well Spring Intervention LLC',
        creator='Z.ai',
        subject=f'{title} — Rev. 2.13 (RMDM-Compliant)',
    )


def _form_intro(form_num, title, anchor_text, external_ref=None,
                instructions=None):
    """Emit the section heading + ref + usage banner for a standalone form."""
    out = [
        Paragraph(f'FORM {form_num}', ParagraphStyle(
            name='FormKicker', fontName=BODY_BOLD, fontSize=10, leading=14,
            textColor=ACCENT, alignment=TA_LEFT, spaceAfter=4,
        )),
        Paragraph(title, ParagraphStyle(
            name='FormTitle', fontName=BODY_BOLD, fontSize=18, leading=22,
            textColor=HEADER_FILL, alignment=TA_LEFT, spaceAfter=6,
        )),
        HRFlowable(width=80, color=ACCENT, thickness=2, spaceBefore=2, spaceAfter=10),
    ]
    out.extend(_form_banner_and_heading(
        form_num, title, anchor_text, external_ref=external_ref,
        instructions=instructions,
    )[1:])  # skip the duplicate section_heading; we already emitted a bigger title above
    return out


# ── Form 1: Shift Change & Awake Night Watch Log ──────────────────────
def build_form_1(filepath):
    doc = _standalone_form_doc(filepath, 'Form 1 — Shift Change & Awake Night Watch Log')
    story = []
    story.extend(_form_intro(
        1, 'Shift Change & Awake Night Watch Log',
        'Part 3 · Form 1: Shift Change & Awake Night Watch Log',
        instructions='Initial each box to verify you visually saw the youth breathing and in their bed. Click any cell to type.',
    ))
    story.append(fillable_meta_row([
        ('Facility:', 200, 'Facility name'),
        ('Date:', 120, 'Date of shift'),
    ]))
    story.append(Spacer(1, 4))
    story.append(Paragraph('<b>Awake Overnight Room Checks (Every 15 Minutes)</b>', s_form_section))

    times = ['11:00 PM','11:15 PM','11:30 PM','11:45 PM',
             '12:00 AM','12:15 AM','12:30 AM','12:45 AM',
             '1:00 AM','1:15 AM','1:30 AM','1:45 AM',
             '2:00 AM','2:15 AM','2:30 AM','2:45 AM',
             '3:00 AM','3:15 AM','3:30 AM','3:45 AM',
             '4:00 AM','4:15 AM','4:30 AM','4:45 AM',
             '5:00 AM','5:15 AM','5:30 AM','5:45 AM',
             '6:00 AM','6:15 AM','6:30 AM','6:45 AM']
    col_widths = [0.18*AVAIL_W, 0.16*AVAIL_W, 0.16*AVAIL_W, 0.16*AVAIL_W, 0.16*AVAIL_W, 0.18*AVAIL_W]
    th = ParagraphStyle('f1th_st', fontName=BODY_BOLD, fontSize=8.5, leading=11,
                        textColor=colors.white, alignment=TA_CENTER)
    td_t = ParagraphStyle('f1tdt_st', fontName=BODY_BOLD, fontSize=8, leading=10,
                          textColor=TEXT_PRIMARY, alignment=TA_CENTER)
    data = [[Paragraph('<b>Time</b>', th), Paragraph('<b>Youth 1</b>', th),
             Paragraph('<b>Youth 2</b>', th), Paragraph('<b>Youth 3</b>', th),
             Paragraph('<b>Youth 4</b>', th), Paragraph('<b>Staff Initials</b>', th)]]
    for t in times:
        data.append([Paragraph(t, td_t),
                     *_fillable_data_cells(5, default_width=50, height=12, font_size=8)])
    t1 = Table(data, colWidths=col_widths, hAlign='CENTER', repeatRows=1)
    sc = [('BACKGROUND', (0, 0), (-1, 0), HEADER_FILL),
          ('GRID', (0, 0), (-1, -1), 0.4, BORDER),
          ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
          ('LEFTPADDING', (0, 0), (-1, -1), 3),
          ('RIGHTPADDING', (0, 0), (-1, -1), 3),
          ('TOPPADDING', (0, 0), (-1, -1), 3),
          ('BOTTOMPADDING', (0, 0), (-1, -1), 3)]
    for i in range(1, len(data)):
        bg = colors.HexColor('#f3f2f1') if i % 2 == 1 else colors.white
        sc.append(('BACKGROUND', (0, i), (-1, i), bg))
    t1.setStyle(TableStyle(sc))
    story.append(t1)
    story.append(Spacer(1, 10))
    story.append(Paragraph('<b>Shift Handoff Verification:</b> Controlled substance count verified.', s_form_meta))
    story.append(fillable_signature_row([
        ('Off-Going Staff:', 180, 'Off-going staff signature'),
        ('On-Coming Staff:', 180, 'On-coming staff signature'),
    ]))
    doc.build(story, onFirstPage=_draw_header_footer, onLaterPages=_draw_header_footer)


# ── Form 2: Contraband & Belongings Inventory ─────────────────────────
def build_form_2(filepath):
    doc = _standalone_form_doc(filepath, 'Form 2 — Contraband & Belongings Inventory')
    story = []
    story.extend(_form_intro(
        2, 'Contraband & Belongings Inventory',
        'Part 3 · Form 2: Contraband & Belongings Inventory',
    ))
    story.append(fillable_meta_row([
        ('Youth Name:', 200, 'Youth full name'),
        ('Service Record # / MID:', 120, 'Service record number or MID'),
        ('Date:', 80, 'Date of search'),
    ]))
    story.append(Spacer(1, 4))
    story.append(Paragraph('<b>Search Type:</b>', s_form_meta))
    story.append(fillable_check_row([
        ('Admission', 'Search type: admission'),
        ('Return from Pass', 'Search type: return from pass'),
        ('Probable Cause', 'Search type: probable cause'),
    ]))
    story.append(fillable_meta_row([('QP Approval:', 250, 'QP approval for probable-cause search')]))
    story.append(Spacer(1, 6))
    f2_header = ['Item Description', 'Quantity', 'Brought In / Found', 'Disposition (Kept / Safe / Guardian)', 'Staff Initials']
    f2_rows = [_fillable_data_cells(5, default_width=60, height=14, font_size=9) for _ in range(8)]
    f2_widths = [0.32*AVAIL_W, 0.10*AVAIL_W, 0.18*AVAIL_W, 0.27*AVAIL_W, 0.13*AVAIL_W]
    s_th = ParagraphStyle('f2th_st', fontName=BODY_BOLD, fontSize=9.5, leading=12,
                          textColor=colors.white, alignment=TA_CENTER)
    tbl = Table([[Paragraph(f'<b>{h}</b>', s_th) for h in f2_header]] + f2_rows,
                colWidths=f2_widths, hAlign='CENTER', repeatRows=1)
    tbl.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), HEADER_FILL),
        ('GRID', (0, 0), (-1, -1), 0.6, BORDER),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(tbl)
    story.append(Spacer(1, 8))
    story.append(Paragraph('<b>Youth Acknowledgment:</b> Belongings inventoried in my presence.', s_form_meta))
    story.append(fillable_signature_row([
        ('Youth Signature:', 180, 'Youth signature'),
        ('Staff Signature:', 180, 'Staff signature'),
    ]))
    doc.build(story, onFirstPage=_draw_header_footer, onLaterPages=_draw_header_footer)


# ── Form 3: Physical Restraint & Debriefing Checklist ─────────────────
def build_form_3(filepath):
    doc = _standalone_form_doc(filepath, 'Form 3 — Physical Restraint & Debriefing Checklist')
    story = []
    story.extend(_form_intro(
        3, 'Physical Restraint & Debriefing Checklist',
        'Part 3 · Form 3: Physical Restraint & Debriefing Checklist',
    ))
    story.append(fillable_meta_row([
        ('Youth:', 140, 'Youth name'),
        ('Service Record # / MID:', 100, 'Service record number or MID'),
        ('Date:', 70, 'Date of restraint'),
    ]))
    story.append(fillable_meta_row([
        ('Time Started:', 70, 'Time restraint started'),
        ('Time Ended:', 70, 'Time restraint ended'),
        ('Total Duration (Min):', 60, 'Total duration in minutes'),
        ('Technique:', 150, 'Restraint technique used'),
    ]))
    story.append(Spacer(1, 6))
    story.append(Paragraph('Pre-Restraint De-escalation Attempts:', s_form_section))
    story.append(fillable_check_row([
        ('Verbal redirection', 'De-escalation: verbal redirection'),
        ('Offered break', 'De-escalation: offered break'),
        ('Sensory item', 'De-escalation: sensory item'),
        ('BSP coping skill', 'De-escalation: BSP coping skill'),
        ('Separation', 'De-escalation: separation'),
    ]))
    story.append(Paragraph('Reason for Restraint (Imminent danger):', s_form_section))
    story.append(fillable_check_row([
        ('Danger to Self', 'Reason: danger to self'),
        ('Danger to Others', 'Reason: danger to others'),
        ('Property destruction posing risk', 'Reason: property destruction posing risk'),
    ]))
    story.append(Paragraph('Describe objectively:', s_form_meta))
    story.append(AcroTextField(width=AVAIL_W, height=40, tooltip='Objective description of incident',
                               font_size=9, border_style='underlined'))
    story.append(Spacer(1, 6))
    story.append(Paragraph('Post-Restraint Medical Check (Within 1 hour):', s_form_section))
    story.append(Paragraph('Youth checked for injuries, breathing normally:', s_form_meta))
    story.append(fillable_check_row([
        ('Yes', 'Medical check: yes'),
        ('No (Seek medical attention)', 'Medical check: no — seek medical attention'),
    ]))
    story.append(fillable_signature_row([('Staff Signature:', 280, 'Staff signature for medical check')]))
    story.append(Paragraph('Notifications:', s_form_section))
    story.append(Paragraph('On-Call QP Notified:', s_form_meta))
    story.append(fillable_check_row([('Y', 'On-call QP notified: yes'), ('N', 'On-call QP notified: no')]))
    story.append(fillable_meta_row([('Time:', 80, 'Time QP notified'), ('Guardian Notified:', 0, '')]))
    story.append(fillable_check_row([('Y', 'Guardian notified: yes'), ('N', 'Guardian notified: no')]))
    story.append(fillable_meta_row([('Time:', 80, 'Time guardian notified'), ('IRIS Report Filed:', 0, '')]))
    story.append(fillable_check_row([('Y', 'IRIS report filed: yes'), ('N', 'IRIS report filed: no')]))
    story.append(fillable_meta_row([('IRIS ID #:', 200, 'IRIS report ID number')]))
    story.append(Paragraph('Post-Restraint Debriefing (Within 24 hours):', s_form_section))
    story.append(fillable_meta_row([
        ('Youth debriefed by:', 200, 'Name of person who debriefed youth'),
        ('Date/Time:', 120, 'Date and time of debriefing'),
    ]))
    story.append(Paragraph('Trigger?', s_form_meta))
    story.append(AcroTextField(width=AVAIL_W, height=24, tooltip='Trigger identified during debriefing',
                               font_size=9, border_style='underlined'))
    story.append(Paragraph('Youth alternative?', s_form_meta))
    story.append(AcroTextField(width=AVAIL_W, height=24, tooltip='Youth-identified alternative coping skill',
                               font_size=9, border_style='underlined'))
    story.append(Paragraph('Staff alternative?', s_form_meta))
    story.append(AcroTextField(width=AVAIL_W, height=24, tooltip='Staff-identified alternative intervention',
                               font_size=9, border_style='underlined'))
    story.append(fillable_signature_row([
        ('Youth Signature:', 180, 'Youth signature'),
        ('QP Signature:', 180, 'QP signature'),
    ]))
    doc.build(story, onFirstPage=_draw_header_footer, onLaterPages=_draw_header_footer)


# ── Form 4: Home Pass & Medicaid Billing Exclusion Tracker ─────────────
def build_form_4(filepath):
    doc = _standalone_form_doc(filepath, 'Form 4 — Home Pass & Medicaid Billing Exclusion Tracker')
    story = []
    story.extend(_form_intro(
        4, 'Home Pass & Medicaid Billing Exclusion Tracker',
        'Part 3 · Form 4: Home Pass & Medicaid Billing Exclusion Tracker',
    ))
    story.append(fillable_meta_row([
        ('Youth:', 200, 'Youth name'),
        ('Service Record # / MID:', 120, 'Service record number or MID'),
        ('Month/Year:', 100, 'Month and year'),
    ]))
    story.append(Spacer(1, 6))
    f4_header = ['Date Left', 'Time Left', 'Destination / Pass', 'Date Returned',
                 'Time Returned', 'Total Hours Away', 'Billing Action (Suspension Days)', 'Staff Initials']
    f4_rows = [_fillable_data_cells(8, default_width=60, height=14, font_size=8) for _ in range(12)]
    f4_widths = [0.10*AVAIL_W, 0.09*AVAIL_W, 0.18*AVAIL_W, 0.11*AVAIL_W,
                 0.11*AVAIL_W, 0.12*AVAIL_W, 0.18*AVAIL_W, 0.11*AVAIL_W]
    f4_th = ParagraphStyle('f4th_st', fontName=BODY_BOLD, fontSize=8, leading=10,
                           textColor=colors.white, alignment=TA_CENTER)
    tbl = Table([[Paragraph(f'<b>{h}</b>', f4_th) for h in f4_header]] + f4_rows,
                colWidths=f4_widths, hAlign='CENTER', repeatRows=1)
    tbl.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), HEADER_FILL),
        ('GRID', (0, 0), (-1, -1), 0.6, BORDER),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(tbl)
    story.append(Spacer(1, 8))
    story.append(Paragraph('<b>Billing Coordinator Sign-Off:</b> Medicaid billing adjusted for suspension days.', s_form_meta))
    story.append(fillable_signature_row([
        ('Signature:', 220, 'Billing coordinator signature'),
        ('Date:', 100, 'Date of sign-off'),
    ]))
    doc.build(story, onFirstPage=_draw_header_footer, onLaterPages=_draw_header_footer)


# ── Form 5: Emergency Drill & Environmental Safety Log ────────────────
def build_form_5(filepath):
    doc = _standalone_form_doc(filepath, 'Form 5 — Emergency Drill & Environmental Safety Log')
    story = []
    story.extend(_form_intro(
        5, 'Emergency Drill & Environmental Safety Log',
        'Part 3 · Form 5: Emergency Drill & Environmental Safety Log',
    ))
    story.append(fillable_meta_row([('Facility:', 280, 'Facility name')]))
    story.append(Spacer(1, 6))
    # Fire drills
    story.append(Paragraph('Monthly Fire Drills (Under 3 minutes)', s_form_section))
    f5a_header = ['Month', 'Date', 'Time of Day', '# Youth', 'Evac Time', 'Staff', 'Signature']
    f5a_th = ParagraphStyle('f5ath_st', fontName=BODY_BOLD, fontSize=8.5, leading=11,
                            textColor=colors.white, alignment=TA_CENTER)
    s_td_sm = ParagraphStyle('f5asm_st', fontName=BODY_FONT, fontSize=8, leading=10,
                             textColor=TEXT_PRIMARY, alignment=TA_CENTER)
    f5a_data = [[Paragraph(f'<b>{h}</b>', f5a_th) for h in f5a_header]]
    for m in ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']:
        f5a_data.append([Paragraph(m, s_td_sm),
                         *_fillable_data_cells(6, default_width=50, height=12, font_size=8)])
    f5a_widths = [0.10*AVAIL_W, 0.14*AVAIL_W, 0.16*AVAIL_W, 0.12*AVAIL_W,
                  0.14*AVAIL_W, 0.16*AVAIL_W, 0.18*AVAIL_W]
    t5a = Table(f5a_data, colWidths=f5a_widths, hAlign='CENTER', repeatRows=1)
    sc = [('BACKGROUND', (0, 0), (-1, 0), HEADER_FILL),
          ('GRID', (0, 0), (-1, -1), 0.4, BORDER),
          ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
          ('LEFTPADDING', (0, 0), (-1, -1), 4),
          ('RIGHTPADDING', (0, 0), (-1, -1), 4),
          ('TOPPADDING', (0, 0), (-1, -1), 4),
          ('BOTTOMPADDING', (0, 0), (-1, -1), 4)]
    for i in range(1, len(f5a_data)):
        bg = colors.HexColor('#f3f2f1') if i % 2 == 1 else colors.white
        sc.append(('BACKGROUND', (0, i), (-1, i), bg))
    t5a.setStyle(TableStyle(sc))
    story.append(t5a)
    story.append(Spacer(1, 10))
    # Tornado drills
    story.append(Paragraph('Quarterly Tornado Drills', s_form_section))
    f5b_header = ['Quarter', 'Date', '# Youth', 'Staff', 'Signature']
    f5b_th = ParagraphStyle('f5bth_st', fontName=BODY_BOLD, fontSize=8.5, leading=11,
                            textColor=colors.white, alignment=TA_CENTER)
    f5b_data = [[Paragraph(f'<b>{h}</b>', f5b_th) for h in f5b_header]]
    for q in ['Q1','Q2','Q3','Q4']:
        f5b_data.append([Paragraph(q, s_td_sm),
                         *_fillable_data_cells(4, default_width=60, height=12, font_size=8)])
    f5b_widths = [0.14*AVAIL_W, 0.20*AVAIL_W, 0.18*AVAIL_W, 0.20*AVAIL_W, 0.28*AVAIL_W]
    t5b = Table(f5b_data, colWidths=f5b_widths, hAlign='CENTER', repeatRows=1)
    sc2 = [('BACKGROUND', (0, 0), (-1, 0), HEADER_FILL),
           ('GRID', (0, 0), (-1, -1), 0.4, BORDER),
           ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
           ('LEFTPADDING', (0, 0), (-1, -1), 4),
           ('RIGHTPADDING', (0, 0), (-1, -1), 4),
           ('TOPPADDING', (0, 0), (-1, -1), 4),
           ('BOTTOMPADDING', (0, 0), (-1, -1), 4)]
    for i in range(1, len(f5b_data)):
        bg = colors.HexColor('#f3f2f1') if i % 2 == 1 else colors.white
        sc2.append(('BACKGROUND', (0, i), (-1, i), bg))
    t5b.setStyle(TableStyle(sc2))
    story.append(t5b)
    story.append(Spacer(1, 10))
    # Environmental checks
    story.append(Paragraph('Monthly Environmental Checks', s_form_section))
    f5c_header = ['Month', 'Smoke Detectors (Y/N)', 'Extinguisher (Y/N)',
                  'Hot Water (≤120°F)', 'Fridge (<40°F)', 'Staff Initials']
    f5c_th = ParagraphStyle('f5cth_st', fontName=BODY_BOLD, fontSize=8.5, leading=11,
                            textColor=colors.white, alignment=TA_CENTER)
    f5c_data = [[Paragraph(f'<b>{h}</b>', f5c_th) for h in f5c_header]]
    for m in ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']:
        f5c_data.append([Paragraph(m, s_td_sm),
                         *_fillable_data_cells(5, default_width=50, height=12, font_size=8)])
    f5c_widths = [0.10*AVAIL_W, 0.20*AVAIL_W, 0.18*AVAIL_W,
                  0.20*AVAIL_W, 0.16*AVAIL_W, 0.16*AVAIL_W]
    t5c = Table(f5c_data, colWidths=f5c_widths, hAlign='CENTER', repeatRows=1)
    sc3 = [('BACKGROUND', (0, 0), (-1, 0), HEADER_FILL),
           ('GRID', (0, 0), (-1, -1), 0.4, BORDER),
           ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
           ('LEFTPADDING', (0, 0), (-1, -1), 4),
           ('RIGHTPADDING', (0, 0), (-1, -1), 4),
           ('TOPPADDING', (0, 0), (-1, -1), 4),
           ('BOTTOMPADDING', (0, 0), (-1, -1), 4)]
    for i in range(1, len(f5c_data)):
        bg = colors.HexColor('#f3f2f1') if i % 2 == 1 else colors.white
        sc3.append(('BACKGROUND', (0, i), (-1, i), bg))
    t5c.setStyle(TableStyle(sc3))
    story.append(t5c)
    doc.build(story, onFirstPage=_draw_header_footer, onLaterPages=_draw_header_footer)


# ── Form 6: Employee SOP Acknowledgment ───────────────────────────────
def build_form_6(filepath):
    doc = _standalone_form_doc(filepath, 'Form 6 — Employee SOP Acknowledgment')
    story = []
    story.extend(_form_intro(
        6, 'Employee SOP Acknowledgment',
        'Part 3 · Form 6: Employee SOP Acknowledgment',
    ))
    story.append(fillable_meta_row([('Employee Name:', 320, 'Employee full name')]))
    story.append(Paragraph('<b>Title:</b>', s_form_meta))
    story.append(fillable_check_row([
        ('QP', 'Title: Qualified Professional'),
        ('AP', 'Title: Associate Professional'),
        ('Direct Care Professional', 'Title: Direct Care Professional'),
    ]))
    story.append(Spacer(1, 8))
    story.append(Paragraph(
        'By signing below, I acknowledge that I have received, read, and understand the '
        'SOP Manual for <b>Well Spring Intervention LLC</b> (Rev. 2.13, July 2026, '
        'RMDM-Compliant). I understand these policies are mandated by NC DHSR (10A NCAC '
        '27G), NC Medicaid (CCP 8C), Rule 108 (10A NCAC 27T), the NCDHHS Records '
        'Management and Documentation Manual (Effective July 8, 2025), NCGS Chapter 66 '
        'Article 40 (NC UETA) and the federal E-SIGN Act governing electronic signatures. '
        'I understand that the QP reports to the Clinical Director and is responsible for '
        'scheduling clinical services, assessments, PCPs, and day-to-day supervision of '
        'APs and DCPs according to the Clinical Director\'s direction, and provides '
        'recurring compliance reports to the Clinical Director as defined in §1.4 and '
        '§1.4(a). I acknowledge that QP credentialing requirements are specified in '
        '§1.4(b) per 10A NCAC 27G .0104. I agree to follow these protocols exactly, '
        'including the electronic-signature safeguards and system-unavailability '
        'procedures in §10.7. I understand failure to do so may result in disciplinary '
        'action, termination, or legal consequences regarding Medicaid fraud and '
        'regulatory non-compliance.',
        s_body
    ))
    story.append(Spacer(1, 20))
    story.append(fillable_signature_row([
        ('Employee Signature:', 260, 'Employee signature'),
        ('Date:', 100, 'Date signed'),
    ]))
    story.append(Spacer(1, 14))
    story.append(fillable_signature_row([
        ('QP / Supervisor Signature:', 260, 'QP or supervisor signature'),
        ('Date:', 100, 'Date signed by QP/supervisor'),
    ]))
    doc.build(story, onFirstPage=_draw_header_footer, onLaterPages=_draw_header_footer)


# ── Form 7: Full Service Note Template ────────────────────────────────
def build_form_7(filepath):
    doc = _standalone_form_doc(filepath, 'Form 7 — Full Service Note Template')
    story = []
    story.extend(_form_intro(
        7, 'Full Service Note Template (Mandatory)',
        'Part 3 · Form 7: Full Service Note Template',
        external_ref='RMDM Chapter 6 — Contents of a Full Service Note',
        instructions='This template must be used for all shift notes. Backdating is prohibited. '
                     'Photocopying or repeating notes verbatim from a prior date or another '
                     'individual\'s record is strictly prohibited. Click any cell in the '
                     'Content column to type.',
    ))
    story.append(Spacer(1, 4))
    f7_rows = [
        'Youth Name', 'Service Record # / MID', 'Date of Service', 'Type of Contact',
        'Place of Service', 'Shift / Coverage Hours', 'Staff Present (for ratios)',
        'Purpose / ISP Goal Addressed', 'Interventions Provided',
        'Effectiveness & Youth Response', 'Signature / Credentials / Date',
        'Late Entry (if applicable)',
    ]
    f7_th = ParagraphStyle('f7th_st', fontName=BODY_BOLD, fontSize=9, leading=12,
                           textColor=colors.white, alignment=TA_LEFT)
    f7_td_l = ParagraphStyle('f7tdl_st', fontName=BODY_BOLD, fontSize=9, leading=12,
                             textColor=TEXT_PRIMARY, alignment=TA_LEFT)
    f7_data = [[Paragraph('<b>Field</b>', f7_th), Paragraph('<b>Content</b>', f7_th)]]
    for label in f7_rows:
        field_tf = AcroTextField(width=AVAIL_W * 0.66, height=22,
                                 tooltip=f'Content for: {label}',
                                 font_size=9, border_style='underlined')
        f7_data.append([Paragraph(label, f7_td_l), field_tf])
    f7_widths = [0.32*AVAIL_W, 0.68*AVAIL_W]
    t7 = Table(f7_data, colWidths=f7_widths, hAlign='CENTER', repeatRows=1)
    sc7 = [('BACKGROUND', (0, 0), (-1, 0), HEADER_FILL),
           ('GRID', (0, 0), (-1, -1), 0.4, BORDER),
           ('VALIGN', (0, 0), (-1, -1), 'TOP'),
           ('LEFTPADDING', (0, 0), (-1, -1), 5),
           ('RIGHTPADDING', (0, 0), (-1, -1), 5),
           ('TOPPADDING', (0, 0), (-1, -1), 6),
           ('BOTTOMPADDING', (0, 0), (-1, -1), 6)]
    for i in range(1, len(f7_data)):
        bg = colors.HexColor('#f3f2f1') if i % 2 == 1 else colors.white
        sc7.append(('BACKGROUND', (0, i), (-1, i), bg))
    t7.setStyle(TableStyle(sc7))
    story.append(t7)
    doc.build(story, onFirstPage=_draw_header_footer, onLaterPages=_draw_header_footer)


# ── Form 8: Comprehensive Clinical Record Content Checklist ───────────
def build_form_8(filepath):
    doc = _standalone_form_doc(filepath, 'Form 8 — Comprehensive Clinical Record Content Checklist')
    story = []
    story.extend(_form_intro(
        8, 'Comprehensive Clinical Record Content Checklist',
        'Part 3 · Form 8: Comprehensive Clinical Record Content Checklist',
        external_ref='RMDM Chapter 2 — Full Clinical Service Records',
        instructions='To be maintained in each youth\'s chart and reviewed quarterly by the QP. '
                     'Mark each element Present (Y), Absent (N), or N/A, with date verified.',
    ))
    story.append(Spacer(1, 4))
    f8_elements = [
        'Treatment Consent', 'PCP Consent',
        'Restrictive Intervention Consent (if applicable)',
        'Emergency Care Consent', 'HIPAA Notice Acknowledgement',
        'Third-Party Release', 'ROI(s)',
        'Demographics (name, DOB, contact, etc.)',
        'Emergency Contact / Preferred Physician / Hospital',
        'Advance Directives (or notation of none)',
        'Medication Allergies / Adverse Reactions / None',
        'Health / Behavioral Health History',
        'DSM-5-TR Diagnosis / ICD-10', 'Medication Orders / MAR',
        'Lab Results (if applicable)',
        'Notification of Rights / Explanation',
        'Restrictive Intervention Documentation (if applicable)',
        'CCA (by licensed professional)', 'ASAM Level of Care (if SUD)',
        'PCP / Service Plan / Crisis Plan', 'Service Order (signed)',
        'Discharge Plan / Summary', 'Accounting of Disclosures Log',
        '42 CFR 2.22 Summary (for SUD)',
        'Guardianship / POA / Legal Documents',
        'Incoming/Outgoing Correspondence',
        'Service Notes (per shift, compliant)',
        'Incident Occurrence Notations (reports filed separately)',
    ]
    f8_header = ['Element', 'Present? (Y/N/Date)', 'Notes']
    f8_th = ParagraphStyle('f8th_st', fontName=BODY_BOLD, fontSize=8.5, leading=11,
                           textColor=colors.white, alignment=TA_LEFT)
    s_td = ParagraphStyle('f8td_st', fontName=BODY_FONT, fontSize=9, leading=12,
                          textColor=TEXT_PRIMARY, alignment=TA_LEFT)
    f8_data = [[Paragraph(f'<b>{h}</b>', f8_th) for h in f8_header]]
    for el in f8_elements:
        f8_data.append([
            Paragraph(el, s_td),
            AcroTextField(width=80, height=12, tooltip=f'Present? for: {el}',
                          font_size=8.5, border_style='underlined'),
            AcroTextField(width=140, height=12, tooltip=f'Notes for: {el}',
                          font_size=8.5, border_style='underlined'),
        ])
    f8_widths = [0.46*AVAIL_W, 0.22*AVAIL_W, 0.32*AVAIL_W]
    t8 = Table(f8_data, colWidths=f8_widths, hAlign='CENTER', repeatRows=1)
    sc8 = [('BACKGROUND', (0, 0), (-1, 0), HEADER_FILL),
           ('GRID', (0, 0), (-1, -1), 0.4, BORDER),
           ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
           ('LEFTPADDING', (0, 0), (-1, -1), 4),
           ('RIGHTPADDING', (0, 0), (-1, -1), 4),
           ('TOPPADDING', (0, 0), (-1, -1), 4),
           ('BOTTOMPADDING', (0, 0), (-1, -1), 4)]
    for i in range(1, len(f8_data)):
        bg = colors.HexColor('#f3f2f1') if i % 2 == 1 else colors.white
        sc8.append(('BACKGROUND', (0, i), (-1, i), bg))
    t8.setStyle(TableStyle(sc8))
    story.append(t8)
    story.append(Spacer(1, 8))
    story.append(fillable_signature_row([
        ('QP Quarterly Audit Signature:', 220, 'QP quarterly audit signature'),
        ('Date:', 100, 'Date of quarterly audit'),
    ]))
    doc.build(story, onFirstPage=_draw_header_footer, onLaterPages=_draw_header_footer)


# ── Form 9: Accounting of Disclosures Log ─────────────────────────────
def build_form_9(filepath):
    doc = _standalone_form_doc(filepath, 'Form 9 — Accounting of Disclosures Log')
    story = []
    story.extend(_form_intro(
        9, 'Accounting of Disclosures Log',
        'Part 3 · Form 9: Accounting of Disclosures Log',
        external_ref='RMDM Chapter 3 — Documentation Requirements when Disclosing Information',
        instructions='Maintain for minimum 6 years per HIPAA and RMDM requirements. One log per youth. '
                     'All disclosures of SUD treatment information must additionally comply with 42 CFR Part 2.',
    ))
    story.append(fillable_meta_row([
        ('Youth Name:', 200, 'Youth name'),
        ('Service Record # / MID:', 160, 'Service record number or MID'),
    ]))
    story.append(Spacer(1, 4))
    f9_header = ['Date of Disclosure', 'Recipient (Agency/Individual)', 'Purpose of Disclosure',
                 'Description of Info Disclosed', 'Disclosing Staff (Name/Title)', 'Authorization / Exception Basis']
    f9_th = ParagraphStyle('f9th_st', fontName=BODY_BOLD, fontSize=8, leading=10,
                           textColor=colors.white, alignment=TA_LEFT)
    f9_data = [[Paragraph(f'<b>{h}</b>', f9_th) for h in f9_header]]
    for _ in range(20):  # 20 rows in standalone version (vs 8 in manual) for ample capacity
        f9_data.append(_fillable_data_cells(6, default_width=80, height=22, font_size=8))
    f9_widths = [0.13*AVAIL_W, 0.20*AVAIL_W, 0.18*AVAIL_W,
                 0.20*AVAIL_W, 0.15*AVAIL_W, 0.14*AVAIL_W]
    t9 = Table(f9_data, colWidths=f9_widths, hAlign='CENTER', repeatRows=1)
    sc9 = [('BACKGROUND', (0, 0), (-1, 0), HEADER_FILL),
           ('GRID', (0, 0), (-1, -1), 0.4, BORDER),
           ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
           ('LEFTPADDING', (0, 0), (-1, -1), 4),
           ('RIGHTPADDING', (0, 0), (-1, -1), 4),
           ('TOPPADDING', (0, 0), (-1, -1), 8),
           ('BOTTOMPADDING', (0, 0), (-1, -1), 8)]
    for i in range(1, len(f9_data)):
        bg = colors.HexColor('#f3f2f1') if i % 2 == 1 else colors.white
        sc9.append(('BACKGROUND', (0, i), (-1, i), bg))
    t9.setStyle(TableStyle(sc9))
    story.append(t9)
    doc.build(story, onFirstPage=_draw_header_footer, onLaterPages=_draw_header_footer)


# ── Main ──────────────────────────────────────────────────────────────
def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    forms = [
        ('Form_1_Shift_Change_Awake_Night_Watch_Log.pdf', build_form_1),
        ('Form_2_Contraband_Belongings_Inventory.pdf', build_form_2),
        ('Form_3_Physical_Restraint_Debriefing_Checklist.pdf', build_form_3),
        ('Form_4_Home_Pass_Medicaid_Billing_Exclusion_Tracker.pdf', build_form_4),
        ('Form_5_Emergency_Drill_Environmental_Safety_Log.pdf', build_form_5),
        ('Form_6_Employee_SOP_Acknowledgment.pdf', build_form_6),
        ('Form_7_Full_Service_Note_Template.pdf', build_form_7),
        ('Form_8_Comprehensive_Clinical_Record_Content_Checklist.pdf', build_form_8),
        ('Form_9_Accounting_of_Disclosures_Log.pdf', build_form_9),
    ]
    print(f'Generating {len(forms)} standalone fillable forms in {OUTPUT_DIR}...')
    for filename, builder in forms:
        filepath = os.path.join(OUTPUT_DIR, filename)
        builder(filepath)
        size_kb = os.path.getsize(filepath) / 1024
        print(f'  ✓ {filename}  ({size_kb:.1f} KB)')
    print(f'Done. {len(forms)} forms generated.')


if __name__ == '__main__':
    main()
