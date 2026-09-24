"""
merge_sop60_audit.py — Merge SOP-60 audit cover + body into final deliverable.

Inputs:
  /home/z/my-project/scripts/sop60_audit_cover.pdf  (1 page, cover)
  /home/z/my-project/scripts/sop60_audit_body.pdf    (TOC + 8 content sections)

Output:
  /home/z/my-project/download/WSI_SOP_v2.24_Operational_Audit_Report.pdf
"""
import os
from pypdf import PdfWriter, PdfReader
from pypdf.generic import RectangleObject

COVER  = '/home/z/my-project/scripts/sop60_audit_cover.pdf'
BODY   = '/home/z/my-project/scripts/sop60_audit_body.pdf'
OUTPUT = '/home/z/my-project/download/WSI_SOP_v2.24_Operational_Audit_Report.pdf'

# A4 page dimensions in points (1pt = 1/72in, A4 = 595.28 x 841.89 pt)
A4_W = 595.28
A4_H = 841.89
TOLERANCE = 0.5

def normalize_a4(reader):
    """Force every page to exact A4 dimensions to avoid sub-pixel mismatch."""
    for page in reader.pages:
        box = RectangleObject((0, 0, A4_W, A4_H))
        page.mediabox = box
        page.cropbox = box
        page.bleedbox = box
        page.trimbox = box
        page.artbox = box
    return reader

def main():
    if not os.path.exists(COVER):
        print(f"ERROR: cover not found: {COVER}")
        return 1
    if not os.path.exists(BODY):
        print(f"ERROR: body not found: {BODY}")
        return 1

    writer = PdfWriter()

    # Cover
    cover_reader = PdfReader(COVER)
    cover_reader = normalize_a4(cover_reader)
    for p in cover_reader.pages:
        writer.add_page(p)

    # Body
    body_reader = PdfReader(BODY)
    body_reader = normalize_a4(body_reader)
    for p in body_reader.pages:
        writer.add_page(p)

    # Metadata
    writer.add_metadata({
        '/Title': 'Well Spring Intervention LLC — SOP v2.24 / CARF Plans v1.2 Operational Audit Report',
        '/Author': 'Z.ai',
        '/Creator': 'Z.ai',
        '/Subject': 'Operational audit of SOP Manual v2.24 + CARF Plans v1.2 — service code, staffing, capacity, Alliance Health Tailored Plan, WakeMed OON, policy completeness (Rev. 1.0)',
        '/Keywords': 'WSI, SOP, CARF, CYS 2026, Inaugural Accreditation, Operational Audit, 10A NCAC 27G .1700, Staffing Ratios, .1704, .1706(a), Alliance Health Tailored Plan, WakeMed OON',
    })

    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    with open(OUTPUT, 'wb') as fh:
        writer.write(fh)

    size_kb = os.path.getsize(OUTPUT) / 1024
    n_pages = len(cover_reader.pages) + len(body_reader.pages)
    print(f"  Final audit report PDF: {OUTPUT}")
    print(f"  Size: {size_kb:.1f} KB ({n_pages} pages)")
    return 0


if __name__ == '__main__':
    sys_exit = main()
    import sys
    sys.exit(sys_exit)
