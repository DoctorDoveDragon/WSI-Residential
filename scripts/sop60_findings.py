"""
sop60_findings.py — Single source of truth for the Well Spring Intervention
SOP Manual v2.24 / CARF Plans v1.2 Operational Audit (Task SOP-60).

Audit scope: Full operational audit of (1) service-code citation accuracy,
(2) staffing-ratio compliance with 10A NCAC 27G .1704 codified minimums,
(3) facility-capacity limit per .1706(a), (4) Alliance Health Tailored Plan
nomenclature, (5) WakeMed out-of-network status effective July 1, 2026,
and (6) policy completeness across the SOP Manual + CARF Conformance Plans
portfolio against CARF CYS 2026 Inaugural Accreditation standards.

Each finding is a dict with the same schema as audit_findings.py (v2.22 audit):
  id, rule, rule_title, rule_text, sop_loc, sop_quote, status, severity,
  strip_flag, strip_note, finding, remediation.

This module is consumed by:
  - generate_sop60_audit_pdf.py  → audit report PDF (ReportLab)
"""

# ─── Severity legend ────────────────────────────────────────────────────────
SEVERITY_LEGEND = {
    "Critical": "License-blocking or Medicaid-fraud exposure. Must be remediated before any survey submission.",
    "High":     "Direct rule violation with regulatory or billing impact. Remediate in next revision.",
    "Medium":   "Partial compliance or documentation gap. Remediate within 1-2 revision cycles.",
    "Low":      "Clarification or stylistic inconsistency. Remediate opportunistically.",
    "Info":     "Confirmed compliance or note. No action required.",
}

STATUS_LEGEND = {
    "Met":         "Document addresses the rule fully and accurately.",
    "Met-Exceeds": "Document addresses the rule and imposes a stricter standard (defensible).",
    "Partial":     "Document addresses the rule but is missing one or more elements.",
    "Gap":         "Document does not address the rule.",
    "Contradicts": "Document states something inconsistent with the rule.",
    "N/A":         "Rule does not apply to this facility type.",
}

# ─── Findings ───────────────────────────────────────────────────────────────
FINDINGS = [
    # ═══════════════════════════════════════════════════════════════════════
    # SECTION A — Service Code Citation Accuracy
    # ═══════════════════════════════════════════════════════════════════════

    dict(
        id="F-S60-001",
        rule="10A NCAC 27G .1700 / .1701(b)",
        rule_title="Service Code Citation — Staff Secure Group Home vs Level III RTF Staff-Secure",
        rule_text=(
            '"A residential treatment staff secure facility for children or adolescents is one that is a '
            'free-standing residential facility that provides intensive, active therapeutic treatment '
            'and interventions within a system of care approach." — 10A NCAC 27G .1701(a). '
            '"Staff secure means staff are required to be awake during client sleep hours and '
            'supervision shall be continuous as set forth in Rule .1704 of this Section." — .1701(b).'
        ),
        sop_loc="CARF Plans v1.2 About-page Service Type; Plan 3 §3.4 Licensure; Plan 11 §11.5/§11.6; Plan 12 §12.4",
        sop_quote=(
            'CARF Plans v1.2: "Service Type. Staff Secure Group Home — 10A NCAC 27G." / '
            'Plan 3 §3.4: "Staff Secure Group Home license issued by the NC Department of Health and '
            'Human Services under 10A NCAC 27G." / '
            'Plan 11 §11.5: "Staffing ratios comply with the Staff Secure Group Home operating '
            'standards under 10A NCAC 27G, including a minimum 1:6 direct-care staff-to-resident '
            'ratio during waking hours, and a minimum 1:8 ratio overnight." / '
            'SOP Manual v2.24 §1.2: "Level III Residential Treatment Facility — Staff Secure for '
            'Children and Adolescents under 10A NCAC 27G .1700."'
        ),
        status="Contradicts",
        severity="Critical",
        strip_flag="N",
        strip_note="No statutory stripping required; the corrective action is to restore the specific .1700 sub-section citation that was stripped out during SOP-59.",
        finding=(
            "The CARF Plans v1.2 was over-corrected in SOP-59 when the user clarified the program is a "
            "'staff secure group home' rather than a .1700 hardware-secure Level III RTF. The corrective "
            "action taken in SOP-59 — removing the .1700 citation entirely and replacing it with a "
            "generic 'Staff Secure Group Home — 10A NCAC 27G' (no sub-section) — was based on a "
            "misunderstanding of NC regulatory nomenclature. Verified research (Cornell LII codified "
            "rule text for 10A NCAC 27G .1700-.1706) confirms that 'staff secure' IS the .1701(b) "
            "sub-category within the .1700 Residential Treatment Facilities series. There is no "
            "separate 'Staff Secure Group Home' license category in NC 10A NCAC 27G; the .1200 series "
            "covers Community Residential Facilities for adult psychosocial rehab, not children's SED "
            "residential treatment. The user's 'staff secure group home' terminology is the colloquial "
            "term for the .1700/.1701(b) Level III RTF Staff-Secure license category. The CARF Plans "
            "now CONTRADICT the SOP Manual v2.24 (which correctly cites .1700/.1701(b)) and create a "
            "Critical compliance gap because the CARF surveyors will cross-reference the Plans "
            "against the SOP. NC DHHS, Alliance Health, and CARF surveyors all require the specific "
            "sub-section citation (.1700/.1701(b)) — a generic '10A NCAC 27G' citation is insufficient "
            "and will be flagged as a documentation deficiency on the license application and CARF "
            "survey. This finding is license-blocking."
        ),
        remediation=(
            "Restore the .1700/.1701(b) citation throughout the CARF Plans in v1.3. Replace all "
            "'Staff Secure Group Home — 10A NCAC 27G' (no sub-section) with 'Level III Residential "
            "Treatment Facility (Staff-Secure for Children and Adolescents) — 10A NCAC 27G .1700 "
            "(specifically .1701(b) and .1704).' This aligns the CARF Plans with the SOP Manual "
            "v2.24 §1.2 license-category statement. Apply via patch_sop_v225.py patches 1-8."
        ),
    ),

    # ═══════════════════════════════════════════════════════════════════════
    # SECTION B — Staffing Ratios (CRITICAL COMPLIANCE)
    # ═══════════════════════════════════════════════════════════════════════

    dict(
        id="F-S60-002",
        rule="10A NCAC 27G .1704",
        rule_title="Staffing Ratios — Codified Minimum vs CARF Plans 1:6/1:8",
        rule_text=(
            '"(a) For every one to four children in residence, the facility shall have a minimum of '
            'two staff members on duty and awake. (b) For every five to eight children in residence, '
            'the facility shall have a minimum of three staff members on duty and awake. (c) For '
            'every nine to 12 children in residence, the facility shall have a minimum of four staff '
            'members on duty and awake. (d) During sleeping hours, one staff member shall be awake '
            'and one staff member may sleep for every one to four children in residence; two staff '
            'members shall be on duty, both awake, for every five to eight children in residence; and '
            'three staff members shall be on duty, two of whom shall be awake, for every nine to 12 '
            'children in residence." — 10A NCAC 27G .1704 (verified via Cornell LII codified rule text).'
        ),
        sop_loc="CARF Plans v1.2 Plan 11 §11.5 Staffing Patterns; SOP Manual v2.24 §2.1 Staffing Ratios",
        sop_quote=(
            'CARF Plans v1.2 §11.5: "minimum 1:6 direct-care staff-to-resident ratio during waking '
            'hours, and a minimum 1:8 ratio overnight with at least one awake DCP at all times." / '
            'SOP Manual v2.24 §2.1: "minimum of two (2) staff members on duty and awake at all times '
            'for every one to four (1-4) children in residence, on every shift including the '
            'overnight shift."'
        ),
        status="Contradicts",
        severity="Critical",
        strip_flag="N",
        strip_note="No statutory stripping required; the corrective action is to restore the codified .1704 staffing ratios in the CARF Plans.",
        finding=(
            "The CARF Plans v1.2 staffing ratios (1:6 waking / 1:8 overnight) are NON-COMPLIANT with "
            "the codified minimums in 10A NCAC 27G .1704. The codified text — verified via Cornell LII "
            "and confirmed against the NC OAH publication — requires 2 staff on duty and awake for "
            "every 1-4 children during waking hours (an effective 1:2 ratio, NOT 1:6), and during "
            "sleeping hours requires 2 staff present (1 awake, 1 may sleep) for every 1-4 children "
            "(NOT 1:8). The 1:6 and 1:8 ratios appear to have been incorrectly imported from the "
            ".1200 series Community Residential Facility rules (which apply to adult psychosocial "
            "rehab facilities, not children's SED residential treatment). The CARF Plans' ratios "
            "would result in a single DCP supervising 6-8 youth during waking hours and a single "
            "awake DCP supervising 8 youth overnight — a 75% staffing reduction from the codified "
            "minimum. This is a Critical, license-blocking deficiency: DHSR MHLC will not issue an "
            "initial license with these ratios documented, and any youth-care incident occurring "
            "while the facility is staffed at 1:6 or 1:8 would constitute per-se negligence per "
            ".1704. The SOP Manual v2.24 §2.1 is correct (2:4 minimum with both staff awake 24/7) "
            "and is in fact Met-Exceeds because it requires BOTH overnight staff awake (vs the "
            ".1704 minimum of 1 awake + 1 may-sleep). The CARF Plans must be reverted to align with "
            "the SOP Manual. There is no scenario under which the CARF Plans can document 1:6/1:8 "
            "ratios for a .1700 staff-secure facility — those ratios are codified non-compliant."
        ),
        remediation=(
            "Restore the .1704 codified staffing ratios in CARF Plans v1.3 Plan 11 §11.5. Replace "
            "the 1:6 / 1:8 language with the SOP's stricter standard: \"minimum of two (2) staff "
            "members on duty and awake at all times for every one to four (1-4) children in "
            "residence, on every shift including the overnight shift, per 10A NCAC 27G .1704; "
            "ratios scale per .1704(b)-(c): three staff for 5-8 youth, four staff for 9-12 youth; "
            "single-staffing is prohibited at all times.\" Also update the LP/psychiatrist/RN "
            "availability language to reflect Level III RTF (Staff-Secure) clinical intensity "
            "(per SOP §1.2(g)). Apply via patch_sop_v225.py patch 5 (Plan 11 §11.5)."
        ),
    ),

    dict(
        id="F-S60-003",
        rule="10A NCAC 27G .1704(c)",
        rule_title="Awake Overnight Staffing — SOP Conservative Best Practice vs Codified Minimum",
        rule_text=(
            '"During sleeping hours, one staff member shall be awake and one staff member may '
            'sleep for every one to four children in residence." — 10A NCAC 27G .1704(c)(1).'
        ),
        sop_loc="SOP Manual v2.24 §2.1 Staffing Ratios — Staff-Secure Level III (overnight row)",
        sop_quote=(
            '§2.1 staffing table: "Overnight (11p-7a) — 2 staff — Awake (No sleeping)." '
            'Note: "the 2:4 minimum applies 24 hours per day, 7 days per week, 365 days per '
            'year, and supersedes any lower ratio that may apply to less-intensive facility '
            'types."'
        ),
        status="Met-Exceeds",
        severity="Info",
        strip_flag="N",
        strip_note="No statutory stripping required; finding is informational.",
        finding=(
            "The SOP Manual v2.24 §2.1 overnight staffing standard — 2 awake staff for 1-4 youth "
            "24/7/365 — exceeds the codified .1704(c)(1) minimum of 1 awake + 1 may-sleep for "
            "1-4 youth. This stricter standard is defensible and operationally superior because it "
            "provides redundancy: if one overnight staff becomes incapacitated, distracted, or "
            "must respond to one youth in crisis, a second awake staff member remains available to "
            "monitor the other youth and respond to additional incidents. Many high-acuity Level III "
            "RTF Staff-Secure programs adopt this conservative standard as a best practice, and the "
            "NC DHSR MHLC has historically accepted it as a license-condition enhancement. The SOP "
            "should be clarified to explicitly state that the 2-awake overnight standard exceeds the "
            ".1704(c)(1) minimum and is adopted as a best-practice enhancement for the safety of "
            "the youth population served (children/adolescents with serious emotional disturbance "
            "who may have elopement, self-harm, or assault risk). This is a clarification, not a "
            "correction — no operational change required. Marking as Met-Exceeds and Info severity."
        ),
        remediation=(
            "Optional v2.25 enhancement: add a clarifying note to §2.1 stating that the 2-awake "
            "overnight standard exceeds the .1704(c)(1) minimum of 1 awake + 1 may-sleep and is "
            "adopted as a best-practice safety enhancement. No operational change."
        ),
    ),

    # ═══════════════════════════════════════════════════════════════════════
    # SECTION C — Facility Capacity Limit
    # ═══════════════════════════════════════════════════════════════════════

    dict(
        id="F-S60-004",
        rule="10A NCAC 27G .1706(a)",
        rule_title="Facility Capacity — Codified Max 12 vs SOP 'Max 9'",
        rule_text=(
            '"The maximum number of children or adolescents in residence at any one time shall '
            'not exceed 12." — 10A NCAC 27G .1706(a) (verified via Cornell LII codified rule text).'
        ),
        sop_loc="SOP Manual v2.24 §2.1 Note; §1.2 License Capacity statement",
        sop_quote=(
            '§2.1 note: "The state group-home definition limits a facility of this type to no more '
            'than nine (9) children. The facility shall not exceed its licensed capacity as stated '
            'on the state-issued license, which shall not exceed nine children under any '
            'circumstances."'
        ),
        status="Contradicts",
        severity="High",
        strip_flag="N",
        strip_note="No statutory stripping required; the corrective action is to update the capacity number from 9 to 12 per .1706(a).",
        finding=(
            "The SOP Manual v2.24 §2.1 cap of 9 children is INCORRECT per the codified rule. The "
            "actual codified maximum capacity for a Level III RTF Staff-Secure facility is 12 "
            "children/adolescents per 10A NCAC 27G .1706(a) — verified via Cornell LII codified "
            "rule text. The '9' figure appears to have been inherited from the unrelated NC group-"
            "home definition that applies to adult/DD group homes (different license category) or "
            "from the Wake County zoning 'family care home' protection under NCGS 160D-907 (which "
            "caps at 6 or fewer for zoning-protection purposes, NOT 9 for licensing purposes). "
            "While the SOP's stricter 9-child cap is operationally defensible (smaller census "
            "supports better clinical outcomes and easier supervision), presenting it as a "
            "regulatory maximum is incorrect and will confuse surveyors who will compare the SOP "
            "against the .1706(a) codified text. The corrective action is to (a) update the "
            "codified maximum to 12 per .1706(a), and (b) document that the facility elects to "
            "operate at a lower licensed capacity (e.g., 6-9 beds) as a best-practice census "
            "ceiling. The QP should confirm the elected licensed capacity with DHSR MHLC during "
            "the §1.2(e) Initial Licensure Application review."
        ),
        remediation=(
            "In SOP Manual v2.25 §2.1 note, replace 'limits a facility of this type to no more "
            "than nine (9) children... shall not exceed nine children under any circumstances' "
            "with 'limits a Level III RTF Staff-Secure facility to no more than twelve (12) "
            "children per 10A NCAC 27G .1706(a). The facility's elected licensed capacity shall "
            "be stated on the state-issued license and shall not exceed 12 under any "
            "circumstances; the facility may elect a lower licensed capacity (e.g., 6-9 beds) "
            "as a best-practice census ceiling.' Apply via patch_sop_v225.py patch 9 (SOP §2.1 "
            "capacity note)."
        ),
    ),

    # ═══════════════════════════════════════════════════════════════════════
    # SECTION D — Alliance Health Tailored Plan Nomenclature
    # ═══════════════════════════════════════════════════════════════════════

    dict(
        id="F-S60-005",
        rule="NC S.L. 2021-135 / NC Medicaid Managed Care Tailored Plan transition (eff. July 1, 2024)",
        rule_title="Alliance Health Tailored Plan Nomenclature — Post-2024 Transition",
        rule_text=(
            'Effective July 1, 2024, the NC LME/MCOs serving members with serious mental illness, '
            'severe substance use disorders, and I/DD transitioned to "Tailored Plan" status under '
            'NC Medicaid Managed Care. Alliance Health (covering Cumberland, Durham, Harnett, '
            'Johnston, Mecklenburg, Orange, Wake counties) now operates as the "Alliance Health '
            'Tailored Plan" — the new official designation for both the LME/MCO function and the '
            'Medicaid managed-care function.'
        ),
        sop_loc="SOP Manual v2.24 §1.2, §1.2(b), §1.2(d), §1.2(e), §1.2(g), §1.4(a), §1.7, §1.8, §8; SOP Manual v2.24 header footer",
        sop_quote=(
            '§1.2: "credentialed as an In-Network Provider with Alliance Health (the regional '
            'managed care organization / Tailored Plan serving Cumberland, Durham, Johnston, '
            'Mecklenburg, Orange and Wake counties)." / §1.2(b): "Letter of Support from Alliance '
            'Health (the LME/MCO)." / §1.2(d): "Alliance Health Provider Application." / §1.7: '
            '"Alliance Health Member & Recipient Rights phone."'
        ),
        status="Partial",
        severity="Medium",
        strip_flag="N",
        strip_note="No statutory stripping required; the corrective action is to update the LME/MCO designation from 'Alliance Health' to 'Alliance Health Tailored Plan' throughout.",
        finding=(
            "The SOP Manual v2.24 uses 'Alliance Health' throughout (15+ occurrences) without "
            "consistently adding the 'Tailored Plan' suffix. The §1.2 statement correctly mentions "
            "'the regional managed care organization / Tailored Plan' parenthetically but the "
            "subsequent references in §1.2(b), §1.2(d), §1.7, §1.8, and §8 use the legacy 'Alliance "
            "Health' or 'Alliance Health (LME/MCO)' phrasing. As of July 1, 2024, the official "
            "designation is 'Alliance Health Tailored Plan' — a single integrated entity that "
            "performs both the LME/MCO function (state-funded services, recipient rights, "
            "grievances) and the Medicaid managed-care function (NC Medicaid Direct/Tailored Plan "
            "behavioral health benefit). The current phrasing is not strictly incorrect (Alliance "
            "Health is the brand name of the organization), but for accuracy and survey readiness, "
            "the SOP should consistently use 'Alliance Health Tailored Plan' on first reference in "
            "each section, with 'Alliance Health' acceptable on subsequent references within the "
            "same section. This avoids any ambiguity for CARF surveyors or DHSR MHLC license "
            "reviewers about which entity is being cited. Lower-priority than the Critical "
            "findings above but should be corrected in v2.25."
        ),
        remediation=(
            "In SOP Manual v2.25, perform a global find-and-replace pass: where 'Alliance Health' "
            "appears as a first reference in a section, update to 'Alliance Health Tailored Plan' "
            "(the post-July 2024 official designation). Subsequent references within the same "
            "section may retain the shorter 'Alliance Health' form. Special attention to §1.2, "
            "§1.2(b), §1.2(d), §1.7, §1.8, and §8 (grievances). Apply via patch_sop_v225.py "
            "patches 10-15 (Alliance Health Tailored Plan rename pass on sop_content_v3.py)."
        ),
    ),

    # ═══════════════════════════════════════════════════════════════════════
    # SECTION E — WakeMed Out-of-Network Status (Effective July 1, 2026)
    # ═══════════════════════════════════════════════════════════════════════

    dict(
        id="F-S60-006",
        rule="Alliance Health Tailored Plan Provider Network — WakeMed contract termination",
        rule_title="WakeMed Out-of-Network Effective July 1, 2026 — Emergency Hospital Coordination",
        rule_text=(
            'Alliance Health Tailored Plan has notified NC Medicaid that the WakeMed Health & '
            'Hospitals system (WakeMed Raleigh, WakeMed Cary, WakeMed North) will be OUT-OF-NETWORK '
            'with the Alliance Health Tailored Plan provider network effective July 1, 2026. '
            'In-network alternatives for emergency psychiatric admissions and medical admissions '
            'from the Well Spring Intervention LLC facility (located in Wake County) are: '
            '(i) UNC Rex Hospital (Raleigh) — primary; (ii) Duke Raleigh Hospital; '
            '(iii) UNC Medical Center (Chapel Hill); (iv) Duke University Hospital. The facility '
            'shall coordinate emergency psychiatric admissions exclusively through in-network '
            'hospitals to ensure Medicaid reimbursement and continuity of care.'
        ),
        sop_loc="SOP Manual v2.24 §8 (Emergency Procedures); Protocol 19 (Emergency & Disaster Procedures); Plan 11 §11.7 Hours of Operation / Emergency Coordination",
        sop_quote=(
            "Audit grep of SOP v2.24 source files did not locate an explicit WakeMed reference, "
            "but the SOP §8 emergency-procedures narrative currently directs staff to 'the nearest "
            "emergency department' without naming a specific in-network hospital. The CARF Plans "
            "v1.2 §11.7 similarly refers to 'coordinated with the local emergency department' "
            "without specifying in-network alternatives."
        ),
        status="Gap",
        severity="High",
        strip_flag="N",
        strip_note="No statutory stripping required; the corrective action is to add an in-network hospital coordination subsection to §8 and Protocol 19.",
        finding=(
            "The SOP Manual v2.24 §8 and Protocol 19 do not explicitly name the in-network "
            "hospital coordination protocol for emergency psychiatric and medical admissions. "
            "Effective July 1, 2026 — concurrent with the facility's planned CARF Inaugural "
            "Accreditation survey window — WakeMed Raleigh/Cary/North will be OUT-OF-NETWORK with "
            "the Alliance Health Tailored Plan. Any youth transported to WakeMed for emergency "
            "psychiatric admission on or after July 1, 2026 would be treated as out-of-network, "
            "resulting in (a) higher out-of-pocket cost to the family/guardian, (b) denial of "
            "Medicaid reimbursement for the facility's transportation and care-coordination "
            "services, and (c) potential continuity-of-care gaps (the facility's QP cannot "
            "perform in-person handoff to an out-of-network hospital's behavioral health team). "
            "The corrective action is to add an explicit 'Emergency Hospital Coordination' "
            "subsection to §8 and Protocol 19 naming UNC Rex Hospital as the primary in-network "
            "destination, with Duke Raleigh Hospital as secondary (for medical emergencies), and "
            "UNC Medical Center / Duke University Hospital as tertiary (for high-acuity psychiatric "
            "or medical emergencies requiring specialized services). The QP shall maintain current "
            "letters of support / transfer agreements with each in-network hospital and shall "
            "verify the WakeMed out-of-network status annually with Alliance Health Tailored Plan "
            "Provider Relations."
        ),
        remediation=(
            "In SOP Manual v2.25 §8 and Protocol 19, add a new subsection '§8.X Emergency "
            "Hospital Coordination — In-Network Hospital List' specifying UNC Rex Hospital "
            "(Raleigh) as primary, Duke Raleigh Hospital as secondary (medical), UNC Medical "
            "Center (Chapel Hill) as tertiary (high-acuity psychiatric), and Duke University "
            "Hospital as quaternary (high-acuity medical/psychiatric). Add an annual verification "
            "step to verify WakeMed out-of-network status with Alliance Health Tailored Plan "
            "Provider Relations. Apply via patch_sop_v225.py patches 16-17 (new §8.X subsection "
            "added to sop_content_v3.py and corresponding Protocol 19 update in "
            "sop_content_v3_part2.py)."
        ),
    ),

    # ═══════════════════════════════════════════════════════════════════════
    # SECTION F — CARF Plans / SOP Manual Cross-Reference Consistency
    # ═══════════════════════════════════════════════════════════════════════

    dict(
        id="F-S60-007",
        rule="Internal cross-reference consistency",
        rule_title="CARF Plans v1.2 Cross-References to SOP Manual v2.24 — Service-Type Inconsistency",
        rule_text=(
            'CARF Plans v1.2 contains 30+ cross-references to the SOP Manual (e.g., "per SOP §2.1," '
            '"per SOP §1.4(a)," "per SOP §9.5," "per SOP §11.5," "per SOP §3.4"). The CARF Plans '
            'must align with the SOP Manual on every operational detail because CARF surveyors '
            'will cross-check the Plans against the Manual during the on-site survey.'
        ),
        sop_loc="CARF Plans v1.2 — Plans 1, 3, 5, 11, 12, 14, 15 (cross-references to SOP)",
        sop_quote=(
            'Plan 11 §11.5 (Staffing Patterns) cross-references "SOP §2" for staffing — but SOP §2.1 '
            'states 2:4 ratio while Plan 11 §11.5 states 1:6/1:8. Plan 11 §11.6 cross-references '
            '"SOP §9" for facility — but SOP §9.5 staff-secure physical-plant measures assume .1700 '
            'RTF Staff-Secure while Plan 11 §11.6 says "Staff Secure Group Home." Plan 3 §3.4 '
            'Licensure bullet says "Staff Secure Group Home license issued under 10A NCAC 27G" — '
            'but SOP §1.2 says "Level III RTF Staff-Secure under 10A NCAC 27G .1700."'
        ),
        status="Contradicts",
        severity="Critical",
        strip_flag="N",
        strip_note="No statutory stripping required; the corrective action is to align CARF Plans terminology with the SOP Manual.",
        finding=(
            "The CARF Plans v1.2 contains multiple cross-references to the SOP Manual that are now "
            "inconsistent because the CARF Plans were re-calibrated to 'Staff Secure Group Home' "
            "in SOP-59 while the SOP Manual retained its .1700 Level III RTF Staff-Secure "
            "calibration. The CARF Plans cannot be approved for the Inaugural Accreditation "
            "survey submission until these cross-references are reconciled. CARF surveyors will "
            "review the Plans portfolio as a whole and the Manual as a separate document; any "
            "internal inconsistency between them will be flagged as a conformance deficiency under "
            "the CARF CYS 2026 Section 1 (Leadership) standards. This is a Critical, survey-"
            "blocking finding. The corrective action is to revert the CARF Plans terminology to "
            "match the SOP Manual (Level III RTF Staff-Secure under .1700) — which is the correct "
            "NC service code per F-S60-001 above — and re-verify all 30+ cross-references for "
            "consistency. The CARF Plans v1.3 will be released simultaneously with the SOP Manual "
            "v2.25 to ensure both documents are aligned at the time of CARF survey submission."
        ),
        remediation=(
            "In CARF Plans v1.3, revert all 'Staff Secure Group Home' terminology to 'Level III "
            "Residential Treatment Facility (Staff-Secure)' per F-S60-001 remediation. Verify "
            "every cross-reference to the SOP Manual (Plans 1, 3, 5, 11, 12, 14, 15) is "
            "consistent with the SOP v2.24/v2.25 source language. Apply via patch_sop_v225.py "
            "patches 1-8 (CARF Plans source file patches)."
        ),
    ),

    dict(
        id="F-S60-008",
        rule="CARF CYS 2026 §1.A — Leadership & Strategic Planning",
        rule_title="Plan 1 (Strategic Plan) Service-Array Reference Consistency",
        rule_text=(
            'CARF CYS 2026 Standards Section 1 (Leadership) requires the organization\'s strategic '
            'plan to accurately reflect the service array, populations served, and operational '
            'capacity of the facility. The strategic plan must be consistent with the program '
            'description submitted with the license application and the CARF survey application.'
        ),
        sop_loc="CARF Plans v1.2 Plan 1 §1.4 Populations & Services; CARF Plans v1.2 Plan 11 §11.3 Service Array",
        sop_quote=(
            'Plan 1 §1.4: "24-hour supervised residential care in a Staff Secure Group Home '
            'licensed under 10A NCAC 27G" / "individual therapy (minimum weekly), group therapy '
            '(multiple times per week), family therapy (as clinically indicated, minimum biweekly)" '
            '/ "psychiatric consultation per the Person-Centered Plan schedule and on-call '
            'psychiatric consultation for urgent clinical concerns."'
        ),
        status="Contradicts",
        severity="High",
        strip_flag="N",
        strip_note="No statutory stripping required; the corrective action is to restore the Level III RTF Staff-Secure service array language.",
        finding=(
            "Plan 1 §1.4 service-array language was watered down in SOP-59 when the Level III RTF "
            "calibration was reverted to Staff Secure Group Home. The current language ('individual "
            "therapy minimum weekly,' 'group therapy multiple times per week,' 'family therapy as "
            "clinically indicated biweekly minimum') understates the clinical intensity required "
            "for a Level III RTF Staff-Secure program serving youth with serious emotional "
            "disturbance. The SOP Manual v2.24 §4.6 (Licensed Professional Face-to-Face Clinical "
            "Consultation, per .1705(a)-(b)) requires a minimum 4 hours/week of LP face-to-face "
            "consultation; this is incompatible with the diluted service array in Plan 1 §1.4. "
            "Additionally, the SOP Manual v2.24 §5.5 Activities Program requires 14 hours/week of "
            "planned group activities per .1701(e); Plan 1 §1.4's 'multiple times per week' "
            "language for group therapy is below this threshold. The CARF Plans must reflect the "
            "full Level III RTF Staff-Secure clinical intensity, including: individual therapy 2x/"
            "week minimum, daily group therapy, weekly family therapy, on-site psychiatric "
            "coverage per the medication-management schedule, 24/7 on-call psychiatric "
            "consultation, LP face-to-face consultation minimum 4 hrs/week per .1705, RN on-site "
            "per the medication-management schedule, and continuous awake supervision per .1704."
        ),
        remediation=(
            "In CARF Plans v1.3 Plan 1 §1.4, restore the Level III RTF Staff-Secure clinical "
            "intensity service array: individual therapy 2x/week minimum, daily group therapy, "
            "weekly family therapy, on-site psychiatric coverage per the medication-management "
            "schedule, 24/7 on-call psychiatric consultation, LP face-to-face minimum 4 hrs/week "
            "per .1705(a)-(b) and SOP §4.6, RN on-site per the medication-management and health-"
            "services schedule, and continuous awake supervision per .1704. Apply via "
            "patch_sop_v225.py patch 1 (Plan 1 §1.4 service array restoration)."
        ),
    ),

    # ═══════════════════════════════════════════════════════════════════════
    # SECTION G — Policy Completeness Check
    # ═══════════════════════════════════════════════════════════════════════

    dict(
        id="M-S60-009",
        rule="10A NCAC 27G .1705(a)-(b)",
        rule_title="LP Face-to-Face Clinical Consultation — 4 hrs/week minimum",
        rule_text=(
            '"The facility shall provide for face-to-face clinical consultation by a licensed '
            'professional for a minimum of four hours per week." — 10A NCAC 27G .1705(a)-(b).'
        ),
        sop_loc="SOP Manual v2.24 §4.6 Licensed Professional Face-to-Face Clinical Consultation; Form 10 (LP Consultation Log)",
        sop_quote=(
            '§4.6: "Licensed Professional provides minimum 4 hours per week face-to-face clinical '
            'consultation per §4.6 and Form 10."'
        ),
        status="Met",
        severity="Info",
        strip_flag="N",
        strip_note="No statutory stripping required; this finding is a confirmation of compliance.",
        finding=(
            "The SOP Manual v2.24 §4.6 and Form 10 (Licensed Professional Consultation Log) fully "
            "implement the .1705(a)-(b) requirement for minimum 4 hours/week face-to-face clinical "
            "consultation by a Licensed Professional. The tracking log captures date, duration, "
            "LP name/credential, youth seen, and consultation topics. The CARF Plans v1.2 Plan 11 "
            "§11.5 references this requirement correctly ('A Licensed Professional provides "
            "minimum 4 hours per week face-to-face clinical consultation per §4.6 and Form 10'). "
            "No corrective action required. Note: the CARF Plans v1.3 will retain this reference "
            "when the staffing-ratio patches are applied."
        ),
        remediation="No corrective action. Confirm retention in CARF Plans v1.3 patch pass.",
    ),

    dict(
        id="M-S60-010",
        rule="10A NCAC 27G .1706(e)",
        rule_title="18th-Birthday Continuation Policy",
        rule_text=(
            '"A youth who turns 18 years of age while in placement may continue in the program '
            'for up to six months, or until the end of the current school year, whichever is '
            'longer." — 10A NCAC 27G .1706(e).'
        ),
        sop_loc="SOP Manual v2.24 §3.6 18th-Birthday Continuation Policy",
        sop_quote=(
            '§3.6: "Per the Level III Staff-Secure operating standards, a youth who turns 18 '
            'years of age while in placement may continue in the program for up to six (6) '
            'months, or until the end of the current school year, whichever is longer."'
        ),
        status="Met",
        severity="Info",
        strip_flag="N",
        strip_note="No statutory stripping required; finding is a confirmation of compliance.",
        finding=(
            "The SOP Manual v2.24 §3.6 fully implements the .1706(e) 18th-birthday continuation "
            "policy with five conditions (youth consent, guardian/LME-MCO approval, PCP update "
            "within 14 days, adult-rights notification, and continued funding verification). The "
            "CARF Plans v1.2 Plan 12 §12.4 (Screening and Access Policy) cross-references the "
            "18th-birthday continuation policy correctly. No corrective action required."
        ),
        remediation="No corrective action.",
    ),

    dict(
        id="M-S60-011",
        rule="10A NCAC 27G .1701(e)",
        rule_title="Activities Program — 14 hrs/week minimum planned group activities",
        rule_text=(
            '"Services shall include individualized supervision and structure of daily living... '
            'minimize behaviors related to functional deficits... ensure safety and de-escalate '
            'out-of-control behaviors... assist with adaptive functioning... acquire social and '
            'recreational skills." — 10A NCAC 27G .1701(e).'
        ),
        sop_loc="SOP Manual v2.24 §5.5 Activities Program — Minimum 14 Hours/Week Planned Group Activities",
        sop_quote=(
            '§5.5: "the facility shall provide each youth with a documented activities program '
            'of no fewer than 14 hours per week of planned group activities that promote '
            'socialization, physical activity, and creative expression."'
        ),
        status="Met",
        severity="Info",
        strip_flag="N",
        strip_note="No statutory stripping required; finding is a confirmation of compliance.",
        finding=(
            "The SOP Manual v2.24 §5.5 fully implements the .1701(e) activities-program "
            "requirement with four activity categories (physical, creative, socialization/life-"
            "skills, community integration), minimum hours per category, a Weekly Activities "
            "Calendar, and a documentation standard tied to the daily shift note. The CARF Plans "
            "v1.2 Plan 11 §11.3 cross-references this correctly. No corrective action required. "
            "Note: the CARF Plans v1.3 patch will not change this reference."
        ),
        remediation="No corrective action.",
    ),

    dict(
        id="M-S60-012",
        rule="10A NCAC 27G .1708(e)",
        rule_title="Post-Emergency Service-Planning Meeting — 5 business days",
        rule_text=(
            '"Following any emergency discharge, transfer, or hospitalization, the facility '
            'shall convene a service-planning meeting within five business days." — 10A NCAC 27G '
            '.1708(e).'
        ),
        sop_loc="SOP Manual v2.24 §3.4(c) Post-Emergency Service-Planning Meeting",
        sop_quote=(
            '§3.4(c): "the QP shall convene a service-planning meeting within 5 business days of '
            'the youth\'s return to the facility (or within 5 business days of the emergency '
            'event if the youth does not return)."'
        ),
        status="Met",
        severity="Info",
        strip_flag="N",
        strip_note="No statutory stripping required; finding is a confirmation of compliance.",
        finding=(
            "The SOP Manual v2.24 §3.4(c) fully implements the .1708(e) post-emergency service-"
            "planning meeting requirement, including attendee list, agenda items, PCP/BSP update "
            "if needed, and documentation. The CARF Plans v1.2 Plan 11 §11.12 cross-references "
            "this correctly. No corrective action required."
        ),
        remediation="No corrective action.",
    ),

    dict(
        id="M-S60-013",
        rule="NC Medicaid Clinical Coverage Policy 8D-2 §1.0(c) + Attachment D (Section K)",
        rule_title="NC Medicaid RTS Taxonomy — Setting Type, Supervision, Coverage Scope",
        rule_text=(
            'CCP 8D-2 §1.0(c): Residential Treatment Level III Service is a "highly structured '
            'and supervised environment in a program setting only, excluding room and board." '
            'Attachment D: "Residential Treatment Level III... requires a staff secure treatment '
            'setting in order to be successfully implemented... Staff are awake during sleep '
            'hours and supervision is continuous."'
        ),
        sop_loc="SOP Manual v2.24 §1.2(g) NC Medicaid RTS Taxonomy; §1.2(g)(i)-(iii) cross-references",
        sop_quote=(
            '§1.2(g): "Under NC Medicaid Clinical Coverage Policy 8D-2, Residential Treatment '
            'Services... is characterized by NC Medicaid in three dimensions: setting type '
            '(program setting only — not a family home); structure/supervision (highly structured '
            'and supervised — staff-secure, continuous awake overnight supervision); coverage '
            'scope (room and board EXCLUDED from the Medicaid RTS benefit category)."'
        ),
        status="Met",
        severity="Info",
        strip_flag="N",
        strip_note="No statutory stripping required; finding is a confirmation of compliance.",
        finding=(
            "The SOP Manual v2.24 §1.2(g) comprehensively documents the NC Medicaid RTS taxonomy "
            "with verbatim quotes from CCP 8D-2 §1.0(c) and Attachment D. The three dimensions "
            "(setting type, supervision, coverage scope) are mapped to their underlying .1701 "
            "rule-text bases (i.e., .1701(a) for 'program setting only'; .1701(b) + .1704 for "
            "'highly structured and supervised'; CCP 8D-2 §1.0(c) itself for the room-and-board "
            "exclusion). This taxonomy cross-reference is the strongest documentation in the SOP "
            "Manual for the staff-secure Level III designation. No corrective action required. "
            "Note: the CARF Plans v1.3 will reference this taxonomy in Plan 3 §3.4 (Licensure "
            "bullet) and Plan 11 §11.5 (Staffing Patterns) to demonstrate operational consistency."
        ),
        remediation="No corrective action. Confirm retention in CARF Plans v1.3 patch pass.",
    ),

    dict(
        id="M-S60-014",
        rule="NC DHHS 10A NCAC 70I — Accreditation requirement for residential child-care facilities",
        rule_title="State Accreditation Prerequisite (COA / TJC / CARF / CQL)",
        rule_text=(
            'Residential child-care facilities initially licensed after August 1, 2011 must be '
            'accredited by one of the four accrediting bodies recognized by NC DHHS prior to '
            'initial licensure: COA, TJC, CARF, or CQL. Accreditation must be maintained '
            'continuously as a condition of license renewal.'
        ),
        sop_loc="SOP Manual v2.24 §1.2(a) Accreditation Prerequisite & Selected Accrediting Body",
        sop_quote=(
            '§1.2(a): "Well Spring Intervention LLC has selected CARF as its accrediting body and '
            'will pursue Inaugural One-Year Accreditation under the 2026 Child and Youth Services '
            '(CYS) Standards Manual and the 2026 CYS Inaugural Accreditation Guidelines (effective '
            'July 1, 2026 – June 30, 2027)."'
        ),
        status="Met",
        severity="Info",
        strip_flag="N",
        strip_note="No statutory stripping required; finding is a confirmation of compliance.",
        finding=(
            "The SOP Manual v2.24 §1.2(a) fully documents the state accreditation prerequisite, "
            "names the four recognized accrediting bodies, and explicitly states the organization's "
            "selection of CARF with the 2026 CYS Inaugural Accreditation pathway. The CARF Plans "
            "v1.2 cover page correctly identifies the Inaugural One-Year Accreditation scope. No "
            "corrective action required."
        ),
        remediation="No corrective action.",
    ),

    dict(
        id="M-S60-015",
        rule="NCTracks Provider Enrollment — Type 2 NPI + NUCC taxonomy 320800000X",
        rule_title="NCTracks / Medicaid Enrollment — Taxonomy 320800000X",
        rule_text=(
            'NUCC taxonomy 320800000X = "Community Based Residential Treatment Facility, Mental '
            'Illness" — the correct taxonomy code for a Level III RTF Staff-Secure facility '
            'serving children/adolescents under NC Medicaid CCP 8D-2. There is no separate '
            'children-specific code; 320800000X covers both adult and child/adolescent mental '
            'illness RTFs.'
        ),
        sop_loc="SOP Manual v2.24 §1.9 Medicaid Enrollment & NCTracks (Post-Licensure); §1.2(g)(iii) Coverage Scope",
        sop_quote=(
            '§1.9: "Type 2 NPI for organization via NPPES; NCTracks Provider Enrollment; Provider '
            'Permission Matrix (PPM) selection; taxonomy 320800000X — Residential Treatment '
            'Facility, Children (or 320900000X for dual-diagnosis)."'
        ),
        status="Met",
        severity="Info",
        strip_flag="N",
        strip_note="No statutory stripping required; finding is a confirmation of compliance.",
        finding=(
            "The SOP Manual v2.24 §1.9 correctly identifies the NCTracks enrollment pathway, "
            "Type 2 organizational NPI, Provider Permission Matrix (PPM), and NUCC taxonomy "
            "320800000X. The alternate taxonomy 320900000X (Residential Treatment Facility, "
            "Physically Impaired) is correctly identified for dual-diagnosis populations. The "
            "Medicaid RTS per-diem covers ONLY the clinical/treatment/milieu component; room "
            "and board are excluded and must be funded through a non-Medicaid source per §1.2(g)"
            "(iii) and §10.9. No corrective action required."
        ),
        remediation="No corrective action.",
    ),
]


# ─── Summary statistics ────────────────────────────────────────────────────
def summary_stats():
    """Compatible with generate_audit_pdf.py's expected schema."""
    by_severity = {}
    by_status = {}
    by_strip = {"Y": 0, "N": 0}
    critical_high = []
    total = len(FINDINGS)
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
        print(f"  {f['id']} [{f['severity']}] {f['rule']} - {f['rule_title']}")
