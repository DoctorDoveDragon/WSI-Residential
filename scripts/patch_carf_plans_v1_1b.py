#!/usr/bin/env python3
"""
patch_carf_plans_v1_1b.py — v1.1 Level III RTF calibration (Take 2).

Uses exact source-code matching (multi-line Python string literals preserved)
to fix the patches that failed in v1.1a.  Only patches the carf_plans_content.py
file; the generate/cover/merge patches already succeeded in v1.1a.
"""

import ast
import sys
from pathlib import Path

CONTENT = Path('/home/z/my-project/scripts/carf_plans_content.py')

patches_applied = 0
patches_failed = 0


def patch(path: Path, old: str, new: str, label: str) -> None:
    global patches_applied, patches_failed
    text = path.read_text(encoding='utf-8')
    count = text.count(old)
    if count == 0:
        print(f'  [FAIL] {label}: old_str not found')
        patches_failed += 1
        return
    if count > 1:
        print(f'  [FAIL] {label}: old_str matches {count} times — needs more context')
        patches_failed += 1
        return
    new_text = text.replace(old, new, 1)
    path.write_text(new_text, encoding='utf-8')
    print(f'  [ OK ] {label}')
    patches_applied += 1


print('\n── Patching carf_plans_content.py (Take 2) ──')

# ─── Patch 1: Plan 1 §1.4 Populations & Services ─────────────────────
patch(
    CONTENT,
    """        'criteria but require removal from the home and treatment in a staff-secure '
        'residential setting. The service array includes: residential care in a '
        'Level III Staff-Secure facility; clinical services including individual, '
        'group, and family therapy; psychiatric medication management; behavioral '
        'support and crisis intervention; educational coordination through the '
        'local public school system; case management and care coordination with '
        'the LME/MCO and other system-of-care partners; and structured '
        'recreational, social, and life-skills programming.'""",
    """        'criteria but require removal from the home and treatment in a Level '
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
        'integrated into the daily milieu-therapy schedule.'""",
    'Plan 1 §1.4 — Level III RTF service array expansion',
)

# ─── Patch 2: Plan 3 §3.4 Licensure bullet ───────────────────────────
patch(
    CONTENT,
    """        '<b>Licensure.</b> Level III Residential Treatment Facility — Staff '
        'Secure license issued by the state mental health authority (SOP §1.2); '
        'renewed prior to expiration; changes in ownership, capacity, population, '
        'or location require prior written approval.',""",
    """        '<b>Licensure.</b> Level III Residential Treatment Facility '
        '(Hardware-Secure) license issued by the NC Department of Health and '
        'Human Services under 10A NCAC 27G .1703 (SOP §1.2); renewed prior '
        'to expiration; changes in ownership, capacity, population, or '
        'location require prior written approval. Level III is the highest-'
        'acuity NC RTF category and authorizes the organization to serve '
        'children and adolescents with severe emotional disturbance whose '
        'clinical needs cannot be safely met in a less restrictive (Level I '
        'or II) residential setting.',""",
    'Plan 3 §3.4 Licensure bullet — Level III RTF .1703 citation',
)

# ─── Patch 3: Plan 11 §11.2 Populations Served ───────────────────────
patch(
    CONTENT,
    """        'criteria but require removal from the home '
        'and treatment in a staff-secure residential setting. The program '
        'is designed to serve youth with severe emotional disturbance '
        '(SED) who require intensive, active therapeutic treatment within '
        'a system-of-care approach. Admission criteria are documented in '
        'SOP §3.1 and the Screening and Access Policy (Plan 12).'""",
    """        'criteria but require removal from the home '
        'and treatment in a Level III Residential Treatment Facility '
        '(hardware-secure, intensive clinical). The program is designed '
        'to serve youth with severe emotional disturbance (SED) whose '
        'clinical acuity exceeds what can be safely managed in a less '
        'restrictive Level I or Level II residential setting, and who '
        'require intensive, active therapeutic treatment within a '
        'system-of-care approach. Admission criteria are documented in '
        'SOP §3.1 and the Screening and Access Policy (Plan 12).'""",
    'Plan 11 §11.2 Populations Served — Level III RTF calibration',
)

# ─── Patch 4: Plan 11 §11.3 residential care bullet ──────────────────
patch(
    CONTENT,
    """        '<b>Residential care</b> — 24-hour supervised living in a Level '
        'III Staff-Secure facility (SOP §9);',""",
    """        '<b>Residential treatment</b> — 24-hour intensive residential '
        'treatment in a Level III RTF (hardware-secure) licensed under '
        '10A NCAC 27G .1703 (SOP §9);',""",
    'Plan 11 §11.3 Service Array — residential treatment bullet',
)

# ─── Patch 5: Plan 11 §11.5 Staffing Patterns ────────────────────────
patch(
    CONTENT,
    """        'The program is staffed per SOP §2, including: Executive Director, '
        'Clinical Director, Qualified Professional (QP), Associated '
        'Professionals (APs), Direct Care Professionals (DCPs) on day, '
        'evening, and awake-overnight shifts, House Manager, Registered '
        'Nurse (RN), and Billing Coordinator. Staffing ratios comply '
        'with the Level III Staff-Secure operating standards, including '
        'continuous supervision and awake overnight staff per .1701(b) '
        'and .1704. The QP provides clinical supervision per §1.4(a) and '
        '§2.2(a). A Licensed Professional provides minimum 4 hours per '
        'week face-to-face clinical consultation per §4.6 and Form 10.'""",
    """        'The program is staffed per SOP §2, including: Executive Director, '
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
        'clinical consultation per §4.6 and Form 10.'""",
    'Plan 11 §11.5 Staffing Patterns — Level III RTF ratios + psychiatrist/RN 24/7',
)

# ─── Patch 6: Plan 11 §11.6 Physical Environment ─────────────────────
patch(
    CONTENT,
    """        'The facility is a free-standing residential treatment facility '
        'designed and licensed as Level III Staff-Secure for children '
        'and adolescents. Physical-plant requirements are documented in '
        'SOP §9. The facility includes: resident bedrooms (single or '
        'double occupancy per licensing standards); communal dining and '
        'living areas; kitchen and food-storage areas; clinical offices '
        'and therapy rooms; a quiet room (not used for seclusion); '
        'medication storage area (double-locked per SOP §6.3(c)); '
        'laundry facilities; outdoor recreation area; and administrative '
        'offices. The facility complies with NFPA 101 Life Safety Code, '
        'ADA accessibility standards, and state fire/building codes.'""",
    """        'The facility is a free-standing residential treatment facility '
        'designed and licensed as a Level III Residential Treatment '
        'Facility (Hardware-Secure) under 10A NCAC 27G .1703 for '
        'children and adolescents. Physical-plant requirements are '
        'documented in SOP §9. The facility includes: resident bedrooms '
        '(single or double occupancy per licensing standards); communal '
        'dining and living areas; kitchen and food-storage areas; '
        'clinical offices and therapy rooms; a quiet room / de-escalation '
        'room (not used for seclusion — seclusion is prohibited under '
        'the organization\\'s restraint-and-seclusion-minimization policy '
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
        'under .1703.'""",
    'Plan 11 §11.6 Physical Environment — Level III RTF hardware-secure features',
)

# ─── Patch 7: Plan 12 §12.4 Screening Criteria ───────────────────────
patch(
    CONTENT,
    """        'substance-related disorder); (c) clinical acuity (does not '
        'meet inpatient criteria but requires staff-secure residential '
        'treatment); (d) medical stability (no acute medical condition '""",
    """        'substance-related disorder); (c) clinical acuity (does not '
        'meet inpatient criteria but requires the Level III RTF level '
        'of care — i.e., hardware-secure, intensive clinical services '
        'with 24-hour on-site Licensed Professional availability and '
        'psychiatric on-call, and whose acuity exceeds what can be '
        'safely managed in a less restrictive Level I or II setting); '
        '(d) medical stability (no acute medical condition '""",
    'Plan 12 §12.4 Screening Criteria — Level III RTF acuity descriptor',
)


# ═══════════════════════════════════════════════════════════════════════
# VALIDATION
# ═══════════════════════════════════════════════════════════════════════
print('\n── Syntax validation ──')
try:
    ast.parse(CONTENT.read_text(encoding='utf-8'))
    print('  [ OK ] carf_plans_content.py — ast.parse OK')
except SyntaxError as e:
    print(f'  [FAIL] carf_plans_content.py — SyntaxError: {e}')
    patches_failed += 1

print('\n── Stale-reference check (should all be 0) ──')
text = CONTENT.read_text(encoding='utf-8')
stale_checks = [
    'Staff-Secure',
    'staff-secure residential',
    'Level 3 Supervised Residential',
    '.1701(b)',
]
for needle in stale_checks:
    n = text.count(needle)
    marker = ' OK ' if n == 0 else 'FAIL'
    print(f'  [{marker}] carf_plans_content.py: "{needle}" → {n} occurrence(s)')

print('\n── New-reference check (should all be ≥1) ──')
new_checks = [
    'Level III Residential Treatment Facility',
    '10A NCAC 27G .1703',
    'hardware-secure',
    'psychiatrist',
    '1:4 direct-care',
    '1:8 ratio overnight',
    'on-site Licensed Professional',
    'controlled-egress',
]
for needle in new_checks:
    n = text.count(needle)
    marker = ' OK ' if n >= 1 else 'FAIL'
    print(f'  [{marker}] carf_plans_content.py: "{needle}" → {n} occurrence(s)')

print(f'\n══ Patches applied: {patches_applied}, failed: {patches_failed} ══')
sys.exit(0 if patches_failed == 0 else 1)
