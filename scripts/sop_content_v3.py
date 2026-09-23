# ────────────────────────────────────────────────────────────────────
# Content builders — Version 3.0 (Legislation-Free Public Edition) (RMDM-Compliant, July 2026)
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
        anchor='§1',
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
        '<b>1.2 Licensing &amp; Credentialing.</b> The facility operates under a valid license '
        'as a <b>Level III Residential Treatment Facility — Staff Secure for Children and '
        'Adolescents</b> under <b>our staff-secure operating standards</b>, issued by the '
        'applicable state mental health authority — <b>not</b> under foster-care licensing, '
        'and therefore does <b>not</b> operate as a family-home placement. The facility is '
        'credentialed as an In-Network Provider with <b>Alliance Health Tailored Plan</b> '
        '(the regional managed care organization / Tailored Plan serving Cumberland, '
        'Durham, Johnston, Mecklenburg, Orange and Wake counties, post-July 2024 NC S.L. '
        '2021-135 Tailored Plan transition). The Executive Director maintains the original '
        'license on site, posts a current copy in a public area of the facility, and renews it '
        'prior to expiration. Any change in ownership, capacity, population served, or physical '
        'location requires prior written approval from the state licensing authority and '
        'notification to Alliance Health.'
    ))
    story.append(Paragraph('<b>1.2(a) Accreditation Prerequisite &amp; Selected Accrediting Body.</b>', s_h2))
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
    ))
    story.append(Paragraph('<b>1.2(b) LME/MCO Letter of Support — the Resident Rights framework.1.</b>', s_h2))
    story.append(para(
        'Under the Resident Rights framework.1, the license application to DHSR MHLC must be accompanied by a '
        '<b>Letter of Support</b> from Alliance Health Tailored Plan (the LME/MCO/Tailored Plan) documenting that additional '
        'residential-treatment capacity is needed within the catchment area. The Executive '
        'Director shall request the Letter of Support from Alliance Health in writing prior to '
        'submitting the license application, attaching a needs-assessment summary, projected '
        'census, target population, and a service-area description. Alliance Health evaluates '
        'the request against current capacity, utilization data, and gap analysis, and may issue '
        'the Letter of Support, request additional information, or decline. The Letter of Support '
        'is valid for a limited period (typically 12 months) and must be current at the time of '
        'license application submission. Renewal applications and capacity-expansion applications '
        'require a new Letter of Support. The QP retains the original Letter of Support in the '
        'facility compliance binder for the duration of the license cycle.'
    ))
    story.append(Paragraph('<b>1.2(c) Certificate of Need (CON) Determination.</b>', s_h2))
    story.append(para(
        'North Carolina is a Certificate of Need (CON) state under state law Chapter 131E, Article 9. '
        'The Executive Director shall submit a written CON inquiry to the NC Department of Health '
        'and Human Services (DHHS) Acute and Home Care Licensure and Certification Section to '
        'determine whether the proposed Level III RTF bed count, services, and capital expenditure '
        'trigger CON review. If CON review is required, the application timeline typically '
        'extends by <b>4 to 9 months</b> and the project cannot proceed until a CON is issued. '
        'The CON determination letter (whether affirming review is required or stating review is '
        'not required) shall be retained in the facility compliance binder and shall accompany '
        'the DHSR MHLC license application. If CON is required and issued, the QP shall ensure '
        'the licensed bed count and services match the CON approval exactly. Material changes to '
        'bed count, services, or capital structure require a new CON determination prior to '
        'implementation.'
    ))
    story.append(Paragraph('<b>1.2(d) Alliance Health Tailored Plan Provider Network Application.</b>', s_h2))
    story.append(para(
        'Separate from the DHSR MHLC license, the facility must complete the <b>Alliance Health Tailored '
        'Plan Provider Application</b> to be enrolled in the Alliance Health Tailored Plan provider network and to '
        'bill Medicaid CCP 8D-2 (Residential Level III) per-diem services. The application package '
        'includes: (i) completed Provider Application; (ii) completed Self-Assessment Checklist '
        'demonstrating readiness across all our staff-secure operating standards standards; (iii) Mission and '
        'Vision statements; (iv) current DHSR license; (v) accreditation certificate; (vi) '
        'liability insurance certificate; (vii) governing-body roster; (viii) organizational '
        'formation documents; (ix) policies and procedures (this Manual); and (x) QP / QMHP '
        'credentialing files for clinical staff. Alliance Health conducts a <b>site review</b> '
        'prior to network approval, and the Alliance Health Medical Director (or designee) '
        'issues <b>credentialing approval</b> for each clinical staff member prior to billable '
        'service delivery. The QP maintains the Alliance Health provider agreement, site-review '
        'report, and credentialing-approval letters in the facility compliance binder and '
        're-credentials per the Alliance Health credentialing cycle (typically every 3 years).'
    ))
    story.append(Paragraph('<b>1.2(e) DHSR MHLC License Application Procedure.</b>', s_h2))
    story.append(para(
        'The DHSR MHLC license-application package shall be assembled by the QP and submitted '
        'as a single, complete packet containing: (i) the completed <b>Initial Licensure '
        'Application Form (DHHS/DHSR/MHL 5001)</b> — available from the DHSR MHLC website at '
        'https://info.ncdhhs.gov/dhsr/mhlcforms/index.html; (ii) a <b>Cover Letter</b> on '
        'company letterhead, signed by the Executive Director, briefly describing the proposed '
        'facility, license category (Level III RTF — Staff Secure, our staff-secure operating standards), '
        'catchment area, target population, projected census, and requested effective date; '
        '(iii) the accreditation certificate or letter of pending accreditation from one of the '
        'four approved accrediting bodies per §1.2(a); (iv) the Letter of Support from Alliance '
        'Health per §1.2(b); (v) the CON determination letter per §1.2(c); (vi) local approvals '
        '— zoning compliance letter per §9.6, building-code approval, fire-marshal approval, '
        'and sanitation approval; (vii) the facility floor plan and site diagram; (viii) '
        'corporate documents per §1.8 (Articles of Incorporation, Operating Agreement, '
        'governing-body roster, EIN, liability-insurance certificates, lease/deed); (ix) the '
        'Policies &amp; Procedures Manual (this document) with the MH Licensure P&amp;P '
        'Worksheet attached per §1.2(f); and (x) the non-refundable license-application fee '
        'per the current DHSR fee schedule. Upon receipt of a complete application, DHSR MHLC '
        'assigns a <b>Licensure &amp; Training Consultant</b> who serves as the facility\'s '
        'primary point of contact throughout the licensing process. <b>The six (6) month '
        'application-review period begins on the date of the first in-person meeting with the '
        'assigned Licensure &amp; Training Consultant.</b> The QP shall calendar the '
        'six-month deadline and provide monthly status updates to the Executive Director; any '
        'deficiencies identified by the Consultant shall be corrected within 30 calendar days '
        'whenever practicable. A license shall not be issued until the Licensure &amp; Training '
        'Consultant has confirmed that all application items are complete, all local approvals '
        'are current, and the facility has passed the on-site licensure survey per §10.10.'
    ))
    story.append(Paragraph('<b>1.2(f) MH Licensure Policies &amp; Procedures Worksheet.</b>', s_h2))
    story.append(para(
        'The <b>MH Licensure Policies &amp; Procedures Worksheet</b> is a DHSR MHLC-issued '
        'checklist that maps each our operating standards rule to a corresponding section of the facility\'s '
        'Policies &amp; Procedures Manual. The Worksheet is <b>not a substitute for the rules</b> '
        'and is <b>not a stand-alone document</b>; rather, it functions as a crosswalk that '
        'allows the Licensure &amp; Training Consultant to verify, at a glance, that every '
        'applicable 27G requirement is addressed somewhere in the P&amp;P Manual. The QP shall '
        'complete the Worksheet in full, attach it to the front of this Manual behind the cover '
        'letter, and update it any time a Manual section is substantively revised or a new '
        'section is added. The Worksheet shall reference the specific SOP section number '
        '(e.g., §2.1 for staffing ratios, §6.1 for admission physical examination, §9.5 for '
        'staff-secure physical-plant measures) where each rule is addressed. The completed '
        'Worksheet shall be retained in the facility compliance binder and made available to '
        'DHSR MHLC surveyors, Alliance Health site reviewers, and accrediting-body surveyors '
        'upon request. The current Worksheet is available from the DHSR MHLC website at '
        'https://info.ncdhhs.gov/dhsr/mhlcforms/index.html.'
    ))
    story.append(Paragraph('<b>1.2(g) NC Medicaid Residential Treatment Services Taxonomy — Setting Type, Supervision Intensity &amp; Coverage Scope.</b>', s_h2))
    story.append(para(
        'Under <b>NC Medicaid Clinical Coverage Policy 8D-2, "Residential Treatment '
        'Services" (Amended January 1, 2025)</b>, Section 1.0(c), the facility — operating as '
        'a <b>Residential Treatment Level III Service (Residential Treatment High)</b> for '
        'children/adolescents under age 21 — is characterized by NC Medicaid in three '
        'controlling respects that govern the program model, the supervision intensity, and '
        'the scope of Medicaid reimbursement:'
    ))
    story.append(para(
        '<b>Cross-reference to licensure rule — our staff-secure operating standards.</b> The three '
        'Medicaid taxonomy items below are consistent with, and operationally implemented '
        'through, the facility\'s licensure under <b>our staff-secure operating standards</b> — specifically '
        '<b>our staff-secure operating standards</b> (Authority state law; Eff. April 3, '
        '2006), which provides the regulatory basis for each item: (i) the "program setting '
        'only" limitation flows from .1701(a), which defines the facility as "a free-'
        'standing residential facility that provides intensive, active therapeutic treatment '
        'and interventions within a system of care approach" and provides that the facility '
        '"shall not be the primary residence of an individual who is not a client of the '
        'facility" — i.e., a family-home placement is structurally excluded at the licensure '
        'tier; (ii) the "highly structured and highly supervised" requirement flows from '
        '.1701(b) ("Staff secure means staff are required to be awake during client sleep '
        'hours and supervision shall be continuous as set forth in Rule .1704 of this '
        'Section") and .1701(e)(1) (services shall "include individualized supervision and '
        'structure of daily living"); and (iii) the room-and-board exclusion is a feature of '
        'the Medicaid RTS benefit category under CCP 8D-2 §1.0(c) and is not a licensure-'
        'side rule. The full text of .1701 SCOPE is retained in the facility compliance '
        'binder as documentation of the licensure framework governing this facility.'
    ))
    story.extend(bullets([
        '<b>(i) Setting type — Program setting only (not a family home).</b> '
        'CCP 8D-2 §1.0(c) provides: "Residential Treatment Level III Service (Residential '
        'Treatment High) has a highly structured and supervised environment <b>in a program '
        'setting only</b>, excluding room and board." The phrase "program setting only" is '
        'deliberate: NC Medicaid assigns a graduated setting-type hierarchy across the four '
        'RTS levels — Level I = "family setting"; Level II = "family <i>or</i> program '
        'setting"; Level III = "program setting <i>only</i>"; Level IV = "program setting '
        '<i>only</i>." The explicit "only" qualifier on Levels III and IV is the textual '
        'mechanism by which NC Medicaid excludes family-home placement at the Level III tier. '
        'Consistent with this, the facility is licensed under <b>state mental health law</b> by NC '
        'DHSR MHLC — not under state law Chapter 131D by DSS, which licenses foster-care family '
        'homes. The facility therefore does not, and cannot, operate as a family-home '
        'placement for any youth at any time.',
        '<b>(ii) Structure &amp; supervision — Highly structured and highly supervised.</b> '
        'CCP 8D-2 §1.0(c) and Attachment D (Section K) describe the Level III setting as '
        '"<b>highly structured and supervised</b>" — language NC Medicaid uses to '
        'distinguish Level III from the lower RTS tiers (Level I = "low to moderate '
        'structured and supervised"; Level II = "moderate to highly structured and '
        'supervised"). Attachment D further specifies: "Residential Treatment Level III '
        'service is responsive to the need for intensive, active therapeutic intervention, '
        'which requires a <b>staff secure</b> treatment setting in order to be successfully '
        'implemented… Staff are awake during sleep hours and supervision is continuous." '
        'The facility\'s operational implementation of this requirement includes: (a) the '
        '2:4 staffing ratio per §2.1 (two awake staff for every 1–4 youth 24/7/365); '
        '(b) continuous line-of-sight supervision per §9.5; (c) the 14-hours-per-week '
        'planned group activities program per §5.5; (d) the Behavior Support Plan (BSP) '
        'framework per §5.3; and (e) continuous awake overnight supervision per §2.1 and '
        'the DCP Awake Overnight schedule in Protocol 22.',
        '<b>(iii) Coverage scope — Room and board EXCLUDED from the Medicaid RTS benefit '
        'category.</b> CCP 8D-2 §1.0(c) provides that the Level III benefit "has a highly '
        'structured and supervised environment in a program setting only, <b>excluding room '
        'and board</b>." The "excluding room and board" clause is appended to every RTS '
        'level (I, II, III, and IV) in CCP 8D-2 §1.0 and is a feature of the RTS benefit '
        'category itself — not merely a billing limitation. Accordingly, the NC Medicaid '
        'RTS per-diem reimburses only the <b>clinical/treatment/milieu component</b> of '
        'residential care (assessments, PCP, individual/family/group therapy, behavioral '
        'interventions, 24-hour supervision, medication administration, crisis response, '
        'and related clinical services). The beneficiary\'s lodging and meals (room and '
        'board) must be funded through a <b>non-Medicaid source</b> — e.g., state/local '
        'social-services funds, foster care maintenance payments under Title IV-E, SSI/ISS, '
        'or other third-party resources. The QP and Billing Coordinator shall verify at '
        'admission and re-verify at each PCP review that an identified non-Medicaid room-'
        'and-board funding source is in place for every youth; the absence of such a '
        'funding source does not shift room-and-board costs to the Medicaid RTS per-diem '
        'under any circumstances.',
    ]))
    story.append(para(
        '<b>PRTF distinction — 42 CFR 483.352 / NC Medicaid CCP 8D-1.</b> The room-and-board '
        'exclusion verified above applies <b>only</b> to the RTS benefit under CCP 8D-2 '
        '(Levels I–IV, taxonomy 320800000X). It does <b>not</b> apply to <b>Psychiatric '
        'Residential Treatment Facilities (PRTFs)</b>, which are a separate, federally '
        'defined <b>inpatient</b> benefit Under our operating standards, Subpart G (§§ 483.350–'
        '483.376) and NC Medicaid CCP 8D-1. Because PRTF payment is an inpatient facility '
        'benefit, the PRTF per-diem <b>includes</b> the equivalent of room and board. This '
        'facility is <b>not</b> a PRTF; it is a Level III RTS Under our operating standards, and the room-'
        'and-board exclusion applies in full. See §7.3 for the facility-based-school '
        'determination that further distinguishes Level III RTS from PRTF.'
    ))
    story.append(para(
        '<i>Primary source: NC Medicaid Clinical Coverage Policy 8D-2, "Residential '
        'Treatment Services," Amended January 1, 2025, §1.0(c) and Attachment D — '
        'https://medicaid.ncdhhs.gov/8d-2-residential-treatment-services/download?attachment. '
        'Corroborating source: NC Medicaid Managed Care Health Plan Billing Guide, Version 31 '
        '(June 18, 2025) — '
        'https://medicaid.ncdhhs.gov/health-plan-billing-guide-version-31/open. '
        'Federal PRTF authority: 42 CFR Part 483, Subpart G — '
        'https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-G/part-483/subpart-G. '
        'NC PRTF policy: NC Medicaid CCP 8D-1 — '
        'https://medicaid.ncdhhs.gov/8d-1-psychiatric-residential-treatment-facilities-children-under-age-21/download?attachment.</i>'
    ))
    story.append(Paragraph('<b>1.2(h) Regulatory Citation Verification Note (Compliance Flag).</b>', s_h2))
    story.append(para(
        '<b>This subsection is a transparent compliance flag for review by the Executive '
        'Director, the QP, the facility\'s licensing consultant, and (as needed) DHSR MHLC '
        'and Alliance Health. It does not change any operational policy elsewhere in this '
        'Manual; it documents an open regulatory-citation question that must be resolved '
        'before initial licensure submission.</b>'
    ))
    story.append(para(
        '<b>(a) our operating standards vs .1700 — RESOLVED in v2.21.</b> The open question '
        'flagged in v2.20 — whether the operative NC Administrative Code section for a '
        'Level III Residential Treatment Facility — Staff Secure for Children or '
        'Adolescents is <b>our operating standards</b> or <b>our staff-secure operating standards</b> — has been '
        '<b>resolved in favor of .1700</b>. The text of <b>our staff-secure operating standards</b> '
        ' directly confirms that '
        '<b>.1700 is the codified section governing "Residential Treatment Staff Secure for '
        'Children or Adolescents."</b> Subsection .1701(a) defines the facility as "a free-'
        'standing residential facility that provides intensive, active therapeutic '
        'treatment and interventions within a system of care approach" and provides that '
        'the facility "shall not be the primary residence of an individual who is not a '
        'client of the facility"; .1701(b) defines "staff secure" as requiring that '
        '"staff are required to be awake during client sleep hours and supervision shall '
        'be continuous as set forth in Rule .1704 of this Section"; .1701(c)–(d) specify '
        'the population served and the clinical criteria (primary diagnosis of mental '
        'illness, emotional disturbance or substance-related disorders; not meeting '
        'criteria for inpatient psychiatric services; requiring removal from home and '
        'treatment in a staff secure setting); .1701(e) requires services to include '
        '"individualized supervision and structure of daily living," minimize behaviors '
        'related to functional deficits, ensure safety and de-escalate out-of-control '
        'behaviors, assist with adaptive functioning, and support step-down to a less '
        'intensive setting; .1701(f) requires coordination with other individuals and '
        'agencies within the child\'s system of care. Accordingly, <b>all ".2600" '
        'citations throughout this Manual have been updated to ".1700" in this v2.21 '
        'revision</b>. The QP shall retain a printed copy of the .1701 SCOPE rule text '
        '(as provided by the organization) in the facility compliance binder as '
        'documentation of this resolution. No further action is required on this '
        'subsection (a); the Licensure &amp; Training Consultant written confirmation '
        'referenced in v2.20 §1.2(h)(a) is no longer necessary to resolve the citation '
        'number, although the QP should still confirm operational rule subsections '
        '(.1702–.1709) with the assigned Licensure &amp; Training Consultant per §1.2(e) at '
        'the first in-person meeting.'
    ))
    story.append(para(
        '<b>(b) NC Medicaid "CCP 8C" vs "CCP 8D-2" — RESOLVED in v2.23.</b> The open '
        'question flagged in v2.20 — whether the correct NC Medicaid Clinical Coverage '
        'Policy for Level III Residential Treatment Services is <b>CCP 8C</b> or <b>CCP '
        '8D-2</b> — is hereby <b>resolved in favor of CCP 8D-2</b>. The NC Medicaid '
        'clinical coverage policy library confirms that CCP 8C is "Outpatient Behavioral '
        'Health Services Provided by Direct-Enrolled Providers" — a different benefit '
        'category that does <b>not</b> cover residential treatment services. The correct '
        'NC Medicaid clinical coverage policy for Residential Treatment Services '
        '(Levels I–IV) is <b>CCP 8D-2</b>, "Residential Treatment Services" (Amended '
        'January 1, 2025), available at '
        'https://medicaid.ncdhhs.gov/8d-2-residential-treatment-services/download?attachment. '
        'CCP 8D-1 covers Psychiatric Residential Treatment Facilities (PRTFs) and CCP '
        '8D-3/8D-4/8D-5 cover adult ASAM-aligned SUD residential services. '
        '<b>All legacy "CCP 8C" references in this Manual have been globally updated '
        'to "CCP 8D-2" in this v2.23 revision</b> — including the reference lines of '
        '§1.2, §2, §3, §4, §5, §6, and §10, and the §1.2(e) Medicaid billing description. '
        'The QP shall retain a printed copy of the CCP 8D-2 policy (Amended January 1, '
        '2025) in the facility compliance binder as documentation of this resolution. '
        '§1.2(g), §1.9, and §10.9 already cited CCP 8D-2 as the operative authority '
        'for the RTS benefit and the room-and-board exclusion; with v2.23 the entire '
        'Manual is now internally consistent on CCP 8D-2. No further action is required '
        'on this subsection (b).'
    ))
    story.append(para(
        '<b>(c) No operational impact.</b> Nothing in this §1.2(h) changes the facility\'s '
        'license category (Level III RTF — Staff Secure under <b>our staff-secure operating standards</b>), '
        'its staffing ratios (2:4 minimum per §2.1), its admission physical-exam timing '
        '(90 days prior per §6.1), its resident-rights obligations (the Resident Rights framework '
        'per §1.7), its Medicaid taxonomy (320800000X per §1.9), or its room-and-board '
        'exclusion (per §1.2(g) and §10.9). <b>The .2600 → .1700 citation question '
        '(subsection (a) above) was resolved in v2.21; the CCP 8C → CCP 8D-2 citation '
        'question (subsection (b) above) is resolved in this v2.23 revision.</b> With both '
        'citation questions now closed, §1.2(h) is fully resolved and no open compliance '
        'flags remain in this subsection.'
    ))
    story.append(para(
        '<b>(d) Cross-reference clarification note (compliance binder).</b> The Level III '
        'Staff-Secure operating standards cross-reference the "Qualified professional" '
        'definition for the QP credentialing requirements in §1.4(b). The text of that '
        'rule cross-references subsection .0104(18) "Psychiatrist," which appears to be a '
        'typographical error in the rule itself — the operative definition is at '
        '.0104(21) "Qualified professional." This Manual applies the .0104(21) definition '
        'as the operative QP standard per §1.4(b). The QP shall retain this '
        'cross-reference clarification note in the facility compliance binder and shall '
        'confirm the discrepancy with the assigned Licensure &amp; Training Consultant at '
        'the first in-person meeting per §1.2(e).'
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
        'The <b>Qualified Professional (QP)</b> — also referred to in our staff-secure operating standards as '
        'the <b>Qualified Mental Health Professional (QMHP)</b> — reports to the Clinical '
        'Director and is responsible for scheduling clinical services, assessments, PCPs, and '
        'day-to-day supervision of Associate Professionals (APs) and Direct Care Professionals '
        '(DCPs) <b>according to the direction of the Clinical Director</b>. For purposes of '
        'this Manual, "QP" and "QMHP" are used interchangeably and refer to the same role; '
        'the credentialing requirements in §1.4(b) satisfy both the our operating standards QP '
        'definition and the our staff-secure operating standards QMHP definition. The QP supervises staff '
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
        'requirements of <b>our operating standards</b>. A QP is not required to hold a '
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
        'Under our operating standards, 42 CFR Part 2, and the NC General Statutes.'
    ))
    story.append(Paragraph('<b>1.7 Resident Rights &amp; Dignity.</b>', s_h2))
    story.append(para(
        'Pursuant to <b>the Resident Rights framework</b> and our operating standards, every '
        'youth admitted to this facility retains the rights enumerated in this section, '
        'regardless of clinical status, behavioral history, or supervision level. The staff-'
        'secure designation of this facility <b>does not</b> diminish, suspend, or modify '
        'these rights; it only authorizes the physical-plant and supervision measures '
        'described in §9.5. Rights shall be exercised without retaliation, and any staff '
        'interference with the free exercise of rights shall be reported to the QP within '
        '24 hours and logged on the IRIS system per §8 if the interference constitutes a '
        'reportable incident under Rule 108.'
    ))
    story.append(para(
        '<b>(a) Statutory Rights.</b> Each youth has the right to: (i) receive humane, '
        'dignified, and respectful treatment; (ii) be free from abuse, neglect, and '
        'exploitation; (iii) be free from corporal punishment and from physical or '
        'chemical restraint except as specifically authorized in §5; (iv) receive '
        'treatment in the least restrictive environment consistent with clinical need; '
        '(v) participate in the development of, and receive a copy of, the Person-Centered '
        'Plan (PCP) per §4; (vi) refuse treatment except as otherwise provided by law or '
        'court order; (vii) send and receive sealed, unopened mail without staff '
        'inspection except where a specific clinical basis is documented in the PCP; '
        '(viii) reasonable access to a telephone for private communication with family, '
        'guardian, attorney, clergy, and the LME/MCO recipient rights advisor; (ix) '
        'practice the religion of choice or refrain from religious practice; (x) be free '
        'from unnecessary or excessive medication per §6; (xi) be free from coercion to '
        'perform labor for the facility; (xii) retain personal property consistent with '
        'facility safety rules; (xiii) privacy during toileting, bathing, and medical '
        'examinations; (xiv) file a grievance with the LME/MCO, DHSR, or DHHS without '
        'interference or retaliation; and (xv) be informed of these rights orally and in '
        'writing at admission, in a language the youth and guardian understand, with a '
        'signed acknowledgment retained in the clinical record.'
    ))
    story.append(para(
        '<b>(b) Posted Notice.</b> A printed "Youth Rights" notice summarizing the above '
        'rights shall be posted in a conspicuous location in the facility common area and '
        'in each youth bedroom, in both English and Spanish, in a font size no smaller '
        'than 14-point, with the Alliance Health Tailored Plan Member &amp; Recipient Rights phone '
        'number and the NC DHSR complaint line printed at the bottom. The QP shall review '
        'the posted notice at each monthly fire-drill walk-through and replace any missing, '
        'defaced, or outdated copies within 5 business days.'
    ))
    story.append(para(
        '<b>(c) Grievance Procedure.</b> A youth, guardian, or staff member may file a '
        'grievance orally or in writing to the QP, the Clinical Director, or directly to '
        'the Alliance Health Tailored Plan Member &amp; Recipient Rights Office. All grievances shall be '
        'documented on Form 9 (Accounting of Disclosures) if protected health information '
        'is involved, and logged in a dedicated <b>Grievance Log</b> maintained by the QP. '
        'The QP shall acknowledge receipt within 1 business day, investigate within 5 '
        'business days, issue a written response within 15 business days, and report '
        'aggregate grievance data to the Clinical Director at each quarterly compliance '
        'report per §1.4(a). Retaliation against any person filing a grievance is strictly '
        'prohibited and constitutes an immediately reportable personnel action.'
    ))
    story.append(Paragraph('<b>1.8 Organizational &amp; Financial Foundations.</b>', s_h2))
    story.append(para(
        'The following corporate and financial documents shall be maintained in the '
        'facility compliance binder and shall be made available to DHSR MHLC surveyors, '
        'Alliance Health site reviewers, accrediting-body surveyors, and authorized '
        'auditors upon request:'
    ))
    story.extend(bullets([
        '<b>Articles of Incorporation</b> — the LLC Articles filed with the NC Secretary of '
        'State, including all amendments, with current certification from the Secretary of '
        'State (no older than 90 days).',
        '<b>Operating Agreement</b> — the current executed Operating Agreement of Well Spring '
        'Intervention LLC, including all amendments and member-consent resolutions.',
        '<b>Governing Body Roster</b> — a current list of all members of the governing body '
        '(Managing Member / Board of Managers / Board of Directors, as applicable), '
        'including each member\'s full legal name, business address, term of office, and '
        'officer position held (Chair, Secretary, Treasurer, etc.). Updated within 30 days '
        'of any change.',
        '<b>EIN &amp; Tax Documents</b> — IRS Employer Identification Number letter, NC '
        'Department of Revenue tax-account letter, and current business-privilege-license '
        'confirmation if applicable to the locality.',
        '<b>Liability Insurance</b> — current certificates of insurance for: '
        '(i) <b>general liability</b> (minimum $1,000,000 per occurrence / $3,000,000 '
        'aggregate); (ii) <b>professional liability (malpractice)</b> (minimum $1,000,000 '
        'per occurrence / $3,000,000 aggregate); (iii) <b>commercial auto</b> (minimum '
        '$1,000,000 combined single limit for owned, hired, and non-owned vehicles used to '
        'transport youth); (iv) <b>workers\' compensation</b> per NC statutory limits; '
        'and (v) <b>cyber liability</b> covering protected health information (minimum '
        '$1,000,000) given the EHR/EMR system in use. Alliance Health Tailored Plan and DHSR MHLC shall '
        'be listed as <b>additional insureds</b> on the general-liability and '
        'professional-liability policies. Insurance lapses shall be reported to the QP '
        'immediately and to Alliance Health Tailored Plan within 5 business days.',
        '<b>Facility Lease or Deed</b> — current executed lease (with landlord\'s written '
        'consent to operate a Level III RTF on the premises) or recorded warranty deed.',
        '<b>Financial Solvency Documentation</b> — most recent 3 months of bank statements, '
        'most recent filed tax return, and a current balance sheet, sufficient to '
        'demonstrate ongoing financial solvency as required by our operating standards.',
        '<b>Governing Body Meeting Minutes</b> — permanently maintained per the '
        'facility records-retention schedule, documenting all governing-body decisions, '
        'approvals, oversight actions, financial reviews, policy adoptions, and '
        'corporate-compliance oversight. Minutes shall be signed by the Secretary (or '
        'designee) and retained in chronological order in the compliance binder; '
        'electronic copies shall be backed up per the facility disaster-recovery plan.',
        '<b>Client Fee Assessment Policy</b> — written policy governing the assessment '
        'of any client fees (sliding-scale, co-pay, or self-pay) including the fee '
        'schedule, criteria for reduction or waiver, documentation requirements, and '
        'the staff member authorized to approve adjustments.',
        '<b>Lab Test Authorization &amp; Follow-Up Policy</b> — written policy governing '
        'the authorization, ordering, result-tracking, and clinical follow-up of '
        'laboratory tests ordered for youth (including routine labs, drug screens, '
        'and provider-ordered diagnostic studies), specifying the responsible provider, '
        'the result-notification pathway, and the documentation standard in the clinical '
        'record.',
        '<b>Volunteer Services Policy</b> — written policy governing the recruitment, '
        'screening (including background checks per §2.3), orientation, supervision, '
        'scope of permitted activities, and termination of volunteer services. '
        'Volunteers shall never have unsupervised contact with youth and shall not be '
        'counted toward the 2:4 staffing minimum per §2.1.',
    ]))
    story.append(Paragraph('<b>1.9 Medicaid Enrollment &amp; NCTracks (Post-Licensure).</b>', s_h2))
    story.append(para(
        'Upon issuance of the DHSR MHLC license and completion of the Alliance Health '
        'Provider Network Application per §1.2(d), the facility shall complete <b>Medicaid '
        'enrollment</b> through <b>NCTracks</b> — the State of North Carolina\'s Medicaid '
        'Management Information System (MMIS). Medicaid enrollment is a <b>post-licensure</b> '
        'step and is required before the facility may bill Medicaid for any covered service. '
        'The facility enrolls specifically under <b>NC Medicaid Clinical Coverage Policy '
        '8D-2, "Residential Treatment Services" (Amended January 1, 2025)</b> as a Level '
        'III (Residential Treatment High) provider — <b>not</b> under CCP 8C (Outpatient '
        'Behavioral Health) or CCP 8D-1 (PRTF). Per §1.2(g), the Medicaid RTS per-diem '
        'covers only the clinical/treatment/milieu component; <b>room and board are '
        'excluded from the Medicaid RTS benefit category</b> and must be funded through a '
        'non-Medicaid source for every admitted youth. The QP (or designated Billing '
        'Coordinator) shall complete the following steps in sequence:'
    ))
    story.extend(bullets([
        '<b>Obtain a National Provider Identifier (NPI)</b> for the organization (Type 2 '
        'NPI) from the National Plan &amp; Provider Enumeration System (NPPES) at '
        'https://nppes.cms.hhs.gov. Each individual billing clinician shall also obtain a '
        'Type 1 NPI. The NPI is a 10-digit numeric identifier required for all HIPAA-'
        'covered transactions.',
        '<b>Enroll in NCTracks</b> as a Medicaid provider at https://www.nctracks.osbm.nc.gov. '
        'Submit the completed NCTracks Provider Enrollment Application, current DHSR '
        'license, accreditation certificate, NPI confirmation letter, IRS letter confirming '
        'EIN, and the Alliance Health provider-agreement letter. NCTracks assigns the '
        'facility a permanent Medicaid Provider ID after enrollment approval.',
        '<b>Select the correct Medicaid service(s) via the Provider Permission Matrix (PPM)</b>. '
        'For a Level III RTF serving children/adolescents, the applicable taxonomy is '
        '<b>320800000X — Residential Treatment Facility, Children</b> (alternatively '
        '320900000X — Residential Treatment Facility, Physically Impaired, if dual-diagnosis '
        'population is served). The QP shall confirm the current applicable taxonomy code '
        'with Alliance Health and NCTracks at the time of enrollment, as NC Medicaid '
        'covered-service definitions and taxonomy mappings are periodically updated. The '
        'PPM is accessed through the NCTracks provider portal and identifies the specific '
        'service(s) the facility is approved to deliver and bill.',
        '<b>Complete the post-enrollment accreditation timeline.</b> Per the Resident Rights framework and '
        'NC Medicaid policy, residential child-care facilities must achieve full national '
        'accreditation within <b>one (1) year</b> of Medicaid enrollment for most services, '
        'or within <b>three (3) years</b> for services with an extended accreditation '
        'timeline. Because accreditation is a pre-licensure requirement under §1.2(a), this '
        'facility shall enter Medicaid enrollment with current accreditation already in '
        'place; the post-enrollment timeline therefore operates as a re-affirmation of '
        'continuous accreditation maintenance, not as a new deadline.',
        '<b>Maintain enrollment in good standing.</b> Re-attest the NCTracks enrollment '
        'information at least every 12 months (or per the current NCTracks re-attestation '
        'cycle); report any change of address, ownership, licensing capacity, or '
        'accreditation status to NCTracks and to Alliance Health within 30 days; and '
        'respond to all NCTracks and Alliance Health provider inquiries within the '
        'timeframe specified in the inquiry.',
    ]))
    story.append(para(
        'The QP shall retain the NPI confirmation letter, NCTracks enrollment-approval '
        'letter, current PPM, and the most recent NCTracks re-attestation in the facility '
        'compliance binder. Reference links: <b>NPPES NPI Registry</b> '
        'https://nppes.cms.hhs.gov; <b>NCTracks Provider Enrollment</b> '
        'https://www.nctracks.osbm.nc.gov; <b>NCTracks Provider Permission Matrix (PPM) '
        'Help</b> https://www.nctracks.osbm.nc.gov/content/html/providers/provider-permission-'
        'matrix.html; <b>NC Medicaid Tailored Plan Provider Manual</b> '
        'https://medicaid.nc.gov/providers/provider-manuals; <b>NPI Taxonomy — '
        'Residential Treatment Facility codes (NUCC)</b> '
        'https://nucc.org/code-sets.'
    ))

    # ── SOP 2 ──────────────────────────────────────────────────────
    story.append(section_heading(2, 'Human Resources & Staffing Requirements'))
    story.append(ref_line(
        'our operating standards & .1700; NC Medicaid CCP 8D-2; RMDM Chapter 1',
        '§2',
    ))
    story.append(para(
        '<b>2.1 Staffing Ratios — Staff-Secure Level III.</b> Under our staff-secure operating standards, this '
        'Level III Staff-Secure facility shall maintain a <b>minimum of two (2) staff members '
        'on duty and awake at all times for every one to four (1–4) children in residence</b>, '
        'on every shift including the overnight shift. This 2:4 minimum applies 24 hours per '
        'day, 7 days per week, 365 days per year, and supersedes any lower ratio that may '
        'apply to less-intensive facility types. Ratios shall be <b>increased</b> based on PCP '
        'acuity, behavioral incidents, 1:1 supervision orders, gender-match requirements for '
        'two-person restraint protocols, or any time a youth is on continuous observation '
        'status per §5. The QP (or on-call QP designee) is responsible for monitoring ratios '
        'and adjusting assignments in real time to maintain compliance. A staff member who '
        'calls out within 4 hours of a shift shall trigger the on-call system; the on-call QP '
        'shall arrange a replacement <b>before the shift begins</b> and shall cover in-house '
        'personally if no replacement is available — the 2:4 minimum shall never be allowed '
        'to lapse. <b>Single-staffing is prohibited at all times.</b>'
    ))
    story.append(std_table(
        ['Shift', 'Minimum Staff (1–4 youth)', 'Minimum Staff (5–8 youth)', 'Minimum Staff (9 youth)', 'Status'],
        [
            ['Day (7a-3p)', '2 staff', '4 staff', '5 staff', 'Awake / On-site'],
            ['Evening (3p-11p)', '2 staff', '4 staff', '5 staff', 'Awake / On-site'],
            ['Overnight (11p-7a)', '2 staff', '4 staff', '5 staff', 'Awake (No sleeping)'],
        ],
        [0.16*AVAIL_W, 0.18*AVAIL_W, 0.18*AVAIL_W, 0.18*AVAIL_W, 0.30*AVAIL_W],
        first_col_left=True,
    ))
    story.append(Spacer(1, 6))
    story.append(para(
        '<i>Note: The Level III RTF Staff-Secure operating standards under 10A NCAC 27G '
        '.1706(a) limit a facility of this type to no more than twelve (12) children or '
        'adolescents. The facility\'s elected licensed capacity shall be stated on the '
        'state-issued license and shall not exceed twelve children under any '
        'circumstances; the facility may elect a lower licensed capacity (e.g., 6-9 beds) '
        'as a best-practice census ceiling.</i>'
    ))
    story.append(Spacer(1, 8))
    story.append(Paragraph('<b>2.2 Staff Qualifications.</b>', s_h2))
    story.append(para(
        '<b>General requirements for all staff.</b> All staff must: (a) be at least '
        '<b>18 years of age</b> at the time of hire; (b) be <b>literate in English</b> '
        'sufficient to read and understand this Manual, the youth\'s PCP and BSP, '
        'medication administration records, incident-report forms, and emergency '
        'procedures; (c) truthfully <b>disclose any criminal conviction history</b> on '
        'the employment application and consent to the background checks described in '
        '§2.3; and (d) provide documentation of education, licensure, and any '
        'credentials claimed on the employment application. Misrepresentation on the '
        'employment application is grounds for immediate termination.'
    ))
    story.extend(bullets([
        '<b>QPs:</b> Meet one of two pathways per §1.4(b) and our operating standards — <b>Pathway 1:</b> master\'s degree in a human services field plus a recognized NC credential (full license, associate/provisional license, certification, or psychiatric nursing credential) plus at least one year of full-time, post-master\'s supervised MH/DD/SA experience; OR <b>Pathway 2:</b> bachelor\'s degree in a human services field plus two years of full-time, pre- or post-bachelor\'s supervised MH/DD/SA experience. Both pathways require NC-DHHS QP training modules prior to independent practice. The designated facility QP shall also meet the two-year direct client care experience requirement per §1.4(b).',
        '<b>APs:</b> Meet one of four pathways per facility policy — <b>(i)</b> bachelor\'s degree in a human services field plus at least one year of relevant MH/DD/SA experience; <b>(ii)</b> registered nurse license plus at least one year of relevant MH/DD/SA experience; <b>(iii)</b> an equivalent state-recognized certification plus at least one year of relevant MH/DD/SA experience; or <b>(iv)</b> a high school diploma or GED plus at least five years of relevant MH/DD/SA experience. APs supervise paraprofessional Direct Care Professionals (DCPs) regarding PCP and BSP implementation per the individualized supervision plan required by §2.2(a).',
        '<b>Direct Care Professionals (DCPs):</b> High school diploma or GED with at least one year of mental health experience. DCPs work under the supervision of an AP or QP per the individualized supervision plan required by §2.2(a).',
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
        'in the personnel file per §2.5. Each supervision plan shall specify: '
        '(a) the supervisor\'s name, credential, and availability; (b) the frequency '
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
        'document the AP\'s authority to supervise paraprofessional DCPs regarding '
        'PCP and BSP implementation, including the documentation standard for AP '
        'review of DCP shift notes and incident reports.'
    ))
    story.append(Paragraph('<b>2.3 Background Checks (Prior to Unsupervised Contact).</b>', s_h2))
    story.extend(bullets([
        '<b>NC SBI fingerprint criminal background check</b> — must be completed within <b>180 days prior to initial licensure review</b> and re-checked annually thereafter and upon reasonable suspicion.',
        '<b>Health Care Personnel Registry check</b> — must be completed within <b>90 days prior to licensure review</b> (initial and renewal) and re-checked annually thereafter.',
        '<b>DSS Child Abuse and Neglect Registry check</b> (every state of residence in prior 5 years) — within 90 days prior to licensure review and annually thereafter.',
        '<b>Motor Vehicle Record (MVR)</b> for staff who transport residents — annually.',
        'Re-checks completed annually and upon reasonable suspicion.',
    ]))
    story.append(para(
        'No staff member shall have unsupervised contact with any youth until all four background-screening '
        'items above are complete, current, and on file in the personnel record. The QP shall maintain a '
        '<b>Background Check Expiration Tracking Log</b> showing for each staff member the date of the most '
        'recent criminal-background check, HCP-Registry check, DSS-CAN-Registry check, and MVR check, with '
        'automatic 30-day advance-notice alerts prior to each annual expiration. Any staff member whose '
        'background check has expired shall be removed from the schedule until the re-check is complete and '
        'on file.'
    ))
    story.append(Paragraph('<b>2.4 Mandatory Training (Prior to Independent Duty; Annual Refreshers).</b>', s_h2))
    story.extend(bullets([
        '<b>CPR with Heimlich Maneuver / First Aid</b> (annually; <b>in-person only</b> — no online-only certification accepted)',
        '<b>NCI or CPI restraint and de-escalation</b> (annually; <b>in-person only</b> for the physical-restraint module)',
        '<b>Medication Administration</b> (RN-delegated, annually; <b>in-person only</b>)',
        '<b>Bloodborne Pathogens</b> (annually)',
        '<b>Trauma-Informed Care</b> (annually)',
        '<b>Rule 108 incident reporting</b> (annually)',
        '<b>Population-Specific Training</b> — children/adolescents with serious emotional disturbance (SED), '
        'co-occurring disorders, trauma history, and the developmental, cognitive, and clinical '
        'characteristics of the population served by this facility (orientation + annual refresher)',
        '<b>Adolescent development, C-SSRS suicide risk assessment, and person-centered planning</b> '
        '(orientation + quarterly)',
        '<b>Alternatives to Restrictive Interventions (De-Escalation Training)</b> — verbal de-escalation, '
        'environmental modification, sensory regulation, and trauma-informed redirection (orientation + annual refresher)',
        '<b>Seclusion, Physical Restraint &amp; Isolation Time-Out</b> — physical-restraint techniques, '
        'release criteria, post-restraint medical/clinical monitoring, and documentation (annually; '
        '<b>in-person only</b>)',
        '<b>Client Rights &amp; Confidentiality</b> — the Resident Rights framework and HIPAA (orientation + annual refresher)',
        '<b>General Organization Orientation</b> — mission, policies, chain of command, emergency '
        'procedures (orientation)',
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
    story.append(Paragraph('<b>2.5(a) Continuing Education Units (CEUs) — Licensed Clinical Staff.</b>', s_h2))
    story.append(para(
        'Each licensed clinical staff member (LCSW, LPC, LMFT, LCAS, Licensed Psychologist, '
        'psychiatric RN / NP / CNS, etc.) shall complete the continuing-education hours '
        'required by their licensing board for each license-renewal cycle, and shall '
        'maintain original CEU certificates in the personnel file. Minimum CEU requirements '
        'by license type (verify current board rules — these are the typical NC minimums): '
        '<b>LCSW &amp; LCSW-A (NCSWCLB):</b> 40 contact hours / 2-year cycle, including 4 hrs '
        'ethics; <b>LPC &amp; LPC-A (NCBLPC):</b> 40 contact hours / 2-year cycle, including '
        '4 hrs ethics; <b>LMFT &amp; LMFT-A (NCMFT Licensure Board):</b> 20 contact hours / '
        '1-year cycle, including 3 hrs ethics; <b>LCAS &amp; LCAS-P (NCSAPPB):</b> 40 contact '
        'hours / 2-year cycle, including 4 hrs ethics and 3 hrs substance-abuse-specific; '
        '<b>Registered Nurses (NC BON):</b> 30 contact hours / 2-year cycle. The QP shall '
        'maintain a <b>CEU Tracking Log</b> showing for each licensed staff member: license '
        'type, license number, expiration date, current-cycle hours completed, hours '
        'remaining, ethics hours completed, and the date of the next renewal. The log shall '
        'be reviewed monthly by the QP; any staff member within 60 days of license expiry '
        'with insufficient CEUs shall be placed on a documented performance-improvement '
        'plan and removed from billable-service delivery if the license lapses. Lapsed '
        'licenses shall be reported to the Clinical Director within 1 business day and to '
        'Alliance Health credentialing within 5 business days.'
    ))
    story.append(Paragraph('<b>2.6 Staff Leave &amp; Time-Off Policy.</b>', s_h2))
    story.append(para(
        'Pursuant to our operating standards, the facility shall provide each full-time '
        'employee with <b>scheduled time off</b> as follows: (a) a minimum of two '
        'non-consecutive scheduled days off per 14-day pay period for direct-care staff '
        '(DCPs, APs) working 12-hour shifts, and a minimum of two scheduled days off per '
        '7-day week for administrative and clinical staff (QP, RN, Billing Coordinator) '
        'working 8-hour shifts; (b) paid time off (PTO) accruing at no less than the '
        'facility standard published in the Employee Handbook (currently 10 days/year in '
        'year 1, 15 days/year in years 2–4, and 20 days/year in year 5+); (c) <b>protected '
        'rest periods</b> of no fewer than 8 hours between consecutive shifts unless the '
        'staff member voluntarily waives the rest period in writing; (d) meal breaks of no '
        'fewer than 30 minutes per 8-hour shift and 60 minutes per 12-hour shift, during '
        'which the staff member is relieved of all youth-supervision duties (a second '
        'staff member shall be on duty to maintain the 2:4 minimum); (e) sick leave '
        'consistent with NC statutory requirements; (f) bereavement leave of up to 3 days '
        'per qualifying event; (g) family-medical leave consistent with the federal FMLA '
        'and NC leave laws; and (h) reasonable accommodation for religious observance. The '
        'QP publishes the schedule no fewer than 14 days in advance, posts it in the staff '
        'area, and accommodates time-off requests on a first-come-first-served basis '
        'subject to the 2:4 staffing minimum. Time-off denials shall be documented in '
        'writing with the operational basis. <b>Staff shall not be required to work more '
        'than 16 consecutive hours</b> except in a declared facility emergency, and any '
        'such extended shift shall be followed by no fewer than 10 hours of off-duty rest.'
    ))
    story.append(Paragraph('<b>2.7 Instructor Credentials &amp; Trainer Certifications.</b>', s_h2))
    story.append(para(
        'For each mandatory training topic listed in §2.4, the facility shall retain documentation '
        'of the instructor\'s qualifications and current instructor-level certification in the '
        'facility compliance binder (separate from individual staff personnel files). At a minimum, '
        'instructor credentials shall be maintained for: (a) <b>CPR with Heimlich Maneuver / First '
        'Aid</b> — current American Heart Association (AHA) Basic Life Support (BLS) Instructor '
        'certification or American Red Cross First Aid/CPR/AED Instructor certification; (b) '
        '<b>NCI or CPI restraint and de-escalation</b> — current NCI Instructor certification '
        'or CPI Certified Instructor credential; (c) <b>Medication Administration</b> — '
        'RN with current, unrestricted NC license who has completed the NC-DHHS-approved '
        'Medication Administration Trainer course (or equivalent) and is authorized by the '
        'facility\'s Clinical Director to delegate and train; (d) <b>Bloodborne Pathogens</b> — '
        'RN or qualified designee trained on the OSHA Bloodborne Pathogens Standard (29 CFR '
        '1910.1030); (e) <b>Seclusion, Physical Restraint &amp; Isolation Time-Out</b> — same '
        'instructor credentials as (b) above. For each instructor, the QP shall maintain: '
        'instructor name; certification body; certification number; issue date; expiration '
        'date; copy of the instructor certificate; and a list of all training sessions '
        'delivered (date, topic, attendee roster). Instructor certifications shall be '
        're-verified annually; expired instructor certifications shall be renewed before '
        'the instructor delivers any further training. Training delivered by an uncertified '
        'or expired-certified instructor is invalid and shall be re-delivered by a '
        'properly-certified instructor.'
    ))

    # ── SOP 3 ──────────────────────────────────────────────────────
    story.append(section_heading(3, 'Admissions, Discharges, and Transition Planning'))
    story.append(ref_line(
        'our staff-secure operating standards & .5604; NC Medicaid CCP 8D-2; RMDM Chapters 2 & 5',
        '§3',
    ))
    story.append(para(
        '<b>3.1 Admission Criteria.</b> The program serves youth with a primary mental '
        'health or behavioral diagnosis requiring supervised living, who are medically '
        'stable, and whose clinical needs can be safely met in a Level III Staff-Secure '
        'setting. Per §1.2(g) and NC Medicaid Clinical Coverage Policy 8D-2 §1.0(c), '
        'the Level III (Residential Treatment High) setting is a <b>"highly structured '
        'and supervised environment in a program setting only, excluding room and '
        'board"</b> — meaning the facility provides treatment in a structured <b>program '
        'setting</b> (not a family home), with continuous awake supervision per §2.1 and '
        '§9.5, and with the clinical/treatment/milieu component reimbursed by the '
        'Medicaid RTS per-diem while room and board are funded through a non-Medicaid '
        'source. Exclusions include acute psychiatric crisis requiring inpatient '
        'hospitalization, medical instability, or fire-setting that cannot be safely '
        'managed. The '
        'QP reviews each referral packet and documents the admission decision, '
        'including verification that an identified non-Medicaid room-and-board funding '
        'source is in place for the youth per §1.2(g)(iii) and §10.9.'
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
        'care, the CFT shall additionally confirm the step-down provider\'s admission '
        'date and any trial-home-visit schedule.'
    ))
    story.append(Paragraph('<b>3.4(c) Post-Emergency Service-Planning Meeting.</b>', s_h2))
    story.append(para(
        'Following any <b>emergency discharge, transfer, or hospitalization</b> (e.g., '
        'acute psychiatric hospitalization, medical hospitalization, safety-motivated '
        'transfer, or significant restraint event), the QP shall convene a '
        '<b>service-planning meeting within 5 business days</b> of the youth\'s return '
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
        'licensing authority; and (e) the facility <b>confirms that the youth\'s '
        'Medicaid eligibility and non-Medicaid room-and-board funding source</b> '
        'continue to cover the extended placement per §1.2(g)(iii) and §10.9. '
        'If any of these conditions cannot be met, the QP shall initiate transition '
        'planning to an appropriate adult placement <b>no later than 30 days before '
        'the youth\'s 18th birthday</b>, with the discharge date set on or before the '
        '18th birthday. The QP shall document satisfaction of each condition (a)–(e) '
        'in the clinical record and shall retain the youth\'s written consent and the '
        'LME/MCO approval letter in the facility compliance binder.'
    ))

    # ── SOP 4 ──────────────────────────────────────────────────────
    story.append(section_heading(4, 'Clinical Services, Assessments & Person-Centered Planning'))
    story.append(ref_line(
        'our operating standards; NC Medicaid CCP 8D-2; RMDM Chapter 4',
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
    story.append(Paragraph('<b>4.6 Licensed Professional Face-to-Face Clinical Consultation.</b>', s_h2))
    story.append(para(
        'Per the Level III Staff-Secure operating standards, the facility shall arrange '
        'for a <b>Licensed Professional to provide at least four (4) hours per week of '
        'face-to-face clinical consultation</b> with the clinical team. The Licensed '
        'Professional shall be a <b>clinician licensed by the applicable state licensing '
        'board to independently provide mental health services</b> (e.g., a licensed '
        'psychiatrist, psychologist, LCSW, LPC, or LMFT), and may be the facility\'s '
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
        'Professional\'s signature. The QP shall retain all consultation logs in the '
        'facility compliance binder and shall report weekly consultation-hour totals to '
        'the Clinical Director at each quarterly compliance report per §1.4(a).'
    ))

    # ── SOP 5 ──────────────────────────────────────────────────────
    story.append(section_heading(5, 'Behavioral Management & Restraint'))
    story.append(ref_line(
        'our operating standards; CMS Mental Health Parity Rules; RMDM Chapters 2 & 6',
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
        'Written notifications, consents, approvals, and other documentation per our '
        'service planning standards are required whenever a restrictive intervention is used as a '
        'planned intervention. Any planned restrictive interventions must be included in '
        'the youth\'s service plan per our operating standards. Documentation in the '
        'service record must meet requirements of our operating standards, '
        'including rights restrictions and use of protective devices.'
    ))
    story.append(Paragraph('<b>5.5 Activities Program — Minimum 14 Hours/Week Planned Group Activities.</b>', s_h2))
    story.append(para(
        'Pursuant to <b>our staff-secure operating standards</b> (and the service-design requirements of '
        '.1701(e), including "individualized supervision and structure of daily living" '
        'and acquisition of "social and recreational skills"), the facility shall provide '
        'each youth '
        'with a documented <b>activities program of no fewer than 14 hours per week of '
        'planned group activities</b> that promote socialization, physical activity, and '
        'creative expression. Activities shall be: (a) age- and developmental-stage '
        'appropriate; (b) culturally responsive; (c) consistent with each youth\'s PCP '
        'goals (per §4) and ISP objectives; (d) trauma-informed, with voluntary '
        'participation and the right to decline without consequence (except where a '
        'specific activity is ordered by a licensed clinician as part of the treatment '
        'plan); and (e) inclusive of all youth regardless of mobility, sensory, or '
        'cognitive accommodation needs, with reasonable modifications provided per the '
        'ADA and Section 504 of the Rehabilitation Act.'
    ))
    story.append(para(
        '<b>(a) Activity Categories.</b> The 14-hour weekly minimum shall be distributed '
        'across the following categories: <b>(i) physical activity</b> — structured '
        'sports, yoga, walking, swimming, gym visits, outdoor games (minimum 4 hrs/week); '
        '<b>(ii) creative expression</b> — art, music, journaling, theater, dance, '
        'photography, creative writing (minimum 3 hrs/week); <b>(iii) socialization &amp; '
        'life-skills</b> — cooperative games, group problem-solving, cooking, budgeting, '
        'self-care skills, communication skills (minimum 4 hrs/week); <b>(iv) community '
        'integration</b> — supervised outings to parks, libraries, cultural events, '
        'volunteer activities, faith-based services (where the youth elects) (minimum 3 '
        'hrs/week). Activities may overlap categories (e.g., a community outing that '
        'involves physical activity may count toward both categories\' minimums, but the '
        'total weekly hours still must sum to no fewer than 14 unique contact hours).'
    ))
    story.append(para(
        '<b>(b) Documentation.</b> The QP shall publish a written <b>Weekly Activities '
        'Calendar</b> no fewer than 7 days in advance, post it in the facility common '
        'area, and provide a copy to each youth at the weekly community meeting. Each '
        'scheduled activity shall be documented on the Activities Log (a sub-section of '
        'the daily shift note per §10.3) showing: date, activity name, category, '
        'duration (start/end time), staff facilitating, youth participating, youth '
        'declining (with brief reason), and any incidents or notable interactions. The '
        'QP shall total the weekly activity hours at each Monday shift-change huddle and '
        'shall report any week in which the 14-hour minimum was not met — with the '
        'reason and corrective-action plan — to the Clinical Director at the next '
        'monthly compliance report.'
    ))
    story.append(para(
        '<b>(c) Coordination with Protocol 22 Daily Workflow.</b> The Daily Workflow '
        'Schedules in Protocol 22 (DCP Day Shift, DCP Evening Shift, and weekend '
        'schedules) shall incorporate specific activity time-blocks sufficient to meet '
        'the 14-hour weekly minimum. The QP may adjust the daily schedule to accommodate '
        'school attendance, therapy appointments, weather, and behavioral acuity, '
        'provided the weekly 14-hour minimum is met. Activities shall be suspended only '
        'for documented safety reasons (e.g., a youth in crisis, an active IRIS '
        'investigation, a facility lockdown) and shall resume as soon as safety allows.'
    ))

    # ── SOP 6 ──────────────────────────────────────────────────────
    story.append(section_heading(6, 'Health, Medication, & Nutrition Management'))
    story.append(ref_line(
        'our operating standards; NC Nursing Practice Act; RMDM Chapters 5',
        '§6',
    ))
    story.append(Paragraph('<b>6.1 Medical Care.</b>', s_h2))
    story.append(para(
        'Each resident has an identified Primary Care Physician (PCP) and psychiatrist '
        'upon admission. <b>Per our staff-secure operating standards, a complete medical (physical) '
        'examination must be conducted within 90 days PRIOR to admission</b>, and the '
        'exam report must be reviewed by the QP and the RN prior to the youth\'s move-in '
        'date. The pre-admission exam shall include a comprehensive physical assessment, '
        'vision and hearing screening, immunization review (with documentation per state law '
        '§130A-152), TB screening per §6.2, and any indicated laboratory studies. If the '
        'physical exam is older than 90 days at the time of admission, a new exam shall '
        'be scheduled and completed within 7 days post-admission (with documentation of '
        'the scheduling in the clinical record) — this 7-day post-admission exam is a '
        'contingency only; it does NOT replace the 90-day pre-admission requirement. '
        '<b>Annual</b> physical examinations shall be conducted thereafter for the duration '
        'of the youth\'s stay. Medical history (including immunizations, allergies, and '
        'current prescriptions) is maintained and updated at every visit. Physician\'s '
        'directions for management of any identified medical conditions shall be '
        'documented in the PCP and communicated to all shift staff. The original physical '
        'exam report shall be retained in the clinical record per §1.6.'
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
        'All medications are stored in a double-locked cabinet/cart per §6.3(c). '
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
        'given the youth\'s diagnoses, age, weight, and clinical response; (2) any '
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
        'admission (the youth\'s most recent prior review may satisfy this requirement '
        'if completed within the prior 6 months and a copy is obtained).'
    ))
    story.append(Paragraph('<b>6.3(b) Medication Receipt &amp; Verification.</b>', s_h2))
    story.append(para(
        'All medications received at the facility — whether from a pharmacy, guardian, '
        'hospital, or other source — shall be <b>verified by the RN</b> (or '
        'designated RN-delegated staff) <b>at the time of receipt</b>. Verification '
        'shall confirm: (a) the medication is in <b>tamper-resistant packaging</b> per '
        'the state controlled-substances and pharmacy rules; (b) the <b>label contains</b> '
        'the youth\'s full name, medication name, strength, dose, route, frequency, '
        'prescribing provider, pharmacy name and phone number, prescription number, fill '
        'date, and expiration date; (c) the medication <b>matches the prescriber\'s '
        'order</b> in the youth\'s clinical record; and (d) the medication is <b>not '
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
        'secure, climate-controlled area maintained between <b>59°F and 86°F</b>. '
        'Medications requiring refrigeration shall be stored in a <b>dedicated medication '
        'refrigerator</b> (not used for food) maintained between <b>36°F and 46°F</b>, '
        'with the temperature documented on Form 5 (Environmental Safety Log) daily. '
        'Controlled substances shall be stored in the <b>inner locked compartment</b> of '
        'the double-locked cabinet, with a count documented at every shift change. Each '
        'youth\'s medications shall be stored in individually labeled containers. '
        'Medications shall <b>not</b> be stored in bathrooms, kitchens (except the '
        'medication refrigerator), or other areas exposed to moisture, heat, or direct '
        'sunlight. Expired or discontinued medications shall be segregated in a clearly '
        'labeled "To Be Disposed" container pending disposal per §6.3(d). The RN '
        'shall audit the medication storage area weekly and document the audit on Form 5.'
    ))
    story.append(Paragraph('<b>6.3(d) Medication Disposal Documentation.</b>', s_h2))
    story.append(para(
        'Discontinued, expired, or refused medications shall be disposed of in '
        'accordance with the state controlled-substances act and applicable federal '
        'medication-disposal rules. For each medication disposal event, the RN (or '
        'designated RN-delegated staff) shall document on the <b>Medication Disposal '
        'Log</b> (maintained in the med room): the youth\'s name, medication name, '
        'strength, quantity disposed, disposal method (e.g., pharmaceutical take-back, '
        'DEA-authorized collection receptacle, mail-back package), disposal date, '
        'witness signature, and RN signature. <b>Controlled-substance disposals shall '
        'be witnessed by a second staff member</b> and the witness signature shall be '
        'obtained prior to disposal. Medications transferred to the guardian at '
        'discharge shall be documented on the Medication Transfer Form (with the '
        'guardian\'s signature) and are <b>not</b> recorded on the Disposal Log. The '
        'QP shall review the Medication Disposal Log monthly as part of the controlled-'
        'substance reconciliation audit and shall report any discrepancies to the '
        'Clinical Director per §1.4(a).'
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
        'of adherence and the risks of abrupt discontinuation; (7) the youth\'s right '
        'to ask questions and to refuse medication (except as otherwise provided by law '
        'or court order per §1.7); and (8) what to do if a dose is missed. The '
        'youth\'s understanding shall be assessed (e.g., teach-back method) and '
        'documented after each education session. <b>Family/guardian medication '
        'education</b> shall also be offered at admission, at each medication change, '
        'and at least quarterly, with the offer and any education provided documented '
        'in the clinical record. The QP shall track medication-education due dates on '
        'the youth\'s PCP review calendar and shall report any youth with overdue '
        'medication education to the Clinical Director at each quarterly compliance '
        'report per §1.4(a).'
    ))
    story.append(Paragraph('<b>6.4 Nutrition.</b>', s_h2))
    story.append(para(
        'Meals follow USDA guidelines. Special diets are accommodated with provider '
        'documentation. Menus are posted and retained 30 days. Food is never withheld as '
        'a consequence. Staff preparing food maintain current food handler certifications.'
    ))
    story.append(Paragraph('<b>6.5 Infection Control Program.</b>', s_h2))
    story.append(para(
        'The facility shall maintain a written <b>Infection Control Program</b> consistent '
        'with <b>CDC guidelines</b> for residential congregate-care settings and '
        'OSHA Bloodborne Pathogens Standard (29 CFR 1910.1030). The '
        'program is overseen by the RN (with monthly QP review) and includes the '
        'following components:'
    ))
    story.extend(bullets([
        '<b>(a) Written Infection-Control Plan.</b> A facility-specific plan covering '
        'hand hygiene, standard precautions, transmission-based precautions, cleaning '
        'and disinfection, laundry handling, waste disposal, exposure response, '
        'outbreak response, and respiratory etiquette. Reviewed and updated annually '
        'and after any infection-control incident.',
        '<b>(b) Cleaning &amp; Disinfection Schedules.</b> Written daily, weekly, and '
        'monthly cleaning schedules specifying each area of the facility (kitchen, '
        'bathrooms, bedrooms, common areas, laundry, vehicles), the cleaning agent '
        'and concentration, the surface-contact time, and the staff member responsible. '
        'Schedules are posted in each area and the completed checklists are filed '
        'monthly in the facility compliance binder.',
        '<b>(c) Blood / Body Fluid Precautions.</b> Standard Precautions are observed '
        'with all youth at all times. <b>OSHA Bloodborne Pathogens exposure-control '
        'plan</b> on file: engineering controls (sharps containers), work-practice '
        'controls (no recapping needles), PPE (gloves, gowns, face protection), '
        'hepatitis-B vaccination offered to staff at no cost, post-exposure prophylaxis '
        'protocol available 24/7 via the RN and the local emergency department. All '
        'blood and body-fluid exposures (staff or youth) are documented on an Incident '
        'Report (§8) and IRIS-filed within 24 hours.',
        '<b>(d) Hand Hygiene.</b> Staff and youth perform hand hygiene: before meals '
        'and food preparation; after toileting or assisting a youth with toileting; '
        'after coughing, sneezing, or blowing the nose; before and after glove use; '
        'before and after medication administration; and after handling soiled laundry '
        'or trash. Alcohol-based hand sanitizer (60–95% alcohol) is available in every '
        'room except where flammable (e.g., kitchens with open flame). Soap and '
        'running water are used when hands are visibly soiled.',
        '<b>(e) Outbreak Response.</b> Two or more youth with identical symptoms '
        '(gastrointestinal, respiratory, or febrile) within 72 hours shall trigger an '
        'outbreak response: cohort-affected youth, increase sanitation, notify the '
        'County Health Department within 24 hours for any reportable communicable '
        'disease, and document the outbreak response in the facility compliance binder. '
        'The QP shall file an IRIS report for any communicable-disease outbreak '
        'affecting two or more youth.',
        '<b>(f) Immunization Compliance.</b> Each youth\'s immunization status shall be '
        'verified at admission per state law §130A-152 and updated per the CDC '
        'immunization schedule. Staff annual influenza vaccination is strongly '
        'recommended and documented in the personnel file. COVID-19 vaccination '
        'status of staff and youth is documented per current CDC and DHHS guidance.',
        '<b>(g) PPE Inventory.</b> The facility maintains a current inventory of '
        'exam gloves (multiple sizes), surgical masks, N95 respirators (for staff '
        'caring for youth with airborne precautions), gowns, eye protection, face '
        'shields, sharps containers, biohazard bags, and EPA-registered hospital '
        'disinfectants. The RN shall audit the inventory monthly and replenish '
        'before stock falls below a 30-day supply.',
        '<b>(h) Staff Training.</b> All staff complete <b>Bloodborne Pathogens</b> '
        'training annually and Infection Control training at hire and annually '
        'thereafter. The RN conducts the training and documents completion in the '
        'personnel file.',
    ]))

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
    story.append(Paragraph('<b>7.3 Facility-Based School Determination (Level III RTF vs. PRTF).</b>', s_h2))
    story.append(para(
        'A <b>facility-based school is a condition of licensure for Psychiatric Residential '
        'Treatment Facilities (PRTFs)</b> under 42 CFR 483.350-483.376 and the federal '
        ' Individuals with Disabilities Education Act (IDEA), but it is <b>not</b> required '
        'for a <b>Level III Residential Treatment Facility (Staff-Secure)</b> licensed '
        'under our staff-secure operating standards. <b>This facility is licensed as a Level III RTF '
        '(Staff-Secure), not as a PRTF.</b> Accordingly, this facility does not operate a '
        'facility-based school and is not required to do so under its current license; '
        'youth attend public school in the community per §7.1, with the facility '
        'providing transportation, after-school homework support, and IEP coordination.'
    ))
    story.append(para(
        '<b>Medicaid benefit distinction — CCP 8D-2 (RTS) vs CCP 8D-1 (PRTF).</b> The '
        'facility-based-school distinction parallels a Medicaid benefit-category '
        'distinction that is critical for billing compliance (see §1.2(g) and §10.9). '
        'This facility enrolls under <b>NC Medicaid Clinical Coverage Policy 8D-2 '
        '("Residential Treatment Services")</b> as a Level III (Residential Treatment '
        'High) provider; the Medicaid RTS per-diem reimburses only the clinical/treatment/'
        'milieu component and <b>excludes room and board</b>. A PRTF, by contrast, '
        'enrolls under <b>NC Medicaid Clinical Coverage Policy 8D-1 ("Psychiatric '
        'Residential Treatment Facilities for Children under the Age of 21")</b> as an '
        '<b>inpatient</b> facility benefit Under our operating standards, Subpart G; the PRTF '
        'per-diem <b>includes</b> the equivalent of room and board. The two benefit '
        'categories are mutually exclusive — a single facility cannot bill both 8D-1 and '
        '8D-2 for the same youth on the same day. The QP and Billing Coordinator shall '
        'verify at admission that the youth\'s authorization is for CCP 8D-2 Level III '
        'RTS (taxonomy 320800000X), not CCP 8D-1 PRTF.'
    ))
    story.append(para(
        '<b>If the facility elects to pursue PRTF designation</b> in the future, the '
        'facility shall, prior to that designation: (a) notify DHSR MHLC and apply for '
        'PRTF licensure under 42 CFR 483.350 et seq.; (b) establish a facility-based '
        'school meeting IDEA, NC State Board of Education, and accreditation standards; '
        '(c) employ or contract with licensed special-education teachers and a school '
        'administrator; (d) enter into a written agreement with the LEA for IEP '
        'implementation and educational records transfer; (e) document that the '
        'facility-based school is necessary because the youth\'s clinical acuity prevents '
        'safe participation in community school; (f) update this SOP and the Alliance '
        'Health provider agreement to reflect the PRTF designation; and (g) update '
        'NCTracks enrollment from CCP 8D-2 (RTS) to CCP 8D-1 (PRTF) and verify that '
        'the PRTF per-diem (including room-and-board-equivalent) is properly '
        'authorized. No youth shall be placed at this facility under a PRTF level of '
        'care until DHSR MHLC has issued the PRTF license and Alliance Health has '
        'authorized PRTF-level billing.'
    ))

    # ── SOP 8 ──────────────────────────────────────────────────────
    story.append(section_heading(8, 'Incident Reporting & Response (Rule 108 / IRIS)'))
    story.append(ref_line(anchor='§8'))
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
        'by the individual and actions taken. Reporting duties follow North Carolina '
        'mandatory reporting laws for child abuse and disabled adult abuse, and our '
        'operating standards. The completed incident report is filed separately from '
        'the clinical record per our records management policy.'
    ))

    # ── SOP 9 ──────────────────────────────────────────────────────
    story.append(section_heading(9, 'Facility, Safety, & Environmental Management'))
    story.append(ref_line(anchor='§9'))
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
        'Per the Level III Staff-Secure operating standards, <b>fire drills shall be '
        'conducted monthly AND tornado drills shall be conducted quarterly, with each '
        'drill conducted separately for EACH shift (day, evening, and overnight)</b> — '
        'i.e., 3 fire drills per month (one per shift) and 3 tornado drills per quarter '
        '(one per shift). Drills shall target evacuation under 3 minutes for fire drills '
        'and shall use the lowest interior safe room for tornado drills. Drill '
        'documentation on Form 5 (Environmental Safety Log) shall include: drill type '
        '(fire / tornado), shift (day / evening / overnight), date, start time, '
        'evacuation time (fire drills only), number of youth and staff participating, '
        'any deficiencies identified, corrective actions taken, and the shift '
        'supervisor\'s signature. Smoke detectors, fire extinguishers, sprinklers, and '
        'CO detectors are inspected monthly (staff) and annually (licensed contractors). '
        'Inspection records are maintained on Form 5 for a minimum of 3 years.'
    ))
    story.append(Paragraph('<b>9.3 Hazardous Materials.</b>', s_h2))
    story.append(para(
        'Cleaning chemicals, sharps, tools, and medications are stored in locked areas. '
        'Safety Data Sheets (SDS) are maintained and accessible. No weapons are permitted '
        'on facility grounds at any time.'
    ))
    story.append(Paragraph('<b>9.4 Two-Story &amp; Multi-Level Facility Requirements.</b>', s_h2))
    story.append(para(
        '<b>9.4(a) Applicability &amp; Licensing Notification.</b> This subsection applies '
        'to any facility operated by Well Spring Intervention LLC with two or more stories '
        'above grade, including any basement used for programmatic activities and any '
        'upper-floor youth bedroom. North Carolina family care / group home licensing '
        'rules generally restrict licensed structures to no more than two stories above '
        'grade when residents are housed above the first floor, and require that any '
        'resident housed on the second floor have two direct exterior means of egress. '
        'The Executive Director shall obtain <b>prior written approval</b> from NC DHSR '
        'before: (i) relocating youth bedrooms to a previously unused upper floor, '
        '(ii) increasing licensed capacity on an upper floor, (iii) converting a '
        'single-story operation to a two-story operation, or (iv) housing non-ambulatory '
        'youth on a second floor. Any such change also requires notification to the '
        'LME/MCO and may trigger a new construction inspection by the DHSR Construction '
        'Section. The QP shall retain the DHSR approval letter in the facility compliance '
        'binder for the duration of the license cycle and shall make it available to '
        'surveyors on request.'
    ))
    story.append(para(
        '<b>9.4(b) Means of Egress.</b> Each normally occupied story of the facility '
        'shall have at least two remotely located means of egress. Every second-floor '
        'sleeping room shall be provided with an approved emergency escape and rescue '
        'opening meeting the dimensions below, operable from the inside without keys, '
        'tools, or special knowledge: minimum net clear opening of <b>5.7 sq ft</b> '
        '(4.0 sq ft for grade-floor openings); minimum net clear opening height of '
        '<b>24 inches</b>; minimum net clear opening width of <b>20 inches</b>; and '
        'maximum sill height of <b>44 inches</b> above the floor. The secondary means '
        'of egress from a second-floor sleeping room may be satisfied by either (i) a '
        'second interior enclosed stairway discharging directly to grade, or (ii) an '
        'approved chain-style fire-escape ladder stored in each second-floor youth '
        'bedroom, deployable by staff only (never by youth). Stairways shall have '
        'handrails on both sides, a minimum 36-inch clear width, maximum 7¾-inch riser '
        'height, and minimum 10-inch tread depth for new construction. Stairway '
        'illumination with battery / emergency-backup lighting shall be installed at '
        'both the top and the bottom of every interior stair.'
    ))
    story.append(para(
        '<b>9.4(c) Fire Detection, Suppression &amp; Alarm — Per-Floor Requirements.</b> '
        'Smoke detectors shall be installed on <b>all levels</b> of the facility, '
        'including every sleeping room, outside each separate sleeping area within 21 ft '
        'of bedroom doors, and at least one detector on every story (basement, first '
        'floor, and every upper floor). All smoke detectors shall be interconnected so '
        'that actuation of one alarms all. Carbon monoxide (CO) detectors shall be '
        'installed on every floor containing a fuel-burning appliance or attached '
        'garage, and within 10 ft of each sleeping room; combination smoke/CO detectors '
        'may be used to satisfy both requirements in a single device. Automatic fire '
        'sprinklers are required for all Level III residential treatment facilities under the NC '
        'DHSR license condition and NFPA 13D/13R. Fire extinguishers (minimum 2A-10BC '
        'rating) shall be mounted on each level with a maximum travel distance of 75 ft '
        'from any point in the facility. All detectors, sprinklers, and extinguishers '
        'shall be inspected monthly by staff and annually by licensed contractors, with '
        'the per-floor results documented on the Environmental Safety Log (Form 5).'
    ))
    story.append(para(
        '<b>9.4(d) Per-Floor Staff Supervision.</b> When youth bedrooms are located on '
        'an upper floor, the awake overnight DCP shall be positioned to provide '
        'line-of-sight OR audible-monitoring coverage of the upper-floor hallway. The '
        '15-minute room-check requirement (§7) must be physically performed on <b>every '
        'floor where youth are sleeping</b> — a stair-climbed walk-through, not a '
        'call-up. Each per-floor walk-through shall be documented on the Night Watch Log '
        '(Form 1) Per-Floor Walk-Through Certification block. When only one awake '
        'overnight staff is on duty and youth sleep on multiple floors, the QP shall '
        'authorize one of the following: (i) addition of a second awake overnight staff '
        'member; (ii) relocation of all sleeping youth to the floor staffed by the '
        'awake overnight DCP; or (iii) approved baby-monitor / intercom coverage of the '
        'unstaffed floor with a documented response-time plan not to exceed 60 seconds. '
        'Stair safety gates shall be installed at both the top and the bottom of any '
        'staircase accessible to youth under 12 or to youth with documented elopement '
        'or suicidality risk; gates shall be locked at night with the key held by the '
        'awake overnight staff.'
    ))
    story.append(para(
        '<b>9.4(e) Window Fall Protection.</b> Where any second-floor youth-bedroom '
        'window sill is less than 24 inches above the finished floor, fall-protection '
        'devices (window guards or restrictors limiting the openable width to no more '
        'than 4 inches) shall be installed. Restrictors shall be releasable only by '
        'staff key and shall not defeat the emergency escape function of the window '
        '(i.e., the restrictor must be disengageable from the inside without tools in '
        'an emergency). Window restrictor function shall be checked monthly and '
        'documented on the Environmental Safety Log (Form 5) per-floor sub-table.'
    ))
    story.append(para(
        '<b>9.4(f) Drills — Vertical Evacuation.</b> Monthly fire drills shall include '
        '<b>full vertical evacuation</b> from all second-floor sleeping rooms to grade '
        '— drills that evacuate only the ground floor DO NOT satisfy this requirement. '
        'Total building evacuation time shall target under 3 minutes (per §9.2), with '
        'evacuation time recorded per floor on the Form 5 Monthly Fire Drills sub-table. '
        'Quarterly tornado drills shall use a shelter on the <b>lowest interior level</b> '
        '(basement preferred; if no basement, an interior ground-floor room with no '
        'exterior walls). A second-floor interior bathroom is <b>not</b> an approved '
        'tornado shelter. Annual lockdown drills shall secure all exterior doors and '
        'windows on every floor, including upper-floor windows visible from outside.'
    ))
    story.append(para(
        '<b>9.4(g) Bedroom Placement Policy.</b> When a two-story home has both '
        'ground-floor and upper-floor bedrooms, the QP shall assign bedrooms based on '
        'acuity, mobility, and elopement risk. Lower-acuity, lower-mobility, or younger '
        'youth shall be placed on the ground floor. Higher-acuity youth requiring closer '
        'staff proximity may be placed on the floor staffed by the awake overnight DCP. '
        'No youth bedroom shall be located in an attic or in a basement used for '
        'sleeping purposes. Bedroom placement decisions shall be documented in the '
        'youth\'s PCP and reviewed at each PCP revision.'
    ))
    story.append(para(
        '<b>9.4(h) Posted Evacuation Maps &amp; Signage.</b> Posted floor-plan '
        'evacuation maps shall be displayed on each floor showing two routes to grade, '
        'the designated outdoor meeting point, and the location of fire extinguishers, '
        'smoke/CO detectors, and fire-escape ladders. Stair hazard signage ("No running '
        'on stairs"; "Handrail required") shall be posted at the top and bottom of '
        'every interior stair. Maps and signage shall be reviewed at each monthly fire '
        'drill and updated whenever bedroom assignments change.'
    ))
    story.append(Paragraph('<b>9.5 Staff-Secure Physical-Plant Measures.</b>', s_h2))
    story.append(para(
        'As a <b>Level III Residential Treatment Facility — Staff Secure for Children and '
        'Adolescents</b> under our staff-secure operating standards, this facility shall maintain physical-'
        'plant and operational measures that provide line-of-sight or continuous-auditory '
        'supervision of all youth at all times, and that prevent elopement while preserving '
        'the youth\'s dignity and rights (per §1.7). Staff-secure measures do NOT include '
        'locked seclusion, hardware-restricted youth egress, or any building-code "detention '
        'and correction" occupancy classification. The following staff-secure measures are '
        'in place:'
    ))
    story.extend(bullets([
        '<b>(a) Controlled-Access Entry.</b> All exterior doors are kept locked from the '
        'outside. The main entry is equipped with a doorbell, video-intercom, and '
        'remote-buzz entry; staff visually verify identity before admitting any visitor. '
        'All other exterior doors are locked from the outside and equipped with '
        'exit-only panic hardware on the inside that sounds a localized chime when '
        'actuated (so staff are immediately alerted to any door opening).',
        '<b>(b) Delayed-Egress Hardware (where permitted).</b> Where local building and '
        'fire code permit, exterior exit doors serving youth-occupied areas may be '
        'equipped with delayed-egress hardware actuating 15-second delayed exit with a '
        'continuous audible alarm, allowing staff response time to redirect a youth in '
        'elopement attempt without impeding emergency egress (NFPA 101 §7.2.1.6.1). '
        'Delayed-egress hardware is inspected and tested monthly by staff and annually '
        'by a licensed contractor, with results documented on Form 5.',
        '<b>(c) Line-of-Sight Supervision.</b> Floor-plan configuration allows '
        'line-of-sight from the staff station to all common-area corridors and youth '
        'hallways; blind spots are covered by convex mirrors or CCTV cameras (CCTV '
        'covers common areas only — never bedrooms, bathrooms, or toileting areas). '
        'CCTV footage is retained 30 days and accessed only by the QP, Clinical '
        'Director, and Executive Director.',
        '<b>(d) Window Security.</b> All youth-accessible ground-floor windows are '
        'equipped with staff-key-releasable restrictors limiting the openable width to '
        '4 inches (per §9.4(e)). Second-floor youth-bedroom windows meet the same '
        'standard and additionally serve as emergency-escape openings per §9.4(b).',
        '<b>(e) Perimeter &amp; Outdoor Supervision.</b> The outdoor area is fenced or '
        'naturally bounded to a defined perimeter, with a single controlled-access '
        'point. Outdoor time is supervised at the 2:4 staff ratio at all times; '
        'one staff member remains within line-of-sight of the access point.',
        '<b>(f) Visitor Management.</b> All visitors sign a Visitor Log at entry, '
        'present photo ID, are screened against the youth\'s authorized-visitor list '
        '(maintained in the youth\'s clinical record and updated by the QP / guardian), '
        'and are escorted in common areas at all times. Visitors are never permitted '
        'in youth bedrooms. Visitor interactions are documented on the daily shift note.',
        '<b>(g) Contraband Search.</b> Youth belongings are searched at admission, '
        'upon return from any pass, and upon reasonable suspicion per §5.2 BSP and '
        'Form 2. Searches are conducted by staff of the same gender as the youth, '
        'with a second staff witness, in a private area, using the least intrusive '
        'method consistent with safety. Personal clothing is not removed. Body-cavity '
        'searches are prohibited and, if indicated, shall be performed by medical '
        'personnel at the emergency department per physician order.',
    ]))
    story.append(Paragraph('<b>9.6 Zoning Compliance.</b>', s_h2))
    story.append(para(
        'Prior to initial operation and at any change of physical location, the '
        'Executive Director shall obtain written confirmation from the local zoning '
        'authority that the proposed use (a Level III RTF serving up to nine youth) is '
        'a permitted use at the proposed address under the local zoning ordinance. '
        'Many NC municipalities classify group homes as a permitted residential use '
        'in residential districts under the federal Fair Housing Act Amendments (42 '
        'U.S.C. §3604(f)) and the NC Group Homes Act , but local '
        'ordinances may impose: (a) a minimum separation distance between group homes '
        '(commonly 1,000 feet, measured property-line to property-line); (b) a cap on '
        'the number of unrelated individuals sharing a dwelling; (c) off-street '
        'parking minimums (typically one space per staff member on the largest shift, '
        'plus one space per two youth); and (d) conditional-use permit requirements. '
        'The QP shall maintain the zoning approval letter and any conditional-use '
        'permit in the facility compliance binder, and shall report any zoning-related '
        'complaint or inquiry from neighbors to the Executive Director within 1 '
        'business day. Any material change to the facility (e.g., capacity increase, '
        'physical expansion, change in license category) requires fresh zoning '
        'verification before DHSR MHLC will process the license amendment.'
    ))
    story.append(Paragraph('<b>9.7 Disaster &amp; Emergency Plan (Fire, Tornado, Hurricane, Power Outage).</b>', s_h2))
    story.append(para(
        'The facility shall maintain a written <b>Disaster &amp; Emergency Plan</b> '
        'covering fire, tornado, hurricane, power outage, winter-weather event, '
        'utility failure (water, sewer, heat, gas), active-shooter / lockdown, '
        'bomb threat, and medical emergency. The plan shall be reviewed annually by '
        'the QP, posted in the staff area, and reviewed with all staff at orientation '
        'and annually thereafter. Drills shall be conducted per the cadence in §9.2 '
        'and §9.4(f).'
    ))
    story.append(para(
        '<b>9.7(0) Coordination with Local Emergency Management (OEM).</b> The QP shall '
        'coordinate the written Disaster &amp; Emergency Plan with the <b>local Office of '
        'Emergency Management (OEM)</b> for the county in which the facility is located '
        '(e.g., Wake County Emergency Management, Cumberland County Emergency Services, '
        'Durham County Emergency Management). Prior to initial licensure and annually '
        'thereafter, the QP shall: (a) submit a current copy of the facility Disaster &amp; '
        'Emergency Plan to the local OEM; (b) request and retain written verification '
        'from the local OEM acknowledging receipt and confirming coordination; (c) confirm '
        'the facility\'s 9-1-1 dispatch address, emergency-contact roster, and any '
        'special-needs registry enrollment for youth with mobility, sensory, or medical '
        'vulnerabilities; and (d) confirm the local OEM\'s role in the event of a '
        'community-wide evacuation order. The local OEM\'s written acknowledgment shall '
        'be retained in the facility compliance binder and made available to the DHSR '
        'MHLC Licensure &amp; Training Consultant and surveyors upon request. The North '
        'Carolina Emergency Management directory is available at '
        'https://www.ncdps.gov/our-organization/emergency-management.'
    ))
    story.extend(bullets([
        '<b>(a) Fire.</b> Evacuate immediately upon alarm. Headcount at the rally '
        'point (designated meeting area at the front sidewalk, ≥50 ft from the '
        'building). Call 911 from the rally point. Do not re-enter until the fire '
        'department issues all-clear. Monthly drills required (per §9.2).',
        '<b>(b) Tornado.</b> On a Tornado Watch, alert all staff and review shelter '
        'assignments. On a Tornado Warning, move all youth to the lowest interior '
        'room (basement preferred; if no basement, an interior ground-floor bathroom '
        'or hallway with no exterior walls). Turtle position against interior walls, '
        'away from windows. Bring flashlights, weather radio, and youth MARs. '
        'Quarterly drills required.',
        '<b>(c) Hurricane.</b> For facilities in NC counties subject to hurricane '
        'risk (all NC counties east of I-95 plus coastal counties), the QP shall '
        'monitor the National Hurricane Center advisories during the Atlantic '
        'hurricane season (June 1 – November 30). At Tropical Storm Warning or '
        'Hurricane Watch, the QP shall: secure outdoor furniture and projectiles; '
        'verify generator fuel (if applicable); stock 7-day supply of food, water '
        '(1 gallon per person per day), medications, batteries, and flashlights; '
        'verify youth and staff emergency-contact lists; and contact guardians '
        'regarding the storm plan. At Hurricane Warning, the QP shall coordinate '
        'with the LME/MCO and guardian regarding pre-storm evacuation or shelter-in-'
        'place decision; if evacuation is ordered, transport youth to the '
        'designated host facility (identified in the plan) and document the move '
        'on the IRIS system. After the storm, conduct a facility damage assessment '
        'before re-occupancy, document in the compliance binder, and notify DHSR '
        'MHLC if any structural damage occurred.',
        '<b>(d) Power Outage.</b> Distribute flashlights (one per staff member plus '
        'one per youth bedroom). Verify life-safety systems on battery backup '
        '(smoke detectors, fire alarm, security chimes). Discard refrigerated '
        'food per FDA guidance (4-hour rule for refrigerator; 24-48 hours for '
        'freezer if door stays closed). If power loss is expected to exceed 4 '
        'hours OR if indoor temperature drops below 65°F or rises above 80°F, '
        'initiate the Emergency Relocation Plan. Notify the utility company, '
        'document the outage start/end times, and notify the QP. Generator '
        'backup is recommended (and may be required by local code for facilities '
        'serving medically fragile youth); if installed, the generator shall be '
        'tested monthly under load.',
        '<b>(e) System Failure (heat, water, sewer, gas).</b> Per Protocol 19: '
        'heat loss exceeding 4 hours OR water loss exceeding 8 hours OR sewer '
        'backup OR gas leak (evacuate immediately and call 911) shall trigger '
        'the Emergency Relocation Plan to the designated host facility.',
        '<b>(f) Lockdown (active shooter / external threat).</b> Per Protocol 19: '
        'secure all exterior doors and windows, pull window blinds, silence '
        'phones, hide in the designated safe room away from windows and doors, '
        'do not open for anyone but law enforcement. Annual lockdown drills '
        'required. Staff shall familiarize themselves with the Run / Hide / Fight '
        'protocol and the facility\'s designated safe rooms at orientation.',
        '<b>(g) Emergency Relocation Plan.</b> The written plan identifies a '
        'primary and a secondary host facility (typically another licensed '
        'group home or a hotel with prior arrangement), transportation '
        'arrangements (facility vehicle + staff vehicles + ambulance for '
        'medically fragile youth), medication transport (locked medication box '
        'transported by the RN or QP), youth-identification packets (photo ID, '
        'Medicaid card, allergy / medication list), guardian-notification '
        'protocol (within 1 hour of relocation decision), and DHSR / LME-MCO '
        'notification (within 24 hours). The QP shall maintain the host-facility '
        'agreement letters in the compliance binder.',
    ]))
    story.append(para(
        '<i>Web sources for §9.4–§9.7 regulatory citations (verified July 2026):</i><br/>'
        '&bull; <b>our operating standards (NC Administrative Code Title 10A Ch. 27 Subchapter G — Mental Health/DD/SA)</b> — '
        'http://reports.oah.state.nc.us/ncac/title%2010a%20-%20health%20and%20human%20services/chapter%2027%20-%20mental%20health,%20community%20facilities%20and%20services/subchapter%20g/subchapter%20g%20rules.pdf<br/>'
        '&bull; <b>NC OSFM 2012 NC Building Code Amendments §425 (Board &amp; Care — each occupied story two means of egress; smoke detectors on all levels)</b> — '
        'https://www.ncosfm.gov/2012-north-carolina-building-code-chapters1-1534-end-amendments/open<br/>'
        '&bull; <b>NC Fire Code 2024 Chapter 10 Means of Egress</b> — '
        'https://up.codes/viewer/north_carolina/ifc-2021/chapter/10/means-of-egress<br/>'
        '&bull; <b>NC IFC 2021 Chapter 4 Emergency Planning &amp; Preparedness (§401.6 Evacuation Drills)</b> — '
        'https://up.codes/viewer/north_carolina/ifc-2021/chapter/4/emergency-planning-and-preparedness<br/>'
        '&bull; <b>IBC 2021 §1030 Emergency Escape &amp; Rescue Openings (5.7 sq ft / 24 in / 20 in / 44 in sill)</b> — '
        'https://codes.iccsafe.org/content/IBC2021P2/chapter-10-means-of-egress<br/>'
        '&bull; <b>Family Care Home Fire Safety (NC DHSR)</b> — '
        'https://info.ncdhhs.gov/dhsr/rules/2025/AdultCareHomeFamilyCareHomeRules/feb/10A_NCAC_13F_.0309.pdf<br/>'
        '&bull; <b>Adult Care Home Fire Safety (NC DHSR)</b> — '
        'https://info.ncdhhs.gov/dhsr/rules/2025/AdultCareHomeFamilyCareHomeRules/feb/10A_NCAC_13G_.0316.pdf<br/>'
        '&bull; <b>NC DHSR ACLS — License a Family Care Home (2-6 Beds)</b> — '
        'https://info.ncdhhs.gov/dhsr/acls/flofch.html<br/>'
        '&bull; <b>NC DHSR ACLS Fire Safety &amp; Emergency Preparedness Training (PDF)</b> — '
        'https://info.ncdhhs.gov/dhsr/acls/training/pdf/FireSafetyEmergency-PreparednessRegulations-NCAdultCareHomes.pdf<br/>'
        '&bull; <b>NC Residential Smoke &amp; CO Alarm Requirements (City of Durham summary of NC code)</b> — '
        'https://www.durhamnc.gov/DocumentCenter/View/1012/Residential-Smoke-AlarmsCarbon-Monoxide-Alarms-PDF<br/>'
        '&bull; <b>Orange County NC Smoke Alarms (NFPA 72 — every level, every bedroom)</b> — '
        'https://www.orangecountync.gov/2391/Smoke-Alarms<br/>'
        '&bull; <b>NFPA 101 Life Safety Code — Board &amp; Care Occupancies (§32/§33)</b> — '
        'https://www.nfpa.org/codes-and-standards/nfpa-101-standard-development/101<br/>'
        '&bull; <b>NCSL Carbon Monoxide Detector Installation Statutes by State</b> — '
        'https://www.ncsl.org/environment-and-natural-resources/carbon-monoxide-detector-installation-statutes<br/>'
        '&bull; <b>NC Family Care Home structure rule — no more than 2 stories; second-floor residents require two direct exterior egress</b> — '
        'https://ncbold.com/license/10134.'
    ))

    # ── SOP 10 ─────────────────────────────────────────────────────
    story.append(section_heading(10, 'Medicaid Billing, Documentation Compliance & Record Management'))
    story.append(ref_line(
        'NC Medicaid CCP 8D-2; CMS Documentation Guidelines; RMDM Chapter 6; state law Ch. 66 Art. 40 (NC UETA); E-SIGN Act (15 U.S.C. § 7001 et seq.)',
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
        '</b> and the federal E-SIGN Act (15 U.S.C. '
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
        'Security Rule (45 CFR Part 164 Subpart C), 42 CFR Part 2, and state law '
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
        'The program bills Medicaid on a daily per diem basis under <b>NC Medicaid '
        'Clinical Coverage Policy 8D-2 (Residential Treatment Services — Level III)</b> '
        'via NCTracks. <b>The Medicaid RTS per-diem covers ONLY the clinical/treatment/'
        'milieu component</b> (assessments, PCP, individual/family/group therapy, '
        'behavioral interventions, 24-hour supervision, medication administration, '
        'crisis response, and related clinical services). <b>Room and board are '
        'excluded from the Medicaid RTS benefit category</b> per CCP 8D-2 §1.0(c) '
        'and §1.2(g) of this Manual; the beneficiary\'s lodging and meals must be '
        'funded through a non-Medicaid source (state/local social-services funds, '
        'Title IV-E foster care maintenance, SSI/ISS, or other third-party resources). '
        'The QP and Billing Coordinator shall verify at admission — and re-verify at '
        'each PCP review — that an identified non-Medicaid room-and-board funding '
        'source is documented in the youth\'s clinical record. <b>Under no '
        'circumstances shall room-and-board costs be billed to the Medicaid RTS per-'
        'diem, to Alliance Health, or to NCTracks.</b> Suspected improper billing of '
        'room-and-board costs to Medicaid shall be reported immediately to the '
        'Compliance Officer per §1.3 and shall be corrected via NCTracks claim '
        'adjustment within 30 calendar days of discovery.'
    ))
    story.append(para(
        'Billing is suspended for any day the youth is hospitalized, detained, or on a '
        'home pass exceeding <b>24 consecutive hours</b>. The Home Pass &amp; Medicaid '
        'Billing Exclusion Tracker (Form 4) documents all absences and corresponding '
        'billing action. Billing errors are corrected promptly and reported to the '
        'LME/MCO as required. Records are released only with a signed ROI or as '
        'required by law, court order, or regulatory audit.'
    ))
    story.append(Paragraph('<b>10.10 Mock Client Chart &amp; Licensure Survey Readiness.</b>', s_h2))
    story.append(para(
        'Prior to the on-site <b>DHSR MHLC Licensure Survey</b> (and prior to any '
        're-licensure or accreditation survey), the QP shall prepare and assemble a '
        'complete <b>Mock Client Chart</b> representative of a typical youth served by '
        'the facility. The Mock Client Chart shall be made available to the surveyor on '
        'the first day of the on-site survey and shall demonstrate the facility\'s '
        'documentation practices across the full continuum of care. The Mock Client '
        'Chart shall include the following elements (cross-referenced to the applicable '
        'SOP section and Form number in this Manual):'
    ))
    story.extend(bullets([
        '<b>Identification Face Sheet</b> — youth name, DOB, Medicaid ID, address, '
        'guardian name and contact, primary language, admission date, assigned QP and '
        'psychiatrist (per §3.2, §3.3).',
        '<b>Emergency Information Sheet</b> — emergency contacts, allergies, primary '
        'physician, preferred hospital, pharmacy, and code-status (if applicable).',
        '<b>Consent for Treatment</b> — signed by guardian (and youth if age-appropriate), '
        'including consent for medication, transportation, photography, and Release of '
        'Information (ROI) (per §3.2).',
        '<b>Comprehensive Clinical Assessment (CCA)</b> — completed by a licensed '
        'professional within the required timeframe, including DSM-5-TR/ICD-10 diagnoses, '
        'clinical formulation, and recommended level of care (per §4.1).',
        '<b>Person-Centered Plan (PCP)</b> — signed by all participants, with measurable '
        'goals, objectives, interventions, and assigned responsible staff; reviewed every '
        '90 days (per §4.2, §4.3).',
        '<b>Progress Notes / Service Notes</b> — daily shift notes, weekly clinical '
        'progress notes, group notes, and any 1:1 service notes (per §10.1, §10.2, §10.3).',
        '<b>Medication Orders &amp; Medication Administration Record (MAR)</b> — signed '
        'physician medication orders, current MAR showing all PRN and scheduled '
        'administrations, and any medication-incident reports (per §6.3, §6.4).',
        '<b>Behavior Support Plan (BSP)</b> — if applicable, with proactive strategies, '
        'replacement skills, de-escalation steps, and crisis responses (per §5.3).',
        '<b>Restrictive-Intervention Records</b> — if applicable, all restraint, seclusion, '
        'and isolation time-out documentation with post-incident medical monitoring, '
        'guardian notification, and IRIS reports (per §5.4, §8).',
        '<b>Health Records</b> — pre-admission physical exam report (within 90 days prior '
        'to admission per §6.1), immunization record, TB screening, dental and vision '
        'records, and annual exam documentation.',
        '<b>Activities Log</b> — weekly group activities participation showing the '
        '14-hours-per-week minimum per §5.5.',
        '<b>Grievance Records</b> — if applicable, any grievances filed by or on behalf of '
        'the youth, with documentation of acknowledgement, investigation, response, and '
        'resolution per §1.7(c).',
        '<b>Disclosures &amp; Accounting of Disclosures</b> — Form 9 completed for any '
        'PHI disclosures during the chart period (per §11.4).',
        '<b>Discharge / Transition Plan</b> — initiated at admission, reviewed every 30 '
        'days, with projected discharge date and identified next placement (per §3.4).',
    ]))
    story.append(para(
        'In addition to the Mock Client Chart, the QP shall prepare and make available to '
        'the surveyor: (a) <b>Facility Photographs</b> — labeled photographs of each room '
        'in the facility (exterior, common areas, kitchen, youth bedrooms, staff sleeping '
        'areas if applicable, bathrooms, medication storage area, time-out room if '
        'applicable, exits, fire-safety equipment, and outdoor recreation area), with each '
        'photograph labeled to identify the room; (b) <b>all policies and procedures '
        'referenced in this Manual</b>; (c) <b>all personnel files</b> for current staff '
        'with background-check, training, CEU, and instructor-credential documentation per '
        '§2; (d) <b>all disaster and emergency plans</b> including OEM coordination per '
        '§9.7; (e) <b>the MH Licensure P&amp;P Worksheet</b> per §1.2(f); and (f) <b>the '
        'compliance binder</b> containing all corporate, financial, insurance, and '
        'licensing documents per §1.8. The QP shall conduct a <b>mock survey</b> no fewer '
        'than 30 days prior to the scheduled DHSR MHLC survey, identify and correct any '
        'deficiencies, and document the mock-survey findings and corrective actions.'
    ))

    # ── SOP 11 ─────────────────────────────────────────────────────
    story.append(section_heading(11, 'Privacy, Security, Confidentiality & Access to Records'))
    story.append(ref_line(
        anchor='§11',
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
        'Compliance is required with our resident rights commitments, our operating standards, '
        '<b>42 CFR Part 2</b> (Confidentiality of Alcohol and Drug Abuse Patient '
        'Records), and state law on AIDS/confidential conditions. <b>Substance Use '
        'Information</b>: requires the individual\'s written authorization before '
        'disclosure to other treatment providers (unless court order or allowable '
        'exception per 42 CFR Part 2). Absent written consent, entities must redact '
        'all identifying information from alcohol/drug records when sharing. '
        '<b>Care Coordination Exceptions</b>: Under our operating standards, '
        'entities may share confidential information for coordination of care/treatment '
        'without written consent; however, '
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
        're-disclosure is prohibited except as permitted under our resident rights commitments. '
        'Releases/disclosures from external entities must be contained in the '
        'individual\'s service record.'
    ))
    story.append(Paragraph('<b>11.5 Individual Access to Service Records.</b>', s_h2))
    story.append(para(
        'Individuals and Legally Responsible Persons (LRPs) have the right to access '
        'information contained in their service record, per state law and DHHS provisions. '
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
        'addresses: (a) the organization\'s mission, vision, and values statements (§1.1); '
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
        'consistent with the organization\'s charitable solicitation registration.'
    ))
    story.append(Paragraph('<b>12.2 Input from Persons Served and Other Stakeholders.</b>', s_h2))
    story.append(para(
        'Conformance to CARF CYS Section 1.D is established through the written <b>Stakeholder '
        'Input Plan</b> maintained by the QP. The plan describes at least four methods for '
        'gathering input from persons served, their families/LRP, personnel, referral sources, '
        'payers, and the community, including: (i) quarterly youth satisfaction surveys '
        '(developmentally appropriate, anonymous, available in English and the youth\'s '
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
        'coordinated with the organization\'s legal counsel. The Compliance Officer maintains '
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
        '12, 14–16) is established through the facility\'s existing §9 Facility, Safety, and '
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
        'minimum the organization\'s mission and values; person-centered and '
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
        'facility\'s existing Resident Rights policies as documented in the Resident '
        'Handbook (companion document) and in §3, §5, §6, §8, §9, and §11 of this Manual. '
        'At minimum, written policies address: (a) the right to dignity, privacy, '
        'humane care, and freedom from discrimination; (b) the right to participate in '
        'service planning and to refuse services (with documented consequences of refusal); '
        '(c) the right to confidential communication and visitation; (d) the right to '
        'access one\'s own record per §11.5; (e) the right to file a grievance without '
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
        'plan identifies the organization\'s performance indicators, organized into at '
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
        'used and the platform\'s compliance with applicable privacy and security '
        'law (HIPAA, 42 CFR Part 2, HITECH) per §11; (c) informed consent for '
        'telehealth services, including documentation in the clinical record of the '
        'youth\'s and family/LRP\'s understanding of the benefits, risks, '
        'limitations, and alternatives; (d) personnel training and competency '
        'verification for telehealth service delivery; (e) procedures for '
        'technology failure, including fallback to in-person or telephone contact; '
        '(f) procedures for ensuring the youth\'s privacy during telehealth '
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
        'Manual Sections 3–5 standards and this Manual\'s SOPs, Protocols, and '
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
        'Cross-reference',
        [
            'This §12 framework operates in conjunction with §1.2(a) (CARF designation), §1.4(a) (QP compliance reporting), §1.8 (Governing Body), §2 (Workforce), §3 (Admissions/Discharge), §4 (Clinical Services), §5 (Behavioral Management), §6 (Health/Medication), §7 (Education), §8 (Incident Reporting), §9 (Facility/Safety), §10 (Medicaid Documentation), §11 (Privacy/Records), and the Form 12 (CARF QIP Tracker) in Part 3. The QP shall present this §12 framework to CARF surveyors as the primary evidence of organizational readiness for the Inaugural Accreditation survey.',
        ]
    ))

    return story
