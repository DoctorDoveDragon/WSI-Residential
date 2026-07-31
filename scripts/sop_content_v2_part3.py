
# ────────────────────────────────────────────────────────────────────
# Content builders — Part 3: Forms & Logs (9 forms, RMDM-compliant)
# All forms are interactive AcroForm fillable PDFs: printable, copyable,
# sharable, editable, and fillable. Each form opens with a Form Properties
# banner documenting this. Standalone fillable copies are also generated
# into /home/z/my-project/download/forms/ by build_fillable_forms.py.
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
    AcroTextField, AcroCheckbox,
    fillable_meta_row, fillable_check_row, fillable_signature_row,
    form_usage_banner,
)


def _form_banner_and_heading(form_num, title, anchor_text, external_ref=None,
                             instructions=None):
    """Emit section_heading + ref_line + form_usage_banner + optional
    instructions paragraph. Used as the standard opening for every form."""
    out = [
        section_heading(form_num, title),
        ref_line(external=external_ref, anchor=anchor_text),
        form_usage_banner(form_num),
        Spacer(1, 6),
    ]
    if instructions:
        out.append(Paragraph(instructions, s_form_instr))
        out.append(Spacer(1, 4))
    return out


def _fillable_data_cells(num_cells, default_width=60, height=13, font_size=8.5,
                         tooltips=None):
    """Return a list of AcroTextField flowables for use as table row cells.
    Width is generous; the Table column width will constrain via wrap()."""
    cells = []
    for i in range(num_cells):
        tip = tooltips[i] if tooltips and i < len(tooltips) else ''
        cells.append(AcroTextField(
            width=default_width, height=height,
            tooltip=tip, font_size=font_size,
            border_style='solid', border_width=0,
        ))
    return cells


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
        'clinical-record-content, and disclosure-accounting requirements. As of Rev. 2.16, '
        'all nine forms are interactive AcroForm fillable PDFs — they are printable, '
        'copyable, sharable, editable, and fillable. A Form Properties banner at the top '
        'of each form documents these capabilities, and standalone fillable copies are '
        'available in the /download/forms/ directory for use outside this manual.',
    ))

    # ── FORM 1 ─────────────────────────────────────────────────────
    story.extend(_form_banner_and_heading(
        1, 'Shift Change & Awake Night Watch Log',
        'Part 3 &middot; Form 1: Shift Change &amp; Awake Night Watch Log',
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

    th = ParagraphStyle('f1th', fontName=BODY_BOLD, fontSize=8.5, leading=11, textColor=colors.white, alignment=TA_CENTER)
    td_t = ParagraphStyle('f1tdt', fontName=BODY_BOLD, fontSize=8, leading=10, textColor=TEXT_PRIMARY, alignment=TA_CENTER)
    data = [[Paragraph('<b>Time</b>', th),
             Paragraph('<b>Youth 1</b>', th),
             Paragraph('<b>Youth 2</b>', th),
             Paragraph('<b>Youth 3</b>', th),
             Paragraph('<b>Youth 4</b>', th),
             Paragraph('<b>Staff Initials</b>', th)]]
    for t in times:
        data.append([
            Paragraph(t, td_t),
            *_fillable_data_cells(5, default_width=50, height=12, font_size=8),
        ])

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
    story.append(fillable_signature_row([
        ('Off-Going Staff:', 180, 'Off-going staff signature'),
        ('On-Coming Staff:', 180, 'On-coming staff signature'),
    ]))

    # ── Form 1 addendum: Per-Floor Walk-Through Certification (two-story facilities) ──
    story.append(Spacer(1, 12))
    story.append(Paragraph(
        '<b>Per-Floor Walk-Through Certification (Required for Two-Story / Multi-Level Facilities — §9.4(d))</b>',
        s_form_section,
    ))
    story.append(Paragraph(
        '<i>In addition to the 15-minute youth-by-youth visual checks above, the awake '
        'overnight DCP shall physically walk every floor on which youth are sleeping and '
        'initial the corresponding block. Single-story facilities write "N/A" across '
        'the Floor 2 row.</i>',
        s_form_meta,
    ))
    story.append(Spacer(1, 4))
    f1b_header = ['Time Block', 'Floor 1 — Walked (Initials)', 'Floor 2 — Walked (Initials)', 'Basement — Walked (Initials)', 'Notes / Anomalies']
    f1b_th = ParagraphStyle('f1bth', fontName=BODY_BOLD, fontSize=8.5, leading=11, textColor=colors.white, alignment=TA_CENTER)
    f1b_data = [[Paragraph(f'<b>{h}</b>', f1b_th) for h in f1b_header]]
    f1b_blocks = [
        ('11:00 PM – 1:00 AM',),
        ('1:00 AM – 3:00 AM',),
        ('3:00 AM – 5:00 AM',),
        ('5:00 AM – 7:00 AM',),
    ]
    for (tb,) in f1b_blocks:
        f1b_data.append([
            Paragraph(tb, s_td_sm),
            *_fillable_data_cells(4, default_width=80, height=18, font_size=8),
        ])
    f1b_widths = [0.20*AVAIL_W, 0.18*AVAIL_W, 0.18*AVAIL_W, 0.18*AVAIL_W, 0.26*AVAIL_W]
    t1b = Table(f1b_data, colWidths=f1b_widths, hAlign='CENTER', repeatRows=1)
    sc1b = [
        ('BACKGROUND', (0, 0), (-1, 0), HEADER_FILL),
        ('GRID',       (0, 0), (-1, -1), 0.4, BORDER),
        ('VALIGN',     (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING',  (0, 0), (-1, -1), 4),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4),
        ('TOPPADDING',   (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING',(0, 0), (-1, -1), 5),
    ]
    for i in range(1, len(f1b_data)):
        bg = TABLE_ROW_ODD if i % 2 == 1 else TABLE_ROW_EVEN
        sc1b.append(('BACKGROUND', (0, i), (-1, i), bg))
    t1b.setStyle(TableStyle(sc1b))
    story.append(t1b)

    # ── FORM 2 ─────────────────────────────────────────────────────
    story.append(Spacer(1, 14))
    story.extend(_form_banner_and_heading(
        2, 'Contraband & Belongings Inventory',
        'Part 3 &middot; Form 2: Contraband &amp; Belongings Inventory',
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
    story.append(fillable_meta_row([
        ('QP Approval:', 250, 'QP approval for probable-cause search'),
    ]))
    story.append(Spacer(1, 6))

    f2_header = ['Item Description', 'Quantity', 'Brought In / Found', 'Disposition (Kept / Safe / Guardian)', 'Staff Initials']
    f2_rows = [_fillable_data_cells(5, default_width=60, height=14, font_size=9)
               for _ in range(6)]
    f2_widths = [0.32*AVAIL_W, 0.10*AVAIL_W, 0.18*AVAIL_W, 0.27*AVAIL_W, 0.13*AVAIL_W]
    story.append(form_table(
        [[Paragraph(f'<b>{h}</b>', s_th) for h in f2_header]] + f2_rows,
        f2_widths, has_header=True
    ))
    story.append(Spacer(1, 8))
    story.append(Paragraph('<b>Youth Acknowledgment:</b> Belongings inventoried in my presence.', s_form_meta))
    story.append(fillable_signature_row([
        ('Youth Signature:', 180, 'Youth signature'),
        ('Staff Signature:', 180, 'Staff signature'),
    ]))

    # ── FORM 3 ─────────────────────────────────────────────────────
    story.append(Spacer(1, 14))
    story.extend(_form_banner_and_heading(
        3, 'Physical Restraint & Debriefing Checklist',
        'Part 3 &middot; Form 3: Physical Restraint &amp; Debriefing Checklist',
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
    story.append(AcroTextField(width=AVAIL_W, height=28, tooltip='Objective description of incident',
                               font_size=9, border_style='underlined'))
    story.append(Spacer(1, 6))

    story.append(Paragraph('Post-Restraint Medical Check (Within 1 hour):', s_form_section))
    story.append(Paragraph('Youth checked for injuries, breathing normally:', s_form_meta))
    story.append(fillable_check_row([
        ('Yes', 'Medical check: yes'),
        ('No (Seek medical attention)', 'Medical check: no — seek medical attention'),
    ]))
    story.append(fillable_signature_row([
        ('Staff Signature:', 280, 'Staff signature for medical check'),
    ]))

    story.append(Paragraph('Notifications:', s_form_section))
    story.append(Paragraph('On-Call QP Notified:', s_form_meta))
    story.append(fillable_check_row([
        ('Y', 'On-call QP notified: yes'),
        ('N', 'On-call QP notified: no'),
    ]))
    story.append(fillable_meta_row([
        ('Time:', 80, 'Time QP notified'),
        ('Guardian Notified:', 0, ''),  # label only
    ]))
    story.append(fillable_check_row([
        ('Y', 'Guardian notified: yes'),
        ('N', 'Guardian notified: no'),
    ]))
    story.append(fillable_meta_row([
        ('Time:', 80, 'Time guardian notified'),
        ('IRIS Report Filed:', 0, ''),
    ]))
    story.append(fillable_check_row([
        ('Y', 'IRIS report filed: yes'),
        ('N', 'IRIS report filed: no'),
    ]))
    story.append(fillable_meta_row([
        ('IRIS ID #:', 200, 'IRIS report ID number'),
    ]))

    story.append(Paragraph('Post-Restraint Debriefing (Within 24 hours):', s_form_section))
    story.append(fillable_meta_row([
        ('Youth debriefed by:', 200, 'Name of person who debriefed youth'),
        ('Date/Time:', 120, 'Date and time of debriefing'),
    ]))
    story.append(Paragraph('Trigger?', s_form_meta))
    story.append(AcroTextField(width=AVAIL_W, height=20, tooltip='Trigger identified during debriefing',
                               font_size=9, border_style='underlined'))
    story.append(Paragraph('Youth alternative?', s_form_meta))
    story.append(AcroTextField(width=AVAIL_W, height=20, tooltip='Youth-identified alternative coping skill',
                               font_size=9, border_style='underlined'))
    story.append(Paragraph('Staff alternative?', s_form_meta))
    story.append(AcroTextField(width=AVAIL_W, height=20, tooltip='Staff-identified alternative intervention',
                               font_size=9, border_style='underlined'))
    story.append(fillable_signature_row([
        ('Youth Signature:', 180, 'Youth signature'),
        ('QP Signature:', 180, 'QP signature'),
    ]))

    # ── FORM 4 ─────────────────────────────────────────────────────
    story.append(Spacer(1, 14))
    story.extend(_form_banner_and_heading(
        4, 'Home Pass & Medicaid Billing Exclusion Tracker',
        'Part 3 &middot; Form 4: Home Pass &amp; Medicaid Billing Exclusion Tracker',
    ))
    story.append(fillable_meta_row([
        ('Youth:', 200, 'Youth name'),
        ('Service Record # / MID:', 120, 'Service record number or MID'),
        ('Month/Year:', 100, 'Month and year'),
    ]))
    story.append(Spacer(1, 6))

    f4_header = ['Date Left', 'Time Left', 'Destination / Pass', 'Date Returned', 'Time Returned', 'Total Hours Away', 'Billing Action (Suspension Days)', 'Staff Initials']
    f4_rows = [_fillable_data_cells(8, default_width=60, height=14, font_size=8)
               for _ in range(4)]
    f4_widths = [0.10*AVAIL_W, 0.09*AVAIL_W, 0.18*AVAIL_W, 0.11*AVAIL_W, 0.11*AVAIL_W, 0.12*AVAIL_W, 0.18*AVAIL_W, 0.11*AVAIL_W]
    f4_th = ParagraphStyle('f4th', fontName=BODY_BOLD, fontSize=8, leading=10, textColor=colors.white, alignment=TA_CENTER)
    story.append(form_table(
        [[Paragraph(f'<b>{h}</b>', f4_th) for h in f4_header]] + f4_rows,
        f4_widths, has_header=True
    ))
    story.append(Spacer(1, 8))
    story.append(Paragraph('<b>Billing Coordinator Sign-Off:</b> Medicaid billing adjusted for suspension days.', s_form_meta))
    story.append(fillable_signature_row([
        ('Signature:', 220, 'Billing coordinator signature'),
        ('Date:', 100, 'Date of sign-off'),
    ]))

    # ── FORM 5 ─────────────────────────────────────────────────────
    story.append(Spacer(1, 14))
    story.extend(_form_banner_and_heading(
        5, 'Emergency Drill & Environmental Safety Log',
        'Part 3 &middot; Form 5: Emergency Drill &amp; Environmental Safety Log',
    ))
    story.append(fillable_meta_row([
        ('Facility:', 280, 'Facility name'),
    ]))
    story.append(Spacer(1, 6))

    story.append(Paragraph('Monthly Fire Drills (Under 3 minutes)', s_form_section))
    f5a_header = ['Month', 'Date', 'Time of Day', '# Youth', 'Evac Time', 'Staff', 'Signature']
    f5a_th = ParagraphStyle('f5th', fontName=BODY_BOLD, fontSize=8.5, leading=11, textColor=colors.white, alignment=TA_CENTER)
    f5a_data = [[Paragraph(f'<b>{h}</b>', f5a_th) for h in f5a_header]]
    for month_label in ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']:
        f5a_data.append([
            Paragraph(month_label, s_td_sm),
            *_fillable_data_cells(6, default_width=50, height=12, font_size=8),
        ])
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
        f5b_data.append([
            Paragraph(q, s_td_sm),
            *_fillable_data_cells(4, default_width=60, height=12, font_size=8),
        ])
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
        f5c_data.append([
            Paragraph(m, s_td_sm),
            *_fillable_data_cells(5, default_width=50, height=12, font_size=8),
        ])
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

    # ── Form 5 addendum: Two-Story / Multi-Level Per-Floor Safety Checks (§9.4) ──
    story.append(Spacer(1, 10))
    story.append(Paragraph(
        '<b>Two-Story / Multi-Level Per-Floor Safety Checks (§9.4 — Required Monthly for Two-Story Facilities)</b>',
        s_form_section,
    ))
    story.append(Paragraph(
        '<i>Complete this sub-table each month for every facility with two or more '
        'stories. Single-story facilities write "N/A" across the Floor 2 / Basement '
        'rows. All checks must be Y (pass) or N (fail); any N requires immediate '
        'corrective action and escalation to the QP per §9.1.</i>',
        s_form_meta,
    ))
    story.append(Spacer(1, 4))
    f5d_header = [
        'Floor', 'Smoke Detectors (Y/N)', 'CO Detectors (Y/N)',
        'Extinguisher (Y/N)', 'Egress Window / Escape Ladder (Y/N)',
        'Window Restrictor ≤4 in (Y/N)', 'Stair Gate (Y/N)',
        'Staff Initials',
    ]
    f5d_th = ParagraphStyle('f5dth', fontName=BODY_BOLD, fontSize=8, leading=10, textColor=colors.white, alignment=TA_CENTER)
    f5d_data = [[Paragraph(f'<b>{h}</b>', f5d_th) for h in f5d_header]]
    for floor_label in ['Floor 1 (Ground)', 'Floor 2 (Upper)', 'Basement (if any)']:
        f5d_data.append([
            Paragraph(floor_label, s_td_sm),
            *_fillable_data_cells(7, default_width=42, height=14, font_size=8),
        ])
    f5d_widths = [
        0.14*AVAIL_W,  # Floor
        0.12*AVAIL_W,  # Smoke
        0.11*AVAIL_W,  # CO
        0.11*AVAIL_W,  # Extinguisher
        0.15*AVAIL_W,  # Egress
        0.14*AVAIL_W,  # Restrictor
        0.10*AVAIL_W,  # Stair gate
        0.13*AVAIL_W,  # Staff
    ]
    t5d = Table(f5d_data, colWidths=f5d_widths, hAlign='CENTER', repeatRows=1)
    sc4 = [
        ('BACKGROUND', (0, 0), (-1, 0), HEADER_FILL),
        ('GRID',       (0, 0), (-1, -1), 0.4, BORDER),
        ('VALIGN',     (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING',  (0, 0), (-1, -1), 3),
        ('RIGHTPADDING', (0, 0), (-1, -1), 3),
        ('TOPPADDING',   (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING',(0, 0), (-1, -1), 5),
    ]
    for i in range(1, len(f5d_data)):
        bg = TABLE_ROW_ODD if i % 2 == 1 else TABLE_ROW_EVEN
        sc4.append(('BACKGROUND', (0, i), (-1, i), bg))
    t5d.setStyle(TableStyle(sc4))
    story.append(t5d)

    # ── FORM 6 ─────────────────────────────────────────────────────
    story.append(Spacer(1, 14))
    story.extend(_form_banner_and_heading(
        6, 'Employee SOP Acknowledgment',
        'Part 3 &middot; Form 6: Employee SOP Acknowledgment',
    ))
    story.append(fillable_meta_row([
        ('Employee Name:', 320, 'Employee full name'),
    ]))
    story.append(Paragraph('<b>Title:</b>', s_form_meta))
    story.append(fillable_check_row([
        ('QP', 'Title: Qualified Professional'),
        ('AP', 'Title: Associate Professional'),
        ('Direct Care Professional', 'Title: Direct Care Professional'),
    ]))
    story.append(Spacer(1, 8))
    story.append(Paragraph(
        'By signing below, I acknowledge that I have received, read, and understand the '
        'SOP Manual for <b>Well Spring Intervention LLC</b> (Rev. 2.18, July 2026, '
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
    story.append(fillable_signature_row([
        ('Employee Signature:', 260, 'Employee signature'),
        ('Date:', 100, 'Date signed'),
    ]))
    story.append(Spacer(1, 14))
    story.append(fillable_signature_row([
        ('QP / Supervisor Signature:', 260, 'QP or supervisor signature'),
        ('Date:', 100, 'Date signed by QP/supervisor'),
    ]))

    # ── FORM 7 ─────────────────────────────────────────────────────
    story.append(Spacer(1, 14))
    story.extend(_form_banner_and_heading(
        7, 'Full Service Note Template (Mandatory)',
        'Part 3 &middot; Form 7: Full Service Note Template',
        external_ref='RMDM Chapter 6 — Contents of a Full Service Note',
        instructions='This template must be used for all shift notes. Backdating is prohibited. '
                     'Photocopying or repeating notes verbatim from a prior date or another '
                     'individual\'s record is strictly prohibited. Click any cell in the '
                     'Content column to type.',
    ))
    story.append(Spacer(1, 4))

    f7_rows = [
        'Youth Name',
        'Service Record # / MID',
        'Date of Service',
        'Type of Contact',
        'Place of Service',
        'Shift / Coverage Hours',
        'Staff Present (for ratios)',
        'Purpose / ISP Goal Addressed',
        'Interventions Provided',
        'Effectiveness & Youth Response',
        'Signature / Credentials / Date',
        'Late Entry (if applicable)',
    ]
    f7_th = ParagraphStyle('f7th', fontName=BODY_BOLD, fontSize=9, leading=12, textColor=colors.white, alignment=TA_LEFT)
    f7_td_l = ParagraphStyle('f7tdl', fontName=BODY_BOLD, fontSize=9, leading=12, textColor=TEXT_PRIMARY, alignment=TA_LEFT)
    f7_data = [[Paragraph('<b>Field</b>', f7_th), Paragraph('<b>Content</b>', f7_th)]]
    for label in f7_rows:
        # Service Name row removed (was hardcoded "Level 3 Residential — Shift");
        # now all rows are fillable.
        field_tf = AcroTextField(width=AVAIL_W * 0.66, height=18,
                                 tooltip=f'Content for: {label}',
                                 font_size=9, border_style='underlined')
        f7_data.append([Paragraph(label, f7_td_l), field_tf])
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
    story.extend(_form_banner_and_heading(
        8, 'Comprehensive Clinical Record Content Checklist',
        'Part 3 &middot; Form 8: Comprehensive Clinical Record Content Checklist',
        external_ref='RMDM Chapter 2 — Full Clinical Service Records',
        instructions='To be maintained in each youth\'s chart and reviewed quarterly by the QP. '
                     'Mark each element Present (Y), Absent (N), or N/A, with date verified. '
                     'Click any cell in the Present? or Notes columns to type.',
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
        f8_data.append([
            Paragraph(el, s_td),
            AcroTextField(width=80, height=12, tooltip=f'Present? for: {el}',
                          font_size=8.5, border_style='underlined'),
            AcroTextField(width=140, height=12, tooltip=f'Notes for: {el}',
                          font_size=8.5, border_style='underlined'),
        ])
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
    story.append(fillable_signature_row([
        ('QP Quarterly Audit Signature:', 220, 'QP quarterly audit signature'),
        ('Date:', 100, 'Date of quarterly audit'),
    ]))

    # ── FORM 9 ─────────────────────────────────────────────────────
    story.append(Spacer(1, 14))
    story.extend(_form_banner_and_heading(
        9, 'Accounting of Disclosures Log',
        'Part 3 &middot; Form 9: Accounting of Disclosures Log',
        external_ref='RMDM Chapter 3 — Documentation Requirements when Disclosing Information',
        instructions='Maintain for minimum 6 years per HIPAA and RMDM requirements. One log per youth. '
                     'All disclosures of SUD treatment information must additionally comply with '
                     '42 CFR Part 2. Click any cell to type.',
    ))
    story.append(fillable_meta_row([
        ('Youth Name:', 200, 'Youth name'),
        ('Service Record # / MID:', 160, 'Service record number or MID'),
    ]))
    story.append(Spacer(1, 4))

    f9_header = ['Date of Disclosure', 'Recipient (Agency/Individual)', 'Purpose of Disclosure', 'Description of Info Disclosed', 'Disclosing Staff (Name/Title)', 'Authorization / Exception Basis']
    f9_th = ParagraphStyle('f9th', fontName=BODY_BOLD, fontSize=8, leading=10, textColor=colors.white, alignment=TA_LEFT)
    f9_data = [[Paragraph(f'<b>{h}</b>', f9_th) for h in f9_header]]
    for _ in range(8):
        f9_data.append(_fillable_data_cells(6, default_width=80, height=20, font_size=8))
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
        ['2.6', 'Jul 2026',
         'Cover redesign: Added a symbolic cover illustration (rendered banner between the kicker and the entity title) evoking empowerment, growth, freedom, health, wholeness, and healing — visually framing the trauma-informed, restorative mission of the program. The illustration depicts a stylized tree-human figure rising toward a sunrise over calm water, rendered in a warm earthy palette (terracotta, warm brown, soft rose, cream) consistent with the manual\'s existing cascade palette. A small caption strip below the image reads "Empowerment · Growth · Freedom · Health · Wholeness · Healing". No body-content changes; §1.4(b) QP Credentialing Requirements (Pathway 1 and Pathway 2) and all other SOPs, protocols, and forms remain unchanged from Rev. 2.5.',
         'Executive Director / QP'],
        ['2.7', 'Jul 2026',
         'Cover redesign (continued): Cover is now a full-bleed brand illustration suitable for reuse across company websites, publications, and collateral materials. A new high-resolution 768×1344 portrait rendering of the tree-human-sunrise image fills the entire cover page. Overlay text is reduced to the essentials: company name (Playfair Display 72pt white with text-shadow), tagline ("Empowerment · Growth · Freedom · Health · Wholeness · Healing"), subtitle ("Level 3 Supervised Residential Group Home"), and a bottom document-identification panel (Doc. WSI-SOP-001, Effective July 2026, RMDM-Compliant, Owner, Revision 2.7). All descriptive content previously on the cover (full summary paragraph, Population/Served/Service Type/Effective Date/Owner meta block, and the Regulatory Framework reference block) is relocated to a new About This Manual page (p. 2 of the body, p. 3 of the final merged PDF) immediately preceding the Table of Contents. The About This Manual page also includes a Revision Lineage summary and a Cover Artwork note describing the brand visual\'s intended reuse. TOC page-number offset increased from +1 to +2 to account for the new inside page. Body content (SOPs, protocols, forms, §1.4(b) QP Credentialing Requirements) is unchanged from Rev. 2.6.',
         'Executive Director / QP'],
        ['2.8', 'Jul 2026',
         'Cover redesign (continued): Per organizational direction that versioning is private, all versioning information has been removed from the public-facing cover. The bottom band of the cover previously displayed Doc. WSI-SOP-001, Effective July 2026 · RMDM-Compliant, Owner: Executive Director & Qualified Professional (QP), and a large "Revision 2.7" display — all of these elements have been removed. The cover now displays only the brand-essential content: company name (Well Spring Intervention LLC), service-type subtitle (Level 3 Supervised Residential Group Home), values tagline (Empowerment · Growth · Freedom · Health · Wholeness · Healing), the full horizontal brand illustration, and a document-type label ("SOP & Operational Manual / Standard Operating Procedures, Protocols & Forms") with an accent rule. Versioning information remains fully accessible on internal surfaces only: PDF metadata (/Title, /Subject, /Keywords), the About This Manual inside page (p. 2), body page headers (every body page footer shows Doc ID and Rev. 2.8), the Version History table in Part 3, and Form 6 (Employee SOP Acknowledgment). Body content (SOPs, protocols, forms, §1.4(b) QP Credentialing Requirements) is unchanged from Rev. 2.7.',
         'Executive Director / QP'],
        ['2.9', 'Jul 2026',
         'Three-part enhancement. (1) Cover artwork refresh: the brand illustration is regenerated with lush GREEN leaves (replacing the prior amber/gold leaves) to more vividly symbolize growth, and an explicit well-spring (a circular pool of fresh water with concentric ripples) is added to the foreground directly in front of the tree-human figure, completing the symbolic narrative of wellspring, growth, health, and flourishing. The composition is otherwise unchanged: stylized tree-human figure, warm sunrise over calm water, warm earthy palette, horizontal 1344×768 aspect ratio, text-free. The standalone brand PNG (Well_Spring_Brand_Image_1344x768.png) is regenerated in lockstep. (2) New Protocol 22, Daily Workflow Schedules for All Personnel: codifies time-blocked daily routines for every personnel classification (QP, AP/PP, DCP Day Shift, DCP Evening Shift, DCP Awake Overnight, House Manager, RN, Billing Coordinator), with a master schedule summary table and explicit shift-change huddle / on-call / deviation policies. Aligns the SOP with the operational reality that the QP coordinates and schedules all clinical appointments and supervision across all shifts. (3) Forms enhancement, all nine forms in Part 3 are converted to interactive AcroForm fillable PDF fields. Each form now opens with a Form Properties banner declaring it printable, copyable, sharable, editable, and fillable. AcroTextField flowables replace underscore blanks; AcroCheckbox flowables replace bracket-checkboxes; signature and metadata lines use new fillable_meta_row / fillable_check_row / fillable_signature_row helpers. Standalone fillable PDF copies of all nine forms are also generated into /download/forms/ for use outside this manual. The Form 7 Service Name row (previously hardcoded to "Level 3 Residential, Shift") is removed in favor of fully fillable rows. Body content (SOPs §1-§11, Protocols 1-21, §1.4(b) QP Credentialing Requirements) is otherwise unchanged from Rev. 2.8.',
         'Executive Director / QP'],
        ['2.10', 'Jul 2026',
         'Cover artwork correction. The Rev. 2.9 cover-artwork refresh was intended to swap the original amber-leaves tree-human-sunrise illustration for one with lush green leaves and an explicit well-spring in the foreground, but the regenerated image did not actually persist into the cover source file (sop_cover_image.png) — the v2.9 PDF was rendered with the original Rev. 2.6 amber-leaves artwork and therefore did not visually reflect the green-leaves + well-spring concept the user specified. Rev. 2.10 corrects this by performing an in-place image-edit (rather than a fresh generation from a text prompt) on the canonical Rev. 2.6 horizontal illustration: the foliage is recolored from golden-amber to fresh vivid green (emerald and spring green) to embody growth, renewal, vitality, and flourishing; and a fountain-like well-spring of clear water is added in the immediate foreground directly before the base of the tree-human figure, complete with a subtle stone rim and a few delicate droplets catching the warm sunrise light. The original tree-human silhouette, horizon line, sunrise sky, warm earthy palette (terracotta, soft rose, peach, cream), painterly style, and 1344×768 horizontal aspect ratio are all preserved exactly — only the foliage color and the addition of the well-spring are changed. VLM verification confirms the new image has green leaves, a fountain well-spring in the foreground before the tree, and zero text/letters/numbers/watermarks of any language. The standalone brand PNG (Well_Spring_Brand_Image_1344x768.png) is regenerated in lockstep. Body content (SOPs §1-§11, Protocol 22 Daily Workflow Schedules, all nine AcroForm fillable forms, §1.4(b) QP Credentialing Requirements) is unchanged from Rev. 2.9 — only the cover image is corrected.',
         'Executive Director / QP'],
        ['2.11', 'Jul 2026',
         'Cover artwork iteration. Rev. 2.10 added a well-spring to the cover, but the well-spring was a wide circular stone basin — wider than the user intended. Per the user\'s direction to "use the cover from 2.8" (i.e., start from the original Rev. 2.8 cover with golden-amber foliage and no well-spring) and "make the leaves green and place the wellspring (should not be wider than the tree) in the foreground," Rev. 2.11 performs a fresh in-place image edit on the EXTRACTED ORIGINAL Rev. 2.8 cover image (recovered from the v2.8 PDF via pdfimages) rather than continuing to iterate on the Rev. 2.10 version. Two changes are applied: (1) the foliage is recolored from golden-amber to fresh vivid green (emerald and spring green) to embody growth, renewal, vitality, and flourishing; (2) a NARROW well-spring is added in the immediate foreground directly before the tree — a small vertical jet of clear water bubbling up from a small stone-rimmed opening in the ground, explicitly NARROWER than the tree itself (roughly one-third to one-half the width of the tree\'s leaf canopy), evoking the literal "well spring" of the company name rather than a wide circular pool. The original tree-human silhouette, horizon line, sunrise sky, warm earthy palette (terracotta, soft rose, peach, cream), painterly style, and 1344×768 horizontal aspect ratio are all preserved exactly. VLM verification confirms the new image has vibrant green leaves, a narrow blue water fountain in the foreground directly in front of the tree whose width is significantly smaller than the tree\'s full spread, and zero text/letters/numbers/watermarks of any language. The standalone brand PNG (Well_Spring_Brand_Image_1344x768.png) is regenerated in lockstep. Body content (SOPs §1-§11, Protocol 22 Daily Workflow Schedules, all nine AcroForm fillable forms, §1.4(b) QP Credentialing Requirements) is unchanged from Rev. 2.10 — only the cover image is iterated.',
         'Executive Director / QP'],
        ['2.12', 'Jul 2026',
         'Cover artwork refinement. Per the user\'s direction to "change the orifice that the spring emanates from&nbsp;— lets make it a heart-shaped stone instead of a jagged hole&nbsp;— and make the spring a little taller," Rev. 2.12 performs an in-place image edit on the Rev. 2.11 cover image. Two changes are applied: (1) the small jagged stone-rimmed opening/orifice that the water previously emanated from is replaced with a smooth sculpted HEART-SHAPED STONE&nbsp;— two rounded lobes at the top curving down to meet at a gentle point at the bottom, rendered in a soft warm earth-toned color (terracotta or soft rose) matching the surrounding palette, with a smooth plain surface and no facial features, no markings, no carvings, no patterns. The water now emanates upward from the center/top of this heart-shaped stone. The heart-shaped stone symbolizes the love, compassion, and trauma-informed care at the heart of the program. (2) The vertical jet/spray of water is made a little TALLER&nbsp;— roughly 30-50% taller than in Rev. 2.11&nbsp;— so the upward arc of clear water droplets and the slender column of water reach a bit higher into the air before falling back down. The wellspring remains NARROWER than the tree (its width is still significantly smaller than the tree\'s leaf canopy)&nbsp;— only the HEIGHT increases, not the width. The original green-leaved tree-human silhouette, horizon line, sunrise sky, warm color palette, painterly style, and 1344×768 horizontal aspect ratio are all preserved exactly. VLM verification confirms the new image has bright green leaves, a smooth heart-shaped stone (two rounded lobes at top, pointed bottom) with no facial features or markings, a tall slender vertical water jet reaching upward from the heart-shaped stone, the wellspring still significantly narrower than the tree\'s canopy, and zero text/letters/numbers/watermarks of any language. The standalone brand PNG (Well_Spring_Brand_Image_1344x768.png) is regenerated in lockstep. Body content (SOPs §1-§11, Protocol 22 Daily Workflow Schedules, all nine AcroForm fillable forms, §1.4(b) QP Credentialing Requirements) is unchanged from Rev. 2.11&nbsp;— only the cover image is refined.',
         'Executive Director / QP'],
        ['2.13', 'Jul 2026',
         'Cover artwork refinement. Per the user\'s feedback on Rev. 2.12 that "the fountain is too tall on this one" and "the pool is still there as well&nbsp;— we want to see a stone with a heart shaped likeness with the fountain spring flowing from it," Rev. 2.13 performs a series of in-place image edits on the Rev. 2.12b cover image. Two changes are applied: (1) the vertical water jet is significantly SHORTENED from a tall fountain plume (about 2 to 2.5 times the height of the heart-shaped stone in Rev. 2.12) to a modest, gentle natural spring (roughly one-quarter to one-third the height of the heart-shaped stone itself)&nbsp;— a brief bubbling spurt of clear water just above the top of the heart-shaped stone, evoking a natural wellspring welling up gently rather than a tall dramatic fountain. (2) The pool of water at the base of the wellspring is REMOVED entirely so the heart-shaped stone sits directly on dry warm earthy terrain with no pooling, puddle, wet patch, or rippling water around it&nbsp;— the foreground ground is uniformly dry earthy terrain matching the rest of the scene. The smooth sculpted heart-shaped stone (two rounded lobes at the top curving down to meet at a gentle point at the bottom, soft warm pink/terracotta color, completely smooth and unmarked surface) is preserved exactly, as are the fresh vivid green leaves, the stylized tree-human silhouette, the horizon line, the sunrise sky, the warm earthy color palette, the painterly style, and the 1344×768 horizontal aspect ratio. VLM verification confirms the new image has bright green leaves, a smooth unmarked heart-shaped stone in the foreground directly in front of the tree, a SHORT gentle bubbling water spring (about one-quarter to one-third the height of the stone) emanating from the top of the heart-shaped stone, the wellspring still significantly narrower than the tree\'s canopy, and zero text/letters/numbers/watermarks of any language. The standalone brand PNG (Well_Spring_Brand_Image_1344x768.png) is regenerated in lockstep. Body content (SOPs §1-§11, Protocol 22 Daily Workflow Schedules, all nine AcroForm fillable forms, §1.4(b) QP Credentialing Requirements) is unchanged from Rev. 2.12&nbsp;— only the cover image is refined.',
         'Executive Director / QP'],
        ['2.14', 'Jul 2026',
         'Cover artwork restart from Rev. 2.10. Per the user\'s direction to "start with 2.10 again" with a fundamentally redesigned wellspring&nbsp;— "the heart stone has a grey stone look. A small crack in the stone has the spring rising about belly high to the tree in the back ground. there is no hole or pool"&nbsp;— Rev. 2.14 recovers the original Rev. 2.10 cover image by extracting its embedded PNG from the immutable v2.10 PDF via pdfimages, then performs a major in-place image edit replacing the wide circular stone basin, tall narrow water jet, and circular pool with a single grey heart-shaped stone on dry ground, with a clear water spring rising vertically from a small natural crack in the stone to about belly-high of the tree. Body content (SOPs §1-§11, Protocol 22, all nine AcroForm fillable forms, §1.4(b) QP Credentialing Requirements) is unchanged from Rev. 2.13&nbsp;— only the cover image is redesigned.',
         'Executive Director / QP'],
        ['2.15', 'Jul 2026',
         'Cover redesign featuring the new official circular brand seal as the centerpiece (replaces the previous horizontal brand illustration). The seal combines a pentagonal house outline (with a floor, two vertical walls, two roof slopes meeting at a raised peak, and a horizontal ceiling line connecting the two top corner vertices) enclosing the existing tree-of-life / wellspring / family logo imagery. The full company name "Well Spring Intervention LLC" curves along the top arc between two bold concentric circular hairlines; the descriptor "Residential" curves along the bottom arc inside the inner hairline; small terracotta accent dots at 9:00/3:00 and a bottom closure ornament frame the composition; and the entire seal is rendered on a warm cream parchment background in deep walnut-brown with terracotta accents. The cover layout is a clean three-band composition: a compact top band carrying the "SOP / OPERATIONAL MANUAL" badge and the values tagline; a large middle band in which the cream seal square pops against the dark brown background as the focal point; and a bottom band carrying the document title, subtitle, and website URL. The redundant "Well Spring Intervention LLC" hero text was removed from the top band (the company name now lives on the seal\'s top arc). Two seal variants are produced in lockstep for brand reuse: a square variant (no URL below the circle, for avatar/profile-pic use) and a variant with the website URL below the circle (for letterhead, email signatures, and footer placement). Body content (SOPs §1-§11, Protocol 22, all nine fillable forms, §1.4(b) QP Credentialing Requirements) is unchanged from Rev. 2.14&nbsp;— only the cover is redesigned.',
         'Executive Director / QP'],
        ['2.16', 'Jul 2026',
         'About This Manual page cleanup. (1) Removed the redundant "Revision Lineage" narrative paragraph from the About This Manual inside page&nbsp;— the authoritative Version History table in Part 3 (this section) already serves that purpose, so the duplicate narrative was unnecessary. (2) Corrected the "Cover Artwork" description on the same inside page to accurately describe the new seal-based cover introduced in Rev. 2.15, replacing the now-outdated tree-human-sunrise-heart-stone description from Rev. 2.14. Body content (SOPs §1-§11, Protocol 22 Daily Workflow Schedules, all nine AcroForm fillable forms, §1.4(b) QP Credentialing Requirements) is unchanged from Rev. 2.15&nbsp;— only the About This Manual inside page is edited.',
         'Executive Director / QP'],
        ['2.17', 'Jul 2026',
         'New §9.4 Two-Story &amp; Multi-Level Facility Requirements added to SOP 9 (Facility, Safety, &amp; Environmental Management). New subsection codifies the regulatory requirements specific to two-story group homes: §9.4(a) applicability and DHSR licensing-notification triggers (relocating youth bedrooms upstairs, increasing upper-floor capacity, converting single-story to two-story, housing non-ambulatory youth upstairs); §9.4(b) means of egress per NC OSFM Building Code §425, NC Fire Code Ch. 10, and IBC 2021 §1030 (5.7 sq ft / 24 in / 20 in / 44 in sill emergency-escape openings, two remotely-located means of egress per occupied story, stair geometry, emergency-backup stair lighting, chain-style fire-escape ladders in each second-floor youth bedroom); §9.4(c) per-floor fire detection, suppression, and alarm (interconnected smoke detectors on all levels per NFPA 72, CO detectors on every floor with fuel-burning appliances and within 10 ft of sleeping rooms, automatic sprinklers per NFPA 13D/13R, 2A-10BC extinguishers per level with 75-ft max travel); §9.4(d) per-floor staff supervision (awake overnight DCP positioned to cover upper-floor hallway, 15-minute room checks physically performed on every sleeping floor and documented on Form 1, stair safety gates at top and bottom for youth under 12 or with elopement/suicidality risk, baby-monitor/intercom option with documented 60-second response time); §9.4(e) window fall protection (restrictors limiting opening to ≤4 in. where second-floor sill is &lt;24 in. above floor, staff-key releasable, monthly function check on Form 5); §9.4(f) vertical-evacuation drills (monthly fire drills must include full evacuation from all second-floor sleeping rooms to grade, quarterly tornado drills use lowest interior level only — no second-floor bathrooms); §9.4(g) bedroom placement policy (lower-acuity/lower-mobility/younger youth on ground floor; no attic/basement bedrooms; placement documented in PCP); §9.4(h) posted evacuation maps and stair hazard signage on each floor. Each requirement carries inline hyperlinked web-source citations to the underlying NC Administrative Code (10A NCAC 27G, 13F .0309, 13G .0316), NC OSFM Building Code §425, NC Fire Code 2024 Ch. 10, NC IFC 2021 Ch. 4, IBC 2021 §1030, NC DHSR ACLS Family Care Home licensing and Fire Safety training PDFs, NFPA 101 Life Safety Code (Board &amp; Care §32/33), Durham NC and Orange County NC smoke/CO alarm summaries, NCSL CO Detector Statutes, and the NC Family Care Home structure rule (no more than 2 stories; second-floor residents require two direct exterior egress). Form 1 (Shift Change &amp; Awake Night Watch Log) is extended with a new "Per-Floor Walk-Through Certification" sub-table requiring the awake overnight DCP to initial Floor 1, Floor 2, and Basement walk-throughs every 2 hours (4 time blocks: 11p-1a, 1a-3a, 3a-5a, 5a-7a) — single-story facilities mark N/A. Form 5 (Environmental Safety Log) is extended with a new "Two-Story / Multi-Level Per-Floor Safety Checks" sub-table with three floor rows (Floor 1 / Floor 2 / Basement) and eight check columns (Smoke Detectors, CO Detectors, Extinguisher, Egress Window / Escape Ladder, Window Restrictor ≤4 in., Stair Gate, plus Staff Initials) completed monthly. Form 6 (Employee SOP Acknowledgment) Rev. reference updated from 2.16 to 2.17. All other body content (SOPs §1-§8, §10-§11, Protocol 22 Daily Workflow Schedules, §1.4(b) QP Credentialing Requirements, and all other forms) is unchanged from Rev. 2.16.',
         'Executive Director / QP'],
        ['2.18', 'Jul 2026',
         '<b>LICENSE CATEGORY CORRECTION</b> — Level III Residential Treatment Facility (Staff-Secure for Children and Adolescents) under 10A NCAC 27G .2600. Prior revisions incorrectly identified the facility as a "Level 3 Supervised Residential Group Home" under 27G .5600; the correct license category per organizational direction is <b>Level III RTF Staff-Secure</b> under <b>10A NCAC 27G .2600</b>, issued by NC DHSR Mental Health Licensure &amp; Certification Section (MHLC), credentialed with <b>Alliance Health</b> as the LME/MCO/Tailored Plan. <b>Major content changes:</b> (1) §1.2 rewritten for correct license category, naming DHSR MHLC and Alliance Health, plus four new sub-subsections: §1.2(a) Accreditation Prerequisite (COA/TJC/CARF/CQL per NCGS §122C-26); §1.2(b) LME/MCO Letter of Support per NCGS §122C-23.1; §1.2(c) Certificate of Need (CON) Determination per NCGS Ch. 131E Art. 9; §1.2(d) Alliance Health Provider Network Application. (2) §1.4 updated to use QP/QMHP interchangeably per 27G .2600. (3) NEW §1.7 Resident Rights &amp; Dignity per NCGS §122C-51 through §122C-57. (4) NEW §1.8 Organizational &amp; Financial Foundations (Articles of Incorporation, governing body roster, liability insurance, lease/deed, financial solvency). (5) §2.1 STAFFING RATIO CRITICAL FIX — replaced 1:4 day / 1:8 overnight with <b>2 staff minimum for 1–4 youth 24/7</b> per 27G .2600, scaling to 4 staff for 5–8 youth and 5 staff for 9 youth. (6) NEW §2.5(a) CEU tracking per licensed clinical staff. (7) NEW §2.6 Staff Leave &amp; Time-Off Policy per 27G .0203(e). (8) §3 ADMISSION PHYSICAL EXAM CRITICAL FIX — replaced "within 30 days of admission" with <b>"within 90 days PRIOR to admission"</b> per 27G .2600. (9) NEW §5.5 Activities Program (minimum 14 hrs/week planned group activities per 27G .2600(c)). (10) NEW §6.5 Infection Control Program per CDC, 27G .0209, OSHA BBP (29 CFR 1910.1030). (11) NEW §7.3 Facility-Based School Determination (required for PRTF, not for Level III RTF). (12) NEW §9.5 Staff-Secure Physical-Plant Measures (controlled access, delayed egress, line-of-sight, visitor mgmt, contraband search). (13) NEW §9.6 Zoning Compliance (Fair Housing Act, NC Group Homes Act NCGS §160D-906). (14) NEW §9.7 Disaster &amp; Emergency Plan (fire, tornado, hurricane, power outage, system failure, lockdown, emergency relocation). (15) Protocol 19 in Part 2 expanded (hurricane, power outage, emergency relocation); all .5600 → .2600; overnight staffing updated from 1:8 to 2:4. (16) Form 6 Rev. reference updated from 2.17 to 2.18. Cover subtitle updated to "Level III Residential Treatment Facility (Staff-Secure)". Seal artwork (Rev. 2.15) unchanged.',
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
