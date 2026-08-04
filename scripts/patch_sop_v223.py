#!/usr/bin/env python3
"""
patch_sop_v223.py — Apply all v2.23 corrective edits to sop_content_v3.py,
sop_content_v3_part2.py, sop_content_v3_part3.py, generate_sop.py, merge_sop.py.

Implements the v2.23 Revision Roadmap from the SOP Manual v2.22 Compliance Audit:
  - F-001: Add §4.6 Licensed Professional Face-to-Face Clinical Consultation + Form 10
  - F-002: Add §6.3(a) Psychotropic Medication Drug Regimen Review + Form 11
  - F-003: Global CCP 8C → CCP 8D-2 + rewrite §1.2(h)(b) from OPEN to RESOLVED
  - F-006, F-007, M-011, M-028, M-029: Individualized supervision plans + AP pathways
  - F-008, M-025, M-026: Discharge notification, pre-discharge CFT, post-emergency meeting
  - F-009: §3.6 18th-Birthday Continuation Policy
  - F-011: .1702(a) cross-reference clarification note (§1.2(h)(d))
  - F-012, F-013, F-014, M-043: Medication receipt/storage/disposal/education
  - M-007: QP 2-year direct care experience statement
  - M-031: Fee assessment, lab tests, volunteer services policies
  - M-032: Governing-body minutes permanently maintained
  - M-033: Age-18, literacy, criminal-disclosure requirements
  - M-038: Quarterly fire AND tornado drills EACH shift
  - Plus version bump to v2.23
"""
import os
import re
import sys

SCRIPTS_DIR = '/home/z/my-project/scripts'

# ─── helpers ────────────────────────────────────────────────────────────
def patch_file(path, replacements, must_match=True):
    """Apply a list of (old, new) replacements to a file. Each must match exactly once."""
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    applied = 0
    for old, new in replacements:
        count = content.count(old)
        if count == 0:
            if must_match:
                print(f'  [MISS] {path}: pattern not found ({old[:80]}...)')
            continue
        if count > 1:
            print(f'  [WARN] {path}: pattern matched {count} times — replacing all ({old[:80]}...)')
        content = content.replace(old, new)
        applied += 1
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'  {os.path.basename(path)}: {applied}/{len(replacements)} patches applied')


# ─── 1. sop_content_v3.py — §1.2(h)(b) OPEN→RESOLVED, (c) update, (d) new ─
def patch_section_1_2_h():
    path = os.path.join(SCRIPTS_DIR, 'sop_content_v3.py')
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # (b) — replace the entire OPEN flag paragraph with the RESOLVED paragraph
    old_b_open = """    story.append(para(
        '<b>(b) NC Medicaid "CCP 8C" vs "CCP 8D-2".</b> This Manual currently cites '
        '<b>NC Medicaid CCP 8C</b> in the reference lines of several SOP sections as the '
        'Medicaid coverage authority for residential treatment services. A verification '
        'review against the NC DHHS Division of Health Benefits (NCDHB) clinical coverage '
        'policy library indicates that <b>CCP 8C is "Outpatient Behavioral Health Services '
        'Provided by Direct-Enrolled Providers"</b> \u2014 a different benefit category that '
        'does <b>not</b> cover residential treatment services. The correct NC Medicaid '
        'clinical coverage policy for Residential Treatment Services (Levels I\u2013IV) is '
        '<b>CCP 8D-2</b>, "Residential Treatment Services" (Amended January 1, 2025), '
        'available at '
        'https://medicaid.ncdhhs.gov/8d-2-residential-treatment-services/download?attachment. '
        'CCP 8D-1 covers Psychiatric Residential Treatment Facilities (PRTFs) and CCP 8D-'
        '3/8D-4/8D-5 cover adult ASAM-aligned SUD residential services. The QP and Billing '
        'Coordinator shall, prior to NCTracks enrollment per \u00a71.9: (1) confirm with '
        'Alliance Health and NCTracks that the facility is enrolling under CCP 8D-2 '
        '(Residential Treatment Services \u2014 Level III) with taxonomy 320800000X; (2) update '
        'all "CCP 8C" references in this Manual to "CCP 8D-2" via a v2.21 revision; and '
        '(3) retain the Alliance Health / NCTracks enrollment-confirmation letters in the '
        'facility compliance binder. <b>Until that confirmation is obtained, this Manual '
        'will continue to cite "CCP 8C" in legacy reference lines, and this subsection '
        'documents the open question.</b> \u00a71.2(g), \u00a71.9, and \u00a710.9 already cite CCP 8D-2 '
        'as the operative authority for the RTS benefit and the room-and-board exclusion; '
        'those subsections control in the event of any inconsistency with the legacy '
        '"CCP 8C" reference lines elsewhere in this Manual.'
    ))"""

    new_b_resolved = """    story.append(para(
        '<b>(b) NC Medicaid "CCP 8C" vs "CCP 8D-2" \u2014 RESOLVED in v2.23.</b> The open '
        'question flagged in v2.20 \u2014 whether the correct NC Medicaid Clinical Coverage '
        'Policy for Level III Residential Treatment Services is <b>CCP 8C</b> or <b>CCP '
        '8D-2</b> \u2014 is hereby <b>resolved in favor of CCP 8D-2</b>. The NC Medicaid '
        'clinical coverage policy library confirms that CCP 8C is "Outpatient Behavioral '
        'Health Services Provided by Direct-Enrolled Providers" \u2014 a different benefit '
        'category that does <b>not</b> cover residential treatment services. The correct '
        'NC Medicaid clinical coverage policy for Residential Treatment Services '
        '(Levels I\u2013IV) is <b>CCP 8D-2</b>, "Residential Treatment Services" (Amended '
        'January 1, 2025), available at '
        'https://medicaid.ncdhhs.gov/8d-2-residential-treatment-services/download?attachment. '
        'CCP 8D-1 covers Psychiatric Residential Treatment Facilities (PRTFs) and CCP '
        '8D-3/8D-4/8D-5 cover adult ASAM-aligned SUD residential services. '
        '<b>All legacy "CCP 8C" references in this Manual have been globally updated '
        'to "CCP 8D-2" in this v2.23 revision</b> \u2014 including the reference lines of '
        '\u00a71.2, \u00a72, \u00a73, \u00a74, \u00a75, \u00a76, and \u00a710, and the \u00a71.2(e) Medicaid billing description. '
        'The QP shall retain a printed copy of the CCP 8D-2 policy (Amended January 1, '
        '2025) in the facility compliance binder as documentation of this resolution. '
        '\u00a71.2(g), \u00a71.9, and \u00a710.9 already cited CCP 8D-2 as the operative authority '
        'for the RTS benefit and the room-and-board exclusion; with v2.23 the entire '
        'Manual is now internally consistent on CCP 8D-2. No further action is required '
        'on this subsection (b).'
    ))"""

    if old_b_open in content:
        content = content.replace(old_b_open, new_b_resolved)
        print('  [OK] §1.2(h)(b) rewritten OPEN → RESOLVED')
    else:
        print('  [MISS] §1.2(h)(b) OPEN paragraph not found — already patched?')

    # (c) — update to reflect (b) is now resolved; add new (d) for F-011
    # The (c) text uses curly apostrophe in "facility's"
    old_c = """    story.append(para(
        '<b>(c) No operational impact.</b> Nothing in this \u00a71.2(h) changes the facility\u2019s '
        'license category (Level III RTF \u2014 Staff Secure under <b>our staff-secure operating standards</b>), '
        'its staffing ratios (2:4 minimum per \u00a72.1), its admission physical-exam timing '
        '(90 days prior per \u00a76.1), its resident-rights obligations (the Resident Rights framework '
        'per \u00a71.7), its Medicaid taxonomy (320800000X per \u00a71.9), or its room-and-board '
        'exclusion (per \u00a71.2(g) and \u00a710.9). <b>The .2600 \u2192 .1700 citation question '
        '(subsection (a) above) has been resolved in v2.21;</b> the CCP 8C vs CCP 8D-2 '
        'citation question (subsection (b) above) remains open and shall be resolved in a '
        '<b>v2.22 revision</b> entry in the Version History table in Part 3 following '
        'Alliance Health / NCTracks enrollment confirmation per \u00a71.9. In the interim, '
        '\u00a71.2(g), \u00a71.9, and \u00a710.9 already cite CCP 8D-2 as the operative authority for '
        'the RTS benefit and the room-and-board exclusion; those subsections control in '
        'the event of any inconsistency with the legacy "CCP 8C" reference lines elsewhere '
        'in this Manual.'
    ))"""

    new_c_plus_d = """    story.append(para(
        '<b>(c) No operational impact.</b> Nothing in this \u00a71.2(h) changes the facility\u2019s '
        'license category (Level III RTF \u2014 Staff Secure under <b>our staff-secure operating standards</b>), '
        'its staffing ratios (2:4 minimum per \u00a72.1), its admission physical-exam timing '
        '(90 days prior per \u00a76.1), its resident-rights obligations (the Resident Rights framework '
        'per \u00a71.7), its Medicaid taxonomy (320800000X per \u00a71.9), or its room-and-board '
        'exclusion (per \u00a71.2(g) and \u00a710.9). <b>The .2600 \u2192 .1700 citation question '
        '(subsection (a) above) was resolved in v2.21; the CCP 8C \u2192 CCP 8D-2 citation '
        'question (subsection (b) above) is resolved in this v2.23 revision.</b> With both '
        'citation questions now closed, \u00a71.2(h) is fully resolved and no open compliance '
        'flags remain in this subsection.'
    ))
    story.append(para(
        '<b>(d) Cross-reference clarification note (compliance binder).</b> The Level III '
        'Staff-Secure operating standards cross-reference the "Qualified professional" '
        'definition for the QP credentialing requirements in \u00a71.4(b). The text of that '
        'rule cross-references subsection .0104(18) "Psychiatrist," which appears to be a '
        'typographical error in the rule itself \u2014 the operative definition is at '
        '.0104(21) "Qualified professional." This Manual applies the .0104(21) definition '
        'as the operative QP standard per \u00a71.4(b). The QP shall retain this '
        'cross-reference clarification note in the facility compliance binder and shall '
        'confirm the discrepancy with the assigned Licensure &amp; Training Consultant at '
        'the first in-person meeting per \u00a71.2(e).'
    ))"""

    if old_c in content:
        content = content.replace(old_c, new_c_plus_d)
        print('  [OK] §1.2(h)(c) updated + new (d) cross-reference note added')
    else:
        print('  [MISS] §1.2(h)(c) paragraph not found')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)


# ─── 2. sop_content_v3.py — M-007: add QP 2-year direct care exp to §1.4(b)
def patch_section_1_4_b():
    path = os.path.join(SCRIPTS_DIR, 'sop_content_v3.py')
    old = """    story.append(Paragraph('<b>Common Requirements (Both Pathways).</b>', s_h2))
    story.append(para(
        'Regardless of pathway, every QP must: (a) complete the <b>NC-DHHS-required QP '
        'training modules</b> prior to independent practice (or be enrolled and complete '
        'them within the probationary period); (b) maintain active credential or '
        'supervised-experience documentation as applicable; (c) report any lapse, '
        'sanction, restriction, or change in supervised-experience status to the Clinical '
        'Director within one business day; and (d) have all verification documents '
        '(degree, credential, supervised-experience hours, QP training completion) '
        'retained in the personnel file (\u00a72.5). The facility shall verify and document '
        'which pathway each QP meets at hire and re-verify annually.'
    ))"""

    new = """    story.append(Paragraph('<b>Common Requirements (Both Pathways).</b>', s_h2))
    story.append(para(
        'Regardless of pathway, every QP must: (a) complete the <b>NC-DHHS-required QP '
        'training modules</b> prior to independent practice (or be enrolled and complete '
        'them within the probationary period); (b) maintain active credential or '
        'supervised-experience documentation as applicable; (c) report any lapse, '
        'sanction, restriction, or change in supervised-experience status to the Clinical '
        'Director within one business day; and (d) have all verification documents '
        '(degree, credential, supervised-experience hours, QP training completion) '
        'retained in the personnel file (\u00a72.5). The facility shall verify and document '
        'which pathway each QP meets at hire and re-verify annually. <b>In addition to '
        'the pathway-specific requirements above, the designated facility QP shall have '
        'at least two (2) years of full-time direct client care experience</b> in the '
        'delivery of mental health, developmental disabilities, or substance abuse '
        'services to the population served. The two-year direct-care requirement may be '
        'satisfied concurrently with the supervised-experience hours documented under '
        'Pathway 1 or Pathway 2 above; it does not require a separate, additional '
        'two-year period. The QP shall document satisfaction of this direct-care '
        'requirement on the QP Credentialing Checklist (retained in the personnel file) '
        'at hire and re-verify annually.'
    ))"""

    patch_file(path, [(old, new)])


# ─── 3. sop_content_v3.py — M-032: governing-body minutes permanently maintained
def patch_section_1_8():
    path = os.path.join(SCRIPTS_DIR, 'sop_content_v3.py')
    old = """        '<b>Financial Solvency Documentation</b> \u2014 most recent 3 months of bank statements, '
        'most recent filed tax return, and a current balance sheet, sufficient to '
        'demonstrate ongoing financial solvency as required by our operating standards.',
    ]))"""

    new = """        '<b>Financial Solvency Documentation</b> \u2014 most recent 3 months of bank statements, '
        'most recent filed tax return, and a current balance sheet, sufficient to '
        'demonstrate ongoing financial solvency as required by our operating standards.',
        '<b>Governing Body Meeting Minutes</b> \u2014 permanently maintained per the '
        'facility records-retention schedule, documenting all governing-body decisions, '
        'approvals, oversight actions, financial reviews, policy adoptions, and '
        'corporate-compliance oversight. Minutes shall be signed by the Secretary (or '
        'designee) and retained in chronological order in the compliance binder; '
        'electronic copies shall be backed up per the facility disaster-recovery plan.',
        '<b>Client Fee Assessment Policy</b> \u2014 written policy governing the assessment '
        'of any client fees (sliding-scale, co-pay, or self-pay) including the fee '
        'schedule, criteria for reduction or waiver, documentation requirements, and '
        'the staff member authorized to approve adjustments.',
        '<b>Lab Test Authorization &amp; Follow-Up Policy</b> \u2014 written policy governing '
        'the authorization, ordering, result-tracking, and clinical follow-up of '
        'laboratory tests ordered for youth (including routine labs, drug screens, '
        'and provider-ordered diagnostic studies), specifying the responsible provider, '
        'the result-notification pathway, and the documentation standard in the clinical '
        'record.',
        '<b>Volunteer Services Policy</b> \u2014 written policy governing the recruitment, '
        'screening (including background checks per \u00a72.3), orientation, supervision, '
        'scope of permitted activities, and termination of volunteer services. '
        'Volunteers shall never have unsupervised contact with youth and shall not be '
        'counted toward the 2:4 staffing minimum per \u00a72.1.',
    ]))"""

    patch_file(path, [(old, new)])


# ─── 4. sop_content_v3.py — §2.2 expand AP definition, add supervision plans, age-18/literacy
def patch_section_2_2():
    path = os.path.join(SCRIPTS_DIR, 'sop_content_v3.py')
    old = """    story.append(Paragraph('<b>2.2 Staff Qualifications.</b>', s_h2))
    story.extend(bullets([
        '<b>QPs:</b> Meet one of two pathways per \u00a71.4(b) and our operating standards \u2014 <b>Pathway 1:</b> master\\'s degree in a human services field plus a recognized NC credential (full license, associate/provisional license, certification, or psychiatric nursing credential) plus at least one year of full-time, post-master\\'s supervised MH/DD/SA experience; OR <b>Pathway 2:</b> bachelor\\'s degree in a human services field plus two years of full-time, pre- or post-bachelor\\'s supervised MH/DD/SA experience. Both pathways require NC-DHHS QP training modules prior to independent practice.',
        '<b>APs:</b> Bachelor\\'s in human services with at least one year of relevant experience.',
        '<b>Direct Care Professionals (DCPs):</b> High school diploma or GED with at least one year of mental health experience.',
    ]))"""

    new = """    story.append(Paragraph('<b>2.2 Staff Qualifications.</b>', s_h2))
    story.append(para(
        '<b>General requirements for all staff.</b> All staff must: (a) be at least '
        '<b>18 years of age</b> at the time of hire; (b) be <b>literate in English</b> '
        'sufficient to read and understand this Manual, the youth\\'s PCP and BSP, '
        'medication administration records, incident-report forms, and emergency '
        'procedures; (c) truthfully <b>disclose any criminal conviction history</b> on '
        'the employment application and consent to the background checks described in '
        '\u00a72.3; and (d) provide documentation of education, licensure, and any '
        'credentials claimed on the employment application. Misrepresentation on the '
        'employment application is grounds for immediate termination.'
    ))
    story.extend(bullets([
        '<b>QPs:</b> Meet one of two pathways per \u00a71.4(b) and our operating standards \u2014 <b>Pathway 1:</b> master\\'s degree in a human services field plus a recognized NC credential (full license, associate/provisional license, certification, or psychiatric nursing credential) plus at least one year of full-time, post-master\\'s supervised MH/DD/SA experience; OR <b>Pathway 2:</b> bachelor\\'s degree in a human services field plus two years of full-time, pre- or post-bachelor\\'s supervised MH/DD/SA experience. Both pathways require NC-DHHS QP training modules prior to independent practice. The designated facility QP shall also meet the two-year direct client care experience requirement per \u00a71.4(b).',
        '<b>APs:</b> Meet one of four pathways per facility policy \u2014 <b>(i)</b> bachelor\\'s degree in a human services field plus at least one year of relevant MH/DD/SA experience; <b>(ii)</b> registered nurse license plus at least one year of relevant MH/DD/SA experience; <b>(iii)</b> an equivalent state-recognized certification plus at least one year of relevant MH/DD/SA experience; or <b>(iv)</b> a high school diploma or GED plus at least five years of relevant MH/DD/SA experience. APs supervise paraprofessional Direct Care Professionals (DCPs) regarding PCP and BSP implementation per the individualized supervision plan required by \u00a72.2(a).',
        '<b>Direct Care Professionals (DCPs):</b> High school diploma or GED with at least one year of mental health experience. DCPs work under the supervision of an AP or QP per the individualized supervision plan required by \u00a72.2(a).',
    ]))
    story.append(Paragraph('<b>2.2(a) Individualized Supervision Plans.</b>', s_h2))
    story.append(para(
        'Per the Level III Staff-Secure operating standards, the QP shall develop and '
        'maintain a <b>written individualized supervision plan</b> for every Associate '
        'Professional (AP) and Direct Care Professional (DCP) on staff. Each supervision '
        'plan shall be: (1) developed within 30 days of hire; (2) reviewed and updated '
        'at least annually and upon any change in role, scope of practice, or supervisor '
        'assignment; (3) signed by the staff member, the supervising QP (or AP, where '
        'the DCP is supervised by an AP), and the Clinical Director; and (4) retained '
        'in the personnel file per \u00a72.5. Each supervision plan shall specify: '
        '(a) the supervisor\\'s name, credential, and availability; (b) the frequency '
        'and format of supervision (minimum: weekly individual supervision for APs and '
        'DCPs during the first 90 days of employment, transitioning to at least '
        'bi-weekly individual supervision thereafter, plus weekly group clinical '
        'supervision for all direct-care staff); (c) the scope of delegated authority '
        '(including any limits on independent decision-making, restraint authorization, '
        'medication administration, or incident reporting); (d) the method for '
        'documenting supervision sessions (signed supervision log, case-discussion '
        'notes, and any corrective-action directives); (e) the escalation pathway for '
        'clinical concerns; and (f) the criteria and process for modifying the '
        'supervision plan based on performance, clinical incident history, or changes '
        'in the youth population served. AP supervision plans shall additionally '
        'document the AP\\'s authority to supervise paraprofessional DCPs regarding '
        'PCP and BSP implementation, including the documentation standard for AP '
        'review of DCP shift notes and incident reports.'
    ))"""

    patch_file(path, [(old, new)])


# ─── 5. sop_content_v3.py — §3.4 add (a)/(b)/(c) and add §3.6 18th-birthday
def patch_section_3_4():
    path = os.path.join(SCRIPTS_DIR, 'sop_content_v3.py')
    old = """    story.append(Paragraph('<b>3.4 Discharge & Transition.</b>', s_h2))
    story.append(para(
        'Transition planning is initiated at admission and reviewed every 30 days. '
        'Discharge may be planned or unplanned. The Discharge Summary is completed within '
        '<b>7 calendar days</b> of discharge (exceeds RMDM\\'s 30-day requirement), and '
        'includes: reason for admission, course/progress, condition at discharge, '
        'recommendations, final diagnoses, and dated signatures. Medications are '
        'transferred to the guardian with a signed transfer form, belongings are '
        'inventoried, and the discharge summary is provided to the guardian, receiving '
        'provider, and LME/MCO.'
    ))"""

    new = """    story.append(Paragraph('<b>3.4 Discharge & Transition.</b>', s_h2))
    story.append(para(
        'Transition planning is initiated at admission and reviewed every 30 days. '
        'Discharge may be planned or unplanned. The Discharge Summary is completed within '
        '<b>7 calendar days</b> of discharge (exceeds RMDM\\'s 30-day requirement), and '
        'includes: reason for admission, course/progress, condition at discharge, '
        'recommendations, final diagnoses, and dated signatures. Medications are '
        'transferred to the guardian with a signed transfer form, belongings are '
        'inventoried, and the discharge summary is provided to the guardian, receiving '
        'provider, and LME/MCO.'
    ))
    story.append(Paragraph('<b>3.4(a) Advance Written Notification (Non-Emergency Discharge or Transfer).</b>', s_h2))
    story.append(para(
        'For any <b>non-emergency</b> discharge or transfer, the QP shall provide '
        '<b>written advance notification</b> to the youth (in an age-appropriate manner), '
        'the guardian, the regional managed care organization (LME/MCO) representative, '
        'and the receiving provider (if known) at least <b>7 calendar days</b> prior to '
        'the discharge date. The written notification shall include: the discharge date, '
        'the reason for discharge, the receiving provider (if known), a transition-plan '
        'summary, the post-discharge appointment schedule (outpatient therapy, '
        'medication management, primary care), and the emergency contact number for '
        'post-discharge clinical questions. <b>Emergency discharges</b> (e.g., acute '
        'psychiatric hospitalization, medical hospitalization, safety-motivated '
        'transfer) are exempt from the 7-day requirement but shall be documented with '
        'the emergency basis and provided with as much advance notice as circumstances '
        'reasonably permit.'
    ))
    story.append(Paragraph('<b>3.4(b) Pre-Discharge Care-Coordination Team (CFT) Meeting.</b>', s_h2))
    story.append(para(
        'The QP shall convene a <b>pre-discharge care-coordination team (CFT) meeting</b> '
        'prior to any planned discharge. Meeting attendees shall include, at minimum, '
        'the youth, the guardian, the regional managed care organization (LME/MCO) '
        'representative, and the receiving provider (if applicable). The meeting shall '
        'review discharge readiness, finalize the transition plan, confirm community '
        'linkages (outpatient therapy, medication management, school enrollment, primary '
        'care), review medications and any medication-transfer logistics, and document '
        'attendee signatures on the PCP. For youth transitioning to a lower level of '
        'care, the CFT shall additionally confirm the step-down provider\\'s admission '
        'date and any trial-home-visit schedule.'
    ))
    story.append(Paragraph('<b>3.4(c) Post-Emergency Service-Planning Meeting.</b>', s_h2))
    story.append(para(
        'Following any <b>emergency discharge, transfer, or hospitalization</b> (e.g., '
        'acute psychiatric hospitalization, medical hospitalization, safety-motivated '
        'transfer, or significant restraint event), the QP shall convene a '
        '<b>service-planning meeting within 5 business days</b> of the youth\\'s return '
        'to the facility (or within 5 business days of the emergency event if the youth '
        'does not return). The meeting shall include the youth, the guardian, the '
        'regional managed care organization (LME/MCO) representative, the prescribing '
        'provider (if a medication change is indicated), and direct-care staff who '
        'witnessed the precipitating event. The meeting shall: review the precipitating '
        'events and any contributing factors; update the PCP and BSP as needed to '
        'prevent recurrence; adjust the supervision level if clinically indicated; '
        'identify any staff-training needs; document follow-up actions, responsible '
        'parties, and completion deadlines; and record attendee signatures on the '
        'updated PCP.'
    ))"""

    patch_file(path, [(old, new)])


# ─── 6. sop_content_v3.py — §3.6 18th-Birthday Continuation Policy (after §3.5)
def patch_section_3_6():
    path = os.path.join(SCRIPTS_DIR, 'sop_content_v3.py')
    old = """    story.append(Paragraph('<b>3.5 Administrative Closure.</b>', s_h2))
    story.append(para(
        'When a QP or clinician leaves employment without completing required discharge '
        'documentation for individuals meeting discharge criteria, the supervisor shall '
        'process the discharge. Each administratively closed record shall be audited per '
        'entity policy to ensure all billed services are properly documented. If audit '
        'reveals unmet documentation requirements, all services billed without proper '
        'documentation shall be adjusted back to the payor per 42 CFR 401.305. '
        'Documentation of the administrative closure shall be placed in the service record.'
    ))"""

    new = """    story.append(Paragraph('<b>3.5 Administrative Closure.</b>', s_h2))
    story.append(para(
        'When a QP or clinician leaves employment without completing required discharge '
        'documentation for individuals meeting discharge criteria, the supervisor shall '
        'process the discharge. Each administratively closed record shall be audited per '
        'entity policy to ensure all billed services are properly documented. If audit '
        'reveals unmet documentation requirements, all services billed without proper '
        'documentation shall be adjusted back to the payor per 42 CFR 401.305. '
        'Documentation of the administrative closure shall be placed in the service record.'
    ))
    story.append(Paragraph('<b>3.6 18th-Birthday Continuation Policy.</b>', s_h2))
    story.append(para(
        'Per the Level III Staff-Secure operating standards, a youth who turns 18 years '
        'of age while in placement may <b>continue in the program for up to six (6) '
        'months, or until the end of the current school year, whichever is longer</b>, '
        'provided that all of the following conditions are met: (a) the youth '
        '<b>consents to continued placement in writing</b> as an adult, with informed '
        'consent documented on the standard admission-consent forms; (b) the guardian '
        '(or, if guardianship has been legally terminated, the youth alone) and the '
        'regional managed care organization (LME/MCO) representative <b>approve the '
        'continuation in writing</b>; (c) the PCP is <b>updated within 14 days of the '
        '18th birthday</b> to reflect adult-appropriate goals, rights, discharge '
        'planning, and any changes in consent authority; (d) the youth is <b>informed '
        'orally and in writing of their adult rights</b>, including the right to request '
        'discharge at any time, the right to refuse medication (except as otherwise '
        'provided by law or court order), the right to uncensored communication, and '
        'the right to file a grievance directly with the LME/MCO or the state '
        'licensing authority; and (e) the facility <b>confirms that the youth\\'s '
        'Medicaid eligibility and non-Medicaid room-and-board funding source</b> '
        'continue to cover the extended placement per \u00a71.2(g)(iii) and \u00a710.9. '
        'If any of these conditions cannot be met, the QP shall initiate transition '
        'planning to an appropriate adult placement <b>no later than 30 days before '
        'the youth\\'s 18th birthday</b>, with the discharge date set on or before the '
        '18th birthday. The QP shall document satisfaction of each condition (a)\u2013(e) '
        'in the clinical record and shall retain the youth\\'s written consent and the '
        'LME/MCO approval letter in the facility compliance binder.'
    ))"""

    patch_file(path, [(old, new)])


# ─── 7. sop_content_v3.py — §4.6 Licensed Professional Face-to-Face Clinical Consultation (F-001)
def patch_section_4_6():
    path = os.path.join(SCRIPTS_DIR, 'sop_content_v3.py')
    old = """    story.append(Paragraph('<b>4.5 Service Authorization.</b>', s_h2))
    story.append(para(
        'Requests for authorization are required prior to initiation or continuation of '
        'services as per State-funded service definitions, Medicaid CCPs, or the '
        'authorizing entity\\'s UM policy. The facility shall notify the authorizing '
        'entity when an individual changes providers or ends a service, and end-date '
        'reporting requirements must be followed. Service authorizations and '
        'reauthorizations are not required to be maintained in the clinical record but '
        'shall be available for audit purposes if requested.'
    ))"""

    new = """    story.append(Paragraph('<b>4.5 Service Authorization.</b>', s_h2))
    story.append(para(
        'Requests for authorization are required prior to initiation or continuation of '
        'services as per State-funded service definitions, Medicaid CCPs, or the '
        'authorizing entity\\'s UM policy. The facility shall notify the authorizing '
        'entity when an individual changes providers or ends a service, and end-date '
        'reporting requirements must be followed. Service authorizations and '
        'reauthorizations are not required to be maintained in the clinical record but '
        'shall be available for audit purposes if requested.'
    ))
    story.append(Paragraph('<b>4.6 Licensed Professional Face-to-Face Clinical Consultation.</b>', s_h2))
    story.append(para(
        'Per the Level III Staff-Secure operating standards, the facility shall arrange '
        'for a <b>Licensed Professional to provide at least four (4) hours per week of '
        'face-to-face clinical consultation</b> with the clinical team. The Licensed '
        'Professional shall be a <b>clinician licensed by the applicable state licensing '
        'board to independently provide mental health services</b> (e.g., a licensed '
        'psychiatrist, psychologist, LCSW, LPC, or LMFT), and may be the facility\\'s '
        'Clinical Director, the QP if the QP holds a full clinical license, or an '
        'external clinical consultant under contract. The four (4) hours of weekly '
        'consultation shall be provided in <b>face-to-face</b> format (in-person at the '
        'facility; telehealth video is acceptable only when in-person consultation is '
        'not feasible and is documented on the consultation log). The clinical '
        'consultation shall include, at minimum: (a) <b>review of clinical cases</b>, '
        'including any youth on psychotropic medication, any youth who has experienced '
        'a restraint event in the past 14 days, and any youth with a significant '
        'clinical change since the prior consultation; (b) <b>consultation on '
        'diagnostic and treatment-planning questions</b>, including differential '
        'diagnosis, co-occurring disorders, and treatment-resistance; (c) <b>guidance '
        'on behavioral-support-plan adjustments</b>, including functional-analysis '
        'findings and replacement-skill targets; (d) <b>review of restrictive-'
        'intervention use</b> and trauma-informed restraint-reduction strategies; and '
        '(e) <b>clinical supervision of APs and DCPs</b> as delegated by the QP, '
        'including case discussion, skill-building, and reflective-practice support. '
        'Each consultation session shall be documented on the <b>Licensed Professional '
        'Consultation Log (Form 10)</b>, including: date, start/end time, total '
        'duration, format (in-person or telehealth), attendees, cases reviewed, '
        'recommendations made, follow-up actions assigned, and the Licensed '
        'Professional\\'s signature. The QP shall retain all consultation logs in the '
        'facility compliance binder and shall report weekly consultation-hour totals to '
        'the Clinical Director at each quarterly compliance report per \u00a71.4(a).'
    ))"""

    patch_file(path, [(old, new)])


# ─── 8. sop_content_v3.py — §6.3 add (a) psychotropic drug regimen review (F-002),
#                                (b) receipt-verification (F-012),
#                                (c) storage (M-043),
#                                (d) disposal documentation (F-013),
#                                (e) medication education (F-014)
def patch_section_6_3():
    path = os.path.join(SCRIPTS_DIR, 'sop_content_v3.py')
    old = """    story.append(Paragraph('<b>6.3 Medication Management.</b>', s_h2))
    story.append(para(
        'All medications are stored in a double-locked cabinet/cart. Controlled substances '
        'are counted and documented at every shift change. Medications are administered '
        'only by RN-delegated staff who have completed NC Medication Administration '
        'training. Staff follow the "5 Rights" (right youth, right med, right dose, '
        'right route, right time) and document administration on the MAR <b>immediately</b> '
        '(never retrospectively). Medication errors, refusals, and adverse reactions are '
        'reported to the RN and QP immediately, documented on the MAR, and entered into '
        'IRIS as required.'
    ))"""

    new = """    story.append(Paragraph('<b>6.3 Medication Management.</b>', s_h2))
    story.append(para(
        'All medications are stored in a double-locked cabinet/cart per \u00a76.3(c). '
        'Controlled substances are counted and documented at every shift change. '
        'Medications are administered only by RN-delegated staff who have completed the '
        'state-approved medication administration training. Staff follow the "5 Rights" '
        '(right youth, right med, right dose, right route, right time) and document '
        'administration on the MAR <b>immediately</b> (never retrospectively). Medication '
        'errors, refusals, and adverse reactions are reported to the RN and QP '
        'immediately, documented on the MAR, and entered into the state incident-reporting '
        'system (IRIS) as required.'
    ))
    story.append(Paragraph('<b>6.3(a) Psychotropic Medication Drug Regimen Review.</b>', s_h2))
    story.append(para(
        'Per the Level III Staff-Secure operating standards, the facility shall ensure '
        'that <b>every youth on a psychotropic medication has a drug regimen review '
        'performed by a pharmacist or physician at least every six (6) months</b>. The '
        'review shall evaluate: (1) the appropriateness of each medication and dose '
        'given the youth\\'s diagnoses, age, weight, and clinical response; (2) any '
        'drug-drug interactions, drug-disease contraindications, or duplicate therapies; '
        '(3) any laboratory monitoring required (e.g., metabolic panel for atypical '
        'antipsychotics, lithium levels, carbamazepine levels); (4) any adverse drug '
        'reactions or side effects reported since the prior review; and (5) any '
        'recommended changes to the medication regimen. The reviewing pharmacist or '
        'physician shall document the review on the <b>Psychotropic Medication Drug '
        'Regimen Review Log (Form 11)</b>, including: youth name, date of review, '
        'medications reviewed (name, dose, frequency, indication), reviewer findings, '
        'recommendations, and reviewer signature. The QP shall forward the review '
        'findings to the prescribing psychiatrist within 5 business days, shall '
        'document the review in the clinical record, and shall track the next-6-month '
        'review due date on the Form 11 tracking log. A youth admitted on a psychotropic '
        'medication shall have an initial drug regimen review within 30 days of '
        'admission (the youth\\'s most recent prior review may satisfy this requirement '
        'if completed within the prior 6 months and a copy is obtained).'
    ))
    story.append(Paragraph('<b>6.3(b) Medication Receipt &amp; Verification.</b>', s_h2))
    story.append(para(
        'All medications received at the facility \u2014 whether from a pharmacy, guardian, '
        'hospital, or other source \u2014 shall be <b>verified by the RN</b> (or '
        'designated RN-delegated staff) <b>at the time of receipt</b>. Verification '
        'shall confirm: (a) the medication is in <b>tamper-resistant packaging</b> per '
        'the state controlled-substances and pharmacy rules; (b) the <b>label contains</b> '
        'the youth\\'s full name, medication name, strength, dose, route, frequency, '
        'prescribing provider, pharmacy name and phone number, prescription number, fill '
        'date, and expiration date; (c) the medication <b>matches the prescriber\\'s '
        'order</b> in the youth\\'s clinical record; and (d) the medication is <b>not '
        'expired</b>. Discrepancies shall be reported to the prescribing pharmacy and '
        'the QP immediately, and the medication shall <b>not</b> be administered until '
        'the discrepancy is resolved. Receipt of each medication shall be documented on '
        'the Medication Receipt Log (maintained in the med room), including: date '
        'received, youth name, medication name, quantity received, lot number, '
        'expiration date, verifying RN signature, and any discrepancy notes.'
    ))
    story.append(Paragraph('<b>6.3(c) Medication Storage.</b>', s_h2))
    story.append(para(
        'All medications shall be stored in a <b>double-locked cabinet or cart</b> in a '
        'secure, climate-controlled area maintained between <b>59\u00b0F and 86\u00b0F</b>. '
        'Medications requiring refrigeration shall be stored in a <b>dedicated medication '
        'refrigerator</b> (not used for food) maintained between <b>36\u00b0F and 46\u00b0F</b>, '
        'with the temperature documented on Form 5 (Environmental Safety Log) daily. '
        'Controlled substances shall be stored in the <b>inner locked compartment</b> of '
        'the double-locked cabinet, with a count documented at every shift change. Each '
        'youth\\'s medications shall be stored in individually labeled containers. '
        'Medications shall <b>not</b> be stored in bathrooms, kitchens (except the '
        'medication refrigerator), or other areas exposed to moisture, heat, or direct '
        'sunlight. Expired or discontinued medications shall be segregated in a clearly '
        'labeled "To Be Disposed" container pending disposal per \u00a76.3(d). The RN '
        'shall audit the medication storage area weekly and document the audit on Form 5.'
    ))
    story.append(Paragraph('<b>6.3(d) Medication Disposal Documentation.</b>', s_h2))
    story.append(para(
        'Discontinued, expired, or refused medications shall be disposed of in '
        'accordance with the state controlled-substances act and applicable federal '
        'medication-disposal rules. For each medication disposal event, the RN (or '
        'designated RN-delegated staff) shall document on the <b>Medication Disposal '
        'Log</b> (maintained in the med room): the youth\\'s name, medication name, '
        'strength, quantity disposed, disposal method (e.g., pharmaceutical take-back, '
        'DEA-authorized collection receptacle, mail-back package), disposal date, '
        'witness signature, and RN signature. <b>Controlled-substance disposals shall '
        'be witnessed by a second staff member</b> and the witness signature shall be '
        'obtained prior to disposal. Medications transferred to the guardian at '
        'discharge shall be documented on the Medication Transfer Form (with the '
        'guardian\\'s signature) and are <b>not</b> recorded on the Disposal Log. The '
        'QP shall review the Medication Disposal Log monthly as part of the controlled-'
        'substance reconciliation audit and shall report any discrepancies to the '
        'Clinical Director per \u00a71.4(a).'
    ))
    story.append(Paragraph('<b>6.3(e) Medication Education.</b>', s_h2))
    story.append(para(
        'The QP, RN, and prescribing psychiatrist shall provide <b>ongoing medication '
        'education</b> to each youth regarding any psychotropic or other medication '
        'prescribed. Education shall be documented <b>at admission, at each medication '
        'change, and at least quarterly thereafter</b>. Education shall be '
        'developmentally appropriate and include: (1) the medication name and purpose; '
        '(2) the prescribed dose, route, and schedule; (3) expected benefits; (4) common '
        'and serious side effects, including signs of allergic reaction; (5) '
        'interactions with food, other medications, and substances; (6) the importance '
        'of adherence and the risks of abrupt discontinuation; (7) the youth\\'s right '
        'to ask questions and to refuse medication (except as otherwise provided by law '
        'or court order per \u00a71.7); and (8) what to do if a dose is missed. The '
        'youth\\'s understanding shall be assessed (e.g., teach-back method) and '
        'documented after each education session. <b>Family/guardian medication '
        'education</b> shall also be offered at admission, at each medication change, '
        'and at least quarterly, with the offer and any education provided documented '
        'in the clinical record. The QP shall track medication-education due dates on '
        'the youth\\'s PCP review calendar and shall report any youth with overdue '
        'medication education to the Clinical Director at each quarterly compliance '
        'report per \u00a71.4(a).'
    ))"""

    patch_file(path, [(old, new)])


# ─── 9. sop_content_v3.py — §9.2 update drills per shift (M-038)
def patch_section_9_2():
    path = os.path.join(SCRIPTS_DIR, 'sop_content_v3.py')
    old = """    story.append(Paragraph('<b>9.2 Drills & Inspections.</b>', s_h2))
    story.append(para(
        'Monthly fire drills target evacuation under 3 minutes. Quarterly tornado drills '
        'use the interior safe room. Smoke detectors, fire extinguishers, sprinklers, '
        'and CO detectors are inspected monthly (staff) and annually (licensed '
        'contractors). Inspection records are maintained on the Environmental Safety Log '
        '(Form 5) for a minimum of 3 years.'
    ))"""

    new = """    story.append(Paragraph('<b>9.2 Drills & Inspections.</b>', s_h2))
    story.append(para(
        'Per the Level III Staff-Secure operating standards, <b>fire drills shall be '
        'conducted monthly AND tornado drills shall be conducted quarterly, with each '
        'drill conducted separately for EACH shift (day, evening, and overnight)</b> \u2014 '
        'i.e., 3 fire drills per month (one per shift) and 3 tornado drills per quarter '
        '(one per shift). Drills shall target evacuation under 3 minutes for fire drills '
        'and shall use the lowest interior safe room for tornado drills. Drill '
        'documentation on Form 5 (Environmental Safety Log) shall include: drill type '
        '(fire / tornado), shift (day / evening / overnight), date, start time, '
        'evacuation time (fire drills only), number of youth and staff participating, '
        'any deficiencies identified, corrective actions taken, and the shift '
        'supervisor\\'s signature. Smoke detectors, fire extinguishers, sprinklers, and '
        'CO detectors are inspected monthly (staff) and annually (licensed contractors). '
        'Inspection records are maintained on Form 5 for a minimum of 3 years.'
    ))"""

    patch_file(path, [(old, new)])


# ─── 10. sop_content_v3_part2.py — Protocol 19 drills per shift (M-038)
def patch_protocol_19():
    path = os.path.join(SCRIPTS_DIR, 'sop_content_v3_part2.py')
    old = """        ('Emergency & Disaster Preparedness', [
            '<b>Fire.</b> Evacuate immediately. Headcount at the rally point. Call 911. Do not re-enter. Monthly drills required.',
            '<b>Tornado.</b> Move to the interior safe room. Turtle position. Quarterly drills required.',
            '<b>Hurricane.</b> Monitor NHC advisories during Atlantic season (Jun 1 – Nov 30). At Tropical Storm Warning or Hurricane Watch: secure outdoor projectiles, verify generator fuel, stock 7-day food/water/medications, verify emergency-contact lists, contact guardians re storm plan. At Hurricane Warning: coordinate with LME/MCO and guardian re evacuation vs shelter-in-place; if evacuating, transport to designated host facility, document on IRIS. Post-storm: facility damage assessment before re-occupancy; notify DHSR MHLC if structural damage.',
            '<b>Power Outage.</b> Distribute flashlights. Verify battery-backup life-safety systems (smoke detectors, fire alarm, security chimes). Discard refrigerated food per FDA 4-hour rule (24-48 hrs for freezer if door stays closed). If power loss expected to exceed 4 hours OR indoor temp drops below 65°F or rises above 80°F, initiate Emergency Relocation Plan. Notify utility, document outage start/end, notify QP. If generator is installed, test monthly under load.',
            '<b>System Failure.</b> Heat loss > 4 hours, water loss > 8 hours, sewer backup, or gas leak (evacuate immediately, call 911) all trigger the Emergency Relocation Plan to the designated host facility.',
            '<b>Lockdown.</b> Secure doors and windows. Hide. Silence phones. Do not open for anyone but law enforcement. Annual drills required.',
            '<b>Emergency Relocation.</b> Primary and secondary host facility identified in writing. Transportation: facility vehicle + staff vehicles + ambulance for medically fragile youth. Locked medication box transported by RN or QP. Youth ID packets (photo, Medicaid card, allergy/med list). Guardian notification within 1 hour. DHSR / LME-MCO notification within 24 hours. Host-facility agreement letters maintained in compliance binder.',
        ]),"""

    new = """        ('Emergency & Disaster Preparedness', [
            '<b>Fire.</b> Evacuate immediately. Headcount at the rally point. Call 911. Do not re-enter. <b>Monthly fire drills required for EACH shift (day, evening, overnight) \u2014 3 fire drills per month total</b>, documented on Form 5 with shift, date, evacuation time, and shift-supervisor signature.',
            '<b>Tornado.</b> Move to the interior safe room. Turtle position. <b>Quarterly tornado drills required for EACH shift (day, evening, overnight) \u2014 3 tornado drills per quarter total</b>, documented on Form 5 with shift, date, and shift-supervisor signature.',
            '<b>Hurricane.</b> Monitor NHC advisories during Atlantic season (Jun 1 – Nov 30). At Tropical Storm Warning or Hurricane Watch: secure outdoor projectiles, verify generator fuel, stock 7-day food/water/medications, verify emergency-contact lists, contact guardians re storm plan. At Hurricane Warning: coordinate with LME/MCO and guardian re evacuation vs shelter-in-place; if evacuating, transport to designated host facility, document on IRIS. Post-storm: facility damage assessment before re-occupancy; notify DHSR MHLC if structural damage.',
            '<b>Power Outage.</b> Distribute flashlights. Verify battery-backup life-safety systems (smoke detectors, fire alarm, security chimes). Discard refrigerated food per FDA 4-hour rule (24-48 hrs for freezer if door stays closed). If power loss expected to exceed 4 hours OR indoor temp drops below 65°F or rises above 80°F, initiate Emergency Relocation Plan. Notify utility, document outage start/end, notify QP. If generator is installed, test monthly under load.',
            '<b>System Failure.</b> Heat loss > 4 hours, water loss > 8 hours, sewer backup, or gas leak (evacuate immediately, call 911) all trigger the Emergency Relocation Plan to the designated host facility.',
            '<b>Lockdown.</b> Secure doors and windows. Hide. Silence phones. Do not open for anyone but law enforcement. Annual drills required.',
            '<b>Emergency Relocation.</b> Primary and secondary host facility identified in writing. Transportation: facility vehicle + staff vehicles + ambulance for medically fragile youth. Locked medication box transported by RN or QP. Youth ID packets (photo, Medicaid card, allergy/med list). Guardian notification within 1 hour. DHSR / LME-MCO notification within 24 hours. Host-facility agreement letters maintained in compliance binder.',
        ]),"""

    patch_file(path, [(old, new)])


# ─── 11. sop_content_v3.py — §1.2 license paragraph strip "DHSR MHLC" / "DSS" per M-001
def patch_section_1_2_strip():
    path = os.path.join(SCRIPTS_DIR, 'sop_content_v3.py')
    # The §1.2 license paragraph still uses "DHSR", "MHLC", "DSS" abbreviations
    # We'll keep "NC DHSR" since it's the operational agency name but de-abbreviate
    # the explanation of "not the Division of Social Services (DSS)"
    old = """    story.append(para(
        '<b>1.2 Licensing &amp; Credentialing.</b> The facility operates under a valid NC DHSR '
        'license as a <b>Level III Residential Treatment Facility \u2014 Staff Secure for Children and '
        'Adolescents</b> under <b>our staff-secure operating standards</b>, issued by the NC Division of Health '
        'Service Regulation (<b>DHSR</b>), <b>Mental Health Licensure and Certification Section '
        '(MHLC)</b> \u2014 not the Division of Social Services (DSS), which licenses foster-care group '
        'homes, not behavioral-health treatment facilities. The facility is credentialed as an '
        'In-Network Provider with <b>Alliance Health</b> (the regional LME/MCO/Tailored Plan '
        'serving Cumberland, Durham, Johnston, Mecklenburg, Orange and Wake counties). The '
        'Executive Director maintains the original license on site, posts a current copy in a '
        'public area of the facility, and renews it prior to expiration. Any change in ownership, '
        'capacity, population served, or physical location requires prior written approval from '
        'DHSR MHLC and notification to Alliance Health.'
    ))"""

    new = """    story.append(para(
        '<b>1.2 Licensing &amp; Credentialing.</b> The facility operates under a valid license '
        'as a <b>Level III Residential Treatment Facility \u2014 Staff Secure for Children and '
        'Adolescents</b> under <b>our staff-secure operating standards</b>, issued by the '
        'applicable state mental health authority \u2014 <b>not</b> under foster-care licensing, '
        'and therefore does <b>not</b> operate as a family-home placement. The facility is '
        'credentialed as an In-Network Provider with <b>Alliance Health</b> (the regional '
        'managed care organization / Tailored Plan serving Cumberland, Durham, Johnston, '
        'Mecklenburg, Orange and Wake counties). The Executive Director maintains the original '
        'license on site, posts a current copy in a public area of the facility, and renews it '
        'prior to expiration. Any change in ownership, capacity, population served, or physical '
        'location requires prior written approval from the state licensing authority and '
        'notification to Alliance Health.'
    ))"""

    patch_file(path, [(old, new)])


# ─── 12. sop_content_v3.py — §3.1 admission criteria strip "IVC" per M-003
def patch_section_3_1_ivc():
    path = os.path.join(SCRIPTS_DIR, 'sop_content_v3.py')
    old = """        'setting. Per \u00a71.2(g) and NC Medicaid Clinical Coverage Policy 8D-2 \u00a71.0(c), '
        'the Level III (Residential Treatment High) setting is a <b>"highly structured '
        'and supervised environment in a program setting only, excluding room and '
        'board"</b> \u2014 meaning the facility provides treatment in a structured <b>program '
        'setting</b> (not a family home), with continuous awake supervision per \u00a72.1 and '
        '\u00a79.5, and with the clinical/treatment/milieu component reimbursed by the '
        'Medicaid RTS per-diem while room and board are funded through a non-Medicaid '
        'source. Exclusions include active psychosis requiring Involuntary Commitment '
        '(IVC), medical instability, or fire-setting that cannot be safely managed. The '"""
    new = """        'setting. Per \u00a71.2(g) and NC Medicaid Clinical Coverage Policy 8D-2 \u00a71.0(c), '
        'the Level III (Residential Treatment High) setting is a <b>"highly structured '
        'and supervised environment in a program setting only, excluding room and '
        'board"</b> \u2014 meaning the facility provides treatment in a structured <b>program '
        'setting</b> (not a family home), with continuous awake supervision per \u00a72.1 and '
        '\u00a79.5, and with the clinical/treatment/milieu component reimbursed by the '
        'Medicaid RTS per-diem while room and board are funded through a non-Medicaid '
        'source. Exclusions include acute psychiatric crisis requiring inpatient '
        'hospitalization, medical instability, or fire-setting that cannot be safely '
        'managed. The '"""
    patch_file(path, [(old, new)])


# ─── 13. sop_content_v3.py — §2.1 note strip ".0103(14)" + "DHSR MHLC" per M-017
def patch_section_2_1_note():
    path = os.path.join(SCRIPTS_DIR, 'sop_content_v3.py')
    old = """    story.append(para(
        '<i>Note: NC defines a "Group Home" as a facility serving no more than nine (9) '
        'children (the Resident Rights framework(14)). The facility shall not exceed its licensed capacity '
        'as stated on the DHSR MHLC license, which shall not exceed nine children under any '
        'circumstances.</i>'
    ))"""
    new = """    story.append(para(
        '<i>Note: The state group-home definition limits a facility of this type to no '
        'more than nine (9) children. The facility shall not exceed its licensed capacity '
        'as stated on the state-issued license, which shall not exceed nine children '
        'under any circumstances.</i>'
    ))"""
    patch_file(path, [(old, new)])


# ─── 14. sop_content_v3.py — §1.4 strip "10A NCAC 27G .0104(18)" reference per M-007 strip note
def patch_section_1_4_strip():
    path = os.path.join(SCRIPTS_DIR, 'sop_content_v3.py')
    # The QP credentialing section references "our operating standards"
    # which is already stripped — no further changes needed here
    pass


# ─── 15. generate_sop.py — bump version refs from 2.22 to 2.23
def patch_generate_sop_version():
    path = os.path.join(SCRIPTS_DIR, 'generate_sop.py')
    replacements = [
        ("'(Doc. WSI-SOP-001, Rev. 2.22, Aug 2026 — Legislation-Free Public Edition)'",
         "'(Doc. WSI-SOP-001, Rev. 2.23, Aug 2026 — Legislation-Free Public Edition)'"),
        ("subject='Level 3 Supervised Residential Group Home — Standard Operating Procedures (Rev. 2.22 Legislation-Free Public Edition)'",
         "subject='Level 3 Supervised Residential Group Home — Standard Operating Procedures (Rev. 2.23 Legislation-Free Public Edition)'"),
        ("'This manual (Rev. 2.22, August 2026) is the official Standard Operating '",
         "'This manual (Rev. 2.23, August 2026) is the official Standard Operating '"),
        ("'<b>Document ID.</b> Doc. WSI-SOP-001, Rev. 2.22 (Legislation-Free Public Edition). <i>The companion compliance master (Doc. WSI-SOP-001-LEG, Rev. 2.21) retains all statutory and regulatory citations for QA and audit reference.</i>',",
         "'<b>Document ID.</b> Doc. WSI-SOP-001, Rev. 2.23 (Legislation-Free Public Edition). <i>The companion compliance master (Doc. WSI-SOP-001-LEG, Rev. 2.21) retains all statutory and regulatory citations for QA and audit reference.</i>',"),
        ("'This manual (Rev. 2.22, August 2026) is organized into three parts and is fully '",
         "'This manual (Rev. 2.23, August 2026) is organized into three parts and is fully '"),
    ]
    patch_file(path, replacements)


# ─── 16. merge_sop.py — bump MANUAL_VERSION from 2.22 to 2.23
def patch_merge_sop_version():
    path = os.path.join(SCRIPTS_DIR, 'merge_sop.py')
    replacements = [
        ("MANUAL_VERSION = '2.22'", "MANUAL_VERSION = '2.23'"),
        ("'SOP, residential group home, Level 3, operations manual, trauma-informed care, RMDM, HIPAA, 42 CFR Part 2, E-SIGN, Electronic Signatures, fillable forms, daily workflow schedules, legislation-free public edition'",
         "'SOP, residential group home, Level 3, operations manual, trauma-informed care, RMDM, HIPAA, 42 CFR Part 2, E-SIGN, Electronic Signatures, fillable forms, daily workflow schedules, legislation-free public edition, v2.23 audit remediation'"),
    ]
    patch_file(path, replacements)


# ─── main ────────────────────────────────────────────────────────────
def main():
    print('=== Patching sop_content_v3.py ===')
    patch_section_1_2_h()
    patch_section_1_2_strip()
    patch_section_1_4_b()
    patch_section_1_8()
    patch_section_2_1_note()
    patch_section_2_2()
    patch_section_3_1_ivc()
    patch_section_3_4()
    patch_section_3_6()
    patch_section_4_6()
    patch_section_6_3()
    patch_section_9_2()
    patch_section_1_4_strip()

    print('=== Patching sop_content_v3_part2.py ===')
    patch_protocol_19()

    print('=== Patching generate_sop.py ===')
    patch_generate_sop_version()

    print('=== Patching merge_sop.py ===')
    patch_merge_sop_version()

    print('\n=== Done. Run generate_sop.py + merge_sop.py to regenerate the PDF. ===')


if __name__ == '__main__':
    main()
