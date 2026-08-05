#!/usr/bin/env python3
"""
merge_carf_plans.py — Merge CARF Plans cover + body into final PDF.
"""
import os
from pypdf import PdfWriter, PdfReader

COVER = '/home/z/my-project/scripts/carf_plans_cover.pdf'
BODY = '/home/z/my-project/scripts/carf_plans_body.pdf'
VERSIONED = '/home/z/my-project/download/WSI_CARF_CYS_2026_Conformance_Plans.pdf'

A4_W, A4_H = 595.28, 841.89  # exact A4 in points


def normalize_a4(page):
    """Force page to exact A4 size."""
    page.mediabox.lower_left = (0, 0)
    page.mediabox.upper_right = (A4_W, A4_H)
    page.cropbox.lower_left = (0, 0)
    page.cropbox.upper_right = (A4_W, A4_H)
    return page


def main():
    writer = PdfWriter()

    cover = PdfReader(COVER)
    for p in cover.pages:
        writer.add_page(normalize_a4(p))

    body = PdfReader(BODY)
    for p in body.pages:
        writer.add_page(normalize_a4(p))

    writer.add_metadata({
        '/Title':    'Well Spring Intervention LLC — CARF CYS 2026 Conformance Plans',
        '/Author':   'Well Spring Intervention LLC',
        '/Creator':  'Z.ai',
        '/Producer': 'http://z.ai',
        '/Subject':  'CARF CYS 2026 Inaugural Accreditation Conformance Plan Portfolio (Rev. 1.0)',
        '/Keywords': 'CARF, CYS, 2026, Inaugural Accreditation, Conformance Plans, Strategic Plan, '
                     'Stakeholder Input, Legal Compliance, Financial, ERM, Workforce, Accessibility, '
                     'Performance Measurement, Telehealth, Quality Records',
    })

    with open(VERSIONED, 'wb') as f:
        writer.write(f)

    size_kb = os.path.getsize(VERSIONED) / 1024
    print(f'Final PDF: {VERSIONED}')
    print(f'  ({size_kb:.1f} KB, {len(writer.pages)} pages, Rev. 1.0)')


if __name__ == '__main__':
    main()
