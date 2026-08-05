"""
carf_plans_content.py — Content module for the WSI CARF CYS 2026 Conformance
Plan Portfolio.

Produces 15 fully-developed written plans/policies referenced in SOP §12.1–§12.18
and §12.19 of the Well Spring Intervention LLC SOP Manual v2.24:

  1.  Strategic Plan                              (§12.1)
  2.  Stakeholder Input Plan                      (§12.2)
  3.  Legal Compliance Plan                       (§12.3)
  4.  Financial Plan                              (§12.4)
  5.  Enterprise Risk Management Plan             (§12.5)
  6.  Health & Safety Committee Charter           (§12.6)
  7.  Workforce Development Plan                  (§12.7)
  8.  Resident Rights Policy Compilation          (§12.8)
  9.  Accessibility & Nondiscrimination Plan      (§12.9)
  10. Performance Measurement Plan                (§12.10)
  11. Program Description                         (§12.11)
  12. Screening and Access Policy                 (§12.12)
  13. Quality Records Review Procedure            (§12.17)
  14. Telehealth & ICT Service Delivery Policy    (§12.18)
  15. CARF CYS 2026 Sections 3-5 Standards Crosswalk (§12.19)

Each plan is a self-contained written policy with: Purpose, Scope, Policy
statement, Procedure (numbered steps), Responsible Parties, Review Schedule,
and Approval signature block.

This module imports helpers/styles from generate_sop to maintain visual
consistency with the SOP Manual.
"""
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
    HEADER_FILL, BORDER, ACCENT, ACCENT_2, TEXT_PRIMARY, TEXT_MUTED,
    CARD_BG, TABLE_ROW_ODD, TABLE_ROW_EVEN,
    AVAIL_W,
)


def _plan_header(plan_num, plan_title, sop_ref):
    """Standard plan header: section_heading + ref_line + Purpose intro."""
    story = []
    story.append(section_heading(plan_num, plan_title))
    story.append(ref_line(anchor=sop_ref))
    return story


def _approval_block(plan_title):
    """Standard approval signature block at end of each plan."""
    story = []
    story.append(Spacer(1, 12))
    story.append(Paragraph('<b>Plan Approval</b>', s_h2))
    story.append(para(
        f'The undersigned approve this <b>{plan_title}</b> as a written policy of '
        f'Well Spring Intervention LLC, effective upon the date of the last signature '
        f'below. This plan shall be reviewed at minimum annually and updated as '
        f'needed to reflect changes in CARF standards, regulatory requirements, '
        f'organizational structure, or program design. The QP maintains the signed '
        f'original in the facility compliance binder and provides a copy to all '
        f'personnel with implementation responsibilities.'
    ))
    story.append(Spacer(1, 8))
    sig_data = [
        ['Role', 'Name (Printed)', 'Signature', 'Date'],
        ['Executive Director', '', '', ''],
        ['Clinical Director', '', '', ''],
        ['Qualified Professional (QP)', '', '', ''],
        ['Compliance Officer', '', '', ''],
    ]
    sig_th = ParagraphStyle('sigth', fontName=BODY_BOLD, fontSize=9.5, leading=12,
                             textColor=colors.white, alignment=TA_LEFT)
    sig_td = ParagraphStyle('sigtd', fontName=BODY_FONT, fontSize=9.5, leading=12,
                             textColor=TEXT_PRIMARY, alignment=TA_LEFT)
    sig_data_p = [[Paragraph(f'<b>{h}</b>', sig_th) for h in sig_data[0]]]
    for row in sig_data[1:]:
        sig_data_p.append([Paragraph(c, sig_td) for c in row])
    t = Table(sig_data_p, colWidths=[0.22*AVAIL_W, 0.28*AVAIL_W, 0.32*AVAIL_W, 0.18*AVAIL_W],
              hAlign='CENTER', repeatRows=1)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), HEADER_FILL),
        ('GRID', (0, 0), (-1, -1), 0.4, BORDER),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING', (0, 0), (-1, -1), 4),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4),
        ('TOPPADDING', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
    ]))
    story.append(t)
    story.append(Spacer(1, 12))
    return story


def build_part1():
    """Build all 15 plans as one continuous story."""
    story = []

    # ── Part divider ───────────────────────────────────────────────
    story.extend(part_divider(
        'CARF CYS 2026 CONFORMANCE PLANS',
        'Written Policies, Plans & Procedures Portfolio',
        'This portfolio contains the fifteen written plans, policies, and procedures '
        'referenced in §12.1–§12.19 of the Well Spring Intervention LLC SOP Manual '
        '(Rev. 2.24) required to demonstrate conformance to the 2026 CARF Child and '
        'Youth Services (CYS) Standards Manual at the time of an Inaugural One-Year '
        'Accreditation survey. Each plan is a self-contained written policy with '
        'purpose, scope, policy statement, procedure, responsible parties, review '
        'schedule, and approval signature block. Plans are presented in the order '
        'they are referenced in §12. The QP maintains the signed originals in the '
        'facility compliance binder and presents this portfolio to CARF surveyors '
        'as the primary evidence of organizational readiness.',
    ))

    # ════════════════════════════════════════════════════════════════
    # PLAN 1 — STRATEGIC PLAN (§12.1)
    # ════════════════════════════════════════════════════════════════
    story.extend(_plan_header(1, 'Strategic Plan', '§12.1'))
    story.append(Paragraph('<b>1.1 Purpose.</b>', s_h2))
    story.append(para(
        'The Strategic Plan establishes the long-term direction of Well Spring '
        'Intervention LLC and demonstrates conformance to CARF CYS Section 1.A '
        '(Leadership) and Section 1.C (Strategic Planning). It documents the '
        'organization\'s mission, vision, and values; identifies the populations '
        'to be served and the services to be provided; analyzes the internal and '
        'external environment; sets measurable strategic goals over a three-year '
        'horizon; and assigns responsibility and resources for execution. The '
        'Strategic Plan is the primary evidence of leadership\'s intentional '
        'direction of the organization and is presented to the CARF survey team '
        'at the Inaugural Accreditation survey as the foundational governance '
        'document.'
    ))
    story.append(Paragraph('<b>1.2 Scope.</b>', s_h2))
    story.append(para(
        'This plan applies to the entire organization, including the Governing '
        'Body, Executive Director, Clinical Director, Qualified Professional (QP), '
        'all direct-care and administrative personnel, contractors, and volunteers. '
        'It governs strategic decisions related to program design, population '
        'served, service array, geographic service area, capital development, '
        'workforce composition, financial structure, and accreditation strategy. '
        'Tactical and operational decisions are governed by the SOP Manual and '
        'are not within the scope of this Strategic Plan.'
    ))
    story.append(Paragraph('<b>1.3 Mission, Vision &amp; Values.</b>', s_h2))
    story.append(para(
        '<b>Mission.</b> Well Spring Intervention LLC provides trauma-informed, '
        'high-quality supervised living environments for youth with severe '
        'emotional disturbances (SED), ensuring their safety and clinical growth '
        'through individualized, evidence-based care.'
    ))
    story.append(para(
        '<b>Vision.</b> Every child served by Well Spring Intervention LLC will '
        'experience a stable, predictable, and nurturing environment in which '
        'healing occurs, families are strengthened, and youth transition to less '
        'restrictive settings with the skills and supports needed to thrive.'
    ))
    story.append(para(
        '<b>Values.</b> Safety · Dignity · Accountability · Growth · Empowerment · '
        'Freedom · Health · Wholeness · Healing. These values inform every '
        'personnel decision, clinical intervention, and operational practice.'
    ))
    story.append(Paragraph('<b>1.4 Populations &amp; Services.</b>', s_h2))
    story.append(para(
        'The organization serves children and adolescents (target age range 6–17) '
        'with a primary diagnosis of mental illness, emotional disturbance, or '
        'substance-related disorder, who do not meet inpatient psychiatric '
        'criteria but require removal from the home and treatment in a Level '
        'III Residential Treatment Facility (hardware-secure, intensive '
        'clinical). The service array includes: 24-hour residential treatment '
        'in a Level III RTF licensed under 10A NCAC 27G .1703; clinical '
        'services including individual therapy (minimum 2 sessions/week), '
        'group therapy (daily), family therapy (minimum weekly), and '
        'comprehensive clinical assessments; psychiatric medication management '
        'with on-site psychiatric coverage and 24/7 on-call psychiatric '
        'consultation; behavioral support and crisis intervention with '
        'line-of-sight supervision capability for high-acuity residents; '
        'educational coordination through the local public school system or '
        'facility-based instructional programming; case management and care '
        'coordination with the LME/MCO and other system-of-care partners; '
        'and structured recreational, social, and life-skills programming '
        'integrated into the daily milieu-therapy schedule.'
    ))
    story.append(Paragraph('<b>1.5 Environmental Analysis.</b>', s_h2))
    story.append(para(
        'The Strategic Plan incorporates an annual environmental analysis '
        'considering input from persons served (via the Stakeholder Input Plan, '
        'Plan 2), personnel (via the annual engagement survey), funders (via '
        'Alliance Health and NCDHHS communications), referral sources (via '
        'quarterly referral-pattern review), and the community (via the annual '
        'community advisory convening). The analysis identifies opportunities '
        '(e.g., emerging Medicaid benefit categories, community partnerships, '
        'workforce pipeline programs) and threats (e.g., workforce shortages, '
        'reimbursement rate changes, regulatory shifts, competitive entrants) '
        'over the three-year horizon.'
    ))
    story.append(Paragraph('<b>1.6 Three-Year Strategic Goals (2026–2028).</b>', s_h2))
    story.append(para(
        '<b>Goal 1 — Inaugural CARF Accreditation.</b> Achieve CARF Child &amp; '
        'Youth Services Inaugural One-Year Accreditation by Q1 2027 and '
        'subsequent full Three-Year Accreditation by Q1 2028. Owner: Executive '
        'Director. Measure: Accreditation certificate on file; QIP submitted '
        'within 90 days of notification (Form 12).'
    ))
    story.append(para(
        '<b>Goal 2 — Census Stabilization.</b> Achieve and sustain an average '
        'daily census of 90% of licensed capacity by Q4 2026, with no more than '
        '10% of admissions resulting in unplanned discharge within 30 days. '
        'Owner: Executive Director &amp; QP. Measure: Monthly census report to '
        'Governing Body; discharge-trend dashboard.'
    ))
    story.append(para(
        '<b>Goal 3 — Workforce Stability.</b> Reduce personnel turnover to below '
        '25% annually (industry benchmark) by Q4 2027, with 100% of direct-care '
        'personnel completing the orientation curriculum and annual refresher '
        'training per Plan 7. Owner: QP. Measure: Quarterly personnel engagement '
        'survey; monthly turnover report.'
    ))
    story.append(para(
        '<b>Goal 4 — Clinical Outcomes Excellence.</b> Demonstrate measurable '
        'clinical improvement in 80% of youth served, as measured by validated '
        'symptom and functioning instruments (e.g., PHQ-A, GAD-7, CAFAS) at '
        'admission vs. discharge. Owner: Clinical Director. Measure: Quarterly '
        'outcomes report to Governing Body per Plan 10.'
    ))
    story.append(para(
        '<b>Goal 5 — Financial Sustainability.</b> Maintain a minimum of 60 days '
        'cash-on-hand, achieve annual independent financial audit with no '
        'material findings, and sustain operating margins sufficient to fund '
        'the capital-replacement reserve per Plan 4. Owner: Executive Director. '
        'Measure: Quarterly financial report to Governing Body.'
    ))
    story.append(Paragraph('<b>1.7 Action Plans &amp; Evaluation.</b>', s_h2))
    story.append(para(
        'Each strategic goal has a written action plan identifying the responsible '
        'party, required resources, timeline (quarterly milestones), and '
        'evaluation method. The QP tracks action-plan progress monthly and '
        'reports status to the Executive Director. The Governing Body reviews '
        'progress against the Strategic Plan at each quarterly meeting and '
        'authorizes revisions as needed. The Strategic Plan is reviewed and '
        'updated in full at least annually, with the annual revision '
        'incorporating the year\'s environmental analysis, performance data '
        '(Plan 10), stakeholder input (Plan 2), and any QIP actions (Plan 12 '
        'in SOP §12.20).'
    ))
    story.append(Paragraph('<b>1.8 Succession Planning.</b>', s_h2))
    story.append(para(
        'The Strategic Plan includes a written succession plan for the Executive '
        'Director, Clinical Director, and QP positions. For each role, the '
        'succession plan identifies: (a) the position\'s core competencies and '
        'credentialing requirements; (b) internal candidates and their '
        'development needs; (c) external recruitment strategy and pipeline; '
        '(d) interim coverage procedures in the event of sudden vacancy; and '
        '(e) knowledge-transfer and documentation requirements. The succession '
        'plan is reviewed annually and following any key leadership change.'
    ))
    story.append(Paragraph('<b>1.9 Responsible Parties.</b>', s_h2))
    story.append(para(
        '<b>Executive Director</b> — overall accountability for the Strategic '
        'Plan; chairs the strategic planning process; presents the plan to the '
        'Governing Body. <b>Governing Body</b> — reviews, approves, and monitors '
        'the Strategic Plan at each quarterly meeting. <b>QP</b> — coordinates '
        'data collection, environmental analysis, and progress tracking; '
        'maintains the Strategic Plan in the compliance binder. <b>Clinical '
        'Director</b> — provides clinical program input and outcome data. '
        '<b>Compliance Officer</b> — ensures alignment with CARF, regulatory, '
        'and accreditation requirements.'
    ))
    story.append(Paragraph('<b>1.10 Review Schedule.</b>', s_h2))
    story.append(para(
        'Annual full review and revision (due: July 1 of each year, '
        'synchronized with the CARF standards-manual effective date). Quarterly '
        'progress reviews at each Governing Body meeting. Ad-hoc revision '
        'triggered by: significant environmental change, serious incident, '
        'accreditation finding, regulatory change, or leadership transition.'
    ))
    story.extend(_approval_block('Strategic Plan'))
    story.append(PageBreak())

    # ════════════════════════════════════════════════════════════════
    # PLAN 2 — STAKEHOLDER INPUT PLAN (§12.2)
    # ════════════════════════════════════════════════════════════════
    story.extend(_plan_header(2, 'Stakeholder Input Plan', '§12.2'))
    story.append(Paragraph('<b>2.1 Purpose.</b>', s_h2))
    story.append(para(
        'The Stakeholder Input Plan demonstrates conformance to CARF CYS Section '
        '1.D by establishing written methods for gathering, analyzing, and acting '
        'on input from persons served, their families/Legally Responsible Persons '
        '(LRPs), personnel, referral sources, payers, and the community. The '
        'plan ensures that the organization\'s strategic direction, program '
        'design, and service delivery are informed by the voices of those most '
        'affected by its work, and that the organization communicates back to '
        'stakeholders how their input was used.'
    ))
    story.append(Paragraph('<b>2.2 Scope.</b>', s_h2))
    story.append(para(
        'This plan covers all input-gathering activities conducted by the '
        'organization, including surveys, focus groups, advisory convenings, '
        'grievance data, complaint logs, and informal feedback channels. It '
        'applies to all personnel who interact with stakeholders, including '
        'direct-care staff, clinical staff, the QP, the Executive Director, '
        'and Governing Body members.'
    ))
    story.append(Paragraph('<b>2.3 Input Methods.</b>', s_h2))
    story.append(para(
        'The organization uses at least four structured methods for gathering '
        'stakeholder input:'
    ))
    story.extend(bullets([
        '<b>Quarterly Youth Satisfaction Survey.</b> Developmentally appropriate, '
        'anonymous, offered in English and the youth\'s preferred language; '
        'covers safety, respect, food, activities, school, clinical services, '
        'family contact, and overall satisfaction. Administered by the QP or '
        'designee; results aggregated by facility and trended quarterly.',
        '<b>Semi-Annual Family/LRP Feedback Survey.</b> Distributed electronically '
        'and on paper; covers communication, visitation, treatment planning '
        'participation, satisfaction with clinical services, and recommendations. '
        'Results shared with the Clinical Director and the CFT.',
        '<b>Annual Personnel Engagement Survey.</b> Anonymous; covers supervision, '
        'training, safety, workload, communication, leadership, and intent to '
        'remain. Results presented to the Governing Body and inform the '
        'Workforce Development Plan (Plan 7).',
        '<b>Annual Community/Stakeholder Advisory Convening.</b> Open invitation '
        'to LME/MCO representatives, school personnel, DSS, juvenile justice, '
        'former residents and families (with consent), faith community, and '
        'neighborhood residents. Facilitated discussion of program strengths, '
        'gaps, and opportunities; minutes documented and posted.',
    ]))
    story.append(Paragraph('<b>2.4 Input Aggregation &amp; Analysis.</b>', s_h2))
    story.append(para(
        'The QP aggregates all input data at least quarterly, analyzes for '
        'themes and trends, and prepares a written summary for the Governing '
        'Body. The summary identifies: (a) the input methods used; (b) the '
        'number of respondents per method; (c) the key themes; (d) the actions '
        'taken or planned in response; and (e) any unresolved issues requiring '
        'Governing Body direction. Quantitative survey results are presented '
        'with comparison to prior periods to identify trends.'
    ))
    story.append(Paragraph('<b>2.5 "You Said / We Did" Feedback Loop.</b>', s_h2))
    story.append(para(
        'The organization communicates back to stakeholders how their input was '
        'used through visible "You Said / We Did" postings in the facility '
        'common area (updated monthly), in resident community meetings (weekly), '
        'in family newsletters (quarterly), and in personnel meetings (monthly). '
        'This closed-loop feedback is essential to maintaining stakeholder trust '
        'and demonstrating that input is valued and acted upon.'
    ))
    story.append(Paragraph('<b>2.6 Use of Input.</b>', s_h2))
    story.append(para(
        'Stakeholder input directly informs: (a) the annual revision of the '
        'Strategic Plan (Plan 1); (b) the Person-Centered Plan for each youth '
        '(SOP §4.1); (c) program structure and service array decisions (Plan '
        '11); (d) the Workforce Development Plan (Plan 7); (e) the Performance '
        'Measurement Plan (Plan 10); and (f) the Quality Improvement Plan '
        'submitted to CARF (SOP §12.20, Form 12).'
    ))
    story.append(Paragraph('<b>2.7 Non-Retaliation.</b>', s_h2))
    story.append(para(
        'The organization prohibits retaliation against any person served, '
        'family member, LRP, personnel member, or other stakeholder for '
        'providing input, filing a grievance, or reporting a concern. The '
        'non-retaliation policy is published in the Resident Handbook, the '
        'personnel handbook, and posted in the facility. Personnel who '
        'engage in retaliation are subject to disciplinary action up to and '
        'including termination. The QP investigates any allegation of '
        'retaliation within 5 business days.'
    ))
    story.append(Paragraph('<b>2.8 Responsible Parties.</b>', s_h2))
    story.append(para(
        '<b>QP</b> — overall coordination of input-gathering activities, data '
        'aggregation, analysis, and reporting. <b>Executive Director</b> — '
        'convenes the annual community advisory convening; presents input '
        'summary to Governing Body. <b>Governing Body</b> — reviews input '
        'summary at each quarterly meeting; directs action. <b>All Personnel</b> '
        '— encourage stakeholder input, do not retaliate, communicate the '
        '"You Said / We Did" feedback.'
    ))
    story.append(Paragraph('<b>2.9 Review Schedule.</b>', s_h2))
    story.append(para(
        'Quarterly review of input data and aggregation. Annual review of the '
        'Stakeholder Input Plan itself (method effectiveness, response rates, '
        'representation). Ad-hoc review following any grievance trend, serious '
        'incident, or significant stakeholder concern.'
    ))
    story.extend(_approval_block('Stakeholder Input Plan'))
    story.append(PageBreak())

    # ════════════════════════════════════════════════════════════════
    # PLAN 3 — LEGAL COMPLIANCE PLAN (§12.3)
    # ════════════════════════════════════════════════════════════════
    story.extend(_plan_header(3, 'Legal Compliance Plan', '§12.3'))
    story.append(Paragraph('<b>3.1 Purpose.</b>', s_h2))
    story.append(para(
        'The Legal Compliance Plan demonstrates conformance to CARF CYS Section '
        '1.E by establishing a written framework for identifying, monitoring, '
        'and complying with all applicable federal, state, and local legal '
        'requirements governing the organization and the program. The plan '
        'designates a Compliance Officer responsible for monitoring legal '
        'requirements and coordinating the annual legal-compliance review.'
    ))
    story.append(Paragraph('<b>3.2 Scope.</b>', s_h2))
    story.append(para(
        'This plan applies to all legal and regulatory requirements applicable '
        'to the organization\'s operations, including licensure, Medicaid '
        'provider enrollment, health-care fraud and abuse laws, health-privacy '
        'law, child-mandated-reporter law, disability-rights law, civil-rights '
        'law, employment law, and zoning/fire/building/life-safety codes. It '
        'covers written policies, monitoring activities, response to legal '
        'inquiries, and reporting of potential violations.'
    ))
    story.append(Paragraph('<b>3.3 Compliance Officer Designation.</b>', s_h2))
    story.append(para(
        'The Executive Director designates a Compliance Officer (may be the QP) '
        'responsible for: (a) monitoring changes in legal requirements; (b) '
        'maintaining the Legal Compliance Register (Section 3.5); (c) '
        'coordinating the annual legal-compliance review; (d) investigating '
        'reports of potential violations; (e) reporting identified violations '
        'to the Governing Body within 5 business days of discovery; and (f) '
        'coordinating with legal counsel. The Compliance Officer reports '
        'directly to the Executive Director and has access to the Governing '
        'Body as needed.'
    ))
    story.append(Paragraph('<b>3.4 Applicable Legal Requirements.</b>', s_h2))
    story.append(para(
        'The organization maintains written policies addressing compliance with '
        'the following categories of legal requirements:'
    ))
    story.extend(bullets([
        '<b>Licensure.</b> Level III Residential Treatment Facility '
        '(Hardware-Secure) license issued by the NC Department of Health and '
        'Human Services under 10A NCAC 27G .1703 (SOP §1.2); renewed prior '
        'to expiration; changes in ownership, capacity, population, or '
        'location require prior written approval. Level III is the highest-'
        'acuity NC RTF category and authorizes the organization to serve '
        'children and adolescents with severe emotional disturbance whose '
        'clinical needs cannot be safely met in a less restrictive (Level I '
        'or II) residential setting.',
        '<b>Medicaid Provider Enrollment.</b> Enrollment with NCTracks and '
        'Alliance Health; revalidation per CMS schedule; compliance with Medicaid '
        'fraud and abuse laws (False Claims Act, Anti-Kickback Statute, '
        'Physician Self-Referral Law) (SOP §10).',
        '<b>Health Privacy.</b> HIPAA Privacy, Security, and Breach Notification '
        'Rules; HITECH Act; 42 CFR Part 2 (SUD records confidentiality); state '
        'law on AIDS/confidential conditions (SOP §11).',
        '<b>Child Mandated Reporting.</b> State law requiring all personnel to '
        'report suspected child abuse/neglect to DSS; written reporting '
        'procedure (SOP §8).',
        '<b>Disability Rights.</b> Americans with Disabilities Act (ADA) Title '
        'III; Section 504 of the Rehabilitation Act; state disability-rights '
        'law (Plan 9).',
        '<b>Civil Rights.</b> Title VI of the Civil Rights Act; Age '
        'Discrimination Act; state civil-rights law (Plan 9).',
        '<b>Employment Law.</b> Fair Labor Standards Act; Family and Medical '
        'Leave Act; Equal Employment Opportunity laws; OSHA; state employment '
        'law; workers\' compensation.',
        '<b>Life-Safety Codes.</b> NFPA 101 Life Safety Code; state fire code; '
        'building code; zoning ordinance (SOP §9).',
        '<b>Accreditation.</b> CARF CYS 2026 Standards Manual; 2026 CYS '
        'Inaugural Accreditation Guidelines (SOP §12).',
    ]))
    story.append(Paragraph('<b>3.5 Legal Compliance Register.</b>', s_h2))
    story.append(para(
        'The Compliance Officer maintains a written Legal Compliance Register '
        'listing each applicable legal requirement, the controlling authority, '
        'the responsible position, the most recent review date, the next review '
        'due date, and the status. The Register is reviewed monthly by the '
        'Compliance Officer and presented to the Governing Body at each '
        'quarterly meeting. The Register is the source-of-truth document for '
        'all legal compliance activities.'
    ))
    story.append(Paragraph('<b>3.6 Annual Legal-Compliance Review.</b>', s_h2))
    story.append(para(
        'The Compliance Officer coordinates an annual legal-compliance review, '
        'engaging legal counsel as needed. The review covers each item in the '
        'Legal Compliance Register, verifies current compliance, identifies any '
        'gaps, and documents corrective actions. The written annual review '
        'report is presented to the Executive Director and the Governing Body, '
        'with an attestation of compliance signed by the Executive Director and '
        'Clinical Director.'
    ))
    story.append(Paragraph('<b>3.7 Response to Legal Inquiries.</b>', s_h2))
    story.append(para(
        'The organization maintains a written procedure for responding to '
        'subpoenas, court orders, government investigations, and media inquiries. '
        'The procedure requires: (a) immediate notification of the Executive '
        'Director and Compliance Officer; (b) notification of legal counsel '
        'within 24 hours; (c) preservation of all relevant records; (d) '
        'coordination of any response through legal counsel; (e) documentation '
        'of the inquiry and response in the compliance binder; and (f) reporting '
        'to the Governing Body at the next regular meeting (or sooner if '
        'material).'
    ))
    story.append(Paragraph('<b>3.8 Reporting Potential Violations.</b>', s_h2))
    story.append(para(
        'Any personnel member who becomes aware of a potential legal violation '
        'must report it to the Compliance Officer within 24 hours. The '
        'Compliance Officer investigates each report within 5 business days, '
        'documents findings, and reports confirmed violations to the Executive '
        'Director and Governing Body within 5 business days of confirmation. '
        'The organization does not retaliate against any personnel member for '
        'good-faith reporting of a potential violation. Personnel may also '
        'report concerns anonymously through the compliance hotline.'
    ))
    story.append(Paragraph('<b>3.9 Responsible Parties.</b>', s_h2))
    story.append(para(
        '<b>Executive Director</b> — designates the Compliance Officer; signs '
        'the annual compliance attestation. <b>Compliance Officer</b> — '
        'maintains the Legal Compliance Register; coordinates the annual review; '
        'investigates reports. <b>QP</b> — operational compliance for clinical '
        'and program requirements. <b>Governing Body</b> — reviews compliance '
        'reports; ensures corrective action. <b>Legal Counsel</b> — provides '
        'legal advice; reviews legal inquiries.'
    ))
    story.append(Paragraph('<b>3.10 Review Schedule.</b>', s_h2))
    story.append(para(
        'Monthly review of the Legal Compliance Register. Annual full '
        'legal-compliance review with counsel. Ad-hoc review triggered by '
        'regulatory change, serious incident, or legal inquiry.'
    ))
    story.extend(_approval_block('Legal Compliance Plan'))
    story.append(PageBreak())

    # ════════════════════════════════════════════════════════════════
    # PLAN 4 — FINANCIAL PLAN (§12.4)
    # ════════════════════════════════════════════════════════════════
    story.extend(_plan_header(4, 'Financial Plan', '§12.4'))
    story.append(Paragraph('<b>4.1 Purpose.</b>', s_h2))
    story.append(para(
        'The Financial Plan demonstrates conformance to CARF CYS Section 1.F by '
        'establishing written policies and procedures for financial planning, '
        'budgeting, internal controls, audit, billing, and records retention. '
        'The plan ensures the organization maintains financial sustainability '
        'sufficient to deliver quality services and meet its obligations to '
        'persons served, personnel, funders, and the community.'
    ))
    story.append(Paragraph('<b>4.2 Scope.</b>', s_h2))
    story.append(para(
        'This plan covers all financial activities of the organization, '
        'including operating budget, capital budget, cash management, resident '
        'trust funds, billing and collections, payroll, accounts payable, '
        'procurement, financial reporting, audit, and records retention. It '
        'applies to the Executive Director, QP, Billing Coordinator, and any '
        'personnel with financial responsibilities.'
    ))
    story.append(Paragraph('<b>4.3 Annual Operating Budget.</b>', s_h2))
    story.append(para(
        'The Executive Director prepares an annual operating budget covering '
        'all revenue sources (Medicaid, room-and-board, grants, charitable '
        'contributions) and all expense categories (personnel, facility, '
        'clinical, administrative). The budget is reviewed and approved by '
        'the Governing Body prior to the start of the fiscal year. Material '
        'variances (greater than 10% line-item variance) are documented with '
        'explanation and corrective action. The budget is reviewed at each '
        'quarterly Governing Body meeting.'
    ))
    story.append(Paragraph('<b>4.4 Capital-Replacement Reserve.</b>', s_h2))
    story.append(para(
        'The organization maintains a capital-replacement reserve sufficient '
        'to address expected major repairs and replacements over a rolling '
        'five-year horizon. The reserve is funded through an annual allocation '
        'in the operating budget (minimum 3% of operating revenue). The QP '
        'maintains a written five-year capital-replacement schedule listing '
        'each major asset, expected useful life, replacement cost, and target '
        'replacement year. The reserve is held in a separate bank account and '
        'is used only for capital purposes.'
    ))
    story.append(Paragraph('<b>4.5 Internal Controls.</b>', s_h2))
    story.append(para(
        'Written internal controls address: (a) segregation of duties between '
        'the person authorizing payments, the person processing payments, and '
        'the person reconciling bank statements; (b) authorization thresholds '
        'for expenditures (e.g., under $500 — QP; $500–$5,000 — Executive '
        'Director; over $5,000 — Governing Body); (c) monthly bank '
        'reconciliation by an individual not authorized to sign checks; (d) '
        'segregation of resident trust funds from operating funds in a '
        'separate bank account with monthly reconciliation and quarterly '
        'reporting to each resident and LRP; (e) dual signatures on all '
        'checks over $1,000; (f) monthly review of expense reports by the '
        'Executive Director; and (g) annual review of internal controls by '
        'the auditor.'
    ))
    story.append(Paragraph('<b>4.6 Resident Trust Funds.</b>', s_h2))
    story.append(para(
        'The organization maintains a written resident trust-fund policy '
        'addressing: (a) deposits (intake of personal funds at admission, '
        'receipt of SSI/SSDI benefits, gifts); (b) withdrawals (consistent '
        'with the youth\'s Person-Centered Plan, with LRP authorization for '
        'amounts over $50); (c) interest (any interest earned is credited to '
        'the youth\'s account); (d) quarterly accounting to the youth and '
        'LRP; (e) reconciliation at discharge with full disbursement of '
        'remaining funds; and (f) protection from unauthorized access. The '
        'QP conducts monthly audit of resident trust-fund transactions.'
    ))
    story.append(Paragraph('<b>4.7 Independent Financial Audit.</b>', s_h2))
    story.append(para(
        'The organization engages an independent certified public accountant '
        '(CPA) to conduct an annual financial audit (or reviewed financial '
        'statements for organizations below the audit threshold). The audit '
        'engagement letter is approved by the Governing Body. The auditor '
        'issues a written report including the opinion, financial statements, '
        'and any management-letter findings. The Executive Director prepares '
        'a written response to any findings, presented to the Governing Body '
        'within 60 days of receipt. The audit report is retained permanently.'
    ))
    story.append(Paragraph('<b>4.8 Billing &amp; Collections.</b>', s_h2))
    story.append(para(
        'Written billing and collections policies are maintained consistent '
        'with SOP §10.9 and Medicaid requirements. The Billing Coordinator '
        'submits claims within 5 business days of service delivery, monitors '
        'claim status weekly, follows up on denials within 10 business days, '
        'and reports monthly to the QP on claim volume, denial rate, and '
        'aging. The QP coordinates with clinical staff to ensure service '
        'documentation supports billed claims (SOP §10). Write-offs over '
        '$500 require Executive Director approval; write-offs over $5,000 '
        'require Governing Body approval.'
    ))
    story.append(Paragraph('<b>4.9 Financial Records Retention.</b>', s_h2))
    story.append(para(
        'Financial records are retained per the written records-retention '
        'schedule, which is consistent with state law, Medicaid requirements, '
        'and IRS requirements. At minimum: tax returns — permanent; audit '
        'reports — permanent; bank statements — 7 years; accounts payable '
        'and accounts receivable — 7 years; payroll records — 7 years; '
        'resident trust-fund records — 7 years after discharge. Records are '
        'stored securely with access limited to authorized personnel.'
    ))
    story.append(Paragraph('<b>4.10 Financial Reporting.</b>', s_h2))
    story.append(para(
        'The Executive Director prepares a quarterly financial report for the '
        'Governing Body including: (a) balance sheet; (b) income statement '
        '(actual vs. budget); (c) cash-flow statement; (d) days-cash-on-hand '
        'calculation; (e) accounts-receivable aging; (f) resident '
        'trust-fund balance; and (g) capital-replacement reserve balance. '
        'The report is presented at each quarterly Governing Body meeting '
        'and retained in the compliance binder.'
    ))
    story.append(Paragraph('<b>4.11 Responsible Parties.</b>', s_h2))
    story.append(para(
        '<b>Executive Director</b> — overall financial accountability; '
        'prepares budget; presents to Governing Body. <b>Governing Body</b> — '
        'approves budget; reviews quarterly financial reports; engages '
        'auditor. <b>QP</b> — coordinates billing oversight and resident '
        'trust-fund audit. <b>Billing Coordinator</b> — daily billing '
        'operations; weekly claim-status monitoring. <b>Compliance Officer</b> '
        '— ensures internal controls are followed.'
    ))
    story.append(Paragraph('<b>4.12 Review Schedule.</b>', s_h2))
    story.append(para(
        'Monthly internal financial review (Executive Director + QP). '
        'Quarterly Governing Body financial review. Annual independent audit. '
        'Annual full review of the Financial Plan itself.'
    ))
    story.extend(_approval_block('Financial Plan'))
    story.append(PageBreak())

    # ════════════════════════════════════════════════════════════════
    # PLAN 5 — ENTERPRISE RISK MANAGEMENT PLAN (§12.5)
    # ════════════════════════════════════════════════════════════════
    story.extend(_plan_header(5, 'Enterprise Risk Management Plan', '§12.5'))
    story.append(Paragraph('<b>5.1 Purpose.</b>', s_h2))
    story.append(para(
        'The Enterprise Risk Management (ERM) Plan demonstrates conformance to '
        'CARF CYS Section 1.G by establishing a written framework for '
        'identifying, assessing, mitigating, and monitoring risks across the '
        'organization. The plan includes the Enterprise Risk Register, '
        'business-continuity plan, and the procedures for integrating risk '
        'management into governance, operations, and incident response.'
    ))
    story.append(Paragraph('<b>5.2 Scope.</b>', s_h2))
    story.append(para(
        'This plan covers all categories of risk facing the organization, '
        'including clinical, operational, financial, legal/compliance, '
        'reputational, and external risks. It applies to the Governing Body, '
        'Executive Director, Compliance Officer, QP, and all personnel with '
        'risk-management responsibilities.'
    ))
    story.append(Paragraph('<b>5.3 Risk-Management Governance.</b>', s_h2))
    story.append(para(
        'The Compliance Officer serves as the risk-management lead, reporting '
        'directly to the Executive Director with access to the Governing Body '
        'as needed. The Compliance Officer: (a) maintains the Enterprise Risk '
        'Register; (b) coordinates the annual risk-management review; '
        '(c) reviews serious incidents within one business day; (d) trends '
        'incidents monthly; (e) presents risk-management reports to the '
        'Governing Body at each quarterly meeting; and (f) coordinates the '
        'business-continuity plan and annual drill.'
    ))
    story.append(Paragraph('<b>5.4 Enterprise Risk Register.</b>', s_h2))
    story.append(para(
        'The Enterprise Risk Register identifies at minimum the following '
        'risk categories, with each risk scored on likelihood (1–5) and '
        'impact (1–5), and assigned a mitigation action, responsible '
        'position, and review date:'
    ))
    # Risk register table
    rr_header = ['Risk Category', 'Specific Risk', 'Likelihood (1-5)', 'Impact (1-5)', 'Mitigation Action', 'Owner', 'Review Date']
    rr_rows = [
        ['Clinical', 'Suicide attempt / self-harm', '3', '5', 'Columbia suicide-risk screening at admission & weekly; safety plan; line-of-sight supervision as needed; staff training', 'Clinical Director', 'Quarterly'],
        ['Clinical', 'Elopement from facility', '2', '5', 'Hardware-secure Level III RTF physical plant with controlled-egress doors (key-card / staff-controlled); alarmed perimeter; awake overnight line-of-sight supervision; elopement risk assessment at admission & weekly; community-search protocol; police notification within 30 min', 'QP', 'Quarterly'],
        ['Clinical', 'Restraint-related injury', '2', '5', 'De-escalation training; restraint-avoidance policy; post-incident debriefing (Form 3); quarterly restraint review', 'Clinical Director', 'Quarterly'],
        ['Clinical', 'Medication error', '3', '4', 'Med-pass training; 6-month regimen review (Form 11); med-error reporting; double-check for high-alert meds', 'RN / QP', 'Monthly'],
        ['Operational', 'Staffing shortage', '4', '4', 'Recruitment plan; PRN pool; agency contract backup; sign-on incentive; retention bonuses', 'Executive Director', 'Monthly'],
        ['Operational', 'Capacity under-utilization', '3', '3', 'Referral-source relationships; LME/MCO engagement; marketing; admission-decision responsiveness', 'Executive Director', 'Monthly'],
        ['Operational', 'IT system failure (EHR)', '2', '4', 'Daily off-site backup; paper-fallback procedures (SOP §10.7); 72-hour transcription SLA; vendor support contract', 'QP', 'Quarterly'],
        ['Financial', 'Medicaid audit finding', '2', '5', 'Monthly service-note audit (Form 8); quarterly QP review; annual external documentation audit; staff training', 'QP', 'Quarterly'],
        ['Financial', 'Payer-mix concentration', '3', '3', 'Diversification strategy; grant-seeking; charitable fundraising; cost-rate analysis', 'Executive Director', 'Annual'],
        ['Financial', 'Cash-flow shortfall', '2', '5', '60-day cash reserve; line of credit; monthly cash-flow projection; accelerated billing', 'Executive Director', 'Monthly'],
        ['Legal/Compliance', 'Privacy breach (PHI)', '2', '5', 'HIPAA training; access controls; encryption; breach-response plan; annual risk assessment', 'Compliance Officer', 'Quarterly'],
        ['Legal/Compliance', 'Licensing deficiency', '2', '5', 'Mock survey annually; continuous compliance monitoring; corrective-action tracking', 'Compliance Officer', 'Annual'],
        ['Legal/Compliance', 'Employment claim', '2', '4', 'Personnel policies; EPLI insurance; documentation; supervisory training', 'Executive Director', 'Annual'],
        ['Reputational', 'Adverse media / community concern', '2', '4', 'Crisis-communication plan; community engagement; transparent incident reporting', 'Executive Director', 'Annual'],
        ['External', 'Natural disaster (tornado/hurricane)', '2', '5', 'Emergency Operations Plan (Protocol 19); drill per shift quarterly; supply cache; evacuation plan', 'QP', 'Quarterly'],
        ['External', 'Public-health emergency (pandemic)', '2', '5', 'Infection-control plan (Protocol 18); PPE supply; telehealth capability; visitor screening', 'RN / QP', 'Quarterly'],
    ]
    story.append(std_table(rr_header, rr_rows,
                           col_widths=[0.10*AVAIL_W, 0.16*AVAIL_W, 0.07*AVAIL_W, 0.07*AVAIL_W,
                                       0.30*AVAIL_W, 0.14*AVAIL_W, 0.10*AVAIL_W],
                           header_align='left', first_col_left=True, small=True))
    story.append(Spacer(1, 6))
    story.append(Paragraph('<b>5.5 Business-Continuity Plan.</b>', s_h2))
    story.append(para(
        'The organization maintains a written business-continuity plan '
        'coordinated with SOP §9 Emergency Operations Plan and Protocol 19. '
        'The plan addresses: (a) critical functions to be maintained during '
        'a disruption (resident care, medication administration, clinical '
        'services, billing); (b) alternate facility arrangements in the event '
        'the primary facility is uninhabitable; (c) communication procedures '
        'with personnel, families/LRPs, LME/MCO, and licensing authority; '
        '(d) IT system recovery procedures (daily off-site backup, vendor '
        'recovery SLA, paper-fallback); (e) essential-vendor list (pharmacy, '
        'medical, food, fuel); and (f) annual continuity-plan drill with '
        'after-action review.'
    ))
    story.append(Paragraph('<b>5.6 Incident-Review Integration.</b>', s_h2))
    story.append(para(
        'The Compliance Officer reviews every serious incident report (per '
        'SOP §8 IRIS) within one business day of submission. The review '
        'identifies any new risks not yet on the Enterprise Risk Register, '
        'updates likelihood/impact scores for existing risks as warranted, '
        'and ensures corrective actions are tracked to completion. Serious '
        'incidents are trended monthly by type, location, shift, and '
        'personnel. Trends are presented to the Health &amp; Safety Committee '
        '(Plan 6) and to the Governing Body quarterly.'
    ))
    story.append(Paragraph('<b>5.7 Annual Risk-Management Review.</b>', s_h2))
    story.append(para(
        'The Compliance Officer coordinates an annual risk-management review '
        'presented to the Governing Body. The review includes: (a) summary '
        'of all risks on the Enterprise Risk Register with current scoring '
        'and mitigation status; (b) analysis of incident trends; (c) review '
        'of any near-misses; (d) evaluation of mitigation-action '
        'effectiveness; (e) identification of emerging risks; (f) revision '
        'of the Register as needed; and (g) recommendations for the coming '
        'year. The annual review is documented in writing and retained in '
        'the compliance binder.'
    ))
    story.append(Paragraph('<b>5.8 Responsible Parties.</b>', s_h2))
    story.append(para(
        '<b>Compliance Officer</b> — risk-management lead; maintains Register; '
        'coordinates annual review. <b>Executive Director</b> — overall '
        'accountability; allocates resources to mitigation. <b>Governing Body</b> '
        '— reviews Register at each quarterly meeting; directs major '
        'mitigation actions. <b>QP</b> — operational risk management for '
        'clinical/program risks. <b>RN</b> — clinical/medication risks.'
    ))
    story.append(Paragraph('<b>5.9 Review Schedule.</b>', s_h2))
    story.append(para(
        'Quarterly review of the Enterprise Risk Register by the Governing '
        'Body. Annual full risk-management review. Ad-hoc review following '
        'any serious incident, near-miss, or significant organizational '
        'change.'
    ))
    story.extend(_approval_block('Enterprise Risk Management Plan'))
    story.append(PageBreak())

    # ════════════════════════════════════════════════════════════════
    # PLAN 6 — HEALTH & SAFETY COMMITTEE CHARTER (§12.6)
    # ════════════════════════════════════════════════════════════════
    story.extend(_plan_header(6, 'Health & Safety Committee Charter', '§12.6'))
    story.append(Paragraph('<b>6.1 Purpose.</b>', s_h2))
    story.append(para(
        'The Health &amp; Safety Committee Charter demonstrates conformance to '
        'CARF CYS Section 1.H by establishing a standing committee responsible '
        'for ongoing oversight of health, safety, and environmental conditions '
        'in the facility. The committee reviews inspections, drills, incidents, '
        'infection-control surveillance, medication errors, and work-related '
        'injuries, and recommends corrective action to the Executive Director '
        'and Governing Body.'
    ))
    story.append(Paragraph('<b>6.2 Scope.</b>', s_h2))
    story.append(para(
        'The committee\'s scope covers all health and safety matters within '
        'the facility and during organization-sponsored activities off-site. '
        'This includes physical-plant safety, environmental health, '
        'infection control, emergency preparedness, drill scheduling and '
        'evaluation, incident review, medication-error review, '
        'workplace-violence prevention, and personnel safety training.'
    ))
    story.append(Paragraph('<b>6.3 Committee Composition.</b>', s_h2))
    story.append(para(
        'The standing members of the Health &amp; Safety Committee are: '
        '(a) <b>QP</b> (chair, voting); (b) <b>House Manager</b> (voting); '
        '(c) <b>Direct Care Professional representative</b> (rotating among '
        'day/evening/overnight shifts, voting); (d) <b>RN or designee</b> '
        '(voting); (e) <b>Compliance Officer</b> (non-voting, advisory); '
        'and (f) <b>Executive Director</b> (ex officio, non-voting). The '
        'committee may invite additional subject-matter experts (facilities '
        'manager, IT coordinator, etc.) as needed. Membership is reviewed '
        'annually.'
    ))
    story.append(Paragraph('<b>6.4 Meeting Frequency &amp; Quorum.</b>', s_h2))
    story.append(para(
        'The committee meets at least monthly, on the second Tuesday of '
        'each month at 1:00 PM. Special meetings may be called by the chair '
        'or any two voting members with at least 48 hours\' notice. Quorum '
        'is a majority of voting members (3 of 4). Decisions are made by '
        'consensus where possible; otherwise by majority vote of voting '
        'members present. The chair does not vote except to break a tie.'
    ))
    story.append(Paragraph('<b>6.5 Standing Agenda.</b>', s_h2))
    story.append(para('Each monthly meeting follows a standing agenda:'))
    story.extend(bullets([
        'Review and approval of prior meeting minutes',
        'Monthly environmental safety inspection results (Form 5)',
        'Fire, tornado, and lockdown drills per shift (§9.2)',
        'Incident reports trended by type, location, shift, and personnel (§8)',
        'Infection-control surveillance (§6.1, Protocol 18)',
        'Medication-error trends (§6.3)',
        'Work-related injury trends',
        'Equipment and physical-plant work orders',
        'Safety-plan revisions',
        'Emergency-preparedness plan revisions',
        'Old business / action-item follow-up',
        'New business',
    ]))
    story.append(Paragraph('<b>6.6 Minutes &amp; Documentation.</b>', s_h2))
    story.append(para(
        'The committee maintains written minutes documenting attendance, '
        'topics reviewed, decisions made, and action items with responsible '
        'parties and due dates. Minutes are distributed to all committee '
        'members within 5 business days of the meeting, retained permanently '
        'in the compliance binder, and made available to CARF surveyors on '
        'request. Action items are tracked to completion at each subsequent '
        'meeting.'
    ))
    story.append(Paragraph('<b>6.7 Reporting.</b>', s_h2))
    story.append(para(
        'The QP (as chair) reports committee activities and trends to the '
        'Clinical Director at each quarterly compliance report (per SOP '
        '§1.4(a)) and to the Governing Body at each quarterly meeting. The '
        'report includes: (a) summary of inspections and drills; (b) '
        'incident trends; (c) infection-control surveillance; (d) '
        'medication-error trends; (e) work-related injury trends; (f) '
        'action-item status; and (g) recommendations for resource allocation '
        'or policy revision.'
    ))
    story.append(Paragraph('<b>6.8 Written Health &amp; Safety Policies.</b>', s_h2))
    story.append(para(
        'Written health-and-safety policies are maintained in the facility '
        'policy library, addressing at minimum:'
    ))
    story.extend(bullets([
        'Emergency response (fire, tornado, lockdown, evacuation, medical emergency)',
        'Infection control (hand hygiene, PPE, isolation, cleaning/disinfection, surveillance)',
        'Hazard communication (chemical inventory, SDS, labeling, training)',
        'Bloodborne pathogens (exposure control plan, Hepatitis B vaccination, post-exposure)',
        'Workplace violence prevention (warning signs, reporting, response)',
        'Hot work / environmental safety (facility-specific hazards)',
        'Food safety (kitchen sanitation, temperature monitoring, allergen control)',
        'Pool/water safety (if applicable)',
        'Vehicle and transport safety (if applicable)',
    ]))
    story.append(para(
        'Each policy is reviewed at least annually by the committee, with '
        'revision as needed to reflect changes in regulation, facility, or '
        'practice. Personnel are trained on each applicable policy at '
        'orientation and annually thereafter.'
    ))
    story.append(Paragraph('<b>6.9 Responsible Parties.</b>', s_h2))
    story.append(para(
        '<b>QP (chair)</b> — convenes meetings; sets agenda; tracks action '
        'items; reports to Governing Body. <b>House Manager</b> — '
        'physical-plant inspections; work-order coordination. <b>DCP '
        'representative</b> — frontline perspective; identifies operational '
        'safety concerns. <b>RN</b> — infection control; medication safety. '
        '<b>Compliance Officer</b> — regulatory alignment; risk integration. '
        '<b>Executive Director</b> — resource allocation; policy approval.'
    ))
    story.append(Paragraph('<b>6.10 Review Schedule.</b>', s_h2))
    story.append(para(
        'Monthly committee meetings. Annual review of the Charter itself, '
        'including membership, scope, and effectiveness. Ad-hoc meetings '
        'following any serious incident, environmental emergency, or '
        'regulatory inspection.'
    ))
    story.extend(_approval_block('Health & Safety Committee Charter'))
    story.append(PageBreak())

    # ════════════════════════════════════════════════════════════════
    # PLAN 7 — WORKFORCE DEVELOPMENT PLAN (§12.7)
    # ════════════════════════════════════════════════════════════════
    story.extend(_plan_header(7, 'Workforce Development Plan', '§12.7'))
    story.append(Paragraph('<b>7.1 Purpose.</b>', s_h2))
    story.append(para(
        'The Workforce Development Plan demonstrates conformance to CARF CYS '
        'Section 1.I by establishing written policies for recruiting, hiring, '
        'orienting, training, supervising, evaluating, and retaining '
        'personnel. The plan ensures the organization has a qualified, '
        'competent, and engaged workforce sufficient to deliver quality '
        'services to the persons served.'
    ))
    story.append(Paragraph('<b>7.2 Scope.</b>', s_h2))
    story.append(para(
        'This plan covers all personnel of the organization, including '
        'full-time, part-time, PRN, and temporary personnel; contractors '
        'with direct contact with persons served; and volunteers and interns. '
        'It addresses recruiting, hiring, orientation, annual training, '
        'position descriptions, performance evaluation, supervision, '
        'personnel records, succession, and engagement.'
    ))
    story.append(Paragraph('<b>7.3 Recruiting &amp; Hiring.</b>', s_h2))
    story.append(para(
        'The organization maintains a written recruiting and hiring policy '
        '(SOP §2.2) addressing: (a) position descriptions for every role, '
        'consistent with SOP §2; (b) posting and recruitment strategy '
        '(online job boards, professional associations, referral incentives, '
        'partnerships with local colleges); (c) application review and '
        'interview procedures, including structured interview questions '
        'aligned with position competencies; (d) background-check '
        'requirements per SOP §2.3 (criminal, abuse/neglect registry, '
        'sex-offender registry, education verification, license verification, '
        'reference checks); (e) credential verification per SOP §1.4(b) and '
        '§2.2; (f) offer of employment contingent on satisfactory background '
        'and credential verification; and (g) written acknowledgment of '
        'personnel policies (Form 6 — Employee SOP Acknowledgment).'
    ))
    story.append(Paragraph('<b>7.4 Orientation Curriculum.</b>', s_h2))
    story.append(para(
        'Every new personnel member completes a written orientation '
        'curriculum prior to working independently with persons served. '
        'The orientation curriculum covers at minimum:'
    ))
    story.extend(bullets([
        'Mission, vision, and values of the organization',
        'Person-centered and trauma-informed care principles',
        'Person-Centered Plan process (SOP §4.1)',
        'Behavioral support and restraint policies (SOP §5)',
        'Medication administration policies (SOP §6.3) — for personnel '
        'who administer medications',
        'Infection control (SOP §6.1, Protocol 18)',
        'Incident reporting (SOP §8 — IRIS)',
        'Privacy and confidentiality (SOP §11 — HIPAA, 42 CFR Part 2)',
        'Cultural and linguistic competency',
        'Mandated reporting of suspected child abuse/neglect',
        'Emergency procedures (fire, tornado, lockdown, evacuation)',
        'Documentation requirements (SOP §10)',
        'Resident rights (Plan 8)',
        'Personnel code of conduct',
        'Workplace violence prevention',
        'Bloodborne pathogens / exposure control',
        'Vehicle and transport safety (if applicable)',
    ]))
    story.append(para(
        'Orientation is conducted by the QP or designee and is documented '
        'in the personnel file. A new-hire may not work independently with '
        'persons served until orientation is complete and the QP has '
        'verified competency.'
    ))
    story.append(Paragraph('<b>7.5 Annual Training Plan.</b>', s_h2))
    story.append(para(
        'The QP maintains a written annual training plan covering refresher '
        'training and competency verification for all personnel. The plan '
        'identifies required training topics, frequency (annual, biennial, '
        'or as needed), target completion dates, trainers, and documentation '
        'method. Required annual training includes at minimum: '
        'trauma-informed care refresher; CPR/First Aid (biennial); '
        'bloodborne pathogens; HIPAA refresher; mandated reporter refresher; '
        'crisis prevention/intervention (CPI or equivalent) refresher; '
        'medication administration refresher (for med-pass personnel); and '
        'any topic identified through incident trends, performance '
        'evaluation, or regulatory change. The QP tracks training completion '
        'in the master training calendar and individual personnel files.'
    ))
    story.append(Paragraph('<b>7.6 Position Descriptions.</b>', s_h2))
    story.append(para(
        'Written position descriptions are maintained for every role in the '
        'organization, including: Executive Director, Clinical Director, QP, '
        'Associated Professional (AP), Direct Care Professional (DCP), House '
        'Manager, Registered Nurse (RN), Billing Coordinator, Cook/Household '
        'Manager, and any other role. Each position description includes: '
        '(a) position title; (b) reports-to; (c) summary of responsibilities; '
        '(d) essential duties; (e) minimum qualifications (education, '
        'experience, credentials); (f) physical requirements; (g) working '
        'conditions; and (h) acknowledgment signature. Position descriptions '
        'are reviewed annually and updated to reflect changes in scope.'
    ))
    story.append(Paragraph('<b>7.7 Performance Evaluation.</b>', s_h2))
    story.append(para(
        'Written performance-evaluation policy requires annual performance '
        'evaluation for every personnel member, conducted by the supervisor. '
        'The evaluation includes: (a) review of position description and '
        'essential duties; (b) competency assessment against position-specific '
        'criteria; (c) review of training completion; (d) review of any '
        'incidents or complaints; (e) self-assessment by the personnel '
        'member; (f) supervisor feedback; (g) goals for the coming year; '
        'and (h) signatures. New personnel receive a 90-day and 180-day '
        'evaluation in addition to the annual cycle. Evaluations are '
        'documented in the personnel file.'
    ))
    story.append(Paragraph('<b>7.8 Supervision.</b>', s_h2))
    story.append(para(
        'Written supervision policy consistent with SOP §2.2(a) '
        'Individualized Supervision Plans. Each AP and DCP has a written '
        'individualized supervision plan specifying the frequency and format '
        'of supervision (individual, group, on-the-job observation), the '
        'supervisor, and the documentation method. The QP supervises clinical '
        'staff per the Clinical Director\'s direction. The House Manager '
        'supervises DCPs on shift. Supervision is documented in the '
        'personnel file with date, topics discussed, and any action items.'
    ))
    story.append(Paragraph('<b>7.9 Personnel Records.</b>', s_h2))
    story.append(para(
        'Written personnel-records policy consistent with SOP §2.4. The QP '
        'maintains personnel files in a locked cabinet (or secured EHR) '
        'with access limited to the personnel member, the supervisor, the '
        'QP, the Executive Director, and authorized auditors. Files include '
        'at minimum: application, resume, position description acknowledgment, '
        'background-check results, credential verification, orientation '
        'documentation, training records, performance evaluations, '
        'supervision notes, and any disciplinary actions. Personnel files '
        'are retained for 7 years after separation.'
    ))
    story.append(Paragraph('<b>7.10 Volunteer &amp; Intern Management.</b>', s_h2))
    story.append(para(
        'Written volunteer and intern management policy per SOP §1.8. '
        'Volunteers and interns with direct contact with persons served '
        'complete a modified orientation, background check, and supervision '
        'plan. Volunteers and interns do not administer medications, conduct '
        'clinical interventions, or work unsupervised with persons served. '
        'A volunteer/intern coordinator (may be the QP) maintains records '
        'and schedules.'
    ))
    story.append(Paragraph('<b>7.11 Continuing Education Support.</b>', s_h2))
    story.append(para(
        'The organization supports continuing education for personnel '
        'through: (a) paid time off for required licensure continuing '
        'education; (b) tuition reimbursement for job-related coursework '
        '(up to $2,000 per personnel member per year, subject to budget '
        'approval); (c) in-service training sessions; (d) access to online '
        'training platforms; and (e) conference attendance (with Executive '
        'Director approval). Continuing-education completion is documented '
        'in the personnel file.'
    ))
    story.append(Paragraph('<b>7.12 Succession Planning.</b>', s_h2))
    story.append(para(
        'Written succession plan for the Executive Director, Clinical '
        'Director, and QP positions is maintained as part of the Strategic '
        'Plan (Plan 1, Section 1.8). For each role, the plan identifies '
        'core competencies, internal candidates, external recruitment '
        'strategy, interim coverage procedures, and knowledge-transfer '
        'requirements. The succession plan is reviewed annually and '
        'following any key leadership change.'
    ))
    story.append(Paragraph('<b>7.13 Workforce Engagement &amp; Recognition.</b>', s_h2))
    story.append(para(
        'The organization maintains a written workforce engagement and '
        'recognition plan including: (a) annual personnel engagement survey '
        '(per Plan 2); (b) monthly personnel meetings with structured '
        'agenda; (c) peer-recognition program; (d) employee-of-the-quarter '
        'award; (e) annual personnel appreciation event; (f) wellness '
        'initiatives; and (g) exit interviews to identify retention '
        'opportunities. Engagement data is incorporated into the Workforce '
        'Development Plan annual revision.'
    ))
    story.append(Paragraph('<b>7.14 Responsible Parties.</b>', s_h2))
    story.append(para(
        '<b>QP</b> — overall coordination of workforce development; '
        'orientation curriculum; annual training plan; personnel records; '
        'supervision of clinical staff. <b>Executive Director</b> — '
        'recruiting strategy; succession planning; resource allocation. '
        '<b>House Manager</b> — DCP supervision; scheduling. <b>Clinical '
        'Director</b> — clinical supervision direction; clinical competency '
        'verification. <b>Governing Body</b> — reviews workforce data; '
        'approves compensation structure.'
    ))
    story.append(Paragraph('<b>7.15 Review Schedule.</b>', s_h2))
    story.append(para(
        'Monthly review of training completion and turnover data. Quarterly '
        'review by the Governing Body. Annual full review of the Workforce '
        'Development Plan, incorporating engagement survey results and '
        'turnover analysis.'
    ))
    story.extend(_approval_block('Workforce Development Plan'))
    story.append(PageBreak())

    # ════════════════════════════════════════════════════════════════
    # PLAN 8 — RESIDENT RIGHTS POLICY COMPILATION (§12.8)
    # ════════════════════════════════════════════════════════════════
    story.extend(_plan_header(8, 'Resident Rights Policy Compilation', '§12.8'))
    story.append(Paragraph('<b>8.1 Purpose.</b>', s_h2))
    story.append(para(
        'The Resident Rights Policy Compilation demonstrates conformance to '
        'CARF CYS Section 1.J by consolidating the organization\'s written '
        'policies on the rights of persons served into a single reference '
        'document. The policies are also published in the Resident Handbook '
        '(companion document) and in SOP §§3, 5, 6, 8, 9, and 11; this '
        'compilation serves as the comprehensive reference for personnel, '
        'persons served, families/LRPs, and CARF surveyors.'
    ))
    story.append(Paragraph('<b>8.2 Scope.</b>', s_h2))
    story.append(para(
        'This compilation covers all rights of persons served, including '
        'dignity, participation in services, confidentiality, access to '
        'records, grievance procedures, freedom from unnecessary restraint '
        'and seclusion, informed consent, religious freedom, personal-funds '
        'management, and advance notification of discharge. It applies to '
        'all personnel and to all youth served by the organization.'
    ))
    story.append(Paragraph('<b>8.3 Statement of Rights.</b>', s_h2))
    story.append(para(
        'Every youth served by Well Spring Intervention LLC has the right to:'
    ))
    story.extend(bullets([
        '<b>Dignity and respect.</b> Be treated with dignity, respect, and '
        'humane care at all times, free from discrimination on the basis of '
        'race, color, national origin, religion, sex, gender identity or '
        'expression, sexual orientation, age, disability, or any other '
        'protected classification.',
        '<b>Privacy.</b> Reasonable privacy in personal care, '
        'communications, visitation, and personal space; privacy of '
        'personal mail and telephone communications (consistent with safety '
        'and the Person-Centered Plan).',
        '<b>Participation in service planning.</b> Participate in the '
        'development and review of the Person-Centered Plan (SOP §4.1); '
        'receive a copy of the plan; and refuse services (with documented '
        'consequences of refusal).',
        '<b>Confidential communication and visitation.</b> Receive and send '
        'mail; receive visitors (subject to safety and the Person-Centered '
        'Plan); and communicate with family, attorneys, advocates, and '
        'clergy.',
        '<b>Access to records.</b> Access one\'s own service record per '
        'SOP §11.5; receive a copy upon request; and appeal any restriction '
        'of access.',
        '<b>File a grievance.</b> File a grievance without retaliation; '
        'receive a written acknowledgment within 2 business days; receive '
        'a written response within 30 calendar days; and appeal to the '
        'Executive Director and external advocacy resources.',
        '<b>Freedom from unnecessary restraint and seclusion.</b> Be free '
        'from restraint and seclusion except as a last-resort safety '
        'intervention per SOP §5; receive post-incident debriefing (Form 3); '
        'and have restraint use reviewed by the QP and Clinical Director.',
        '<b>Informed consent.</b> Give informed consent (or have the LRP '
        'give consent) for treatment and medication, with explanation of '
        'benefits, risks, alternatives, and the right to refuse.',
        '<b>Religious freedom.</b> Exercise religious freedom; receive '
        'reasonable accommodation for religious practices; and not have any '
        'religious belief imposed.',
        '<b>Personal funds management.</b> Have personal funds managed '
        'per SOP §1.8 and Plan 4; receive quarterly accounting; and '
        'receive full disbursement at discharge.',
        '<b>Advance notification of discharge.</b> Receive advance written '
        'notification of any discharge or transfer per SOP §3.4(a); '
        'participate in transition planning per SOP §3.4 and §3.6; and '
        'appeal an involuntary discharge.',
    ]))
    story.append(Paragraph('<b>8.4 Grievance Procedure.</b>', s_h2))
    story.append(para(
        'The organization maintains a written grievance procedure. Any '
        'youth, family member, LRP, or other stakeholder may file a '
        'grievance orally or in writing with any personnel member. The '
        'personnel member receiving the grievance documents it on the '
        'grievance log and forwards it to the QP within 24 hours. The QP '
        '(or designee) acknowledges the grievance in writing within 2 '
        'business days, investigates, and provides a written response '
        'within 30 calendar days. If the grievant is not satisfied with '
        'the response, they may appeal to the Executive Director within '
        '10 business days; the Executive Director issues a written decision '
        'within 15 business days. The grievant is also informed of external '
        'advocacy resources, including the LME/MCO, the state licensing '
        'authority, Disability Rights NC, and the CARF complaint process. '
        'The QP maintains the grievance log, trends grievances quarterly, '
        'and reports to the Governing Body.'
    ))
    story.append(Paragraph('<b>8.5 Personnel Training.</b>', s_h2))
    story.append(para(
        'All personnel are trained on resident rights at orientation and '
        'annually thereafter. Training covers: (a) the statement of rights; '
        '(b) the grievance procedure; (c) the non-retaliation policy; '
        '(d) informed consent; (e) freedom from restraint and seclusion; '
        '(f) confidentiality; and (g) reporting rights violations. Training '
        'completion is documented in the personnel file.'
    ))
    story.append(Paragraph('<b>8.6 Audit &amp; Trend Reporting.</b>', s_h2))
    story.append(para(
        'The QP audits the grievance log, restraint log, and rights-related '
        'incident reports quarterly. Findings are trended and reported to '
        'the Clinical Director, Executive Director, and Governing Body. '
        'Trends inform personnel training, supervision, and policy revision. '
        'Serious or repeated rights violations are reported to the state '
        'licensing authority per regulatory requirements.'
    ))
    story.append(Paragraph('<b>8.7 Responsible Parties.</b>', s_h2))
    story.append(para(
        '<b>QP</b> — overall management of resident rights; grievance '
        'investigation; quarterly audit. <b>Clinical Director</b> — '
        'clinical-care rights; restraint review. <b>All Personnel</b> — '
        'respect resident rights; report violations; do not retaliate. '
        '<b>Governing Body</b> — reviews trends; ensures corrective action.'
    ))
    story.append(Paragraph('<b>8.8 Review Schedule.</b>', s_h2))
    story.append(para(
        'Quarterly audit of grievance log, restraint log, and rights-related '
        'incidents. Annual review of the Resident Rights Policy Compilation '
        'itself. Ad-hoc review following any serious rights violation or '
        'regulatory change.'
    ))
    story.extend(_approval_block('Resident Rights Policy Compilation'))
    story.append(PageBreak())

    # ════════════════════════════════════════════════════════════════
    # PLAN 9 — ACCESSIBILITY & NONDISCRIMINATION PLAN (§12.9)
    # ════════════════════════════════════════════════════════════════
    story.extend(_plan_header(9, 'Accessibility & Nondiscrimination Plan', '§12.9'))
    story.append(Paragraph('<b>9.1 Purpose.</b>', s_h2))
    story.append(para(
        'The Accessibility &amp; Nondiscrimination Plan demonstrates '
        'conformance to CARF CYS Section 1.K by establishing written '
        'policies ensuring that persons served, family members, personnel, '
        'and visitors are not subjected to discrimination and that the '
        'program is accessible to persons with disabilities and persons '
        'with limited English proficiency.'
    ))
    story.append(Paragraph('<b>9.2 Scope.</b>', s_h2))
    story.append(para(
        'This plan covers all aspects of the organization\'s operations, '
        'including admission, service delivery, employment, facility '
        'accessibility, communication, and grievance procedures. It applies '
        'to all personnel and to all persons seeking or receiving services.'
    ))
    story.append(Paragraph('<b>9.3 Nondiscrimination Policy.</b>', s_h2))
    story.append(para(
        'The organization does not discriminate on the basis of race, color, '
        'national origin, religion, sex, gender identity or expression, '
        'sexual orientation, age, disability, veteran status, or any other '
        'classification protected by applicable federal, state, or local '
        'law. This policy applies to admission, treatment, employment, '
        'and all other organizational activities. The policy is published '
        'in the Resident Handbook, the personnel handbook, on the '
        'organization\'s website, and posted in the facility. The '
        'Compliance Officer is designated as the Section 504 Coordinator '
        'and the Civil Rights Coordinator.'
    ))
    story.append(Paragraph('<b>9.4 Language Access Plan.</b>', s_h2))
    story.append(para(
        'The organization maintains a written language access plan '
        'providing for: (a) qualified interpreter services at no cost to '
        'the youth and family, available within 60 minutes for spoken '
        'languages and within 4 hours for sign language; (b) translation '
        'of vital documents (intake forms, consent forms, Resident '
        'Handbook, discharge summary, grievance procedure) into the '
        'languages commonly encountered in the service area (at minimum '
        'Spanish); (c) primary-language preference documented in the '
        'clinical record; (d) language-assistance need identified at '
        'intake; (e) use of qualified interpreters rather than family '
        'members or untrained personnel, except in emergencies; (f) '
        'tracking of language-assistance utilization for resource planning; '
        'and (g) annual review of language-access needs based on census '
        'data.'
    ))
    story.append(Paragraph('<b>9.5 Reasonable Accommodation Policy.</b>', s_h2))
    story.append(para(
        'The organization provides reasonable accommodation to youth, '
        'family members, personnel, and visitors with disabilities, '
        'consistent with the ADA and Section 504. Accommodations may '
        'include: (a) physical accessibility modifications (ramps, '
        'grab bars, accessible bathrooms); (b) communication '
        'accommodations (large-print materials, screen readers, captioning, '
        'auxiliary aids); (c) programmatic accommodations (modified '
        'schedules, modified activities, assistive technology); and '
        '(d) dietary accommodations (medical-diagnosis-driven). Requests '
        'for accommodation are made to the QP or Compliance Officer, '
        'documented in writing, evaluated within 5 business days, and '
        'implemented within 15 business days (or sooner if urgently '
        'needed). Denials are documented with rationale and appeal rights.'
    ))
    story.append(Paragraph('<b>9.6 Physical Accessibility.</b>', s_h2))
    story.append(para(
        'The organization conducts a written accessibility review of the '
        'physical facility at least annually, using the ADA Checklist for '
        'Existing Facilities. The review identifies barriers and corrective '
        'actions, with priority given to barriers affecting program access. '
        'The review is documented and maintained in the compliance binder. '
        'Any new construction or alteration complies with the ADA Standards '
        'for Accessible Design. The QP maintains an accessibility-barrier '
        'removal plan with target dates and budget.'
    ))
    story.append(Paragraph('<b>9.7 Nondiscrimination Grievance Procedure.</b>', s_h2))
    story.append(para(
        'The organization maintains a written grievance procedure for '
        'nondiscrimination complaints, distinct from but coordinated with '
        'the resident grievance procedure in Plan 8. The procedure '
        'includes: (a) submission of the complaint to the Compliance '
        'Officer (Section 504 Coordinator); (b) written acknowledgment '
        'within 5 business days; (c) investigation within 30 calendar '
        'days; (d) written decision with rationale; (e) appeal to the '
        'Executive Director within 10 business days; (f) Executive '
        'Director decision within 15 business days; and (g) notice of '
        'external appeal rights (OCR, EEOC, state human relations '
        'commission). The procedure is published in the Resident Handbook '
        'and the personnel handbook.'
    ))
    story.append(Paragraph('<b>9.8 Personnel Training.</b>', s_h2))
    story.append(para(
        'All personnel are trained on nondiscrimination, language access, '
        'and reasonable accommodation at orientation and annually '
        'thereafter. Training covers: (a) the nondiscrimination policy; '
        '(b) language-access procedures; (c) reasonable-accommodation '
        'procedures; (d) cultural and linguistic competency; '
        '(e) the grievance procedure; and (f) the role of the Section 504 '
        'Coordinator. Training completion is documented in the personnel '
        'file.'
    ))
    story.append(Paragraph('<b>9.9 Responsible Parties.</b>', s_h2))
    story.append(para(
        '<b>Compliance Officer</b> — Section 504 Coordinator; Civil Rights '
        'Coordinator; investigates grievances. <b>QP</b> — operational '
        'implementation; intake screening; accommodation evaluation. '
        '<b>Executive Director</b> — resource allocation; appeals. '
        '<b>Governing Body</b> — reviews accessibility data; ensures '
        'barrier-removal funding.'
    ))
    story.append(Paragraph('<b>9.10 Review Schedule.</b>', s_h2))
    story.append(para(
        'Annual review of the Accessibility &amp; Nondiscrimination Plan, '
        'including the physical accessibility review, language-access '
        'utilization, and grievance trends. Ad-hoc review following any '
        'regulatory change, demographic shift, or grievance.'
    ))
    story.extend(_approval_block('Accessibility & Nondiscrimination Plan'))
    story.append(PageBreak())

    # ════════════════════════════════════════════════════════════════
    # PLAN 10 — PERFORMANCE MEASUREMENT PLAN (§12.10)
    # ════════════════════════════════════════════════════════════════
    story.extend(_plan_header(10, 'Performance Measurement Plan', '§12.10'))
    story.append(Paragraph('<b>10.1 Purpose.</b>', s_h2))
    story.append(para(
        'The Performance Measurement Plan demonstrates conformance to CARF '
        'CYS Section 1.L by establishing the organization\'s performance '
        'indicators, data-collection methods, analysis cadence, and '
        'reporting structure. The plan ensures the organization collects, '
        'analyzes, and acts on data to improve services and outcomes for '
        'persons served.'
    ))
    story.append(Paragraph('<b>10.2 Scope.</b>', s_h2))
    story.append(para(
        'This plan covers all performance indicators tracked by the '
        'organization, organized into seven domains: access; '
        'person-centered planning; clinical outcomes; safety; personnel; '
        'financial; and person-served experience. It applies to the QP '
        '(data aggregation), all personnel (data collection), the '
        'Executive Director (resource allocation), and the Governing Body '
        '(review and oversight).'
    ))
    story.append(Paragraph('<b>10.3 Performance Indicators.</b>', s_h2))
    story.append(para(
        'The organization tracks the following performance indicators, '
        'with target values and reporting frequency:'
    ))
    pm_header = ['Domain', 'Indicator', 'Target', 'Frequency', 'Data Source', 'Owner']
    pm_rows = [
        ['Access', 'Time from referral to admission decision', '≤ 5 business days', 'Monthly', 'Referral log', 'QP'],
        ['Access', 'Time from admission to first clinical contact', '≤ 72 hours', 'Monthly', 'Clinical record', 'Clinical Director'],
        ['Access', 'No-show rate for scheduled appointments', '≤ 10%', 'Monthly', 'Scheduling system', 'QP'],
        ['PCP', 'PCP completed within required timeframe', '100%', 'Monthly', 'Clinical record audit', 'QP'],
        ['PCP', 'PCP reviewed at required intervals', '100%', 'Monthly', 'Clinical record audit', 'QP'],
        ['PCP', 'Youth/family participation in PCP meetings', '≥ 90%', 'Quarterly', 'PCP signature page', 'Clinical Director'],
        ['Outcomes', 'Symptom improvement (PHQ-A / GAD-7)', '≥ 80% show improvement', 'Quarterly', 'Validated instruments', 'Clinical Director'],
        ['Outcomes', 'Functional improvement (CAFAS)', '≥ 70% show improvement', 'Quarterly', 'CAFAS scoring', 'Clinical Director'],
        ['Outcomes', 'Restraint frequency', '≤ 0.5 per 1,000 youth-days', 'Monthly', 'Restraint log', 'QP'],
        ['Outcomes', 'Elopement frequency', '≤ 0.3 per 1,000 youth-days', 'Monthly', 'Incident reports', 'QP'],
        ['Outcomes', 'Incident frequency and severity', 'Trend analysis', 'Monthly', 'IRIS reports', 'Compliance Officer'],
        ['Safety', 'Incident-free days', 'Trending upward', 'Monthly', 'IRIS reports', 'Compliance Officer'],
        ['Safety', 'Time-to-investigation', '≤ 1 business day', 'Monthly', 'IRIS reports', 'Compliance Officer'],
        ['Safety', 'Repeat-incident rate', '≤ 10%', 'Quarterly', 'IRIS reports', 'Compliance Officer'],
        ['Safety', 'Medication-error rate', '≤ 1 per 1,000 doses', 'Monthly', 'MAR / med-error log', 'RN'],
        ['Personnel', 'Turnover rate (annual)', '≤ 25%', 'Quarterly', 'Personnel records', 'QP'],
        ['Personnel', 'Time-to-fill open positions', '≤ 45 days', 'Monthly', 'Recruiting log', 'Executive Director'],
        ['Personnel', 'Training completion rate', '100%', 'Monthly', 'Training calendar', 'QP'],
        ['Personnel', 'Personnel engagement score', '≥ 4.0 / 5.0', 'Annual', 'Engagement survey', 'Executive Director'],
        ['Financial', 'Days cash-on-hand', '≥ 60 days', 'Monthly', 'Financial statements', 'Executive Director'],
        ['Financial', 'Medicaid denial rate', '≤ 5%', 'Monthly', 'Billing system', 'Billing Coordinator'],
        ['Financial', 'Cost per youth per day', 'Trend analysis', 'Quarterly', 'Financial statements', 'Executive Director'],
        ['Experience', 'Youth satisfaction score', '≥ 4.0 / 5.0', 'Quarterly', 'Satisfaction survey', 'QP'],
        ['Experience', 'Family/LRP satisfaction score', '≥ 4.0 / 5.0', 'Semi-annual', 'Satisfaction survey', 'QP'],
        ['Experience', 'Complaint volume and resolution time', 'Trend analysis', 'Quarterly', 'Grievance log', 'QP'],
    ]
    story.append(std_table(pm_header, pm_rows,
                           col_widths=[0.10*AVAIL_W, 0.30*AVAIL_W, 0.18*AVAIL_W, 0.10*AVAIL_W,
                                       0.18*AVAIL_W, 0.14*AVAIL_W],
                           header_align='left', first_col_left=True, small=True))
    story.append(Spacer(1, 6))
    story.append(Paragraph('<b>10.4 Data Collection &amp; Aggregation.</b>', s_h2))
    story.append(para(
        'Each indicator has a designated data source and owner responsible '
        'for data collection. The QP aggregates data monthly, calculates '
        'the indicator value, and compares to the target. Data is stored '
        'in a master performance-measurement spreadsheet (or EHR analytics '
        'module) with monthly time-stamped entries. Data quality is '
        'verified quarterly through spot-checks against source records.'
    ))
    story.append(Paragraph('<b>10.5 Analysis &amp; Reporting.</b>', s_h2))
    story.append(para(
        'The QP analyzes performance data monthly for trends, identifies '
        'indicators that are off-target, and prepares a written quarterly '
        'report for the Governing Body. The report includes: (a) current '
        'value for each indicator; (b) trend over time (with comparison '
        'to prior quarters); (c) indicators that are off-target; (d) '
        'analysis of root causes; (e) recommended corrective actions; '
        'and (f) status of prior corrective actions. The report is '
        'presented at each quarterly Governing Body meeting.'
    ))
    story.append(Paragraph('<b>10.6 Use of Performance Data.</b>', s_h2))
    story.append(para(
        'Performance data is used to: (a) inform the annual revision of '
        'the Strategic Plan (Plan 1); (b) identify areas for quality '
        'improvement (incorporated into the QIP per SOP §12.20); (c) '
        'allocate resources (personnel, training, capital); (d) recognize '
        'and reinforce positive performance; and (e) demonstrate '
        'accountability to stakeholders. Performance data is shared with '
        'personnel and with persons served (in developmentally appropriate, '
        'aggregated form) at least quarterly through the "You Said / We '
        'Did" feedback loop (Plan 2).'
    ))
    story.append(Paragraph('<b>10.7 Responsible Parties.</b>', s_h2))
    story.append(para(
        '<b>QP</b> — overall coordination; data aggregation; quarterly '
        'report. <b>Clinical Director</b> — clinical outcomes data. '
        '<b>Compliance Officer</b> — safety data. <b>RN</b> — medication '
        'data. <b>Billing Coordinator</b> — financial data. <b>Executive '
        'Director</b> — personnel and overall financial data; resource '
        'allocation. <b>Governing Body</b> — reviews quarterly report; '
        'directs corrective action.'
    ))
    story.append(Paragraph('<b>10.8 Review Schedule.</b>', s_h2))
    story.append(para(
        'Monthly data aggregation. Quarterly analysis and Governing Body '
        'report. Annual full review of the Performance Measurement Plan, '
        'including indicator selection, target values, and data-collection '
        'methods.'
    ))
    story.extend(_approval_block('Performance Measurement Plan'))
    story.append(PageBreak())

    # ════════════════════════════════════════════════════════════════
    # PLAN 11 — PROGRAM DESCRIPTION (§12.11)
    # ════════════════════════════════════════════════════════════════
    story.extend(_plan_header(11, 'Program Description', '§12.11'))
    story.append(Paragraph('<b>11.1 Purpose.</b>', s_h2))
    story.append(para(
        'The Program Description demonstrates conformance to CARF CYS '
        'Section 2.A by documenting the populations served, the service '
        'array, the program philosophy, staffing patterns, physical '
        'environment, hours of operation, referral and intake process, '
        'cultural and linguistic competency plan, coordination with '
        'external systems of care, and the Person-Centered Plan process. '
        'The Program Description is approved by the Governing Body and '
        'serves as the primary evidence of the organization\'s program '
        'design for CARF surveyors.'
    ))
    story.append(Paragraph('<b>11.2 Populations Served.</b>', s_h2))
    story.append(para(
        'The program serves children and adolescents (target age range '
        '6–17) with a primary diagnosis of mental illness, emotional '
        'disturbance, or substance-related disorder, who do not meet '
        'inpatient psychiatric criteria but require removal from the home '
        'and treatment in a Level III Residential Treatment Facility '
        '(hardware-secure, intensive clinical). The program is designed '
        'to serve youth with severe emotional disturbance (SED) whose '
        'clinical acuity exceeds what can be safely managed in a less '
        'restrictive Level I or Level II residential setting, and who '
        'require intensive, active therapeutic treatment within a '
        'system-of-care approach. Admission criteria are documented in '
        'SOP §3.1 and the Screening and Access Policy (Plan 12).'
    ))
    story.append(Paragraph('<b>11.3 Service Array.</b>', s_h2))
    story.append(para('The program provides the following services:'))
    story.extend(bullets([
        '<b>Residential treatment</b> — 24-hour intensive residential '
        'treatment in a Level III RTF (hardware-secure) licensed under '
        '10A NCAC 27G .1703 (SOP §9);',
        '<b>Clinical services</b> — individual therapy, group therapy, '
        'family therapy, and clinical assessments (SOP §4);',
        '<b>Psychiatric medication management</b> — psychiatric evaluation, '
        'medication management, 6-month drug-regimen review (SOP §6.3);',
        '<b>Behavioral support</b> — behavioral assessment, behavioral '
        'support plan, crisis intervention, de-escalation, and (as '
        'last-resort) restraint (SOP §5);',
        '<b>Educational coordination</b> — coordination with the local '
        'public school system, facility-based school programming when '
        'needed, IEP coordination (SOP §7);',
        '<b>Case management</b> — care coordination with LME/MCO, DSS, '
        'juvenile justice, medical home, and other system-of-care '
        'partners;',
        '<b>Recreational, social, and life-skills programming</b> — '
        'structured daily activities, community integration, life-skills '
        'curriculum (SOP §5.4);',
        '<b>Family engagement</b> — family therapy, family visitation, '
        'family education, and transition support.',
    ]))
    story.append(Paragraph('<b>11.4 Program Philosophy.</b>', s_h2))
    story.append(para(
        'The program is grounded in trauma-informed care, which recognizes '
        'that the vast majority of youth served have experienced '
        'significant trauma and that all interactions must be conducted '
        'in a manner that promotes safety, trustworthiness, choice, '
        'collaboration, and empowerment. The program is also '
        'person-centered, meaning that each youth\'s treatment is '
        'individualized based on their strengths, needs, goals, and '
        'preferences, as documented in the Person-Centered Plan (SOP §4.1). '
        'The program is committed to the use of evidence-based and '
        'evidence-informed practices, including cognitive-behavioral '
        'therapy, trauma-focused CBT, motivational interviewing, and '
        'positive behavior support.'
    ))
    story.append(Paragraph('<b>11.5 Staffing Patterns.</b>', s_h2))
    story.append(para(
        'The program is staffed per SOP §2, including: Executive Director, '
        'Clinical Director, Qualified Professional (QP), Associated '
        'Professionals (APs), Direct Care Professionals (DCPs) on day, '
        'evening, and awake-overnight shifts, House Manager, Registered '
        'Nurse (RN), and Billing Coordinator. Staffing ratios comply with '
        'the Level III RTF operating standards under 10A NCAC 27G .1703, '
        'including a minimum 1:4 direct-care staff-to-resident ratio '
        'during waking hours (1:3 for high-acuity residents on line-of-'
        'sight supervision), and a minimum 1:8 ratio overnight with at '
        'least one awake DCP at all times. A Licensed Professional (LP) '
        'is on-site a minimum of 16 hours per day, 7 days per week, with '
        'on-call LP coverage outside those hours. A board-certified '
        'psychiatrist provides on-site coverage per the medication-'
        'management schedule and is on call 24/7 for psychiatric '
        'emergencies. A Registered Nurse (RN) is on-site or on call 24/7 '
        'for medical and medication-related needs. The QP provides '
        'clinical supervision per §1.4(a) and §2.2(a). A Licensed '
        'Professional provides minimum 4 hours per week face-to-face '
        'clinical consultation per §4.6 and Form 10.'
    ))
    story.append(Paragraph('<b>11.6 Physical Environment.</b>', s_h2))
    story.append(para(
        'The facility is a free-standing residential treatment facility '
        'designed and licensed as a Level III Residential Treatment '
        'Facility (Hardware-Secure) under 10A NCAC 27G .1703 for '
        'children and adolescents. Physical-plant requirements are '
        'documented in SOP §9. The facility includes: resident bedrooms '
        '(single or double occupancy per licensing standards); communal '
        'dining and living areas; kitchen and food-storage areas; '
        'clinical offices and therapy rooms; a quiet room / de-escalation '
        'room (not used for seclusion — seclusion is prohibited under '
        'the organization\'s restraint-and-seclusion-minimization policy '
        'per SOP §5); medication storage area (double-locked per SOP '
        '§6.3(c)); laundry facilities; outdoor recreation area with '
        'controlled-egress perimeter; and administrative offices. '
        'Hardware-secure features include staff-controlled egress doors '
        '(key-card or staff-activated release), alarmed perimeter doors '
        'and windows, 24-hour video monitoring of common areas and '
        'exterior approaches (not in bedrooms, bathrooms, or therapy '
        'rooms to protect privacy), and a secured visitor-entry '
        'vestibule. The facility complies with NFPA 101 Life Safety '
        'Code, ADA accessibility standards, and state fire/building '
        'codes, including the hardware-secure facility requirements '
        'under .1703.'
    ))
    story.append(Paragraph('<b>11.7 Hours of Operation.</b>', s_h2))
    story.append(para(
        'The program operates 24 hours per day, 7 days per week, 365 days '
        'per year. Clinical services are provided Monday–Friday 8:00 AM '
        'to 6:00 PM, with on-call clinical coverage outside those hours. '
        'Educational services are provided Monday–Friday during the '
        'school year per the local public school calendar. Recreational '
        'and life-skills programming is provided daily, including '
        'weekends.'
    ))
    story.append(Paragraph('<b>11.8 Referral &amp; Intake Process.</b>', s_h2))
    story.append(para(
        'Referrals are accepted from LME/MCOs, DSS, juvenile justice, '
        'inpatient psychiatric facilities, families/LRPs, and other '
        'system-of-care partners. The referral and intake process is '
        'documented in SOP §3 and the Screening and Access Policy '
        '(Plan 12). The QP screens each referral against admission '
        'criteria, communicates the admission decision within 5 business '
        'days, and coordinates intake logistics with the referring party.'
    ))
    story.append(Paragraph('<b>11.9 Cultural &amp; Linguistic Competency.</b>', s_h2))
    story.append(para(
        'The program is committed to cultural and linguistic competency, '
        'as documented in the Accessibility &amp; Nondiscrimination Plan '
        '(Plan 9). Personnel receive annual cultural-competency training. '
        'The program collects data on the demographic characteristics '
        'of persons served (race, ethnicity, primary language, religion) '
        'and uses this data to inform program design and personnel '
        'composition. Interpreter services are available at no cost to '
        'the youth and family. Vital documents are translated into the '
        'languages commonly encountered in the service area.'
    ))
    story.append(Paragraph('<b>11.10 Coordination with External Systems of Care.</b>', s_h2))
    story.append(para(
        'The program coordinates with the following external systems of '
        'care: (a) <b>LME/MCO</b> (Alliance Health) — authorization, '
        'utilization management, care coordination; (b) <b>DSS</b> — '
        'custody arrangements, family reunification, visitation; '
        '(c) <b>juvenile justice</b> — court-ordered placements, '
        'probation coordination; (d) <b>local public school system</b> — '
        'educational services, IEP coordination, transition planning; '
        '(e) <b>medical home</b> — primary care, dental, vision; '
        '(f) <b>psychiatric hospital</b> — inpatient admissions, '
        'discharge coordination; and (g) <b>community-based providers</b> '
        '— outpatient therapy, case management, peer support, '
        'recreational/faith-based activities. Coordination is documented '
        'in the Person-Centered Plan and the service record.'
    ))
    story.append(Paragraph('<b>11.11 Person-Centered Plan Process.</b>', s_h2))
    story.append(para(
        'Each youth has an individualized Person-Centered Plan developed '
        'within required timeframes per SOP §4.1. The PCP is developed '
        'by an interdisciplinary team including the youth (as '
        'developmentally appropriate), the family/LRP, the QP, the '
        'Clinical Director or designee, and other CFT members. The PCP '
        'addresses strengths, needs, goals, objectives, services, '
        'responsible parties, and review dates. The PCP is reviewed at '
        'required intervals and signed by all participants. Progress is '
        'documented in the service record per SOP §10.'
    ))
    story.append(Paragraph('<b>11.12 Discharge &amp; Transition Planning.</b>', s_h2))
    story.append(para(
        'Transition planning begins at admission, per SOP §3.4 and '
        'Plan 14. The youth and family/LRP participate in transition '
        'planning. The receiving provider (if any) is identified and '
        'engaged. The discharge summary is completed and provided to '
        'the youth, family/LRP, and receiving provider. Post-discharge '
        'follow-up occurs per Protocol 11. Advance written notification '
        'of discharge is provided per §3.4(a). Emergency discharges are '
        'followed by the 5-business-day post-emergency service-planning '
        'meeting per §3.4(c). The 18th-birthday continuation policy '
        'per §3.6 applies.'
    ))
    story.append(Paragraph('<b>11.13 Records of Persons Served.</b>', s_h2))
    story.append(para(
        'Records of persons served are maintained per SOP §1.6, §10, '
        'and §11, and per the Quality Records Review Procedure (Plan '
        '13). Records are retained per §1.6 (12 years post-majority). '
        'Confidentiality is maintained per §11. A mock chart containing '
        'forms for use with or by persons served is maintained per the '
        'CARF CYS General Program Standards note.'
    ))
    story.append(Paragraph('<b>11.14 Responsible Parties.</b>', s_h2))
    story.append(para(
        '<b>Clinical Director</b> — overall clinical program; approves '
        'Program Description. <b>Executive Director</b> — operational '
        'program; resource allocation. <b>QP</b> — daily program '
        'operations; intake; PCP coordination. <b>Governing Body</b> — '
        'approves Program Description; reviews annually.'
    ))
    story.append(Paragraph('<b>11.15 Review Schedule.</b>', s_h2))
    story.append(para(
        'Annual review and update of the Program Description, '
        'incorporating any changes in population, service array, '
        'staffing, facility, regulatory requirements, or program design. '
        'Ad-hoc review following any significant program change.'
    ))
    story.extend(_approval_block('Program Description'))
    story.append(PageBreak())

    # ════════════════════════════════════════════════════════════════
    # PLAN 12 — SCREENING AND ACCESS POLICY (§12.12)
    # ════════════════════════════════════════════════════════════════
    story.extend(_plan_header(12, 'Screening and Access Policy', '§12.12'))
    story.append(Paragraph('<b>12.1 Purpose.</b>', s_h2))
    story.append(para(
        'The Screening and Access Policy demonstrates conformance to CARF '
        'CYS Section 2.B by establishing written procedures for referral '
        'intake, screening, admission decisions, waitlist management, '
        'emergency access, denial of admission, and coordination with '
        'the LME/MCO access line.'
    ))
    story.append(Paragraph('<b>12.2 Scope.</b>', s_h2))
    story.append(para(
        'This policy covers all referrals received by the organization '
        'and all admission decisions. It applies to the QP (referral '
        'intake and admission decision), the Executive Director (denial '
        'appeals), and the Clinical Director (clinical eligibility).'
    ))
    story.append(Paragraph('<b>12.3 Referral Intake Process.</b>', s_h2))
    story.append(para(
        'Referrals are accepted from LME/MCOs, DSS, juvenile justice, '
        'inpatient psychiatric facilities, families/LRPs, and other '
        'system-of-care partners. The QP (or designee) receives each '
        'referral, documents it in the referral log within 1 business '
        'day, and acknowledges receipt to the referring party within '
        '2 business days. The referral packet includes at minimum: '
        '(a) youth demographic information; (b) current clinical '
        'assessment; (c) current medications; (d) recent hospitalization '
        'or treatment history; (e) school information; (f) custody/'
        'legal status; (g) insurance/Medicaid information; and (h) '
        'reason for referral.'
    ))
    story.append(Paragraph('<b>12.4 Screening Criteria.</b>', s_h2))
    story.append(para(
        'Each referral is screened against the admission criteria in '
        'SOP §3.1. The QP evaluates: (a) age (6–17); (b) primary '
        'diagnosis (mental illness, emotional disturbance, or '
        'substance-related disorder); (c) clinical acuity (does not '
        'meet inpatient criteria but requires the Level III RTF level '
        'of care — i.e., hardware-secure, intensive clinical services '
        'with 24-hour on-site Licensed Professional availability and '
        'psychiatric on-call, and whose acuity exceeds what can be '
        'safely managed in a less restrictive Level I or II setting); '
        '(d) medical stability (no acute medical condition '
        'requiring hospital-level care); (e) behavioral history '
        '(no pattern of sexual aggression requiring a specialized '
        'program); (f) cognitive functioning (IQ ≥ 50, sufficient to '
        'benefit from the program); (g) educational needs (can be met '
        'through the local public school system or facility-based '
        'programming); and (h) bed availability.'
    ))
    story.append(Paragraph('<b>12.5 Admission Decision.</b>', s_h2))
    story.append(para(
        'The QP makes the admission decision within 5 business days of '
        'receiving the complete referral packet. The decision is one of: '
        '(a) admit; (b) deny (with documented reason and appeal rights); '
        '(c) defer pending additional information; or (d) waitlist '
        '(if no bed is available). The decision is documented in the '
        'referral log and communicated to the referring party in writing '
        'within 1 business day of the decision. For admissions, the QP '
        'coordinates intake logistics (date, time, transportation, '
        'orientation) with the referring party.'
    ))
    story.append(Paragraph('<b>12.6 Waitlist Management.</b>', s_h2))
    story.append(para(
        'If no bed is available, the youth is placed on the waitlist. '
        'The QP maintains the waitlist in writing, ranked by date of '
        'admission decision and clinical priority (e.g., youth in '
        'inpatient holding, youth in emergency custody). The QP '
        'contacts the referring party weekly with waitlist status '
        'updates. When a bed becomes available, the QP contacts the '
        'next youth on the waitlist, re-confirms continued need, and '
        'coordinates intake. The waitlist is reviewed weekly by the QP '
        'and monthly by the Executive Director.'
    ))
    story.append(Paragraph('<b>12.7 Emergency/Crisis Access.</b>', s_h2))
    story.append(para(
        'For after-hours or emergency referrals, the on-call QP is '
        'available 24/7 via the on-call phone. The on-call QP conducts '
        'an abbreviated screening, coordinates with the referring party '
        '(e.g., emergency department, inpatient unit), and admits '
        'pending full screening within 24 hours. If admission is not '
        'appropriate, the on-call QP refers the youth to the LME/MCO '
        'access line or to the appropriate emergency service.'
    ))
    story.append(Paragraph('<b>12.8 Denial of Admission.</b>', s_h2))
    story.append(para(
        'If admission is denied, the QP documents the reason for denial '
        'in the referral log and communicates the denial in writing to '
        'the referring party within 1 business day. The written denial '
        'notice includes: (a) the specific reason for denial; (b) any '
        'recommended alternative services or providers; (c) the appeal '
        'procedure (written appeal to the Executive Director within '
        '10 business days); and (d) external appeal rights (LME/MCO, '
        'state licensing authority). The Executive Director reviews '
        'appeals within 5 business days and issues a written decision '
        'within 10 business days.'
    ))
    story.append(Paragraph('<b>12.9 Coordination with LME/MCO.</b>', s_h2))
    story.append(para(
        'The organization coordinates with Alliance Health (LME/MCO) '
        'access line for: (a) referrals through the LME/MCO access '
        'line; (b) prior authorization for admission; (c) continued '
        'stay reviews; (d) discharge planning; and (e) post-discharge '
        'service linkage. The QP is the primary point of contact with '
        'the LME/MCO. The QP ensures that all required authorizations '
        'are obtained prior to admission and maintained throughout the '
        'stay.'
    ))
    story.append(Paragraph('<b>12.10 Nondiscrimination in Access.</b>', s_h2))
    story.append(para(
        'Admission decisions are made without discrimination on the '
        'basis of race, color, national origin, religion, sex, gender '
        'identity or expression, sexual orientation, age, disability, '
        'or any other classification protected by applicable law (per '
        'Plan 9). Decisions are based solely on the youth\'s clinical '
        'needs and the program\'s ability to meet those needs safely '
        'and effectively.'
    ))
    story.append(Paragraph('<b>12.11 Access Data Tracking.</b>', s_h2))
    story.append(para(
        'The QP maintains access data including: (a) number of '
        'referrals received (by source); (b) number of admissions; '
        '(c) number of denials (by reason); (d) time-to-decision; '
        '(e) waitlist size and time-on-waitlist; and (f) demographic '
        'characteristics of referrals and admissions. This data is '
        'reported to the Governing Body quarterly as part of the '
        'Performance Measurement Plan (Plan 10) and is used to identify '
        'access disparities or inefficiencies.'
    ))
    story.append(Paragraph('<b>12.12 Responsible Parties.</b>', s_h2))
    story.append(para(
        '<b>QP</b> — referral intake; screening; admission decision; '
        'waitlist management; LME/MCO coordination. <b>Executive '
        'Director</b> — denial appeals; resource allocation. '
        '<b>Clinical Director</b> — clinical eligibility consultation. '
        '<b>On-call QP</b> — after-hours emergency access. <b>Governing '
        'Body</b> — reviews access data quarterly.'
    ))
    story.append(Paragraph('<b>12.13 Review Schedule.</b>', s_h2))
    story.append(para(
        'Monthly review of access data by the QP. Quarterly review by '
        'the Governing Body. Annual review of the Screening and Access '
        'Policy itself, including admission criteria, screening process, '
        'and denial trends.'
    ))
    story.extend(_approval_block('Screening and Access Policy'))
    story.append(PageBreak())

    # ════════════════════════════════════════════════════════════════
    # PLAN 13 — QUALITY RECORDS REVIEW PROCEDURE (§12.17)
    # ════════════════════════════════════════════════════════════════
    story.extend(_plan_header(13, 'Quality Records Review Procedure', '§12.17'))
    story.append(Paragraph('<b>13.1 Purpose.</b>', s_h2))
    story.append(para(
        'The Quality Records Review Procedure demonstrates conformance to '
        'CARF CYS Section 2.G and Section 2.H (Standard 4) by establishing '
        'a systematic process for reviewing clinical records for '
        'completeness, timeliness, and quality. The procedure ensures '
        'that records meet the standards of SOP §1.6, §10, and §11, and '
        'that deficiencies are identified, trended, and corrected through '
        'personnel feedback, retraining, and policy revision.'
    ))
    story.append(Paragraph('<b>13.2 Scope.</b>', s_h2))
    story.append(para(
        'This procedure covers all clinical records maintained by the '
        'organization for persons served, including intake documentation, '
        'assessments, Person-Centered Plans, service notes, medication '
        'records, incident reports, correspondence, and discharge '
        'documentation. It applies to the QP (audit lead), the Clinical '
        'Director (clinical oversight), and all personnel who create or '
        'maintain records.'
    ))
    story.append(Paragraph('<b>13.3 Review Frequency &amp; Sample.</b>', s_h2))
    story.append(para(
        'The QP conducts a quarterly records review using the '
        'Comprehensive Clinical Record Content Checklist (Form 8). The '
        'review includes: (a) 100% of records of youth discharged in the '
        'prior quarter; (b) a random 25% sample of active records; and '
        '(c) any records flagged for concern (e.g., recent incident, '
        'complaint, or extended stay). At minimum, 10 records per quarter '
        'are reviewed. The QP documents the sample selection methodology '
        'and the records reviewed.'
    ))
    story.append(Paragraph('<b>13.4 Review Criteria.</b>', s_h2))
    story.append(para(
        'Each record is reviewed against the Form 8 criteria, including:'
    ))
    story.extend(bullets([
        'Intake documentation complete (consent, release of information, '
        'rights acknowledgment, financial responsibility)',
        'Assessments completed within required timeframes (clinical, '
        'medical, psychiatric, behavioral, educational)',
        'Person-Centered Plan completed within required timeframe, '
        'signed by all participants, reviewed at required intervals',
        'Service notes completed per SOP §10.1–10.4 (timely, complete, '
        'authenticated)',
        'Medication records complete (MAR, consent, regimen review per '
        'Form 11)',
        'Incident reports complete and properly documented per SOP §8',
        'Correspondence filed and authorized per SOP §11.4',
        'Discharge documentation complete (summary, aftercare plan, '
        'transferred records)',
        'Record retention per SOP §1.6',
        'Confidentiality safeguards (locked storage, access controls, '
        'disclosure accounting per Form 9)',
    ]))
    story.append(Paragraph('<b>13.5 Findings Documentation.</b>', s_h2))
    story.append(para(
        'The QP documents findings on Form 8 for each record reviewed, '
        'noting: (a) record identifier; (b) date of review; (c) criteria '
        'met; (d) criteria not met (with specific deficiency); (e) '
        'responsible personnel member; (f) corrective action required '
        '(re-documentation, retraining, etc.); and (g) target completion '
        'date. Findings are aggregated quarterly to identify trends by '
        'criterion, by personnel member, by shift, and by program '
        'component.'
    ))
    story.append(Paragraph('<b>13.6 Trend Analysis &amp; Reporting.</b>', s_h2))
    story.append(para(
        'The QP analyzes quarterly findings to identify: (a) most common '
        'deficiencies; (b) personnel members or shifts with higher '
        'deficiency rates; (c) program components with systemic issues; '
        'and (d) improvements from prior quarters. The QP prepares a '
        'written quarterly report for the Clinical Director and Governing '
        'Body including: (a) number of records reviewed; (b) overall '
        'compliance rate; (c) most common deficiencies; (d) trend '
        'analysis; (e) corrective actions taken; and (f) recommendations '
        'for systemic improvement.'
    ))
    story.append(Paragraph('<b>13.7 Corrective Action.</b>', s_h2))
    story.append(para(
        'Deficiencies are addressed through: (a) individual personnel '
        'feedback within 5 business days of identification; (b) '
        're-documentation by the responsible personnel member within '
        '10 business days; (c) retraining for systemic deficiencies; '
        '(d) policy revision for systemic issues; and (e) disciplinary '
        'action for repeated or willful non-compliance. The QP tracks '
        'corrective actions to completion and verifies effectiveness in '
        'the subsequent quarter\'s review.'
    ))
    story.append(Paragraph('<b>13.8 Records Retention &amp; Confidentiality.</b>', s_h2))
    story.append(para(
        'Records are retained per SOP §1.6 (12 years post-majority). '
        'Confidentiality of records is maintained per SOP §11. Records-release '
        'accounting is maintained per SOP §11.4 and Form 9. The QP '
        'coordinates with the Compliance Officer to ensure that '
        'records-release accounting is up-to-date and that any '
        'unauthorized access is investigated.'
    ))
    story.append(Paragraph('<b>13.9 Responsible Parties.</b>', s_h2))
    story.append(para(
        '<b>QP</b> — audit lead; quarterly review; trend analysis; '
        'reporting. <b>Clinical Director</b> — clinical oversight; '
        'corrective-action direction. <b>Compliance Officer</b> — '
        'confidentiality oversight; records-release accounting. <b>All '
        'Personnel</b> — timely and complete documentation; cooperation '
        'with audit. <b>Governing Body</b> — reviews quarterly report; '
        'ensures corrective action.'
    ))
    story.append(Paragraph('<b>13.10 Review Schedule.</b>', s_h2))
    story.append(para(
        'Quarterly records review. Quarterly trend report to the '
        'Governing Body. Annual review of the Quality Records Review '
        'Procedure itself, including review criteria, sample '
        'methodology, and effectiveness.'
    ))
    story.extend(_approval_block('Quality Records Review Procedure'))
    story.append(PageBreak())

    # ════════════════════════════════════════════════════════════════
    # PLAN 14 — TELEHEALTH & ICT SERVICE DELIVERY POLICY (§12.18)
    # ════════════════════════════════════════════════════════════════
    story.extend(_plan_header(14, 'Telehealth & ICT Service Delivery Policy', '§12.18'))
    story.append(Paragraph('<b>14.1 Purpose.</b>', s_h2))
    story.append(para(
        'The Telehealth &amp; Information and Communication Technologies '
        '(ICT) Service Delivery Policy demonstrates conformance to CARF '
        'CYS Section 2.I by establishing written procedures for the '
        'delivery of services via telehealth and other '
        'technology-mediated platforms. The policy ensures that '
        'technology-mediated services are delivered in a manner that '
        'protects privacy, ensures informed consent, maintains quality, '
        'and provides appropriate fallback when technology fails.'
    ))
    story.append(Paragraph('<b>14.2 Scope.</b>', s_h2))
    story.append(para(
        'This policy covers all services delivered via information and '
        'communication technologies, including: videoconferencing '
        '(individual, family, and group therapy); telephone contact; '
        'secure messaging; remote psychiatric medication management; '
        'clinical supervision; and care-coordination meetings. It '
        'applies to all clinical personnel who deliver technology-mediated '
        'services and to the QP (oversight).'
    ))
    story.append(Paragraph('<b>14.3 Eligible Services.</b>', s_h2))
    story.append(para(
        'The following services may be delivered via telehealth/ICT, '
        'subject to clinical appropriateness and the youth\'s '
        'Person-Centered Plan:'
    ))
    story.extend(bullets([
        'Family therapy sessions (especially for geographically distant '
        'family members)',
        'Psychiatric medication management follow-up (initial '
        'evaluation preferably in person)',
        'Clinical supervision of APs and DCPs',
        'Care-coordination meetings with external providers (LME/MCO, '
        'DSS, school, medical home)',
        'Individual therapy sessions (when in-person is not feasible '
        'or as clinically indicated)',
        'Group therapy sessions (limited use, subject to clinical '
        'judgment)',
    ]))
    story.append(Paragraph('<b>14.4 Technology Platforms.</b>', s_h2))
    story.append(para(
        'The organization uses only HIPAA-compliant, end-to-end encrypted '
        'telehealth platforms that have executed Business Associate '
        'Agreements (BAAs) with the organization. Approved platforms '
        'are listed in the IT inventory and reviewed annually. Personnel '
        'may not use consumer-grade videoconferencing (e.g., personal '
        'FaceTime, personal Skype) for service delivery. The platform '
        'must support: (a) waiting rooms / virtual lobby; (b) multi-'
        'factor authentication; (c) session encryption; (d) no '
        'recording without explicit consent; and (e) audit logging.'
    ))
    story.append(Paragraph('<b>14.5 Informed Consent.</b>', s_h2))
    story.append(para(
        'Informed consent for telehealth services is obtained prior to '
        'the first telehealth session and documented in the clinical '
        'record. The consent includes: (a) description of the services '
        'to be delivered via telehealth; (b) benefits of telehealth '
        '(access, convenience, continuity); (c) risks (technology '
        'failure, privacy breach, limitations of remote assessment); '
        '(d) alternatives (in-person services); (e) right to withdraw '
        'consent at any time without affecting other services; (f) '
        'procedures for technology failure; (g) procedures for '
        'emergencies during a telehealth session; and (h) confidentiality '
        'and privacy safeguards. The consent is signed by the youth (as '
        'developmentally appropriate), the family/LRP, and the '
        'clinician.'
    ))
    story.append(Paragraph('<b>14.6 Personnel Training &amp; Competency.</b>', s_h2))
    story.append(para(
        'Personnel who deliver telehealth services complete training on: '
        '(a) the telehealth platform (technical operation); (b) clinical '
        'considerations for telehealth (modified assessment techniques, '
        'managing engagement remotely, crisis response); (c) privacy '
        'and security requirements; (d) informed consent; (e) '
        'documentation requirements; and (f) emergency procedures. '
        'Training is documented in the personnel file. The QP verifies '
        'competency through direct observation prior to independent '
        'telehealth practice.'
    ))
    story.append(Paragraph('<b>14.7 Technology Failure Procedures.</b>', s_h2))
    story.append(para(
        'If the technology platform fails during a session, the '
        'clinician: (a) attempts to reconnect within 5 minutes; (b) if '
        'reconnection fails, calls the youth/family by telephone to '
        'continue the session by phone or reschedule; (c) documents '
        'the technology failure and the alternative arrangement in the '
        'service note; and (d) reports recurring technology failures to '
        'the QP. For scheduled telehealth sessions, the clinician '
        'confirms a backup telephone number for the youth/family prior '
        'to the session.'
    ))
    story.append(Paragraph('<b>14.8 Privacy During Telehealth Sessions.</b>', s_h2))
    story.append(para(
        'The clinician conducts telehealth sessions from a private '
        'location (closed-door office, no other personnel or youth '
        'within hearing range, headset used). The youth/family is '
        'asked to be in a private location as well. The clinician '
        'verifies the youth\'s identity and location at the start of '
        'each session (for emergency-response purposes). The clinician '
        'documents the youth\'s location in the service note. Sessions '
        'are not recorded without explicit written consent.'
    ))
    story.append(Paragraph('<b>14.9 Emergency Procedures.</b>', s_h2))
    story.append(para(
        'The clinician confirms the youth\'s physical location at the '
        'start of each telehealth session. If the youth exhibits '
        'suicidal ideation, homicidal ideation, or other acute risk '
        'during a telehealth session, the clinician: (a) maintains '
        'connection with the youth; (b) alerts on-site personnel (DCP, '
        'House Manager) via telephone or messaging; (c) contacts the '
        'on-call QP or Clinical Director; (d) calls 911 if the youth '
        'cannot be located or if the risk is acute; and (e) documents '
        'the emergency response in the service note and an incident '
        'report per SOP §8.'
    ))
    story.append(Paragraph('<b>14.10 Documentation.</b>', s_h2))
    story.append(para(
        'Telehealth sessions are documented in the service record per '
        'SOP §10. The service note includes: (a) date, time, and '
        'duration of the session; (b) modality (video, phone); (c) '
        'platform used; (d) youth\'s location; (e) clinician\'s '
        'location; (f) participants (e.g., family members present); '
        '(g) clinical content; and (h) any technology issues '
        'encountered. The note is authenticated per SOP §10.6.'
    ))
    story.append(Paragraph('<b>14.11 Payer Coordination.</b>', s_h2))
    story.append(para(
        'The QP coordinates with the LME/MCO and other payers to '
        'confirm coverage of telehealth services, including any '
        'authorization requirements, documentation requirements, and '
        'reimbursement rates. The Billing Coordinator is informed of '
        'telehealth coverage policies to ensure accurate billing. The '
        'organization monitors changes in telehealth coverage (which '
        'have evolved rapidly) and updates this policy as needed.'
    ))
    story.append(Paragraph('<b>14.12 Responsible Parties.</b>', s_h2))
    story.append(para(
        '<b>Clinical Director</b> — overall clinical oversight of '
        'telehealth services. <b>QP</b> — operational implementation; '
        'training coordination; payer coordination; competency '
        'verification. <b>IT Coordinator</b> — platform management; '
        'security; BAA execution. <b>Clinical Personnel</b> — service '
        'delivery; documentation; emergency response. <b>Compliance '
        'Officer</b> — privacy oversight.'
    ))
    story.append(Paragraph('<b>14.13 Review Schedule.</b>', s_h2))
    story.append(para(
        'Annual review of the Telehealth &amp; ICT Service Delivery '
        'Policy, including platform review, training updates, and payer '
        'coverage changes. Ad-hoc review following any technology '
        'failure, privacy incident, or regulatory change.'
    ))
    story.extend(_approval_block('Telehealth & ICT Service Delivery Policy'))
    story.append(PageBreak())

    # ════════════════════════════════════════════════════════════════
    # PLAN 15 — SECTIONS 3-5 STANDARDS CROSSWALK (§12.19)
    # ════════════════════════════════════════════════════════════════
    story.extend(_plan_header(15, 'CARF CYS 2026 Sections 3–5 Standards Crosswalk', '§12.19'))
    story.append(Paragraph('<b>15.1 Purpose.</b>', s_h2))
    story.append(para(
        'The Sections 3–5 Standards Crosswalk demonstrates conformance '
        'to CARF CYS Section 3 (Core Program Standards), Section 4 (Core '
        'Residential Program Standards), and Section 5 (Specialty '
        'Designation Standards) at the time of the Inaugural Accreditation '
        'survey. Per the 2026 CYS Inaugural Accreditation Guidelines, '
        'all standards in Sections 3–5 are applicable to the extent '
        'possible. This crosswalk maps each applicable standard to the '
        'SOP Manual section, Plan, Protocol, or Form that addresses it, '
        'and identifies any standards not yet addressed with a written '
        'plan for addressing them prior to the subsequent resurvey.'
    ))
    story.append(Paragraph('<b>15.2 Scope.</b>', s_h2))
    story.append(para(
        'This crosswalk covers all standards in Sections 3, 4, and 5 of '
        'the 2026 CYS Standards Manual. Because the full text of those '
        'standards is proprietary to CARF and not reproduced here, the '
        'crosswalk identifies the standard area (e.g., "Residential '
        'Treatment — Admissions"), the SOP/Plan/Protocol/Form location '
        'where the organization\'s written policy addresses the standard, '
        'and the status (Met / In Progress / To Be Developed).'
    ))
    story.append(Paragraph('<b>15.3 Crosswalk.</b>', s_h2))
    story.append(para(
        'The following crosswalk maps the Sections 3–5 standard areas '
        'to the organization\'s written policies. The QP shall update '
        'this crosswalk after obtaining the full 2026 CYS Standards '
        'Manual to include specific standard numbers and any additional '
        'standards not anticipated here.'
    ))
    xw_header = ['#', 'Standard Area (Sections 3-5)', 'Organization\'s Written Policy Location', 'Status']
    xw_rows = [
        ['1', 'Core Program — Individualized Service Planning', 'SOP §4.1 (Person-Centered Plan); Plan 11 §11.11; Plan 13', 'Met'],
        ['2', 'Core Program — Service Delivery', 'SOP §4 (Clinical Services); SOP §5 (Behavioral); SOP §6 (Health); SOP §7 (Education)', 'Met'],
        ['3', 'Core Program — Coordination of Care', 'SOP §3 (Admissions/Discharge); SOP §4.5; Plan 11 §11.10', 'Met'],
        ['4', 'Core Program — Family Engagement', 'SOP §4 (family therapy); SOP §3.4 (transition); Plan 2 (family survey)', 'Met'],
        ['5', 'Core Residential — Admissions', 'SOP §3.1; Plan 12 (Screening & Access Policy)', 'Met'],
        ['6', 'Core Residential — Discharge & Transition', 'SOP §3.4; SOP §3.6; Plan 11 §11.12; Protocol 11', 'Met'],
        ['7', 'Core Residential — Daily Structure & Programming', 'SOP §5.4 (activities); Protocol 22 (Daily Workflow)', 'Met'],
        ['8', 'Core Residential — Physical Environment', 'SOP §9 (Facility/Safety); Plan 11 §11.6', 'Met'],
        ['9', 'Core Residential — Supervision & Staffing', 'SOP §2 (HR/Staffing); SOP §2.2(a) (Individualized Supervision); Plan 11 §11.5', 'Met'],
        ['10', 'Core Residential — Awake Overnight Supervision', 'SOP §2.1; Plan 11 §11.5; Protocol 22 (DCP Awake Overnight)', 'Met'],
        ['11', 'Core Residential — Behavioral Support & Crisis Intervention', 'SOP §5 (Behavioral Management & Restraint); Form 3 (Restraint Debriefing)', 'Met'],
        ['12', 'Core Residential — Medication Management', 'SOP §6.3; Form 10 (LP Consult Log); Form 11 (Drug Regimen Review)', 'Met'],
        ['13', 'Core Residential — Health & Wellness', 'SOP §6 (Health/Medication); SOP §6.1 (TB/Infection Control); Protocol 18', 'Met'],
        ['14', 'Core Residential — Nutrition & Food Service', 'SOP §6.4 (Nutrition); Plan 6 §6.8 (food safety policy)', 'Met'],
        ['15', 'Core Residential — Education Services', 'SOP §7 (Education & Vocational Support); Plan 11 §11.10 (school coordination)', 'Met'],
        ['16', 'Core Residential — Recreation & Leisure', 'SOP §5.4 (Activities); Plan 11 §11.3 (service array)', 'Met'],
        ['17', 'Core Residential — Cultural & Spiritual Activities', 'SOP §5.4; Plan 9 (Accessibility); Plan 11 §11.9', 'Met'],
        ['18', 'Core Residential — Resident Rights & Responsibilities', 'SOP §3, §5, §6, §8, §11; Plan 8; Resident Handbook', 'Met'],
        ['19', 'Core Residential — Grievance Procedure', 'Plan 8 §8.4; Resident Handbook', 'Met'],
        ['20', 'Core Residential — Personal Funds Management', 'SOP §1.8; Plan 4 §4.6', 'Met'],
        ['21', 'Core Residential — Personal Belongings & Contraband', 'SOP §9.3; Form 2 (Contraband/Belongings Inventory); Protocol 5', 'Met'],
        ['22', 'Core Residential — Visitation & Communication', 'SOP §3; Resident Handbook; Plan 8', 'Met'],
        ['23', 'Core Residential — Privacy & Modesty', 'SOP §11; Plan 8; Resident Handbook', 'Met'],
        ['24', 'Core Residential — Incident Reporting & Investigation', 'SOP §8 (IRIS); Form 5 (Drill/Safety Log); Plan 5 §5.6', 'Met'],
        ['25', 'Core Residential — Emergency Preparedness', 'SOP §9.2; Protocol 19; Plan 5 §5.5; Plan 6', 'Met'],
        ['26', 'Core Residential — Records & Documentation', 'SOP §1.6, §10, §11; Plan 13; Form 7 (Service Note); Form 8 (Record Content)', 'Met'],
        ['27', 'Core Residential — Quality Improvement', 'SOP §1.4(a); Plan 10 (Performance Measurement); SOP §12.20 (QIP); Form 12', 'Met'],
        ['28', 'Core Residential — Workforce Competency', 'SOP §2; Plan 7; SOP §2.2(a) (Individualized Supervision)', 'Met'],
        ['29', 'Specialty Designation — Trauma-Informed Care', 'SOP §1.1 (mission); Plan 7 §7.4 (orientation); Plan 11 §11.4 (philosophy)', 'Met'],
        ['30', 'Specialty Designation — Person-Centered Planning', 'SOP §4.1; Plan 11 §11.11; Plan 13', 'Met'],
        ['31', 'Specialty Designation — Family-Driven & Youth-Guided', 'SOP §4.1 (PCP); Plan 2 (Stakeholder Input); Plan 8 (Rights)', 'Met'],
        ['32', 'Specialty Designation — Cultural & Linguistic Competency', 'Plan 9; Plan 11 §11.9; Plan 7 §7.4 (training)', 'Met'],
        ['33', 'Specialty Designation — Evidence-Based Practices', 'SOP §4 (Clinical); Plan 11 §11.4 (philosophy)', 'Met'],
        ['34', 'Specialty Designation — Strengths-Based Approach', 'SOP §4.1 (PCP); Plan 11 §11.4 (philosophy)', 'Met'],
        ['35', 'Specialty Designation — Community Integration', 'SOP §5.4 (activities); Plan 11 §11.10 (coordination)', 'Met'],
        ['36', 'Specialty Designation — Outcome Measurement', 'Plan 10 (Performance Measurement); SOP §12.10', 'Met'],
        ['37', 'Specialty Designation — Continuous Quality Improvement', 'Plan 10; SOP §12.20 (QIP); Form 12', 'Met'],
        ['38', 'Additional Standards — To Be Identified', 'Pending acquisition of full 2026 CYS Standards Manual', 'In Progress'],
    ]
    story.append(std_table(xw_header, xw_rows,
                           col_widths=[0.05*AVAIL_W, 0.32*AVAIL_W, 0.45*AVAIL_W, 0.18*AVAIL_W],
                           header_align='left', first_col_left=True, small=True))
    story.append(Spacer(1, 6))
    story.append(Paragraph('<b>15.4 Standards Not Yet Addressed.</b>', s_h2))
    story.append(para(
        'Standard area #38 ("Additional Standards — To Be Identified") '
        'reflects the organization\'s commitment to conduct a complete '
        'crosswalk upon receipt of the full 2026 CYS Standards Manual. '
        'The QP shall order the manual from www.carf.org/catalog, '
        'conduct the complete crosswalk, and retain the updated crosswalk '
        'in the compliance binder prior to the Inaugural Accreditation '
        'survey. Any standard not addressed by an existing written policy '
        'will be addressed through a written plan with target completion '
        'date prior to the subsequent resurvey.'
    ))
    story.append(Paragraph('<b>15.5 Review Schedule.</b>', s_h2))
    story.append(para(
        'The crosswalk is reviewed at each quarterly QP compliance '
        'report (per SOP §1.4(a)) and updated as standards are addressed '
        'or as the CYS Standards Manual is revised. The CARF CYS '
        'Standards Manual is published annually with a July 1 effective '
        'date; the QP obtains the updated manual each year and updates '
        'this crosswalk accordingly. The subsequent resurvey will likely '
        'be conducted under a newer version of the standards manual '
        'than the one used for the Inaugural Accreditation survey.'
    ))
    story.append(Paragraph('<b>15.6 Responsible Parties.</b>', s_h2))
    story.append(para(
        '<b>QP</b> — overall coordination; crosswalk maintenance; '
        'identification of gaps. <b>Compliance Officer</b> — regulatory '
        'alignment; gap remediation tracking. <b>Executive Director</b> '
        '— resource allocation for gap remediation. <b>Governing Body</b> '
        '— reviews crosswalk quarterly; ensures gaps are addressed.'
    ))
    story.extend(_approval_block('CARF CYS 2026 Sections 3–5 Standards Crosswalk'))

    return story
