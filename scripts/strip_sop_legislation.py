#!/usr/bin/env python3
"""
Strip legislation references from SOP content modules — CONSERVATIVE PASS.

Strategy (safe, surgical):
  1. Copy v2 content modules to v3 files
  2. Remove `external='...'` first argument from ref_line() calls ONLY
     when the external string contains legislation keywords
  3. Remove inline parenthetical legislation citations like "(NCGS §122C-55)"
     ONLY when the entire parenthetical is a legislation reference
  4. Replace the most common legislation-citing sentence openers manually
     via targeted regex with surgical replacements
  5. Do NOT touch whitespace, do NOT collapse commas globally — those
     operations damage Python syntax inside string literals.

The legislated copy (v2.21 PDF) is retained as the compliance reference.
This v3 build is the public-facing operations manual.
"""
import re
import shutil
from pathlib import Path

SCRIPTS_DIR = Path('/home/z/my-project/scripts')

V2_FILES = [
    'sop_content_v2.py',
    'sop_content_v2_part2.py',
    'sop_content_v2_part3.py',
]
V3_FILES = [
    'sop_content_v3.py',
    'sop_content_v3_part2.py',
    'sop_content_v3_part3.py',
]

LEGIS_KW = re.compile(r'(?:NCGS|NCAC|G\.S\.|122C-|10A\sNCAC|RMDM|HIPAA|CFR|E-SIGN|NC\sMedicaid|CCP|Rule\s108|Chapter\s122C|G\.S\.)')


def strip_external_from_ref_line(text: str) -> str:
    """
    Remove the `external=` first argument from ref_line() calls.

    Three forms to handle:
      (a) ref_line('EXTERNAL', 'anchor')         -> ref_line('anchor')  if EXTERNAL has legislation
      (b) ref_line('EXTERNAL')                    -> ref_line()           if EXTERNAL has legislation
      (c) ref_line(external='X', anchor='Y')     -> ref_line(anchor='Y') if X has legislation
    """
    # Form (c): ref_line(external='X', anchor='Y')
    def repl_external_kw(m):
        ext = m.group(1)
        anc = m.group(2)
        if LEGIS_KW.search(ext):
            return f"ref_line(anchor={anc})"
        return m.group(0)
    text = re.sub(
        r"ref_line\(\s*external='([^']*)'\s*,\s*(anchor='[^']*')\s*\)",
        repl_external_kw,
        text,
    )

    # Form (a): ref_line('EXTERNAL', 'ANCHOR')  -- two positional args
    # Convert to ref_line(anchor='ANCHOR') if EXTERNAL contains legislation
    def repl_two_arg(m):
        ext = m.group(1)
        anc = m.group(2)
        if LEGIS_KW.search(ext):
            return f"ref_line(anchor='{anc}')"
        return m.group(0)
    text = re.sub(
        r"ref_line\(\s*'([^']*)'\s*,\s*'([^']*)'\s*\)",
        repl_two_arg,
        text,
    )

    # Form (b): ref_line('EXTERNAL')  -- single arg, only if legislation
    def repl_one_arg(m):
        ext = m.group(1)
        if LEGIS_KW.search(ext):
            return "ref_line()"
        return m.group(0)
    text = re.sub(
        r"ref_line\(\s*'([^']*)'\s*\)",
        repl_one_arg,
        text,
    )

    return text


def strip_inline_citations(text: str) -> str:
    """
    Remove inline legislation citations from body text —
    BUT only safe patterns that won't break Python syntax.

    Safe patterns:
      (a) "(NCGS §122C-55)"                            -> ""
      (b) "(per 10A NCAC 27G .1700)"                   -> ""
      (c) "NCGS §122C-55"                              -> "state rule" (placeholder)
      (d) "10A NCAC 27G .1700"                         -> "our operating standards"
      (e) "10A NCAC 27G .1701"                         -> "our operating standards"
      (f) "G.S. 122C-26"                               -> ""
      (g) "Authority G.S. 122C-26; 143B-147; Eff. April 3, 2006"  -> ""

    We do NOT touch commas or whitespace globally.
    """
    # (a) (b) — full parenthetical legislation citations
    # ONLY match parens that look like inline citations, i.e. they START with
    # a legislation keyword or citation opener. This prevents us from eating
    # entire Python tuples that happen to mention legislation somewhere in
    # their content.
    # Patterns matched:
    #   (NCGS §122C-55)              -> ""
    #   (per 10A NCAC 27G .1700)     -> ""
    #   (Authority G.S. ...)         -> ""
    #   (see NCGS §...)              -> ""
    text = re.sub(
        r"\(\s*(?:NCGS|NCAC|G\.S\.|10A\sNCAC|Authority\s+G\.S\.|per\s+10A\sNCAC|see\s+NCGS|see\s+also\s+NCGS|under\s+NCGS|under\s+10A\sNCAC|pursuant\s+to\s+NCGS)[^\n()]*?\)",
        "",
        text,
    )

    # (g) "(Authority G.S. ...; ... Eff. ...)" — already covered by (a)(b)
    # but also catch ones that span multiple sentences
    text = re.sub(
        r"\(Authority\s+G\.S\.[^)]*?Eff\.\s+\w+\s+\d+,\s+\d+\)",
        "",
        text,
    )

    # (c) (d) (e) (f) — bare references
    # Replace common patterns with operational language
    # NCGS §122C-XX through §122C-YY  -> "the Resident Rights Act"
    text = re.sub(
        r"NCGS\s*&sect;\s*122C-\d+\s+through\s+&sect;\s*122C-\d+",
        "the Resident Rights framework",
        text,
    )
    text = re.sub(
        r"NCGS\s*&sect;\s*122C-\d+(?:\s+et\s+seq\.)?",
        "the Resident Rights framework",
        text,
    )
    text = re.sub(
        r"NCGS\s+§\s*122C-\d+(?:\s+through\s+§\s*122C-\d+)?(?:\s+et\s+seq\.)?",
        "the Resident Rights framework",
        text,
    )
    # "NCGS §122C-224" specific
    text = re.sub(
        r"NCGS\s*(?:&sect;|§)\s*122C-224[^,.)]*",
        "state judicial review requirements",
        text,
    )
    # Chapter 122C
    text = re.sub(
        r"NCGS\s+Chapter\s+122C",
        "state mental health law",
        text,
    )
    text = re.sub(
        r"Chapter\s+122C",
        "state mental health law",
        text,
    )
    # 10A NCAC 27G .1700/.1701
    text = re.sub(
        r"10A\sNCAC\s+27G\s*\.\s*1701\s*(?:SCOPE)?",
        "our staff-secure operating standards",
        text,
    )
    text = re.sub(
        r"10A\sNCAC\s+27G\s*\.\s*1700",
        "our staff-secure operating standards",
        text,
    )
    text = re.sub(
        r"10A\sNCAC\s+27G\s*\.\s*\d{4}(?:\([a-z0-9]+\))*",
        "our operating standards",
        text,
    )
    text = re.sub(
        r"10A\sNCAC\s+27[A-Z]\s*\.\s*\d{4}(?:\([a-z0-9]+\))*",
        "our operating standards",
        text,
    )
    text = re.sub(
        r"10A\sNCAC\s+27T",
        "our clinical record standards",
        text,
    )
    text = re.sub(
        r"10A\sNCAC\s+27E\s*\.\s*\d{4}(?:\([a-z0-9]+\))*",
        "our service planning standards",
        text,
    )
    text = re.sub(
        r"10A\sNCAC\s+27G",
        "our operating standards",
        text,
    )
    text = re.sub(
        r"10A\sNCAC\s+\d+[A-Z](?:\s*\.\s*\d{4})?",
        "our operating standards",
        text,
    )
    # G.S. XXX-XX
    text = re.sub(
        r"G\.S\.\s+\d+[A-Z]*-\d+[A-Za-z]*(?:;\s*\d+[A-Z]*-\d+[A-Za-z]*)?",
        "state law",
        text,
    )
    # Bare "NCGS" leftover
    text = re.sub(
        r"\bNCGS\b",
        "state law",
        text,
    )

    # "Pursuant to <legislation>, ..." -> "Under our operating standards, ..."
    # CRITICAL: exclude newlines so we don't span across function call arguments.
    def pursuant_repl(m):
        prefix = m.group(0)
        # If the Pursuant-to clause contains legislation, replace opener
        if LEGIS_KW.search(prefix):
            return "Under our operating standards, "
        return m.group(0)
    text = re.sub(
        r"[Pp]ursuant to [^\n,.]{1,120}?,\s+",
        pursuant_repl,
        text,
    )

    # "Under <legislation>, ..." -> "Under our operating standards, ..."
    def under_repl(m):
        prefix = m.group(0)
        if LEGIS_KW.search(prefix):
            return "Under our operating standards, "
        return m.group(0)
    text = re.sub(
        r"[Uu]nder [^\n,.]{1,120}?,\s+",
        under_repl,
        text,
    )

    # "Consistent with <legislation>, ..." -> "Consistent with our operating standards, ..."
    def consistent_repl(m):
        prefix = m.group(0)
        if LEGIS_KW.search(prefix):
            return "Consistent with our operating standards, "
        return m.group(0)
    text = re.sub(
        r"[Cc]onsistent with [^\n,.]{1,120}?,\s+",
        consistent_repl,
        text,
    )

    # Cleanup — SURGICAL ONLY. Do NOT collapse double spaces globally,
    # because that destroys Python indentation. Do NOT touch whitespace
    # before commas — same reason. Only fix obvious sentence-level artifacts
    # that occur WITHIN string literals (between quotes).
    # We assume legislation stripping leaves minor double-space artifacts
    # in body text — those are acceptable and can be polished in a manual
    # pass if needed.

    return text


def process_file(src: Path, dst: Path) -> tuple[int, list[str]]:
    src_text = src.read_text()
    original_len = len(src_text)
    logs = []

    # Step 1: Strip external= args from ref_line() calls
    before = len(src_text)
    src_text = strip_external_from_ref_line(src_text)
    diff = before - len(src_text)
    if diff > 0:
        logs.append(f"  ref_line external args stripped ({diff} bytes)")

    # Step 2: Strip inline citations
    before = len(src_text)
    src_text = strip_inline_citations(src_text)
    diff = before - len(src_text)
    if diff > 0:
        logs.append(f"  inline legislation citations stripped ({diff} bytes)")

    # Step 3: Update version comment
    src_text = src_text.replace(
        'Content builders — Version 2.0',
        'Content builders — Version 3.0 (Legislation-Free Public Edition)',
    )

    total_bytes = original_len - len(src_text)
    logs.insert(0, f"  Total bytes removed: {total_bytes}")

    dst.write_text(src_text)
    return total_bytes, logs


def main():
    print("=" * 64)
    print("SOP Manual — Legislation Stripper (Conservative Pass)")
    print("Source: v2 content modules (RETAINED as legislated compliance copy)")
    print("Target: v3 content modules (public-facing operations manual)")
    print("=" * 64)

    total = 0
    for v2, v3 in zip(V2_FILES, V3_FILES):
        src = SCRIPTS_DIR / v2
        dst = SCRIPTS_DIR / v3
        print(f"\nProcessing {v2} -> {v3}")
        bytes_removed, logs = process_file(src, dst)
        total += bytes_removed
        for log in logs:
            print(log)

    print(f"\n{'=' * 64}")
    print(f"Total bytes stripped across all modules: {total}")


if __name__ == '__main__':
    main()
