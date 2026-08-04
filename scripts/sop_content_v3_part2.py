
# ────────────────────────────────────────────────────────────────────
# Content builders — Part 2: Protocols (22 protocols, RMDM-compliant)
# ────────────────────────────────────────────────────────────────────
from generate_sop import (
    part_divider, section_heading, ref_line, para, bullets,
    Paragraph, Spacer, AVAIL_W, s_bullet, s_body, s_h2, s_form_section,
    Table, TableStyle, ParagraphStyle, colors, TA_LEFT, TA_CENTER,
    BODY_FONT, BODY_BOLD, BORDER, HEADER_FILL, TEXT_PRIMARY, TEXT_MUTED,
    TABLE_ROW_ODD, TABLE_ROW_EVEN,
)


def build_part2():
    story = []
    story.extend(part_divider(
        'PART 2',
        'Actionable Workflows & Protocols',
        'These 22 protocols translate the SOP policies into clear, sequential, step-by-step '
        'actions for daily operations. Each protocol is designed to be referenced quickly '
        'during a shift and followed exactly. Deviations from protocol require QP approval '
        'and must be documented. Protocols 20 and 21 are new in Version 2.0 and address '
        'service orders/authorizations and record management/disclosure accounting per '
        'RMDM requirements. Protocol 22 is new in Version 2.9 and codifies the daily '
        'workflow schedules for every personnel classification so that each shift, role, '
        'and hand-off has a documented time-blocked routine.',
    ))

    protocols = [
        ('Admissions & Pending Record Protocol', [
            '<b>Pre-Admission.</b> QP reviews referral packet, verifies active Medicaid, schedules tour with guardian and youth.',
            '<b>Pending Record Creation.</b> If individual presents for screening but is not immediately enrolled, create a Pending Record with screening/consultation info.',
            '<b>Day of Admission.</b> QP obtains all signed consents (treatment, medication, transportation, ROI, photos). DCP conducts respectful property search and secures medications. QP administers C-SSRS and documents clinical status. Convert Pending Record to Full Clinical Record (merge all documentation).',
            '<b>Post-Admission.</b> RN visits within 72 hours for medication delegation and nursing assessment. ISP/PCP meeting scheduled within 30 days.',
        ]),
        ('Daily Direct Care Protocol (DCP)', [
            '<b>Day Shift (7a-3p).</b> Shift change handoff and controlled-substance med count. Wake youth per schedule with 15-minute visual checks. Breakfast and AM medications. School transportation. Daily chores.',
            '<b>Evening Shift (3p-11p).</b> Shift change. Therapy and clinical groups. Chores, dinner, and PM medications. Free time and hygiene routine. 10:00 PM bedtime.',
            '<b>Night Shift (11p-7a).</b> Shift change and med count. Conduct 15-minute line-of-sight room checks documented on the Night Watch Log. Awake at all times — no sleeping permitted.',
        ]),
        ('Incident Response & IRIS Protocol', [
            '<b>Immediate.</b> Ensure scene safety; call 911 if medical emergency or active danger. Notify the On-Call QP immediately.',
            '<b>Notifications.</b> DSS immediately for abuse allegations. Guardian within 1 hour. LME/MCO per their requirements.',
            '<b>Reporting.</b> QP enters the IRIS report within 24 hours using objective, factual narrative — no interpretations or labels.',
            '<b>Investigation.</b> QP completes the internal investigation within 14 days and uploads findings and CAP to IRIS.',
            '<b>Separate Filing.</b> Record the occurrence of the incident in the service note. File the completed incident report separately in administrative files — NOT in the clinical record.',
        ]),
        ('Behavioral Crisis & Restraint Protocol', [
            '<b>Tier 1 — De-escalation.</b> Use BSP coping skills: sensory items, breaks, verbal redirection, change of environment.',
            '<b>Tier 2 — Crisis.</b> Clear the area of other youth. Call for staff backup. Use the NCI/CPI verbal continuum and physical distancing.',
            '<b>Tier 3 — Restraint.</b> Only for imminent serious harm. Apply NCI hold; never use prone, mechanical, or chemical restraints. End the hold the moment danger passes.',
            '<b>Post-Restraint.</b> Medical check within 1 hour. Notify guardian within 1 hour. Debrief with youth within 24 hours. File IRIS report.',
        ]),
        ('Medication Administration Protocol', [
            '<b>Prep.</b> Wash hands. Unlock med cart. Verify the "5 Rights" against the MAR: right youth, right med, right dose, right route, right time.',
            '<b>Administer.</b> Verify youth identity. Pour medication into a labeled cup. Observe swallowing. Check the mouth for "cheeking".',
            '<b>Document.</b> Initial the MAR immediately. Circle "R" if refused; notify RN and QP. Never pre-initial or backdate.',
            '<b>Errors.</b> Stop, isolate remaining meds, call RN/Psychiatrist, monitor the youth, file IRIS, and notify the guardian.',
        ]),
        ('Medicaid Service Note & Documentation Protocol', [
            'Write the shift note by end of shift. No backdating — ever.',
            '<b>Mandatory Fields.</b> Youth Name & Service Record # / MID. Full Date & Place of Service. Name of Service & Type of Contact (in-person, collateral, etc.). Purpose (ISP Goal # referenced). Objective Description of Interventions (factual, specific). Duration (for time-based services; for per diem, indicate shift coverage hours). Effectiveness & Youth Response/Progress. Full Signature with Credentials and Date.',
            '<b>Shift Notes.</b> Identify coverage hours and names of all staff present for ratios.',
            '<b>Late Entries.</b> Mark "Late Entry made on [date] for service on [date]" if after 24 hours.',
            '<b>Alterations.</b> Correct with explanation, signed/dated; never obscure original. Alterations exceeding 7 business days are not billable.',
            'Billing suspended for any day youth is away for more than 24 consecutive hours.',
        ]),
        ('AWOL / Missing Child Response', [
            '<b>Discovery.</b> Call the staff code for missing youth. Search the immediate area and check all cameras.',
            '<b>Notifications (within 15-30 minutes).</b> Law enforcement, guardian, LME/MCO, and DSS (if applicable).',
            '<b>Documentation.</b> File IRIS within 24 hours with a complete narrative.',
            '<b>Return.</b> Conduct a medical check, contraband search, and trauma-informed debriefing. Notify all parties who were previously contacted.',
        ]),
        ('Suicide Risk & Self-Harm Management', [
            '<b>Screening.</b> C-SSRS at admission and immediately whenever threats or self-harm occur.',
            '<b>Safety.</b> Remove hazards (ligatures, sharps, cords). Implement 1:1 line-of-sight supervision.',
            '<b>Clinical.</b> QP assesses within 1 hour. If imminent risk: call 911 or initiate IVC. If moderate risk: update the Safety Plan and increase supervision.',
            '<b>Documentation.</b> File IRIS. Staff sign the updated Safety Plan and acknowledge the increased supervision level.',
        ]),
        ('Contraband & Room Search Protocol', [
            '<b>Definition.</b> Contraband includes weapons, drugs, unauthorized medications, lighters, chargers with frayed cords, and any item prohibited by house rules.',
            '<b>Routine.</b> Conducted at admission and on return from any pass. The youth must be present.',
            '<b>Probable Cause.</b> Requires QP approval. Two staff must be present. Document the basis for the search.',
            '<b>Execution.</b> Search systematically (one area at a time). Safe items are locked in the safe and returned at discharge. Illegal items are turned over to law enforcement.',
        ]),
        ('PCP Implementation & Review', [
            '<b>Development (30 Days).</b> QP schedules the meeting with the team and drafts measurable, individualized goals.',
            '<b>Operationalize.</b> QP creates a "Staff Cheat Sheet" summarizing each youth\'s goals, triggers, and interventions. Staff sign the PCP Acknowledgment Form.',
            '<b>90-Day Review.</b> QP tracks expirations and schedules reviews. Updates progress, obtains signatures, and writes addendums for any significant change.',
            '<b>Service Order.</b> The signed PCP serves as the service order for all services delivered.',
        ]),
        ('Transportation & Community Outing Safety', [
            '<b>Driver Prep.</b> Valid license, clean MVR on file. Complete the daily vehicle safety checklist. Confirm first-aid kit and Medicaid cards are present.',
            '<b>Transport.</b> Conduct a headcount before leaving and upon return. If transporting one youth, staff sits in the back seat. Seatbelts on at all times. Never leave youth unattended in a vehicle.',
            '<b>Outings.</b> Tied to an ISP goal. Assess behavioral stability (no restraint in the last 4 hours). Carry the agency cell phone and emergency contact list.',
        ]),
        ('Grievance Process for Youth', [
            '<b>Accessibility.</b> Process is explained at admission. Blank forms and a locked grievance box are located in the common area. LME/MCO grievance numbers are posted.',
            '<b>Filing.</b> Verbal or written. Staff assist immediately upon request. Place the grievance in the locked box within 1 hour.',
            '<b>Resolution.</b> QP opens the box daily. Acknowledges within 24 hours. Provides written resolution within 7 days. Abuse allegations trigger an IRIS report and immediate DSS notification.',
        ]),
        ('Staffing Ratio & Awake Overnight Protocols', [
            '<b>Ratios.</b> 2 staff minimum for 1–4 youth (Level III Staff-Secure, per our staff-secure operating standards). Ratios scale with census: 4 staff for 5–8 youth; 5 staff for 9 youth. The 2:4 minimum applies 24/7 including overnight. If a staff member calls out, the on-call system activates a replacement before the shift begins; the on-call QP covers in-house personally if no replacement is available. Single-staffing is prohibited at all times.',
            '<b>Awake Overnight.</b> Two (2) awake staff on duty at all times for 1–4 youth. Sleeping is prohibited. 15-minute visual room checks are documented on the Night Watch Log (Form 1), including the Per-Floor Walk-Through Certification sub-table for two-story facilities. Hallway lights remain on. Engage nighttime wakers quietly and briefly — do not start conversations that escalate arousal.',
        ]),
        ('Medical Emergencies & Acute Illness Response', [
            '<b>Triage.</b> Assess the situation. Call QP and/or RN. Err on the side of caution — when in doubt, transport.',
            '<b>Emergency.</b> Call 911. Staff rides in the ambulance. QP calls in additional staff to maintain ratio at the facility.',
            '<b>Non-Emergency.</b> Contact PCP for a same-day appointment. Take consent forms and Medicaid card.',
            '<b>Documentation.</b> Guardian notified within 1 hour. IRIS filed. Billing suspended if the youth is hospitalized overnight.',
        ]),
        ('Educational Coordination & School Reintegration', [
            '<b>Enrollment (5 Days).</b> QP contacts the LEA McKinney-Vento liaison or EC Director. Signs ROI. Coordinates transportation.',
            '<b>IEP.</b> QP/AP attends IEP meetings. Advocates for an aligned BIP. Files the IEP in the youth\'s chart.',
            '<b>Attendance.</b> Morning check before transport. Log daily. Refusal is an ISP issue, not a punishable offense. Collect daily behavior reports from the school.',
        ]),
        ('Family Engagement, Visitation & Home Passes', [
            '<b>Visitation.</b> Based on ISP/court orders. Approved visitor list is maintained in the office. Staff search bags before visits. Document all visits.',
            '<b>Home Passes.</b> QP and guardian must approve. Pass medications are provided in a locked box with administration instructions.',
            '<b>Billing Exclusion.</b> If the youth is away for more than 24 consecutive hours, Medicaid per diem is suspended. Notify the Billing Coordinator immediately.',
        ]),
        ('Discharge & Transition Protocol', [
            '<b>Planning.</b> Begins at admission. Trial home visits are conducted prior to discharge whenever possible.',
            '<b>Step-Down.</b> Discharge meeting is scheduled. Community linkages (outpatient therapy, medication management, school) are established and confirmed before discharge.',
            '<b>Discharge Day.</b> Medications are handed directly to the guardian with a signed transfer form. Belongings are inventoried. Discharge summary is completed within 7 days.',
            '<b>Administrative Closure.</b> If QP/clinician leaves without completing discharge documentation, the supervisor processes the discharge and audits the record. Billed services without proper documentation are adjusted back to the payor per 42 CFR 401.305.',
        ]),
        ('Infectious Disease & Bloodborne Pathogen Control', [
            '<b>Universal Precautions.</b> Treat all bodily fluids as infectious. Wear appropriate PPE (gloves, mask, eye protection) when exposure is possible.',
            '<b>Exposure.</b> Wash the affected area with soap and water. Notify QP and RN. Go to Urgent Care within 2 hours. File IRIS. Offer post-exposure testing per protocol.',
            '<b>Outbreak.</b> Two or more youth with identical symptoms = isolate, increase sanitation, and notify the County Health Department if the illness is reportable.',
        ]),
        ('Emergency & Disaster Preparedness', [
            '<b>Fire.</b> Evacuate immediately. Headcount at the rally point. Call 911. Do not re-enter. <b>Monthly fire drills required for EACH shift (day, evening, overnight) — 3 fire drills per month total</b>, documented on Form 5 with shift, date, evacuation time, and shift-supervisor signature.',
            '<b>Tornado.</b> Move to the interior safe room. Turtle position. <b>Quarterly tornado drills required for EACH shift (day, evening, overnight) — 3 tornado drills per quarter total</b>, documented on Form 5 with shift, date, and shift-supervisor signature.',
            '<b>Hurricane.</b> Monitor NHC advisories during Atlantic season (Jun 1 – Nov 30). At Tropical Storm Warning or Hurricane Watch: secure outdoor projectiles, verify generator fuel, stock 7-day food/water/medications, verify emergency-contact lists, contact guardians re storm plan. At Hurricane Warning: coordinate with LME/MCO and guardian re evacuation vs shelter-in-place; if evacuating, transport to designated host facility, document on IRIS. Post-storm: facility damage assessment before re-occupancy; notify DHSR MHLC if structural damage.',
            '<b>Power Outage.</b> Distribute flashlights. Verify battery-backup life-safety systems (smoke detectors, fire alarm, security chimes). Discard refrigerated food per FDA 4-hour rule (24-48 hrs for freezer if door stays closed). If power loss expected to exceed 4 hours OR indoor temp drops below 65°F or rises above 80°F, initiate Emergency Relocation Plan. Notify utility, document outage start/end, notify QP. If generator is installed, test monthly under load.',
            '<b>System Failure.</b> Heat loss > 4 hours, water loss > 8 hours, sewer backup, or gas leak (evacuate immediately, call 911) all trigger the Emergency Relocation Plan to the designated host facility.',
            '<b>Lockdown.</b> Secure doors and windows. Hide. Silence phones. Do not open for anyone but law enforcement. Annual drills required.',
            '<b>Emergency Relocation.</b> Primary and secondary host facility identified in writing. Transportation: facility vehicle + staff vehicles + ambulance for medically fragile youth. Locked medication box transported by RN or QP. Youth ID packets (photo, Medicaid card, allergy/med list). Guardian notification within 1 hour. DHSR / LME-MCO notification within 24 hours. Host-facility agreement letters maintained in compliance binder.',
        ]),
        ('Service Orders & Authorization Protocol', [
            '<b>Service Order.</b> The PCP shall serve as the service order when signed by the appropriate professional. If a separate format is used, ensure a separate service order is signed.',
            '<b>Verbal Orders.</b> If a verbal order is obtained, document in the record on the date given: date, who gave, who received, services ordered, and reason for verbal. The professional must countersign within 72 hours.',
            '<b>Authorization.</b> Submit authorization requests to the authorizing entity prior to initiation or continuation per their UM policy.',
            '<b>End-Date Reporting.</b> Notify authorizing entity immediately when youth changes providers or ends service. Follow entity-specified protocol.',
            'Maintain authorization/reauthorization records in an audit-ready file (not in clinical record).',
        ]),
        ('Record Management, Retention, Access & Disclosure Accounting', [
            '<b>Retention.</b> Minors — 12 years after age 18 (until age 30); Adults — 11 years after last encounter. Personnel/Admin records per DHHS schedule. Records not on a schedule require DMH/DD/SUS authorization before destruction.',
            '<b>Record Abandonment.</b> Strictly prohibited. Notify payor, accreditor, and DHHS if suspected. Violations are subject to legal sanctions.',
            '<b>Access.</b> Youth/LRP may access records. If access is restricted, document justification in record. Appeal rights apply.',
            '<b>Accounting of Disclosures.</b> Maintain Form 9 (Accounting of Disclosures Log) for each youth. Include: Name, Record #, Date disclosed, Recipient, Purpose, Description of info, Disclosing party. Retain for minimum 6 years.',
            '<b>Confidentiality.</b> Comply with 42 CFR Part 2 for SUD records. Obtain written ROI for SUD disclosures. Minimum necessary standard applies.',
            '<b>Transport.</b> Only designated staff; secured in locked compartment; documented policy for loss/theft.',
        ]),
    ]

    for i, (title, steps) in enumerate(protocols, start=1):
        story.append(section_heading(i, title))
        story.append(ref_line(anchor=f'Part 2 &middot; Protocol {i}: {title}'))
        for j, step in enumerate(steps, start=1):
            story.append(Paragraph(f'{step}', s_bullet))
        story.append(Spacer(1, 4))

    # ── Protocol 22: Daily Workflow Schedules for All Personnel ────────
    # New in v2.9 — codifies the time-blocked daily routine for every
    # personnel classification so each shift, role, and hand-off has a
    # documented schedule. Displayed as structured narrative followed by
    # a master schedule table summarizing all roles.
    story.append(section_heading(22, 'Daily Workflow Schedules for All Personnel'))
    story.append(ref_line(anchor='Part 2 &middot; Protocol 22: Daily Workflow Schedules for All Personnel'))
    story.append(Paragraph(
        'This protocol codifies the daily workflow schedule for every personnel '
        'classification at Well Spring Intervention LLC. Each role has a '
        'time-blocked routine that aligns with the 24/7 residential operation, '
        'the 2:4 day/evening/overnight staffing ratios required by our staff-secure operating standards, '
        'and the documentation cadences required by the '
        'RMDM and Rule 108. Schedules are templates — actual shift assignments '
        'may flex to cover call-outs, school transportation, medical '
        'appointments, and clinical visits, but every role must complete its '
        'documentation obligations by end of shift. The QP maintains the master '
        'staffing schedule; deviations are tracked on the Shift Change &amp; '
        'Awake Night Watch Log (Form 1).',
        s_body
    ))

    # ── (a) Qualified Professional (QP) ──────────────────────────────
    story.append(Paragraph('(a) Qualified Professional (QP)', s_h2))
    story.append(Paragraph(
        'The QP is the clinical and operational lead on-site. The QP does not '
        'carry a fixed 1:4 youth-supervision caseload; instead, the QP floats '
        'across the program to deliver clinical services, supervise staff, and '
        'ensure documentation compliance. The QP reports to the Clinical '
        'Director per §1.4 and §1.4(a).',
        s_body
    ))
    qp_sched = [
        ('7:00 AM', 'Arrive; review the prior 24-hour Night Watch Log (Form 1) and IRIS queue. Brief with off-going overnight staff. Verify controlled-substance count.'),
        ('7:30 AM', 'Lead shift-change huddle with on-coming DCPs. Assign youth supervision ratios. Review Behavior Support Plans and any overnight incidents.'),
        ('8:00 AM', 'Wake youth per house schedule. Coordinate breakfast and AM medications with the DCP. Confirm school transportation.'),
        ('9:00 AM', 'Begin clinical block: individual therapy sessions, PCP/ISP reviews, family collateral calls, or coordination with the LEA / IEP team.'),
        ('11:00 AM', 'Audit prior day\'s service notes for RMDM compliance (Form 7 template). Flag any backdated, missing, or non-compliant notes for correction before the 24-hour deadline.'),
        ('12:00 PM', 'Lunch (youth supervised by DCP). QP reviews email, prior-authorization requests, and any LME/MCO correspondence.'),
        ('1:00 PM', 'Clinical block continued: CCA assessments, ASAM screenings (if SUD), safety-plan updates, or scheduled psychiatric telehealth visits.'),
        ('3:00 PM', 'Shift-change huddle with on-coming evening DCPs. Brief on any clinical concerns, restrictions, or supervision-level changes.'),
        ('4:00 PM', 'Group therapy or skill-building group (QP leads or co-leads with an AP). Document each youth\'s response in a service note.'),
        ('5:30 PM', 'Family visitation oversight; review approved visitor list; coordinate bag searches with the DCP.'),
        ('7:00 PM', 'Documentation block: complete all clinical service notes for the day, sign PCP addendums, file Form 9 disclosure entries.'),
        ('8:00 PM', 'Final round — verify evening medications administered and MAR initialled. Confirm tomorrow\'s appointments and transportation.'),
        ('9:00 PM', 'Shift-change huddle with overnight DCP. Hand off clinical concerns, supervision-level changes, and any pending IRIS investigations.'),
        ('9:30 PM', 'Depart. On-call QP coverage begins; carry the agency phone until 7:00 AM next day.'),
    ]
    story.append(_schedule_table(qp_sched))
    story.append(Spacer(1, 6))

    # ── (b) Associate Professional (AP) / Paraprofessional (PP) ───────
    story.append(Paragraph('(b) Associate Professional (AP) / Paraprofessional (PP)', s_h2))
    story.append(Paragraph(
        'APs and PPs provide direct behavioral-health services under QP '
        'supervision per §2.2. They carry a 1:4 youth-supervision ratio on '
        'day or evening shift and lead structured clinical and skill-building '
        'activities. APs may co-lead group therapy with the QP.',
        s_body
    ))
    ap_sched = [
        ('7:00 AM', 'Arrive; controlled-substance count with off-going overnight DCP. Review the Night Watch Log and any incident reports from overnight.'),
        ('7:30 AM', 'Shift-change huddle with QP. Receive youth-supervision assignment and BSP talking points for the day.'),
        ('8:00 AM', 'Wake youth; assist with morning hygiene and AM routine. Administer AM medications per MAR (under RN delegation).'),
        ('8:30 AM', 'Breakfast; supervise mealtime behaviors and document any concerns. Coordinate school transportation with the DCP.'),
        ('9:30 AM', 'Structured clinical block: lead or co-lead a skill-building group (coping skills, emotional regulation, social skills). Document each youth\'s participation.'),
        ('11:00 AM', 'Individual check-ins with assigned youth (15 min each). Review BSP goals, address any overnight stressors, update the youth\'s daily log.'),
        ('12:30 PM', 'Lunch supervision; chore rotation; structured free time.'),
        ('2:00 PM', 'Co-lead group therapy with QP (or lead an AP-run activity group). Document interventions and youth response.'),
        ('3:00 PM', 'Shift-change huddle with evening DCP. Hand off youth-supervision assignment, behavior status, and any clinical concerns.'),
        ('3:30 PM', 'Continue with youth supervision. Coordinate homework support, recreational activities, and community outings per ISP goals.'),
        ('5:00 PM', 'Family visitation support (if scheduled). Coordinate bag searches with the DCP; supervise visitation room.'),
        ('6:00 PM', 'Dinner; supervise mealtime. Administer PM medications per MAR.'),
        ('7:30 PM', 'Wind-down routine: hygiene, structured quiet time, journaling, or sensory activities per BSP.'),
        ('9:00 PM', 'Youth bedtime routine. Document the day\'s service note (Form 7) before end of shift.'),
        ('10:00 PM', 'Shift-change huddle with overnight DCP. Brief on each youth\'s emotional status, sleep considerations, and any restrictions.'),
        ('11:00 PM', 'End of shift. On-call AP coverage rotates weekly.'),
    ]
    story.append(_schedule_table(ap_sched))
    story.append(Spacer(1, 6))

    # ── (c) Direct Care Professional (DCP) — Day Shift (7a-3p) ────────
    story.append(Paragraph('(c) Direct Care Professional (DCP) — Day Shift (7a-3p)', s_h2))
    story.append(Paragraph(
        'DCPs carry the primary 1:4 youth-supervision ratio. Day-shift DCPs '
        'focus on morning routine, school transportation, and structured '
        'daytime activities.',
        s_body
    ))
    dcp_day_sched = [
        ('6:45 AM', 'Arrive; clock in. Receive shift-change briefing from overnight DCP. Controlled-substance count verified and signed.'),
        ('7:00 AM', 'Confirm youth headcount; verify all youth are awake and accounted for. Begin AM room inspections.'),
        ('7:30 AM', 'Shift-change huddle with QP and AP. Receive youth-supervision assignment and BSP talking points.'),
        ('8:00 AM', 'Wake any youth still sleeping; assist with morning hygiene. Administer AM medications per MAR.'),
        ('8:30 AM', 'Breakfast; supervise mealtime. Verify each youth eats; document any food refusal or concerns.'),
        ('9:00 AM', 'School transportation: headcount before leaving and upon arrival. Confirm seatbelts. Drop off at school; obtain school behavior report.'),
        ('10:00 AM', 'Return to facility. House chores: assign and supervise cleaning rotations per the chore chart. Document completion.'),
        ('11:00 AM', 'Structured activity block: outdoor time, life-skills lesson, or community outing per ISP goals. Maintain line-of-sight supervision.'),
        ('12:30 PM', 'Lunch; supervise mealtime. Administer midday medications if ordered.'),
        ('1:30 PM', 'Documentation block: complete the daily log for each assigned youth. Note any behavioral incidents, BSP interventions used, and effectiveness.'),
        ('2:00 PM', 'School pickup: headcount; obtain daily behavior report from school staff. Transport back to facility.'),
        ('2:45 PM', 'Shift-change preparation: complete handoff notes for evening DCP. Verify controlled-substance count.'),
        ('3:00 PM', 'Shift-change huddle with evening DCP. Brief on each youth\'s day, school reports, and any incidents. End of shift.'),
    ]
    story.append(_schedule_table(dcp_day_sched))
    story.append(Spacer(1, 6))

    # ── (d) DCP — Evening Shift (3p-11p) ──────────────────────────────
    story.append(Paragraph('(d) Direct Care Professional (DCP) — Evening Shift (3p-11p)', s_h2))
    story.append(Paragraph(
        'Evening-shift DCPs cover the after-school and bedtime routine. They '
        'administer PM medications, supervise dinner and evening activities, '
        'and prepare youth for sleep.',
        s_body
    ))
    dcp_eve_sched = [
        ('2:45 PM', 'Arrive; clock in. Review the prior shift\'s handoff notes and the Night Watch Log.'),
        ('3:00 PM', 'Shift-change huddle with day DCP and QP. Receive youth-supervision assignment, school behavior reports, and any restrictions.'),
        ('3:30 PM', 'Controlled-substance count verified and signed. Receive keys, agency phone, and any visitor approvals.'),
        ('4:00 PM', 'After-school snack; supervised homework time. Coordinate with AP on any scheduled therapy sessions.'),
        ('5:00 PM', 'Family visitation (if scheduled). Conduct bag searches; supervise visitation; document the visit in each youth\'s log.'),
        ('6:00 PM', 'Dinner preparation and mealtime. Administer PM medications per MAR; verify swallowing; check mouth for "cheeking".'),
        ('7:00 PM', 'Evening activity: structured recreation, life-skills lesson, or community outing per ISP goals.'),
        ('8:30 PM', 'Wind-down routine: hygiene, pajamas, quiet activities (reading, journaling, sensory items per BSP).'),
        ('9:30 PM', 'Youth bedtime. Confirm each youth is in their assigned bed. Begin 15-minute room checks (continue into overnight shift).'),
        ('10:00 PM', 'Documentation block: complete the daily log and shift note (Form 7) for each assigned youth. Address any behavioral incidents.'),
        ('10:45 PM', 'Shift-change preparation: complete handoff notes for overnight DCP. Verify controlled-substance count.'),
        ('11:00 PM', 'Shift-change huddle with overnight DCP. Brief on each youth\'s evening, bedtime status, and any concerns. End of shift.'),
    ]
    story.append(_schedule_table(dcp_eve_sched))
    story.append(Spacer(1, 6))

    # ── (e) DCP — Awake Overnight Shift (11p-7a) ──────────────────────
    story.append(Paragraph('(e) Direct Care Professional (DCP) — Awake Overnight Shift (11p-7a)', s_h2))
    story.append(Paragraph(
        'Awake overnight DCPs maintain the 2:4 Level III Staff-Secure ratio (two awake staff for 1–4 youth, per our staff-secure operating standards). Sleeping '
        'is strictly prohibited. 15-minute visual room checks are documented '
        'on the Night Watch Log (Form 1) throughout the shift.',
        s_body
    ))
    dcp_night_sched = [
        ('10:45 PM', 'Arrive; clock in. Review the prior shift\'s handoff notes. Receive keys and agency phone.'),
        ('11:00 PM', 'Shift-change huddle with evening DCP. Receive youth-supervision assignment and any nighttime considerations (sleepwalking, night terrors, etc.).'),
        ('11:15 PM', 'Controlled-substance count verified and signed. Confirm hallway lights remain on. Verify all youth are in their assigned beds.'),
        ('11:30 PM', 'Begin 15-minute room checks (continue throughout the shift). Each check: visually confirm each youth breathing and in bed; initial the Night Watch Log (Form 1).'),
        ('12:00 AM', 'House security check: verify all exterior doors and windows locked. Verify alarm system armed. Document on the Night Watch Log.'),
        ('1:00 AM', 'Administrative block: restock supplies, sanitize common areas, prepare for morning routine (set out breakfast supplies, prep medications for AM count).'),
        ('3:00 AM', 'Continue 15-minute room checks. Engage nighttime wakers quietly and briefly — do not start conversations that escalate arousal. Document any incidents.'),
        ('5:00 AM', 'Begin AM preparations: start coffee, set the table, prepare breakfast menu. Confirm AM medication pull for the day DCP.'),
        ('6:00 AM', 'Final security check. Complete end-of-shift Night Watch Log summary. Document any incidents, AWOL attempts, or medical concerns from overnight.'),
        ('6:45 AM', 'Day-shift DCP arrives. Controlled-substance count verified and signed. Brief on overnight events.'),
        ('7:00 AM', 'Shift-change huddle with day DCP and QP. Hand off any concerns. End of shift.'),
    ]
    story.append(_schedule_table(dcp_night_sched))
    story.append(Spacer(1, 6))

    # ── (f) House Manager ─────────────────────────────────────────────
    story.append(Paragraph('(f) House Manager', s_h2))
    story.append(Paragraph(
        'The House Manager is a senior DCP who supervises day-to-day facility '
        'operations, inventory, maintenance, and the chore system. The House '
        'Manager reports to the QP and works Monday-Friday 9a-5p with on-call '
        'availability.',
        s_body
    ))
    hm_sched = [
        ('9:00 AM', 'Arrive; review the prior 24 hours of Night Watch Logs and incident reports. Brief with the QP on any facility issues.'),
        ('9:30 AM', 'Facility walk-through: inspect all common areas, bedrooms, bathrooms, kitchen, and outdoor space. Document any maintenance needs.'),
        ('10:00 AM', 'Inventory check: food, cleaning supplies, PPE, first-aid supplies. Place orders as needed within the household budget.'),
        ('10:30 AM', 'Coordinate with maintenance vendors for any scheduled repairs or inspections. Document all work orders.'),
        ('11:30 AM', 'Review and update the chore chart. Meet briefly with each youth to assign/reinforce chore expectations.'),
        ('12:30 PM', 'Lunch.'),
        ('1:00 PM', 'Audit the medication cart with the QP and RN (if on-site). Verify MAR completion, controlled-substance log, and expired medication disposal.'),
        ('2:00 PM', 'Compliance audit: check fire-extinguisher tags, smoke-detector test logs, environmental safety logs (Form 5). Schedule any missing drills.'),
        ('3:00 PM', 'Brief with the on-coming evening DCP. Reinforce any facility-related instructions for the shift.'),
        ('4:00 PM', 'Administrative block: file maintenance records, update the household budget tracker, prepare the weekly facility report for the QP.'),
        ('5:00 PM', 'End of shift. On-call availability for facility emergencies (water leak, heating failure, alarm activation) until 9:00 AM next day.'),
    ]
    story.append(_schedule_table(hm_sched))
    story.append(Spacer(1, 6))

    # ── (g) Registered Nurse (RN) ─────────────────────────────────────
    story.append(Paragraph('(g) Registered Nurse (RN)', s_h2))
    story.append(Paragraph(
        'The RN provides medical oversight per §6 and our staff-secure operating standards. '
        'The RN visits the facility at minimum weekly and within 72 hours of '
        'any new admission, and is on-call 24/7 for medical questions and '
        'medication errors.',
        s_body
    ))
    rn_sched = [
        ('9:00 AM', 'Arrive on scheduled visit day. Brief with the QP on any medical concerns, medication changes, or recent incidents.'),
        ('9:30 AM', 'Medication cart audit: verify MAR completion, inspect for expired medications, review any PRN administration patterns.'),
        ('10:00 AM', 'Individual youth health checks: vital signs if ordered, weight checks, skin checks, assessment of any reported symptoms.'),
        ('11:00 AM', 'Coordinate with the prescribing psychiatrist via telehealth or phone. Document any medication changes and update the MAR.'),
        ('12:00 PM', 'Train DCPs on any new medication orders, administration techniques, or delegation updates per our staff-secure operating standards.'),
        ('1:00 PM', 'Documentation block: complete nursing notes in each youth\'s chart. Update the medication administration record. File any new lab orders.'),
        ('2:00 PM', 'Coordinate medical appointments: schedule PCP visits, dental visits, vision screenings, and any specialty referrals.'),
        ('3:00 PM', 'Brief with the QP and House Manager on any medical-action items. Depart facility; on-call coverage continues 24/7.'),
        ('On-Call', 'Available by phone for medication errors, adverse reactions, acute illness triage, and any medical questions. Responds within 15 minutes; documents all calls in the nursing log.'),
    ]
    story.append(_schedule_table(rn_sched))
    story.append(Spacer(1, 6))

    # ── (h) Billing Coordinator ──────────────────────────────────────
    story.append(Paragraph('(h) Billing Coordinator', s_h2))
    story.append(Paragraph(
        'The Billing Coordinator manages Medicaid per-diem billing, '
        'authorization tracking, and suspension-day accounting. The Billing '
        'Coordinator reports to the Executive Director and works Monday-Friday '
        '8a-4p remotely or on-site.',
        s_body
    ))
    bc_sched = [
        ('8:00 AM', 'Arrive; review the prior day\'s admission/discharge log. Confirm Medicaid eligibility for each youth via NCTracks.'),
        ('8:30 AM', 'Process the prior day\'s per-diem billing. Verify each youth was in residence; apply any suspension-day exclusions from Form 4.'),
        ('9:30 AM', 'Track authorization end dates. Submit reauthorization requests to the LME/MCO at least 14 days before expiration.'),
        ('10:30 AM', 'Reconcile any claim denials. Document the reason for each denial and the corrective action taken. Escalate systemic issues to the QP.'),
        ('12:00 PM', 'Lunch.'),
        ('1:00 PM', 'Coordinate with the QP on any youth who were AWOL, hospitalized, or on home pass in the prior 24 hours. Apply billing exclusions per Protocol 16 and Form 4.'),
        ('2:00 PM', 'Audit service-note completion in the EHR. Flag any youth with missing notes from the prior 24 hours; notify the QP for correction before the 7-business-day alteration deadline.'),
        ('3:00 PM', 'Prepare the weekly billing summary for the Executive Director. Include total billable days, suspension days, denials, and pending authorizations.'),
        ('4:00 PM', 'End of shift. On-call availability for billing-related questions during business hours; the QP handles after-hours billing emergencies.'),
    ]
    story.append(_schedule_table(bc_sched))
    story.append(Spacer(1, 6))

    # ── (i) Master Schedule Summary ──────────────────────────────────
    story.append(Paragraph('(i) Master Schedule Summary', s_h2))
    story.append(Paragraph(
        'The table below summarizes the standard shift windows and primary '
        'documentation obligations for each role. All shifts overlap by 15 '
        'minutes to support a structured shift-change huddle and '
        'controlled-substance count.',
        s_body
    ))
    master_data = [
        ['Role', 'Standard Shift', 'Coverage', 'Primary Documentation'],
        ['Qualified Professional (QP)', '7a-9:30p (float)', 'On-site + on-call 24/7', 'Service notes, PCP addendums, Form 9, IRIS reports'],
        ['Associate Professional (AP)', '7a-11p (rotating)', '2:4 staff minimum (Level III Staff-Secure)', 'Service notes, group documentation, BSP updates'],
        ['DCP — Day Shift', '7a-3p', '2:4 staff minimum', 'Daily logs, MAR, Form 1 handoff, Form 7 notes'],
        ['DCP — Evening Shift', '3p-11p', '2:4 staff minimum', 'Daily logs, MAR, Form 1 handoff, Form 7 notes'],
        ['DCP — Awake Overnight', '11p-7a', '2:4 staff minimum (awake, no sleeping)', 'Night Watch Log (Form 1), 15-min room checks, security log'],
        ['House Manager', '9a-5p Mon-Fri', 'On-site + on-call', 'Maintenance log, inventory, Form 5 environmental checks'],
        ['Registered Nurse (RN)', 'Weekly visit + on-call', 'On-call 24/7', 'Nursing notes, MAR updates, delegation training log'],
        ['Billing Coordinator', '8a-4p Mon-Fri', 'On-site or remote', 'Per-diem billing, Form 4 suspensions, auth tracking, weekly summary'],
    ]
    story.append(_master_schedule_table(master_data))
    story.append(Spacer(1, 8))
    story.append(Paragraph(
        '<b>Shift-Change Huddle.</b> Every shift transition (7:00 AM, 3:00 PM, '
        '11:00 PM) begins with a 15-minute overlap during which the off-going '
        'and on-coming staff conduct a controlled-substance count, review any '
        'incident reports from the prior shift, and brief on each youth\'s '
        'clinical and behavioral status. The huddle is documented on Form 1 '
        '(Shift Change &amp; Awake Night Watch Log).',
        s_body
    ))
    story.append(Paragraph(
        '<b>On-Call Coverage.</b> The QP carries the agency phone 24/7 on a '
        'rotating weekly schedule. The RN is on-call 24/7 for medical '
        'questions. The House Manager is on-call for facility emergencies '
        'during off-hours. The Billing Coordinator is reachable during '
        'business hours; the QP handles after-hours billing emergencies. '
        'All on-call responses are logged in the on-call binder with timestamp, '
        'caller, issue, and resolution.',
        s_body
    ))
    story.append(Paragraph(
        '<b>Deviation Policy.</b> Schedule deviations (call-outs, late '
        'arrivals, unplanned overtime) are documented on Form 1. The QP '
        'maintains the master staffing schedule and approves any role '
        'substitution. Per our staff-secure operating standards, ratios must be maintained at '
        'all times; if a replacement is not available, the QP covers in-house '
        'until a replacement arrives. Chronic staffing gaps are reported to '
        'the Clinical Director per §1.4(a) and may trigger a corrective '
        'action plan.',
        s_body
    ))

    return story


def _schedule_table(rows):
    """Helper: render a (time, activity) schedule as a 2-column table."""
    th_time = ParagraphStyle('sch_th_time', fontName=BODY_BOLD, fontSize=9,
                             leading=11, textColor=colors.white, alignment=TA_CENTER)
    th_act = ParagraphStyle('sch_th_act', fontName=BODY_BOLD, fontSize=9,
                            leading=11, textColor=colors.white, alignment=TA_LEFT)
    td_time = ParagraphStyle('sch_td_time', fontName=BODY_BOLD, fontSize=8.5,
                             leading=11, textColor=TEXT_PRIMARY, alignment=TA_CENTER)
    td_act = ParagraphStyle('sch_td_act', fontName=BODY_FONT, fontSize=9,
                            leading=12, textColor=TEXT_PRIMARY, alignment=TA_LEFT)
    data = [[Paragraph('<b>Time</b>', th_time), Paragraph('<b>Activity</b>', th_act)]]
    for t, a in rows:
        data.append([Paragraph(t, td_time), Paragraph(a, td_act)])
    widths = [0.13 * AVAIL_W, 0.87 * AVAIL_W]
    tbl = Table(data, colWidths=widths, hAlign='CENTER', repeatRows=1)
    sc = [
        ('BACKGROUND', (0, 0), (-1, 0), HEADER_FILL),
        ('GRID', (0, 0), (-1, -1), 0.4, BORDER),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
    ]
    for i in range(1, len(data)):
        bg = TABLE_ROW_ODD if i % 2 == 1 else TABLE_ROW_EVEN
        sc.append(('BACKGROUND', (0, i), (-1, i), bg))
    tbl.setStyle(TableStyle(sc))
    return tbl


def _master_schedule_table(rows):
    """Helper: render the master schedule summary table."""
    th = ParagraphStyle('mst_th', fontName=BODY_BOLD, fontSize=8.5,
                        leading=11, textColor=colors.white, alignment=TA_CENTER)
    th_l = ParagraphStyle('mst_th_l', parent=th, alignment=TA_LEFT)
    td = ParagraphStyle('mst_td', fontName=BODY_FONT, fontSize=8.5,
                        leading=11, textColor=TEXT_PRIMARY, alignment=TA_LEFT)
    td_b = ParagraphStyle('mst_td_b', parent=td, fontName=BODY_BOLD)
    data = [[Paragraph(f'<b>{h}</b>', th_l if i > 0 else th) for i, h in enumerate(rows[0])]]
    for row in rows[1:]:
        data.append([Paragraph(row[0], td_b), Paragraph(row[1], td),
                     Paragraph(row[2], td), Paragraph(row[3], td)])
    widths = [0.22 * AVAIL_W, 0.18 * AVAIL_W, 0.20 * AVAIL_W, 0.40 * AVAIL_W]
    tbl = Table(data, colWidths=widths, hAlign='CENTER', repeatRows=1)
    sc = [
        ('BACKGROUND', (0, 0), (-1, 0), HEADER_FILL),
        ('GRID', (0, 0), (-1, -1), 0.4, BORDER),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING', (0, 0), (-1, -1), 4),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
    ]
    for i in range(1, len(data)):
        bg = TABLE_ROW_ODD if i % 2 == 1 else TABLE_ROW_EVEN
        sc.append(('BACKGROUND', (0, i), (-1, i), bg))
    tbl.setStyle(TableStyle(sc))
    return tbl
