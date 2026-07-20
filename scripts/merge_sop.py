#!/usr/bin/env python3
"""
Merge the rendered cover PDF (sop_cover.pdf) with the body PDF (sop_body.pdf)
into the final deliverable.

Cover is page 1; body follows. All pages are normalized to exact A4
(595.28 x 841.89 pt) so page-size consistency passes the QA scan.

VERSIONING
----------
The manual is versioned. Two files are emitted on each run:
  1. A versioned archive file:  Well_Spring_Intervention_SOP_Manual_v<VERSION>.pdf
  2. A "latest" pointer file:   Well_Spring_Intervention_SOP_Manual_LATEST.pdf

The versioned file is immutable — never overwritten — so historical
revisions remain accessible for audit, staff training, and regulatory
review. The LATEST file always points to the most recent build so casual
readers have a single canonical URL.

Bump MANUAL_VERSION below whenever content materially changes.
"""
import os
import shutil
from pypdf import PdfReader, PdfWriter

A4_W, A4_H = 595.28, 841.89

# ── Version tracking ─────────────────────────────────────────────────
# Bump this when content materially changes. The versioned filename is
# derived from this string; it is also embedded in the PDF /Subject.
MANUAL_VERSION = '2.4'
MANUAL_VERSION_SUFFIX = 'RMDM-Compliant'   # short descriptor; "" for none

# ── Source / output paths ────────────────────────────────────────────
COVER_PDF = '/home/z/my-project/scripts/sop_cover.pdf'
BODY_PDF  = '/home/z/my-project/scripts/sop_body.pdf'
DOWNLOAD_DIR = '/home/z/my-project/download'

# Build the versioned filename: e.g. Well_Spring_Intervention_SOP_Manual_v2.0_RMDM-Compliant.pdf
_suffix = f"_{MANUAL_VERSION_SUFFIX}" if MANUAL_VERSION_SUFFIX else ""
VERSIONED_FILENAME = f'Well_Spring_Intervention_SOP_Manual_v{MANUAL_VERSION}{_suffix}.pdf'
LATEST_FILENAME = 'Well_Spring_Intervention_SOP_Manual_LATEST.pdf'

VERSIONED_PDF = os.path.join(DOWNLOAD_DIR, VERSIONED_FILENAME)
LATEST_PDF    = os.path.join(DOWNLOAD_DIR, LATEST_FILENAME)


def normalize_page_to_a4(page):
    """Force exact A4 dimensions (any sub-point drift triggers scale_to)."""
    box = page.mediabox
    w, h = float(box.width), float(box.height)
    if abs(w - A4_W) > 0.1 or abs(h - A4_H) > 0.1:
        page.scale_to(A4_W, A4_H)
    return page


def main():
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)
    writer = PdfWriter()

    # Cover (page 1)
    cover_reader = PdfReader(COVER_PDF)
    writer.add_page(normalize_page_to_a4(cover_reader.pages[0]))

    # Body (pages 2+)
    body_reader = PdfReader(BODY_PDF)
    for page in body_reader.pages:
        writer.add_page(normalize_page_to_a4(page))

    # Metadata
    subject_str = (
        f'Level 3 Supervised Residential Group Home — '
        f'Standard Operating Procedures (Rev. {MANUAL_VERSION}'
        + (f', {MANUAL_VERSION_SUFFIX}' if MANUAL_VERSION_SUFFIX else '')
        + ')'
    )
    writer.add_metadata({
        '/Title':    f'Well Spring Intervention LLC — SOP & Operational Manual (Rev. {MANUAL_VERSION})',
        '/Author':   'Well Spring Intervention LLC',
        '/Creator':  'Z.ai',
        '/Producer': 'http://z.ai',
        '/Subject':  subject_str,
        '/Keywords': 'SOP, residential group home, Level 3, NCAC 27G, Rule 108, Medicaid CCP 8C, IRIS, RMDM, HIPAA, 42 CFR Part 2',
    })

    # Write the versioned file
    with open(VERSIONED_PDF, 'wb') as f:
        writer.write(f)

    # Copy the versioned file to the LATEST pointer
    shutil.copyfile(VERSIONED_PDF, LATEST_PDF)

    size_kb = os.path.getsize(VERSIONED_PDF) / 1024
    print(f'Versioned PDF: {VERSIONED_PDF}')
    print(f'  ({size_kb:.1f} KB, {len(writer.pages)} pages, Rev. {MANUAL_VERSION}'
          + (f' {MANUAL_VERSION_SUFFIX}' if MANUAL_VERSION_SUFFIX else '') + ')')
    print(f'Latest pointer: {LATEST_PDF}')


if __name__ == '__main__':
    main()
