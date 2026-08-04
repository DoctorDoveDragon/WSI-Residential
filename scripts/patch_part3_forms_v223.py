#!/usr/bin/env python3
"""patch_part3_forms_v223.py — Add Form 10 (LP Consultation Log), Form 11
(Psychotropic Drug Regimen Review Log), and v2.22/v2.23 version history rows.
"""
import os

PATH = '/home/z/my-project/scripts/sop_content_v3_part3.py'

with open(PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# ─── Insert Form 10 + Form 11 BEFORE the Version History section ────────
# Find the Version History marker
vh_marker = "    # ── Version History ────────────────────────────────────────────\n"
if vh_marker not in content:
    print('[MISS] Version History marker not found')
    raise SystemExit(1)

forms_10_11 = '''    # ── Form 10: Licensed Professional Consultation Log (NEW in v2.23) ──
    story.extend(_form_banner_and_heading(
        10, 'Licensed Professional Consultation Log',
        'Part 3 &middot; Form 10: Licensed Professional Consultation Log',
        external_ref='Level III Staff-Secure operating standards \u2014 Licensed Professional face-to-face clinical consultation (\u00a74.6)',
        instructions='Document every weekly Licensed Professional face-to-face clinical consultation session per \u00a74.6 (minimum 4 hours per week). '
                     'One log per facility per week. Maintain in facility compliance binder for the full record-retention period per \u00a71.6. '
                     'Click any cell to type.',
    ))
    story.append(fillable_meta_row([
        ('Facility:', 200, 'Facility name'),
        ('Week of (Sun \u2014 Sat):', 160, 'Week start date'),
    ]))
    story.append(Spacer(1, 4))
    story.append(Paragraph('<b>Weekly Consultation Sessions</b>', s_form_section))

    f10_header = ['Date', 'Start Time', 'End Time', 'Total Hours', 'Format (In-Person / Telehealth)', 'Attendees', 'Cases Reviewed', 'Recommendations / Follow-Up Actions', 'LP Signature']
    f10_th = ParagraphStyle('f10th', fontName=BODY_BOLD, fontSize=8, leading=10, textColor=colors.white, alignment=TA_LEFT)
    f10_data = [[Paragraph(f'<b>{h}</b>', f10_th) for h in f10_header]]
    for _ in range(8):
        f10_data.append(_fillable_data_cells(9, default_width=55, height=22, font_size=8))
    f10_widths = [0.08*AVAIL_W, 0.08*AVAIL_W, 0.08*AVAIL_W, 0.08*AVAIL_W, 0.12*AVAIL_W, 0.14*AVAIL_W, 0.14*AVAIL_W, 0.20*AVAIL_W, 0.08*AVAIL_W]
    t10 = Table(f10_data, colWidths=f10_widths, hAlign='CENTER', repeatRows=1)
    sc10 = [
        ('BACKGROUND', (0, 0), (-1, 0), HEADER_FILL),
        ('GRID',       (0, 0), (-1, -1), 0.4, BORDER),
        ('VALIGN',     (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING',  (0, 0), (-1, -1), 3),
        ('RIGHTPADDING', (0, 0), (-1, -1), 3),
        ('TOPPADDING',   (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING',(0, 0), (-1, -1), 8),
    ]
    for i in range(1, len(f10_data)):
        bg = TABLE_ROW_ODD if i % 2 == 1 else TABLE_ROW_EVEN
        sc10.append(('BACKGROUND', (0, i), (-1, i), bg))
    t10.setStyle(TableStyle(sc10))
    story.append(t10)
    story.append(Spacer(1, 8))
    story.append(Paragraph(
        '<b>Weekly Total Face-to-Face Hours:</b> __________ hrs &nbsp;&nbsp; '
        '<b>Meets 4-hour minimum (\u00a74.6)?</b> \u2610 Yes &nbsp; \u2610 No (if No, document remediation below) '
        '<b>QP Signature:</b> ___________________________ <b>Date:</b> __________',
        s_form_meta
    ))
    story.append(Spacer(1, 12))

    # ── Form 11: Psychotropic Medication Drug Regimen Review Log (NEW in v2.23) ──
    story.extend(_form_banner_and_heading(
        11, 'Psychotropic Medication Drug Regimen Review Log',
        'Part 3 &middot; Form 11: Psychotropic Medication Drug Regimen Review Log',
        external_ref='Level III Staff-Secure operating standards \u2014 Psychotropic drug regimen review every 6 months by pharmacist/physician (\u00a76.3(a))',
        instructions='Document every 6-month psychotropic medication drug regimen review per \u00a76.3(a). '
                     'One log per youth. Initial review within 30 days of admission; subsequent reviews at least every 6 months thereafter. '
                     'Maintain in clinical record per \u00a71.6. Click any cell to type.',
    ))
    story.append(fillable_meta_row([
        ('Youth Name:', 200, 'Youth name'),
        ('Service Record # / MID:', 160, 'Service record number or MID'),
        ('Date of Birth:', 120, 'Youth date of birth'),
    ]))
    story.append(Spacer(1, 4))
    story.append(fillable_meta_row([
        ('Prescribing Psychiatrist:', 220, 'Prescribing psychiatrist name'),
        ('Pharmacy:', 200, 'Pharmacy name and phone'),
    ]))
    story.append(Spacer(1, 4))
    story.append(Paragraph('<b>6-Month Review Tracking</b>', s_form_section))

    f11_header = ['Review Date', 'Reviewer Name', 'Reviewer Credential (PharmD / MD / DO)', 'Medications Reviewed (Name / Dose / Frequency / Indication)', 'Findings (Interactions, Adverse Effects, Lab Monitoring Needed)', 'Recommendations to Prescriber', 'Date Sent to Prescriber', 'Next Review Due (6 months)']
    f11_th = ParagraphStyle('f11th', fontName=BODY_BOLD, fontSize=8, leading=10, textColor=colors.white, alignment=TA_LEFT)
    f11_data = [[Paragraph(f'<b>{h}</b>', f11_th) for h in f11_header]]
    for _ in range(6):
        f11_data.append(_fillable_data_cells(8, default_width=60, height=28, font_size=8))
    f11_widths = [0.08*AVAIL_W, 0.10*AVAIL_W, 0.12*AVAIL_W, 0.18*AVAIL_W, 0.16*AVAIL_W, 0.14*AVAIL_W, 0.10*AVAIL_W, 0.12*AVAIL_W]
    t11 = Table(f11_data, colWidths=f11_widths, hAlign='CENTER', repeatRows=1)
    sc11 = [
        ('BACKGROUND', (0, 0), (-1, 0), HEADER_FILL),
        ('GRID',       (0, 0), (-1, -1), 0.4, BORDER),
        ('VALIGN',     (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING',  (0, 0), (-1, -1), 3),
        ('RIGHTPADDING', (0, 0), (-1, -1), 3),
        ('TOPPADDING',   (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING',(0, 0), (-1, -1), 8),
    ]
    for i in range(1, len(f11_data)):
        bg = TABLE_ROW_ODD if i % 2 == 1 else TABLE_ROW_EVEN
        sc11.append(('BACKGROUND', (0, i), (-1, i), bg))
    t11.setStyle(TableStyle(sc11))
    story.append(t11)
    story.append(Spacer(1, 8))
    story.append(Paragraph(
        '<b>Initial Review (within 30 days of admission):</b> \u2610 Completed &nbsp; \u2610 Most-recent prior review obtained '
        '(date: __________) &nbsp; <b>Reviewer Signature:</b> ___________________________',
        s_form_meta
    ))
    story.append(Spacer(1, 12))

'''

# Insert forms before Version History
new_content = content.replace(vh_marker, forms_10_11 + vh_marker)
print('[OK] Inserted Form 10 (LP Consultation Log) and Form 11 (Psychotropic Drug Regimen Review Log)')

# ─── Add v2.22 and v2.23 rows to Version History ─────────────────────
# The last row in vh_rows is v2.21; we need to add v2.22 and v2.23 after it
# Find the v2.21 row's closing `],` (which ends the vh_rows list)

# v2.21 row ends with: 'Executive Director / QP'],\n    ]
v221_end = """         'Executive Director / QP'],
    ]"""

v22_plus_23_rows = """         'Executive Director / QP'],
        ['2.22', 'Aug 2026',
         '<b>PUBLIC EDITION (LEGISLATION-FREE).</b> Removes all statutory and regulatory citations (NCGS, NCAC, G.S., 10A NCAC, 122C-XX) from the public-facing manual. Companion compliance master (Doc. WSI-SOP-001-LEG, Rev. 2.21) retains all citations for QA and audit reference. Operational language substituted throughout (e.g., "10A NCAC 27G .1700" \u2192 "the Level III Staff-Secure operating standards"; "NCGS \u00a7122C-XX" \u2192 "the Resident Rights framework"; "LME/MCO" \u2192 "the regional managed care organization" where contextually appropriate; "NC DHSR MHLC" \u2192 "the state licensing authority"; "HIPAA" \u2192 "the federal health-privacy law" where contextually appropriate). Resident Handbook v1.0 published as companion document. Resident Handbook v1.1 signs Welcome Letter as T. Thompson and removes legislation references from sidebars. All operational policies, staffing ratios, clinical requirements, medication management, incident reporting, and resident rights obligations remain unchanged from v2.21.',
         'Executive Director / QP'],
        ['2.23', 'Aug 2026',
         '<b>v2.22 COMPLIANCE AUDIT REMEDIATION.</b> Implements all 22 corrective actions from the SOP Manual v2.22 Compliance Audit against 10A NCAC 27G .1700 + cross-referenced core rules (.0104, .0201\u2013.0210). <b>HIGH severity (3):</b> F-001 \u2014 adds new \u00a74.6 Licensed Professional Face-to-Face Clinical Consultation per .1705(a)-(b) (minimum 4 hrs/wk face-to-face consultation by a Licensed Professional) and new Form 10 (Licensed Professional Consultation Log); F-002 \u2014 adds new \u00a76.3(a) Psychotropic Medication Drug Regimen Review per .0209(f) (every 6 months by pharmacist or physician) and new Form 11 (Psychotropic Medication Drug Regimen Review Log); F-003 \u2014 <b>RESOLVES the open \u00a71.2(h)(b) compliance flag</b> in favor of CCP 8D-2; all legacy "CCP 8C" references in \u00a71.2, \u00a72, \u00a73, \u00a74, \u00a75, \u00a76, and \u00a710 reference lines globally updated to "CCP 8D-2"; \u00a71.2(h)(b) rewritten from OPEN to RESOLVED; \u00a71.2(h)(c) updated to reflect both (a) and (b) now resolved. <b>MEDIUM severity (18):</b> M-007 \u2014 adds QP 2-year direct client care experience statement to \u00a71.4(b); F-006/F-007/M-011/M-028/M-029 \u2014 adds new \u00a72.2(a) Individualized Supervision Plans for APs and DCPs and expands AP definition to enumerate all four .0104(1) pathways; M-033 \u2014 adds age-18, literacy, and criminal-conviction self-disclosure requirements to \u00a72.2; F-009 \u2014 adds new \u00a73.6 18th-Birthday Continuation Policy per .1706(e) (up to 6 months or end of school year, whichever is longer); M-025 \u2014 adds \u00a73.4(a) 7-day advance written notification for non-emergency discharge; M-026 \u2014 adds \u00a73.4(b) pre-discharge CFT meeting; F-008 \u2014 adds \u00a73.4(c) 5-business-day post-emergency service-planning meeting per .1708(e); M-031 \u2014 adds governing-body policies for client fee assessment, lab test authorization/follow-up, and volunteer services to \u00a71.8; M-032 \u2014 adds governing-body minutes permanently maintained statement to \u00a71.8; M-038 \u2014 updates \u00a79.2 and Protocol 19 to require quarterly fire AND tornado drills for EACH shift (day, evening, overnight); F-012 \u2014 adds \u00a76.3(b) Medication Receipt &amp; Verification (tamper-resistant packaging + label content); M-043 \u2014 adds \u00a76.3(c) Medication Storage (locked cabinet 59\u201386\u00b0F, dedicated med fridge 36\u201346\u00b0F, daily temp log on Form 5); F-013 \u2014 adds \u00a76.3(d) Medication Disposal Documentation per .0209(d)(1)-(4) (controlled-substance disposal witnessed by 2 staff); F-014 \u2014 adds \u00a76.3(e) Medication Education per .0209(g)(1)-(3) (at admission, at each med change, and quarterly thereafter, with developmentally appropriate content and family/guardian education offered). <b>LOW severity (1):</b> F-011 \u2014 adds new \u00a71.2(h)(d) Cross-Reference Clarification Note documenting the .1702(a) \u2192 .0104(18) vs .0104(21) discrepancy (rule appears to contain a typographical error; Manual applies the .0104(21) "Qualified professional" definition as operative). <b>LEGISLATION STRIPPING (additional):</b> \u00a71.2 license paragraph de-abbreviates "NC DHSR / MHLC / DSS" to "the applicable state mental health authority \u2014 not under foster-care licensing"; \u00a73.1 admission criteria replaces "Involuntary Commitment (IVC)" with "acute psychiatric crisis requiring inpatient hospitalization"; \u00a72.1 note replaces ".0103(14)" citation and "DHSR MHLC" with plain-language "state group-home definition" and "state-issued license"; \u00a76.3 replaces "NC Medication Administration training" with "state-approved medication administration training"; \u00a76.3 replaces "IRIS" abbreviation with "state incident-reporting system (IRIS)" on first use. Companion audit report and XLSX crosswalk matrix delivered at /download/WSI_SOP_v2.22_Compliance_Audit_Report.pdf and /download/WSI_SOP_v2.22_Compliance_Audit_Crosswalk.xlsx.',
         'Executive Director / QP'],
    ]"""

if v221_end in new_content:
    new_content = new_content.replace(v221_end, v22_plus_23_rows)
    print('[OK] Added v2.22 and v2.23 rows to Version History')
else:
    print('[MISS] v2.21 row end not found — checking for alternative patterns')
    # Maybe the closing pattern is slightly different
    import re
    m = re.search(r"\['2\.21', 'Aug 2026',.{500}?Executive Director / QP'\],\s*\]", new_content, re.DOTALL)
    if m:
        print('Found v2.21 row via regex, replacing')
        new_content = new_content[:m.end()-len("    ]")] + v22_plus_23_rows.split("         'Executive Director / QP'],\n    ]")[1] + new_content[m.end():]
    else:
        print('Could not find v2.21 row end')

# Update Part 3 divider intro to mention 11 forms instead of 9
old_intro = """        'The following nine forms and logs are the official documentation instruments for '"""
new_intro = """        'The following eleven forms and logs are the official documentation instruments for '"""
if old_intro in new_content:
    new_content = new_content.replace(old_intro, new_intro)
    print('[OK] Updated Part 3 intro: 9 forms → 11 forms')
else:
    print('[MISS] Part 3 intro not found')

old_intro2 = """        'available in the /download/forms/ directory for use outside this manual.',"""
new_intro2 = """        'available in the /download/forms/ directory for use outside this manual. '
        'Forms 10 and 11 are new in Version 2.23 to address the Licensed Professional '
        'consultation-log and psychotropic-medication drug-regimen-review requirements.',"""
if old_intro2 in new_content:
    new_content = new_content.replace(old_intro2, new_intro2)
    print('[OK] Added Forms 10/11 new-in-v2.23 note to Part 3 intro')

# Update generate_sop.py Part 3 description in TOC intro
with open('/home/z/my-project/scripts/generate_sop.py', 'r', encoding='utf-8') as f:
    gen_content = f.read()

old_toc_p3 = """        'and logs, including the Full Service Note Template, Comprehensive Clinical '\n        'Record Content Checklist, and Accounting of Disclosures Log. A complete '\n        'revision history appears in the Version History table at the end of Part 3.',"""
new_toc_p3 = """        'and logs, including the Full Service Note Template, Comprehensive Clinical '\n        'Record Content Checklist, Accounting of Disclosures Log, the Licensed '\n        'Professional Consultation Log (new in v2.23), and the Psychotropic Medication '\n        'Drug Regimen Review Log (new in v2.23). A complete revision history appears '\n        'in the Version History table at the end of Part 3.',"""
if old_toc_p3 in gen_content:
    gen_content = gen_content.replace(old_toc_p3, new_toc_p3)
    print('[OK] Updated generate_sop.py TOC intro to mention Forms 10 & 11')
    with open('/home/z/my-project/scripts/generate_sop.py', 'w', encoding='utf-8') as f:
        f.write(gen_content)

# Write back Part 3
with open(PATH, 'w', encoding='utf-8') as f:
    f.write(new_content)

print('\n=== Done ===')
