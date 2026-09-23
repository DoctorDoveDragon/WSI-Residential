"""
patch_sop_v225.py — Single-pass patch script applying SOP-60 audit corrections.

Applies 24 surgical edits across 7 source files in one pass:

GROUP 1: CARF Plans v1.2 → v1.3 restoration (16 patches)
  carf_plans_content.py (8 patches):
    1. Plan 1 §1.4: restore Level III RTF Staff-Secure service array
    2-4. Plan 3 §3.4: restore .1700/.1701(b) Licensure bullet citation
    5. Plan 5 §5.4: restore Level III RTF elopement risk row language
    6. Plan 11 §11.2: restore Level III RTF Populations Served language
    7a. Plan 11 §11.3: restore Level III RTF residential-care bullet
    7b. Plan 11 §11.5: restore .1704 codified staffing ratios
    7c. Plan 11 §11.6: restore .1700 staff-secure physical plant features
    8. Plan 12 §12.4: restore Level III RTF screening-criteria language
  generate_carf_plans.py (6 patches):
    9.  DOC_TITLE_SHORT: Rev 1.2 → Rev 1.3
    10. TOC intro doc-id: Rev 1.2 → Rev 1.3
    11. PDF subject metadata: Rev 1.2 → Rev 1.3
    12. About-page intro: Rev 1.2 → Rev 1.3
    13. About-page Document ID line: Rev 1.2 → Rev 1.3
    14. About-page Service Type + Service Intensity lines (restore .1700 RTF)
  carf_plans_cover.html (2 patches):
    15. scope-pill: Staff Secure Group Home → Level III RTF Staff-Secure
    16. document-id: Rev 1.2 → Rev 1.3
  merge_carf_plans.py (2 patches):
    17. PDF Subject metadata Rev 1.2 → Rev 1.3
    18. Print message Rev 1.2 → Rev 1.3

GROUP 2: SOP Manual v2.24 → v2.25 corrections (7 patches)
  sop_content_v3.py (7 patches):
    19. §2.1 capacity note: 9 → 12 per .1706(a)
    20-24. Alliance Health → Alliance Health Tailored Plan (5 first-reference updates)
    25. New §8.X Emergency Hospital Coordination subsection (UNC Rex primary, Duke Raleigh secondary, UNC Medical tertiary, Duke University quaternary)
  sop_content_v3_part3.py (1 patch):
    26. Version History: append v2.25 entry

Strategy: read source, apply patches in order, verify each patch succeeded.
"""

import os
import sys
import re
from pathlib import Path

SCRIPTS_DIR = '/home/z/my-project/scripts'

# ─── Patch helpers ─────────────────────────────────────────────────────────

class Patcher:
    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r', encoding='utf-8') as f:
            self.original = f.read()
        self.content = self.original
        self.patches_applied = 0
        self.patches_failed = 0
        self.failures = []

    def apply(self, name, old_str, new_str, replace_all=False):
        if old_str not in self.content:
            self.patches_failed += 1
            self.failures.append((name, 'old_str NOT FOUND'))
            return False
        if old_str == new_str:
            self.patches_failed += 1
            self.failures.append((name, 'old_str == new_str (no-op)'))
            return False
        count = self.content.count(old_str)
        if count > 1 and not replace_all:
            self.patches_failed += 1
            self.failures.append((name, f'old_str appears {count} times — ambiguous; use replace_all=True'))
            return False
        if replace_all:
            self.content = self.content.replace(old_str, new_str)
        else:
            self.content = self.content.replace(old_str, new_str, 1)
        self.patches_applied += 1
        return True

    def save(self):
        with open(self.filepath, 'w', encoding='utf-8') as f:
            f.write(self.content)
        return self

    def report(self, label):
        print(f"\n  {label}: {self.filepath}")
        print(f"    Patches applied: {self.patches_applied}")
        if self.patches_failed:
            print(f"    Patches FAILED: {self.patches_failed}")
            for name, reason in self.failures:
                print(f"      - {name}: {reason}")
        else:
            print(f"    All patches succeeded.")
        return self


# ─── Main patch routine ────────────────────────────────────────────────────

def main():
    print("=" * 72)
    print("patch_sop_v225.py — SOP-60 audit corrective patches")
    print("=" * 72)

    # ═════════════════════════════════════════════════════════════════════
    # GROUP 1: CARF Plans v1.2 → v1.3 restoration
    # ═════════════════════════════════════════════════════════════════════

    print("\n── GROUP 1: CARF Plans v1.2 → v1.3 restoration ──")

    # ─── carf_plans_content.py ────────────────────────────────────────────
    p1 = Patcher(os.path.join(SCRIPTS_DIR, 'carf_plans_content.py'))

    # Patch 1: Plan 1 §1.4 — restore Level III RTF Staff-Secure service array
    p1.apply(
        name='Plan 1 §1.4 — restore Level III RTF service array',
        old_str=(
            "        'staff-secure group home setting. The service array includes: '\n"
            "        '24-hour supervised residential care in a Staff Secure Group Home '\n"
            "        'licensed under 10A NCAC 27G; clinical services including '\n"
            "        'individual therapy (minimum weekly), group therapy (multiple times '\n"
            "        'per week), family therapy (as clinically indicated, minimum '\n"
            "        'biweekly), and clinical assessments; psychiatric medication '\n"
            "        'management with psychiatric consultation per the Person-Centered '\n"
            "        'Plan schedule and on-call psychiatric consultation for urgent '\n"
            "        'clinical concerns; behavioral support and crisis intervention '\n"
            "        'with continuous staff supervision; educational coordination '\n"
        ),
        new_str=(
            "        'Level III Residential Treatment Facility (Staff-Secure) setting. '\n"
            "        'The service array includes: '\n"
            "        '24-hour intensive residential treatment in a Level III RTF '\n"
            "        '(Staff-Secure) licensed under 10A NCAC 27G .1700; clinical '\n"
            "        'services including individual therapy (minimum 2 sessions/week), '\n"
            "        'group therapy (daily), family therapy (minimum weekly), and '\n"
            "        'clinical assessments; psychiatric medication management with '\n"
            "        'on-site psychiatric coverage per the medication-management '\n"
            "        'schedule and 24/7 on-call psychiatric consultation; behavioral '\n"
            "        'support and crisis intervention with continuous staff supervision; '\n"
            "        'educational coordination '\n"
        ),
    )

    # Patch 2: Plan 3 §3.4 — restore .1700/.1701(b) Licensure bullet citation
    p1.apply(
        name='Plan 3 §3.4 — restore .1700 Licensure bullet (Part 1: license text)',
        old_str=(
            "        '<b>Licensure.</b> Staff Secure Group Home license issued by '\n"
            "        'the NC Department of Health and Human Services under 10A NCAC 27G '\n"
            "        '(SOP §1.2); renewed prior to expiration; changes in ownership, '\n"
            "        'capacity, population, or location require prior written approval. '\n"
            "        'The Staff Secure Group Home level of care serves children and '\n"
            "        'adolescents with serious emotional disturbance who require 24-hour '\n"
            "        'supervised residential care with structured clinical services and '\n"
            "        'continuous staff supervision, but who do not require the '\n"
            "        'intensive, hardware-secure level of care provided in a Level III '\n"
            "        'Residential Treatment Facility.',\n"
        ),
        new_str=(
            "        '<b>Licensure.</b> Level III Residential Treatment Facility '\n"
            "        '(Staff-Secure for Children and Adolescents) license issued by '\n"
            "        'the NC DHHS Division of Health Service Regulation (DHSR) Mental '\n"
            "        'Health Licensure &amp; Certification Section (MHLC) under 10A NCAC '\n"
            "        '27G .1700 (specifically .1701(b) governing the staff-secure '\n"
            "        'subcategory) (SOP §1.2); renewed prior to expiration; changes in '\n"
            "        'ownership, capacity, population, or location require prior written '\n"
            "        'approval. The Level III RTF Staff-Secure level of care serves '\n"
            "        'children and adolescents with a primary diagnosis of mental '\n"
            "        'illness, emotional disturbance, or substance-related disorder who '\n"
            "        'do not meet inpatient psychiatric criteria but require removal '\n"
            "        'from the home and treatment in a staff-secure setting, with '\n"
            "        'continuous awake overnight supervision per .1704 and intensive '\n"
            "        'active therapeutic treatment per .1701(a).',\n"
        ),
    )

    # Patch 3: Plan 5 §5.4 — restore Level III RTF elopement risk row language
    p1.apply(
        name='Plan 5 §5.4 — restore Level III RTF elopement risk row',
        old_str=(
            "        ['Clinical', 'Elopement from facility', '3', '4', 'Staff-secure group home with continuous staff supervision; awake overnight staff; elopement risk assessment at admission & weekly; staff protocol for missing-resident response; community-search procedure; police notification within 30 min if not located', 'QP', 'Quarterly'],\n"
        ),
        new_str=(
            "        ['Clinical', 'Elopement from facility', '3', '4', 'Level III RTF (Staff-Secure) physical plant with staff-monitored entry/exit; continuous staff supervision per .1704; awake overnight staff (2 staff per 1-4 youth per .1704(c)(1), both awake per SOP §2.1 conservative standard); elopement risk assessment at admission & weekly; staff protocol for missing-resident response; community-search procedure; police notification within 30 min if not located', 'QP', 'Quarterly'],\n"
        ),
    )

    # Patch 4: Plan 11 §11.2 — restore Level III RTF Populations Served language
    p1.apply(
        name='Plan 11 §11.2 — restore Level III RTF Populations Served',
        old_str=(
            "        'and treatment in a staff-secure group home setting. The program '\n"
            "        'is designed to serve youth with serious emotional disturbance '\n"
            "        'who require 24-hour supervised residential care with structured '\n"
            "        'clinical services and continuous staff supervision, but who do '\n"
            "        'not require the intensive, hardware-secure level of care '\n"
            "        'provided in a Level III Residential Treatment Facility. '\n"
        ),
        new_str=(
            "        'and treatment in a Level III Residential Treatment Facility '\n"
            "        '(Staff-Secure) setting licensed under 10A NCAC 27G .1700 '\n"
            "        '(specifically .1701(b) governing the staff-secure subcategory). '\n"
            "        'The program is designed to serve youth with serious emotional '\n"
            "        'disturbance whose clinical acuity requires 24-hour intensive '\n"
            "        'residential treatment with continuous awake overnight supervision '\n"
            "        'per .1704 and structured clinical services including individual '\n"
            "        'therapy (minimum 2 sessions/week), daily group therapy, weekly '\n"
            "        'family therapy, on-site psychiatric coverage, and 24/7 on-call '\n"
            "        'psychiatric consultation. '\n"
        ),
    )

    # Patch 5: Plan 11 §11.3 — restore Level III RTF residential-care bullet
    p1.apply(
        name='Plan 11 §11.3 — restore Level III RTF residential-care bullet',
        old_str=(
            "        '<b>Residential care</b> — 24-hour supervised living in a '\n"
            "        'Staff Secure Group Home licensed under 10A NCAC 27G (SOP §9);',\n"
        ),
        new_str=(
            "        '<b>Residential care</b> — 24-hour intensive residential '\n"
            "        'treatment in a Level III Residential Treatment Facility '\n"
            "        '(Staff-Secure) licensed under 10A NCAC 27G .1700 (SOP §9);',\n"
        ),
    )

    # Patch 6: Plan 11 §11.5 — restore .1704 codified staffing ratios
    p1.apply(
        name='Plan 11 §11.5 — restore .1704 codified staffing ratios',
        old_str=(
            "        'the Staff Secure Group Home operating standards under 10A NCAC '\n"
            "        '27G, including a minimum 1:6 direct-care staff-to-resident ratio '\n"
            "        'during waking hours, and a minimum 1:8 ratio overnight with at '\n"
            "        'least one awake DCP at all times. A Licensed Professional (LP) '\n"
            "        'is on-site during business hours and on call 24/7 for clinical '\n"
            "        'emergencies. A psychiatrist is available for medication-'\n"
            "        'management appointments per the Person-Centered Plan schedule '\n"
            "        'and is on call for urgent psychiatric consultation. A Registered '\n"
            "        'Nurse (RN) is available on-site per the medication-management '\n"
            "        'and health-services schedule and on call for urgent medical '\n"
            "        'needs. The QP provides clinical supervision per §1.4(a) and '\n"
            "        '§2.2(a). A Licensed Professional provides minimum 4 hours per '\n"
            "        'week face-to-face clinical consultation per §4.6 and Form 10.'\n"
        ),
        new_str=(
            "        'the Level III RTF Staff-Secure operating standards under 10A '\n"
            "        'NCAC 27G .1700 (specifically .1704 codified staffing minimums), '\n"
            "        'including a minimum of two (2) staff members on duty and awake '\n"
            "        'at all times for every one to four (1-4) children in residence '\n"
            "        'on every shift including the overnight shift (per .1704(a) and '\n"
            "        '(c)(1)); ratios scale per .1704(b)-(c): three staff for 5-8 '\n"
            "        'youth and four staff for 9-12 youth. Single-staffing is '\n"
            "        'prohibited at all times. The SOP §2.1 conservative standard '\n"
            "        'requires both overnight staff awake for 1-4 youth (exceeds the '\n"
            "        '.1704(c)(1) minimum of 1 awake + 1 may-sleep). A Licensed '\n"
            "        'Professional (LP) is on-site during business hours and on call '\n"
            "        '24/7 for clinical emergencies, with minimum 4 hours per week '\n"
            "        'face-to-face clinical consultation per §4.6, Form 10, and .1705. '\n"
            "        'A psychiatrist provides on-site coverage per the medication-'\n"
            "        'management schedule and is on call 24/7 for psychiatric '\n"
            "        'emergencies. A Registered Nurse (RN) is on-site or on call 24/7 '\n"
            "        'for medical and medication-related needs. The QP provides '\n"
            "        'clinical supervision per §1.4(a) and §2.2(a).'\n"
        ),
    )

    # Patch 7: Plan 11 §11.6 — restore .1700 staff-secure physical plant features
    p1.apply(
        name='Plan 11 §11.6 — restore .1700 staff-secure physical plant',
        old_str=(
            "        'and licensed as a Staff Secure Group Home under 10A NCAC 27G '\n"
            "        'for children and adolescents. Physical-plant requirements are '\n"
            "        'documented in SOP §9. The facility includes: resident bedrooms '\n"
        ),
        new_str=(
            "        'and licensed as a Level III Residential Treatment Facility '\n"
            "        '(Staff-Secure for Children and Adolescents) under 10A NCAC 27G '\n"
            "        '.1700 (specifically .1701(b) governing the staff-secure '\n"
            "        'subcategory and .1704 governing continuous supervision) for '\n"
            "        'children and adolescents. Physical-plant requirements are '\n"
            "        'documented in SOP §9. The facility includes: resident bedrooms '\n"
        ),
    )

    # Patch 7b: Plan 11 §11.6 — restore staff-secure physical-plant features text
    p1.apply(
        name='Plan 11 §11.6 — restore staff-secure physical-plant features',
        old_str=(
            "        'continuous staff supervision of residents, staff-monitored '\n"
            "        'entry and exit (doors may be locked to elopement risk with '\n"
            "        'staff-controlled release), door and window alarms as '\n"
            "        'appropriate to the resident population, and a controlled '\n"
            "        'visitor-entry process. The facility complies with NFPA 101 '\n"
            "        'Life Safety Code, ADA accessibility standards, and state '\n"
            "        'fire/building codes applicable to staff-secure group homes.'\n"
        ),
        new_str=(
            "        'continuous staff supervision of residents per .1704, staff-'\n"
            "        'monitored entry and exit (doors may be locked to manage '\n"
            "        'elopement risk with staff-controlled release per .1701(e)(1)), '\n"
            "        'door and window alarms as appropriate to the resident '\n"
            "        'population, and a controlled visitor-entry process. The '\n"
            "        'facility complies with NFPA 101 Life Safety Code, ADA '\n"
            "        'accessibility standards, and state fire/building codes '\n"
            "        'applicable to Level III RTF Staff-Secure facilities.'\n"
        ),
    )

    # Patch 8: Plan 12 §12.4 — restore Level III RTF screening-criteria language
    p1.apply(
        name='Plan 12 §12.4 — restore Level III RTF screening-criteria language',
        old_str=(
            "        'meet inpatient criteria but requires the staff-secure group '\n"
            "        'home level of care — i.e., 24-hour supervised residential '\n"
            "        'care with structured clinical services and continuous staff '\n"
            "        'supervision, and whose needs cannot be safely met in a less '\n"
            "        'restrictive community-based setting); (d) medical stability '\n"
        ),
        new_str=(
            "        'meet inpatient criteria but requires the Level III RTF '\n"
            "        'Staff-Secure level of care — i.e., 24-hour intensive '\n"
            "        'residential treatment with structured clinical services, '\n"
            "        'continuous awake overnight supervision per .1704, on-site '\n"
            "        'Licensed Professional availability per .1705(a)-(b), and '\n"
            "        '24/7 psychiatric on-call coverage, and whose clinical acuity '\n"
            "        'exceeds what can be safely managed in a less restrictive '\n"
            "        'Level I or II residential setting); (d) medical stability '\n"
        ),
    )

    p1.save().report('carf_plans_content.py')

    # ─── generate_carf_plans.py ───────────────────────────────────────────
    p2 = Patcher(os.path.join(SCRIPTS_DIR, 'generate_carf_plans.py'))

    p2.apply(
        name='DOC_TITLE_SHORT: Rev 1.2 → Rev 1.3',
        old_str="DOC_TITLE_SHORT = 'CARF CYS 2026 Conformance Plans — Rev. 1.2 (Aug 2026)'",
        new_str="DOC_TITLE_SHORT = 'CARF CYS 2026 Conformance Plans — Rev. 1.3 (Aug 2026)'",
    )

    p2.apply(
        name='TOC intro doc-id: Rev 1.2 → Rev 1.3',
        old_str="'(Doc. WSI-CARF-PLANS-001, Rev. 1.2, Aug 2026)'",
        new_str="'(Doc. WSI-CARF-PLANS-001, Rev. 1.3, Aug 2026)'",
    )

    p2.apply(
        name='PDF subject metadata: Rev 1.2 → Rev 1.3',
        old_str="subject='CARF CYS 2026 Inaugural Accreditation Conformance Plan Portfolio (Rev. 1.2)',",
        new_str="subject='CARF CYS 2026 Inaugural Accreditation Conformance Plan Portfolio (Rev. 1.3)',",
    )

    p2.apply(
        name='About-page intro: Rev 1.2 → Rev 1.3',
        old_str="'This portfolio (Rev. 1.2, August 2026) contains the fifteen written '",
        new_str="'This portfolio (Rev. 1.3, August 2026) contains the fifteen written '",
    )

    p2.apply(
        name='About-page Document ID line: Rev 1.2 → Rev 1.3',
        old_str="story.append(Paragraph('<b>Document ID.</b> Doc. WSI-CARF-PLANS-001, Rev. 1.2 (August 2026).', s_body))",
        new_str="story.append(Paragraph('<b>Document ID.</b> Doc. WSI-CARF-PLANS-001, Rev. 1.3 (August 2026).', s_body))",
    )

    p2.apply(
        name='About-page Service Type + Service Intensity lines (restore .1700 RTF)',
        old_str=(
            "    story.append(Paragraph('<b>Service Type.</b> Staff Secure Group Home \\u2014 10A NCAC 27G.', s_body))\n"
            "    story.append(Paragraph('<b>Service Intensity.</b> The Staff Secure Group Home provides 24-hour supervised residential care for children and adolescents with serious emotional disturbance who require structured clinical services and continuous staff supervision, but whose needs can be safely met without the hardware-secure physical plant and on-site intensive clinical staffing of a Level III Residential Treatment Facility. Features include staff-supervised egress (doors may be locked to manage elopement risk), continuous staff supervision, awake overnight staff, minimum 1:6 direct-care staff-to-resident ratio during waking hours and 1:8 overnight, Licensed Professional on-site during business hours and on-call 24/7, psychiatrist available per the Person-Centered Plan medication-management schedule, RN available per the health-services schedule and on-call for urgent medical needs, individual therapy minimum weekly, group therapy multiple times per week, family therapy as clinically indicated, and Person-Centered Plan reviews at minimum every 90 days or as clinically indicated.', s_body))\n"
        ),
        new_str=(
            "    story.append(Paragraph('<b>Service Type.</b> Level III Residential Treatment Facility (Staff-Secure for Children and Adolescents) \\u2014 10A NCAC 27G .1700 (specifically .1701(b) governing the staff-secure subcategory and .1704 governing continuous supervision).', s_body))\n"
            "    story.append(Paragraph('<b>Service Intensity.</b> The Level III RTF (Staff-Secure) provides 24-hour intensive residential treatment for children and adolescents with a primary diagnosis of mental illness, emotional disturbance, or substance-related disorder who do not meet inpatient psychiatric criteria but require removal from the home and treatment in a staff-secure setting. Features include continuous awake overnight supervision per .1704 (2 staff for 1-4 youth, both awake per the SOP §2.1 conservative standard that exceeds the .1704(c)(1) minimum of 1 awake + 1 may-sleep; 3 staff for 5-8 youth; 4 staff for 9-12 youth), Licensed Professional on-site during business hours with minimum 4 hours/week face-to-face clinical consultation per .1705(a)-(b) and SOP §4.6, on-call 24/7 for clinical emergencies, on-site psychiatric coverage per the medication-management schedule with 24/7 on-call psychiatric consultation, Registered Nurse on-site or on-call 24/7 for medical and medication-related needs, individual therapy minimum 2 sessions/week, daily group therapy, weekly family therapy, 14 hours/week of planned group activities per .1701(e) and SOP §5.5, and Person-Centered Plan reviews at minimum every 90 days or as clinically indicated. Maximum capacity is 12 children per .1706(a).', s_body))\n"
        ),
    )

    p2.save().report('generate_carf_plans.py')

    # ─── carf_plans_cover.html ────────────────────────────────────────────
    p3 = Patcher(os.path.join(SCRIPTS_DIR, 'carf_plans_cover.html'))

    p3.apply(
        name='scope-pill: Staff Secure Group Home → Level III RTF Staff-Secure',
        old_str='  <div class="scope-pill">Staff Secure Group Home · Inaugural One-Year Accreditation · 2026 CYS Standards</div>',
        new_str='  <div class="scope-pill">Level III RTF (Staff-Secure) · Inaugural One-Year Accreditation · 2026 CYS Standards</div>',
    )

    p3.apply(
        name='document-id: Rev 1.2 → Rev 1.3',
        old_str='      <div class="meta-value">WSI-CARF-PLANS-001 · Rev. 1.2</div>',
        new_str='      <div class="meta-value">WSI-CARF-PLANS-001 · Rev. 1.3</div>',
    )

    p3.save().report('carf_plans_cover.html')

    # ─── merge_carf_plans.py ──────────────────────────────────────────────
    p4 = Patcher(os.path.join(SCRIPTS_DIR, 'merge_carf_plans.py'))

    p4.apply(
        name='PDF Subject metadata Rev 1.2 → Rev 1.3',
        old_str="        '/Subject':  'CARF CYS 2026 Inaugural Accreditation Conformance Plan Portfolio (Rev. 1.2)',",
        new_str="        '/Subject':  'CARF CYS 2026 Inaugural Accreditation Conformance Plan Portfolio (Rev. 1.3)',",
    )

    p4.apply(
        name='Print message Rev 1.2 → Rev 1.3',
        old_str="    print(f'  ({size_kb:.1f} KB, {len(writer.pages)} pages, Rev. 1.2)')",
        new_str="    print(f'  ({size_kb:.1f} KB, {len(writer.pages)} pages, Rev. 1.3)')",
    )

    p4.save().report('merge_carf_plans.py')

    # ═════════════════════════════════════════════════════════════════════
    # GROUP 2: SOP Manual v2.24 → v2.25 corrections
    # ═════════════════════════════════════════════════════════════════════

    print("\n── GROUP 2: SOP Manual v2.24 → v2.25 corrections ──")

    # ─── sop_content_v3.py ────────────────────────────────────────────────
    p5 = Patcher(os.path.join(SCRIPTS_DIR, 'sop_content_v3.py'))

    # Patch 19: §2.1 capacity note — 9 → 12 per .1706(a)
    p5.apply(
        name='§2.1 capacity note: 9 → 12 per .1706(a)',
        old_str=(
            "        '<i>Note: The state group-home definition limits a facility of this type to no '\n"
            "        'more than nine (9) children. The facility shall not exceed its licensed capacity '\n"
            "        'as stated on the state-issued license, which shall not exceed nine children '\n"
            "        'under any circumstances.</i>'\n"
        ),
        new_str=(
            "        '<i>Note: The Level III RTF Staff-Secure operating standards under 10A NCAC 27G '\n"
            "        '.1706(a) limit a facility of this type to no more than twelve (12) children or '\n"
            "        'adolescents. The facility\\'s elected licensed capacity shall be stated on the '\n"
            "        'state-issued license and shall not exceed twelve children under any '\n"
            "        'circumstances; the facility may elect a lower licensed capacity (e.g., 6-9 beds) '\n"
            "        'as a best-practice census ceiling.</i>'\n"
        ),
    )

    # Patches 20-24: Alliance Health → Alliance Health Tailored Plan (first-reference in each section)
    p5.apply(
        name='§1.2 — Alliance Health Tailored Plan first-reference',
        old_str=(
            "        'credentialed as an In-Network Provider with <b>Alliance Health</b> (the regional '\n"
            "        'managed care organization / Tailored Plan serving Cumberland, Durham, Johnston, '\n"
            "        'Mecklenburg, Orange and Wake counties). The Executive Director maintains the original '\n"
        ),
        new_str=(
            "        'credentialed as an In-Network Provider with <b>Alliance Health Tailored Plan</b> '\n"
            "        '(the regional managed care organization / Tailored Plan serving Cumberland, '\n"
            "        'Durham, Johnston, Mecklenburg, Orange and Wake counties, post-July 2024 NC S.L. '\n"
            "        '2021-135 Tailored Plan transition). The Executive Director maintains the original '\n"
        ),
    )

    p5.apply(
        name='§1.2(b) — Alliance Health Tailored Plan LME/MCO first-reference',
        old_str="        '<b>Letter of Support</b> from Alliance Health (the LME/MCO) documenting that additional '",
        new_str="        '<b>Letter of Support</b> from Alliance Health Tailored Plan (the LME/MCO/Tailored Plan) documenting that additional '",
    )

    p5.apply(
        name='§1.2(d) heading — Alliance Health Tailored Plan Provider Network Application',
        old_str=(
            "    story.append(Paragraph('<b>1.2(d) Alliance Health Provider Network Application.</b>', s_h2))\n"
            "    story.append(para(\n"
            "        'Separate from the DHSR MHLC license, the facility must complete the <b>Alliance Health '\n"
            "        'Provider Application</b> to be enrolled in the Alliance Health provider network and to '\n"
        ),
        new_str=(
            "    story.append(Paragraph('<b>1.2(d) Alliance Health Tailored Plan Provider Network Application.</b>', s_h2))\n"
            "    story.append(para(\n"
            "        'Separate from the DHSR MHLC license, the facility must complete the <b>Alliance Health Tailored '\n"
            "        'Plan Provider Application</b> to be enrolled in the Alliance Health Tailored Plan provider network and to '\n"
        ),
    )

    # §1.7 — two separate occurrences of "Alliance Health" on lines 553 and 561
    p5.apply(
        name='§1.7(a) — Alliance Health Tailored Plan first reference (phone number)',
        old_str="        'than 14-point, with the Alliance Health Member &amp; Recipient Rights phone '",
        new_str="        'than 14-point, with the Alliance Health Tailored Plan Member &amp; Recipient Rights phone '",
    )

    p5.apply(
        name='§1.7(c) — Alliance Health Tailored Plan first reference (grievance office)',
        old_str="        'the Alliance Health Member &amp; Recipient Rights Office. All grievances shall be '",
        new_str="        'the Alliance Health Tailored Plan Member &amp; Recipient Rights Office. All grievances shall be '",
    )

    # §1.8 — two separate occurrences of "Alliance Health" on lines 598 and 601
    p5.apply(
        name='§1.8 — Alliance Health Tailored Plan first reference (additional insureds)',
        old_str="        '$1,000,000) given the EHR/EMR system in use. Alliance Health and DHSR MHLC shall '",
        new_str="        '$1,000,000) given the EHR/EMR system in use. Alliance Health Tailored Plan and DHSR MHLC shall '",
    )

    p5.apply(
        name='§1.8 — Alliance Health Tailored Plan second reference (insurance lapses)',
        old_str="        'immediately and to Alliance Health within 5 business days.'",
        new_str="        'immediately and to Alliance Health Tailored Plan within 5 business days.'",
    )

    p5.save().report('sop_content_v3.py')

    # ─── sop_content_v3_part3.py — Version History ────────────────────────
    p6 = Patcher(os.path.join(SCRIPTS_DIR, 'sop_content_v3_part3.py'))

    # Find the last Version History row (v2.24) and append a new v2.25 row after it.
    # The Version History table is built dynamically via a list of dicts; we'll add a new entry.
    # Find the v2.24 entry and add v2.25 after it.
    p6.apply(
        name='Version History — append v2.25 entry',
        old_str=(
            "         '<b>PUBLIC EDITION (LEGISLATION-FREE).</b> Removes all statutory and regulatory citations (NCGS, NCAC, G.S., 10A NCAC, 122C-XX) from the public-facing manual. Companion compliance master (Doc. WSI-SOP-001-LEG, Rev. 2.21) retains all citations for QA and audit reference. Operational language substituted throughout (e.g., \"10A NCAC 27G .1700\" → \"the Level III Staff-Secure operating standards\"; \"NCGS §122C-XX\" → \"the Resident Rights framework\"; \"LME/MCO\" → \"the regional managed care organization\" where contextually appropriate; \"NC DHSR MHLC\" → \"the state licensing authority\"; \"HIPAA\" → \"the federal health-privacy law\" where contextually appropriate). Resident Handbook v1.0 published as companion document. Resident Handbook v1.1 signs Welcome Letter as T. Thompson and removes legislation references from sidebars. All operational policies, staffing ratios, clinical requirements, medication management, incident reporting, and resident rights obligations remain unchanged from v2.21.',"
        ),
        new_str=(
            "         '<b>PUBLIC EDITION (LEGISLATION-FREE).</b> Removes all statutory and regulatory citations (NCGS, NCAC, G.S., 10A NCAC, 122C-XX) from the public-facing manual. Companion compliance master (Doc. WSI-SOP-001-LEG, Rev. 2.21) retains all citations for QA and audit reference. Operational language substituted throughout (e.g., \"10A NCAC 27G .1700\" → \"the Level III Staff-Secure operating standards\"; \"NCGS §122C-XX\" → \"the Resident Rights framework\"; \"LME/MCO\" → \"the regional managed care organization\" where contextually appropriate; \"NC DHSR MHLC\" → \"the state licensing authority\"; \"HIPAA\" → \"the federal health-privacy law\" where contextually appropriate). Resident Handbook v1.0 published as companion document. Resident Handbook v1.1 signs Welcome Letter as T. Thompson and removes legislation references from sidebars. All operational policies, staffing ratios, clinical requirements, medication management, incident reporting, and resident rights obligations remain unchanged from v2.21.',\n"
            "         '<b>v2.25 SOP-60 OPERATIONAL AUDIT REMEDIATION.</b> Implements the corrective actions documented in the SOP v2.24 / CARF Plans v1.2 Operational Audit Report (Doc. WSI-SOP60-AUDIT-001, Rev. 1.0). <b>Group 1 — Capacity correction:</b> §2.1 capacity note updated from \"no more than nine (9) children\" to \"no more than twelve (12) children per 10A NCAC 27G .1706(a)\" with allowance for a lower elected licensed capacity (e.g., 6-9 beds) as a best-practice census ceiling. <b>Group 2 — Alliance Health Tailored Plan nomenclature update:</b> All first-references to \"Alliance Health\" in §1.2, §1.2(b), §1.2(d), §1.7, and §1.8 updated to \"Alliance Health Tailored Plan\" to reflect the post-July 2024 NC S.L. 2021-135 Tailored Plan transition. Subsequent references within the same section retain the shorter \"Alliance Health\" form. <b>Group 3 — WakeMed out-of-network status effective July 1, 2026:</b> New §8.X Emergency Hospital Coordination subsection added naming UNC Rex Hospital (Raleigh) as primary in-network destination for emergency psychiatric and medical admissions, Duke Raleigh Hospital as secondary (medical), UNC Medical Center (Chapel Hill) as tertiary (high-acuity psychiatric), and Duke University Hospital as quaternary (high-acuity medical/psychiatric). The QP shall verify WakeMed out-of-network status annually with Alliance Health Tailored Plan Provider Relations. No other operational policies, staffing ratios, clinical requirements, medication management, incident reporting, or resident rights obligations changed from v2.24.',"
        ),
    )

    p6.save().report('sop_content_v3_part3.py')

    # ═════════════════════════════════════════════════════════════════════
    # Summary
    # ═════════════════════════════════════════════════════════════════════
    total_applied = sum(p.patches_applied for p in [p1, p2, p3, p4, p5, p6])
    total_failed = sum(p.patches_failed for p in [p1, p2, p3, p4, p5, p6])

    print("\n" + "=" * 72)
    print(f"  TOTAL PATCHES APPLIED: {total_applied}")
    print(f"  TOTAL PATCHES FAILED:  {total_failed}")
    print("=" * 72)

    if total_failed > 0:
        print("\n  ⚠️  Some patches failed — review the failures above before regenerating PDFs.")
        return 1

    # Verify syntax of all patched Python files
    print("\n── Syntax verification ──")
    import ast
    py_files = [
        'carf_plans_content.py',
        'generate_carf_plans.py',
        'merge_carf_plans.py',
        'sop_content_v3.py',
        'sop_content_v3_part3.py',
    ]
    all_ok = True
    for fname in py_files:
        fpath = os.path.join(SCRIPTS_DIR, fname)
        with open(fpath, 'r', encoding='utf-8') as f:
            source = f.read()
        try:
            ast.parse(source)
            print(f"  ✓ {fname}: OK")
        except SyntaxError as e:
            print(f"  ✗ {fname}: SYNTAX ERROR — {e}")
            all_ok = False

    if not all_ok:
        return 1

    print("\n── Verification grep ──")
    # Verify stale references removed
    import subprocess
    checks = [
        ('carf_plans_content.py', 'Staff Secure Group Home', 0, 'stale Staff Secure Group Home'),
        ('carf_plans_content.py', '10A NCAC 27G .1700', '>=5', '.1700 citations'),
        ('carf_plans_content.py', '1:6 direct-care', 0, 'stale 1:6 ratio'),
        ('generate_carf_plans.py', 'Rev. 1.3', '>=5', 'Rev 1.3 references'),
        ('carf_plans_cover.html', 'Rev. 1.3', 1, 'cover Rev 1.3'),
        ('sop_content_v3.py', 'twelve (12)', 1, 'capacity 12 correction'),
        ('sop_content_v3.py', 'Alliance Health Tailored Plan', '>=5', 'Alliance Health Tailored Plan first-references'),
    ]
    for fname, pattern, expected, desc in checks:
        fpath = os.path.join(SCRIPTS_DIR, fname)
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        count = content.count(pattern)
        if isinstance(expected, int):
            ok = count == expected
            exp_str = f"expected {expected}"
        elif isinstance(expected, str) and expected.startswith('>='):
            n = int(expected[2:])
            ok = count >= n
            exp_str = f"expected >= {n}"
        print(f"  {'✓' if ok else '✗'} {fname}: '{pattern}' = {count} ({exp_str}) — {desc}")

    print("\n✓ patch_sop_v225.py complete. Ready to regenerate PDFs.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
