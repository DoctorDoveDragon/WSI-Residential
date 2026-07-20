"""Merge cover PDF + body PDF into the final book PDF."""

from pypdf import PdfReader, PdfWriter

A4_W, A4_H = 595.28, 841.89  # A4 in points


def normalize_page_to_a4(page):
    """Force every page to exact A4 dimensions to avoid sub-point mismatches."""
    box = page.mediabox
    w, h = float(box.width), float(box.height)
    if abs(w - A4_W) > 0.1 or abs(h - A4_H) > 0.1:
        page.scale_to(A4_W, A4_H)
    return page


def main():
    cover_pdf = '/home/z/my-project/scripts/cover.pdf'
    body_pdf = '/home/z/my-project/scripts/body.pdf'
    output_pdf = '/home/z/my-project/download/The_Quiet_Edge.pdf'

    writer = PdfWriter()

    # Cover as page 1
    cover_page = PdfReader(cover_pdf).pages[0]
    writer.add_page(normalize_page_to_a4(cover_page))

    # Body pages
    for page in PdfReader(body_pdf).pages:
        writer.add_page(normalize_page_to_a4(page))

    writer.add_metadata({
        '/Title': 'The Quiet Edge',
        '/Author': 'Z.ai Press',
        '/Creator': 'Z.ai',
        '/Subject': 'How ordinary habits create extraordinary lives',
    })

    with open(output_pdf, 'wb') as f:
        writer.write(f)

    print(f'Final PDF: {output_pdf}')
    print(f'Total pages: {len(writer.pages)}')


if __name__ == '__main__':
    main()
