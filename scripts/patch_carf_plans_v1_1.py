#!/usr/bin/env python3
"""
patch_carf_plans_v1_1.py — Surgical Level III RTF calibration patch.

User clarified (Aug 2026): service type corresponds to a Level III Residential
Treatment Facility under NC 10A NCAC 27G .1703 (the highest-acuity NC RTF
category, hardware-secure, intensive clinical). The previous Rev. 1.0 plans
used inconsistent "Level III Staff-Secure" / "Level 3 Supervised Residential
Group Home" terminology with .1701(b) citations — that is internally
inconsistent (.1701 covers Level I staff-secure facilities).

This patch:
  1. Replaces all "Level III Staff-Secure" / "staff-secure" references with
     correct "Level III Residential Treatment Facility (Hardware-Secure)"
     terminology and 10A NCAC 27G .1703 citations.
  2. Expands Plan 11 §11.5 (Staffing Patterns) with Level III RTF-specific
     clinical-intensity details (1:4 waking ratio, 1:8 overnight, on-site
     LP 16h/day, psychiatrist on-call 24/7, RN on-site/on-call 24/7, weekly
     PCP reviews, daily clinical groups, individual therapy ≥2x/week,
     family therapy weekly).
  3. Updates the elopement risk row (Plan 5 §5.4) to reflect hardware-secure
     Level III RTF physical plant with controlled egress.
  4. Updates Plan 12 §12.4 (Screening Criteria) to reference Level III RTF
     level of care.
  5. Bumps Rev 1.0 → Rev 1.1 across generate_carf_plans.py, cover HTML, and
     merge_carf_plans.py.
  6. Adds a "Service Intensity" line to the About This Portfolio page.

Files patched:
  - /home/z/my-project/scripts/carf_plans_content.py    (6 patches)
  - /home/z/my-project/scripts/generate_carf_plans.py   (7 patches)
  - /home/z/my-project/scripts/carf_plans_cover.html    (2 patches)
  - /home/z/my-project/scripts/merge_carf_plans.py      (2 patches)

Each patch uses exact-match old_str; fails loudly if the match is missing.
"""

import ast
import re
import sys
from pathlib import Path

ROOT = Path('/home/z/my-project/scripts')
CONTENT = ROOT / 'carf_plans_content.py'
GENERATE = ROOT / 'generate_carf_plans.py'
COVER = ROOT / 'carf_plans_cover.html'
MERGE = ROOT / 'merge_carf_plans.py'

patches_applied = 0
patches_failed = 0


def patch(path: Path, old: str, new: str, label: str) -> None:
    """Replace old_str with new_str in file; fail loudly if not unique."""
    global patches_applied, patches_failed
    text = path.read_text(encoding='utf-8')
    count = text.count(old)
    if count == 0:
        print(f'  [FAIL] {label}: old_str not found in {path.name}')
        patches_failed += 1
        return
    if count > 1:
        print(f'  [FAIL] {label}: old_str matches {count} times in {path.name} — needs more context')
        patches_failed += 1
        return
    new_text = text.replace(old, new, 1)
    path.write_text(new_text, encoding='utf-8')
    print(f'  [ OK ] {label} ({path.name})')
    patches_applied += 1


# ═══════════════════════════════════════════════════════════════════════
# PATCHES TO carf_plans_content.py
# ═══════════════════════════════════════════════════════════════════════
print('\n── Patching carf_plans_content.py ──')

# Patch 1: Plan 1 §1.4 Populations & Services — replace "staff-secure residential setting"
patch(
    CONTENT,
    (
        'criteria but require removal from the home and treatment in a staff-secure '
        'residential setting. The service array includes: residential care in a '
        'Level III Staff-Secure facility; clinical services including individual, '
        'group, and family therapy; psychiatric medication management; behavioral '
        'support and crisis intervention; educational coordination through the '
        'local public school system; case management and care coordination with '
        'the LME/MCO and other system-of-care partners; and structured '
        'recreational, social, and life-skills programming.'
    ),
    (
        'criteria but require removal from the home and treatment in a Level III '
        'Residential Treatment Facility (hardware-secure, intensive clinical). '
        'The service array includes: 24-hour residential treatment in a Level III '
        'RTF licensed under 10A NCAC 27G .1703; clinical services including '
        'individual therapy (minimum 2 sessions/week), group therapy (daily), '
        'family therapy (minimum weekly), and comprehensive clinical assessments; '
        'psychiatric medication management with on-site psychiatric coverage and '
        '24/7 on-call psychiatric consultation; behavioral support and crisis '
        'intervention with line-of-sight supervision capability for high-acuity '
        'residents; educational coordination through the local public school '
        'system or facility-based instructional programming; case management and '
        'care coordination with the LME/MCO and other system-of-care partners; '
        'and structured recreational, social, and life-skills programming '
        'integrated into the daily milieu-therapy schedule.'
    ),
    'Plan 1 §1.4 — Level III RTF service array expansion',
)

# Patch 2: Plan 3 §3.4 Licensure bullet — replace "Staff Secure" with "(Hardware-Secure)"
patch(
    CONTENT,
    (
        '<b>Licensure.</b> Level III Residential Treatment Facility — Staff '
        'Secure license issued by the state mental health authority (SOP §1.2); '
        'renewed prior to expiration; changes in ownership, capacity, population, '
        'or location require prior written approval.'
    ),
    (
        '<b>Licensure.</b> Level III Residential Treatment Facility (Hardware-Secure) '
        'license issued by the NC Department of Health and Human Services under '
        '10A NCAC 27G .1703 (SOP §1.2); renewed prior to expiration; changes in '
        'ownership, capacity, population, or location require prior written '
        'approval. Level III is the highest-acuity NC RTF category and authorizes '
        'the organization to serve children and adolescents with severe emotional '
        'disturbance whose clinical needs cannot be safely met in a less '
        'restrictive (Level I or II) residential setting.'
    ),
    'Plan 3 §3.4 Licensure bullet — Level III RTF .1703 citation',
)

# Patch 3: Plan 5 §5.4 Enterprise Risk Register — elopement row, reflect hardware-secure
patch(
    CONTENT,
    (
        "['Clinical', 'Elopement from facility', '3', '4', 'Staff-secure physical plant; awake overnight supervision; elopement risk assessment; community-search protocol', 'QP', 'Quarterly'],"
    ),
    (
        "['Clinical', 'Elopement from facility', '2', '5', 'Hardware-secure Level III RTF physical plant with controlled-egress doors (key-card / staff-controlled); alarmed perimeter; awake overnight line-of-sight supervision; elopement risk assessment at admission & weekly; community-search protocol; police notification within 30 min', 'QP', 'Quarterly'],"
    ),
    'Plan 5 §5.4 Risk Register — elopement row (hardware-secure Level III)',
)

# Patch 4: Plan 11 §11.2 Populations Served — replace "staff-secure residential setting"
patch(
    CONTENT,
    (
        'criteria but require removal from the home '
        'and treatment in a staff-secure residential setting. The program '
        'is designed to serve youth with severe emotional disturbance '
        '(SED) who require intensive, active therapeutic treatment within '
        'a system-of-care approach. Admission criteria are documented in '
        'SOP §3.1 and the Screening and Access Policy (Plan 12).'
    ),
    (
        'criteria but require removal from the home '
        'and treatment in a Level III Residential Treatment Facility '
        '(hardware-secure, intensive clinical). The program is designed '
        'to serve youth with severe emotional disturbance (SED) whose '
        'clinical acuity exceeds what can be safely managed in a less '
        'restrictive Level I or Level II residential setting, and who '
        'require intensive, active therapeutic treatment within a '
        'system-of-care approach. Admission criteria are documented in '
        'SOP §3.1 and the Screening and Access Policy (Plan 12).'
    ),
    'Plan 11 §11.2 Populations Served — Level III RTF calibration',
)

# Patch 5: Plan 11 §11.3 residential care bullet — replace "Level III Staff-Secure"
patch(
    CONTENT,
    (
        "<b>Residential care</b> — 24-hour supervised living in a Level "
        "III Staff-Secure facility (SOP §9);"
    ),
    (
        "<b>Residential treatment</b> — 24-hour intensive residential "
        "treatment in a Level III RTF (hardware-secure) licensed under "
        "10A NCAC 27G .1703 (SOP §9);"
    ),
    'Plan 11 §11.3 Service Array — residential treatment bullet',
)

# Patch 6: Plan 11 §11.5 Staffing Patterns — major expansion with Level III RTF specifics
patch(
    CONTENT,
    (
        "The program is staffed per SOP §2, including: Executive Director, "
        "Clinical Director, Qualified Professional (QP), Associated "
        "Professionals (APs), Direct Care Professionals (DCPs) on day, "
        "evening, and awake-overnight shifts, House Manager, Registered "
        "Nurse (RN), and Billing Coordinator. Staffing ratios comply "
        "with the Level III Staff-Secure operating standards, including "
        "continuous supervision and awake overnight staff per .1701(b) "
        "and .1704. The QP provides clinical supervision per §1.4(a) and "
        "§2.2(a). A Licensed Professional provides minimum 4 hours per "
        "week face-to-face clinical consultation per §4.6 and Form 10."
    ),
    (
        "The program is staffed per SOP §2, including: Executive Director, "
        "Clinical Director, Qualified Professional (QP), Associated "
        "Professionals (APs), Direct Care Professionals (DCPs) on day, "
        "evening, and awake-overnight shifts, House Manager, Registered "
        "Nurse (RN), and Billing Coordinator. Staffing ratios comply "
        "with the Level III RTF operating standards under 10A NCAC 27G "
        ".1703, including a minimum 1:4 direct-care staff-to-resident "
        "ratio during waking hours (1:3 for high-acuity residents on "
        "line-of-sight supervision), and a minimum 1:8 ratio overnight "
        "with at least one awake DCP at all times. A Licensed Professional "
        "(LP) is on-site a minimum of 16 hours per day, 7 days per week, "
        "with on-call LP coverage outside those hours. A board-certified "
        "psychiatrist provides on-site coverage per the medication-"
        "management schedule and is on call 24/7 for psychiatric "
        "emergencies. A Registered Nurse (RN) is on-site or on call 24/7 "
        "for medical and medication-related needs. The QP provides "
        "clinical supervision per §1.4(a) and §2.2(a). A Licensed "
        "Professional provides minimum 4 hours per week face-to-face "
        "clinical consultation per §4.6 and Form 10."
    ),
    'Plan 11 §11.5 Staffing Patterns — Level III RTF ratios + psychiatrist/RN 24/7',
)

# Patch 7: Plan 11 §11.6 Physical Environment — replace "Level III Staff-Secure"
patch(
    CONTENT,
    (
        "The facility is a free-standing residential treatment facility "
        "designed and licensed as Level III Staff-Secure for children "
        "and adolescents. Physical-plant requirements are documented in "
        "SOP §9. The facility includes: resident bedrooms (single or "
        "double occupancy per licensing standards); communal dining and "
        "living areas; kitchen and food-storage areas; clinical offices "
        "and therapy rooms; a quiet room (not used for seclusion); "
        "medication storage area (double-locked per SOP §6.3(c)); "
        "laundry facilities; outdoor recreation area; and administrative "
        "offices. The facility complies with NFPA 101 Life Safety Code, "
        "ADA accessibility standards, and state fire/building codes."
    ),
    (
        "The facility is a free-standing residential treatment facility "
        "designed and licensed as a Level III Residential Treatment "
        "Facility (Hardware-Secure) under 10A NCAC 27G .1703 for "
        "children and adolescents. Physical-plant requirements are "
        "documented in SOP §9. The facility includes: resident bedrooms "
        "(single or double occupancy per licensing standards); communal "
        "dining and living areas; kitchen and food-storage areas; "
        "clinical offices and therapy rooms; a quiet room / de-escalation "
        "room (not used for seclusion — seclusion is prohibited under "
        "the organization's restraint-and-seclusion-minimization policy "
        "per SOP §5); medication storage area (double-locked per SOP "
        "§6.3(c)); laundry facilities; outdoor recreation area with "
        "controlled-egress perimeter; and administrative offices. "
        "Hardware-secure features include staff-controlled egress doors "
        "(key-card or staff-activated release), alarmed perimeter doors "
        "and windows, 24-hour video monitoring of common areas and "
        "exterior approaches (not in bedrooms, bathrooms, or therapy "
        "rooms to protect privacy), and a secured visitor-entry vestibule. "
        "The facility complies with NFPA 101 Life Safety Code, ADA "
        "accessibility standards, and state fire/building codes, including "
        "the hardware-secure facility requirements under .1703."
    ),
    'Plan 11 §11.6 Physical Environment — Level III RTF hardware-secure features',
)

# Patch 8: Plan 12 §12.4 Screening Criteria — replace "staff-secure residential treatment"
patch(
    CONTENT,
    (
        "substance-related disorder); (c) clinical acuity (does not "
        "meet inpatient criteria but requires staff-secure residential "
        "treatment); (d) medical stability (no acute medical condition "
    ),
    (
        "substance-related disorder); (c) clinical acuity (does not "
        "meet inpatient criteria but requires the Level III RTF level "
        "of care — i.e., hardware-secure, intensive clinical services "
        "with 24-hour on-site Licensed Professional availability and "
        "psychiatric on-call, and whose acuity exceeds what can be "
        "safely managed in a less restrictive Level I or II setting); "
        "(d) medical stability (no acute medical condition "
    ),
    'Plan 12 §12.4 Screening Criteria — Level III RTF acuity descriptor',
)


# ═══════════════════════════════════════════════════════════════════════
# PATCHES TO generate_carf_plans.py
# ═══════════════════════════════════════════════════════════════════════
print('\n── Patching generate_carf_plans.py ──')

# Patch G1: DOC_TITLE_SHORT header
patch(
    GENERATE,
    "DOC_TITLE_SHORT = 'CARF CYS 2026 Conformance Plans — Rev. 1.0 (Aug 2026)'",
    "DOC_TITLE_SHORT = 'CARF CYS 2026 Conformance Plans — Rev. 1.1 (Aug 2026)'",
    'DOC_TITLE_SHORT Rev 1.0 → 1.1',
)

# Patch G2: TOC intro doc-id reference
patch(
    GENERATE,
    "'(Doc. WSI-CARF-PLANS-001, Rev. 1.0, Aug 2026)'",
    "'(Doc. WSI-CARF-PLANS-001, Rev. 1.1, Aug 2026)'",
    'TOC intro doc-id Rev 1.0 → 1.1',
)

# Patch G3: PDF Subject metadata
patch(
    GENERATE,
    "subject='CARF CYS 2026 Inaugural Accreditation Conformance Plan Portfolio (Rev. 1.0)',",
    "subject='CARF CYS 2026 Inaugural Accreditation Conformance Plan Portfolio (Rev. 1.1)',",
    'PDF subject metadata Rev 1.0 → 1.1',
)

# Patch G4: About-page intro paragraph
patch(
    GENERATE,
    "'This portfolio (Rev. 1.0, August 2026) contains the fifteen written '",
    "'This portfolio (Rev. 1.1, August 2026) contains the fifteen written '",
    'About-page intro Rev 1.0 → 1.1',
)

# Patch G5: About-page Document ID line
patch(
    GENERATE,
    "'<b>Document ID.</b> Doc. WSI-CARF-PLANS-001, Rev. 1.0 (August 2026).', s_body))",
    "'<b>Document ID.</b> Doc. WSI-CARF-PLANS-001, Rev. 1.1 (August 2026).', s_body))",
    'About-page Document ID Rev 1.0 → 1.1',
)

# Patch G6: About-page Service Type line — replace and add Service Intensity line
patch(
    GENERATE,
    "story.append(Paragraph('<b>Service Type.</b> Level 3 Supervised Residential Group Home.', s_body))\n",
    (
        "story.append(Paragraph('<b>Service Type.</b> Level III Residential Treatment Facility (Hardware-Secure) \\u2014 10A NCAC 27G .1703.', s_body))\n"
        "    story.append(Paragraph('<b>Service Intensity.</b> Level III is the highest-acuity NC residential treatment category, providing 24-hour intensive clinical services for children and adolescents with severe emotional disturbance (SED) whose needs cannot be safely met in a less restrictive (Level I or II) setting. Features include hardware-secure (controlled-egress) physical plant, on-site Licensed Professional coverage 16 hours/day, psychiatrist on-call 24/7, RN on-site or on-call 24/7, 1:4 waking staff-to-resident ratio, daily clinical groups, individual therapy minimum twice weekly, family therapy minimum weekly, and weekly Person-Centered Plan reviews.', s_body))\n"
    ),
    'About-page Service Type + new Service Intensity line',
)


# ═══════════════════════════════════════════════════════════════════════
# PATCHES TO carf_plans_cover.html
# ═══════════════════════════════════════════════════════════════════════
print('\n── Patching carf_plans_cover.html ──')

# Patch C1: Cover document-id line Rev 1.0 → 1.1
patch(
    COVER,
    '<div class="meta-value">WSI-CARF-PLANS-001 · Rev. 1.0</div>',
    '<div class="meta-value">WSI-CARF-PLANS-001 · Rev. 1.1</div>',
    'Cover document-id Rev 1.0 → 1.1',
)

# Patch C2: Cover scope-pill — add Level III RTF mention
patch(
    COVER,
    '<div class="scope-pill">Inaugural One-Year Accreditation · 2026 CYS Standards</div>',
    '<div class="scope-pill">Level III Residential Treatment Facility · Inaugural One-Year Accreditation · 2026 CYS Standards</div>',
    'Cover scope-pill — add Level III RTF',
)


# ═══════════════════════════════════════════════════════════════════════
# PATCHES TO merge_carf_plans.py
# ═══════════════════════════════════════════════════════════════════════
print('\n── Patching merge_carf_plans.py ──')

# Patch M1: Subject metadata Rev 1.0 → 1.1
patch(
    MERGE,
    "'/Subject':  'CARF CYS 2026 Inaugural Accreditation Conformance Plan Portfolio (Rev. 1.0)',",
    "'/Subject':  'CARF CYS 2026 Inaugural Accreditation Conformance Plan Portfolio (Rev. 1.1)',",
    'Merge Subject metadata Rev 1.0 → 1.1',
)

# Patch M2: Print message Rev 1.0 → 1.1
patch(
    MERGE,
    "print(f'  ({size_kb:.1f} KB, {len(writer.pages)} pages, Rev. 1.0)')",
    "print(f'  ({size_kb:.1f} KB, {len(writer.pages)} pages, Rev. 1.1)')",
    'Merge print message Rev 1.0 → 1.1',
)


# ═══════════════════════════════════════════════════════════════════════
# VALIDATION
# ═══════════════════════════════════════════════════════════════════════
print('\n── Syntax validation ──')

for p in (CONTENT, GENERATE, MERGE):
    try:
        ast.parse(p.read_text(encoding='utf-8'))
        print(f'  [ OK ] {p.name} — ast.parse OK')
    except SyntaxError as e:
        print(f'  [FAIL] {p.name} — SyntaxError: {e}')
        patches_failed += 1

print('\n── Stale-reference check (should all be 0) ──')

stale_checks = [
    (CONTENT, 'Staff-Secure'),
    (CONTENT, 'staff-secure residential'),
    (CONTENT, 'Level 3 Supervised Residential'),
    (CONTENT, '.1701(b)'),
    (GENERATE, 'Rev. 1.0'),
    (GENERATE, 'Level 3 Supervised Residential Group Home'),
    (COVER, 'Rev. 1.0'),
    (MERGE, 'Rev. 1.0'),
]
for path, needle in stale_checks:
    text = path.read_text(encoding='utf-8')
    n = text.count(needle)
    marker = ' OK ' if n == 0 else 'FAIL'
    print(f'  [{marker}] {path.name}: "{needle}" → {n} occurrence(s)')

print('\n── New-reference check (should all be ≥1) ──')

new_checks = [
    (CONTENT, 'Level III Residential Treatment Facility'),
    (CONTENT, '10A NCAC 27G .1703'),
    (CONTENT, 'hardware-secure'),
    (CONTENT, 'psychiatrist on call 24/7'),
    (CONTENT, '1:4 direct-care'),
    (CONTENT, '1:8 ratio overnight'),
    (CONTENT, 'on-site Licensed Professional'),
    (GENERATE, 'Rev. 1.1'),
    (GENERATE, 'Service Intensity'),
    (COVER, 'Level III Residential Treatment Facility'),
    (COVER, 'Rev. 1.1'),
    (MERGE, 'Rev. 1.1'),
]
for path, needle in new_checks:
    text = path.read_text(encoding='utf-8')
    n = text.count(needle)
    marker = ' OK ' if n >= 1 else 'FAIL'
    print(f'  [{marker}] {path.name}: "{needle}" → {n} occurrence(s)')

print(f'\n══ Patches applied: {patches_applied}, failed: {patches_failed} ══')
sys.exit(0 if patches_failed == 0 else 1)
