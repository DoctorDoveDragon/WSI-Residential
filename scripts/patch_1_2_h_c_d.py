#!/usr/bin/env python3
"""patch_1_2_h_c_d.py — Rewrite §1.2(h)(c) and add new (d) cross-ref note."""
import os

path = '/home/z/my-project/scripts/sop_content_v3.py'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# The source code uses facility\'s (escaped apostrophe in single-quoted string)
old_c = """    story.append(para(
        '<b>(c) No operational impact.</b> Nothing in this \u00a71.2(h) changes the facility\\'s '
        'license category (Level III RTF \u2014 Staff Secure under <b>our staff-secure operating standards</b>), '
        'its staffing ratios (2:4 minimum per \u00a72.1), its admission physical-exam timing '
        '(90 days prior per \u00a76.1), its resident-rights obligations (the Resident Rights framework '
        'per \u00a71.7), its Medicaid taxonomy (320800000X per \u00a71.9), or its room-and-board '
        'exclusion (per \u00a71.2(g) and \u00a710.9). <b>The .2600 \u2192 .1700 citation question '
        '(subsection (a) above) has been resolved in v2.21;</b> the CCP 8C vs CCP 8D-2 '
        'citation question (subsection (b) above) remains open and shall be resolved in a '
        '<b>v2.22 revision</b> entry in the Version History table in Part 3 following '
        'Alliance Health / NCTracks enrollment confirmation per \u00a71.9. In the interim, '
        '\u00a71.2(g), \u00a71.9, and \u00a710.9 already cite CCP 8D-2 as the operative authority for '
        'the RTS benefit and the room-and-board exclusion; those subsections control in '
        'the event of any inconsistency with the legacy "CCP 8C" reference lines elsewhere '
        'in this Manual.'
    ))"""

new_c_plus_d = """    story.append(para(
        '<b>(c) No operational impact.</b> Nothing in this \u00a71.2(h) changes the facility\\'s '
        'license category (Level III RTF \u2014 Staff Secure under <b>our staff-secure operating standards</b>), '
        'its staffing ratios (2:4 minimum per \u00a72.1), its admission physical-exam timing '
        '(90 days prior per \u00a76.1), its resident-rights obligations (the Resident Rights framework '
        'per \u00a71.7), its Medicaid taxonomy (320800000X per \u00a71.9), or its room-and-board '
        'exclusion (per \u00a71.2(g) and \u00a710.9). <b>The .2600 \u2192 .1700 citation question '
        '(subsection (a) above) was resolved in v2.21; the CCP 8C \u2192 CCP 8D-2 citation '
        'question (subsection (b) above) is resolved in this v2.23 revision.</b> With both '
        'citation questions now closed, \u00a71.2(h) is fully resolved and no open compliance '
        'flags remain in this subsection.'
    ))
    story.append(para(
        '<b>(d) Cross-reference clarification note (compliance binder).</b> The Level III '
        'Staff-Secure operating standards cross-reference the "Qualified professional" '
        'definition for the QP credentialing requirements in \u00a71.4(b). The text of that '
        'rule cross-references subsection .0104(18) "Psychiatrist," which appears to be a '
        'typographical error in the rule itself \u2014 the operative definition is at '
        '.0104(21) "Qualified professional." This Manual applies the .0104(21) definition '
        'as the operative QP standard per \u00a71.4(b). The QP shall retain this '
        'cross-reference clarification note in the facility compliance binder and shall '
        'confirm the discrepancy with the assigned Licensure &amp; Training Consultant at '
        'the first in-person meeting per \u00a71.2(e).'
    ))"""

if old_c in content:
    content = content.replace(old_c, new_c_plus_d)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print('[OK] §1.2(h)(c) rewritten + new (d) cross-reference note added')
else:
    print('[MISS] §1.2(h)(c) not found')
    # Debug: show actual chars
    import re
    m = re.search(r'\(c\) No operational.{200}', content)
    if m:
        print('actual:', repr(m.group(0)))
