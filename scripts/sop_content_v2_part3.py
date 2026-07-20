
# ────────────────────────────────────────────────────────────────────
# Content builders — Part 3: Forms & Logs (9 forms, RMDM-compliant)
# ────────────────────────────────────────────────────────────────────
from generate_sop import (
    part_divider, section_heading, ref_line, para, bullets,
    Paragraph, Spacer, AVAIL_W,
    ParagraphStyle, Table, TableStyle, colors, TA_LEFT, TA_CENTER,
    BODY_FONT, BODY_BOLD, BODY_ITAL,
    s_body, s_form_meta, s_form_instr, s_form_section,
    s_th, s_td, s_td_sm,
    HEADER_FILL, BORDER, ACCENT, TEXT_PRIMARY, TEXT_MUTED,
    TABLE_ROW_ODD, TABLE_ROW_EVEN,
    form_table,
)


def build_part3():
    story = []
    story.extend(part_divider(
        'PART 3',
        'Customized Forms & Logs',
        'The following nine forms and logs are the official documentation instruments for '
        'daily operations. Each form must be completed in ink or in the electronic record '
        'system, signed by the responsible staff member, and filed in the youth\'s chart or '
        'the facility\'s operational binder as indicated. Originals are retained per the '
        'record retention policy (12 years after the minor reaches age 18; 11 years for '
        'adults). Forms 7, 8, and 9 are new in Version 2.0 to address RMDM service-note, '
        'clinical-record-content, and disclosure-accounting requirements.',
    ))

    # ── FORM 1 ─────────────────────────────────────────────────────
    story.append(section_heading(1, 'Shift Change & Awake Night Watch Log'))
    story.append(ref_line(anchor='Part 3 &middot; Form 1: Shift Change &amp; Awake Night Watch Log'))
    story.append(Paragraph('<b>Facility:</b> Well Spring Intervention LLC   <b>Date:</b> __________________', s_form_meta))
    story.append(Paragraph('<b>Awake Overnight Room Checks (Every 15 Minutes)</b>', s_form_section))
    story.append(Paragraph('Instructions: Initial each box to verify you visually saw the youth breathing and in their bed.', s_form_instr))

    times = ['11:00 PM','11:15 PM','11:30 PM','11:45 PM',
             '12:00 AM','12:15 AM','12:30 AM','12:45 AM',
             '1:00 AM','1:15 AM','1:30 AM','1:45 AM',
             '2:00 AM','2:15 AM','2:30 AM','2:45 AM',
             '3:00 AM','3:15 AM','3:30 AM','3:45 AM',
             '4:00 AM','4:15 AM','4:30 AM','4:45 AM',
             '5:00 AM','5:15 AM','5:30 AM','5:45 AM',
             '6:00 AM','6:15 AM','6:30 AM','6:45 AM']
    col_widths = [0.18*AVAIL_W, 0.16*AVAIL_W, 0.16*AVAIL_W, 0.16*AVAIL_W, 0.16*AVAIL_W, 0.18*AVAIL_W]

    th = ParagraphStyle('f1th', fontName=BODY_BOLD, fontSize=8.5, leading=11, textColor=colors.white, alignment=TA_CENTER)
    td_t = ParagraphStyle('f1tdt', fontName=BODY_BOLD, fontSize=8, leading=10, textColor=TEXT_PRIMARY, alignment=TA_CENTER)
    data = [[Paragraph('<b>Time</b>', th),
             Paragraph('<b>Youth 1</b>', th),
             Paragraph('<b>Youth 2</b>', th),
             Paragraph('<b>Youth 3</b>', th),
             Paragraph('<b>Youth 4</b>', th),
             Paragraph('<b>Staff Initials</b>', th)]]
    for t in times:
        data.append([Paragraph(t, td_t), '', '', '', '', ''])

    t1 = Table(data, colWidths=col_widths, hAlign='CENTER', repeatRows=1)
    style_cmds = [
        ('BACKGROUND', (0, 0), (-1, 0), HEADER_FILL),
        ('GRID',       (0, 0), (-1, -1), 0.4, BORDER),
        ('VALIGN',     (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING',  (0, 0), (-1, -1), 3),
        ('RIGHTPADDING', (0, 0), (-1, -1), 3),
        ('TOPPADDING',   (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING',(0, 0), (-1, -1), 3),
    ]
    for i in range(1, len(data)):
        bg = TABLE_ROW_ODD if i % 2 == 1 else TABLE_ROW_EVEN
        style_cmds.append(('BACKGROUND', (0, i), (-1, i), bg))
    t1.setStyle(TableStyle(style_cmds))
    story.append(t1)
    story.append(Spacer(1, 10))
    story.append(Paragraph('<b>Shift Handoff Verification:</b> Controlled substance count verified.', s_form_meta))
    story.append(Paragraph('Off-Going Staff: ____________________________   On-Coming Staff: ____________________________', s_form_meta))

    # ── FORM 2 ─────────────────────────────────────────────────────
    story.append(Spacer(1, 14))
    story.append(section_heading(2, 'Contraband & Belongings Inventory'))
    story.append(ref_line(anchor='Part 3 &middot; Form 2: Contraband &amp; Belongings Inventory'))
    story.append(Paragraph('<b>Youth Name:</b> ____________________________   <b>Service Record # / MID:</b> _______________   <b>Date:</b> _______________', s_form_meta))
    story.append(Paragraph('<b>Search Type:</b>   [  ] Admission   [  ] Return from Pass   [  ] Probable Cause (QP Approval: ____________________)', s_form_meta))
    story.append(Spacer(1, 6))

    f2_header = ['Item Description', 'Quantity', 'Brought In / Found', 'Disposition (Kept / Safe / Guardian)', 'Staff Initials']
    f2_rows = [['', '', '', '', ''] for _ in range(6)]
    f2_widths = [0.32*AVAIL_W, 0.10*AVAIL_W, 0.18*AVAIL_W, 0.27*AVAIL_W, 0.13*AVAIL_W]
    story.append(form_table(
        [[Paragraph(f'<b>{h}</b>', s_th) for h in f2_header]] + f2_rows,
        f2_widths, has_header=True
    ))
    story.append(Spacer(1, 8))
    story.append(Paragraph('<b>Youth Acknowledgment:</b> Belongings inventoried in my presence.', s_form_meta))
    story.append(Paragraph('Youth Signature: ____________________________   Staff Signature: ____________________________', s_form_meta))

    # ── FORM 3 ─────────────────────────────────────────────────────
    story.append(Spacer(1, 14))
    story.append(section_heading(3, 'Physical Restraint & Debriefing Checklist'))
    story.append(ref_line(anchor='Part 3 &middot; Form 3: Physical Restraint &amp; Debriefing Checklist'))
    story.append(Paragraph('<b>Youth:</b> ____________________   <b>Service Record # / MID:</b> ___________   <b>Date:</b> ___________   <b>Time Started:</b> ________   <b>Time Ended:</b> ________', s_form_meta))
    story.append(Paragraph('<b>Total Duration (Min):</b> _______   <b>Technique:</b> __________________________', s_form_meta))
    story.append(Spacer(1, 6))

    story.append(Paragraph('Pre-Restraint De-escalation Attempts:', s_form_section))
    story.append(Paragraph('[  ] Verbal redirection   [  ] Offered break   [  ] Sensory item   [  ] BSP coping skill   [  ] Separation', s_form_meta))

    story.append(Paragraph('Reason for Restraint (Imminent danger):', s_form_section))
    story.append(Paragraph('[  ] Danger to Self   [  ] Danger to Others   [  ] Property destruction posing risk', s_form_meta))
    story.append(Paragraph('Describe objectively: _________________________________________________________________________', s_form_meta))
    story.append(Paragraph('_________________________________________________________________________________________________', s_form_meta))

    story.append(Paragraph('Post-Restraint Medical Check (Within 1 hour):', s_form_section))
    story.append(Paragraph('Youth checked for injuries, breathing normally:   [  ] Yes   [  ] No (Seek medical attention)', s_form_meta))
    story.append(Paragraph('Staff Signature: ____________________________________', s_form_meta))

    story.append(Paragraph('Notifications:', s_form_section))
    story.append(Paragraph('On-Call QP Notified:   [  ] Y   [  ] N   Time: _______    Guardian Notified:   [  ] Y   [  ] N   Time: _______', s_form_meta))
    story.append(Paragraph('IRIS Report Filed:   [  ] Y   [  ] N   IRIS ID #: ______________', s_form_meta))

    story.append(Paragraph('Post-Restraint Debriefing (Within 24 hours):', s_form_section))
    story.append(Paragraph('Youth debriefed by: ______________________   Date/Time: _______________', s_form_meta))
    story.append(Paragraph('Trigger? ___________________________________________________________________________________', s_form_meta))
    story.append(Paragraph('Youth alternative? _________________________________________________________________________', s_form_meta))
    story.append(Paragraph('Staff alternative? _________________________________________________________________________', s_form_meta))
    story.append(Paragraph('Youth Signature: ____________________________   QP Signature: ____________________________', s_form_meta))

    # ── FORM 4 ─────────────────────────────────────────────────────
    story.append(Spacer(1, 14))
    story.append(section_heading(4, 'Home Pass & Medicaid Billing Exclusion Tracker'))
    story.append(ref_line(anchor='Part 3 &middot; Form 4: Home Pass &amp; Medicaid Billing Exclusion Tracker'))
    story.append(Paragraph('<b>Youth:</b> ____________________________   <b>Service Record # / MID:</b> _______________   <b>Month/Year:</b> _______________', s_form_meta))
    story.append(Spacer(1, 6))

    f4_header = ['Date Left', 'Time Left', 'Destination / Pass', 'Date Returned', 'Time Returned', 'Total Hours Away', 'Billing Action (Suspension Days)', 'Staff Initials']
    f4_rows = [['', '', '', '', '', '', '', ''] for _ in range(4)]
    f4_widths = [0.10*AVAIL_W, 0.09*AVAIL_W, 0.18*AVAIL_W, 0.11*AVAIL_W, 0.11*AVAIL_W, 0.12*AVAIL_W, 0.18*AVAIL_W, 0.11*AVAIL_W]
    f4_th = ParagraphStyle('f4th', fontName=BODY_BOLD, fontSize=8, leading=10, textColor=colors.white, alignment=TA_CENTER)
    story.append(form_table(
        [[Paragraph(f'<b>{h}</b>', f4_th) for h in f4_header]] + f4_rows,
        f4_widths, has_header=True
    ))
    story.append(Spacer(1, 8))
    story.append(Paragraph('<b>Billing Coordinator Sign-Off:</b> Medicaid billing adjusted for suspension days.', s_form_meta))
    story.append(Paragraph('Signature: ____________________________   Date: ______________', s_form_meta))

    # ── FORM 5 ─────────────────────────────────────────────────────
    story.append(Spacer(1, 14))
    story.append(section_heading(5, 'Emergency Drill & Environmental Safety Log'))
    story.append(ref_line(anchor='Part 3 &middot; Form 5: Emergency Drill &amp; Environmental Safety Log'))
    story.append(Paragraph('<b>Facility:</b> Well Spring Intervention LLC', s_form_meta))
    story.append(Spacer(1, 6))

    story.append(Paragraph('Monthly Fire Drills (Under 3 minutes)', s_form_section))
    f5a_header = ['Month', 'Date', 'Time of Day', '# Youth', 'Evac Time', 'Staff', 'Signature']
    f5a_th = ParagraphStyle('f5th', fontName=BODY_BOLD, fontSize=8.5, leading=11, textColor=colors.white, alignment=TA_CENTER)
    f5a_data = [[Paragraph(f'<b>{h}</b>', f5a_th) for h in f5a_header]]
    for month_label in ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']:
        f5a_data.append([Paragraph(month_label, s_td_sm), '', '', '', '', '', ''])
    f5a_widths = [0.10*AVAIL_W, 0.14*AVAIL_W, 0.16*AVAIL_W, 0.12*AVAIL_W, 0.14*AVAIL_W, 0.16*AVAIL_W, 0.18*AVAIL_W]
    t5a = Table(f5a_data, colWidths=f5a_widths, hAlign='CENTER', repeatRows=1)
    sc = [
        ('BACKGROUND', (0, 0), (-1, 0), HEADER_FILL),
        ('GRID',       (0, 0), (-1, -1), 0.4, BORDER),
        ('VALIGN',     (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING',  (0, 0), (-1, -1), 4),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4),
        ('TOPPADDING',   (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING',(0, 0), (-1, -1), 4),
    ]
    for i in range(1, len(f5a_data)):
        bg = TABLE_ROW_ODD if i % 2 == 1 else TABLE_ROW_EVEN
        sc.append(('BACKGROUND', (0, i), (-1, i), bg))
    t5a.setStyle(TableStyle(sc))
    story.append(t5a)

    story.append(Spacer(1, 10))
    story.append(Paragraph('Quarterly Tornado Drills', s_form_section))
    f5b_header = ['Quarter', 'Date', '# Youth', 'Staff', 'Signature']
    f5b_th = ParagraphStyle('f5bth', fontName=BODY_BOLD, fontSize=8.5, leading=11, textColor=colors.white, alignment=TA_CENTER)
    f5b_data = [[Paragraph(f'<b>{h}</b>', f5b_th) for h in f5b_header]]
    for q in ['Q1','Q2','Q3','Q4']:
        f5b_data.append([Paragraph(q, s_td_sm), '', '', '', ''])
    f5b_widths = [0.14*AVAIL_W, 0.20*AVAIL_W, 0.18*AVAIL_W, 0.20*AVAIL_W, 0.28*AVAIL_W]
    t5b = Table(f5b_data, colWidths=f5b_widths, hAlign='CENTER', repeatRows=1)
    sc2 = [
        ('BACKGROUND', (0, 0), (-1, 0), HEADER_FILL),
        ('GRID',       (0, 0), (-1, -1), 0.4, BORDER),
        ('VALIGN',     (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING',  (0, 0), (-1, -1), 4),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4),
        ('TOPPADDING',   (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING',(0, 0), (-1, -1), 4),
    ]
    for i in range(1, len(f5b_data)):
        bg = TABLE_ROW_ODD if i % 2 == 1 else TABLE_ROW_EVEN
        sc2.append(('BACKGROUND', (0, i), (-1, i), bg))
    t5b.setStyle(TableStyle(sc2))
    story.append(t5b)

    story.append(Spacer(1, 10))
    story.append(Paragraph('Monthly Environmental Checks', s_form_section))
    f5c_header = ['Month', 'Smoke Detectors (Y/N)', 'Extinguisher (Y/N)', 'Hot Water (≤120°F)', 'Fridge (<40°F)', 'Staff Initials']
    f5c_th = ParagraphStyle('f5cth', fontName=BODY_BOLD, fontSize=8.5, leading=11, textColor=colors.white, alignment=TA_CENTER)
    f5c_data = [[Paragraph(f'<b>{h}</b>', f5c_th) for h in f5c_header]]
    for m in ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']:
        f5c_data.append([Paragraph(m, s_td_sm), '', '', '', '', ''])
    f5c_widths = [0.10*AVAIL_W, 0.20*AVAIL_W, 0.18*AVAIL_W, 0.20*AVAIL_W, 0.16*AVAIL_W, 0.16*AVAIL_W]
    t5c = Table(f5c_data, colWidths=f5c_widths, hAlign='CENTER', repeatRows=1)
    sc3 = [
        ('BACKGROUND', (0, 0), (-1, 0), HEADER_FILL),
        ('GRID',       (0, 0), (-1, -1), 0.4, BORDER),
        ('VALIGN',     (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING',  (0, 0), (-1, -1), 4),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4),
        ('TOPPADDING',   (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING',(0, 0), (-1, -1), 4),
    ]
    for i in range(1, len(f5c_data)):
        bg = TABLE_ROW_ODD if i % 2 == 1 else TABLE_ROW_EVEN
        sc3.append(('BACKGROUND', (0, i), (-1, i), bg))
    t5c.setStyle(TableStyle(sc3))
    story.append(t5c)

    # ── FORM 6 ─────────────────────────────────────────────────────
    story.append(Spacer(1, 14))
    story.append(section_heading(6, 'Employee SOP Acknowledgment'))
    story.append(ref_line(anchor='Part 3 &middot; Form 6: Employee SOP Acknowledgment'))
    story.append(Paragraph('<b>Employee Name:</b> _____________________________________________', s_form_meta))
    story.append(Paragraph('<b>Title:</b>   [  ] QP   [  ] AP   [  ] Direct Care Professional', s_form_meta))
    story.append(Spacer(1, 8))
    story.append(Paragraph(
        'By signing below, I acknowledge that I have received, read, and understand the '
        'SOP Manual for <b>Well Spring Intervention LLC</b> (Rev. 2.5, July 2026, '
        'RMDM-Compliant). I understand these policies are mandated by NC DHSR (10A NCAC '
        '27G), NC Medicaid (CCP 8C), Rule 108 (10A NCAC 27T), the NCDHHS Records '
        'Management and Documentation Manual (Effective July 8, 2025), NCGS Chapter 66 '
        'Article 40 (NC UETA) and the federal E-SIGN Act governing electronic signatures. '
        'I understand that the QP reports to the Clinical Director and is responsible for '
        'scheduling clinical services, assessments, PCPs, and day-to-day supervision of '
        'APs and DCPs according to the Clinical Director\'s direction, and provides '
        'recurring compliance reports to the Clinical Director as defined in §1.4 and '
        '§1.4(a). I acknowledge that QP credentialing requirements are specified in '
        '§1.4(b) per 10A NCAC 27G .0104 — there are two acceptable pathways: Pathway 1 '
        '(master\'s degree + recognized NC credential + 1 year post-master\'s supervised '
        'MH/DD/SA experience) or Pathway 2 (bachelor\'s degree + 2 years full-time pre- '
        'or post-bachelor\'s supervised MH/DD/SA experience); a QP is not required to '
        'hold a full, unrestricted clinical license. I agree to follow these protocols '
        'exactly, including the electronic-signature safeguards and system-unavailability '
        'procedures in §10.7. I understand failure to do so may result in disciplinary '
        'action, termination, or legal consequences regarding Medicaid fraud and '
        'regulatory non-compliance.',
        s_body
    ))
    story.append(Spacer(1, 20))
    story.append(Paragraph('<b>Employee Signature:</b> ____________________________________   <b>Date:</b> _______________', s_form_meta))
    story.append(Spacer(1, 14))
    story.append(Paragraph('<b>QP / Supervisor Signature:</b> ______________________________   <b>Date:</b> _______________', s_form_meta))

    # ── FORM 7 ─────────────────────────────────────────────────────
    story.append(Spacer(1, 14))
    story.append(section_heading(7, 'Full Service Note Template (Mandatory)'))
    story.append(ref_line(
        'RMDM Chapter 6 — Contents of a Full Service Note',
        'Part 3 &middot; Form 7: Full Service Note Template',
    ))
    story.append(Paragraph(
        'This template must be used for all shift notes. Backdating is prohibited. '
        'Photocopying or repeating notes verbatim from a prior date or another '
        'individual\'s record is strictly prohibited.',
        s_form_instr
    ))
    story.append(Spacer(1, 4))

    f7_rows = [
        ['Youth Name', '[Last, First]'],
        ['Service Record # / MID', '[Record # / MID]'],
        ['Date of Service', '[MM/DD/YYYY]'],
        ['Service Name', 'Level 3 Residential — Shift'],
        ['Type of Contact', '[ ] In-person   [ ] Telehealth   [ ] Telephonic   [ ] Collateral'],
        ['Place of Service', '[Facility Address / Location]'],
        ['Shift / Coverage Hours', '[e.g., Day Shift 7a-3p]'],
        ['Staff Present (for ratios)', '[List all staff names/titles on shift]'],
        ['Purpose / ISP Goal Addressed', '[Reference specific ISP/PCP goal # and objective]'],
        ['Interventions Provided', '[Objective, factual description of interventions, supports, activities, and de-escalation attempts if any]'],
        ['Effectiveness & Youth Response', '[Specific, individualized description of youth\'s response and progress toward goal]'],
        ['Signature / Credentials / Date', '[Full signature, credentials, and date authenticated]'],
        ['Late Entry (if applicable)', '[Late Entry made on ____ for service on ____]'],
    ]
    f7_th = ParagraphStyle('f7th', fontName=BODY_BOLD, fontSize=9, leading=12, textColor=colors.white, alignment=TA_LEFT)
    f7_td_l = ParagraphStyle('f7tdl', fontName=BODY_BOLD, fontSize=9, leading=12, textColor=TEXT_PRIMARY, alignment=TA_LEFT)
    f7_td_r = ParagraphStyle('f7tdr', fontName=BODY_FONT, fontSize=9, leading=12, textColor=TEXT_PRIMARY, alignment=TA_LEFT)
    f7_data = [[Paragraph('<b>Field</b>', f7_th), Paragraph('<b>Content</b>', f7_th)]]
    for label, content in f7_rows:
        f7_data.append([Paragraph(label, f7_td_l), Paragraph(content, f7_td_r)])
    f7_widths = [0.32*AVAIL_W, 0.68*AVAIL_W]
    t7 = Table(f7_data, colWidths=f7_widths, hAlign='CENTER', repeatRows=1)
    sc7 = [
        ('BACKGROUND', (0, 0), (-1, 0), HEADER_FILL),
        ('GRID',       (0, 0), (-1, -1), 0.4, BORDER),
        ('VALIGN',     (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING',  (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
        ('TOPPADDING',   (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING',(0, 0), (-1, -1), 6),
    ]
    for i in range(1, len(f7_data)):
        bg = TABLE_ROW_ODD if i % 2 == 1 else TABLE_ROW_EVEN
        sc7.append(('BACKGROUND', (0, i), (-1, i), bg))
    t7.setStyle(TableStyle(sc7))
    story.append(t7)

    # ── FORM 8 ─────────────────────────────────────────────────────
    story.append(Spacer(1, 14))
    story.append(section_heading(8, 'Comprehensive Clinical Record Content Checklist'))
    story.append(ref_line(
        'RMDM Chapter 2 — Full Clinical Service Records',
        'Part 3 &middot; Form 8: Comprehensive Clinical Record Content Checklist',
    ))
    story.append(Paragraph(
        'To be maintained in each youth\'s chart and reviewed quarterly by the QP. '
        'Mark each element Present (Y), Absent (N), or N/A, with date verified.',
        s_form_instr
    ))
    story.append(Spacer(1, 4))

    f8_elements = [
        'Treatment Consent',
        'PCP Consent',
        'Restrictive Intervention Consent (if applicable)',
        'Emergency Care Consent',
        'HIPAA Notice Acknowledgement',
        'Third-Party Release',
        'ROI(s)',
        'Demographics (name, DOB, contact, etc.)',
        'Emergency Contact / Preferred Physician / Hospital',
        'Advance Directives (or notation of none)',
        'Medication Allergies / Adverse Reactions / None',
        'Health / Behavioral Health History',
        'DSM-5-TR Diagnosis / ICD-10',
        'Medication Orders / MAR',
        'Lab Results (if applicable)',
        'Notification of Rights / Explanation',
        'Restrictive Intervention Documentation (if applicable)',
        'CCA (by licensed professional)',
        'ASAM Level of Care (if SUD)',
        'PCP / Service Plan / Crisis Plan',
        'Service Order (signed)',
        'Discharge Plan / Summary',
        'Accounting of Disclosures Log',
        '42 CFR 2.22 Summary (for SUD)',
        'Guardianship / POA / Legal Documents',
        'Incoming/Outgoing Correspondence',
        'Service Notes (per shift, compliant)',
        'Incident Occurrence Notations (reports filed separately)',
    ]
    f8_header = ['Element', 'Present? (Y/N/Date)', 'Notes']
    f8_th = ParagraphStyle('f8th', fontName=BODY_BOLD, fontSize=8.5, leading=11, textColor=colors.white, alignment=TA_LEFT)
    f8_data = [[Paragraph(f'<b>{h}</b>', f8_th) for h in f8_header]]
    for el in f8_elements:
        f8_data.append([Paragraph(el, s_td), '', ''])
    f8_widths = [0.46*AVAIL_W, 0.22*AVAIL_W, 0.32*AVAIL_W]
    t8 = Table(f8_data, colWidths=f8_widths, hAlign='CENTER', repeatRows=1)
    sc8 = [
        ('BACKGROUND', (0, 0), (-1, 0), HEADER_FILL),
        ('GRID',       (0, 0), (-1, -1), 0.4, BORDER),
        ('VALIGN',     (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING',  (0, 0), (-1, -1), 4),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4),
        ('TOPPADDING',   (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING',(0, 0), (-1, -1), 4),
    ]
    for i in range(1, len(f8_data)):
        bg = TABLE_ROW_ODD if i % 2 == 1 else TABLE_ROW_EVEN
        sc8.append(('BACKGROUND', (0, i), (-1, i), bg))
    t8.setStyle(TableStyle(sc8))
    story.append(t8)
    story.append(Spacer(1, 8))
    story.append(Paragraph('<b>QP Quarterly Audit Signature:</b> ____________________________   <b>Date:</b> _______________', s_form_meta))

    # ── FORM 9 ─────────────────────────────────────────────────────
    story.append(Spacer(1, 14))
    story.append(section_heading(9, 'Accounting of Disclosures Log'))
    story.append(ref_line(
        'RMDM Chapter 3 — Documentation Requirements when Disclosing Information',
        'Part 3 &middot; Form 9: Accounting of Disclosures Log',
    ))
    story.append(Paragraph(
        'Maintain for minimum 6 years per HIPAA and RMDM requirements. One log per youth. '
        'All disclosures of SUD treatment information must additionally comply with '
        '42 CFR Part 2.',
        s_form_instr
    ))
    story.append(Paragraph('<b>Youth Name:</b> ____________________________   <b>Service Record # / MID:</b> _______________', s_form_meta))
    story.append(Spacer(1, 4))

    f9_header = ['Date of Disclosure', 'Recipient (Agency/Individual)', 'Purpose of Disclosure', 'Description of Info Disclosed', 'Disclosing Staff (Name/Title)', 'Authorization / Exception Basis']
    f9_th = ParagraphStyle('f9th', fontName=BODY_BOLD, fontSize=8, leading=10, textColor=colors.white, alignment=TA_LEFT)
    f9_data = [[Paragraph(f'<b>{h}</b>', f9_th) for h in f9_header]]
    for _ in range(8):
        f9_data.append(['', '', '', '', '', ''])
    f9_widths = [0.13*AVAIL_W, 0.20*AVAIL_W, 0.18*AVAIL_W, 0.20*AVAIL_W, 0.15*AVAIL_W, 0.14*AVAIL_W]
    t9 = Table(f9_data, colWidths=f9_widths, hAlign='CENTER', repeatRows=1)
    sc9 = [
        ('BACKGROUND', (0, 0), (-1, 0), HEADER_FILL),
        ('GRID',       (0, 0), (-1, -1), 0.4, BORDER),
        ('VALIGN',     (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING',  (0, 0), (-1, -1), 4),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4),
        ('TOPPADDING',   (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING',(0, 0), (-1, -1), 8),
    ]
    for i in range(1, len(f9_data)):
        bg = TABLE_ROW_ODD if i % 2 == 1 else TABLE_ROW_EVEN
        sc9.append(('BACKGROUND', (0, i), (-1, i), bg))
    t9.setStyle(TableStyle(sc9))
    story.append(t9)

    # ── Version History ────────────────────────────────────────────
    story.append(Spacer(1, 18))
    story.append(section_heading(10, 'Version History'))
    story.append(ref_line(anchor='Part 3 &middot; Version History'))
    vh_header = ['Version', 'Date', 'Summary of Changes', 'Author']
    vh_rows = [
        ['1.0', 'Jan 2026', 'Original SOP.', 'Executive Director / QP'],
        ['2.0', 'Jul 2026',
         'Updated to full RMDM (July 2025) compliance: Added CDW/data reporting (§1.5); revised record retention to 12 years post-majority (§1.6); added CCA requirements & ASAM (§4.1); added medical necessity (§4.2); added service orders incl. verbal/72-hour (§4.4); added service authorization (§4.5); expanded service note content (§10.1-10.4); added alterations policy (§10.5); added authentication incl. initials/ADA/rubber stamps (§10.6); added administrative closure (§3.5); added accounting of disclosures (§11.4); added privacy/security/42 CFR Part 2 (§11); added individual access (§11.5); added transporting records (§11.6); added grids/modified notes (§10.4); added TB screening (§6.2); added comprehensive clinical record checklist (Form 8); added Full Service Note Template (Form 7); added Accounting of Disclosures Log (Form 9); added Protocol 20 (Service Orders & Auth) and Protocol 21 (Record Management).',
         'Executive Director / QP'],
        ['2.1', 'Jul 2026',
         'Auditor recommendation: Added §10.7 Electronic Signatures policy explicitly referencing NCGS Chapter 66, Article 40 (NC Uniform Electronic Transactions Act) and the federal E-SIGN Act (15 U.S.C. § 7001 et seq.). §10.7(a) specifies required administrative, technical, and physical safeguards (unique credentials, MFA, session timeout, TLS/encryption, immutable audit trails, RBAC, immediate revocation, annual review). §10.7(b) establishes System Unavailability Procedures, including paper-fallback handwritten signatures with date/credentials, QP-declared Documentation Continuity Event, 72-hour transcription into EHR with late-entry notation, paper source-document retention, 7-business-day QP review for delayed transcription, and a Documentation Continuity Event log. Prior §10.7 Service Authorizations and §10.8 Billing renumbered to §10.8 and §10.9 respectively.',
         'Executive Director / QP'],
        ['2.2', 'Jul 2026',
         'Organizational clarification: §1.4 rewritten to separate the Clinical Director role (overall clinical program responsibility) from the Qualified Professional (QP) role. The QP now reports to the Clinical Director, supervises staff according to the Clinical Director\'s direction, and escalates clinical, staffing, and quality-of-care concerns. New §1.4(a) QP Compliance Reporting to the Clinical Director defines seven recurring compliance report types: monthly service-note audit summaries, monthly IRIS incident-report status, quarterly Clinical Record Content Checklist audits (Form 8), quarterly Accounting of Disclosures reviews (Form 9), quarterly personnel-file audits, annual electronic-signature safeguard review (§10.7(a)), and ad-hoc immediate reporting of breaches, complaints, licensing visits, and Medicaid audits. Clinical Director signs acknowledgment of each report and directs corrective action.',
         'Executive Director / QP'],
        ['2.3', 'Jul 2026',
         'QP responsibilities clarification: §1.4 updated to explicitly include "scheduling" as a QP responsibility. The QP is now responsible for scheduling clinical services, assessments, and PCPs (in addition to clinical services, assessments, PCPs themselves and day-to-day AP/DCP supervision), according to the direction of the Clinical Director. Aligns the SOP with the operational reality that the QP coordinates and schedules all clinical appointments, assessment windows, and Person-Centered Plan meetings for each youth in care.',
         'Executive Director / QP'],
        ['2.4', 'Jul 2026',
         'QP credentialing correction (10A NCAC 27G .0104): New §1.4(b) QP Credentialing Requirements added — specifies that a QP is NOT required to hold a full, unrestricted clinical license, but a bachelor\'s degree alone is not sufficient. Acceptable NC credentials listed across four categories: (i) full clinical license (LCSW, LPC, LMFT, Licensed Psychologist, LPA, psychiatrist MD/DO); (ii) associate/provisional license (LCSW-A, LPC-A, LMFT-A, LCAS-P); (iii) certification (LCAS, CCS with master\'s, CMSW); or (iv) psychiatric nursing credential (CNS or NP with psychiatric/mental health certification). Plus master\'s degree in human services, plus one year of full-time post-master\'s supervised experience, plus NC-DHHS QP training modules. QP must report any lapse/sanction/restriction to the Clinical Director within one business day. §2.2 Staff Qualifications QP bullet updated to match (previous bullet incorrectly stated "Master\'s or Bachelor\'s degree... licensed or license-eligible" — a bachelor\'s degree alone is not 27G .0104-compliant).',
         'Executive Director / QP'],
        ['2.5', 'Jul 2026',
         'QP credentialing correction (continued): Rev. 2.4 incorrectly removed the bachelor\'s-degree pathway to QP status. Rev. 2.5 restores BOTH pathways per 10A NCAC 27G .0104: §1.4(b) restructured into Pathway 1 (master\'s degree in human services + recognized NC credential [full license / associate-provisional license / certification / psychiatric nursing credential] + 1 year full-time post-master\'s supervised MH/DD/SA experience) AND Pathway 2 (bachelor\'s degree in a human services field + 2 years full-time pre- or post-bachelor\'s supervised MH/DD/SA experience, documented by supervising QP, with practice under clinical supervision of a Pathway 1 QP or the Clinical Director until NC-DHHS QP training is completed). Common Requirements subsection added covering QP training, lapse/sanction reporting, personnel-file verification, and annual re-verification of pathway. §2.2 QP bullet updated to list both pathways.',
         'Executive Director / QP'],
    ]
    vh_th = ParagraphStyle('vhth', fontName=BODY_BOLD, fontSize=9, leading=11, textColor=colors.white, alignment=TA_LEFT)
    vh_td = ParagraphStyle('vhtd', fontName=BODY_FONT, fontSize=8.5, leading=11, textColor=TEXT_PRIMARY, alignment=TA_LEFT)
    vh_td_b = ParagraphStyle('vhtdb', fontName=BODY_BOLD, fontSize=8.5, leading=11, textColor=TEXT_PRIMARY, alignment=TA_LEFT)
    vh_data = [[Paragraph(f'<b>{h}</b>', vh_th) for h in vh_header]]
    for row in vh_rows:
        vh_data.append([
            Paragraph(row[0], vh_td_b),
            Paragraph(row[1], vh_td),
            Paragraph(row[2], vh_td),
            Paragraph(row[3], vh_td),
        ])
    vh_widths = [0.08*AVAIL_W, 0.10*AVAIL_W, 0.62*AVAIL_W, 0.20*AVAIL_W]
    tvh = Table(vh_data, colWidths=vh_widths, hAlign='CENTER', repeatRows=1)
    scvh = [
        ('BACKGROUND', (0, 0), (-1, 0), HEADER_FILL),
        ('GRID',       (0, 0), (-1, -1), 0.4, BORDER),
        ('VALIGN',     (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING',  (0, 0), (-1, -1), 4),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4),
        ('TOPPADDING',   (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING',(0, 0), (-1, -1), 5),
    ]
    for i in range(1, len(vh_data)):
        bg = TABLE_ROW_ODD if i % 2 == 1 else TABLE_ROW_EVEN
        scvh.append(('BACKGROUND', (0, i), (-1, i), bg))
    tvh.setStyle(TableStyle(scvh))
    story.append(tvh)

    return story
