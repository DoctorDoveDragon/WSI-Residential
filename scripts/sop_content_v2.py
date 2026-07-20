# ────────────────────────────────────────────────────────────────────
# Content builders — Version 2.0 (RMDM-Compliant, July 2026)
# 11 SOP sections + 21 protocols + 9 forms
# ────────────────────────────────────────────────────────────────────
# Import all helpers/styles/palette from the main generate_sop module
from generate_sop import (
    part_divider, section_heading, ref_line, para, bullets, callout,
    std_table, form_table, signature_line,
    Paragraph, Spacer, PageBreak, Table, TableStyle, HRFlowable,
    ParagraphStyle, colors, TA_LEFT, TA_CENTER,
    BODY_FONT, BODY_BOLD, BODY_ITAL,
    s_part, s_part_kicker, s_part_intro, s_h1, s_h2, s_body, s_body_just,
    s_ref, s_bullet, s_callout, s_callout_label,
    s_form_title, s_form_meta, s_form_instr, s_form_section,
    s_th, s_th_left, s_td, s_td_c, s_td_b, s_td_sm,
    s_toc_title, s_toc_kicker, s_toc_intro, s_toc_l0, s_toc_l1,
    HEADER_FILL, BORDER, ACCENT, ACCENT_2, TEXT_PRIMARY, TEXT_MUTED,
    CARD_BG, TABLE_ROW_ODD, TABLE_ROW_EVEN,
    AVAIL_W,
)


def build_part1():
    story = []
    story.extend(part_divider(
        'PART 1',
        'Standard Operating Procedures',
        'These eleven SOP sections define the foundational policies, governance, staffing, '
        'clinical, privacy, and compliance obligations that govern every aspect of program '
        'operation. Version 2.0 expands coverage to full RMDM (Effective July 8, 2025) '
        'compliance, including record retention, CDW data reporting, comprehensive clinical '
        'record content, CCA requirements, service orders/authorizations, and privacy/'
        'confidentiality under HIPAA and 42 CFR Part 2. Every staff member is responsible '
        'for knowing and adhering to these policies.',
    ))

    # ── SOP 1 ──────────────────────────────────────────────────────
    story.append(section_heading(1, 'Agency Overview & Governance'))
    story.append(ref_line(
        '10A NCAC 27G .0100; NC Medicaid Managed Care Tailored Plan Requirements; RMDM Chapter 1',
        '§1',
    ))
    story.append(para(
        '<b>1.1 Mission Statement.</b> Well Spring Intervention LLC is dedicated to providing '
        'trauma-informed, high-quality supervised living environments for youth with severe '
        'emotional disturbances (SED), ensuring their safety and clinical growth. Our program '
        'philosophy is rooted in the belief that every child deserves a stable, predictable, '
        'and nurturing environment in which healing can occur. All staff actions, decisions, '
        'and interventions must align with this mission and reflect our core values of safety, '
        'dignity, accountability, and growth.'
    ))
    story.append(para(
        '<b>1.2 Licensing & Credentialing.</b> The facility operates under a valid NC DHSR '
        'license (Level 3 Supervised Residential Group Home) and is credentialed as an '
        'In-Network Provider with the regional LME/MCO/Tailored Plan. The Executive Director '
        'maintains the original license on site, posts a current copy in a public area of the '
        'facility, and renews it prior to expiration. Any change in ownership, capacity, '
        'population served, or physical location requires prior written approval from DHSR '
        'and notification to the LME/MCO.'
    ))
    story.append(para(
        '<b>1.3 Corporate Compliance.</b> Well Spring Intervention LLC maintains a Corporate '
        'Compliance Plan to prevent Medicaid fraud, waste, and abuse. All staff receive '
        'compliance training upon hire and annually thereafter. The Compliance Officer '
        'receives reports, investigates concerns, and coordinates with the LME/MCO and '
        'Medicaid Fraud Investigations Unit. Retaliation against good-faith reporters is '
        'strictly prohibited and itself constitutes a reportable offense.'
    ))
    story.append(para(
        '<b>1.4 Organizational Structure.</b> The Executive Director holds overall authority '
        'and accountability. The <b>Clinical Director</b> is a licensed clinical professional '
        'with overall responsibility for the clinical program, including setting the clinical '
        'vision, approving clinical policies, and providing direction to clinical leadership. '
        'The <b>Qualified Professional (QP)</b> reports to the Clinical Director and is '
        'responsible for scheduling clinical services, assessments, PCPs, and day-to-day '
        'supervision of Associate Professionals (APs) and Direct Care Professionals (DCPs) '
        '<b>according to the direction of the Clinical Director</b>. The QP supervises staff '
        'in accordance with the Clinical Director\'s clinical guidance, programmatic '
        'priorities, and performance expectations, and shall escalate clinical concerns, '
        'staffing issues, and quality-of-care matters to the Clinical Director in a timely '
        'manner. An On-Call QP is available 24/7/365 for clinical decision-making. All '
        'staff report incidents, concerns, and operational needs through the documented '
        'chain of command.'
    ))
    story.append(Paragraph('<b>1.4(a) QP Compliance Reporting to the Clinical Director.</b>', s_h2))
    story.append(para(
        'In addition to clinical supervision, the QP shall provide <b>compliance reports</b> '
        'to the Clinical Director on a recurring basis, ensuring the Clinical Director has '
        'timely visibility into the facility\'s regulatory and documentation posture. These '
        'reports include: (a) <b>monthly</b> summaries of service-note audit findings, late '
        'entries, and alterations (per §10.1, §10.3, §10.5); (b) <b>monthly</b> IRIS '
        'incident-report status including any restraint events, restrictive interventions, '
        'and follow-up actions completed (per §5.4, §8); (c) <b>quarterly</b> Clinical Record '
        'Content Checklist audit results using Form 8, with corrective-action plans for any '
        'deficiencies; (d) <b>quarterly</b> Accounting of Disclosures review using Form 9, '
        'including any 42 CFR Part 2 disclosures; (e) <b>quarterly</b> personnel-file audit '
        'results, sanctions reviews, and training-completion rates (per §2.5); (f) '
        '<b>annual</b> review of the electronic-signature safeguards in §10.7(a), conducted '
        'jointly with the IT vendor; and (g) <b>ad-hoc</b> immediate reporting of any '
        'reportable breach, complaint, licensing visit, or Medicaid audit. The Clinical '
        'Director reviews each report, signs acknowledgment, and directs corrective action '
        'as needed. The QP retains all compliance reports and Clinical Director '
        'acknowledgments in the facility compliance binder for the full record-retention '
        'period specified in §1.6.'
    ))
    story.append(Paragraph('<b>1.4(b) QP Credentialing Requirements.</b>', s_h2))
    story.append(para(
        'The Qualified Professional (QP) for this facility must meet the credentialing '
        'requirements of <b>10A NCAC 27G .0104</b>. A QP is not required to hold a '
        'full, unrestricted clinical license. There are <b>two acceptable QP pathways</b> '
        'as set out below; either pathway satisfies the QP definition for this facility.'
    ))
    story.append(Paragraph('<b>Pathway 1 — Master\'s Degree plus Recognized NC Credential.</b>', s_h2))
    story.append(para(
        'A master\'s degree in a human services field from an accredited institution, '
        'plus <b>at least one year of full-time, post-master\'s supervised experience</b> '
        'in the delivery of mental health, developmental disabilities, or substance abuse '
        'services to the population served, plus one of the following North Carolina '
        'credentials: (i) a <b>full clinical license</b> — LCSW, LPC, LMFT, Licensed '
        'Psychologist, Licensed Psychological Associate, or psychiatrist (MD/DO); '
        '(ii) an <b>associate or provisional license</b> — LCSW-A (Associate), LPC-A '
        '(Associate), LMFT-A (Associate), or LCAS-P (Provisional); (iii) a recognized '
        '<b>certification</b> — LCAS (Licensed Clinical Addiction Specialist), CCS '
        '(Certified Clinical Supervisor) with a master\'s degree, or CMSW (Certified '
        'Master Social Worker); or (iv) for the nursing discipline, a <b>Clinical Nurse '
        'Specialist (CNS)</b> or <b>Nurse Practitioner (NP)</b> with psychiatric/mental '
        'health certification.'
    ))
    story.append(Paragraph('<b>Pathway 2 — Bachelor\'s Degree plus Supervised Experience.</b>', s_h2))
    story.append(para(
        'A <b>bachelor\'s degree in a human services field</b> from an accredited '
        'institution, plus <b>two years of full-time, pre- or post-bachelor\'s supervised '
        'experience in the delivery of mental health, developmental disabilities, or '
        'substance abuse (MH/DD/SA) services</b> to the population served. The supervised '
        'experience must be documented by the supervising QP and verifiable upon request. '
        'A bachelor\'s-degree-level QP operating under Pathway 2 is not required to hold '
        'an NC clinical license, but must complete the NC-DHHS-required QP training '
        'modules and must practice under the clinical supervision of a Pathway 1 QP (or '
        'the Clinical Director) until such training is completed.'
    ))
    story.append(Paragraph('<b>Common Requirements (Both Pathways).</b>', s_h2))
    story.append(para(
        'Regardless of pathway, every QP must: (a) complete the <b>NC-DHHS-required QP '
        'training modules</b> prior to independent practice (or be enrolled and complete '
        'them within the probationary period); (b) maintain active credential or '
        'supervised-experience documentation as applicable; (c) report any lapse, '
        'sanction, restriction, or change in supervised-experience status to the Clinical '
        'Director within one business day; and (d) have all verification documents '
        '(degree, credential, supervised-experience hours, QP training completion) '
        'retained in the personnel file (§2.5). The facility shall verify and document '
        'which pathway each QP meets at hire and re-verify annually.'
    ))
    story.append(Paragraph('<b>1.5 Data Reporting &amp; Consumer Data Warehouse (CDW).</b>', s_h2))
    story.append(para(
        'The facility shall enroll all eligible individuals in the Consumer Data Warehouse '
        '(CDW) as required by DMH/DD/SUS. The QP shall ensure termination/discharge from '
        'CDW is completed after 60 consecutive days of no billable services. Statistical '
        'data required by DHHS, the General Assembly, and federally funded programs shall '
        'be submitted per contractual requirements. The QP shall maintain a log of CDW '
        'enrollment, updates, and terminations and review it monthly.'
    ))
    story.append(Paragraph('<b>1.6 Record Retention and Disposition.</b>', s_h2))
    story.append(para(
        'Clinical service records of minors shall be retained for <b>12 years after the '
        'minor reaches the age of majority (age 18)</b> — i.e., until age 30 — or longer '
        'if required by law or pending litigation. Clinical service records of adults shall '
        'be retained for <b>11 years after the date of the last encounter</b>, or longer '
        'if required. Personnel and administrative records are retained per the DHHS '
        'Records Retention and Disposition Schedule. Incident reports and investigatory '
        'files are retained per DNCR / Division of Archives and Records requirements.'
    ))
    story.append(para(
        'Destruction of records not listed in an applicable schedule requires prior '
        'authorization from DMH/DD/SUS and the Division of Archives and Records via the '
        '"Request for Disposal of Unscheduled Records" form. <b>Record abandonment is '
        'strictly prohibited.</b> If abandonment is suspected, the facility shall notify '
        'the payor entity, relevant accrediting organizations, and DHHS, and shall '
        'cooperate fully with any investigation. Violations are subject to legal sanctions '
        'under HIPAA, 42 CFR Part 2, and the NC General Statutes.'
    ))

    # ── SOP 2 ──────────────────────────────────────────────────────
    story.append(section_heading(2, 'Human Resources & Staffing Requirements'))
    story.append(ref_line(
        '10A NCAC 27G .0203 & .5600; NC Medicaid CCP 8C; RMDM Chapter 1',
        '§2',
    ))
    story.append(para(
        '<b>2.1 Staffing Ratios.</b> Minimum staffing ratios are mandated at all times to '
        'ensure resident safety and adequate supervision. Day and evening shifts maintain a '
        '1:4 staff-to-resident ratio (awake and on-site), while the overnight shift maintains '
        'a 1:8 ratio (awake — no sleeping permitted). Ratios may be increased based on PCP '
        'acuity, behavioral incidents, or 1:1 supervision orders. The QP is responsible for '
        'monitoring ratios and adjusting assignments to maintain compliance at all times.'
    ))
    story.append(std_table(
        ['Shift', 'Minimum Ratio', 'Status', 'Notes'],
        [
            ['Day (7a-3p)', '1 : 4', 'Awake / On-site', 'May increase per PCP acuity'],
            ['Evening (3p-11p)', '1 : 4', 'Awake / On-site', 'May increase per PCP acuity'],
            ['Overnight (11p-7a)', '1 : 8', 'Awake (No sleeping)', '15-minute visual checks required'],
        ],
        [0.18*AVAIL_W, 0.15*AVAIL_W, 0.25*AVAIL_W, 0.42*AVAIL_W],
        first_col_left=True,
    ))
    story.append(Spacer(1, 8))
    story.append(Paragraph('<b>2.2 Staff Qualifications.</b>', s_h2))
    story.extend(bullets([
        '<b>QPs:</b> Meet one of two pathways per §1.4(b) and 10A NCAC 27G .0104 — <b>Pathway 1:</b> master\'s degree in a human services field plus a recognized NC credential (full license, associate/provisional license, certification, or psychiatric nursing credential) plus at least one year of full-time, post-master\'s supervised MH/DD/SA experience; OR <b>Pathway 2:</b> bachelor\'s degree in a human services field plus two years of full-time, pre- or post-bachelor\'s supervised MH/DD/SA experience. Both pathways require NC-DHHS QP training modules prior to independent practice.',
        '<b>APs:</b> Bachelor\'s in human services with at least one year of relevant experience.',
        '<b>Direct Care Professionals (DCPs):</b> High school diploma or GED with at least one year of mental health experience.',
    ]))
    story.append(Paragraph('<b>2.3 Background Checks (Prior to Unsupervised Contact).</b>', s_h2))
    story.extend(bullets([
        'NC SBI fingerprint criminal background check.',
        'Health Care Personnel Registry check.',
        'DSS Child Abuse and Neglect Registry check (every state of residence in prior 5 years).',
        'Motor Vehicle Record (MVR) for staff who transport residents.',
        'Re-checks completed annually and upon reasonable suspicion.',
    ]))
    story.append(Paragraph('<b>2.4 Mandatory Training (Prior to Independent Duty; Annual Refreshers).</b>', s_h2))
    story.extend(bullets([
        'CPR / First Aid (annually)',
        'NCI or CPI restraint and de-escalation (annually)',
        'Medication Administration (RN-delegated, annually)',
        'Bloodborne Pathogens (annually)',
        'Trauma-Informed Care (annually)',
        'Rule 108 incident reporting (annually)',
        'Adolescent development, C-SSRS suicide risk assessment, and person-centered planning (orientation + quarterly)',
    ]))
    story.append(Paragraph('<b>2.5 Personnel Records.</b>', s_h2))
    story.append(para(
        'Personnel files shall contain: position descriptions; education verification; '
        'licensure and credentials; continuing education and training records; clinical '
        'and administrative supervision documentation; supervision plans; sanctions '
        'reviews from professional boards; documented review of the NC Health Care '
        'Personnel Registry; and criminal background check results. Records shall be '
        'retained per applicable DHHS retention schedules. The QP audits personnel files '
        'annually to ensure completeness and compliance with RMDM Chapter 1.'
    ))

    # ── SOP 3 ──────────────────────────────────────────────────────
    story.append(section_heading(3, 'Admissions, Discharges, and Transition Planning'))
    story.append(ref_line(
        '10A NCAC 27G .5604; NC Medicaid CCP 8C; RMDM Chapters 2 & 5',
        '§3',
    ))
    story.append(para(
        '<b>3.1 Admission Criteria.</b> The program serves youth with a primary mental '
        'health or behavioral diagnosis requiring supervised living, who are medically '
        'stable, and whose clinical needs can be safely met in a Level 3 group home '
        'setting. Exclusions include active psychosis requiring Involuntary Commitment '
        '(IVC), medical instability, or fire-setting that cannot be safely managed. The '
        'QP reviews each referral packet and documents the admission decision.'
    ))
    story.append(Paragraph('<b>3.2 Admission Process — Pending vs. Full Records.</b>', s_h2))
    story.append(para(
        'Upon initial presentation for screening, a <b>Pending Record</b> is created. This '
        'contains initial screening information, consultation and administrative '
        'coordination, and court-ordered evaluations that do not yet result in active '
        'enrollment. If the individual is enrolled in active services, the Pending Record '
        'shall be converted into a <b>Full Clinical Service Record</b> using the same '
        'record number, with all pending documentation merged. On the Day of Admission, '
        'the QP obtains signed consents (treatment, medication, transportation, ROI, '
        'photographs), the DCP conducts a respectful property search and secures '
        'medications, the QP administers the C-SSRS screening and documents immediate '
        'clinical status, and an RN visit is scheduled within 72 hours.'
    ))
    story.append(Paragraph('<b>3.3 Full Clinical Service Record — Required Elements.</b>', s_h2))
    story.append(para(
        'Upon conversion to a Full Record, the chart must contain all applicable elements '
        'enumerated in the Comprehensive Clinical Record Content Checklist (Form 8). '
        'Categories include: Consents; Demographics and Emergency Information; Health '
        'History (including DSM-5-TR/ICD-10 diagnosis and documentation of medication '
        'allergies, adverse reactions, and <b>absence of known allergies</b>); Medications '
        'and Labs; Rights and Restrictive Interventions; Assessments (CCA by a licensed '
        'professional); Planning (PCP with MID, service plan, signed service order); '
        'Discharge information; Referral information; Service notes/grids; Incidents '
        '(filed separately; occurrence noted in record); Disclosures and Legal documents; '
        '42 CFR 2.22 summary for SUD; Accounting of Disclosures; and incoming/outgoing '
        'correspondence.'
    ))
    story.append(Paragraph('<b>3.4 Discharge & Transition.</b>', s_h2))
    story.append(para(
        'Transition planning is initiated at admission and reviewed every 30 days. '
        'Discharge may be planned or unplanned. The Discharge Summary is completed within '
        '<b>7 calendar days</b> of discharge (exceeds RMDM\'s 30-day requirement), and '
        'includes: reason for admission, course/progress, condition at discharge, '
        'recommendations, final diagnoses, and dated signatures. Medications are '
        'transferred to the guardian with a signed transfer form, belongings are '
        'inventoried, and the discharge summary is provided to the guardian, receiving '
        'provider, and LME/MCO.'
    ))
    story.append(Paragraph('<b>3.5 Administrative Closure.</b>', s_h2))
    story.append(para(
        'When a QP or clinician leaves employment without completing required discharge '
        'documentation for individuals meeting discharge criteria, the supervisor shall '
        'process the discharge. Each administratively closed record shall be audited per '
        'entity policy to ensure all billed services are properly documented. If audit '
        'reveals unmet documentation requirements, all services billed without proper '
        'documentation shall be adjusted back to the payor per 42 CFR 401.305. '
        'Documentation of the administrative closure shall be placed in the service record.'
    ))

    # ── SOP 4 ──────────────────────────────────────────────────────
    story.append(section_heading(4, 'Clinical Services, Assessments & Person-Centered Planning'))
    story.append(ref_line(
        '10A NCAC 27E .0300; NC Medicaid CCP 8C; RMDM Chapter 4',
        '§4',
    ))
    story.append(Paragraph('<b>4.1 Comprehensive Clinical Assessment (CCA).</b>', s_h2))
    story.append(para(
        'A CCA performed by a licensed professional (QP) is required <b>prior to service '
        'delivery</b>, except in crisis/emergency situations or when a current CCA (with '
        'no substantive change) is on file. The CCA must contain: (1) presenting problems, '
        'source of distress, precipitating events, associated symptoms; (2) chronological '
        'general health, past trauma, behavioral health history (MH/SU including tobacco), '
        'treatment history and response; (3) current medications for medical, psychiatric, '
        'and SUD treatment, including past ineffective medications or significant side '
        'effects; (4) review of biological, psychological, familial, social, developmental, '
        'and environmental dimensions identifying strengths, needs, and risks; (5) evidence '
        'of beneficiary and LRP participation; (6) analysis and case formulation; '
        '(7) <b>ASAM level of care determination</b> when substance use disorder is '
        'present; (8) DSM-5-TR diagnoses (MH, SUD, IDD, physical health, functional '
        'impairment); (9) recommendations for additional assessments, services, supports, '
        'or treatment; and (10) dated signature of the licensed professional completing '
        'the assessment.'
    ))
    story.append(para(
        'For children and youth, the CCA must address Child and Family Team involvement; '
        'if new to services, recommend a Child and Family Team meeting; assess strengths '
        'of the child/youth and family (preferably with a strengths-based tool); and '
        'utilize IEPs and psychological testing reports if available. <b>Reassessment</b> '
        'is required when clinically indicated (new behaviors, unmet needs, annual PCP '
        'review, or when the service definition requires). If reassessment results in a '
        'diagnosis change, a written report is required; if refinement only, a clinical '
        'note is sufficient.'
    ))
    story.append(Paragraph('<b>4.2 Medical Necessity Determination.</b>', s_h2))
    story.append(para(
        'Medical necessity is established by the QP (or licensed/certified professional) '
        'based on diagnostic criteria and established best practice guidelines. The CCA '
        'and subsequent assessments shall support medical necessity for each service '
        'delivered. Medical necessity must meet applicable Medicaid and State-funded '
        'policy requirements (NC Medicaid Behavioral Health CCPs; DMH/DD/SUS State-Funded '
        'Service Definitions). The QP documents medical necessity in the PCP.'
    ))
    story.append(Paragraph('<b>4.3 Person-Centered Plan (PCP) Development.</b>', s_h2))
    story.append(para(
        'Within <b>30 calendar days</b> of admission, the QP facilitates a PCP meeting '
        'including the youth, guardian, LME/MCO representative, and other supports '
        'identified by the family. The PCP documents strengths, needs, goals, specific '
        'interventions, and a crisis plan. The PCP is signed by all participants, reviewed '
        'every 90 days thereafter, and updated via addendum for significant clinical '
        'changes (new diagnosis, medication change, major incident, or living arrangement '
        'change). Staff implement PCP goals daily and document progress in shift notes. '
        'The QP creates a "Staff Cheat Sheet" summarizing goals, triggers, and '
        'interventions for each youth, and staff sign the PCP Acknowledgment Form.'
    ))
    story.append(Paragraph('<b>4.4 Service Orders.</b>', s_h2))
    story.append(para(
        'Service orders are required for all Medicaid and State-funded services that '
        'require them. The service order is indicated by the appropriate professional\'s '
        'signature on the PCP. If a separate format is used, a separate service order is '
        'required. <b>Verbal orders</b>: treatment may proceed based on a verbal order; '
        'the verbal order must be documented in the service record on the date given, '
        'specifying the date, who gave the order, who received the order, and each '
        'distinct service ordered. Documentation must reflect why a verbal order was '
        'obtained in lieu of a written order. The appropriate professional must '
        'countersign the order with a dated signature <b>within 72 hours</b> of the '
        'verbal order.'
    ))
    story.append(Paragraph('<b>4.5 Service Authorization.</b>', s_h2))
    story.append(para(
        'Requests for authorization are required prior to initiation or continuation of '
        'services as per State-funded service definitions, Medicaid CCPs, or the '
        'authorizing entity\'s UM policy. The facility shall notify the authorizing '
        'entity when an individual changes providers or ends a service, and end-date '
        'reporting requirements must be followed. Service authorizations and '
        'reauthorizations are not required to be maintained in the clinical record but '
        'shall be available for audit purposes if requested.'
    ))

    # ── SOP 5 ──────────────────────────────────────────────────────
    story.append(section_heading(5, 'Behavioral Management & Restraint'))
    story.append(ref_line(
        '10A NCAC 27G .0209; CMS Mental Health Parity Rules; RMDM Chapters 2 & 6',
        '§5',
    ))
    story.append(para(
        '<b>5.1 Philosophy.</b> Well Spring Intervention LLC employs a trauma-informed, '
        'positive behavioral interventions model. We recognize that behavior is '
        'communication, and our role is to teach and reinforce safer, more adaptive '
        'skills rather than punish behavior. Corporal punishment, withholding meals or '
        'sleep, social isolation as punishment, humiliation, and degradation are strictly '
        'prohibited and constitute reportable abuse under Rule 108.'
    ))
    story.append(Paragraph('<b>5.2 Behavioral Support Plan (BSP).</b>', s_h2))
    story.append(para(
        'Developed by the QP within 14 calendar days of admission, based on a Functional '
        'Behavioral Assessment (FBA). The BSP includes proactive strategies, replacement '
        'skills, de-escalation steps, and crisis responses. All staff review and sign '
        'the BSP Acknowledgment Form before working independently with the youth.'
    ))
    story.append(Paragraph('<b>5.3 Restraint.</b>', s_h2))
    story.append(para(
        'Restraint is an absolute last resort, used only when a youth is in imminent '
        'danger of serious harm to self or others and after less restrictive de-escalation '
        'has failed. Mechanical, chemical, and seclusion restraints are prohibited. Only '
        'NCI/CPI-trained staff may apply restraint, using the least restrictive hold. '
        '<b>Prone (face-down) positions are prohibited.</b> Post-restraint medical check '
        '(within 1 hour), debriefing (within 24 hours), and guardian notification '
        '(within 1 hour) are required. All restraints are reported in IRIS.'
    ))
    story.append(Paragraph('<b>5.4 Restrictive Intervention Documentation.</b>', s_h2))
    story.append(para(
        'Written notifications, consents, approvals, and other documentation per 10A NCAC '
        '27E .0104(e)(9) are required whenever a restrictive intervention is used as a '
        'planned intervention. Any planned restrictive interventions must be included in '
        'the youth\'s service plan per 10A NCAC 27E .0104(f). Documentation in the '
        'service record must meet requirements of 10A NCAC 27E .0104(g)(2) and (g)(6), '
        'including rights restrictions (G.S. §122C-62(e)) and use of protective devices.'
    ))

    # ── SOP 6 ──────────────────────────────────────────────────────
    story.append(section_heading(6, 'Health, Medication, & Nutrition Management'))
    story.append(ref_line(
        '10A NCAC 27G .0209; NC Nursing Practice Act; RMDM Chapters 5',
        '§6',
    ))
    story.append(Paragraph('<b>6.1 Medical Care.</b>', s_h2))
    story.append(para(
        'Each resident has an identified Primary Care Physician (PCP) and psychiatrist '
        'upon admission. A complete medical examination is conducted within 30 days of '
        'admission and annually thereafter. Medical history (including immunizations, '
        'allergies, and current prescriptions) is maintained and updated at every visit. '
        '<b>Immunization compliance</b> for children is documented per NCGS §130A-152. '
        'Physician\'s directions for management of any identified medical conditions '
        'must be in the record.'
    ))
    story.append(Paragraph('<b>6.2 Tuberculosis (TB) Screening.</b>', s_h2))
    story.append(para(
        '<b>Applicable if the facility receives SAPTBG funds for treatment services.</b> '
        'Screenings must query: medical treatment in the past 3 months; current residence '
        '(jail, streets, shelter, etc.); history of TB tests; and physical symptoms '
        '(night sweats, prolonged cough, shortness of breath, unexplained weight loss). '
        'Positive responses require referral to the local county health department or '
        'medical practitioner for follow-up testing and care. Completed screening and '
        'follow-up are documented in the service record.'
    ))
    story.append(Paragraph('<b>6.3 Medication Management.</b>', s_h2))
    story.append(para(
        'All medications are stored in a double-locked cabinet/cart. Controlled substances '
        'are counted and documented at every shift change. Medications are administered '
        'only by RN-delegated staff who have completed NC Medication Administration '
        'training. Staff follow the "5 Rights" (right youth, right med, right dose, '
        'right route, right time) and document administration on the MAR <b>immediately</b> '
        '(never retrospectively). Medication errors, refusals, and adverse reactions are '
        'reported to the RN and QP immediately, documented on the MAR, and entered into '
        'IRIS as required.'
    ))
    story.append(Paragraph('<b>6.4 Nutrition.</b>', s_h2))
    story.append(para(
        'Meals follow USDA guidelines. Special diets are accommodated with provider '
        'documentation. Menus are posted and retained 30 days. Food is never withheld as '
        'a consequence. Staff preparing food maintain current food handler certifications.'
    ))

    # ── SOP 7 ──────────────────────────────────────────────────────
    story.append(section_heading(7, 'Education & Vocational Support'))
    story.append(ref_line(
        'NC General Statutes (Education of Homeless Children); IDEA; RMDM Chapter 4',
        '§7',
    ))
    story.append(Paragraph('<b>7.1 Education Coordination.</b>', s_h2))
    story.append(para(
        'The QP serves as Education Liaison for every youth in the program. Within 10 '
        'calendar days of admission, the QP contacts the Local Education Agency (LEA) — '
        'specifically the McKinney-Vento liaison and the EC Director — for enrollment, '
        'transportation, and service continuity. The QP signs an ROI for school '
        'communication, attends all IEP meetings, advocates for an aligned Behavioral '
        'Intervention Plan (BIP), and tracks daily school attendance. School refusal is '
        'treated as a clinical issue addressed through the PCP, not as a behavioral '
        'violation.'
    ))
    story.append(Paragraph('<b>7.2 Vocational Support.</b>', s_h2))
    story.append(para(
        'For youth age 14 and older, the PCP includes vocational and independent-living '
        'goals aligned with the transition plan. The QP coordinates with Vocational '
        'Rehabilitation and community-based employment programs to support the youth\'s '
        'transition to adulthood and post-discharge stability.'
    ))

    # ── SOP 8 ──────────────────────────────────────────────────────
    story.append(section_heading(8, 'Incident Reporting & Response (Rule 108 / IRIS)'))
    story.append(ref_line('10A NCAC 27T (Rule 108); RMDM Chapter 6', '§8'))
    story.append(Paragraph('<b>8.1 Reportable Incidents.</b>', s_h2))
    story.append(para(
        'The following events are reportable under Rule 108 and must be entered into the '
        'Incident Reporting and Investigative System (IRIS): death (including suicide '
        'attempts resulting in death), serious injury, alleged abuse or neglect, sexual '
        'abuse allegations, use of physical restraint, AWOL/missing child, medication '
        'errors, suicidal ideation or self-harm, and any other event meeting the '
        'regulatory definition of a reportable incident. When in doubt, staff report.'
    ))
    story.append(Paragraph('<b>8.2 Reporting Timeframes.</b>', s_h2))
    story.append(para(
        'Staff notify the On-Call QP <b>immediately</b> upon discovery of a reportable '
        'incident. The QP enters the IRIS report <b>within 24 hours</b> of discovery. '
        'Allegations of abuse/neglect and missing child trigger <b>immediate (within 15 '
        'minutes)</b> notification to DSS and law enforcement as appropriate. The guardian '
        'is notified <b>within 1 hour</b> of incident discovery (unless doing so would '
        'compromise an investigation). Verbal notifications are followed by written '
        'documentation.'
    ))
    story.append(Paragraph('<b>8.3 Investigations.</b>', s_h2))
    story.append(para(
        'Internal investigations are initiated within 24 hours and completed within 14 '
        'calendar days. Investigations include interviews, video review, documentation '
        'review, and a written narrative. A Corrective Action Plan (CAP) is developed '
        'for systemic or individual performance issues and uploaded to IRIS.'
    ))
    story.append(Paragraph('<b>8.4 Incident Documentation — Separate Filing.</b>', s_h2))
    story.append(para(
        'The occurrence of an incident shall be recorded in the service notes. <b>The '
        'completed incident report shall NOT be referenced or filed in the clinical '
        'service record.</b> It shall be filed separately in administrative files. All '
        'incident reports are maintained per the Records Retention and Disposition '
        'Schedule.'
    ))
    story.append(Paragraph('<b>8.5 Abuse/Neglect/Exploitation Reporting.</b>', s_h2))
    story.append(para(
        'Relevant facts must be documented in the service record, including reports made '
        'by the individual and actions taken. Reporting duties follow G.S. §7B-301 (child '
        'abuse), G.S. §108A-102 (disabled adult), and 10A NCAC 27G .0604. The completed '
        'incident report is filed separately from the clinical record as required by '
        'RMDM Chapter 6.'
    ))

    # ── SOP 9 ──────────────────────────────────────────────────────
    story.append(section_heading(9, 'Facility, Safety, & Environmental Management'))
    story.append(ref_line('10A NCAC 27G .0600; NC Fire Code; RMDM Chapter 3', '§9'))
    story.append(Paragraph('<b>9.1 Environment.</b>', s_h2))
    story.append(para(
        'The facility maintains a safe, clean, home-like environment. Maximum occupancy '
        'is two youth per bedroom, with each youth having individual storage space for '
        'personal belongings. Indoor temperatures are maintained between 68°F and 80°F. '
        'Hot water is regulated to ≤120°F to prevent scalding. Daily safety inspections '
        'are conducted by the DCP; weekly inspections by the QP. Hazards are corrected '
        'immediately or escalated to the Executive Director.'
    ))
    story.append(Paragraph('<b>9.2 Drills & Inspections.</b>', s_h2))
    story.append(para(
        'Monthly fire drills target evacuation under 3 minutes. Quarterly tornado drills '
        'use the interior safe room. Smoke detectors, fire extinguishers, sprinklers, '
        'and CO detectors are inspected monthly (staff) and annually (licensed '
        'contractors). Inspection records are maintained on the Environmental Safety Log '
        '(Form 5) for a minimum of 3 years.'
    ))
    story.append(Paragraph('<b>9.3 Hazardous Materials.</b>', s_h2))
    story.append(para(
        'Cleaning chemicals, sharps, tools, and medications are stored in locked areas. '
        'Safety Data Sheets (SDS) are maintained and accessible. No weapons are permitted '
        'on facility grounds at any time.'
    ))

    # ── SOP 10 ─────────────────────────────────────────────────────
    story.append(section_heading(10, 'Medicaid Billing, Documentation Compliance & Record Management'))
    story.append(ref_line(
        'NC Medicaid CCP 8C; CMS Documentation Guidelines; RMDM Chapter 6; NCGS Ch. 66 Art. 40 (NC UETA); E-SIGN Act (15 U.S.C. § 7001 et seq.)',
        '§10',
    ))
    story.append(Paragraph('<b>10.1 Service Notes — General Requirements.</b>', s_h2))
    story.append(para(
        'Service notes are the supporting evidence of individual outcomes and must be '
        'individualized. <b>Photocopying or repeating notes verbatim from a prior date '
        'or another individual\'s record is strictly prohibited.</b> When referencing '
        'another individual, use initials, record number, or role (e.g., "sibling") '
        'rather than full name unless clinically pertinent and reviewed prior to release. '
        '<b>Timelines</b>: facility-based services (this program) must be documented at '
        'time of service or <b>within 1 standard business day (not to exceed 24 hours)</b>. '
        '<b>Late entries</b> are entries after the required timeframe, must be marked '
        '"Late Entry" with the date of entry and the date the service was provided '
        '(e.g., "Late Entry made on 7/15/26 for service provided on 7/10/26"), and '
        'require a dated signature. Entries exceeding the timeline can only be billed '
        'up to <b>7 business days</b> beyond the service date; after 7 days, the note '
        'is not billable.'
    ))
    story.append(Paragraph('<b>10.2 Full Service Note — Required Content.</b>', s_h2))
    story.append(para('Every shift/service note must include:'))
    story.extend(bullets([
        '<b>Name</b> of the individual receiving the service (on each page).',
        '<b>Service Record Number</b> issued by the payor along with the <b>Medicaid Identification Number (MID)</b> (as applicable), or unique identifier issued by the entity.',
        '<b>Full date</b> the service was provided (month/day/year).',
        '<b>Name of the service</b> provided.',
        '<b>Type of contact</b>: In person, Telehealth, Telephonic, or Collateral.',
        '<b>Place of service</b>.',
        '<b>Purpose</b> of the contact (tied to specific goals in the PCP/ISP).',
        '<b>Description of the interventions, treatment, and support provided</b> (specific and individualized).',
        '<b>Duration</b>: total time spent performing the service (must include active engagement). For this residential per diem service, total time is not required for billing, but interventions must accurately reflect treatment for the event/per diem.',
        '<b>Effectiveness</b> of the intervention(s) and the <b>individual\'s response/progress</b> toward goal(s).',
        '<b>Authentication</b>: electronic signature date stamp and credentials (or handwritten signature with date and credentials). <b>Use of cursive font in a Word document is NOT a valid electronic signature.</b> Pre- or post-dating signatures is prohibited.',
        'Additional requirements per Medicaid CCP or State-funded service definition.',
    ]))
    story.append(para(
        'Program, Intervention, and Evaluation (PIE) elements are part of the full '
        'service note. All required elements must be included for billing and audit '
        'purposes. Use Form 7 (Full Service Note Template) as the standardized format.'
    ))
    story.append(Paragraph('<b>10.3 Shift Notes (Twenty-Four-Hour Services).</b>', s_h2))
    story.append(para(
        'For 24-hour facilities, there must be a note for each shift, and <b>coverage '
        'hours for each shift must be clearly identified</b> in each note. If no '
        'intervention occurs (e.g., youth asleep or at school), the shift note shall '
        'reflect the care, oversight, support, and non-treatment events during the '
        'shift. When more than one staff person is providing services for a shift, '
        '<b>only one staff is required to document and sign the shift note</b>; however, '
        'the note must <b>identify the names and titles/positions of other staff persons '
        'present</b> to demonstrate staffing ratios are met.'
    ))
    story.append(Paragraph('<b>10.4 Modified Service Notes & Grids.</b>', s_h2))
    story.append(para(
        '<b>Modified notes</b> may be used only for services where explicitly allowed in '
        'CCP/State Service Definitions (e.g., Respite). Modified notes must include: '
        'Name, Service Record #/MID/Unique ID, Service provided, Date, Duration, Goal '
        'addressed/tasks performed, and Full dated signature/credentials (or initials '
        'if full signature is on the page). <b>Grids</b> may be used only for specified '
        'services (e.g., Residential Supports — NC Innovations, Respite). Grids must '
        'include: Name, Service Record #/MID/Unique ID, Service, Date, Duration, '
        'Goals/Interventions, and Full dated signature/credentials (or initials if '
        'full signature is on the page). For NC Innovations, grids must include an '
        'intervention key, progress key, and a comment section with dated entries. '
        '<b>This facility will primarily use full shift notes.</b> If using grids for '
        'Respite, the grid must meet all requirements above.'
    ))
    story.append(Paragraph('<b>10.5 Alterations to Service Documentation.</b>', s_h2))
    story.append(para(
        'The original entry must not be deleted or altered so it is not clearly legible '
        'in its original context. Corrections must be made by the person who initially '
        'authored the entry, with an explanation of the correction. If that is not '
        'possible, the person updating the documentation must reflect the needed change '
        'and the rationale. Any change must be <b>signed and dated</b>. The revised/'
        'corrected entry must be in proximity to the original entry. EHR systems with '
        'tracked changes and timestamps satisfy these guidelines. <b>Alterations '
        'exceeding 7 business days beyond the service date are not billable.</b>'
    ))
    story.append(Paragraph('<b>10.6 Authenticating Service Documentation.</b>', s_h2))
    story.append(para(
        'All entries are validated via signature (EHR or paper) with signature date, '
        'credentials, degree, licensure, and/or title. <b>Initials are only permitted</b> '
        'for updates/corrections or for notations entered on a service grid (where full '
        'signature is noted on the grid signifying appropriate initials). <b>Pre- or '
        'post-dating signatures in any form is prohibited.</b> <b>ADA Accommodations</b>: '
        'if an individual has a documented medical/physical reason (per ADA) for not '
        'being able to sign, another means for providing signature is acceptable; the '
        'process must be incorporated in facility policy. <b>Unavailable Original Author</b>: '
        'if the original author is no longer available to sign or amend an entry, a '
        'notation reflecting this shall be documented in the record and signed/dated by '
        'the appropriate party. <b>Rubber Stamps</b>: only used for medical/physical '
        'reasons with ADA accommodations; if unable to use stamp, the individual may '
        'authorize someone of their choosing in writing.'
    ))
    story.append(Paragraph('<b>10.7 Electronic Signatures.</b>', s_h2))
    story.append(para(
        'Electronic signatures are permitted for authenticating service documentation, '
        'consents, treatment plans, and other records governed by this manual, in '
        'accordance with the <b>North Carolina Uniform Electronic Transactions Act '
        '(NCGS Chapter 66, Article 40)</b> and the federal E-SIGN Act (15 U.S.C. '
        '&sect; 7001 et seq.). An electronic signature is an electronic sound, symbol, '
        'or process attached to or logically associated with a record and executed or '
        'adopted by a person with the intent to sign the record. Where electronic '
        'signatures are used, they carry the same legal weight and enforceability as '
        'handwritten signatures for transactions conducted electronically. <b>Use of a '
        'cursive font in a word-processing document does not constitute a valid '
        'electronic signature</b>; the signature must be applied through the facility\'s '
        'authenticated EHR/EMR system or an approved secure signing platform that '
        'captures the signer\'s identity, timestamp, and intent. Each electronic '
        'signature shall be uniquely linked to the signer, render any subsequent '
        'modification detectable, and include an auditable timestamp reflecting the '
        'date and time of execution.'
    ))
    story.append(Paragraph('<b>10.7(a) Safeguards.</b>', s_h2))
    story.append(para(
        'The facility shall implement and maintain reasonable administrative, '
        'technical, and physical safeguards to ensure the integrity, confidentiality, '
        'and non-repudiation of electronic signatures, consistent with the HIPAA '
        'Security Rule (45 CFR Part 164 Subpart C), 42 CFR Part 2, and NCGS '
        '&sect; 66-40(d). Required safeguards include: (a) <b>unique user credentials</b> '
        'for each authorized signer, with shared logins strictly prohibited; '
        '(b) <b>multi-factor authentication</b> where technically feasible; '
        '(c) <b>automatic session timeout</b> after no more than 15 minutes of '
        'inactivity; (d) <b>encrypted transmission</b> (TLS 1.2 or higher) and '
        '<b>at-rest encryption</b> of all signed records; (e) <b>immutable audit '
        'trails</b> capturing the signer\'s identity, date, time, IP address or device '
        'identifier, and the document version signed; (f) <b>role-based access '
        'controls</b> limiting signature authority to staff with appropriate '
        'licensure, credentials, and documented training; (g) <b>immediate '
        'revocation</b> of credentials upon termination, role change, or suspected '
        'compromise; and (h) <b>annual review</b> by the QP and IT vendor to verify '
        'continued compliance. Lost, stolen, or shared credentials must be reported '
        'to the QP within one business day; the facility shall deactivate the '
        'compromised credentials and investigate the scope of any unauthorized '
        'signatures before reissuing access.'
    ))
    story.append(Paragraph('<b>10.7(b) System Unavailability Procedures.</b>', s_h2))
    story.append(para(
        'In the event the EHR/EMR system or approved electronic signing platform is '
        'unavailable — whether due to planned maintenance, internet outage, vendor '
        'outage, cyber-incident, or natural disaster — staff shall revert to '
        'paper-based documentation and handwritten signatures with date, credentials, '
        'and title. The QP or designee shall declare a <b>Documentation Continuity '
        'Event</b>, notify all shifts in writing (or by phone tree if email is '
        'unavailable), and distribute blank copies of the required forms (Shift Note, '
        'MAR, Restraint &amp; Debriefing Checklist, Incident Report). Staff shall '
        'legibly sign and date each paper entry in blue or black ink. When the '
        'electronic system is restored — and in no event later than <b>72 hours</b> '
        'after the original entry — the originating staff member (or, if unavailable, '
        'the on-duty QP) shall transcribe the paper entry verbatim into the '
        'electronic record, mark the entry as <i>"Late Entry &mdash; System '
        'Unavailability (date/time of restoration)"</i>, reference the original paper '
        'document by scan or filename, and electronically sign the transcribed entry. '
        'The original paper document shall be scanned and attached to the electronic '
        'record, then retained as a source document per the record retention policy '
        '(§1.6) for the full retention period. Paper entries that cannot be '
        'transcribed within <b>7 business days</b> must be reviewed by the QP, who '
        'shall document the reason for delay and the corrective action taken. The QP '
        'shall maintain a log of all Documentation Continuity Events, including the '
        'start/end time, cause, records affected, and verification that all paper '
        'entries were transcribed and electronically authenticated.'
    ))
    story.append(Paragraph('<b>10.8 Service Authorizations & End-Date Reporting.</b>', s_h2))
    story.append(para(
        'The facility shall maintain service authorizations/reauthorizations in a '
        'separate audit file (not required in clinical record but available upon '
        'request). When a youth changes providers or ends a service, the facility must '
        'notify the authorizing entity per their specified protocol. End-date reporting '
        'shall follow the authorizing entity\'s requirements.'
    ))
    story.append(Paragraph('<b>10.9 Billing.</b>', s_h2))
    story.append(para(
        'The program bills Medicaid on a daily per diem basis. Billing is suspended for '
        'any day the youth is hospitalized, detained, or on a home pass exceeding '
        '<b>24 consecutive hours</b>. The Home Pass & Medicaid Billing Exclusion Tracker '
        '(Form 4) documents all absences and corresponding billing action. Billing '
        'errors are corrected promptly and reported to the LME/MCO as required. Records '
        'are released only with a signed ROI or as required by law, court order, or '
        'regulatory audit.'
    ))

    # ── SOP 11 ─────────────────────────────────────────────────────
    story.append(section_heading(11, 'Privacy, Security, Confidentiality & Access to Records'))
    story.append(ref_line(
        'RMDM Chapter 3; HIPAA Privacy/Security Rule; 42 CFR Part 2; HITECH Act; NCGS §122C-52 through 122C-56',
        '§11',
    ))
    story.append(Paragraph('<b>11.1 Privacy and Security Policies.</b>', s_h2))
    story.append(para(
        'The facility shall maintain comprehensive policies addressing how information is '
        'recorded, stored, retrieved, disseminated, and protected against loss, theft, '
        'destruction, unauthorized access (breach), and natural disasters. Compliance '
        'with the HIPAA Privacy and Security Rules, the Omnibus HIPAA final rule, the '
        'HITECH Act, and ARRA is mandatory. Policies shall address electronic '
        'communication (email, voice messaging, SMS/text speak, EHR usage). Where '
        'multiple requirements exist, the <b>most stringent</b> applies, including '
        'professional codes of ethics.'
    ))
    story.append(Paragraph('<b>11.2 Safeguards.</b>', s_h2))
    story.append(para(
        'Formal policies and procedures shall reasonably protect against unauthorized '
        'uses and disclosures of PHI, and against reasonably anticipated threats or '
        'hazards (42 CFR § 2.16). Secure storage: locked, climate-controlled areas with '
        'limited access; electronic records backed up daily and stored securely off-site.'
    ))
    story.append(Paragraph('<b>11.3 Confidentiality.</b>', s_h2))
    story.append(para(
        'Compliance is required with NCGS §122C-51 through 122C-56; 10A NCAC 26B; '
        '<b>42 CFR Part 2</b> (Confidentiality of Alcohol and Drug Abuse Patient '
        'Records); and NCGS §130A-143 (AIDS and related conditions). <b>Substance Use '
        'Information</b>: requires the individual\'s written authorization before '
        'disclosure to other treatment providers (unless court order or allowable '
        'exception per 42 CFR Part 2). Absent written consent, entities must redact '
        'all identifying information from alcohol/drug records when sharing. '
        '<b>Care Coordination Exceptions</b>: under HIPAA and NCGS §122C-55(a), '
        'entities may share confidential information for coordination of care/treatment '
        'without written consent (requirements of NCGS §122C-55(a)7 apply); however, '
        '42 CFR Part 2 still requires written authorization for SUD records.'
    ))
    story.append(Paragraph('<b>11.4 Disclosure Documentation and Accounting.</b>', s_h2))
    story.append(para(
        'Authorization must be in writing, voluntary, and informed (understanding what '
        'is exchanged, with whom, and for what purpose). Staff must verify the identity '
        'of the person requesting PHI and obtain required documentation/representations '
        'per Omnibus HIPAA rules. The <b>minimum necessary</b> standard (164.502(b)) '
        'applies. <b>Accounting of Disclosures</b> must be maintained for a minimum of '
        '<b>six years</b>. The accounting must include: name of the individual; medical '
        'record or ID number; date the information was released/disclosed; provider/'
        'entity/agency/individual to whom information was released; purpose of the '
        'release/disclosure; description of specific information released/disclosed; '
        'and name of person disclosing the information (recommended). All disclosures '
        'or re-disclosures of SUD treatment information must comply with 42 CFR Part 2; '
        're-disclosure is prohibited except per NCGS §122C-53 through 122C-56. '
        'Releases/disclosures from external entities must be contained in the '
        'individual\'s service record.'
    ))
    story.append(Paragraph('<b>11.5 Individual Access to Service Records.</b>', s_h2))
    story.append(para(
        'Individuals and Legally Responsible Persons (LRPs) have the right to access '
        'information contained in their service record, per NCGS and DHHS provisions. '
        '<b>Limited Access</b>: if access is restricted, proper justification for '
        'restricting access must be clearly indicated in the service record. Individuals '
        'have the right to appeal such determination. Refer to Article 3, Part 1 (Client '
        'Rights), the Omnibus HIPAA Final Rule, and DHHS Privacy/Security policies.'
    ))
    story.append(Paragraph('<b>11.6 Transporting Records.</b>', s_h2))
    story.append(para(
        'Service records shall only be transported by designated individuals (hard copy, '
        'USB, tablet, CPU, etc.). When removed from premises, records shall be secured '
        'in a locked compartment and protected from unauthorized access. Policy must '
        'address what occurs if information is lost or stolen during transport, '
        'including immediate notification of the QP, Compliance Officer, and — if PHI '
        'is compromised — notification of affected individuals and DHHS per breach '
        'notification rules.'
    ))
    story.append(Paragraph('<b>11.7 Storage and Maintenance.</b>', s_h2))
    story.append(para(
        'Storage and maintenance are consistent with privacy/security principles. '
        'Electronic records self-warranty per NC State Archives guidelines. "Managing '
        'Public Records Produced by Information Technology Systems" guidelines apply. '
        'The QP conducts quarterly audits of storage security and access logs.'
    ))

    return story
