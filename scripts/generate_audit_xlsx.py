"""
generate_audit_xlsx.py — Crosswalk matrix XLSX for the Well Spring Intervention
SOP Manual v2.22 Compliance Audit.

Output: /home/z/my-project/download/WSI_SOP_v2.22_Compliance_Audit_Crosswalk.xlsx

Workbook structure:
  Sheet 1: Audit Summary       — high-level stats, severity counts, strip counts
  Sheet 2: Findings Crosswalk  — one row per finding, all fields, filterable/sortable
  Sheet 3: Strip Recommendations — strip-flag findings only, with strip-and-replace text
  Sheet 4: Revision Roadmap    — v2.23 corrective action tracker with owner/target date columns
"""

import os
import sys
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from audit_findings import FINDINGS, summary_stats, SEVERITY_LEGEND, STATUS_LEGEND

from openpyxl import Workbook
from openpyxl.styles import (
    PatternFill, Font, Border, Side, Alignment, NamedStyle,
)
from openpyxl.utils import get_column_letter
from openpyxl.formatting.rule import CellIsRule, FormulaRule
from openpyxl.worksheet.table import Table, TableStyleInfo


# ─── Brand palette (Well Spring Intervention) ────────────────────────────
TERRACOTTA   = "7C2D12"   # deep terracotta — primary brand
CREAM        = "FAF6EE"   # warm cream parchment — page background
WALNUT       = "5C4A2E"   # walnut brown — secondary
SECTION_BG   = "F1ECE0"
TABLE_STRIPE = "F5F0E2"
BORDER_CLR   = "D6CFC0"
TEXT_PRIMARY = "1F2937"
TEXT_MUTED   = "6B6457"

# Severity colors (fills)
SEV_FILL = {
    "Critical": "7F1D1D",
    "High":     "991B1B",
    "Medium":   "B45309",
    "Low":      "4D7C0F",
    "Info":     "1E40AF",
}
# Status colors (fills)
STATUS_FILL = {
    "Met":         "166534",
    "Met-Exceeds": "166534",
    "Partial":     "B45309",
    "Gap":         "991B1B",
    "Contradicts": "7F1D1D",
    "N/A":         "6B6457",
}
# Lighter variants for row backgrounds
SEV_ROW_BG = {
    "Critical": "FECACA",
    "High":     "FEE2E2",
    "Medium":   "FEF3C7",
    "Low":      "ECFCCB",
    "Info":     "DBEAFE",
}

WHITE = "FFFFFF"

# ─── Reusable style components ────────────────────────────────────────────
def thin_border(color=BORDER_CLR):
    s = Side(border_style="thin", color=color)
    return Border(left=s, right=s, top=s, bottom=s)

def header_fill(color=TERRACOTTA):
    return PatternFill(start_color=color, end_color=color, fill_type="solid")

def header_font():
    return Font(name="Calibri", size=11, bold=True, color=WHITE)

def body_font(size=10, bold=False, color=TEXT_PRIMARY):
    return Font(name="Calibri", size=size, bold=bold, color=color)

def cell_alignment(wrap=True, h="left", v="top"):
    return Alignment(wrap_text=wrap, horizontal=h, vertical=v)


# ─── Build workbook ───────────────────────────────────────────────────────
def build_workbook(output_path):
    wb = Workbook()
    wb.properties.creator = "Z.ai"
    wb.properties.title = "WSI SOP v2.22 Compliance Audit Crosswalk"
    wb.properties.subject = "Rule-by-rule crosswalk of SOP Manual v2.22 against 10A NCAC 27G .1700 + core rules"

    # ─── Sheet 1: Audit Summary ──────────────────────────────────────────
    ws1 = wb.active
    ws1.title = "Audit Summary"

    # Title block
    ws1["A1"] = "Well Spring Intervention LLC"
    ws1["A1"].font = Font(name="Calibri", size=18, bold=True, color=TERRACOTTA)
    ws1["A2"] = "SOP Manual v2.22 — Compliance Audit Crosswalk Matrix"
    ws1["A2"].font = Font(name="Calibri", size=14, bold=True, color=TEXT_PRIMARY)
    ws1["A3"] = f"Doc. WSI-AUDIT-001 · Rev. 1.0 · Generated {datetime.now().strftime('%B %d, %Y')}"
    ws1["A3"].font = Font(name="Calibri", size=10, italic=True, color=TEXT_MUTED)
    ws1["A4"] = "Audit scope: 10A NCAC 27G .1700 + cross-referenced core rules (.0104, .0201-.0210)"
    ws1["A4"].font = Font(name="Calibri", size=10, color=TEXT_PRIMARY)

    stats = summary_stats()

    # Severity summary table
    ws1["A6"] = "Findings by Severity"
    ws1["A6"].font = Font(name="Calibri", size=12, bold=True, color=TERRACOTTA)
    ws1["A6"].fill = header_fill(SECTION_BG)
    ws1.merge_cells("A6:C6")

    headers = ["Severity", "Count", "Definition"]
    for col, h in enumerate(headers, start=1):
        c = ws1.cell(row=7, column=col, value=h)
        c.font = header_font()
        c.fill = header_fill()
        c.alignment = cell_alignment(h="center", v="center")
        c.border = thin_border()

    sev_order = ["Critical", "High", "Medium", "Low", "Info"]
    for i, sev in enumerate(sev_order, start=8):
        count = stats["by_severity"].get(sev, 0)
        ws1.cell(row=i, column=1, value=sev).font = body_font(bold=True, color=SEV_FILL[sev])
        ws1.cell(row=i, column=2, value=count).font = body_font(bold=True)
        ws1.cell(row=i, column=2).alignment = cell_alignment(h="center")
        ws1.cell(row=i, column=3, value=SEVERITY_LEGEND[sev]).font = body_font()
        for col in range(1, 4):
            ws1.cell(row=i, column=col).border = thin_border()
            ws1.cell(row=i, column=col).alignment = cell_alignment(h="left" if col != 2 else "center")

    # Total row
    total_row = 8 + len(sev_order)
    ws1.cell(row=total_row, column=1, value="TOTAL").font = body_font(bold=True, color=WHITE)
    ws1.cell(row=total_row, column=1).fill = header_fill(WALNUT)
    ws1.cell(row=total_row, column=2, value=stats["total_findings"]).font = body_font(bold=True, color=WHITE)
    ws1.cell(row=total_row, column=2).fill = header_fill(WALNUT)
    ws1.cell(row=total_row, column=2).alignment = cell_alignment(h="center")
    ws1.cell(row=total_row, column=3, value="").fill = header_fill(WALNUT)
    for col in range(1, 4):
        ws1.cell(row=total_row, column=col).border = thin_border()

    # Status summary table
    ws1["A15"] = "Findings by Status"
    ws1["A15"].font = Font(name="Calibri", size=12, bold=True, color=TERRACOTTA)
    ws1["A15"].fill = header_fill(SECTION_BG)
    ws1.merge_cells("A15:C15")

    for col, h in enumerate(["Status", "Count", "Definition"], start=1):
        c = ws1.cell(row=16, column=col, value=h)
        c.font = header_font()
        c.fill = header_fill()
        c.alignment = cell_alignment(h="center", v="center")
        c.border = thin_border()

    status_order = ["Met", "Met-Exceeds", "Partial", "Gap", "Contradicts", "N/A"]
    for i, st in enumerate(status_order, start=17):
        count = stats["by_status"].get(st, 0)
        ws1.cell(row=i, column=1, value=st).font = body_font(bold=True, color=STATUS_FILL[st])
        ws1.cell(row=i, column=2, value=count).font = body_font(bold=True)
        ws1.cell(row=i, column=2).alignment = cell_alignment(h="center")
        ws1.cell(row=i, column=3, value=STATUS_LEGEND[st]).font = body_font()
        for col in range(1, 4):
            ws1.cell(row=i, column=col).border = thin_border()
            ws1.cell(row=i, column=col).alignment = cell_alignment(h="left" if col != 2 else "center")

    # Strip flag summary
    ws1["A24"] = "Legislation-Stripping Summary"
    ws1["A24"].font = Font(name="Calibri", size=12, bold=True, color=TERRACOTTA)
    ws1["A24"].fill = header_fill(SECTION_BG)
    ws1.merge_cells("A24:C24")

    for col, h in enumerate(["Strip Flag", "Count", "Meaning"], start=1):
        c = ws1.cell(row=25, column=col, value=h)
        c.font = header_font()
        c.fill = header_fill()
        c.alignment = cell_alignment(h="center", v="center")
        c.border = thin_border()

    strip_rows = [
        ("Y", stats["by_strip"]["Y"], "Statutory/regulatory citation to strip and replace with plain-language text in v2.23 public edition."),
        ("N", stats["by_strip"]["N"], "Operational language only — no statutory citation to strip."),
    ]
    for i, (flag, count, meaning) in enumerate(strip_rows, start=26):
        ws1.cell(row=i, column=1, value=flag).font = body_font(bold=True, color=TERRACOTTA if flag == "Y" else TEXT_MUTED)
        ws1.cell(row=i, column=2, value=count).font = body_font(bold=True)
        ws1.cell(row=i, column=2).alignment = cell_alignment(h="center")
        ws1.cell(row=i, column=3, value=meaning).font = body_font()
        for col in range(1, 4):
            ws1.cell(row=i, column=col).border = thin_border()
            ws1.cell(row=i, column=col).alignment = cell_alignment(h="left" if col != 2 else "center")

    # Critical & High findings callout
    ws1["A30"] = "Critical & High Severity Findings (require v2.23 remediation)"
    ws1["A30"].font = Font(name="Calibri", size=12, bold=True, color=TERRACOTTA)
    ws1["A30"].fill = header_fill(SECTION_BG)
    ws1.merge_cells("A30:E30")

    ch_headers = ["Finding ID", "Rule", "Title", "Severity", "Status"]
    for col, h in enumerate(ch_headers, start=1):
        c = ws1.cell(row=31, column=col, value=h)
        c.font = header_font()
        c.fill = header_fill()
        c.alignment = cell_alignment(h="center", v="center")
        c.border = thin_border()

    for i, f in enumerate(stats["critical_high_findings"], start=32):
        ws1.cell(row=i, column=1, value=f["id"]).font = body_font(bold=True)
        ws1.cell(row=i, column=2, value=f["rule"]).font = body_font()
        ws1.cell(row=i, column=3, value=f["rule_title"]).font = body_font()
        ws1.cell(row=i, column=4, value=f["severity"]).font = body_font(bold=True, color=SEV_FILL[f["severity"]])
        ws1.cell(row=i, column=5, value=f["status"]).font = body_font(bold=True, color=STATUS_FILL[f["status"]])
        for col in range(1, 6):
            ws1.cell(row=i, column=col).border = thin_border()
            ws1.cell(row=i, column=col).alignment = cell_alignment(h="left")

    # Column widths
    ws1.column_dimensions["A"].width = 18
    ws1.column_dimensions["B"].width = 14
    ws1.column_dimensions["C"].width = 55
    ws1.column_dimensions["D"].width = 12
    ws1.column_dimensions["E"].width = 14

    # ─── Sheet 2: Findings Crosswalk ────────────────────────────────────
    ws2 = wb.create_sheet("Findings Crosswalk")

    # Title
    ws2["A1"] = "Findings Crosswalk — Rule-by-Rule Matrix"
    ws2["A1"].font = Font(name="Calibri", size=14, bold=True, color=TERRACOTTA)
    ws2.merge_cells("A1:K1")
    ws2["A2"] = "One row per finding. Filter, sort, and pivot as needed. All 56 findings listed."
    ws2["A2"].font = Font(name="Calibri", size=10, italic=True, color=TEXT_MUTED)
    ws2.merge_cells("A2:K2")

    headers = [
        "Finding ID", "Rule Citation", "Rule Title", "Status", "Severity",
        "Strip Flag", "SOP Location", "Rule Text (verbatim)", "SOP Quote / Paraphrase",
        "Finding Narrative", "Remediation",
    ]
    for col, h in enumerate(headers, start=1):
        c = ws2.cell(row=4, column=col, value=h)
        c.font = header_font()
        c.fill = header_fill()
        c.alignment = cell_alignment(h="center", v="center")
        c.border = thin_border()

    # Sort findings: by rule section, then by ID
    def sort_key(f):
        # Extract numeric prefix from rule (e.g. ".1701" -> 1701, ".0209" -> 209)
        rule = f["rule"]
        if rule.startswith("."):
            try:
                return (int(rule[1:5]), rule)
            except ValueError:
                return (9999, rule)
        return (9999, rule)

    sorted_findings = sorted(FINDINGS, key=sort_key)

    for i, f in enumerate(sorted_findings, start=5):
        row_data = [
            f["id"],
            f["rule"],
            f["rule_title"],
            f["status"],
            f["severity"],
            f["strip_flag"],
            f["sop_loc"],
            f["rule_text"],
            f["sop_quote"],
            f["finding"],
            f["remediation"],
        ]
        for col, val in enumerate(row_data, start=1):
            c = ws2.cell(row=i, column=col, value=val)
            c.font = body_font()
            c.alignment = cell_alignment()
            c.border = thin_border()
        # Color the status and severity cells
        ws2.cell(row=i, column=4).font = body_font(bold=True, color=STATUS_FILL.get(f["status"], TEXT_PRIMARY))
        ws2.cell(row=i, column=5).font = body_font(bold=True, color=SEV_FILL.get(f["severity"], TEXT_PRIMARY))
        # Row background by severity (subtle)
        row_bg = SEV_ROW_BG.get(f["severity"], WHITE)
        # Only apply to finding ID + rule citation columns (1-2) to keep table readable
        for col in (1, 2):
            ws2.cell(row=i, column=col).fill = PatternFill(start_color=row_bg, end_color=row_bg, fill_type="solid")

    # Column widths
    widths = [10, 14, 40, 13, 10, 8, 32, 60, 50, 70, 60]
    for i, w in enumerate(widths, start=1):
        ws2.column_dimensions[get_column_letter(i)].width = w

    # Freeze top headers
    ws2.freeze_panes = "C5"

    # Enable autofilter
    last_row = 4 + len(sorted_findings)
    ws2.auto_filter.ref = f"A4:K{last_row}"

    # Row heights — let Excel auto-fit, but set a reasonable default
    for r in range(5, last_row + 1):
        ws2.row_dimensions[r].height = 90  # tall enough for wrapped narrative

    # ─── Sheet 3: Strip Recommendations ─────────────────────────────────
    ws3 = wb.create_sheet("Strip Recommendations")

    ws3["A1"] = "Legislation-Stripping Recommendations — v2.23 Public Edition"
    ws3["A1"].font = Font(name="Calibri", size=14, bold=True, color=TERRACOTTA)
    ws3.merge_cells("A1:F1")
    ws3["A2"] = "Each row identifies a statutory/regulatory citation in the current SOP Manual v2.22 Public Edition that should be stripped and replaced with plain-language operational text. The companion compliance master (Doc. WSI-SOP-001-LEG, Rev. 2.21) retains all citations for QA/audit reference."
    ws3["A2"].font = Font(name="Calibri", size=10, italic=True, color=TEXT_MUTED)
    ws3.merge_cells("A2:F2")
    ws3.row_dimensions[2].height = 32

    strip_headers = [
        "Finding ID", "Rule Citation", "SOP Location", "Strip Text (citation to remove)",
        "Replacement Text (plain-language operational)", "Status (TODO/Done)",
    ]
    for col, h in enumerate(strip_headers, start=1):
        c = ws3.cell(row=4, column=col, value=h)
        c.font = header_font()
        c.fill = header_fill()
        c.alignment = cell_alignment(h="center", v="center")
        c.border = thin_border()

    strip_findings = [f for f in sorted_findings if f["strip_flag"] == "Y"]
    for i, f in enumerate(strip_findings, start=5):
        # Parse the strip_note — split on the first ';' if it contains both strip and replace
        note = f["strip_note"]
        # Try to split on common patterns
        strip_text = note
        replace_text = ""
        # Case-insensitive split on "replace with"
        lower_note = note.lower()
        idx = lower_note.find("replace with")
        if idx >= 0:
            strip_text = note[:idx].strip()
            replace_text = note[idx + len("replace with"):].strip()

        row_data = [
            f["id"],
            f["rule"],
            f["sop_loc"],
            strip_text,
            replace_text,
            "TODO",
        ]
        for col, val in enumerate(row_data, start=1):
            c = ws3.cell(row=i, column=col, value=val)
            c.font = body_font()
            c.alignment = cell_alignment()
            c.border = thin_border()
        # Color the TODO cell
        ws3.cell(row=i, column=6).font = body_font(bold=True, color=TERRACOTTA)
        ws3.cell(row=i, column=6).alignment = cell_alignment(h="center", v="center")

    # Column widths
    strip_widths = [10, 14, 32, 50, 50, 14]
    for i, w in enumerate(strip_widths, start=1):
        ws3.column_dimensions[get_column_letter(i)].width = w

    ws3.freeze_panes = "C5"
    last_strip_row = 4 + len(strip_findings)
    ws3.auto_filter.ref = f"A4:F{last_strip_row}"
    for r in range(5, last_strip_row + 1):
        ws3.row_dimensions[r].height = 60

    # Add a data validation for the Status column (TODO/Done)
    from openpyxl.worksheet.datavalidation import DataValidation
    dv = DataValidation(type="list", formula1='"TODO,In Progress,Done,N/A"', allow_blank=True)
    dv.add(f"F5:F{last_strip_row}")
    ws3.add_data_validation(dv)

    # Conditional formatting: green fill for "Done"
    done_fill = PatternFill(start_color="D1FAE5", end_color="D1FAE5", fill_type="solid")
    ws3.conditional_formatting.add(
        f"F5:F{last_strip_row}",
        CellIsRule(operator="equal", formula=['"Done"'], fill=done_fill),
    )

    # ─── Sheet 4: Revision Roadmap ──────────────────────────────────────
    ws4 = wb.create_sheet("Revision Roadmap v2.23")

    ws4["A1"] = "v2.23 Revision Roadmap — Corrective Action Tracker"
    ws4["A1"].font = Font(name="Calibri", size=14, bold=True, color=TERRACOTTA)
    ws4.merge_cells("A1:H1")
    ws4["A2"] = "Tracker for the 19 recommended v2.23 corrective actions. Assign owners and target dates; update Status as work progresses."
    ws4["A2"].font = Font(name="Calibri", size=10, italic=True, color=TEXT_MUTED)
    ws4.merge_cells("A2:H2")

    rm_headers = [
        "#", "Corrective Action", "Closes Finding(s)", "Priority",
        "Owner", "Target Date", "Status", "Notes",
    ]
    for col, h in enumerate(rm_headers, start=1):
        c = ws4.cell(row=4, column=col, value=h)
        c.font = header_font()
        c.fill = header_fill()
        c.alignment = cell_alignment(h="center", v="center")
        c.border = thin_border()

    roadmap = [
        ("Add §4.6 Licensed Professional Face-to-Face Clinical Consultation", "F-001", "High"),
        ("Add §6.3(a) Psychotropic Medication Drug Regimen Review (6-month)", "F-002", "High"),
        ("Global find/replace 'CCP 8C' → 'CCP 8D-2' in all legacy reference lines", "F-003", "High"),
        ("Add §6.3(b) Medication Disposal Documentation", "F-013", "Medium"),
        ("Add §6.3(c) Medication Receipt Verification — tamper-resistant packaging & label contents", "F-012", "Medium"),
        ("Add §6.3(d) Medication Education for Clients on Psychotropic Meds", "F-014", "Medium"),
        ("Expand §6.3 Medication Storage — all 5 .0209(e)(1) requirements", "M-043", "Medium"),
        ("Add §2.2(a) AP Individualized Supervision Plan", "F-006, M-028", "Medium"),
        ("Add §2.2(b) Paraprofessional Individualized Supervision Plan", "F-007, M-029", "Medium"),
        ("Add §3.4(a) Emergency Transfer/Discharge — 5-business-day service planning meeting", "F-008", "Medium"),
        ("Add §3.6 18th-Birthday Continuation Policy", "F-009", "Medium"),
        ("Add §3.4(b) Advance Written Notification for Non-Emergency Discharge/Transfer", "M-025", "Medium"),
        ("Add §3.4(c) Pre-Discharge CFT Service Planning Meeting", "M-026", "Medium"),
        ("Update §2.2 Age-18, Literacy, Criminal-Conviction Disclosure", "M-033", "Medium"),
        ("Update §1.8 Governing Body Minutes Permanently Maintained", "M-032", "Medium"),
        ("Add §1.X Client Fee Assessment / Lab Test Authorization / Volunteer Services policies", "M-031", "Medium"),
        ("Update §1.4(b) QP 2-Year Direct Client Care Experience", "M-007", "Medium"),
        ("Update Protocol 19 & Form 5 — Quarterly Drills Per Shift", "M-038", "Medium"),
        ("Execute Legislation-Stripping per audit Section E (31 plain-language replacements)", "All strip-flag findings (28)", "Medium"),
    ]
    for i, (action, closes, priority) in enumerate(roadmap, start=5):
        ws4.cell(row=i, column=1, value=i - 4).font = body_font(bold=True)
        ws4.cell(row=i, column=2, value=action).font = body_font()
        ws4.cell(row=i, column=3, value=closes).font = body_font()
        ws4.cell(row=i, column=4, value=priority).font = body_font(bold=True,
            color=SEV_FILL.get(priority, TEXT_PRIMARY))
        ws4.cell(row=i, column=5, value="").font = body_font()  # Owner
        ws4.cell(row=i, column=6, value="").font = body_font()  # Target Date
        ws4.cell(row=i, column=7, value="TODO").font = body_font(bold=True, color=TERRACOTTA)
        ws4.cell(row=i, column=8, value="").font = body_font()  # Notes
        for col in range(1, 9):
            ws4.cell(row=i, column=col).border = thin_border()
            ws4.cell(row=i, column=col).alignment = cell_alignment(h="left" if col != 1 else "center")

    rm_widths = [5, 60, 22, 10, 18, 14, 12, 30]
    for i, w in enumerate(rm_widths, start=1):
        ws4.column_dimensions[get_column_letter(i)].width = w

    ws4.freeze_panes = "B5"
    last_rm_row = 4 + len(roadmap)
    ws4.auto_filter.ref = f"A4:H{last_rm_row}"
    for r in range(5, last_rm_row + 1):
        ws4.row_dimensions[r].height = 40

    # Data validation for Status column
    dv2 = DataValidation(type="list", formula1='"TODO,In Progress,Done,Deferred,N/A"', allow_blank=True)
    dv2.add(f"G5:G{last_rm_row}")
    ws4.add_data_validation(dv2)

    # Conditional formatting: green for Done, yellow for In Progress, red for Deferred
    done_fill2 = PatternFill(start_color="D1FAE5", end_color="D1FAE5", fill_type="solid")
    prog_fill = PatternFill(start_color="FEF3C7", end_color="FEF3C7", fill_type="solid")
    def_fill = PatternFill(start_color="FEE2E2", end_color="FEE2E2", fill_type="solid")
    ws4.conditional_formatting.add(
        f"G5:G{last_rm_row}",
        CellIsRule(operator="equal", formula=['"Done"'], fill=done_fill2),
    )
    ws4.conditional_formatting.add(
        f"G5:G{last_rm_row}",
        CellIsRule(operator="equal", formula=['"In Progress"'], fill=prog_fill),
    )
    ws4.conditional_formatting.add(
        f"G5:G{last_rm_row}",
        CellIsRule(operator="equal", formula=['"Deferred"'], fill=def_fill),
    )

    # ─── Save ────────────────────────────────────────────────────────────
    wb.save(output_path)
    print(f"XLSX crosswalk saved: {output_path}")
    print(f"  Sheets: {wb.sheetnames}")
    print(f"  Findings Crosswalk rows: {len(FINDINGS)}")
    print(f"  Strip Recommendations rows: {stats['by_strip']['Y']}")
    print(f"  Revision Roadmap rows: {len(roadmap)}")


if __name__ == "__main__":
    output = "/home/z/my-project/download/WSI_SOP_v2.22_Compliance_Audit_Crosswalk.xlsx"
    build_workbook(output)
    import os
    size_kb = os.path.getsize(output) / 1024
    print(f"File size: {size_kb:.1f} KB")
