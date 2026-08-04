"""
audit_findings.py — Single source of truth for the Well Spring Intervention
SOP Manual v2.22 compliance audit against 10A NCAC 27G .1700 + core rules.

Each finding is a dict with:
  id          — F-001 etc. (gaps) or M-001 etc. (met/exceeds)
  rule        — Rule subsection citation (e.g. ".1701(a)", ".0209(f)")
  rule_title  — Short rule title (e.g. "SCOPE — Free-standing facility")
  rule_text   — Verbatim rule text quoted from 10A NCAC 27G source
  sop_loc     — SOP Manual v2.22 location (e.g. "§2.1", "Protocol 13")
  sop_quote   — Quote or paraphrase of what the SOP currently says
  status      — Met / Met-Exceeds / Partial / Gap / Contradicts / N/A
  severity    — Critical / High / Medium / Low / Info
  strip_flag  — Y/N — does this finding involve statutory text to strip from public edition?
  strip_note  — specific text to strip + plain-language replacement
  finding     — Detailed finding narrative (≥150 words for High+)
  remediation — Concrete corrective action with target revision

This module is consumed by:
  - generate_audit_pdf.py  → audit report PDF (ReportLab)
  - generate_audit_xlsx.py → crosswalk matrix XLSX (openpyxl)
"""

# ─── Severity legend ────────────────────────────────────────────────────────
SEVERITY_LEGEND = {
    "Critical": "License-blocking, safety risk, or Medicaid fraud exposure. Must be remediated before next survey.",
    "High":     "Direct rule violation with regulatory or billing impact. Remediate in next revision.",
    "Medium":   "Partial compliance or documentation gap. Remediate within 1-2 revision cycles.",
    "Low":      "Clarification or stylistic inconsistency. Remediate opportunistically.",
    "Info":     "Confirmed compliance or note. No action required.",
}

STATUS_LEGEND = {
    "Met":         "SOP addresses the rule fully and accurately.",
    "Met-Exceeds": "SOP addresses the rule and imposes a stricter standard (defensible).",
    "Partial":     "SOP addresses the rule but is missing one or more elements.",
    "Gap":         "SOP does not address the rule.",
    "Contradicts": "SOP states something inconsistent with the rule (in either direction).",
    "N/A":         "Rule does not apply to this facility type.",
}

# ─── Findings ───────────────────────────────────────────────────────────────
FINDINGS = [
    # ═══════════════════════════════════════════════════════════════════════
    # SECTION A — .1700 Residential Treatment Staff Secure
    # ═══════════════════════════════════════════════════════════════════════

    # .1701 SCOPE
    dict(
        id="M-001",
        rule=".1701(a)",
        rule_title="SCOPE — Free-standing residential facility, not primary residence",
        rule_text='"A residential treatment staff secure facility for children or adolescents is one that is a free-standing residential facility that provides intensive, active therapeutic treatment and interventions within a system of care approach. It shall not be the primary residence of an individual who is not a client of the facility."',
        sop_loc="§1.2(g)(i) — NC Medicaid RTS Taxonomy: Setting Type",
        sop_quote='The facility is licensed under state mental health law by NC DHSR MHLC — not under state law Chapter 131D by DSS, which licenses foster-care family homes. The facility therefore does not, and cannot, operate as a family-home placement for any youth at any time.',
        status="Met",
        severity="Info",
        strip_flag="Y",
        strip_note='Strip "NC DHSR MHLC", "state law Chapter 131D", "DSS" citations; replace with "licensed under the applicable state mental health authority — not under foster-care licensing — and therefore does not operate as a family-home placement."',
        finding=(
            "The SOP Manual v2.22 correctly characterizes the facility as a free-standing residential treatment facility that is not a family-home placement. "
            "Section 1.2(g)(i) explicitly cross-references .1701(a) and explains the program-setting-only taxonomy under NC Medicaid Clinical Coverage Policy 8D-2. "
            "The SOP quote tracks the rule text verbatim in substance, and the operational implementation — admission criteria in §3.1 exclude family-home placements, "
            "staffing ratios in §2.1 reflect a 24/7 program setting, and discharge planning in §3.4 transitions youth to less-restrictive settings rather than returning them to a primary residence at the facility — "
            "is consistent with the rule. No corrective action required. The only strip-flag work is removing the statutory citations from the public edition per the user's legislation-stripping directive."
        ),
        remediation="No operational change. Strip statutory citations in v2.23 per Section E of the audit report.",
    ),
    dict(
        id="M-002",
        rule=".1701(b)",
        rule_title="SCOPE — Staff secure means awake during sleep hours, continuous supervision per .1704",
        rule_text='"Staff secure means staff are required to be awake during client sleep hours and supervision shall be continuous as set forth in Rule .1704 of this Section."',
        sop_loc="§2.1 Staffing Ratios — Staff-Secure Level III; Protocol 13; Protocol 22(e) DCP Awake Overnight",
        sop_quote='Under .1700, this Level III Staff-Secure facility shall maintain a minimum of two (2) staff members on duty and awake at all times for every one to four (1-4) children in residence, on every shift including the overnight shift. … Sleeping is strictly prohibited. 15-minute visual room checks are documented on the Night Watch Log (Form 1).',
        status="Met-Exceeds",
        severity="Info",
        strip_flag="Y",
        strip_note='Strip ".1700" citation; replace with "Under the Level III Staff-Secure operating standards, this facility shall maintain…"',
        finding=(
            "The SOP exceeds the .1701(b) minimum by requiring BOTH overnight staff to be awake for 1-4 youth, whereas .1704(c)(1) only requires ONE of the two present staff to be awake. "
            "This stricter standard is defensible because it provides redundancy: if one overnight staff becomes incapacitated or distracted, a second awake staff member remains available to respond. "
            "The continuous-supervision requirement is operationally implemented via 15-minute line-of-sight room checks documented on Form 1 (Shift Change & Awake Night Watch Log), with a Per-Floor Walk-Through Certification sub-table for two-story facilities. "
            "Protocol 22(e) codifies the awake overnight DCP schedule from 11p-7a with specific time-blocked room-check cadence. No corrective action required."
        ),
        remediation="No operational change. Strip statutory citations in v2.23.",
    ),
    dict(
        id="M-003",
        rule=".1701(c)",
        rule_title="SCOPE — Population served (children/adolescents with MI/ED/SUD; not inpatient)",
        rule_text='"The population served shall be children or adolescents who have a primary diagnosis of mental illness, emotional disturbance or substance-related disorders; and may also have co-occurring disorders including developmental disabilities. These children or adolescents shall not meet criteria for inpatient psychiatric services."',
        sop_loc="§3.1 Admission Criteria; §1.1 Mission Statement",
        sop_quote='The program serves youth with a primary mental health or behavioral diagnosis requiring supervised living, who are medically stable, and whose clinical needs can be safely met in a Level III Staff-Secure setting. Exclusions include active psychosis requiring Involuntary Commitment (IVC), medical instability, or fire-setting that cannot be safely managed.',
        status="Met",
        severity="Info",
        strip_flag="Y",
        strip_note='Strip "Involuntary Commitment (IVC)" legal term; replace with "acute psychiatric crisis requiring inpatient hospitalization."',
        finding=(
            "Admission criteria in §3.1 directly track .1701(c): primary mental health or behavioral diagnosis, medical stability (proxy for not meeting inpatient criteria), "
            "and explicit exclusion of active psychosis requiring involuntary commitment. The population-served statement in §1.1 (children and adolescents with mental health and behavioral challenges) "
            "aligns with the rule. The exclusion list also appropriately addresses fire-setting and medical instability, which are operational safety exclusions rather than rule violations. "
            "Co-occurring developmental disabilities are not explicitly addressed in §3.1; the QP should consider adding a sentence acknowledging that youth with co-occurring IDD may be admitted "
            "provided their clinical needs can be met in a Level III Staff-Secure setting, mirroring the rule's permissive language."
        ),
        remediation="Optional v2.23 enhancement: add co-occurring IDD acknowledgment sentence to §3.1.",
    ),
    dict(
        id="M-004",
        rule=".1701(d)",
        rule_title="SCOPE — Removal from home + staff-secure setting required",
        rule_text='The children or adolescents served shall require: (1) removal from home to a community-based residential setting in order to facilitate treatment; and (2) treatment in a staff secure setting.',
        sop_loc="§3.1 Admission Criteria",
        sop_quote='The program serves youth with a primary mental health or behavioral diagnosis requiring supervised living, who are medically stable, and whose clinical needs can be safely met in a Level III Staff-Secure setting.',
        status="Met",
        severity="Info",
        strip_flag="N",
        strip_note="No statutory citation to strip; rule-text language is operational.",
        finding=(
            "§3.1 implicitly requires both elements: 'requiring supervised living' addresses the removal-from-home requirement, and 'Level III Staff-Secure setting' addresses the staff-secure requirement. "
            "The QP documents the admission decision in the clinical record per §3.1, including verification that the youth's clinical needs cannot be safely met in a less restrictive setting. "
            "However, the SOP does not explicitly use the phrase 'removal from home' or 'community-based residential setting' from the rule. To improve audit defensibility, the QP should consider "
            "adding an explicit admission criterion mirroring the rule's two-prong test, so a surveyor can immediately verify both elements are documented at admission."
        ),
        remediation="Optional v2.23 enhancement: add explicit two-prong admission criterion to §3.1 mirroring .1701(d)(1)-(2).",
    ),
    dict(
        id="M-005",
        rule=".1701(e)",
        rule_title="SCOPE — Services designed: supervision, behavior minimization, safety, adaptive functioning, step-down",
        rule_text=(
            'Services shall be designed to: (1) include individualized supervision and structure of daily living; '
            '(2) minimize the occurrence of behaviors related to functional deficits; '
            '(3) ensure safety and deescalate out of control behaviors including frequent crisis management with or without physical restraint; '
            '(4) assist the child or adolescent in the acquisition of adaptive functioning in self-control, communication, social and recreational skills; and '
            '(5) support the child or adolescent in gaining the skills needed to step-down to a less intensive treatment setting.'
        ),
        sop_loc="§1.1 Mission; §5.5 Activities Program (14 hrs/wk); §5.3 BSP; §4.3 PCP; §3.4 Discharge & Transition",
        sop_quote='§5.5 provides each youth with a documented activities program of no fewer than 14 hours per week of planned group activities that promote socialization, physical activity, and creative expression. §5.3 BSP includes proactive strategies, replacement skills, de-escalation steps, and crisis responses.',
        status="Met-Exceeds",
        severity="Info",
        strip_flag="Y",
        strip_note='Strip ".1701(e)" and ".1700" citations from §5.5; replace with "Per the Level III Staff-Secure operating standards…".',
        finding=(
            "All five .1701(e) service-design elements are operationalized in the SOP: "
            "(e)(1) individualized supervision and structure of daily living is implemented via Protocol 22 (Daily Workflow Schedules for All Personnel) and the 2:4 staffing ratio; "
            "(e)(2) minimizing behaviors related to functional deficits is implemented via §5.2 Behavioral Support Plan based on Functional Behavioral Assessment; "
            "(e)(3) ensuring safety and de-escalating out-of-control behaviors is implemented via §5.3 Restraint policy, Protocol 4 (Behavioral Crisis & Restraint Protocol), and Protocol 8 (Suicide Risk); "
            "(e)(4) acquisition of adaptive functioning in self-control, communication, social and recreational skills is implemented via §5.5 Activities Program (14 hrs/wk minimum, exceeding any rule minimum) with explicit activity categories (physical, creative, socialization/life-skills, community integration); "
            "(e)(5) step-down to less intensive setting is implemented via §3.4 Discharge & Transition (planning initiated at admission, 30-day reviews, trial home visits). "
            "No corrective action required."
        ),
        remediation="No operational change. Strip statutory citations in v2.23.",
    ),
    dict(
        id="M-006",
        rule=".1701(f)",
        rule_title="SCOPE — Coordination with system of care",
        rule_text='"The residential treatment staff secure facility shall coordinate with other individuals and agencies within the child or adolescent\'s system of care."',
        sop_loc="§1.4 Organizational Structure; §4.3 PCP Development; §7.3 Facility-Based School Determination; Protocol 15 Educational Coordination",
        sop_quote='§4.3: Within 30 calendar days of admission, the QP facilitates a PCP meeting including the youth, guardian, LME/MCO representative, and other supports identified by the family.',
        status="Met",
        severity="Info",
        strip_flag="Y",
        strip_note='Strip "LME/MCO" abbreviation; replace with "the regional managed care organization representative."',
        finding=(
            "System-of-care coordination is implemented through multiple SOP mechanisms: PCP meetings with guardian, LME/MCO representative, and family-identified supports (§4.3); "
            "educational coordination with the LEA McKinney-Vento liaison or EC Director (Protocol 15); family engagement and visitation (Protocol 16); "
            "discharge planning that establishes community linkages (Protocol 17); and DSS notification for abuse allegations (Protocol 3). "
            "The QP is the designated care-coordination lead per §1.4. No corrective action required."
        ),
        remediation="No operational change. Strip statutory abbreviations in v2.23.",
    ),

    # .1702 QP REQUIREMENTS
    dict(
        id="M-007",
        rule=".1702(a)",
        rule_title="QP REQUIREMENTS — At least one QP direct care staff + 2 years direct client care experience",
        rule_text='"Each facility shall utilize at least one direct care staff who meets the requirements of a qualified professional as set forth in 10A NCAC 27G .0104(18). In addition, this qualified professional shall have two years of direct client care experience."',
        sop_loc="§1.4(b) QP Credentialing Requirements",
        sop_quote='Pathway 1: master\'s degree in a human services field plus a recognized NC credential plus at least one year of full-time, post-master\'s supervised MH/DD/SA experience. Pathway 2: bachelor\'s degree in a human services field plus two years of full-time, pre- or post-bachelor\'s supervised MH/DD/SA experience.',
        status="Partial",
        severity="Medium",
        strip_flag="Y",
        strip_note='Strip "10A NCAC 27G .0104(18)" citation (note: rule cross-references .0104(18) "Psychiatrist" but appears to intend .0104(21) "Qualified professional" — see F-011); replace with "meets the qualified professional definition per facility policy." Also strip "NC credential" specifics.',
        finding=(
            "The SOP correctly defines the QP pathways per .0104(21), but the rule's cross-reference to .0104(18) is a likely typographical error in the rule itself — .0104(18) is the 'Psychiatrist' definition, not the 'Qualified Professional' definition. "
            "The substantive QP definition is at .0104(21), which the SOP correctly follows. The SOP's Pathway 1 requires 1 year of post-master's supervised experience, but .1702(a) additionally requires 2 years of direct client care experience "
            "for the QP serving in the .1702 role. The SOP does not explicitly state the 2-year direct client care experience requirement on top of the .0104(21) pathway requirements. This is a Medium severity gap: a Pathway 1 QP with only 1 year of post-master's experience "
            "would satisfy .0104(21)(b) but not .1702(a)'s additional 2-year requirement. The QP should add an explicit sentence to §1.4(b) confirming that the designated .1702 QP also has 2 years of direct client care experience."
        ),
        remediation="v2.23: Add to §1.4(b) an explicit statement that the designated facility QP also meets the .1702(a) 2-year direct client care experience requirement (in addition to the .0104(21) pathway).",
    ),
    dict(
        id="M-008",
        rule=".1702(b)-(c)",
        rule_title="QP REQUIREMENTS — 10 hrs/wk (≤5 beds) or 32 hrs/wk (≥6 beds); 70% during awake hours",
        rule_text=(
            '(b) For each facility of five or less beds: (1) the qualified professional specified in Paragraph (a) of this Rule shall perform clinical and administrative responsibilities a minimum of 10 hours each week; and (2) 70% of the time shall occur when children or adolescents are awake and present in the facility. '
            '(c) For each facility of six or more beds: (1) the qualified professional specified in Paragraph (a) of this Rule shall perform clinical and administrative responsibilities a minimum of 32 hours each week; and (2) 70% of the time shall occur when children or adolescents are awake and present in the facility.'
        ),
        sop_loc="§1.4 Organizational Structure; Protocol 22(a) QP Daily Workflow",
        sop_quote='Protocol 22(a): QP on-site 7:00 AM to 9:30 PM float schedule, on-call 24/7/365. §1.4: An On-Call QP is available 24/7/365 for clinical decision-making.',
        status="Met-Exceeds",
        severity="Info",
        strip_flag="N",
        strip_note="No statutory citation to strip; this is an operational standard.",
        finding=(
            "The facility is licensed for up to 9 youth (per §2.1 note), placing it in the .1702(c) 'six or more beds' category requiring 32 hours of QP time per week with 70% during awake hours. "
            "Protocol 22(a) shows the QP on-site from 7:00 AM to 9:30 PM (14.5 hours) on weekdays, plus on-call coverage 24/7/365. At 14.5 hrs/day × 5 days = 72.5 hrs/wk on-site, the SOP vastly exceeds the 32-hour minimum. "
            "All on-site hours occur during awake youth hours (7a-9:30p), exceeding the 70% requirement. The QP also provides clinical services during weekend on-call rotations. "
            "No corrective action required. The SOP should consider adding an explicit statement that the QP meets/exceeds the 32-hour weekly minimum and 70% awake-hours requirement for documentation clarity."
        ),
        remediation="Optional v2.23: add explicit weekly hour and awake-% statement to §1.4 or Protocol 22(a).",
    ),
    dict(
        id="M-009",
        rule=".1702(d)(1)-(6)",
        rule_title="QP REQUIREMENTS — Written policies specifying QP clinical/admin responsibilities (6 items)",
        rule_text=(
            'The governing body responsible for each facility shall develop and implement written policies that specify the clinical and administrative responsibilities of its qualified professional(s). At a minimum these policies shall include: '
            '(1) supervision of its associate professional(s) as set forth in Rule .1703 of this Section; '
            '(2) oversight of emergencies; '
            '(3) provision of direct psychoeducational services to children or adolescents; '
            '(4) participation in treatment planning meetings; '
            '(5) coordination of each child or adolescent\'s treatment plan; and '
            '(6) provision of basic case management functions.'
        ),
        sop_loc="§1.4 Organizational Structure; §1.4(a) QP Compliance Reporting to the Clinical Director",
        sop_quote='§1.4: The QP is responsible for scheduling clinical services, assessments, PCPs, and day-to-day supervision of APs and DCPs according to the direction of the Clinical Director. §1.4(a): monthly IRIS incident-report status, quarterly audits, ad-hoc breach/complaint/audit reporting.',
        status="Met",
        severity="Info",
        strip_flag="N",
        strip_note="No statutory citation to strip.",
        finding=(
            "All six .1702(d) QP responsibility items are addressed in the SOP: "
            "(1) supervision of APs is in §1.4 (QP supervises APs and DCPs) and §1.4(a) (quarterly personnel-file audits); "
            "(2) oversight of emergencies is in §1.4 (On-Call QP 24/7) and Protocol 3 (Incident Response); "
            "(3) direct psychoeducational services is in Protocol 22(a) (QP clinical block 9a-12p and 1p-3p includes individual therapy, family collateral calls); "
            "(4) participation in treatment planning meetings is in §4.3 (QP facilitates PCP meeting); "
            "(5) coordination of each youth's treatment plan is in §1.4 and Protocol 10 (PCP Implementation & Review); "
            "(6) basic case management functions are in Protocol 15 (Educational Coordination), Protocol 16 (Family Engagement), Protocol 17 (Discharge & Transition). "
            "No corrective action required."
        ),
        remediation="No operational change.",
    ),

    # .1703 AP REQUIREMENTS
    dict(
        id="M-010",
        rule=".1703(a)",
        rule_title="AP REQUIREMENTS — At least one full-time AP per .0104(1)",
        rule_text='"In addition to the qualified professional specified in Rule .1702 of this Section, each facility shall have at least one full-time direct care staff who meets or exceeds the requirements of an associate professional as set forth in 10A NCAC 27G .0104(1)."',
        sop_loc="§2.2 Staff Qualifications (AP bullet); Protocol 22(b) AP/PP Daily Workflow",
        sop_quote='§2.2 APs: Bachelor\'s in human services with at least one year of relevant experience. Protocol 22(b): APs and PPs provide direct behavioral-health services under QP supervision per §2.2. They carry a 1:4 youth-supervision ratio on day or evening shift.',
        status="Met",
        severity="Info",
        strip_flag="Y",
        strip_note='Strip "10A NCAC 27G .0104(1)" citation; replace with "meets the associate professional definition per facility policy."',
        finding=(
            "The SOP §2.2 AP definition aligns with .0104(1)(b) (bachelor's degree in human services field with less than two years of post-bachelor's MH/DD/SA experience). "
            "Protocol 22(b) confirms the AP works full-time (7a-11p rotating schedule, 14.5 hrs/day × 5 days = 72.5 hrs/wk). "
            "However, the SOP does not explicitly state that the AP position is full-time. To improve audit defensibility, the QP should add 'full-time' to the §2.2 AP bullet. "
            "The AP supervision requirement (.0104(1)(b) requires QP supervision until 2 years of experience) is partially addressed in §1.4 (QP supervises APs) but the SOP does not explicitly state the supervision-plan requirement."
        ),
        remediation="v2.23: Add 'full-time' qualifier to §2.2 AP bullet. Address F-006 (AP individualized supervision plan).",
    ),
    dict(
        id="M-011",
        rule=".1703(b)(1)-(3)",
        rule_title="AP REQUIREMENTS — Written policies specifying AP responsibilities (3 items)",
        rule_text=(
            'The governing body responsible for each facility shall develop and implement written policies that specify the responsibilities of its associate professional(s). At a minimum these policies shall address the following: '
            '(1) management of the day to day operations of the facility; '
            '(2) supervision of paraprofessionals regarding responsibilities related to the implementation of each child or adolescent\'s treatment plan; and '
            '(3) participation in service planning meetings.'
        ),
        sop_loc="§1.4; Protocol 22(b) AP/PP Daily Workflow",
        sop_quote='Protocol 22(b): APs lead or co-lead skill-building groups, individual check-ins, group therapy, family visitation support, documentation block.',
        status="Partial",
        severity="Medium",
        strip_flag="N",
        strip_note="No statutory citation to strip.",
        finding=(
            "The SOP addresses .1703(b)(1) (day-to-day operations) and .1703(b)(3) (participation in service planning meetings) through Protocol 22(b). "
            "However, .1703(b)(2) — explicit AP supervision of paraprofessionals regarding treatment-plan implementation — is not clearly stated. "
            "Protocol 22(b) shows APs leading groups and conducting check-ins, but the supervisory relationship between APs and paraprofessional DCPs is not codified. "
            "This is a Medium severity gap. The SOP should add an explicit statement that APs supervise paraprofessional DCPs regarding the implementation of each youth's PCP/BSP. "
            "This gap is related to F-006 (.0203(f) individualized supervision plan for APs) and F-007 (.0204(f) individualized supervision plan for paraprofessionals)."
        ),
        remediation="v2.23: Add to §1.4 or §2.2 an explicit statement that APs supervise paraprofessional DCPs regarding PCP/BSP implementation, and add individualized supervision plan requirements per F-006 and F-007.",
    ),

    # .1704 MINIMUM STAFFING
    dict(
        id="M-012",
        rule=".1704(a)",
        rule_title="MINIMUM STAFFING — QP available by phone/page; direct care staff within 30 minutes",
        rule_text='"A qualified professional shall be available by telephone or page. A direct care staff shall be able to reach the facility within 30 minutes at all times."',
        sop_loc="§1.4 Organizational Structure; Protocol 22(i) Master Schedule Summary — On-Call Coverage",
        sop_quote='§1.4: An On-Call QP is available 24/7/365 for clinical decision-making. Protocol 22(i): The QP carries the agency phone 24/7 on a rotating weekly schedule. The RN is on-call 24/7 for medical questions. The House Manager is on-call for facility emergencies during off-hours.',
        status="Met",
        severity="Info",
        strip_flag="N",
        strip_note="No statutory citation to strip.",
        finding=(
            "QP availability by phone/page is fully addressed via the 24/7 on-call QP rotation. The 'direct care staff within 30 minutes' requirement is not explicitly stated but is operationally satisfied by the on-call system described in Protocol 22(i) — "
            "the on-call QP 'shall arrange a replacement before the shift begins and shall cover in-house personally if no replacement is available' (§2.1). "
            "For full audit defensibility, the SOP should add an explicit 30-minute response-time commitment to Protocol 22(i) or §2.1."
        ),
        remediation="Optional v2.23: Add explicit 30-minute response-time statement to Protocol 22(i) or §2.1.",
    ),
    dict(
        id="M-013",
        rule=".1704(b)",
        rule_title="MINIMUM STAFFING — Awake hours: 2/1-4, 3/5-8, 4/9-12",
        rule_text=(
            'The minimum number of direct care staff required when children or adolescents are present and awake is as follows: '
            '(1) two direct care staff shall be present for one, two, three or four children or adolescents; '
            '(2) three direct care staff shall be present for five, six, seven or eight children or adolescents; and '
            '(3) four direct care staff shall be present for nine, ten, eleven or twelve children or adolescents.'
        ),
        sop_loc="§2.1 Staffing Ratios — Staff-Secure Level III (table)",
        sop_quote='Day (7a-3p): 2 staff (1-4 youth), 4 staff (5-8 youth), 5 staff (9 youth). Evening (3p-11p): same. Overnight (11p-7a): same.',
        status="Met-Exceeds",
        severity="Info",
        strip_flag="Y",
        strip_note='Strip ".1700" citation; replace with "Per the Level III Staff-Secure operating standards."',
        finding=(
            "The SOP is stricter than .1704(b) minimums: where the rule requires 3 staff for 5-8 youth and 4 staff for 9-12 youth, the SOP requires 4 staff for 5-8 youth and 5 staff for 9 youth. "
            "This stricter standard is defensible — it provides additional supervision capacity for a staff-secure setting serving youth with severe emotional disturbance. "
            "The SOP appropriately does not exceed the licensed capacity of 9 youth (per §2.1 note). No corrective action required."
        ),
        remediation="No operational change. Strip statutory citations in v2.23.",
    ),
    dict(
        id="M-014",
        rule=".1704(c)",
        rule_title="MINIMUM STAFFING — Sleep hours: 2/1-4 (1 awake), 2/5-8 (both awake), 3/9-12 (2 awake)",
        rule_text=(
            'The minimum number of direct care staff during child or adolescent sleep hours is as follows: '
            '(1) two direct care staff shall be present and one shall be awake for one through four children or adolescents; '
            '(2) two direct care staff shall be present and both shall be awake for five through eight children or adolescents; and '
            '(3) three direct care staff shall be present of which two shall be awake and the third may be asleep for nine, ten, eleven or twelve children or adolescents.'
        ),
        sop_loc="§2.1 Staffing Ratios — Staff-Secure Level III (table); Protocol 13 Staffing Ratio & Awake Overnight Protocols",
        sop_quote='§2.1 Overnight (11p-7a): 2 staff (1-4 youth), 4 staff (5-8 youth), 5 staff (9 youth) — Awake (No sleeping). Protocol 13: Two (2) awake staff on duty at all times for 1-4 youth. Sleeping is prohibited.',
        status="Met-Exceeds",
        severity="Info",
        strip_flag="Y",
        strip_note='Strip ".1700" citation; replace with "Per the Level III Staff-Secure operating standards."',
        finding=(
            "The SOP exceeds .1704(c) minimums in two respects: (1) for 1-4 youth, the rule requires only 1 of 2 staff awake, but the SOP requires BOTH awake; "
            "(2) for 5-8 and 9 youth, the SOP requires more total staff than the rule minimum. This stricter standard is operationally justified by the staff-secure designation and the population served (youth with severe emotional disturbance). "
            "The 'Awake (No sleeping)' annotation in the §2.1 table and the explicit 'Sleeping is strictly prohibited' statement in Protocol 13 eliminate any ambiguity. "
            "The 15-minute room-check cadence documented on Form 1 (Shift Change & Awake Night Watch Log) provides verification of continuous awake supervision. No corrective action required."
        ),
        remediation="No operational change. Strip statutory citations in v2.23.",
    ),
    dict(
        id="M-015",
        rule=".1704(d)",
        rule_title="MINIMUM STAFFING — Additional staff based on individual needs per treatment plan",
        rule_text='"In addition to the minimum number of direct care staff set forth in Paragraphs (a)-(c) of this Rule, more direct care staff shall be required in the facility based on the child or adolescent\'s individual needs as specified in the treatment plan."',
        sop_loc="§2.1 Staffing Ratios — Staff-Secure Level III",
        sop_quote='Ratios shall be increased based on PCP acuity, behavioral incidents, 1:1 supervision orders, gender-match requirements for two-person restraint protocols, or any time a youth is on continuous observation status per §5.',
        status="Met",
        severity="Info",
        strip_flag="N",
        strip_note="No statutory citation to strip.",
        finding=(
            "The SOP explicitly addresses .1704(d) by listing five triggers for staffing increases: PCP acuity, behavioral incidents, 1:1 supervision orders, gender-match for two-person restraint, and continuous observation status. "
            "All five triggers tie back to the PCP or clinical status, satisfying the 'as specified in the treatment plan' requirement. "
            "The QP is designated as responsible for real-time ratio monitoring and adjustment (§2.1). No corrective action required."
        ),
        remediation="No operational change.",
    ),
    dict(
        id="M-016",
        rule=".1704(e)",
        rule_title="MINIMUM STAFFING — Supervision when away from facility per treatment plan",
        rule_text='"Each facility shall be responsible for ensuring supervision of children or adolescents when they are away from the facility in accordance with the child or adolescent\'s individual strengths and needs as specified in the treatment plan."',
        sop_loc="Protocol 11 Transportation & Community Outing Safety; Protocol 15 Educational Coordination & School Reintegration",
        sop_quote='Protocol 11: Conduct a headcount before leaving and upon return. If transporting one youth, staff sits in the back seat. Seatbelts on at all times. Never leave youth unattended in a vehicle. Outings tied to an ISP goal. Assess behavioral stability (no restraint in the last 4 hours).',
        status="Met",
        severity="Info",
        strip_flag="N",
        strip_note="No statutory citation to strip.",
        finding=(
            "Supervision during off-site activities is thoroughly addressed in Protocol 11 (Transportation & Community Outing Safety), which requires ISP-goal linkage, behavioral-stability assessment, headcounts, and continuous staff presence. "
            "Protocol 15 (Educational Coordination) addresses school-attendance supervision. The QP tracks supervision-level changes in the PCP per Protocol 10. No corrective action required."
        ),
        remediation="No operational change.",
    ),

    # .1705 LICENSED PROFESSIONAL — CRITICAL GAP
    dict(
        id="F-001",
        rule=".1705(a)-(b)",
        rule_title="LICENSED PROFESSIONALS — 4 hrs/wk face-to-face clinical consultation by licensed professional",
        rule_text=(
            '(a) Face to face clinical consultation shall be provided in each facility at least four hours a week by a licensed professional. For purposes of this Rule, licensed professional means an individual who holds a license or provisional license issued by the governing board regulating a human service profession in the State of North Carolina. For substance-related disorders this shall include a licensed Clinical Addiction Specialist or a certified Clinical Supervisor. '
            '(b) The consultation specified in Paragraph (a) of this Rule shall include: (1) clinical supervision of the qualified professional specified in Rule .1702 of this Section; (2) individual, group or family therapy services; or (3) involvement in child or adolescent specific treatment plans or overall program issues.'
        ),
        sop_loc="§1.4 Organizational Structure (Clinical Director role); §4 Clinical Services",
        sop_quote='§1.4: The Clinical Director is a licensed clinical professional with overall responsibility for the clinical program, including setting the clinical vision, approving clinical policies, and providing direction to clinical leadership.',
        status="Gap",
        severity="High",
        strip_flag="Y",
        strip_note='Strip "license or provisional license issued by the governing board regulating a human service profession in the State of North Carolina" rule quote if it appears in SOP; replace with "a clinician licensed by the applicable state licensing board."',
        finding=(
            "This is the most significant gap identified in the audit. Rule .1705 requires at least 4 hours per week of face-to-face clinical consultation by a licensed professional, with the consultation including one or more of: clinical supervision of the QP, individual/group/family therapy, or involvement in treatment plans/program issues. "
            "The SOP Manual v2.22 references a 'Clinical Director' who is a licensed clinical professional, and §1.4(a) requires the QP to provide recurring compliance reports to the Clinical Director. However, the SOP does not explicitly commit to a minimum of 4 hours per week of face-to-face clinical consultation by a licensed professional. "
            "The Clinical Director's role is described in broad terms (clinical vision, policy approval, direction to clinical leadership) but not specifically quantified as 4 hours/week of on-site consultation including the three .1705(b) activities. "
            "This is a High severity finding because .1705 is a direct licensure rule — a surveyor will check whether the facility can document 4 hours/week of licensed-professional face-to-face consultation time. "
            "The QP must add a new subsection (proposed §4.6 Licensed Professional Face-to-Face Clinical Consultation) that: (1) commits to a minimum of 4 hours/week of on-site consultation by a licensed professional (LCSW, LPC, LMFT, Licensed Psychologist, or psychiatrist per .0104(14) licensed clinician definition); "
            "(2) enumerates the three .1705(b) consultation activities (clinical supervision of the QP, individual/group/family therapy, treatment-plan involvement); (3) requires documentation of each consultation session (date, duration, licensed professional name/credential, activities performed, youth seen) in a Licensed Professional Consultation Log retained in the facility compliance binder; "
            "(4) designates the Clinical Director as the default licensed professional, with authority to delegate to other licensed clinicians on the facility's clinical staff. "
            "Failure to remediate this gap before the next DHSR MHLC licensure survey is a license-blocking risk."
        ),
        remediation="v2.23: Add new §4.6 Licensed Professional Face-to-Face Clinical Consultation per .1705(a)-(b), including a Licensed Professional Consultation Log (proposed Form 10). Target completion: September 2026.",
    ),

    # .1706 OPERATIONS
    dict(
        id="M-017",
        rule=".1706(a)",
        rule_title="OPERATIONS — Max 12 children/adolescents",
        rule_text='"Each facility shall serve no more than a total of 12 children and adolescents."',
        sop_loc="§2.1 Note",
        sop_quote='Note: NC defines a "Group Home" as a facility serving no more than nine (9) children (.0103(14)). The facility shall not exceed its licensed capacity as stated on the DHSR MHLC license, which shall not exceed nine children under any circumstances.',
        status="Met-Exceeds",
        severity="Info",
        strip_flag="Y",
        strip_note='Strip ".0103(14)" citation; replace with "the state group-home definition." Strip "DHSR MHLC" abbreviation; replace with "the state licensing authority."',
        finding=(
            "The SOP imposes a stricter 9-child maximum (per the state group-home definition cited in the SOP), which is more restrictive than .1706(a)'s 12-child cap. "
            "This is defensible and appropriate for a Level III Staff-Secure RTF. The DHSR MHLC license will state the actual licensed capacity, which the SOP correctly says 'shall not exceed nine children under any circumstances.' "
            "No corrective action required."
        ),
        remediation="No operational change. Strip statutory citations in v2.23.",
    ),
    dict(
        id="M-018",
        rule=".1706(b)",
        rule_title="OPERATIONS — Family/LRP involved in transition planning",
        rule_text='"Family members or other legally responsible persons shall be involved in development of plans in order to assure a smooth transition to a less restrictive setting."',
        sop_loc="§3.4 Discharge & Transition; §4.3 PCP Development; Protocol 16 Family Engagement, Visitation & Home Passes",
        sop_quote='§3.4: Transition planning is initiated at admission and reviewed every 30 days. §4.3: Within 30 calendar days of admission, the QP facilitates a PCP meeting including the youth, guardian, LME/MCO representative, and other supports identified by the family.',
        status="Met",
        severity="Info",
        strip_flag="Y",
        strip_note='Strip "LME/MCO" abbreviation; replace with "the regional managed care organization representative."',
        finding=(
            "Family/LRP involvement in transition planning is thoroughly addressed via §3.4 (transition planning at admission, 30-day reviews), §4.3 (PCP meeting includes guardian and family-identified supports), and Protocol 16 (Family Engagement, Visitation & Home Passes with trial home visits prior to discharge). "
            "No corrective action required."
        ),
        remediation="No operational change. Strip statutory abbreviations in v2.23.",
    ),
    dict(
        id="M-019",
        rule=".1706(c)",
        rule_title="OPERATIONS — Coordinate with LEA for educational needs",
        rule_text='"The residential treatment staff secure facility shall coordinate with the local education agency to ensure that the child\'s educational needs are met as identified in the child\'s education plan and the treatment plan. Most of the children will be able to attend school; for others, the facility will coordinate services across settings such as alternative learning programs, day treatment, or a job placement."',
        sop_loc="§7.3 Facility-Based School Determination; Protocol 15 Educational Coordination & School Reintegration",
        sop_quote='Protocol 15: QP contacts the LEA McKinney-Vento liaison or EC Director. Signs ROI. Coordinates transportation. QP/AP attends IEP meetings. Advocates for an aligned BIP. Files the IEP in the youth\'s chart.',
        status="Met",
        severity="Info",
        strip_flag="Y",
        strip_note='Strip "LEA", "McKinney-Vento", "EC Director", "IEP", "BIP" abbreviations and statutory references; replace with "the local school district liaison for homeless youth or the exceptional children director," "release of information," "individualized education program," "behavioral intervention plan."',
        finding=(
            "Educational coordination is thoroughly addressed via §7.3 (Facility-Based School Determination distinguishing Level III RTS from PRTF) and Protocol 15 (Educational Coordination & School Reintegration with LEA contact, ROI, IEP attendance, daily attendance logging, and behavior-report collection). "
            "The SOP also addresses alternative placements via the §7.3 facility-based-school determination. No corrective action required."
        ),
        remediation="No operational change. Strip statutory abbreviations in v2.23.",
    ),
    dict(
        id="M-020",
        rule=".1706(d)",
        rule_title="OPERATIONS — Psychiatric consultation available as needed",
        rule_text='"Psychiatric consultation shall be available as needed for each child or adolescent."',
        sop_loc="§6.1 Medical Care; Protocol 22(g) RN Daily Workflow",
        sop_quote='§6.1: Each resident has an identified Primary Care Physician (PCP) and psychiatrist upon admission. Protocol 22(g): Coordinate with the prescribing psychiatrist via telehealth or phone. Document any medication changes and update the MAR.',
        status="Met",
        severity="Info",
        strip_flag="N",
        strip_note="No statutory citation to strip.",
        finding=(
            "Psychiatric consultation is addressed via §6.1 (psychiatrist identified at admission) and Protocol 22(g) (RN coordinates with psychiatrist via telehealth/phone for medication changes). "
            "The QP should consider adding an explicit 'available as needed' statement to §6.1 to mirror the rule's language. No corrective action required."
        ),
        remediation="Optional v2.23: add explicit 'available as needed' statement to §6.1.",
    ),
    dict(
        id="F-009",
        rule=".1706(e)",
        rule_title="OPERATIONS — 18th birthday: 6 months or end of state fiscal year, whichever is longer",
        rule_text='"If an adolescent has his 18th birthday while receiving treatment in the facility, he may remain for six months or until the end of the state fiscal year, whichever is longer."',
        sop_loc="§3 Admissions, Discharges, and Transition Planning (no explicit policy)",
        sop_quote='§3 does not contain an explicit policy addressing an adolescent turning 18 while in treatment.',
        status="Gap",
        severity="Medium",
        strip_flag="N",
        strip_note="No statutory citation in SOP (gap is absence of policy, not presence of statute).",
        finding=(
            "The SOP does not explicitly address .1706(e)'s 18th-birthday continuation policy. This rule permits an adolescent who turns 18 while in treatment to remain in the facility for 6 months or until the end of the state fiscal year (June 30), whichever is longer. "
            "Without an explicit policy, staff may incorrectly discharge a youth immediately upon their 18th birthday, which would violate .1706(e). "
            "This is a Medium severity finding because the gap is unlikely to cause harm (the QP would naturally consult the Clinical Director and LME/MCO in such cases), but the absence of a written policy creates audit risk. "
            "The QP should add a new subsection (proposed §3.6 18th-Birthday Continuation Policy) stating that an adolescent who turns 18 while in active treatment may remain for 6 months or until the end of the state fiscal year (June 30), whichever is longer, provided the youth continues to meet medical-necessity criteria and the LME/MCO authorizes continued services. "
            "The policy should also address consent transfer (youth becomes their own LRP at 18 unless guardianship is court-extended) and Medicaid eligibility redetermination."
        ),
        remediation="v2.23: Add new §3.6 18th-Birthday Continuation Policy per .1706(e).",
    ),
    dict(
        id="M-021",
        rule=".1706(f)",
        rule_title="OPERATIONS — Age-appropriate personal belongings",
        rule_text='"Each child or adolescent shall be entitled to age-appropriate personal belongings unless such entitlement is counter-indicated in the treatment plan."',
        sop_loc="§1.7(a)(xii) Resident Rights",
        sop_quote='§1.7(a)(xii): retain personal property consistent with facility safety rules.',
        status="Met",
        severity="Info",
        strip_flag="N",
        strip_note="No statutory citation to strip.",
        finding=(
            "The right to retain personal property is enumerated in §1.7(a)(xii). The 'consistent with facility safety rules' qualifier mirrors the rule's 'counter-indicated in the treatment plan' caveat. "
            "Protocol 9 (Contraband & Room Search Protocol) operationalizes the safety-rule limitation. No corrective action required."
        ),
        remediation="No operational change.",
    ),
    dict(
        id="M-022",
        rule=".1706(g)",
        rule_title="OPERATIONS — 24/7/365 operation",
        rule_text='"Each facility shall operate 24 hours per day, seven days a week, and each day of the year."',
        sop_loc="§1.1 Mission Statement; Protocol 22 Daily Workflow Schedules",
        sop_quote='§2.1: 2:4 minimum applies 24 hours per day, 7 days per week, 365 days per year. Protocol 22: master schedule summary covers QP (on-site + on-call 24/7), AP (rotating 7a-11p), DCP Day (7a-3p), DCP Evening (3p-11p), DCP Awake Overnight (11p-7a), House Manager (on-call), RN (on-call 24/7), Billing Coordinator (8a-4p Mon-Fri).',
        status="Met",
        severity="Info",
        strip_flag="N",
        strip_note="No statutory citation to strip.",
        finding=(
            "24/7/365 operation is explicitly stated in §2.1 and operationalized through Protocol 22's master schedule covering all shifts and on-call rotations. "
            "No corrective action required."
        ),
        remediation="No operational change.",
    ),

    # .1707 PERSONS PERMITTED
    dict(
        id="M-023",
        rule=".1707(a)",
        rule_title="PERSONS PERMITTED — Admitted youth, LRP, staff, family/friends per treatment plan, director permission",
        rule_text='"Only admitted children or adolescents, legally responsible persons, staff, other family and friends identified in the treatment plan, and others permitted by the facility director shall be permitted on the premises."',
        sop_loc="§9.5 Staff-Secure Physical-Plant Measures; Protocol 16 Family Engagement, Visitation & Home Passes",
        sop_quote='§9.5: controlled access, delayed egress, line-of-sight, visitor management, contraband search. Protocol 16: Approved visitor list is maintained in the office. Staff search bags before visits. Document all visits.',
        status="Met",
        severity="Info",
        strip_flag="N",
        strip_note="No statutory citation to strip.",
        finding=(
            "Person-permitted controls are implemented via §9.5 staff-secure physical-plant measures (controlled access, visitor management) and Protocol 16 (approved visitor list, bag searches, visit documentation). "
            "The QP should consider adding an explicit 'facility director permission' statement for non-treatment-plan visitors to mirror the rule's language. No corrective action required."
        ),
        remediation="Optional v2.23: add explicit facility-director-permission statement to §9.5.",
    ),
    dict(
        id="M-024",
        rule=".1707(b)",
        rule_title="PERSONS PERMITTED — Others prohibited except emergency or law",
        rule_text='"Individuals other than those specified in Paragraph (a) of this Rule are prohibited from entering the facility except in instances of emergency or as permitted by law."',
        sop_loc="§9.5 Staff-Secure Physical-Plant Measures; Protocol 19 Emergency & Disaster Preparedness (Lockdown)",
        sop_quote='Protocol 19 Lockdown: Secure doors and windows. Hide. Silence phones. Do not open for anyone but law enforcement.',
        status="Met",
        severity="Info",
        strip_flag="N",
        strip_note="No statutory citation to strip.",
        finding=(
            "The staff-secure access controls in §9.5 and the lockdown protocol in Protocol 19 effectively exclude unauthorized persons. The emergency and law-enforcement exceptions are addressed. No corrective action required."
        ),
        remediation="No operational change.",
    ),

    # .1708 TRANSFER OR DISCHARGE
    dict(
        id="M-025",
        rule=".1708(b)",
        rule_title="TRANSFER OR DISCHARGE — Advance written notification to treatment team (except emergency)",
        rule_text='"A child or adolescent shall not be discharged or transferred from a facility, except in case of emergency, without the advance written notification of the treatment team, including the legally responsible person."',
        sop_loc="§3.4 Discharge & Transition",
        sop_quote='§3.4: Transition planning is initiated at admission and reviewed every 30 days. Discharge may be planned or unplanned. The Discharge Summary is completed within 7 calendar days of discharge.',
        status="Partial",
        severity="Medium",
        strip_flag="N",
        strip_note="No statutory citation in SOP.",
        finding=(
            "The SOP addresses planned discharge via 30-day transition-planning reviews and 7-day Discharge Summary completion, but does not explicitly require advance WRITTEN notification to the treatment team (including LRP) for non-emergency transfers or discharges. "
            "The rule requires advance written notification — not just verbal discussion at a planning meeting. "
            "This is a Medium severity gap. The QP should add an explicit requirement to §3.4 that non-emergency discharge or transfer requires written notification to the treatment team (including LRP, LME/MCO representative, DSS if applicable, LEA if applicable) at least X days in advance (the rule does not specify a minimum number of days, but the facility should set a policy — e.g., 7 calendar days)."
        ),
        remediation="v2.23: Add to §3.4 an explicit advance-written-notification requirement for non-emergency discharge/transfer (recommended: 7 calendar days).",
    ),
    dict(
        id="M-026",
        rule=".1708(c)",
        rule_title="TRANSFER OR DISCHARGE — Service planning meeting with CFT/involved persons prior to transfer/discharge",
        rule_text='"The facility shall meet with existing child and family teams or other involved persons including the parent(s) or legal guardian, area authority or county program representative(s) and other representatives involved in the care and treatment of the child or adolescent, including local Department of Social Services, Local Education Agency and criminal justice agency, to make service planning decisions prior to the transfer or discharge of the child or adolescent from the facility."',
        sop_loc="§3.4 Discharge & Transition; §4.3 PCP Development",
        sop_quote='§3.4: Discharge may be planned or unplanned. The Discharge Summary is completed within 7 calendar days of discharge, and includes: reason for admission, course/progress, condition at discharge, recommendations, final diagnoses, and dated signatures.',
        status="Partial",
        severity="Medium",
        strip_flag="Y",
        strip_note='Strip "Department of Social Services", "Local Education Agency" statutory names; replace with "the local social services agency," "the local school district." Strip "child and family team" if it appears in statutory form; replace with "the youth\'s care-coordination team."',
        finding=(
            "The SOP addresses discharge planning through 30-day transition reviews and a 7-day Discharge Summary, but does not explicitly require a pre-discharge service-planning meeting with the full Child and Family Team (CFT) and involved agencies per .1708(c). "
            "§4.3 PCP meetings include the guardian and LME/MCO representative, but the SOP does not explicitly require DSS, LEA, or criminal-justice participation in discharge planning when those agencies are involved. "
            "This is a Medium severity gap. The QP should add an explicit requirement to §3.4 that a discharge service-planning meeting be convened with the youth's CFT and all involved agencies prior to non-emergency discharge."
        ),
        remediation="v2.23: Add to §3.4 an explicit pre-discharge CFT meeting requirement per .1708(c).",
    ),
    dict(
        id="M-027",
        rule=".1708(d)",
        rule_title="TRANSFER OR DISCHARGE — Emergency: notify treatment team as soon as stabilized",
        rule_text='"In case of an emergency, the facility shall notify the treatment team including the legally responsible person of the transfer or discharge of the child or adolescent as soon as the emergency situation is stabilized."',
        sop_loc="Protocol 3 Incident Response & IRIS Protocol; Protocol 14 Medical Emergencies & Acute Illness Response",
        sop_quote='Protocol 3: Guardian within 1 hour. LME/MCO per their requirements. Protocol 14: Guardian notified within 1 hour. IRIS filed.',
        status="Met",
        severity="Info",
        strip_flag="Y",
        strip_note='Strip "LME/MCO" abbreviation; replace with "the regional managed care organization."',
        finding=(
            "Emergency notifications are addressed in Protocol 3 (guardian within 1 hour, LME/MCO per their requirements) and Protocol 14 (medical emergencies: guardian within 1 hour). "
            "The 'as soon as the emergency situation is stabilized' timing is operationally satisfied by the 1-hour notification window. No corrective action required."
        ),
        remediation="No operational change. Strip statutory abbreviations in v2.23.",
    ),
    dict(
        id="F-008",
        rule=".1708(e)",
        rule_title="TRANSFER OR DISCHARGE — Post-emergency service planning meeting within 5 business days",
        rule_text='"In case of an emergency, notification may be by telephone. A service planning meeting as set forth in Paragraph (c) of this Rule shall be held within five business days of an emergency transfer or discharge."',
        sop_loc="§3.4 Discharge & Transition (no explicit 5-business-day meeting requirement)",
        sop_quote='§3.4: Discharge may be planned or unplanned. The Discharge Summary is completed within 7 calendar days of discharge.',
        status="Gap",
        severity="Medium",
        strip_flag="N",
        strip_note="No statutory citation in SOP (gap is absence of policy).",
        finding=(
            "The SOP does not explicitly require a service-planning meeting within 5 business days of an emergency transfer or discharge. While §3.4 requires a Discharge Summary within 7 calendar days, the rule requires a broader service-planning meeting with the CFT and involved agencies within 5 business days. "
            "This is a Medium severity gap. The 5-business-day requirement is shorter than the 7-calendar-day Discharge Summary window, so the SOP's current 7-day target does not satisfy the rule. "
            "The QP should add to §3.4 an explicit requirement that an emergency transfer or discharge triggers a service-planning meeting with the CFT and involved agencies (DSS, LEA, LME/MCO, criminal justice if applicable) within 5 business days. "
            "Documentation of the meeting (attendees, agenda, decisions) should be filed in the youth's clinical record."
        ),
        remediation="v2.23: Add to §3.4 an explicit 5-business-day post-emergency service-planning meeting requirement per .1708(e).",
    ),

    # ═══════════════════════════════════════════════════════════════════════
    # SECTION B — .0104 Staff Definitions Crosswalk
    # ═══════════════════════════════════════════════════════════════════════

    dict(
        id="M-028",
        rule=".0104(1)(a)-(d) [AP definition]",
        rule_title="STAFF DEFINITIONS — Associate Professional (4 pathways)",
        rule_text=(
            '"Associate Professional (AP)" within the mh/dd/sas system of care means an individual who is either a: '
            '(a) graduate of a college or university with a masters degree in a human service field with less than one year of full-time, post-graduate degree accumulated mh/dd/sa experience with the population served, or a substance abuse professional with less than one year of full-time, post-graduate degree accumulated supervised experience in alcoholism and drug abuse counseling. Supervision shall be provided by a qualified professional with the population served until the individual meets one year of experience. The supervisor and the employee shall develop an individualized supervision plan upon hiring. The parties shall review the plan annually; '
            '(b) [bachelor\'s + <2 yrs]; (c) [bachelor\'s non-human-services + <4 yrs]; (d) [RN with <4 yrs mh/dd/sa experience].'
        ),
        sop_loc="§2.2 Staff Qualifications (AP bullet)",
        sop_quote='APs: Bachelor\'s in human services with at least one year of relevant experience.',
        status="Partial",
        severity="Medium",
        strip_flag="N",
        strip_note="No statutory citation to strip.",
        finding=(
            "The SOP §2.2 AP definition aligns with .0104(1)(b) but does not address the other three AP pathways (.0104(1)(a) master's with <1 year, .0104(1)(c) bachelor's non-human-services with <4 years, .0104(1)(d) RN with <4 years). "
            "More importantly, the SOP does not explicitly require an individualized supervision plan for APs, which .0104(1)(a)-(d) all mandate ('The supervisor and the employee shall develop an individualized supervision plan upon hiring. The parties shall review the plan annually'). "
            "This is a Medium severity gap related to F-006 (.0203(f) AP supervision plan) and F-007 (.0204(f) paraprofessional supervision plan). "
            "The QP should expand §2.2 to enumerate all four AP pathways and add an individualized supervision plan requirement."
        ),
        remediation="v2.23: Expand §2.2 AP definition to enumerate all four .0104(1) pathways and add individualized supervision plan requirement per F-006.",
    ),
    dict(
        id="F-011",
        rule=".0104(18) [Psychiatrist] vs .0104(21) [Qualified Professional]",
        rule_title="STAFF DEFINITIONS — .1702(a) cross-reference appears incorrect",
        rule_text=(
            '.0104(18) "Psychiatrist" means an individual who is licensed to practice medicine in the State of North Carolina and who has completed a training program in psychiatry accredited by the Accreditation Council for Graduate Medical Education. '
            '.0104(21) "Qualified professional" means, within the mh/dd/sas system of care either: (a) an individual who holds a license, provisional license, or certificate… (b) master\'s in human services + 1 yr supervised mh/dd/sa; (c) bachelor\'s in human services + 2 yrs supervised mh/dd/sa; (d) bachelor\'s non-human-services + 4 yrs supervised mh/dd/sa.'
        ),
        sop_loc="§1.4(b) QP Credentialing Requirements",
        sop_quote='§1.4(b): The Qualified Professional (QP) for this facility must meet the credentialing requirements of .0104(21). A QP is not required to hold a full, unrestricted clinical license. There are two acceptable QP pathways as set out below; either pathway satisfies the QP definition for this facility.',
        status="Met",
        severity="Low",
        strip_flag="Y",
        strip_note='Strip ".0104(21)" and ".0104(18)" citations; replace with "the qualified professional definition per facility policy." Note the .1702(a) cross-reference to .0104(18) appears to be a typographical error in the rule itself (it should reference .0104(21) "Qualified professional," not .0104(18) "Psychiatrist").',
        finding=(
            "Rule .1702(a) cross-references .0104(18), but .0104(18) is the 'Psychiatrist' definition, not the 'Qualified Professional' definition. The substantive QP definition is at .0104(21). "
            "This appears to be a typographical error in .1702(a) itself — the rule's intent (a QP with 2 years of direct client care experience) is clearly to reference the QP definition, not the psychiatrist definition. "
            "The SOP correctly follows the substantive QP definition per .0104(21), so this is a Low severity finding (citation clarification only). "
            "The QP should document this citation discrepancy in the facility compliance binder and confirm the operative QP definition with the Licensure & Training Consultant at the first in-person meeting per §1.2(e)."
        ),
        remediation="Document .1702(a) → .0104(21) citation discrepancy in compliance binder; confirm with Licensure & Training Consultant.",
    ),
    dict(
        id="M-029",
        rule=".0104(17) [Paraprofessional]",
        rule_title="STAFF DEFINITIONS — Paraprofessional (HS diploma + supervision)",
        rule_text='"Paraprofessional" within the mh/dd/sas system of care means an individual who, with the exception of staff providing respite services or personal care services, has a GED or high school diploma; those employed prior to November 1, 2001 to provide a mh/dd/sa service are not required to have a GED or high school diploma. Supervision shall be provided by a qualified professional or associate professional with the population served. The supervisor and the employee shall develop an individualized supervision plan upon hiring. The parties shall review the plan annually.',
        sop_loc="§2.2 Staff Qualifications (DCP bullet)",
        sop_quote='Direct Care Professionals (DCPs): High school diploma or GED with at least one year of mental health experience.',
        status="Partial",
        severity="Medium",
        strip_flag="N",
        strip_note="No statutory citation to strip.",
        finding=(
            "The SOP §2.2 DCP definition aligns with .0104(17) (HS diploma or GED) but adds a stricter '1 year mental health experience' requirement, which is permissible. "
            "However, the SOP does not explicitly require an individualized supervision plan for paraprofessional DCPs per .0104(17). "
            "This is a Medium severity gap related to F-007 (.0204(f) paraprofessional supervision plan). "
            "The QP should add an individualized supervision plan requirement for DCPs to §2.2."
        ),
        remediation="v2.23: Add individualized supervision plan requirement for DCPs to §2.2 per F-007.",
    ),
    dict(
        id="M-030",
        rule=".0104(21)(a)-(d) [Qualified Professional]",
        rule_title="STAFF DEFINITIONS — Qualified Professional (4 pathways)",
        rule_text=(
            '"Qualified professional" means, within the mh/dd/sas system of care either: '
            '(a) an individual who holds a license, provisional license, or certificate issued by the governing board regulating a human service profession, including a registered nurse who is licensed to practice in the State of North Carolina by the North Carolina Board of Nursing who also has four years of full-time accumulated experience in mh/dd/sa with the population served; '
            '(b) a graduate of a college or university with a Masters degree in a human service field and has one year of full-time, pre- or post-graduate degree accumulated supervised mh/dd/sa experience with the population served; '
            '(c) a graduate of a college or university with a bachelor\'s degree in a human service field and has two years of full-time, pre- or post-bachelor\'s degree accumulated supervised mh/dd/sa experience with the population served; or '
            '(d) a graduate of a college or university with a bachelor\'s degree in a field other than human services and has four years of full-time, pre- or post-bachelor\'s degree accumulated supervised mh/dd/sa experience with the population served.'
        ),
        sop_loc="§1.4(b) QP Credentialing Requirements (Pathways 1 and 2)",
        sop_quote='Pathway 1: master\'s degree in a human services field plus recognized NC credential plus at least one year of full-time, post-master\'s supervised MH/DD/SA experience. Pathway 2: bachelor\'s degree in a human services field plus two years of full-time, pre- or post-bachelor\'s supervised MH/DD/SA experience.',
        status="Met",
        severity="Info",
        strip_flag="Y",
        strip_note='Strip "NC credential" specifics (LCSW, LPC, LMFT, etc.); replace with "a recognized state clinical credential." Strip ".0104(21)" citation; replace with "the qualified professional definition per facility policy."',
        finding=(
            "The SOP §1.4(b) Pathway 1 aligns with .0104(21)(b) (master's + 1 year supervised MH/DD/SA experience). "
            "Pathway 2 aligns with .0104(21)(c) (bachelor's + 2 years supervised MH/DD/SA experience). "
            "The SOP does not address .0104(21)(a) (licensed/certified professional including RN with 4 years) or .0104(21)(d) (bachelor's non-human-services + 4 years). "
            "These two additional pathways are permissive (the rule says 'either' — meeting any one pathway suffices), so the SOP's two-pathway approach is compliant. "
            "However, the SOP should consider adding a note acknowledging the other two pathways for completeness and to avoid excluding otherwise-qualified candidates. "
            "No corrective action required."
        ),
        remediation="Optional v2.23: add note acknowledging .0104(21)(a) and (d) pathways for completeness.",
    ),

    # ═══════════════════════════════════════════════════════════════════════
    # SECTION C — .0201-.0210 Core Rules Findings
    # ═══════════════════════════════════════════════════════════════════════

    # .0201 Governing Body Policies
    dict(
        id="M-031",
        rule=".0201(a)(1)-(18)",
        rule_title="GOVERNING BODY POLICIES — 18 enumerated written-policy items",
        rule_text=(
            'The governing body responsible for each facility or service shall develop and implement written policies for the following: '
            '(1) delegation of management authority; (2) criteria for admission; (3) criteria for discharge; (4) admission assessments including who performs and time frames; '
            '(5) client record management including (A) persons authorized to document, (B) transporting records, (C) safeguard against loss/tampering/defacement/use by unauthorized persons, (D) record accessibility to authorized users at all times, (E) confidentiality; '
            '(6) screenings including (A) presenting problem/need assessment, (B) whether facility can serve assessment, (C) disposition including referrals; '
            '(7) quality assurance and quality improvement activities (8 sub-items); (8) use of medications by clients; (9) reporting of any incident, unusual occurrence or medication error; '
            '(10) voluntary non-compensated work performed by a client; (11) client fee assessment and collection practices; (12) medical preparedness plan; '
            '(13) authorization for and follow up of lab tests; (14) transportation including accessibility of emergency information; (15) services of volunteers; '
            '(16) areas in which staff receive training and continuing education; (17) safety precautions and requirements for facility areas including special client activity areas; (18) client grievance policy.'
        ),
        sop_loc="§1.3 Corporate Compliance; §1.4 Organizational Structure; §1.7 Resident Rights; §1.8 Organizational & Financial Foundations; §3 Admissions; §6 Health & Medication; §8 Incident Reporting; §9 Facility & Safety; §10 Medicaid Documentation; §11 Privacy & Confidentiality",
        sop_quote='§1.3: Corporate Compliance Plan to prevent Medicaid fraud, waste, and abuse. §1.7: Resident Rights with 15 enumerated rights and grievance procedure. §1.8: Organizational & Financial Foundations. §3.1: Admission Criteria. §3.4: Discharge criteria. §6.3: Medication management. §8: Incident reporting per Rule 108/IRIS.',
        status="Partial",
        severity="Medium",
        strip_flag="Y",
        strip_note='Strip "Rule 108" statutory citation; replace with "the state incident-reporting rule." Strip "IRIS" abbreviation; replace with "the state incident-reporting system."',
        finding=(
            "The SOP addresses most of the 18 .0201(a) governing-body-policy items, but several are not explicitly codified: "
            "(11) client fee assessment and collection practices — not explicitly addressed (the SOP focuses on Medicaid per-diem billing, not client fee assessment); "
            "(13) authorization for and follow-up of lab tests — not explicitly addressed in §6; "
            "(15) services of volunteers including supervision and confidentiality — not explicitly addressed; "
            "(10) voluntary non-compensated work performed by a client — partially addressed via §1.7(a)(xi) (right to be free from coercion to perform labor for the facility) but not as a positive policy on voluntary work. "
            "The other 14 items are addressed across §1.3, §1.4, §1.7, §1.8, §3, §6, §8, §9, §10, §11. "
            "This is a Medium severity gap. The QP should add explicit policies for items (11), (13), and (15) in v2.23."
        ),
        remediation="v2.23: Add explicit policies for .0201(a)(11) client fee assessment, (13) lab test authorization/follow-up, and (15) volunteer services.",
    ),
    dict(
        id="M-032",
        rule=".0201(b)",
        rule_title="GOVERNING BODY POLICIES — Minutes permanently maintained",
        rule_text='"Minutes of the governing body shall be permanently maintained."',
        sop_loc="§1.8 Organizational & Financial Foundations (Governing Body Roster)",
        sop_quote='§1.8: Governing Body Roster — a current list of all members of the governing body… Updated within 30 days of any change.',
        status="Partial",
        severity="Medium",
        strip_flag="N",
        strip_note="No statutory citation to strip.",
        finding=(
            "The SOP §1.8 requires maintaining a governing-body roster but does not explicitly state that governing-body meeting minutes are permanently maintained. "
            "The QP should add an explicit statement to §1.8 that governing-body meeting minutes are permanently maintained (paper or electronic) per .0201(b). "
            "This is a straightforward documentation-policy gap."
        ),
        remediation="v2.23: Add to §1.8 an explicit statement that governing-body meeting minutes are permanently maintained per .0201(b).",
    ),

    # .0202 Personnel Requirements
    dict(
        id="M-033",
        rule=".0202(a)-(g)",
        rule_title="PERSONNEL REQUIREMENTS — Job descriptions, age 18+, literacy, no abuse findings, criminal-conviction disclosure, licensure, personnel file, training (4 items)",
        rule_text=(
            '(a) written job description for each staff position (4 sub-items); (b) each staff person: (1) at least 18 years of age, (2) able to read/write/understand/follow directions, (3) meets minimum qualifications, (4) no substantiated abuse/neglect on NC Health Care Personnel Registry; '
            '(c) applicants shall disclose any criminal conviction; (d) staff shall be currently licensed/registered/certified per applicable state laws; (e) personnel file maintained with training, experience, licensure; (f) continuing education documented; (g) employee training programs including (1) general org orientation, (2) client rights and confidentiality, (3) mh/dd/sa needs per treatment plan, (4) infectious diseases and bloodborne pathogens.'
        ),
        sop_loc="§2.2 Staff Qualifications; §2.3 Background Checks; §2.4 Mandatory Training; §2.5 Personnel Records",
        sop_quote='§2.3: NC SBI fingerprint criminal background check, Health Care Personnel Registry check, DSS Child Abuse and Neglect Registry check, MVR. §2.4: 12 mandatory training topics including general org orientation, client rights/confidentiality, infectious diseases/bloodborne pathogens, population-specific mh/dd/sa needs. §2.5: Personnel files contain position descriptions, education verification, licensure/credentials, training records, supervision documentation.',
        status="Partial",
        severity="Medium",
        strip_flag="Y",
        strip_note='Strip "NC SBI", "Health Care Personnel Registry", "DSS Child Abuse and Neglect Registry" statutory names; replace with "state criminal background check," "state health care personnel registry," "state child abuse and neglect registry." Strip "MVR" abbreviation; replace with "motor vehicle record check."',
        finding=(
            "The SOP addresses most .0202 personnel requirements but has gaps: "
            "(c) criminal-conviction disclosure by applicants — the SOP §2.3 requires background checks but does not explicitly require applicants to self-disclose criminal convictions (a different requirement); "
            "(b)(1)-(2) age-18 and literacy requirements — not explicitly stated in §2.2; "
            "The other items are well-addressed: (a) job descriptions in §2.5; (b)(3) qualifications in §2.2; (b)(4) HCP Registry check in §2.3; (d) licensure in §2.5; (e) personnel file in §2.5; (f) CEUs in §2.5(a); (g) training in §2.4. "
            "This is a Medium severity gap. The QP should add explicit age-18, literacy, and criminal-conviction-disclosure statements to §2.2 or §2.3."
        ),
        remediation="v2.23: Add to §2.2 or §2.3 explicit statements for age-18 minimum, literacy requirement, and applicant criminal-conviction self-disclosure per .0202(b)(1)-(2) and (c).",
    ),
    dict(
        id="M-034",
        rule=".0202(h)",
        rule_title="PERSONNEL REQUIREMENTS — CPR/Heimlich/First Aid trained staff on-site at all times",
        rule_text='"Except as permitted under 10a NCAC 27G .5602(b) of this Subchapter, at least one staff member shall be available in the facility at all times when a client is present. That staff member shall be trained in basic first aid including seizure management, currently trained to provide cardiopulmonary resuscitation and trained in the Heimlich maneuver or other first aid techniques such as those provided by Red Cross, the American Heart Association or their equivalence for relieving airway obstruction."',
        sop_loc="§2.4 Mandatory Training (CPR with Heimlich / First Aid); §2.1 Staffing Ratios (2:4 minimum 24/7)",
        sop_quote='§2.4: CPR with Heimlich Maneuver / First Aid (annually; in-person only — no online-only certification accepted). §2.1: 2:4 minimum staffing applies 24/7/365.',
        status="Met",
        severity="Info",
        strip_flag="Y",
        strip_note='Strip "10A NCAC 27G .5602(b)" citation; replace with "the applicable exception in the state residential facility rules." Strip "Red Cross", "American Heart Association" trademark names if desired; replace with "an equivalent recognized certifying body."',
        finding=(
            "The SOP §2.4 explicitly requires CPR with Heimlich Maneuver / First Aid training annually, in-person only. "
            "Combined with §2.1's 2:4 minimum staffing (always at least 2 staff on duty), there will always be at least one CPR/First Aid certified staff on-site. "
            "However, the SOP does not explicitly state that AT LEAST ONE CPR/First Aid certified staff must be on duty at all times. "
            "The QP should add this explicit statement to §2.4 for audit clarity. Seizure management, while not explicitly listed in §2.4, is operationally covered under First Aid training. No corrective action required beyond the clarification."
        ),
        remediation="Optional v2.23: add explicit 'at least one CPR/First Aid certified staff on duty at all times' statement to §2.4.",
    ),
    dict(
        id="M-035",
        rule=".0202(i)",
        rule_title="PERSONNEL REQUIREMENTS — Infectious disease policies for personnel and clients",
        rule_text='"The governing body shall develop and implement policies and procedures for identifying, reporting, investigating and controlling infectious and communicable diseases of personnel and clients."',
        sop_loc="§6.5 Infection Control Program; Protocol 18 Infectious Disease & Bloodborne Pathogen Control",
        sop_quote='§6.5: facility shall maintain a written Infection Control Program consistent with CDC guidelines for residential congregate-care settings and OSHA Bloodborne Pathogens Standard (29 CFR 1910.1030). Protocol 18: Universal Precautions, exposure response, outbreak response (2+ youth with identical symptoms = isolate, increase sanitation, notify County Health Department if reportable).',
        status="Met",
        severity="Info",
        strip_flag="Y",
        strip_note='Strip "CDC", "OSHA", "29 CFR 1910.1030" statutory references; replace with "applicable federal infection-control guidelines," "the federal bloodborne pathogen standard." Strip "County Health Department" specific statutory name; replace with "the local public health authority."',
        finding=(
            "§6.5 and Protocol 18 comprehensively address .0202(i). The Infection Control Program is overseen by the RN with monthly QP review. "
            "Protocol 18 operationalizes universal precautions, exposure response (wash area, notify QP/RN, urgent care within 2 hours, IRIS), and outbreak response (isolation, sanitation, public health notification). "
            "No corrective action required."
        ),
        remediation="No operational change. Strip statutory references in v2.23.",
    ),

    # .0203 QP/AP Competencies
    dict(
        id="F-006",
        rule=".0203(f)",
        rule_title="QP/AP COMPETENCIES — Individualized supervision plan for APs upon hiring",
        rule_text='"The governing body for each facility shall develop and implement policies and procedures for the initiation of the individualized supervision plan upon hiring each associate professional."',
        sop_loc="§1.4 Organizational Structure (no explicit AP supervision-plan requirement)",
        sop_quote='§1.4: The QP supervises staff in accordance with the Clinical Director\'s clinical guidance, programmatic priorities, and performance expectations. §1.4(a): quarterly personnel-file audits, sanctions reviews, training-completion rates.',
        status="Gap",
        severity="Medium",
        strip_flag="N",
        strip_note="No statutory citation in SOP (gap is absence of policy).",
        finding=(
            "The SOP does not explicitly require an individualized supervision plan for each Associate Professional at hiring, with annual review. "
            ".0203(f) mandates this. While §1.4 and §1.4(a) address QP supervision of APs in general terms, they do not codify the individualized supervision plan requirement. "
            "This is a Medium severity gap related to F-007 (paraprofessional supervision plan). "
            "The QP should add to §1.4 or §2.2 an explicit requirement that each AP has an individualized supervision plan initiated at hiring and reviewed annually, documenting supervision frequency, format, focus areas, and the supervisor's QP credentials."
        ),
        remediation="v2.23: Add to §1.4 or §2.2 an explicit AP individualized supervision plan requirement per .0203(f).",
    ),

    # .0204 Paraprofessional Competencies
    dict(
        id="F-007",
        rule=".0204(f)",
        rule_title="PARAPROFESSIONAL COMPETENCIES — Individualized supervision plan for paraprofessionals upon hiring",
        rule_text='"The governing body for each facility shall develop and implement policies and procedures for the initiation of the individualized supervision plan upon hiring each paraprofessional."',
        sop_loc="§1.4 Organizational Structure (no explicit paraprofessional supervision-plan requirement)",
        sop_quote='§1.4: The QP supervises staff in accordance with the Clinical Director\'s clinical guidance.',
        status="Gap",
        severity="Medium",
        strip_flag="N",
        strip_note="No statutory citation in SOP (gap is absence of policy).",
        finding=(
            "The SOP does not explicitly require an individualized supervision plan for each paraprofessional DCP at hiring, with annual review. "
            ".0204(f) mandates this. This is a Medium severity gap related to F-006 (AP supervision plan). "
            "The QP should add to §1.4 or §2.2 an explicit requirement that each paraprofessional DCP has an individualized supervision plan initiated at hiring and reviewed annually."
        ),
        remediation="v2.23: Add to §1.4 or §2.2 an explicit paraprofessional DCP individualized supervision plan requirement per .0204(f).",
    ),

    # .0205 Assessment and Service Plan
    dict(
        id="M-036",
        rule=".0205(a)-(d)",
        rule_title="ASSESSMENT & SERVICE PLAN — Assessment prior to service; plan within 30 days; 6 plan contents",
        rule_text=(
            '(a) assessment shall be completed for a client prior to delivery of services, including (1) presenting problem, (2) needs and strengths, (3) provisional/admitting diagnosis with established diagnosis within 30 days, (4) pertinent social/family/medical history, (5) evaluations such as psychiatric/substance abuse/medical/vocational; '
            '(b) if services delivered before plan, strategies to address presenting problem shall be documented; '
            '(c) plan shall be developed based on assessment, in partnership with client/LRP, within 30 days of admission for clients expected to receive services beyond 30 days; '
            '(d) plan shall include (1) client outcomes with projected achievement date, (2) strategies, (3) staff responsible, (4) schedule for review at least annually in consultation with client/LRP, (5) basis for evaluation of outcome achievement, (6) written consent or agreement by client/LRP or written statement why consent could not be obtained.'
        ),
        sop_loc="§4.1 CCA; §4.2 Medical Necessity; §4.3 PCP Development",
        sop_quote='§4.1: A CCA performed by a licensed professional (QP) is required prior to service delivery. §4.3: Within 30 calendar days of admission, the QP facilitates a PCP meeting including the youth, guardian, LME/MCO representative. The PCP documents strengths, needs, goals, specific interventions, and a crisis plan. The PCP is signed by all participants, reviewed every 90 days thereafter.',
        status="Met-Exceeds",
        severity="Info",
        strip_flag="Y",
        strip_note='Strip "LME/MCO" abbreviation; replace with "the regional managed care organization representative."',
        finding=(
            "The SOP comprehensively addresses .0205: §4.1 CCA includes all 5 .0205(a) elements (presenting problems, needs/strengths, diagnosis, history, evaluations). "
            "§4.3 PCP within 30 days exceeds the .0205(d)(4) annual review minimum by requiring 90-day reviews. "
            "§4.3 includes strengths, needs, goals, interventions, crisis plan, and signatures (covering .0205(d)(1)-(3) and (6)). "
            "The SOP does not explicitly state the .0205(d)(5) 'basis for evaluation of outcome achievement' but operationally this is documented in the PCP goal-measurement criteria. "
            "No corrective action required."
        ),
        remediation="No operational change. Strip statutory abbreviations in v2.23.",
    ),

    # .0206 Client Records
    dict(
        id="M-037",
        rule=".0206(a)(1)-(9)",
        rule_title="CLIENT RECORDS — Required record contents (9 items)",
        rule_text=(
            'A client record shall be maintained for each individual admitted to the facility, which shall contain: '
            '(1) identification face sheet (name, record #, DOB, race/gender/marital status, admission date, discharge date); '
            '(2) documentation of mental illness/DD/SA diagnosis coded according to DSM IV; (3) documentation of screening and assessment; (4) treatment/habilitation or service plan; '
            '(5) emergency information (contact name/address/phone, preferred physician name/address/phone); (6) signed statement from client/LRP granting permission to seek emergency care; '
            '(7) documentation of services provided; (8) documentation of progress toward outcomes; (9) if applicable: (A) physical disorders diagnosis per ICD-9-CM, (B) medication orders, (C) lab tests, (D) medication errors and adverse drug reactions.'
        ),
        sop_loc="§3.3 Full Clinical Service Record — Required Elements; Form 8 Comprehensive Clinical Record Content Checklist",
        sop_quote='§3.3: Categories include Consents; Demographics and Emergency Information; Health History (including DSM-5-TR/ICD-10 diagnosis); Medications and Labs; Rights and Restrictive Interventions; Assessments (CCA); Planning (PCP with MID, service plan, signed service order); Discharge information; Referral information; Service notes/grids; Incidents; Disclosures and Legal documents; 42 CFR 2.22 summary for SUD; Accounting of Disclosures; and incoming/outgoing correspondence. Form 8: 28-element checklist.',
        status="Met-Exceeds",
        severity="Info",
        strip_flag="Y",
        strip_note='Strip "DSM-5-TR/ICD-10" and "ICD-9-CM" diagnostic manual citations; replace with "the current diagnostic and statistical manual." Strip "42 CFR 2.22" citation; replace with "the federal substance-use-disorder records confidentiality summary."',
        finding=(
            "The SOP §3.3 and Form 8 comprehensively address all 9 .0206(a) record-content items, plus additional RMDM-required elements. "
            "The SOP appropriately updates the rule's DSM-IV/ICD-9-CM references to the current DSM-5-TR/ICD-10. "
            "The Form 8 checklist provides a quarterly QP audit mechanism. No corrective action required."
        ),
        remediation="No operational change. Strip diagnostic manual citations in v2.23.",
    ),

    # .0207 Emergency Plans
    dict(
        id="M-038",
        rule=".0207(a)-(d)",
        rule_title="EMERGENCY PLANS — Written fire/disaster plans; quarterly drills per shift; first aid kit",
        rule_text=(
            '(a) Each facility shall develop a written fire plan and a disaster plan and shall make a copy of these plans available to the county emergency services agencies upon request. The plans shall include evacuation procedures and routes. '
            '(b) The plans shall be made available to all staff and evacuation procedures and routes shall be posted in the facility. '
            '(c) Fire and disaster drills in a 24-hour facility shall be held at least quarterly and shall be repeated for each shift. Drills shall be conducted under conditions that simulate the facility\'s response to fire emergencies. '
            '(d) Each facility shall have a first aid kit accessible for use.'
        ),
        sop_loc="§9.7 Disaster & Emergency Plan; Protocol 19 Emergency & Disaster Preparedness; Form 5 Emergency Drill & Environmental Safety Log",
        sop_quote='§9.7: written Disaster & Emergency Plan including fire, tornado, hurricane, power outage, system failure, lockdown, emergency relocation. Protocol 19: Fire — monthly drills required. Tornado — quarterly drills required. Form 5: Monthly Fire Drills (Under 3 minutes) table with 12 month rows; Quarterly Tornado Drills table with 4 quarter rows.',
        status="Partial",
        severity="Medium",
        strip_flag="N",
        strip_note="No statutory citation in SOP.",
        finding=(
            "The SOP exceeds .0207(c) minimums for fire drills (monthly vs. quarterly) but does not explicitly state that drills must be 'repeated for each shift.' "
            "Form 5 documents fire drills with date, time-of-day, # youth, evacuation time, staff, signature — but does not explicitly require separate drill records for day, evening, and overnight shifts. "
            "This is a Medium severity gap. The QP should update Form 5 and Protocol 19 to explicitly require quarterly drills for EACH shift (day, evening, overnight), not just monthly drills that may all occur on the day shift. "
            "Tornado drills are quarterly per Form 5, satisfying the rule minimum, but should also be repeated for each shift."
        ),
        remediation="v2.23: Update Protocol 19 and Form 5 to explicitly require quarterly fire AND tornado drills for EACH shift (day, evening, overnight) per .0207(c).",
    ),

    # .0208 Client Services
    dict(
        id="M-039",
        rule=".0208(a)(1)-(3)",
        rule_title="CLIENT SERVICES — Activities: safety, suitability, client participation",
        rule_text=(
            'Facilities that provide activities for clients shall assure that: '
            '(1) space and supervision is provided to ensure the safety and welfare of the clients; '
            '(2) activities are suitable for the ages, interests, and treatment/habilitation needs of the clients served; and '
            '(3) clients participate in planning or determining activities.'
        ),
        sop_loc="§5.5 Activities Program — Minimum 14 Hours/Week Planned Group Activities",
        sop_quote='§5.5: 14 hours per week of planned group activities. (a) age- and developmental-stage appropriate; (b) culturally responsive; (c) consistent with each youth\'s PCP goals; (d) trauma-informed, with voluntary participation and the right to decline without consequence; (e) inclusive of all youth regardless of mobility, sensory, or cognitive accommodation needs. §5.5(b): QP shall publish a written Weekly Activities Calendar no fewer than 7 days in advance, post it in the facility common area, and provide a copy to each youth at the weekly community meeting.',
        status="Met-Exceeds",
        severity="Info",
        strip_flag="N",
        strip_note="No statutory citation to strip.",
        finding=(
            "The SOP §5.5 comprehensively exceeds .0208(a) by requiring 14 hours/week of planned group activities, age-appropriateness, cultural responsiveness, PCP-goal alignment, trauma-informed voluntary participation, ADA/Section 504 inclusivity, and a weekly community meeting where youth participate in activity planning. "
            "No corrective action required."
        ),
        remediation="No operational change.",
    ),
    dict(
        id="M-040",
        rule=".0208(b)-(c)",
        rule_title="CLIENT SERVICES — 24-hour services; nutritious meals",
        rule_text=(
            '(b) Facilities or programs designated or described in these Rules as "24-hour" shall make services available 24 hours a day, every day in the year, unless otherwise specified in the rule. '
            '(c) Facilities that serve or prepare meals for clients shall ensure that the meals are nutritious.'
        ),
        sop_loc="§1.1 Mission; §6.4 Nutrition; Protocol 22 Daily Workflow Schedules",
        sop_quote='§6.4: Meals follow USDA guidelines. Special diets are accommodated with provider documentation. Menus are posted and retained 30 days. Food is never withheld as a consequence.',
        status="Met",
        severity="Info",
        strip_flag="Y",
        strip_note='Strip "USDA" statutory reference; replace with "federal nutrition guidelines."',
        finding=(
            "24/7 operation is established via §1.1 and Protocol 22. Meal nutrition is addressed via §6.4 (USDA guidelines, special diets, posted menus). "
            "The 'food never withheld as consequence' rule aligns with §5.1 (corporal punishment, withholding meals prohibited). No corrective action required."
        ),
        remediation="No operational change. Strip statutory reference in v2.23.",
    ),

    # .0209 Medication Requirements — MULTIPLE GAPS
    dict(
        id="M-041",
        rule=".0209(a)(1)",
        rule_title="MEDICATION — Dispensing on written order of physician/prescriber",
        rule_text='"Medications shall be dispensed only on the written order of a physician or other practitioner licensed to prescribe."',
        sop_loc="§6.3 Medication Management; §6.1 Medical Care",
        sop_quote='§6.1: Each resident has an identified Primary Care Physician (PCP) and psychiatrist upon admission. §6.3: Medications are administered only by RN-delegated staff who have completed NC Medication Administration training.',
        status="Met",
        severity="Info",
        strip_flag="Y",
        strip_note='Strip "NC Medication Administration training" statutory reference; replace with "the state-approved medication administration training."',
        finding=(
            "§6.1 establishes physician/psychiatrist oversight. §6.3 requires RN delegation and NC Medication Administration training. "
            "While the SOP focuses on administration rather than dispensing, dispensing is operationally handled by the pharmacy per the physician's order. No corrective action required."
        ),
        remediation="No operational change. Strip statutory reference in v2.23.",
    ),
    dict(
        id="F-012",
        rule=".0209(b)(2)-(3)",
        rule_title="MEDICATION — Tamper-resistant packaging; label contents (6 items)",
        rule_text=(
            '(b)(2) Prescription medications shall be dispensed in tamper-resistant packaging that will minimize the risk of accidental ingestion by children. Such packaging includes plastic or glass bottles/vials with tamper-resistant caps, or in the case of unit-of-use packaged drugs, a zip-lock plastic bag may be adequate. '
            '(b)(3) The packaging label of each prescription drug dispensed must include: (A) client\'s name; (B) prescriber\'s name; (C) current dispensing date; (D) clear directions for self-administration; (E) name, strength, quantity, and expiration date of the prescribed drug; and (F) name, address, and phone number of the pharmacy or dispensing location, and the name of the dispensing practitioner.'
        ),
        sop_loc="§6.3 Medication Management (no explicit tamper-resistant packaging or label-content requirement)",
        sop_quote='§6.3: All medications are stored in a double-locked cabinet/cart. Controlled substances are counted and documented at every shift change. Medications are administered only by RN-delegated staff.',
        status="Gap",
        severity="Medium",
        strip_flag="N",
        strip_note="No statutory citation in SOP (gap is absence of policy).",
        finding=(
            "The SOP §6.3 does not explicitly require tamper-resistant medication packaging per .0209(b)(2), nor does it explicitly verify the 6 label-content items per .0209(b)(3). "
            "While the pharmacy typically handles these requirements, the facility has a duty to verify incoming medications meet tamper-resistance and label-content standards before accepting them. "
            "This is a Medium severity gap. The QP should add to §6.3 an explicit policy that the RN (or designated DCP) verifies upon receipt of each medication that: (1) packaging is tamper-resistant; (2) the label contains all 6 .0209(b)(3) items. "
            "Discrepancies are returned to the pharmacy for correction before administration."
        ),
        remediation="v2.23: Add to §6.3 an explicit medication receipt-verification policy per .0209(b)(2)-(3).",
    ),
    dict(
        id="M-042",
        rule=".0209(c)(1)-(5)",
        rule_title="MEDICATION — Administration: written order, self-administration, licensed/RN-trained, MAR contents",
        rule_text=(
            '(c)(1) Drugs administered only on written order of authorized prescriber; (2) self-administration only when authorized in writing by physician; (3) medications including injections administered only by licensed persons or by unlicensed persons trained by RN/pharmacist/qualified person and privileged to prepare and administer; '
            '(4) MAR of all drugs administered shall be kept current, recorded immediately after administration, including (A) client\'s name, (B) name/strength/quantity of drug, (C) instructions for administering, (D) date and time administered, (E) name or initials of person administering; (5) client requests for medication changes or checks shall be recorded and kept with MAR file followed up by appointment or consultation with physician.'
        ),
        sop_loc="§6.3 Medication Management; Protocol 5 Medication Administration Protocol; Form 7 Full Service Note Template",
        sop_quote='§6.3: Staff follow the "5 Rights" (right youth, right med, right dose, right route, right time) and document administration on the MAR immediately. Protocol 5: Verify the "5 Rights" against the MAR; verify youth identity; pour medication into a labeled cup; observe swallowing; check the mouth for "cheeking"; initial the MAR immediately.',
        status="Met",
        severity="Info",
        strip_flag="N",
        strip_note="No statutory citation to strip.",
        finding=(
            "§6.3 and Protocol 5 comprehensively address .0209(c) administration requirements: 5 Rights verification, immediate MAR documentation, identity verification, swallowing observation, cheeking check. "
            "The 5 MAR content items (.0209(c)(4)(A)-(E)) are operationally satisfied by the standard MAR format. RN delegation satisfies .0209(c)(3). "
            "No corrective action required."
        ),
        remediation="No operational change.",
    ),
    dict(
        id="F-013",
        rule=".0209(d)(1)-(4)",
        rule_title="MEDICATION — Disposal: documentation, controlled substances, post-discharge",
        rule_text=(
            '(d)(1) All prescription and non-prescription medication shall be disposed of in a manner that guards against diversion or accidental ingestion. '
            '(2) Non-controlled substances shall be disposed of by incineration, flushing into septic or sewer system, or by transfer to a local pharmacy for destruction. A record of the medication disposal shall be maintained by the program. Documentation shall specify the client\'s name, medication name, strength, quantity, disposal date and method, the signature of the person disposing of medication, and the person witnessing destruction. '
            '(3) Controlled substances shall be disposed of in accordance with the North Carolina Controlled Substances Act, G.S. 90, Article 5. '
            '(4) Upon discharge of a patient or resident, the remainder of his or her drug supply shall be disposed of promptly unless it is reasonably expected that the patient or resident shall return to the facility and in such case, the remaining drug supply shall not be held for more than 30 calendar days after the date of discharge.'
        ),
        sop_loc="§6.3 Medication Management (no explicit disposal documentation policy); §3.4 Discharge (medications transferred to guardian)",
        sop_quote='§3.4: Medications are transferred to the guardian with a signed transfer form. §6.3: (no disposal documentation policy)',
        status="Gap",
        severity="Medium",
        strip_flag="Y",
        strip_note='Strip "North Carolina Controlled Substances Act, G.S. 90, Article 5" statutory citation; replace with "the state controlled substances act."',
        finding=(
            "The SOP §6.3 does not explicitly address medication disposal documentation per .0209(d)(2). While §3.4 addresses medication transfer to the guardian at discharge (which is the preferred outcome), "
            "the SOP does not address disposal of medications that cannot be transferred (e.g., expired medications, medications for youth who did not return, controlled substances per .0209(d)(3)). "
            "This is a Medium severity gap. The QP should add to §6.3 an explicit medication disposal policy: "
            "(1) non-controlled substances disposed by incineration, sewer, or pharmacy transfer, with documentation of client name, med name, strength, quantity, disposal date/method, disposer signature, witness signature; "
            "(2) controlled substances disposed per the state Controlled Substances Act; "
            "(3) post-discharge medications not transferred to guardian are disposed promptly, or held no more than 30 calendar days if return is expected."
        ),
        remediation="v2.23: Add to §6.3 an explicit medication disposal documentation policy per .0209(d)(1)-(4).",
    ),
    dict(
        id="M-043",
        rule=".0209(e)(1)(A)-(E)",
        rule_title="MEDICATION — Storage: locked cabinet 59-86°F, refrigerated 36-46°F, separate per client, separate external/internal",
        rule_text=(
            'All medication shall be stored: (A) in a securely locked cabinet in a clean, well-lighted, ventilated room between 59º and 86º F.; '
            '(B) in a refrigerator, if required, between 36º and 46º F. If the refrigerator is used for food items, medications shall be kept in a separate, locked compartment or container; '
            '(C) separately for each client; (D) separately for external and internal use; (E) in a secure manner if approved by a physician for a client to self-medicate.'
        ),
        sop_loc="§6.3 Medication Management",
        sop_quote='§6.3: All medications are stored in a double-locked cabinet/cart. Controlled substances are counted and documented at every shift change.',
        status="Partial",
        severity="Medium",
        strip_flag="N",
        strip_note="No statutory citation in SOP.",
        finding=(
            "The SOP §6.3 addresses .0209(e)(1)(A) (locked cabinet) but does not explicitly state: "
            "(B) refrigerated medication temperature range (36-46°F) and separate locked compartment if fridge is shared with food; "
            "(C) medications stored separately per client; "
            "(D) medications for external and internal use stored separately; "
            "(E) self-medication storage if physician-approved. "
            "This is a Medium severity gap. The QP should expand §6.3 to explicitly address all 5 .0209(e)(1) storage requirements. Form 5 (Environmental Safety Log) already tracks fridge temperature (<40°F for food safety) but should be updated to also track medication-fridge temperature (36-46°F) if applicable."
        ),
        remediation="v2.23: Expand §6.3 to explicitly address all 5 .0209(e)(1) storage requirements; update Form 5 to track medication-fridge temperature if applicable.",
    ),
    dict(
        id="F-002",
        rule=".0209(f)",
        rule_title="MEDICATION — Psychotropic drug regimen review every 6 months by pharmacist/physician",
        rule_text='"If the client receives psychotropic drugs, the governing body or operator shall be responsible for obtaining a review of each client\'s drug regimen at least every six months. The review shall be to be performed by a pharmacist or physician. The on-site manager shall assure that the client\'s physician is informed of the results of the review when medical intervention is indicated. The findings of the drug regimen review shall be recorded in the client record along with corrective action, if applicable."',
        sop_loc="§6.3 Medication Management; §6.1 Medical Care (no explicit 6-month drug regimen review)",
        sop_quote='§6.1: Each resident has an identified Primary Care Physician (PCP) and psychiatrist upon admission. Physician\'s directions for management of any identified medical conditions shall be documented in the PCP. §6.3: Medication errors, refusals, and adverse reactions are reported to the RN and QP immediately.',
        status="Gap",
        severity="High",
        strip_flag="N",
        strip_note="No statutory citation in SOP (gap is absence of policy).",
        finding=(
            "This is a High severity gap. The SOP does not explicitly require a 6-month psychotropic drug regimen review by a pharmacist or physician per .0209(f). "
            "While §6.1 establishes psychiatrist oversight and §6.3 addresses medication error reporting, neither codifies the .0209(f) 6-month drug regimen review requirement. "
            "This is a High severity finding because .0209(f) is a direct licensure rule — a surveyor will check each youth's chart for documentation of a 6-month psychotropic drug regimen review by a pharmacist or physician. "
            "Failure to document these reviews is a licensure violation and a Medicaid audit risk. "
            "The QP must add a new subsection (proposed §6.3(a) Psychotropic Medication Drug Regimen Review) that: "
            "(1) requires a review of each youth's psychotropic medication regimen at least every 6 months by the facility psychiatrist or a consulting pharmacist; "
            "(2) requires documentation of the review in the youth's clinical record, including findings and any corrective action; "
            "(3) requires the QP to inform the youth's physician of any findings indicating medical intervention is needed; "
            "(4) requires the QP to maintain a Psychotropic Drug Regimen Review Tracking Log showing for each youth on psychotropic meds: review date, reviewer name/credential, next review due date. "
            "This gap should be remediated in v2.23 before the next DHSR MHLC licensure survey."
        ),
        remediation="v2.23: Add new §6.3(a) Psychotropic Medication Drug Regimen Review per .0209(f), including a tracking log (proposed Form 11). Target: September 2026.",
    ),
    dict(
        id="F-014",
        rule=".0209(g)(1)-(3)",
        rule_title="MEDICATION — Education for clients on psychotropic meds",
        rule_text=(
            '(g)(1) Each client started or maintained on a medication by an area program physician shall receive either oral or written education regarding the prescribed medication by the physician or their designee. In instances where the ability of the client to understand the education is questionable, a responsible person shall be provided either oral or written instructions on behalf of the client. '
            '(2) The medication education provided shall be sufficient to enable the client or other responsible person to make an informed consent, to safely administer the medication and to encourage compliance with the prescribed regimen. '
            '(3) The area program physician or designee shall document in the client record that education for the prescribed psychotropic medication was offered and either provided or declined. If provided, it shall be documented in what manner it was provided (either orally or written or both) and to whom (client or responsible person).'
        ),
        sop_loc="§6.3 Medication Management (no explicit medication-education policy)",
        sop_quote='§6.3: (no medication education policy)',
        status="Gap",
        severity="Medium",
        strip_flag="N",
        strip_note="No statutory citation in SOP (gap is absence of policy).",
        finding=(
            "The SOP §6.3 does not explicitly address .0209(g) medication education for clients started or maintained on psychotropic medications. "
            "While the psychiatrist or RN may provide medication education operationally, the SOP does not codify the requirement or the documentation standard. "
            "This is a Medium severity gap. The QP should add to §6.3 an explicit medication education policy: "
            "(1) each youth started or maintained on a psychotropic medication receives oral or written education about the medication from the psychiatrist, RN, or designee; "
            "(2) when the youth's ability to understand is questionable, the guardian receives the education on the youth's behalf; "
            "(3) the education is documented in the clinical record (offered/provided/declined, manner provided, recipient)."
        ),
        remediation="v2.23: Add to §6.3 an explicit medication education policy per .0209(g)(1)-(3).",
    ),
    dict(
        id="M-044",
        rule=".0209(h)",
        rule_title="MEDICATION — Errors and adverse reactions reported immediately to physician/pharmacist",
        rule_text='"Drug administration errors and significant adverse drug reactions shall be reported immediately to a physician or pharmacist. An entry of the drug administered and the drug reaction shall be properly recorded in the drug record. A client\'s refusal of a drug shall be charted."',
        sop_loc="§6.3 Medication Management; Protocol 5 Medication Administration Protocol (Errors step)",
        sop_quote='§6.3: Medication errors, refusals, and adverse reactions are reported to the RN and QP immediately, documented on the MAR, and entered into IRIS as required. Protocol 5 Errors step: Stop, isolate remaining meds, call RN/Psychiatrist, monitor the youth, file IRIS, and notify the guardian.',
        status="Met",
        severity="Info",
        strip_flag="Y",
        strip_note='Strip "IRIS" abbreviation; replace with "the state incident-reporting system."',
        finding=(
            "§6.3 and Protocol 5 comprehensively address .0209(h): errors reported immediately to RN/QP (and operationally to the psychiatrist via Protocol 5 'call RN/Psychiatrist'), documented on MAR, entered into IRIS. "
            "Refusals are charted (Protocol 5: 'Circle R if refused; notify RN and QP'). No corrective action required."
        ),
        remediation="No operational change. Strip abbreviation in v2.23.",
    ),

    # .0210 Research Review Board
    dict(
        id="M-045",
        rule=".0210",
        rule_title="RESEARCH REVIEW BOARD — Likely N/A for residential RTF",
        rule_text=".0210 addresses Research Review Board requirements for facilities conducting research.",
        sop_loc="N/A",
        sop_quote="The SOP does not address research review because the facility does not conduct research.",
        status="N/A",
        severity="Info",
        strip_flag="N",
        strip_note="No statutory citation to strip.",
        finding=(
            "Rule .0210 (Research Review Board) applies to facilities conducting human-subjects research. "
            "Well Spring Intervention LLC is a residential treatment facility and does not conduct research. "
            "If the facility ever partners with a research institution, the QP should consult .0210 and the IRB requirements of the partner institution. "
            "No corrective action required."
        ),
        remediation="No operational change. If research is contemplated in the future, consult .0210.",
    ),

    # ═══════════════════════════════════════════════════════════════════════
    # SECTION D — Open Compliance Flag Resolution: §1.2(h)(b) CCP 8C vs CCP 8D-2
    # ═══════════════════════════════════════════════════════════════════════

    dict(
        id="F-003",
        rule="NC Medicaid Clinical Coverage Policy 8C vs 8D-2",
        rule_title="OPEN COMPLIANCE FLAG — §1.2(h)(b) CCP 8C vs CCP 8D-2",
        rule_text=(
            "SOP Manual v2.22 §1.2(h)(b) flags an open compliance question: the Manual cites 'NC Medicaid CCP 8C' as the Medicaid coverage authority for residential treatment services in legacy reference lines, "
            "but NC DHHS Division of Health Benefits (NCDHB) clinical coverage policy library indicates CCP 8C is 'Outpatient Behavioral Health Services Provided by Direct-Enrolled Providers' — a different benefit category that does not cover residential treatment. "
            "The correct NC Medicaid clinical coverage policy for Residential Treatment Services (Levels I-IV) is CCP 8D-2, 'Residential Treatment Services' (Amended January 1, 2025)."
        ),
        sop_loc="§1.2(h)(b) — OPEN compliance flag; legacy 'CCP 8C' reference lines in §1.2, §2, §3, §4, §5, §6, §10",
        sop_quote='§1.2(h)(b): "A verification review against the NC DHHS Division of Health Benefits (NCDHB) clinical coverage policy library indicates that CCP 8C is Outpatient Behavioral Health Services Provided by Direct-Enrolled Providers — a different benefit category that does not cover residential treatment services. The correct NC Medicaid clinical coverage policy for Residential Treatment Services (Levels I–IV) is CCP 8D-2."',
        status="Contradicts",
        severity="High",
        strip_flag="Y",
        strip_note='Strip all legacy "CCP 8C" references in §1.2, §2, §3, §4, §5, §6, §10 reference lines; replace with "CCP 8D-2" per .1.2(h)(b) resolution. Strip "NC DHHS Division of Health Benefits (NCDHB)" statutory name; replace with "the state Medicaid authority."',
        finding=(
            "AUDIT RESOLUTION: §1.2(h)(b) is RESOLVED in favor of CCP 8D-2. "
            "Primary source: NC Medicaid Clinical Coverage Policy 8D-2, 'Residential Treatment Services' (Amended January 1, 2025), §1.0(c) — available at https://medicaid.ncdhhs.gov/8d-2-residential-treatment-services/download?attachment. "
            "CCP 8C ('Outpatient Behavioral Health Services Provided by Direct-Enrolled Providers') is a different benefit category covering outpatient services only — it does not cover residential treatment. "
            "CCP 8D-1 covers Psychiatric Residential Treatment Facilities (PRTFs) — a separate inpatient benefit. CCP 8D-3/8D-4/8D-5 cover adult ASAM-aligned SUD residential services. "
            "The SOP Manual v2.22 already correctly cites CCP 8D-2 in §1.2(g), §1.9, and §10.9 as the operative authority for the RTS benefit and the room-and-board exclusion. "
            "However, the Manual continues to cite 'CCP 8C' in legacy reference lines at the top of §1.2, §2, §3, §4, §5, §6, and §10, creating internal inconsistency. "
            "This is a High severity finding because the inconsistency creates audit risk: a surveyor or Medicaid auditor reviewing the Manual will encounter contradictory citations. "
            "The QP must execute a global find-and-replace in v2.23 to update all legacy 'CCP 8C' references to 'CCP 8D-2'. The §1.2(h)(b) compliance flag should be rewritten from OPEN to RESOLVED, mirroring the v2.21 resolution of §1.2(h)(a)."
        ),
        remediation="v2.23: Global find/replace 'CCP 8C' → 'CCP 8D-2' in all legacy reference lines (§1.2, §2, §3, §4, §5, §6, §10). Rewrite §1.2(h)(b) from OPEN to RESOLVED.",
    ),
]


# ─── Summary statistics (computed at import time) ───────────────────────────
def summary_stats():
    """Return summary stats dict for use by PDF and XLSX generators."""
    total = len(FINDINGS)
    by_severity = {}
    by_status = {}
    by_strip = {"Y": 0, "N": 0}
    critical_high = []
    for f in FINDINGS:
        sev = f["severity"]
        by_severity[sev] = by_severity.get(sev, 0) + 1
        st = f["status"]
        by_status[st] = by_status.get(st, 0) + 1
        by_strip[f["strip_flag"]] += 1
        if sev in ("Critical", "High"):
            critical_high.append(f)
    return {
        "total_findings": total,
        "by_severity": by_severity,
        "by_status": by_status,
        "by_strip": by_strip,
        "critical_high_findings": critical_high,
    }


if __name__ == "__main__":
    stats = summary_stats()
    print(f"Total findings: {stats['total_findings']}")
    print(f"By severity: {stats['by_severity']}")
    print(f"By status: {stats['by_status']}")
    print(f"Strip flag Y/N: {stats['by_strip']}")
    print(f"Critical+High findings: {len(stats['critical_high_findings'])}")
    for f in stats["critical_high_findings"]:
        print(f"  {f['id']} [{f['severity']}] {f['rule']} — {f['rule_title']}")
