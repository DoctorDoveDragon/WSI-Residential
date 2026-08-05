#!/usr/bin/env python3
"""
patch_sop_v224.py — SOP Manual v2.23 → v2.24 (CARF CYS 2026 Inaugural Accreditation
Conformance patch).

Applies the following surgical edits:

1. §1.2(a) Accreditation Prerequisite — rewrites to designate CARF Child & Youth
   Services (CYS) 2026 as the selected accrediting body and references the
   2026 CYS Inaugural Accreditation Guidelines as the operative standard for
   the Inaugural One-Year Accreditation survey.

2. New SOP §12 "CARF Accreditation Conformance Framework" — appended to end of
   build_part1() in sop_content_v3.py. Addresses the standards applicable at
   the time of an Inaugural Accreditation survey per Subsection A (Not Operational)
   or Subsection B (Operational) of the 2026 CYS Inaugural Accreditation Guidelines.
   Subsections:
     §12.1 ASPIRE to Excellence® Leadership & Strategic Planning
     §12.2 Input from Persons Served and Other Stakeholders
     §12.3 Legal Requirements
     §12.4 Financial Planning and Management
     §12.5 Risk Management & Enterprise Risk Register
     §12.6 Health & Safety Committee
     §12.7 Workforce Development & Management
     §12.8 Rights of Persons Served
     §12.9 Accessibility & Nondiscrimination
     §12.10 Performance Management & Measurement
     §12.11 General Program Standards — Program/Service Structure
     §12.12 Screening and Access to Services
     §12.13 Individualized Planning
     §12.14 Transition/Discharge Planning
     §12.15 Medication Use
     §12.16 Promoting Nonviolent Practices
     §12.17 Records of Persons Served & Quality Records Management
     §12.18 Service Delivery Using Information and Communication Technologies
     §12.19 Core Program Standards, Core Residential Program Standards, and
           Specialty Designation Standards
     §12.20 Quality Improvement Plan (QIP) — Inaugural Accreditation condition

3. New Form 12 "CARF QIP Tracker" — appended to sop_content_v3_part3.py before
   the Version History section. Tracks QIP actions in response to Inaugural
   Accreditation survey recommendations per 2026 CYS Guidelines Step 9.

4. Adds v2.24 row to Version History table.

5. Bumps version refs in generate_sop.py: SELF_REF → Rev. 2.24; subject → Rev. 2.24;
   About This Manual → Rev. 2.24; Document ID → Rev. 2.24; TOC intro → Rev. 2.24.

6. Bumps MANUAL_VERSION in merge_sop.py: '2.23' → '2.24'.
"""
import re
import pathlib

ROOT = pathlib.Path('/home/z/my-project/scripts')
V3 = ROOT / 'sop_content_v3.py'           # Part 1 (SOPs 1-11)
V3P2 = ROOT / 'sop_content_v3_part2.py'   # Part 2 (Protocols)
V3P3 = ROOT / 'sop_content_v3_part3.py'   # Part 3 (Forms + Version History)
GEN = ROOT / 'generate_sop.py'            # Body generator
MERGE = ROOT / 'merge_sop.py'             # Cover + body merger


# ─── Helper ────────────────────────────────────────────────────────────────
def patch(path: pathlib.Path, old: str, new: str, label: str):
    """Replace `old` with `new` in `path`. Fail loudly if not found."""
    src = path.read_text()
    if old not in src:
        raise SystemExit(f'PATCH FAIL [{label}]: old_str not found in {path.name}')
    if src.count(old) > 1:
        raise SystemExit(f'PATCH FAIL [{label}]: old_str matches {src.count(old)} times in {path.name} (must be unique)')
    path.write_text(src.replace(old, new, 1))
    print(f'  ✓ {label}')


# ─── 1. Rewrite §1.2(a) to designate CARF CYS 2026 ─────────────────────────
def patch_1_2_a_accreditation():
    old = """    story.append(Paragraph('<b>1.2(a) Accreditation Prerequisite.</b>', s_h2))
    story.append(para(
        'Pursuant to the Resident Rights framework and our operating standards, residential child-care facilities '
        'in North Carolina must be accredited by one of the four accrediting bodies recognized '
        'by NC DHHS prior to initial licensure and must maintain continuous accreditation as a '
        'condition of license renewal: <b>(i) the Council on Accreditation (COA)</b>, <b>(ii) The '
        'Joint Commission (TJC)</b>, <b>(iii) the Commission on Accreditation of Rehabilitation '
        'Facilities (CARF)</b>, or <b>(iv) the Council on Quality and Leadership (CQL)</b>. The '
        'Executive Director shall select the accrediting body, complete the self-study, host the '
        'on-site survey, and maintain the accreditation certificate in the facility compliance '
        'binder. The QP shall maintain an accreditation-maintenance calendar tracking annual '
        'reports, interim standards reviews, and the next full re-survey window, and shall report '
        'accreditation status to the Clinical Director at every quarterly compliance report (per '
        '§1.4(a)). Any adverse accreditation finding, conditional approval, or accreditation '
        'suspension/withdrawal shall be reported to DHSR MHLC within 5 business days and to '
        'Alliance Health within 10 business days.'
    ))"""
    new = """    story.append(Paragraph('<b>1.2(a) Accreditation Prerequisite &amp; Selected Accrediting Body.</b>', s_h2))
    story.append(para(
        'Pursuant to the Resident Rights framework and our operating standards, residential child-care facilities '
        'in North Carolina must be accredited by one of the four accrediting bodies recognized '
        'by NC DHHS prior to initial licensure and must maintain continuous accreditation as a '
        'condition of license renewal: <b>(i) the Council on Accreditation (COA)</b>, <b>(ii) The '
        'Joint Commission (TJC)</b>, <b>(iii) the Commission on Accreditation of Rehabilitation '
        'Facilities (CARF)</b>, or <b>(iv) the Council on Quality and Leadership (CQL)</b>. '
        '<b>Well Spring Intervention LLC has selected CARF as its accrediting body and will pursue '
        'Inaugural One-Year Accreditation under the 2026 Child and Youth Services (CYS) Standards '
        'Manual and the 2026 CYS Inaugural Accreditation Guidelines (effective July 1, 2026 – '
        'June 30, 2027).</b> Because the program will have delivered services for less than six '
        'months at the time of the survey, the organization is eligible for the Inaugural '
        'Accreditation pathway and will use Subsection A (Not Operational) of the 2026 CYS '
        'Inaugural Accreditation Guidelines if service delivery has not yet commenced, or '
        'Subsection B (Operational) if it has; the QP shall document the selected subsection in '
        'the compliance binder prior to survey application. The Executive Director shall complete '
        'the CARF self-study, host the on-site survey, and maintain the accreditation certificate '
        'in the facility compliance binder. The QP shall maintain an accreditation-maintenance '
        'calendar tracking (i) the Inaugural Accreditation survey application deadline (must be '
        'received by CARF at least three to four months prior to the target survey window and '
        'prior to six months of service delivery), (ii) the subsequent resurvey window '
        '(approximately 10–11 months after the Inaugural survey), (iii) the Quality Improvement '
        'Plan (QIP) submission deadline (within 90 days of accreditation notification per '
        '§12.20), (iv) interim standards reviews, and (v) the next full re-survey window, and '
        'shall report accreditation status to the Clinical Director at every quarterly compliance '
        'report (per §1.4(a)). Any adverse accreditation finding, conditional approval, or '
        'accreditation suspension/withdrawal shall be reported to the state licensing authority '
        'within 5 business days and to Alliance Health within 10 business days. <b>SOP §12 '
        'CARF Accreditation Conformance Framework</b> establishes the written policies, plans, '
        'and procedures required to demonstrate conformance to the applicable CARF CYS standards '
        'at the time of the Inaugural Accreditation survey.'
    ))"""
    patch(V3, old, new, '§1.2(a) — CARF CYS 2026 designated accrediting body')


# ─── 2. Append new SOP §12 to end of build_part1() ─────────────────────────
SOP12_BLOCK = '''
    # ── SOP 12 (NEW in v2.24) ─────────────────────────────────────
    # CARF CYS 2026 Inaugural Accreditation Conformance Framework
    # ──────────────────────────────────────────────────────────────
    story.append(section_heading(12, 'CARF Accreditation Conformance Framework'))
    story.append(ref_line(
        anchor='§12',
    ))
    story.append(para(
        '<b>12.0 Purpose &amp; Scope.</b> This section establishes the written policies, plans, '
        'procedures, and committees required to demonstrate conformance to the applicable '
        'standards of the <b>2026 CARF Child and Youth Services (CYS) Standards Manual</b> at the '
        'time of an <b>Inaugural One-Year Accreditation survey</b>, per the <b>2026 CYS Inaugural '
        'Accreditation Guidelines</b> (effective July 1, 2026 – June 30, 2027). The standards '
        'applied on an Inaugural Accreditation survey are a subset of the standards in the '
        'current 2026 CYS Standards Manual. Where the program will not have commenced service '
        'delivery at the time of the survey, Subsection A (Not Operational) applies; where '
        'service delivery will have commenced, Subsection B (Operational) applies, and the '
        'additional standards identified as inapplicable in Subsection B are deferred to the '
        'subsequent resurvey (approximately 10–11 months after the Inaugural survey). The QP '
        'shall document the selected subsection in the compliance binder prior to survey '
        'application. Each subsection below identifies the applicable CARF CYS standard area, '
        'the SOP location(s) where existing policies satisfy the standard, and any additional '
        'written policy, plan, or procedure required to demonstrate conformance. Where a '
        'standard requires a written plan, the plan must address all areas of the standard, be '
        'complete, and be in use or ready for implementation, as applicable, at the time of the '
        'survey. By CARF definition, a policy must be in writing; a plan must be in writing; a '
        'procedure must be in writing. Forms in use (or ready for use) by the program may be '
        'used to demonstrate conformance to some standards. Personnel should be able to discuss '
        'and show that they are familiar with and understand how to implement the CARF standards '
        'as applicable to their jobs. If service delivery has commenced, personnel should also '
        'be able to provide evidence of implementation. See Appendices A, B, and C of the 2026 '
        'CYS Standards Manual for documentation, timeline, and education/training requirements.'
    ))
    story.append(Paragraph('<b>12.1 ASPIRE to Excellence® — Leadership &amp; Strategic Planning.</b>', s_h2))
    story.append(para(
        'Conformance to CARF CYS Section 1.A (Leadership) and Section 1.C (Strategic Planning) '
        'is established through the written <b>Strategic Plan</b> maintained by the Executive '
        'Director and reviewed at least annually by the Governing Body. The Strategic Plan '
        'addresses: (a) the organization\\'s mission, vision, and values statements (§1.1); '
        '(b) a statement of the populations and services to be provided; (c) an environmental '
        'analysis considering input from persons served, personnel, funders, and other '
        'stakeholders; (d) strategic goals and measurable objectives for at least a three-year '
        'horizon; (e) action plans identifying responsible parties, resources, timelines, and '
        'evaluation methods; (f) input from persons served and other stakeholders (per §12.2) '
        'documented and incorporated; and (g) a written succession plan for the Executive '
        'Director and other key leadership positions. The Governing Body reviews and approves '
        'the Strategic Plan, monitors progress at each quarterly meeting (per §1.8), and '
        'authorizes revisions as needed. The QP retains the most recent Strategic Plan, '
        'meeting minutes documenting Governing Body review, and any interim revisions in the '
        'compliance binder. Leadership conformance under 1.A Standards 1–3, 5.a, 6.a–c, 7, 8 '
        'is demonstrated by the Governing Body charter and bylaws, position descriptions for '
        'the Executive Director and Clinical Director, the code of conduct/ethics policy, and '
        'the organizational chart. If the organization directly solicits charitable financial '
        'support, Standard 1.A.9 conformance is demonstrated by a written fundraising policy '
        'consistent with the organization\\'s charitable solicitation registration.'
    ))
    story.append(Paragraph('<b>12.2 Input from Persons Served and Other Stakeholders.</b>', s_h2))
    story.append(para(
        'Conformance to CARF CYS Section 1.D is established through the written <b>Stakeholder '
        'Input Plan</b> maintained by the QP. The plan describes at least four methods for '
        'gathering input from persons served, their families/LRP, personnel, referral sources, '
        'payers, and the community, including: (i) quarterly youth satisfaction surveys '
        '(developmentally appropriate, anonymous, available in English and the youth\\'s '
        'preferred language); (ii) semi-annual family/LRP feedback surveys; (iii) annual '
        'personnel engagement surveys; and (iv) community/stakeholder advisory convenings at '
        'least annually. Input is aggregated, analyzed for trends, and presented to the '
        'Governing Body at each quarterly meeting. The QP maintains a Stakeholder Input Log '
        'documenting the method, date, respondent count, key themes, and resulting action '
        'items. Person-served input directly informs the Person-Centered Plan (§4.1), '
        'program structure (§5), and the annual Strategic Plan revision (§12.1). The QP '
        'documents how input was used and communicates outcomes back to respondents through '
        'visible "You Said / We Did" postings in the facility common area and in resident '
        'community meetings. The organization does not retaliate against any person served, '
        'family member, or personnel for providing input, per §1.10 Non-Retaliation policy.'
    ))
    story.append(Paragraph('<b>12.3 Legal Requirements.</b>', s_h2))
    story.append(para(
        'Conformance to CARF CYS Section 1.E (Standards 1–3) is established through the '
        'written <b>Legal Compliance Plan</b> maintained by the Executive Director. The plan '
        'identifies all applicable federal, state, and local legal requirements governing the '
        'organization and the program, including: licensure as a Level III Residential '
        'Treatment Facility — Staff Secure (§1.2); Medicaid provider enrollment and the '
        'federal health-care-program fraud and abuse laws (§10); the federal health-privacy '
        'law and 42 CFR Part 2 (§11); state child-mandated-reporter law (§8); the federal '
        'disability-rights law (ADA) and Section 504 of the Rehabilitation Act (§12.9); the '
        'federal civil-rights law (Title VI); state employment law; and applicable zoning, '
        'fire, building, and life-safety codes (§9). The Executive Director designates a '
        'Compliance Officer (may be the QP) responsible for monitoring changes in legal '
        'requirements, coordinating the annual legal-compliance review, and reporting any '
        'identified violations or potential violations to the Governing Body within five '
        'business days of discovery. Written acknowledgment of legal compliance is provided '
        'annually by the Executive Director and Clinical Director. The plan includes a written '
        'response procedure for subpoenas, court orders, and government investigations, '
        'coordinated with the organization\\'s legal counsel. The Compliance Officer maintains '
        'a Legal Compliance Register listing each requirement, the controlling authority, the '
        'responsible position, the most recent review date, and the next review due date.'
    ))
    story.append(Paragraph('<b>12.4 Financial Planning and Management.</b>', s_h2))
    story.append(para(
        'Conformance to CARF CYS Section 1.F is established through the written <b>Financial '
        'Plan</b> maintained by the Executive Director and reviewed by the Governing Body at '
        'each quarterly meeting. The Financial Plan includes: (a) an annual operating budget '
        'covering all revenue sources (Medicaid, room-and-board, grants, charitable '
        'contributions) and all expense categories (personnel, facility, clinical, '
        'administrative); (b) a cash-flow projection; (c) a capital-replacement reserve '
        'sufficient to address expected major repairs and replacements over a rolling '
        'five-year horizon; (d) written internal controls addressing segregation of duties, '
        'authorization thresholds, bank reconciliation, and segregation of resident trust '
        'funds from operating funds; (e) an annual independent financial audit (or reviewed '
        'financial statements for organizations below the audit threshold) with management '
        'response to any findings; (f) a written billing and collections policy consistent '
        'with §10.9 and Medicaid requirements; and (g) a written records-retention schedule '
        'for financial documents. Written cost reports are submitted to Medicaid and to '
        'applicable funders per their respective deadlines. The QP coordinates with the '
        'Billing Coordinator (per Protocol 22) to ensure that all service documentation '
        'supports billed claims. The Financial Plan is reviewed at each quarterly Governing '
        'Body meeting; material variances (>10% line-item variance) are documented with '
        'corrective action.'
    ))
    story.append(Paragraph('<b>12.5 Risk Management &amp; Enterprise Risk Register.</b>', s_h2))
    story.append(para(
        'Conformance to CARF CYS Section 1.G (Standards 1–4) is established through the '
        'written <b>Enterprise Risk Management Plan</b> maintained by the Compliance Officer. '
        'The plan includes: (a) a written risk-management policy identifying the Compliance '
        'Officer as the risk-management lead and describing the risk identification, '
        'assessment, mitigation, and monitoring process; (b) an <b>Enterprise Risk Register</b> '
        'identifying at least the following risk categories — clinical (suicide risk, '
        'elopement, restraint-related injury, medication error), operational (staffing '
        'shortage, capacity under-utilization, IT system failure), financial (Medicaid audit '
        'finding, payer mix concentration, cash-flow shortfall), legal/compliance '
        '(privacy breach, licensing deficiency, employment claim), reputational (adverse '
        'media, community concern), and external (natural disaster, public-health emergency); '
        '(c) for each identified risk, a documented likelihood, impact, mitigation action, '
        'responsible position, and review date; (d) a written business-continuity plan '
        'coordinated with §9 Emergency Operations Plan and Protocol 19; (e) an annual '
        'risk-management review presented to the Governing Body; and (f) a written '
        'incident-reporting procedure consistent with §8 (IRIS) that ensures serious '
        'incidents are reviewed by the Compliance Officer within one business day and trended '
        'monthly. The Enterprise Risk Register is reviewed at each quarterly Governing Body '
        'meeting and following any serious incident.'
    ))
    story.append(Paragraph('<b>12.6 Health &amp; Safety Committee.</b>', s_h2))
    story.append(para(
        'Conformance to CARF CYS Section 1.H (Standards 1, 2, 4.a, 5, 6, 8, 9.b(2)-(3), 10, '
        '12, 14–16) is established through the facility\\'s existing §9 Facility, Safety, and '
        'Environmental Management SOP and the standing <b>Health &amp; Safety Committee</b> '
        'chartered by this section. The committee meets at least monthly and includes the QP '
        '(chair), the House Manager, a Direct Care Professional representative, the RN or '
        'designee, and the Compliance Officer. The committee reviews: (i) monthly '
        'environmental safety inspection results (Form 5); (ii) fire, tornado, and lockdown '
        'drills per shift per §9.2; (iii) incident reports (§8) trended by type, location, '
        'shift, and personnel; (iv) infection-control surveillance per §6.1 and Protocol 18; '
        '(v) medication-error trends per §6.3; (vi) work-related injury trends; (vii) '
        'equipment and physical-plant work orders; (viii) safety-plan revisions; and '
        '(ix) emergency-preparedness plan revisions. The committee maintains written minutes '
        'documenting attendance, topics reviewed, decisions made, and action items with '
        'responsible parties and due dates. The QP reports committee activities and trends to '
        'the Clinical Director at each quarterly compliance report (per §1.4(a)) and to the '
        'Governing Body at each quarterly meeting. Written health-and-safety policies '
        'addressing emergency response, infection control, hazard communication, bloodborne '
        'pathogens, workplace violence prevention, and hot-work/environmental safety are '
        'maintained in the facility policy library and reviewed at least annually.'
    ))
    story.append(Paragraph('<b>12.7 Workforce Development &amp; Management.</b>', s_h2))
    story.append(para(
        'Conformance to CARF CYS Section 1.I (Standards 1–13) is established through the '
        'written <b>Workforce Development Plan</b> maintained by the QP. The plan includes: '
        '(a) a written recruiting and hiring policy (§2.2), including background-check '
        'requirements per §2.3, reference verification, and credential verification per '
        '§1.4(b) and §2.2; (b) a written orientation curriculum completed by every new '
        'personnel member prior to working independently with persons served, covering at '
        'minimum the organization\\'s mission and values; person-centered and '
        'trauma-informed care; the Person-Centered Plan process (§4.1); behavioral support '
        'and restraint (§5); medication administration (§6.3); infection control (§6.1, '
        'Protocol 18); incident reporting (§8); privacy and confidentiality (§11); '
        'cultural and linguistic competency; mandated reporting; emergency procedures; '
        'documentation requirements (§10); resident rights; and the personnel code of '
        'conduct; (c) a written annual training plan covering refresher training and '
        'competency verification for all personnel, with documented completion dates and '
        'trainers; (d) written position descriptions for every role, consistent with §2; '
        '(e) a written performance-evaluation policy conducted at minimum annually for every '
        'personnel member, with documented competency assessment against position-specific '
        'criteria; (f) a written supervision policy consistent with §2.2(a) Individualized '
        'Supervision Plans; (g) a written personnel records policy consistent with §2.4; '
        '(h) a written volunteer and intern management policy per §1.8; (i) a written '
        'continuing-education support policy; (j) a written succession plan for key '
        'positions; and (k) a written workforce engagement and recognition plan. The QP '
        'maintains the master training calendar and individual personnel training records '
        'in the personnel file. The Workforce Development Plan is reviewed at least annually '
        'and updated to reflect changes in CARF standards, regulatory requirements, or '
        'program design.'
    ))
    story.append(Paragraph('<b>12.8 Rights of Persons Served.</b>', s_h2))
    story.append(para(
        'Conformance to CARF CYS Section 1.J (Standards 1–3) is established through the '
        'facility\\'s existing Resident Rights policies as documented in the Resident '
        'Handbook (companion document) and in §3, §5, §6, §8, §9, and §11 of this Manual. '
        'At minimum, written policies address: (a) the right to dignity, privacy, '
        'humane care, and freedom from discrimination; (b) the right to participate in '
        'service planning and to refuse services (with documented consequences of refusal); '
        '(c) the right to confidential communication and visitation; (d) the right to '
        'access one\\'s own record per §11.5; (e) the right to file a grievance without '
        'retaliation, with a written grievance procedure acknowledging receipt within two '
        'business days and resolving within 30 calendar days, with appeal to the Executive '
        'Director and external advocacy resources; (f) the right to be free from '
        'unnecessary restraint and seclusion per §5; (g) the right to informed consent for '
        'treatment and medication; (h) the right to religious freedom and reasonable '
        'accommodation; (i) the right to personal funds management per the financial '
        'controls in §12.4; and (j) the right to advance written notification of any '
        'discharge or transfer per §3.4(a). Personnel are trained on resident rights at '
        'orientation and annually thereafter. The QP audits grievance logs, restraint '
        'logs, and rights-related incident reports quarterly and reports trends to the '
        'Governing Body.'
    ))
    story.append(Paragraph('<b>12.9 Accessibility &amp; Nondiscrimination.</b>', s_h2))
    story.append(para(
        'Conformance to CARF CYS Section 1.K (Standards 1, 2.a–b(2)) is established through '
        'the written <b>Accessibility &amp; Nondiscrimination Plan</b> maintained by the '
        'Compliance Officer. The plan includes: (a) a written nondiscrimination policy '
        'consistent with applicable federal civil-rights law (Title VI, ADA, Section 504, '
        'Age Discrimination Act) and state law, prohibiting discrimination on the basis of '
        'race, color, national origin, religion, sex, gender identity or expression, '
        'sexual orientation, age, disability, veteran status, or any other protected '
        'classification; (b) a written language-access plan providing for qualified '
        'interpreter services at no cost to the youth and family, translation of vital '
        'documents into the languages commonly encountered in the service area, and '
        'primary-language preference documentation in the clinical record; (c) a written '
        'reasonable-accommodation policy for youth, family, personnel, and visitors with '
        'disabilities, addressing physical accessibility of the facility, communication '
        'accommodations, and programmatic accommodations; (d) a written accessibility '
        'review of the physical facility conducted at least annually, identifying barriers '
        'and corrective actions; and (e) a written grievance procedure for '
        'nondiscrimination complaints, distinct from but coordinated with the resident '
        'grievance procedure in §12.8. The plan is reviewed at least annually and updated '
        'to reflect changes in the served population, facility, or legal requirements.'
    ))
    story.append(Paragraph('<b>12.10 Performance Management &amp; Measurement.</b>', s_h2))
    story.append(para(
        'Conformance to CARF CYS Section 1.L (Standards 1, 2.a(2)/b–g, 3.a) is established '
        'through the written <b>Performance Measurement Plan</b> maintained by the QP. The '
        'plan identifies the organization\\'s performance indicators, organized into at '
        'least the following domains: (i) <b>access</b> — time from referral to admission '
        'decision, time from admission to first clinical contact, no-show rate; '
        '(ii) <b>person-centered planning</b> — PCP completed within required timeframe, '
        'PCP reviewed at required intervals, youth/family participation in PCP meetings; '
        '(iii) <b>clinical outcomes</b> — symptom measures (e.g., Columbia ADHD, PHQ-A, '
        'GAD-7), functional measures (e.g., CAFAS, GAF), restraint-use frequency and '
        'duration, elopement frequency, incident frequency and severity; '
        '(iv) <b>safety</b> — incident-free days, time-to-investigation, repeat-incident '
        'rate, medication-error rate; (v) <b>personnel</b> — turnover rate, time-to-fill, '
        'training completion rate, personnel engagement score; (vi) <b>financial</b> — '
        'days-cash-on-hand, Medicaid denial rate, cost per youth per day; and '
        '(vii) <b>person-served experience</b> — satisfaction survey scores, complaint '
        'volume and resolution time. The QP aggregates data monthly, analyzes trends '
        'quarterly, presents findings to the Governing Body at each quarterly meeting, '
        'and incorporates findings into the annual Strategic Plan revision (§12.1) and '
        'the Quality Improvement Plan (§12.20). Performance data is shared with personnel '
        'and with persons served (in developmentally appropriate, aggregated form) at '
        'least quarterly.'
    ))
    story.append(Paragraph('<b>12.11 General Program Standards — Program/Service Structure.</b>', s_h2))
    story.append(para(
        'Conformance to CARF CYS Section 2.A is established through the written <b>Program '
        'Description</b> maintained by the Clinical Director and approved by the Governing '
        'Body. The Program Description documents: (a) the populations served, including '
        'age range, diagnostic profile, and admission criteria per §3.1; (b) the service '
        'array, including residential care, clinical services (§4), behavioral support '
        '(§5), medication management (§6), educational support (§7), and family '
        'engagement; (c) the program philosophy and trauma-informed care model; '
        '(d) staffing patterns per §2; (e) physical-environment description per §9; '
        '(f) hours and days of operation; (g) referral and intake process per §3 and '
        'Protocol 1; (h) cultural and linguistic competency plan; (i) coordination with '
        'external systems of care (LME/MCO, school, DSS, juvenile justice, medical home); '
        '(j) the Person-Centered Plan process per §4.1; (k) discharge and transition '
        'planning per §3.4 and §3.6; (l) records of persons served per §1.6 and §11; and '
        '(m) quality records management per §12.17. The Program Description is reviewed '
        'annually and updated to reflect changes in program design, population, or '
        'regulatory requirements. A mock chart containing forms for use with or by '
        'persons served is maintained per the CARF CYS General Program Standards note.'
    ))
    story.append(Paragraph('<b>12.12 Screening and Access to Services.</b>', s_h2))
    story.append(para(
        'Conformance to CARF CYS Section 2.B is established through the written '
        '<b>Screening and Access Policy</b> maintained by the QP. The policy documents: '
        '(a) the written referral intake process per §3.1 and Protocol 1; (b) the '
        'screening criteria and decision authority; (c) the response timeframe for '
        'referral acknowledgement and admission decision; (d) the written waitlist '
        'management procedure if applicable; (e) the written emergency/crisis access '
        'procedure; (f) the written procedure for denying admission, including appeal '
        'rights and notification of referral source; (g) coordination with the LME/MCO '
        'and Tailored Plan access line; and (h) nondiscrimination in access per §12.9. '
        'The Screening and Access Policy is reviewed annually. The QP maintains access '
        'data (referrals received, admissions, denials with reasons, time-to-decision) '
        'and reports to the Governing Body quarterly as part of the performance '
        'measurement report (§12.10).'
    ))
    story.append(Paragraph('<b>12.13 Individualized Planning.</b>', s_h2))
    story.append(para(
        'Conformance to CARF CYS Section 2.C is established through the written '
        'Person-Centered Plan policy and procedure per §4.1 of this Manual. The QP '
        'ensures that every youth has an individualized, person-centered plan '
        'developed within required timeframes, reviewed at required intervals, and '
        'signed by the youth (as developmentally appropriate), the family/LRP, the '
        'QP, and other CFT members. The plan addresses strengths, needs, goals, '
        'objectives, services, responsible parties, and review dates. The plan '
        'reflects input from the youth and family/LRP per §12.2. Service delivery '
        'is consistent with the plan, and progress is documented in the service '
        'record per §10. The QP audits PCPs for completeness and timeliness as part '
        'of the quarterly Clinical Record Content Checklist audit (Form 8).'
    ))
    story.append(Paragraph('<b>12.14 Transition/Discharge Planning.</b>', s_h2))
    story.append(para(
        'Conformance to CARF CYS Section 2.D is established through the written '
        'transition and discharge planning policy per §3.4 of this Manual. The QP '
        'ensures that transition planning begins at admission, that the youth and '
        'family/LRP participate in transition planning, that the receiving provider '
        '(if any) is identified and engaged, that the discharge summary is completed '
        'and provided to the youth and family/LRP and to the receiving provider, '
        'and that post-discharge follow-up occurs per Protocol 11. Advance written '
        'notification of discharge is provided per §3.4(a). Emergency discharges '
        'are followed by the 5-business-day post-emergency service-planning meeting '
        'per §3.4(c). The 18th-birthday continuation policy per §3.6 applies.'
    ))
    story.append(Paragraph('<b>12.15 Medication Use.</b>', s_h2))
    story.append(para(
        'Conformance to CARF CYS Section 2.E is established through the written '
        'medication use policies in §6.3 of this Manual. If the program physically '
        'controls medications, the policies address receipt and verification per '
        '§6.3(b), storage per §6.3(c), disposal documentation per §6.3(d), '
        'administration, medication-error reporting, and the 6-month psychotropic '
        'drug regimen review per §6.3(a) and Form 11. If the program prescribes '
        'or administers medications, additional written policies address '
        'prescriber credentials, order verification, administration by qualified '
        'personnel, documentation in the medication administration record (MAR), '
        'medication reconciliation at admission and discharge, and medication '
        'education per §6.3(e). Medication policies are reviewed at least annually.'
    ))
    story.append(Paragraph('<b>12.16 Promoting Nonviolent Practices.</b>', s_h2))
    story.append(para(
        'Conformance to CARF CYS Section 2.F is established through the written '
        'behavioral support and restraint policies in §5 of this Manual. The '
        'organization is committed to promoting nonviolent practices and to the '
        'minimization of restraint and seclusion. Written policies address: '
        '(a) trauma-informed, person-centered behavioral support; (b) preventive '
        'strategies and de-escalation; (c) the least-restrictive intervention '
        'principle; (d) restraint and seclusion use criteria, authorization, '
        'time-limits, monitoring, and documentation; (e) post-incident debriefing '
        'with the youth and personnel per §5.6 and Form 3; (f) restraint-use '
        'review by the QP and Clinical Director with trend reporting to the '
        'Governing Body; and (g) personnel training and competency verification '
        'in de-escalation and restraint per §2.5. If the program intends to use '
        'seclusion or restraint, Standard 2.F.10 conformance is documented '
        'through the written policy and the Physical Restraint Debriefing '
        'Checklist (Form 3).'
    ))
    story.append(Paragraph('<b>12.17 Records of Persons Served &amp; Quality Records Management.</b>', s_h2))
    story.append(para(
        'Conformance to CARF CYS Section 2.G (Standards 1.a, 2–4, 6) and Section 2.H '
        '(Standard 4) is established through the written records-management policies '
        'in §1.6, §10, and §11 of this Manual, together with the written <b>Quality '
        'Records Review Procedure</b> maintained by the QP. The Quality Records Review '
        'Procedure describes the systematic review of clinical records for '
        'completeness, timeliness, and quality, conducted at minimum quarterly using '
        'the Comprehensive Clinical Record Content Checklist (Form 8). Findings are '
        'documented, trended, and reported to the Clinical Director and Governing '
        'Body. Deficiencies are addressed through personnel feedback, retraining, '
        'and policy revision as needed. Records are retained per §1.6 and the '
        'financial records-retention schedule in §12.4. Confidentiality of records '
        'is maintained per §11. The QP coordinates with the Compliance Officer to '
        'ensure that records-release accounting is maintained per §11.4 and Form 9.'
    ))
    story.append(Paragraph('<b>12.18 Service Delivery Using Information and Communication Technologies.</b>', s_h2))
    story.append(para(
        'Conformance to CARF CYS Section 2.I (Standards 1, 2) is established through '
        'the written <b>Telehealth &amp; Technology-Mediated Service Delivery Policy</b> '
        'maintained by the Clinical Director. The policy documents: (a) the services '
        'that may be delivered via information and communication technologies (e.g., '
        'family therapy sessions, psychiatric medication management follow-up, '
        'clinical supervision, care-coordination meetings); (b) the technologies '
        'used and the platform\\'s compliance with applicable privacy and security '
        'law (HIPAA, 42 CFR Part 2, HITECH) per §11; (c) informed consent for '
        'telehealth services, including documentation in the clinical record of the '
        'youth\\'s and family/LRP\\'s understanding of the benefits, risks, '
        'limitations, and alternatives; (d) personnel training and competency '
        'verification for telehealth service delivery; (e) procedures for '
        'technology failure, including fallback to in-person or telephone contact; '
        '(f) procedures for ensuring the youth\\'s privacy during telehealth '
        'sessions; (g) documentation requirements consistent with §10; and '
        '(h) coordination with the LME/MCO and payers regarding coverage of '
        'telehealth services. The policy is reviewed at least annually and updated '
        'to reflect changes in technology, legal requirements, or program design.'
    ))
    story.append(Paragraph('<b>12.19 Core Program Standards, Core Residential Program Standards, and Specialty Designation Standards.</b>', s_h2))
    story.append(para(
        'Per the 2026 CYS Inaugural Accreditation Guidelines, all standards in '
        'Sections 3, 4, and 5 of the 2026 CYS Standards Manual are applicable to '
        'the extent possible at the time of the Inaugural Accreditation survey. '
        'The QP shall complete a written crosswalk between the 2026 CYS Standards '
        'Manual Sections 3–5 standards and this Manual\\'s SOPs, Protocols, and '
        'Forms, and shall retain the crosswalk in the compliance binder. Where a '
        'standard is not addressed by existing policy, the QP shall develop a '
        'written plan for addressing the standard prior to the subsequent '
        'resurvey. The crosswalk is reviewed at each quarterly QP compliance '
        'report (per §1.4(a)) and updated as standards are addressed or as the '
        'CYS Standards Manual is revised.'
    ))
    story.append(Paragraph('<b>12.20 Quality Improvement Plan (QIP) — Inaugural Accreditation Condition.</b>', s_h2))
    story.append(para(
        'Per Step 9 of the 2026 CYS Inaugural Accreditation Guidelines, within '
        '<b>90 days</b> after notification of accreditation, the organization '
        'shall submit to CARF a written <b>Quality Improvement Plan (QIP)</b> '
        'outlining the actions that have been or will be taken in response to '
        'the recommendations identified in the Inaugural Accreditation survey '
        'report. The QP is responsible for developing the QIP in coordination '
        'with the Executive Director and Clinical Director, and for monitoring '
        'implementation. The QIP shall: (a) restate each recommendation from '
        'the survey report; (b) describe the corrective action taken or planned; '
        '(c) identify the responsible position; (d) specify a target completion '
        'date; (e) identify the evidence of implementation that will be '
        'available at the subsequent resurvey; and (f) be approved by the '
        'Executive Director prior to submission. The QP shall maintain the QIP '
        'in the compliance binder, track implementation status at each '
        'quarterly compliance report (per §1.4(a)), and update CARF through '
        'Customer Connect as actions are completed. <b>Form 12 (CARF QIP '
        'Tracker)</b> in Part 3 is the standardized form for tracking QIP '
        'actions. The organization shall prepare for the subsequent resurvey '
        'by addressing all applicable standards in the current 2026 CYS '
        'Standards Manual and by completing all QIP actions. The subsequent '
        'resurvey will occur approximately 10–11 months after the Inaugural '
        'Accreditation survey; there is no application fee for the subsequent '
        'survey, and scheduling begins upon payment of at least half of the '
        'subsequent survey fee. Failure to complete the QIP within 90 days '
        'or failure to complete the subsequent survey within 12 months of the '
        'Inaugural survey will result in expiration of the Inaugural One-Year '
        'Accreditation.'
    ))
    story.append(callout(
        'Cross-reference: This §12 framework operates in conjunction with §1.2(a) (CARF '
        'designation), §1.4(a) (QP compliance reporting), §1.8 (Governing Body), §2 '
        '(Workforce), §3 (Admissions/Discharge), §4 (Clinical Services), §5 (Behavioral '
        'Management), §6 (Health/Medication), §7 (Education), §8 (Incident Reporting), '
        '§9 (Facility/Safety), §10 (Medicaid Documentation), §11 (Privacy/Records), and '
        'the Form 12 (CARF QIP Tracker) in Part 3. The QP shall present this §12 framework '
        'to CARF surveyors as the primary evidence of organizational readiness for the '
        'Inaugural Accreditation survey.'
    ))'''


def patch_append_sop_12():
    """Append SOP 12 to end of build_part1() just before `return story`."""
    old = """    story.append(Paragraph('<b>11.7 Storage and Maintenance.</b>', s_h2))
    story.append(para(
        'Storage and maintenance are consistent with privacy/security principles. '
        'Electronic records self-warranty per NC State Archives guidelines. "Managing '
        'Public Records Produced by Information Technology Systems" guidelines apply. '
        'The QP conducts quarterly audits of storage security and access logs.'
    ))

    return story"""
    new = """    story.append(Paragraph('<b>11.7 Storage and Maintenance.</b>', s_h2))
    story.append(para(
        'Storage and maintenance are consistent with privacy/security principles. '
        'Electronic records self-warranty per NC State Archives guidelines. "Managing '
        'Public Records Produced by Information Technology Systems" guidelines apply. '
        'The QP conducts quarterly audits of storage security and access logs.'
    ))
""" + SOP12_BLOCK + """

    return story"""
    patch(V3, old, new, 'Append SOP §12 CARF Conformance Framework to build_part1()')


# ─── 3. Add Form 12 (CARF QIP Tracker) to part3 ────────────────────────────
def patch_add_form_12():
    # Find the Version History anchor
    old = """    story.append(Spacer(1, 8))
    story.append(Paragraph(
        '<b>Initial Review (within 30 days of admission):</b> ☐ Completed &nbsp; ☐ Most-recent prior review obtained '
        '(date: __________) &nbsp; <b>Reviewer Signature:</b> ___________________________',
        s_form_meta
    ))
    story.append(Spacer(1, 12))

    # ── Version History ────────────────────────────────────────────"""
    new = """    story.append(Spacer(1, 8))
    story.append(Paragraph(
        '<b>Initial Review (within 30 days of admission):</b> ☐ Completed &nbsp; ☐ Most-recent prior review obtained '
        '(date: __________) &nbsp; <b>Reviewer Signature:</b> ___________________________',
        s_form_meta
    ))
    story.append(Spacer(1, 12))

    # ── Form 12: CARF QIP Tracker (NEW in v2.24) ──
    story.extend(_form_banner_and_heading(
        12, 'CARF QIP Tracker',
        'Part 3 &middot; Form 12: CARF QIP Tracker',
        external_ref='2026 CYS Inaugural Accreditation Guidelines Step 9 — Quality Improvement Plan (QIP) due to CARF within 90 days of accreditation notification (§12.20)',
        instructions='Document each recommendation from the Inaugural Accreditation survey report and the corrective action '
                     'taken or planned, per §12.20. One row per recommendation. The QP submits the QIP to CARF within 90 days '
                     'of accreditation notification and updates CARF through Customer Connect as actions are completed. '
                     'Maintain in the compliance binder for the duration of the accreditation cycle. Click any cell to type.',
    ))
    story.append(fillable_meta_row([
        ('Organization:', 220, 'Well Spring Intervention LLC'),
        ('Accreditation Cycle:', 200, '2026 CYS Inaugural One-Year'),
    ]))
    story.append(Spacer(1, 4))
    story.append(fillable_meta_row([
        ('Survey Exit Date:', 160, 'Date of survey exit conference'),
        ('Accreditation Notification Date:', 220, 'Date CARF notified accreditation decision'),
        ('QIP Due Date (90 days):', 160, '90 days after notification',
    ]))
    story.append(Spacer(1, 4))
    story.append(fillable_meta_row([
        ('QP Name:', 200, 'QP name'),
        ('Executive Director:', 220, 'Executive Director name'),
    ]))
    story.append(Spacer(1, 4))
    story.append(Paragraph('<b>QIP Action Tracker</b>', s_form_section))

    f12_header = [
        'Rec #', 'Survey Report Recommendation (verbatim)', 'Corrective Action Taken or Planned',
        'Responsible Position', 'Target Completion Date', 'Evidence of Implementation at Resurvey',
        'Status', 'Date Closed / Reported to CARF',
    ]
    f12_th = ParagraphStyle('f12th', fontName=BODY_BOLD, fontSize=8, leading=10, textColor=colors.white, alignment=TA_LEFT)
    f12_data = [[Paragraph(f'<b>{h}</b>', f12_th) for h in f12_header]]
    for _ in range(10):
        f12_data.append(_fillable_data_cells(8, default_width=55, height=32, font_size=8))
    f12_widths = [
        0.05*AVAIL_W, 0.18*AVAIL_W, 0.18*AVAIL_W, 0.10*AVAIL_W,
        0.10*AVAIL_W, 0.17*AVAIL_W, 0.08*AVAIL_W, 0.14*AVAIL_W,
    ]
    t12 = Table(f12_data, colWidths=f12_widths, hAlign='CENTER', repeatRows=1)
    sc12 = [
        ('BACKGROUND', (0, 0), (-1, 0), HEADER_FILL),
        ('GRID',       (0, 0), (-1, -1), 0.4, BORDER),
        ('VALIGN',     (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING',  (0, 0), (-1, -1), 3),
        ('RIGHTPADDING', (0, 0), (-1, -1), 3),
        ('TOPPADDING',   (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING',(0, 0), (-1, -1), 8),
    ]
    for i in range(1, len(f12_data)):
        bg = TABLE_ROW_ODD if i % 2 == 1 else TABLE_ROW_EVEN
        sc12.append(('BACKGROUND', (0, i), (-1, i), bg))
    t12.setStyle(TableStyle(sc12))
    story.append(t12)
    story.append(Spacer(1, 8))
    story.append(Paragraph(
        '<b>QIP Approval:</b> Submitted to CARF via Customer Connect on: __________ &nbsp; '
        '<b>Executive Director Signature:</b> ___________________________ &nbsp; '
        '<b>Date:</b> __________ &nbsp; <b>QP Signature:</b> ___________________________',
        s_form_meta
    ))
    story.append(Spacer(1, 4))
    story.append(Paragraph(
        '<b>Subsequent Resurvey Window (10–11 months after Inaugural survey):</b> __________ &nbsp; '
        '<b>Subsequent Survey Application Submitted?</b> ☐ Yes &nbsp; ☐ No &nbsp; '
        '<b>Subsequent Survey Fee Paid (≥50%)?</b> ☐ Yes &nbsp; ☐ No',
        s_form_meta
    ))
    story.append(Spacer(1, 12))

    # ── Version History ────────────────────────────────────────────"""
    patch(V3P3, old, new, 'Append Form 12 (CARF QIP Tracker) before Version History')


# ─── 4. Add v2.24 row to Version History ───────────────────────────────────
def patch_add_v224_history():
    old = """        ['2.23', 'Aug 2026',
         '<b>v2.22 COMPLIANCE AUDIT REMEDIATION.</b> Implements all 22 corrective actions from the SOP Manual v2.22 Compliance Audit against 10A NCAC 27G .1700 + cross-referenced core rules (.0104, .0201–.0210). <b>HIGH severity (3):</b> F-001 — adds new §4.6 Licensed Professional Face-to-Face Clinical Consultation per .1705(a)-(b) (minimum 4 hrs/wk face-to-face consultation by a Licensed Professional) and new Form 10 (Licensed Professional Consultation Log); F-002 — adds new §6.3(a) Psychotropic Medication Drug Regimen Review per .0209(f) (every 6 months by pharmacist or physician) and new Form 11 (Psychotropic Medication Drug Regimen Review Log); F-003 — <b>RESOLVES the open §1.2(h)(b) compliance flag</b> in favor of CCP 8D-2; all legacy "CCP 8C" references in §1.2, §2, §3, §4, §5, §6, and §10 reference lines globally updated to "CCP 8D-2"; §1.2(h)(b) rewritten from OPEN to RESOLVED; §1.2(h)(c) updated to reflect both (a) and (b) now resolved. <b>MEDIUM severity (18):</b> M-007 — adds QP 2-year direct client care experience statement to §1.4(b); F-006/F-007/M-011/M-028/M-029 — adds new §2.2(a) Individualized Supervision Plans for APs and DCPs and expands AP definition to enumerate all four .0104(1) pathways; M-033 — adds age-18, literacy, and criminal-conviction self-disclosure requirements to §2.2; F-009 — adds new §3.6 18th-Birthday Continuation Policy per .1706(e) (up to 6 months or end of school year, whichever is longer); M-025 — adds §3.4(a) 7-day advance written notification for non-emergency discharge; M-026 — adds §3.4(b) pre-discharge CFT meeting; F-008 — adds §3.4(c) 5-business-day post-emergency service-planning meeting per .1708(e); M-031 — adds governing-body policies for client fee assessment, lab test authorization/follow-up, and volunteer services to §1.8; M-032 — adds governing-body minutes permanently maintained statement to §1.8; M-038 — updates §9.2 and Protocol 19 to require quarterly fire AND tornado drills for EACH shift (day, evening, overnight); F-012 — adds §6.3(b) Medication Receipt &amp; Verification (tamper-resistant packaging + label content); M-043 — adds §6.3(c) Medication Storage (locked cabinet 59–86°F, dedicated med fridge 36–46°F, daily temp log on Form 5); F-013 — adds §6.3(d) Medication Disposal Documentation per .0209(d)(1)-(4) (controlled-substance disposal witnessed by 2 staff); F-014 — adds §6.3(e) Medication Education per .0209(g)(1)-(3) (at admission, at each med change, and quarterly thereafter, with developmentally appropriate content and family/guardian education offered). <b>LOW severity (1):</b> F-011 — adds new §1.2(h)(d) Cross-Reference Clarification Note documenting the .1702(a) → .0104(18) vs .0104(21) discrepancy (rule appears to contain a typographical error; Manual applies the .0104(21) "Qualified professional" definition as operative). <b>LEGISLATION STRIPPING (additional):</b> §1.2 license paragraph de-abbreviates "NC DHSR / MHLC / DSS" to "the applicable state mental health authority — not under foster-care licensing"; §3.1 admission criteria replaces "Involuntary Commitment (IVC)" with "acute psychiatric crisis requiring inpatient hospitalization"; §2.1 note replaces ".0103(14)" citation and "DHSR MHLC" with plain-language "state group-home definition" and "state-issued license"; §6.3 replaces "NC Medication Administration training" with "state-approved medication administration training"; §6.3 replaces "IRIS" abbreviation with "state incident-reporting system (IRIS)" on first use. Companion audit report and XLSX crosswalk matrix delivered at /download/WSI_SOP_v2.22_Compliance_Audit_Report.pdf and /download/WSI_SOP_v2.22_Compliance_Audit_Crosswalk.xlsx.',
         'Executive Director / QP'],
    ]"""
    new = """        ['2.23', 'Aug 2026',
         '<b>v2.22 COMPLIANCE AUDIT REMEDIATION.</b> Implements all 22 corrective actions from the SOP Manual v2.22 Compliance Audit against 10A NCAC 27G .1700 + cross-referenced core rules (.0104, .0201–.0210). <b>HIGH severity (3):</b> F-001 — adds new §4.6 Licensed Professional Face-to-Face Clinical Consultation per .1705(a)-(b) (minimum 4 hrs/wk face-to-face consultation by a Licensed Professional) and new Form 10 (Licensed Professional Consultation Log); F-002 — adds new §6.3(a) Psychotropic Medication Drug Regimen Review per .0209(f) (every 6 months by pharmacist or physician) and new Form 11 (Psychotropic Medication Drug Regimen Review Log); F-003 — <b>RESOLVES the open §1.2(h)(b) compliance flag</b> in favor of CCP 8D-2; all legacy "CCP 8C" references in §1.2, §2, §3, §4, §5, §6, and §10 reference lines globally updated to "CCP 8D-2"; §1.2(h)(b) rewritten from OPEN to RESOLVED; §1.2(h)(c) updated to reflect both (a) and (b) now resolved. <b>MEDIUM severity (18):</b> M-007 — adds QP 2-year direct client care experience statement to §1.4(b); F-006/F-007/M-011/M-028/M-029 — adds new §2.2(a) Individualized Supervision Plans for APs and DCPs and expands AP definition to enumerate all four .0104(1) pathways; M-033 — adds age-18, literacy, and criminal-conviction self-disclosure requirements to §2.2; F-009 — adds new §3.6 18th-Birthday Continuation Policy per .1706(e) (up to 6 months or end of school year, whichever is longer); M-025 — adds §3.4(a) 7-day advance written notification for non-emergency discharge; M-026 — adds §3.4(b) pre-discharge CFT meeting; F-008 — adds §3.4(c) 5-business-day post-emergency service-planning meeting per .1708(e); M-031 — adds governing-body policies for client fee assessment, lab test authorization/follow-up, and volunteer services to §1.8; M-032 — adds governing-body minutes permanently maintained statement to §1.8; M-038 — updates §9.2 and Protocol 19 to require quarterly fire AND tornado drills for EACH shift (day, evening, overnight); F-012 — adds §6.3(b) Medication Receipt &amp; Verification (tamper-resistant packaging + label content); M-043 — adds §6.3(c) Medication Storage (locked cabinet 59–86°F, dedicated med fridge 36–46°F, daily temp log on Form 5); F-013 — adds §6.3(d) Medication Disposal Documentation per .0209(d)(1)-(4) (controlled-substance disposal witnessed by 2 staff); F-014 — adds §6.3(e) Medication Education per .0209(g)(1)-(3) (at admission, at each med change, and quarterly thereafter, with developmentally appropriate content and family/guardian education offered). <b>LOW severity (1):</b> F-011 — adds new §1.2(h)(d) Cross-Reference Clarification Note documenting the .1702(a) → .0104(18) vs .0104(21) discrepancy (rule appears to contain a typographical error; Manual applies the .0104(21) "Qualified professional" definition as operative). <b>LEGISLATION STRIPPING (additional):</b> §1.2 license paragraph de-abbreviates "NC DHSR / MHLC / DSS" to "the applicable state mental health authority — not under foster-care licensing"; §3.1 admission criteria replaces "Involuntary Commitment (IVC)" with "acute psychiatric crisis requiring inpatient hospitalization"; §2.1 note replaces ".0103(14)" citation and "DHSR MHLC" with plain-language "state group-home definition" and "state-issued license"; §6.3 replaces "NC Medication Administration training" with "state-approved medication administration training"; §6.3 replaces "IRIS" abbreviation with "state incident-reporting system (IRIS)" on first use. Companion audit report and XLSX crosswalk matrix delivered at /download/WSI_SOP_v2.22_Compliance_Audit_Report.pdf and /download/WSI_SOP_v2.22_Compliance_Audit_Crosswalk.xlsx.',
         'Executive Director / QP'],
        ['2.24', 'Aug 2026',
         '<b>CARF CYS 2026 INAUGURAL ACCREDITATION CONFORMANCE.</b> Implements conformance to the applicable standards in the <b>2026 CARF Child and Youth Services (CYS) Standards Manual</b> at the time of an <b>Inaugural One-Year Accreditation survey</b>, per the <b>2026 CYS Inaugural Accreditation Guidelines</b> (effective July 1, 2026 – June 30, 2027). §1.2(a) rewritten to designate <b>CARF as the selected accrediting body</b> and to document Inaugural Accreditation pathway eligibility (program will have delivered services for less than six months at the time of the survey); the QP shall document the selected subsection (Subsection A Not Operational or Subsection B Operational) in the compliance binder prior to survey application. <b>NEW SOP §12 CARF Accreditation Conformance Framework</b> added with twenty subsections addressing every applicable standard area in the 2026 CYS Inaugural Accreditation Guidelines: §12.1 ASPIRE to Excellence® Leadership &amp; Strategic Planning (written Strategic Plan, Governing Body charter, succession plan); §12.2 Input from Persons Served and Other Stakeholders (written Stakeholder Input Plan, quarterly surveys, "You Said / We Did" feedback loop, non-retaliation); §12.3 Legal Requirements (written Legal Compliance Plan, Compliance Officer designation, Legal Compliance Register); §12.4 Financial Planning and Management (written Financial Plan, annual operating budget, capital-replacement reserve, internal controls, independent audit); §12.5 Risk Management &amp; Enterprise Risk Register (written Enterprise Risk Management Plan, six risk categories, business-continuity plan); §12.6 Health &amp; Safety Committee (standing committee charter, monthly meetings, written minutes, trend reporting); §12.7 Workforce Development &amp; Management (written Workforce Development Plan, orientation curriculum, annual training plan, position descriptions, performance evaluation, succession plan); §12.8 Rights of Persons Served (ten written resident-rights policies, grievance procedure, quarterly QP audit); §12.9 Accessibility &amp; Nondiscrimination (written Accessibility &amp; Nondiscrimination Plan, language-access plan, reasonable-accommodation policy, annual accessibility review); §12.10 Performance Management &amp; Measurement (written Performance Measurement Plan, seven performance domains, monthly aggregation, quarterly Governing Body reporting); §12.11 Program/Service Structure (written Program Description approved by Governing Body, mock chart maintained); §12.12 Screening and Access to Services (written Screening and Access Policy, access data tracking); §12.13 Individualized Planning (cross-reference to §4.1 PCP policy); §12.14 Transition/Discharge Planning (cross-reference to §3.4 and §3.6); §12.15 Medication Use (cross-reference to §6.3 expanded medication policies); §12.16 Promoting Nonviolent Practices (cross-reference to §5 behavioral support and restraint policies); §12.17 Records of Persons Served &amp; Quality Records Management (written Quality Records Review Procedure, quarterly Form 8 audits, trend reporting); §12.18 Service Delivery Using Information and Communication Technologies (written Telehealth &amp; Technology-Mediated Service Delivery Policy, platform privacy/security compliance, informed consent, fallback procedures); §12.19 Core Program Standards, Core Residential Program Standards, and Specialty Designation Standards (written crosswalk to 2026 CYS Standards Manual Sections 3–5, retained in compliance binder, reviewed at each quarterly QP compliance report); §12.20 Quality Improvement Plan (QIP) — Inaugural Accreditation Condition (QIP due to CARF within 90 days of accreditation notification per 2026 CYS Guidelines Step 9, monitored at each quarterly compliance report, subsequent resurvey window 10–11 months after Inaugural survey). <b>NEW Form 12 (CARF QIP Tracker)</b> added to Part 3 — 8-column fillable tracker (Recommendation, Corrective Action, Responsible Position, Target Date, Evidence of Implementation, Status, Date Closed/Reported to CARF) plus QIP approval signature block and subsequent resurvey tracking fields. Companion CARF CYS 2026 Inaugural Accreditation Guidelines PDF retained at /upload/2026 CYS Inaugural Accreditation Guidelines 1.pdf. All existing SOPs §1–§11, all 22 Protocols, and Forms 1–11 retained unchanged from v2.23 — only §1.2(a) is rewritten and §12 + Form 12 are appended.',
         'Executive Director / QP'],
    ]"""
    patch(V3P3, old, new, 'Add v2.24 row to Version History')


# ─── 5. Bump version refs in generate_sop.py ───────────────────────────────
def patch_generate_sop_versions():
    # SELF_REF
    patch(GEN,
        "    'Well Spring Intervention LLC SOP &amp; Operational Manual '\n    '(Doc. WSI-SOP-001, Rev. 2.23, Aug 2026 — Legislation-Free Public Edition)'",
        "    'Well Spring Intervention LLC SOP &amp; Operational Manual '\n    '(Doc. WSI-SOP-001, Rev. 2.24, Aug 2026 — Legislation-Free Public Edition)'",
        'generate_sop.py SELF_REF → Rev. 2.24')

    # subject metadata
    patch(GEN,
        "        subject='Level 3 Supervised Residential Group Home — Standard Operating Procedures (Rev. 2.23 Legislation-Free Public Edition)',",
        "        subject='Level 3 Supervised Residential Group Home — Standard Operating Procedures (Rev. 2.24 Legislation-Free Public Edition)',",
        'generate_sop.py subject → Rev. 2.24')

    # About This Manual paragraph
    patch(GEN,
        "        'This manual (Rev. 2.23, August 2026) is the official Standard Operating '",
        "        'This manual (Rev. 2.24, August 2026) is the official Standard Operating '",
        'generate_sop.py About This Manual → Rev. 2.24')

    # Document ID
    patch(GEN,
        "    story.append(Paragraph('<b>Document ID.</b> Doc. WSI-SOP-001, Rev. 2.23 (Legislation-Free Public Edition). <i>The companion compliance master (Doc. WSI-SOP-001-LEG, Rev. 2.21) retains all statutory and regulatory citations for QA and audit reference.</i>', s_body))",
        "    story.append(Paragraph('<b>Document ID.</b> Doc. WSI-SOP-001, Rev. 2.24 (Legislation-Free Public Edition). <i>The companion compliance master (Doc. WSI-SOP-001-LEG, Rev. 2.21) retains all statutory and regulatory citations for QA and audit reference.</i>', s_body))",
        'generate_sop.py Document ID → Rev. 2.24')

    # TOC intro
    patch(GEN,
        "        'This manual (Rev. 2.23, August 2026) is organized into three parts and is fully '",
        "        'This manual (Rev. 2.24, August 2026) is organized into three parts and is fully '",
        'generate_sop.py TOC intro → Rev. 2.24')

    # TOC intro "eleven sections" → "twelve sections"
    patch(GEN,
        "        'compliant with the NCDHHS Records Management and Documentation Manual (RMDM, '\n        'Effective July 8, 2025). Part 1 establishes foundational policies and compliance '\n        'obligations across eleven sections, including dedicated chapters on '",
        "        'compliant with the NCDHHS Records Management and Documentation Manual (RMDM, '\n        'Effective July 8, 2025). Part 1 establishes foundational policies and compliance '\n        'obligations across twelve sections, including dedicated chapters on '",
        'generate_sop.py TOC intro: eleven → twelve sections')

    # TOC intro forms count: "nine customized forms" → "twelve customized forms"
    # + add CARF QIP Tracker (new in v2.24)
    patch(GEN,
        "        'management/disclosure accounting. Part 3 provides nine customized forms '\n        'and logs, including the Full Service Note Template, Comprehensive Clinical '\n        'Record Content Checklist, Accounting of Disclosures Log, the Licensed '\n        'Professional Consultation Log (new in v2.23), and the Psychotropic Medication '\n        'Drug Regimen Review Log (new in v2.23). A complete revision history appears '",
        "        'management/disclosure accounting. Part 3 provides twelve customized forms '\n        'and logs, including the Full Service Note Template, Comprehensive Clinical '\n        'Record Content Checklist, Accounting of Disclosures Log, the Licensed '\n        'Professional Consultation Log (new in v2.23), the Psychotropic Medication '\n        'Drug Regimen Review Log (new in v2.23), and the CARF QIP Tracker (new in '\n        'v2.24). A complete revision history appears '",
        'generate_sop.py TOC intro: nine → twelve forms + add Form 12 note')

    # Comment header "11 SOP sections + 21 protocols + 9 forms + version history"
    # → "12 SOP sections + 22 protocols + 12 forms + version history"
    patch(GEN,
        "# 11 SOP sections + 21 protocols + 9 forms + version history",
        "# 12 SOP sections + 22 protocols + 12 forms + version history",
        'generate_sop.py comment header: 11/21/9 → 12/22/12')


# ─── 6. Bump MANUAL_VERSION in merge_sop.py ────────────────────────────────
def patch_merge_sop_version():
    patch(MERGE,
        "MANUAL_VERSION = '2.23'",
        "MANUAL_VERSION = '2.24'",
        'merge_sop.py MANUAL_VERSION → 2.24')

    # Also update keywords if it includes v2.23
    patch(MERGE,
        "'v2.23 audit remediation'",
        "'v2.24 CARF CYS accreditation conformance'",
        'merge_sop.py keywords: v2.23 → v2.24')


# ─── Main ──────────────────────────────────────────────────────────────────
if __name__ == '__main__':
    print('Patching SOP v2.23 → v2.24 (CARF CYS 2026 Inaugural Accreditation Conformance)...')
    print()
    print('[1/6] Rewriting §1.2(a) to designate CARF CYS 2026...')
    patch_1_2_a_accreditation()
    print()
    print('[2/6] Appending SOP §12 CARF Conformance Framework to build_part1()...')
    patch_append_sop_12()
    print()
    print('[3/6] Adding Form 12 (CARF QIP Tracker) to Part 3...')
    patch_add_form_12()
    print()
    print('[4/6] Adding v2.24 row to Version History...')
    patch_add_v224_history()
    print()
    print('[5/6] Bumping version refs in generate_sop.py...')
    patch_generate_sop_versions()
    print()
    print('[6/6] Bumping MANUAL_VERSION in merge_sop.py...')
    patch_merge_sop_version()
    print()
    print('All patches applied. Ready to regenerate SOP body PDF.')
