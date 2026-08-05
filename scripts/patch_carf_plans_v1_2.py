#!/usr/bin/env python3
"""
patch_carf_plans_v1_2.py — Revert Level III RTF calibration and re-calibrate
to Staff Secure Group Home (Rev 1.1 → Rev 1.2).

User correction (Aug 2026): the earlier "Level III Residential Treatment
Facility" designation was in error. The correct service type is a Staff Secure
Group Home — a less acute level of residential care than a Level III RTF.

This patch:
  1. Reverts the Level III RTF / hardware-secure / .1703 references back to
     "Staff Secure Group Home" terminology.
  2. Adjusts staffing ratios from 1:4 waking / 1:3 line-of-sight to the
     staff-secure group-home standard of 1:6 waking / 1:8 overnight with
     awake overnight staff.
  3. Removes the hardware-secure physical-plant features (controlled-egress
     doors, alarmed perimeter video monitoring, secured visitor vestibule)
     and replaces with staff-secure features (staff-supervised egress,
     door/window alarms as appropriate, controlled visitor entry).
  4. Adjusts clinical-intensity language: replaces "psychiatrist on call 24/7
     for psychiatric emergencies" with "Licensed Professional on-call 24/7
     for clinical emergencies; psychiatrist available for medication
     management per the PCP schedule"; removes "RN on-site or on-call 24/7"
     (replaced with "RN available for medical consultation per the PCP
     schedule and on-call for urgent medical needs").
  5. Updates the elopement risk row to reflect staff-secure (not hardware-
     secure) physical plant.
  6. Updates Plan 12 §12.4 (Screening Criteria) to remove the Level III RTF
     acuity descriptor and replace with the staff-secure group-home level
     of care.
  7. Bumps Rev 1.1 → Rev 1.2 across generate_carf_plans.py, cover HTML, and
     merge_carf_plans.py.
  8. Updates the About-page Service Type + Service Intensity lines.

Files patched:
  - /home/z/my-project/scripts/carf_plans_content.py    (7 patches)
  - /home/z/my-project/scripts/generate_carf_plans.py   (7 patches)
  - /home/z/my-project/scripts/carf_plans_cover.html    (2 patches)
  - /home/z/my-project/scripts/merge_carf_plans.py      (2 patches)
"""

import ast
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
    global patches_applied, patches_failed
    text = path.read_text(encoding='utf-8')
    count = text.count(old)
    if count == 0:
        print(f'  [FAIL] {label}: old_str not found in {path.name}')
        patches_failed += 1
        return
    if count > 1:
        print(f'  [FAIL] {label}: old_str matches {count} times in {path.name}')
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

# Patch 1: Plan 1 §1.4 Populations & Services — revert to Staff Secure Group Home
patch(
    CONTENT,
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
    """        'criteria but require removal from the home and treatment in a '
        'staff-secure group home setting. The service array includes: '
        '24-hour supervised residential care in a Staff Secure Group Home '
        'licensed under 10A NCAC 27G; clinical services including '
        'individual therapy (minimum weekly), group therapy (multiple times '
        'per week), family therapy (as clinically indicated, minimum '
        'biweekly), and clinical assessments; psychiatric medication '
        'management with psychiatric consultation per the Person-Centered '
        'Plan schedule and on-call psychiatric consultation for urgent '
        'clinical concerns; behavioral support and crisis intervention '
        'with continuous staff supervision; educational coordination '
        'through the local public school system or facility-based '
        'instructional programming; case management and care coordination '
        'with the LME/MCO and other system-of-care partners; and structured '
        'recreational, social, and life-skills programming integrated into '
        'the daily activity schedule.'""",
    'Plan 1 §1.4 — revert to Staff Secure Group Home',
)

# Patch 2: Plan 3 §3.4 Licensure bullet — revert to Staff Secure Group Home
patch(
    CONTENT,
    """        '<b>Licensure.</b> Level III Residential Treatment Facility '
        '(Hardware-Secure) license issued by the NC Department of Health and '
        'Human Services under 10A NCAC 27G .1703 (SOP §1.2); renewed prior '
        'to expiration; changes in ownership, capacity, population, or '
        'location require prior written approval. Level III is the highest-'
        'acuity NC RTF category and authorizes the organization to serve '
        'children and adolescents with severe emotional disturbance whose '
        'clinical needs cannot be safely met in a less restrictive (Level I '
        'or II) residential setting.',""",
    """        '<b>Licensure.</b> Staff Secure Group Home license issued by '
        'the NC Department of Health and Human Services under 10A NCAC 27G '
        '(SOP §1.2); renewed prior to expiration; changes in ownership, '
        'capacity, population, or location require prior written approval. '
        'The Staff Secure Group Home level of care serves children and '
        'adolescents with serious emotional disturbance who require 24-hour '
        'supervised residential care with structured clinical services and '
        'continuous staff supervision, but who do not require the '
        'intensive, hardware-secure level of care provided in a Level III '
        'Residential Treatment Facility.',""",
    'Plan 3 §3.4 Licensure bullet — Staff Secure Group Home',
)

# Patch 3: Plan 5 §5.4 Enterprise Risk Register — elopement row, staff-secure
patch(
    CONTENT,
    "['Clinical', 'Elopement from facility', '2', '5', 'Hardware-secure Level III RTF physical plant with controlled-egress doors (key-card / staff-controlled); alarmed perimeter; awake overnight line-of-sight supervision; elopement risk assessment at admission & weekly; community-search protocol; police notification within 30 min', 'QP', 'Quarterly'],",
    "['Clinical', 'Elopement from facility', '3', '4', 'Staff-secure group home with continuous staff supervision; awake overnight staff; elopement risk assessment at admission & weekly; staff protocol for missing-resident response; community-search procedure; police notification within 30 min if not located', 'QP', 'Quarterly'],",
    'Plan 5 §5.4 Risk Register — elopement row (staff-secure)',
)

# Patch 4: Plan 11 §11.2 Populations Served — revert to staff-secure group home
patch(
    CONTENT,
    """        'inpatient psychiatric criteria but require removal from the home '
        'and treatment in a Level III Residential Treatment Facility '
        '(hardware-secure, intensive clinical). The program is designed '
        'to serve youth with severe emotional disturbance (SED) whose '
        'clinical acuity exceeds what can be safely managed in a less '
        'restrictive Level I or Level II residential setting, and who '
        'require intensive, active therapeutic treatment within a '
        'system-of-care approach. Admission criteria are documented in '
        'SOP §3.1 and the Screening and Access Policy (Plan 12).'""",
    """        'inpatient psychiatric criteria but require removal from the home '
        'and treatment in a staff-secure group home setting. The program '
        'is designed to serve youth with serious emotional disturbance '
        'who require 24-hour supervised residential care with structured '
        'clinical services and continuous staff supervision, but who do '
        'not require the intensive, hardware-secure level of care '
        'provided in a Level III Residential Treatment Facility. '
        'Admission criteria are documented in SOP §3.1 and the Screening '
        'and Access Policy (Plan 12).'""",
    'Plan 11 §11.2 Populations Served — Staff Secure Group Home',
)

# Patch 5: Plan 11 §11.3 residential treatment bullet → residential care
patch(
    CONTENT,
    """        '<b>Residential treatment</b> — 24-hour intensive residential '
        'treatment in a Level III RTF (hardware-secure) licensed under '
        '10A NCAC 27G .1703 (SOP §9);',""",
    """        '<b>Residential care</b> — 24-hour supervised living in a '
        'Staff Secure Group Home licensed under 10A NCAC 27G (SOP §9);',""",
    'Plan 11 §11.3 Service Array — residential care bullet (staff-secure)',
)

# Patch 6: Plan 11 §11.5 Staffing Patterns — staff-secure group home ratios
patch(
    CONTENT,
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
    """        'The program is staffed per SOP §2, including: Executive Director, '
        'Clinical Director, Qualified Professional (QP), Associated '
        'Professionals (APs), Direct Care Professionals (DCPs) on day, '
        'evening, and awake-overnight shifts, House Manager, Registered '
        'Nurse (RN), and Billing Coordinator. Staffing ratios comply with '
        'the Staff Secure Group Home operating standards under 10A NCAC '
        '27G, including a minimum 1:6 direct-care staff-to-resident ratio '
        'during waking hours, and a minimum 1:8 ratio overnight with at '
        'least one awake DCP at all times. A Licensed Professional (LP) '
        'is on-site during business hours and on call 24/7 for clinical '
        'emergencies. A psychiatrist is available for medication-'
        'management appointments per the Person-Centered Plan schedule '
        'and is on call for urgent psychiatric consultation. A Registered '
        'Nurse (RN) is available on-site per the medication-management '
        'and health-services schedule and on call for urgent medical '
        'needs. The QP provides clinical supervision per §1.4(a) and '
        '§2.2(a). A Licensed Professional provides minimum 4 hours per '
        'week face-to-face clinical consultation per §4.6 and Form 10.'""",
    'Plan 11 §11.5 Staffing Patterns — Staff Secure Group Home ratios',
)

# Patch 7: Plan 11 §11.6 Physical Environment — staff-secure (not hardware-secure)
patch(
    CONTENT,
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
    """        'The facility is a free-standing residential facility designed '
        'and licensed as a Staff Secure Group Home under 10A NCAC 27G '
        'for children and adolescents. Physical-plant requirements are '
        'documented in SOP §9. The facility includes: resident bedrooms '
        '(single or double occupancy per licensing standards); communal '
        'dining and living areas; kitchen and food-storage areas; '
        'clinical offices and therapy rooms; a quiet room / de-escalation '
        'room (not used for seclusion — seclusion is prohibited under '
        "the organization's restraint-and-seclusion-minimization policy "
        'per SOP §5); medication storage area (double-locked per SOP '
        '§6.3(c)); laundry facilities; outdoor recreation area; and '
        'administrative offices. Staff-secure features include '
        'continuous staff supervision of residents, staff-monitored '
        'entry and exit (doors may be locked to elopement risk with '
        'staff-controlled release), door and window alarms as '
        'appropriate to the resident population, and a controlled '
        'visitor-entry process. The facility complies with NFPA 101 '
        'Life Safety Code, ADA accessibility standards, and state '
        'fire/building codes applicable to staff-secure group homes.'""",
    'Plan 11 §11.6 Physical Environment — Staff Secure Group Home',
)

# Patch 8: Plan 12 §12.4 Screening Criteria — staff-secure group home acuity
patch(
    CONTENT,
    """        'substance-related disorder); (c) clinical acuity (does not '
        'meet inpatient criteria but requires the Level III RTF level '
        'of care — i.e., hardware-secure, intensive clinical services '
        'with 24-hour on-site Licensed Professional availability and '
        'psychiatric on-call, and whose acuity exceeds what can be '
        'safely managed in a less restrictive Level I or II setting); '
        '(d) medical stability (no acute medical condition '""",
    """        'substance-related disorder); (c) clinical acuity (does not '
        'meet inpatient criteria but requires the staff-secure group '
        'home level of care — i.e., 24-hour supervised residential '
        'care with structured clinical services and continuous staff '
        'supervision, and whose needs cannot be safely met in a less '
        'restrictive community-based setting); (d) medical stability '
        '(no acute medical condition '""",
    'Plan 12 §12.4 Screening Criteria — staff-secure group home acuity',
)


# ═══════════════════════════════════════════════════════════════════════
# PATCHES TO generate_carf_plans.py
# ═══════════════════════════════════════════════════════════════════════
print('\n── Patching generate_carf_plans.py ──')

# Patch G1: DOC_TITLE_SHORT header
patch(
    GENERATE,
    "DOC_TITLE_SHORT = 'CARF CYS 2026 Conformance Plans — Rev. 1.1 (Aug 2026)'",
    "DOC_TITLE_SHORT = 'CARF CYS 2026 Conformance Plans — Rev. 1.2 (Aug 2026)'",
    'DOC_TITLE_SHORT Rev 1.1 → 1.2',
)

# Patch G2: TOC intro doc-id reference
patch(
    GENERATE,
    "'(Doc. WSI-CARF-PLANS-001, Rev. 1.1, Aug 2026)'",
    "'(Doc. WSI-CARF-PLANS-001, Rev. 1.2, Aug 2026)'",
    'TOC intro doc-id Rev 1.1 → 1.2',
)

# Patch G3: PDF Subject metadata
patch(
    GENERATE,
    "subject='CARF CYS 2026 Inaugural Accreditation Conformance Plan Portfolio (Rev. 1.1)',",
    "subject='CARF CYS 2026 Inaugural Accreditation Conformance Plan Portfolio (Rev. 1.2)',",
    'PDF subject metadata Rev 1.1 → 1.2',
)

# Patch G4: About-page intro paragraph
patch(
    GENERATE,
    "'This portfolio (Rev. 1.1, August 2026) contains the fifteen written '",
    "'This portfolio (Rev. 1.2, August 2026) contains the fifteen written '",
    'About-page intro Rev 1.1 → 1.2',
)

# Patch G5: About-page Document ID line
patch(
    GENERATE,
    "'<b>Document ID.</b> Doc. WSI-CARF-PLANS-001, Rev. 1.1 (August 2026).', s_body))",
    "'<b>Document ID.</b> Doc. WSI-CARF-PLANS-001, Rev. 1.2 (August 2026).', s_body))",
    'About-page Document ID Rev 1.1 → 1.2',
)

# Patch G6: About-page Service Type + Service Intensity lines
patch(
    GENERATE,
    """    story.append(Paragraph('<b>Service Type.</b> Level III Residential Treatment Facility (Hardware-Secure) \\u2014 10A NCAC 27G .1703.', s_body))
    story.append(Paragraph('<b>Service Intensity.</b> Level III is the highest-acuity NC residential treatment category, providing 24-hour intensive clinical services for children and adolescents with severe emotional disturbance (SED) whose needs cannot be safely met in a less restrictive (Level I or II) setting. Features include hardware-secure (controlled-egress) physical plant, on-site Licensed Professional coverage 16 hours/day, psychiatrist on-call 24/7, RN on-site or on-call 24/7, 1:4 waking staff-to-resident ratio, daily clinical groups, individual therapy minimum twice weekly, family therapy minimum weekly, and weekly Person-Centered Plan reviews.', s_body))""",
    """    story.append(Paragraph('<b>Service Type.</b> Staff Secure Group Home \\u2014 10A NCAC 27G.', s_body))
    story.append(Paragraph('<b>Service Intensity.</b> The Staff Secure Group Home provides 24-hour supervised residential care for children and adolescents with serious emotional disturbance who require structured clinical services and continuous staff supervision, but whose needs can be safely met without the hardware-secure physical plant and on-site intensive clinical staffing of a Level III Residential Treatment Facility. Features include staff-supervised egress (doors may be locked to manage elopement risk), continuous staff supervision, awake overnight staff, minimum 1:6 direct-care staff-to-resident ratio during waking hours and 1:8 overnight, Licensed Professional on-site during business hours and on-call 24/7, psychiatrist available per the Person-Centered Plan medication-management schedule, RN available per the health-services schedule and on-call for urgent medical needs, individual therapy minimum weekly, group therapy multiple times per week, family therapy as clinically indicated, and Person-Centered Plan reviews at minimum every 90 days or as clinically indicated.', s_body))""",
    'About-page Service Type + Service Intensity — Staff Secure Group Home',
)


# ═══════════════════════════════════════════════════════════════════════
# PATCHES TO carf_plans_cover.html
# ═══════════════════════════════════════════════════════════════════════
print('\n── Patching carf_plans_cover.html ──')

# Patch C1: Cover document-id line Rev 1.1 → 1.2
patch(
    COVER,
    '<div class="meta-value">WSI-CARF-PLANS-001 · Rev. 1.1</div>',
    '<div class="meta-value">WSI-CARF-PLANS-001 · Rev. 1.2</div>',
    'Cover document-id Rev 1.1 → 1.2',
)

# Patch C2: Cover scope-pill — replace Level III RTF with Staff Secure Group Home
patch(
    COVER,
    '<div class="scope-pill">Level III Residential Treatment Facility · Inaugural One-Year Accreditation · 2026 CYS Standards</div>',
    '<div class="scope-pill">Staff Secure Group Home · Inaugural One-Year Accreditation · 2026 CYS Standards</div>',
    'Cover scope-pill — Staff Secure Group Home',
)


# ═══════════════════════════════════════════════════════════════════════
# PATCHES TO merge_carf_plans.py
# ═══════════════════════════════════════════════════════════════════════
print('\n── Patching merge_carf_plans.py ──')

# Patch M1: Subject metadata Rev 1.1 → 1.2
patch(
    MERGE,
    "'/Subject':  'CARF CYS 2026 Inaugural Accreditation Conformance Plan Portfolio (Rev. 1.1)',",
    "'/Subject':  'CARF CYS 2026 Inaugural Accreditation Conformance Plan Portfolio (Rev. 1.2)',",
    'Merge Subject metadata Rev 1.1 → 1.2',
)

# Patch M2: Print message Rev 1.1 → 1.2
patch(
    MERGE,
    "print(f'  ({size_kb:.1f} KB, {len(writer.pages)} pages, Rev. 1.1)')",
    "print(f'  ({size_kb:.1f} KB, {len(writer.pages)} pages, Rev. 1.2)')",
    'Merge print message Rev 1.1 → 1.2',
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
    (CONTENT, 'Level III Residential Treatment Facility'),
    (CONTENT, 'Level III RTF'),
    (CONTENT, 'hardware-secure'),
    (CONTENT, 'Hardware-secure'),
    (CONTENT, '10A NCAC 27G .1703'),
    (CONTENT, 'controlled-egress'),
    (CONTENT, '1:4 direct-care'),
    (CONTENT, '1:3 for high-acuity'),
    (CONTENT, 'psychiatrist provides on-site coverage'),
    (CONTENT, 'on-site Licensed Professional'),
    (GENERATE, 'Rev. 1.1'),
    (GENERATE, 'Level III Residential Treatment Facility (Hardware-Secure)'),
    (COVER, 'Level III Residential Treatment Facility'),
    (COVER, 'Rev. 1.1'),
    (MERGE, 'Rev. 1.1'),
]
for path, needle in stale_checks:
    text = path.read_text(encoding='utf-8')
    n = text.count(needle)
    marker = ' OK ' if n == 0 else 'FAIL'
    print(f'  [{marker}] {path.name}: "{needle}" → {n} occurrence(s)')

print('\n── New-reference check (should all be ≥1) ──')

new_checks = [
    (CONTENT, 'Staff Secure Group Home'),
    (CONTENT, 'staff-secure group home'),
    (CONTENT, '1:6 direct-care'),
    (CONTENT, 'Licensed Professional (LP)'),
    (CONTENT, 'continuous staff supervision'),
    (GENERATE, 'Rev. 1.2'),
    (GENERATE, 'Staff Secure Group Home'),
    (COVER, 'Staff Secure Group Home'),
    (COVER, 'Rev. 1.2'),
    (MERGE, 'Rev. 1.2'),
]
for path, needle in new_checks:
    text = path.read_text(encoding='utf-8')
    n = text.count(needle)
    marker = ' OK ' if n >= 1 else 'FAIL'
    print(f'  [{marker}] {path.name}: "{needle}" → {n} occurrence(s)')

print(f'\n══ Patches applied: {patches_applied}, failed: {patches_failed} ══')
sys.exit(0 if patches_failed == 0 else 1)
