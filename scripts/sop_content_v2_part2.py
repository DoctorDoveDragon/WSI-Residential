
# ────────────────────────────────────────────────────────────────────
# Content builders — Part 2: Protocols (21 protocols, RMDM-compliant)
# ────────────────────────────────────────────────────────────────────
from generate_sop import (
    part_divider, section_heading, ref_line, para, bullets,
    Paragraph, Spacer, AVAIL_W, s_bullet,
)


def build_part2():
    story = []
    story.extend(part_divider(
        'PART 2',
        'Actionable Workflows & Protocols',
        'These 21 protocols translate the SOP policies into clear, sequential, step-by-step '
        'actions for daily operations. Each protocol is designed to be referenced quickly '
        'during a shift and followed exactly. Deviations from protocol require QP approval '
        'and must be documented. Protocols 20 and 21 are new in Version 2.0 and address '
        'service orders/authorizations and record management/disclosure accounting per '
        'RMDM requirements.',
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
            '<b>Ratios.</b> 1:4 day and evening. 1:8 overnight. If a staff member calls out, the on-call system activates a replacement; the QP covers in-house if no replacement is available.',
            '<b>Awake Overnight.</b> Sleeping is prohibited. 15-minute visual room checks are documented on the Night Watch Log. Hallway lights remain on. Engage nighttime wakers quietly and briefly — do not start conversations that escalate arousal.',
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
            '<b>Fire.</b> Evacuate immediately. Headcount at the rally point. Call 911. Do not re-enter. Monthly drills required.',
            '<b>Tornado.</b> Move to the interior safe room. Turtle position. Quarterly drills required.',
            '<b>System Failure.</b> Distribute flashlights. If heat loss exceeds 4 hours or water loss exceeds 8 hours, initiate the Emergency Relocation Plan.',
            '<b>Lockdown.</b> Secure doors and windows. Hide. Silence phones. Do not open for anyone but law enforcement. Annual drills required.',
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

    return story
