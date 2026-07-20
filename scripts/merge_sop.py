#!/usr/bin/env python3
"""
Merge the rendered cover PDF (sop_cover.pdf) with the body PDF (sop_body.pdf)
into the final deliverable.

Cover is page 1; body follows. All pages are normalized to exact A4
(595.28 x 841.89 pt) so page-size consistency passes the QA scan.
"""
import os
from pypdf import PdfReader, PdfWriter

A4_W, A4_H = 595.28, 841.89

COVER_PDF = '/home/z/my-project/scripts/sop_cover.pdf'
BODY_PDF  = '/home/z/my-project/scripts/sop_body.pdf'
OUTPUT_PDF = '/home/z/my-project/download/Well_Spring_Intervention_SOP_Manual.pdf'


def normalize_page_to_a4(page):
    """Force exact A4 dimensions (any sub-point drift triggers scale_to)."""
    box = page.mediabox
    w, h = float(box.width), float(box.height)
    if abs(w - A4_W) > 0.1 or abs(h - A4_H) > 0.1:
        page.scale_to(A4_W, A4_H)
    return page


def main():
    os.makedirs(os.path.dirname(OUTPUT_PDF), exist_ok=True)
    writer = PdfWriter()

    # Cover (page 1)
    cover_reader = PdfReader(COVER_PDF)
    writer.add_page(normalize_page_to_a4(cover_reader.pages[0]))

    # Body (pages 2+)
    body_reader = PdfReader(BODY_PDF)
    for page in body_reader.pages:
        writer.add_page(normalize_page_to_a4(page))

    # Metadata
    writer.add_metadata({
        '/Title':    'Well Spring Intervention LLC — SOP & Operational Manual',
        '/Author':   'Well Spring Intervention LLC',
        '/Creator':  'Z.ai',
        '/Producer': 'http://z.ai',
        '/Subject':  'Level 3 Supervised Residential Group Home — Standard Operating Procedures',
        '/Keywords': 'SOP, residential group home, Level 3, NCAC 27G, Rule 108, Medicaid CCP 8C, IRIS',
    })

    with open(OUTPUT_PDF, 'wb') as f:
        writer.write(f)

    size_kb = os.path.getsize(OUTPUT_PDF) / 1024
    print(f'Final PDF written: {OUTPUT_PDF}')
    print(f'Total pages: {len(writer.pages)}')
    print(f'File size: {size_kb:.1f} KB')


if __name__ == '__main__':
    main()
