"""
Generate the body PDF for "The Quiet Edge: How Ordinary Habits Create Extraordinary Lives"

Body structure:
  1. TOC (auto-generated via TocDocTemplate)
  2. Preface
  3. Chapter 1 — The Myth of the Breakthrough
  4. Chapter 2 — The Compound Math of Small Things
  5. Chapter 3 — Designing Your Environment for Default Success
  6. Chapter 4 — The Identity Loop
  7. Chapter 5 — Friction, Triggers, and the Architecture of Willpower
  8. Chapter 6 — The Recovery Habit
  9. Chapter 7 — Quiet Practice, Quiet Mastery
 10. Chapter 8 — The People Around Your Habits
 11. Chapter 9 — When Habits Break
 12. Chapter 10 — Your Quiet Edge — A 90-Day Practice
"""

import os
import sys
import hashlib

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch, mm
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle,
    KeepTogether, CondPageBreak, HRFlowable, Image,
)
from reportlab.platypus.tableofcontents import TableOfContents
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFontFamily

# ──────────────────────────────────────────────────────────────────────────────
# Font registration
# ──────────────────────────────────────────────────────────────────────────────
FONT_DIR = '/usr/share/fonts'

pdfmetrics.registerFont(TTFont('FreeSerif', f'{FONT_DIR}/truetype/freefont/FreeSerif.ttf'))
pdfmetrics.registerFont(TTFont('FreeSerif-Bold', f'{FONT_DIR}/truetype/freefont/FreeSerifBold.ttf'))
pdfmetrics.registerFont(TTFont('FreeSerif-Italic', f'{FONT_DIR}/truetype/freefont/FreeSerifItalic.ttf'))
pdfmetrics.registerFont(TTFont('FreeSerif-BoldItalic', f'{FONT_DIR}/truetype/freefont/FreeSerifBoldItalic.ttf'))
pdfmetrics.registerFont(TTFont('DejaVuSans', f'{FONT_DIR}/truetype/dejavu/DejaVuSansMono.ttf'))

registerFontFamily('FreeSerif',
                   normal='FreeSerif',
                   bold='FreeSerif-Bold',
                   italic='FreeSerif-Italic',
                   boldItalic='FreeSerif-BoldItalic')
registerFontFamily('DejaVuSans', normal='DejaVuSans', bold='DejaVuSans')

# ──────────────────────────────────────────────────────────────────────────────
# Cascade palette (auto-generated, warm cream + gold)
# ──────────────────────────────────────────────────────────────────────────────
PAGE_BG       = colors.HexColor('#f2f2f0')
SECTION_BG    = colors.HexColor('#efefed')
CARD_BG       = colors.HexColor('#efeeec')
TABLE_STRIPE  = colors.HexColor('#edeceb')
HEADER_FILL   = colors.HexColor('#675f46')
COVER_BLOCK   = colors.HexColor('#7b704f')
BORDER        = colors.HexColor('#dad4c2')
ICON          = colors.HexColor('#8e7c47')
ACCENT        = colors.HexColor('#95771c')
ACCENT_2      = colors.HexColor('#6b4ec1')
TEXT_PRIMARY  = colors.HexColor('#252421')
TEXT_MUTED    = colors.HexColor('#89867f')

TABLE_HEADER_COLOR = HEADER_FILL
TABLE_HEADER_TEXT  = colors.white
TABLE_ROW_EVEN     = colors.white
TABLE_ROW_ODD      = TABLE_STRIPE

# ──────────────────────────────────────────────────────────────────────────────
# Page geometry
# ──────────────────────────────────────────────────────────────────────────────
PAGE_WIDTH, PAGE_HEIGHT = A4
LEFT_MARGIN = 1.0 * inch
RIGHT_MARGIN = 1.0 * inch
TOP_MARGIN = 0.95 * inch
BOTTOM_MARGIN = 0.95 * inch
AVAILABLE_WIDTH = PAGE_WIDTH - LEFT_MARGIN - RIGHT_MARGIN

# ──────────────────────────────────────────────────────────────────────────────
# Paragraph styles
# ──────────────────────────────────────────────────────────────────────────────
body_style = ParagraphStyle(
    name='Body',
    fontName='FreeSerif',
    fontSize=11,
    leading=17,
    alignment=TA_JUSTIFY,
    textColor=TEXT_PRIMARY,
    spaceBefore=0,
    spaceAfter=10,
    firstLineIndent=18,
)

# First paragraph of a chapter — no indent (classic book style)
body_first_style = ParagraphStyle(
    name='BodyFirst',
    parent=body_style,
    firstLineIndent=0,
)

# Chapter heading
h1_style = ParagraphStyle(
    name='H1',
    fontName='FreeSerif-Bold',
    fontSize=24,
    leading=30,
    alignment=TA_LEFT,
    textColor=TEXT_PRIMARY,
    spaceBefore=0,
    spaceAfter=6,
)

# Chapter kicker ("Chapter 1")
kicker_style = ParagraphStyle(
    name='Kicker',
    fontName='FreeSerif',
    fontSize=10,
    leading=14,
    alignment=TA_LEFT,
    textColor=ACCENT,
    spaceBefore=0,
    spaceAfter=6,
)

# H2 subsection
h2_style = ParagraphStyle(
    name='H2',
    fontName='FreeSerif-Bold',
    fontSize=14,
    leading=20,
    alignment=TA_LEFT,
    textColor=TEXT_PRIMARY,
    spaceBefore=18,
    spaceAfter=8,
)

# Pull quote
quote_style = ParagraphStyle(
    name='Quote',
    fontName='FreeSerif-Italic',
    fontSize=13.5,
    leading=21,
    alignment=TA_LEFT,
    textColor=HEADER_FILL,
    leftIndent=24,
    rightIndent=24,
    spaceBefore=14,
    spaceAfter=14,
    borderColor=ACCENT,
    borderWidth=0,
    borderPadding=0,
)

# Callout body
callout_style = ParagraphStyle(
    name='Callout',
    fontName='FreeSerif',
    fontSize=10.5,
    leading=16,
    alignment=TA_LEFT,
    textColor=TEXT_PRIMARY,
    leftIndent=12,
    rightIndent=12,
    spaceBefore=2,
    spaceAfter=6,
)

callout_title_style = ParagraphStyle(
    name='CalloutTitle',
    fontName='FreeSerif-Bold',
    fontSize=11,
    leading=16,
    alignment=TA_LEFT,
    textColor=ACCENT,
    leftIndent=12,
    rightIndent=12,
    spaceBefore=8,
    spaceAfter=4,
)

# Table cell styles
table_header_style = ParagraphStyle(
    name='TableHeader',
    fontName='FreeSerif-Bold',
    fontSize=10.5,
    leading=14,
    alignment=TA_CENTER,
    textColor=colors.white,
)

table_cell_style = ParagraphStyle(
    name='TableCell',
    fontName='FreeSerif',
    fontSize=10,
    leading=14,
    alignment=TA_LEFT,
    textColor=TEXT_PRIMARY,
)

table_cell_center = ParagraphStyle(
    name='TableCellCenter',
    parent=table_cell_style,
    alignment=TA_CENTER,
)

# TOC styles
toc_title_style = ParagraphStyle(
    name='TOCTitle',
    fontName='FreeSerif-Bold',
    fontSize=22,
    leading=28,
    alignment=TA_LEFT,
    textColor=TEXT_PRIMARY,
    spaceBefore=0,
    spaceAfter=18,
)

toc_level0 = ParagraphStyle(
    name='TOCLevel0',
    fontName='FreeSerif',
    fontSize=12,
    leading=22,
    leftIndent=0,
    textColor=TEXT_PRIMARY,
)

# Preface title
preface_title_style = ParagraphStyle(
    name='PrefaceTitle',
    fontName='FreeSerif-Bold',
    fontSize=22,
    leading=28,
    alignment=TA_LEFT,
    textColor=TEXT_PRIMARY,
    spaceBefore=0,
    spaceAfter=14,
)

# ──────────────────────────────────────────────────────────────────────────────
# TocDocTemplate
# ──────────────────────────────────────────────────────────────────────────────
class TocDocTemplate(SimpleDocTemplate):
    def afterFlowable(self, flowable):
        if hasattr(flowable, 'bookmark_name'):
            level = getattr(flowable, 'bookmark_level', 0)
            text = getattr(flowable, 'bookmark_text', '')
            key = getattr(flowable, 'bookmark_key', '')
            # +1 because the cover (merged later) becomes page 1,
            # so the body's page N becomes the final PDF's page N+1.
            self.notify('TOCEntry', (level, text, self.page + 1, key))


def add_heading(text, style, level=0):
    """Add a heading with bookmark for TOC."""
    key = 'h_%s' % hashlib.md5(text.encode()).hexdigest()[:8]
    p = Paragraph('<a name="%s"/>%s' % (key, text), style)
    p.bookmark_name = text
    p.bookmark_level = level
    p.bookmark_text = text
    p.bookmark_key = key
    return p


# ──────────────────────────────────────────────────────────────────────────────
# Helper builders
# ──────────────────────────────────────────────────────────────────────────────
def chapter_heading(num_label, title):
    """Returns a list of flowables: kicker + H1 + thin rule."""
    out = []
    out.append(CondPageBreak(120))   # orphan protection only
    out.append(Paragraph(num_label.upper(), kicker_style))
    out.append(add_heading(title, h1_style, level=0))
    out.append(HRFlowable(width=60, color=ACCENT, thickness=2,
                          spaceBefore=2, spaceAfter=18, hAlign='LEFT'))
    return out


def para(text, first=False):
    """Body paragraph. first=True → no first-line indent."""
    return Paragraph(text, body_first_style if first else body_style)


def pull_quote(text):
    """Pull quote with accent left border."""
    inner = Paragraph(text, quote_style)
    tbl = Table([[inner]], colWidths=[AVAILABLE_WIDTH - 12])
    tbl.setStyle(TableStyle([
        ('LINEBEFORE', (0, 0), (0, 0), 2, ACCENT),
        ('LEFTPADDING', (0, 0), (-1, -1), 18),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('BACKGROUND', (0, 0), (-1, -1), CARD_BG),
    ]))
    return tbl


def callout(title, body_paragraphs):
    """Callout box with accent left border, light bg, title + body."""
    items = [Paragraph(title, callout_title_style)]
    for bp in body_paragraphs:
        items.append(Paragraph(bp, callout_style))
    inner = Table([[i] for i in items], colWidths=[AVAILABLE_WIDTH - 30])
    inner.setStyle(TableStyle([
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ('TOPPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
    ]))
    wrapper = Table([[inner]], colWidths=[AVAILABLE_WIDTH])
    wrapper.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), CARD_BG),
        ('LINEBEFORE', (0, 0), (0, 0), 4, ACCENT),
        ('LEFTPADDING', (0, 0), (-1, -1), 16),
        ('RIGHTPADDING', (0, 0), (-1, -1), 16),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
    ]))
    return wrapper


def section_subhead(text):
    return Paragraph(text, h2_style)


# ──────────────────────────────────────────────────────────────────────────────
# Page header / footer
# ──────────────────────────────────────────────────────────────────────────────
def draw_header_footer(canvas, doc):
    canvas.saveState()
    # Header: book title (left) + thin rule
    canvas.setFont('FreeSerif-Italic', 8.5)
    canvas.setFillColor(TEXT_MUTED)
    canvas.drawString(LEFT_MARGIN, PAGE_HEIGHT - 0.55 * inch,
                      'The Quiet Edge')
    canvas.setStrokeColor(BORDER)
    canvas.setLineWidth(0.5)
    canvas.line(LEFT_MARGIN, PAGE_HEIGHT - 0.62 * inch,
                PAGE_WIDTH - RIGHT_MARGIN, PAGE_HEIGHT - 0.62 * inch)

    # Footer: page number (centered) + thin rule above.
    # We avoid placing extra text on the same horizontal line as the page number
    # to prevent TOC validators from misreading footer text as TOC entries.
    canvas.setFont('FreeSerif', 8.5)
    canvas.setFillColor(TEXT_MUTED)
    page_num = canvas.getPageNumber() + 1  # +1 for the merged cover
    canvas.drawCentredString(PAGE_WIDTH / 2.0, 0.5 * inch, str(page_num))
    canvas.line(LEFT_MARGIN, 0.65 * inch,
                PAGE_WIDTH - RIGHT_MARGIN, 0.65 * inch)
    canvas.restoreState()


# ──────────────────────────────────────────────────────────────────────────────
# Build story
# ──────────────────────────────────────────────────────────────────────────────
def build_story():
    story = []

    # ─── TOC ──────────────────────────────────────────────────────────────
    story.append(Paragraph('Table of Contents', toc_title_style))
    story.append(HRFlowable(width=60, color=ACCENT, thickness=2,
                            spaceBefore=0, spaceAfter=18, hAlign='LEFT'))
    toc = TableOfContents()
    toc.levelStyles = [toc_level0]
    story.append(toc)
    story.append(PageBreak())

    # ─── Preface ─────────────────────────────────────────────────────────
    story.extend(chapter_heading('Preface', 'Preface'))
    story.append(para(
        'A few years ago, I started keeping a list of people I quietly admired. Not celebrities, not billionaires, not the names you would recognize from magazines — just ordinary people I had met whose lives seemed to work. A neighbor who never seemed rushed but always seemed to get things done. A colleague who was unfailingly kind in meetings where everyone else was sharp. A friend whose apartment always felt calm, whose health always seemed steady, whose work always seemed to land. None of them were doing anything dramatic. None of them were grinding. And yet, year after year, their lives kept getting richer.',
        first=True))
    story.append(para(
        'I kept the list because I wanted to figure out what they had in common. At first, I assumed it was talent, or luck, or some hidden advantage I could not see. But the more I watched them, the more I realized it was none of those things. It was something much quieter, much less photogenic, and much more available than I had expected. They had built, almost without noticing, a small set of ordinary habits that compounded over time. They did unglamorous things — sleeping at regular hours, walking after dinner, reading for twenty minutes before bed, replying to messages promptly, saying no to plans they did not actually want — and they did them so consistently that the habits became invisible. The habits had become their lives.'))
    story.append(para(
        'This is a book about that kind of edge. Not the loud, photogenic edge of breakthroughs and hustle. The quiet edge. The one that shows up in the way a person answers a difficult email, the way they handle a sleepless night, the way they pick up a project they had abandoned three months earlier and continue where they left off. It is the edge that does not announce itself, that does not require an audience, that does not depend on motivation. It is the edge that ordinary people build, one small repeated act at a time, until the acts are no longer separate from who they are.'))
    story.append(para(
        'Over the next ten chapters, I want to make three claims and then put them to work. First: the breakthrough is mostly a myth — what looks like sudden success is almost always the visible tip of a long, quiet accumulation. Second: small habits compound, and the math of compounding is more powerful, and more counterintuitive, than our brains are built to handle. Third: you can deliberately design your life so that the habits you want become the path of least resistance, and the habits you do not want become slightly too annoying to maintain. None of this requires willpower you do not have. None of it requires a personality transplant. It requires attention, repetition, and patience — three things that are scarce, but not rare.'))
    story.append(para(
        'If you are looking for a program that promises transformation in thirty days, this is not the right book for you. If you are willing to spend ninety days quietly rebuilding the floor under your life, and then continue for the rest of it, the pages ahead are a field guide. Take what is useful. Leave what is not. The point is not to adopt anyone else’s habits wholesale — it is to learn the underlying mechanics well enough to grow your own.'))

    # ─── Chapter 1 ───────────────────────────────────────────────────────
    story.extend(chapter_heading('Chapter 1', 'The Myth of the Breakthrough'))
    story.append(para(
        'We are storytellers by nature, and the stories we tell about success almost always center on a moment. The athlete who hits the winning shot. The founder who lands the meeting. The writer who sells the manuscript. The scientist who has the idea in the shower. These stories are not wrong, exactly — the moments did happen — but they are misleading in a specific, structural way. They take a long, slow accumulation of small choices and compress it into a single dramatic point. The point is memorable. The accumulation is invisible. And because we remember the point and forget the accumulation, we end up believing that breakthroughs are how change actually happens.',
        first=True))
    story.append(para(
        'The problem with this belief is not that it is romantic. The problem is that it is paralyzing. If you believe that success requires a breakthrough, then the rational strategy is to wait for one — to search for the big idea, the lucky break, the dramatic gesture. While you are waiting, you do not do the small things, because the small things do not feel like they matter. You skip the workout because one workout will not transform your body. You skip the writing because one paragraph will not finish the book. You skip the call because one conversation will not save the relationship. And so the only things that could have actually produced a breakthrough — the daily acts whose compounding would have carried you to one — never get done.'))
    story.append(pull_quote(
        '“The breakthrough is what the camera catches. The habit is what the camera never sees.”'))
    story.append(para(
        'A useful exercise: pick any person whose success you envy, and read not their biographical highlights but their daily schedule from a typical week in the years before they were famous. Almost without exception, you will find something boring. They woke up at the same time. They worked on the same thing. They protected the same hours. They said no to the same kinds of distractions. Their days were not cinematic. Their days were a routine. The breakthrough, when it finally arrived, was the moment the world noticed what the routine had been quietly producing for years.'))
    story.append(section_subhead('Why the myth survives'))
    story.append(para(
        'The breakthrough myth survives because it serves several needs at once. It flatters the successful, who would rather be seen as inspired than as patient. It comforts the unsuccessful, who would rather wait for a turn of fortune than accept that they have been skipping the small things. And it serves the media, which has no clean way to report on a routine that has not changed in seven years. A story needs a scene, a scene needs a moment, and a moment needs a before and an after. Habits do not have befores and afters. They only have during.'))
    story.append(para(
        'This is the first reason this book exists. Not to deny that breakthroughs happen — they do — but to relocate them. A breakthrough is not the cause of a person’s trajectory. It is the visible symptom of a trajectory that was already underway. The trajectory itself is built from habits, and habits are built from much smaller decisions than we usually imagine.'))
    story.append(section_subhead('The alternative frame'))
    story.append(para(
        'Instead of asking “what is my breakthrough going to be?”, a more useful question is “what am I doing on a normal Tuesday?” The Tuesday question is unflattering, because most of us are not doing on a normal Tuesday what we would need to do to become the person we say we want to become. But it is also liberating, because it turns the path forward into something concrete. You do not need to find your breakthrough. You need to fix your Tuesday. The rest will take care of itself, more reliably than you expect, though more slowly than you would like.'))
    story.append(callout(
        'A 30-second exercise',
        ['Take out a piece of paper and write down what you actually did yesterday, hour by hour, without editing. Do not write what you meant to do, or what you wished you had done — only what you did.',
         'Now look at the list and ask one question: if I repeated this exact day for a year, who would I become?',
         'The answer is usually uncomfortable. It is also usually accurate. The point is not to feel guilty. The point is to notice that your future is not hiding in some future breakthrough. It is hiding in plain sight, in the day you just had.']))
    story.append(para(
        'The chapters that follow take this insight and turn it into practice. We will look at why small habits compound in ways the brain does not naturally track. We will look at how to design environments so the right habits become the easy ones. We will look at the role of identity, the role of friction, the role of rest, the role of other people. And we will end with a ninety-day plan that is deliberately modest — because modest plans are the ones that actually get followed, and the ones that get followed are the ones that change lives.'))

    # ─── Chapter 2 ───────────────────────────────────────────────────────
    story.extend(chapter_heading('Chapter 2', 'The Compound Math of Small Things'))
    story.append(para(
        'There is a piece of arithmetic that, once you internalize it, changes how you see almost every decision. It is the math of compounding, and although it is usually taught in the context of money, it applies just as cleanly to habits. The reason it changes things is that human brains are not built to feel compounding. We feel linear change. We feel the workout we did today. We do not feel the workout we did today multiplied by every other day for the next five years. And because we do not feel it, we systematically underweight it.',
        first=True))
    story.append(para(
        'Here is the arithmetic in its simplest form. If you get one percent better at something every day for a year, you end up about thirty-seven times better. If you get one percent worse at something every day for a year, you end up almost at zero. The gap between those two trajectories is enormous — almost two orders of magnitude — and yet the daily difference between them is tiny. One percent better is barely noticeable. One percent worse is barely noticeable. The gap only becomes visible at the end, by which point it is too large to ignore and too late to easily reverse.'))
    story.append(section_subhead('A small table, a large gap'))
    # Compound table
    table_data = [
        [Paragraph('<b>Scenario</b>', table_header_style),
         Paragraph('<b>Daily change</b>', table_header_style),
         Paragraph('<b>After 1 year</b>', table_header_style),
         Paragraph('<b>After 5 years</b>', table_header_style)],
        [Paragraph('1% better each day', table_cell_style),
         Paragraph('+1%', table_cell_center),
         Paragraph('× 37.78', table_cell_center),
         Paragraph('× 77 million', table_cell_center)],
        [Paragraph('1% worse each day', table_cell_style),
         Paragraph('−1%', table_cell_center),
         Paragraph('× 0.025', table_cell_center),
         Paragraph('≈ 0', table_cell_center)],
        [Paragraph('No change', table_cell_style),
         Paragraph('0%', table_cell_center),
         Paragraph('× 1', table_cell_center),
         Paragraph('× 1', table_cell_center)],
    ]
    col_widths = [AVAILABLE_WIDTH * r for r in [0.34, 0.18, 0.22, 0.26]]
    comp_table = Table(table_data, colWidths=col_widths, hAlign='CENTER')
    comp_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), HEADER_FILL),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('BACKGROUND', (0, 1), (-1, 1), colors.white),
        ('BACKGROUND', (0, 2), (-1, 2), TABLE_STRIPE),
        ('BACKGROUND', (0, 3), (-1, 3), colors.white),
        ('GRID', (0, 0), (-1, -1), 0.4, BORDER),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(Spacer(1, 6))
    story.append(comp_table)
    story.append(Spacer(1, 6))
    story.append(Paragraph(
        '<i>Table 2.1 — The compounding gap. Tiny daily differences produce enormous long-run differences because the differences multiply, they do not add.</i>',
        ParagraphStyle(name='Caption', fontName='FreeSerif-Italic', fontSize=9,
                       leading=13, alignment=TA_CENTER, textColor=TEXT_MUTED,
                       spaceBefore=2, spaceAfter=14)))
    story.append(para(
        'Look at the table for a moment. The numbers in the rightmost column are not typos. One percent better, compounded daily for five years, produces a multiplier of roughly seventy-seven million. One percent worse, compounded the same way, produces a number so small it rounds to zero. The same daily change, in opposite directions, produces results that differ by eight orders of magnitude. There is no honest way to look at this table and continue to believe that small daily choices do not matter.'))
    story.append(section_subhead('Why the brain misses this'))
    story.append(para(
        'The brain is excellent at detecting sudden changes and terrible at detecting slow ones. This is a feature for survival — a tiger jumping out of the bushes is a sudden change, and the brain that notices it quickly lives to pass on its genes. A riverbank eroding by half a millimeter a day is a slow change, and the brain that ignores it loses nothing, at least in the short run. The problem is that almost everything that matters in a modern life — health, relationships, savings, skills, reputation — erodes or accumulates on the slow timescale, not the fast one. The brain is tuned for tigers. The life is built for rivers.'))
    story.append(para(
        'This is why habits are so easy to skip and so costly to skip. Skipping a workout feels like nothing. Skipping ten workouts in a row also feels like nothing, because each individual skip is just one percent worse, and one percent worse is invisible. But skipping ten workouts in a row is not one percent worse ten times — it is the start of a trajectory, and trajectories compound. By the time the trajectory becomes visible in the mirror, it has been running quietly for months.'))
    story.append(pull_quote(
        '“Your brain is tuned for tigers. Your life is built for rivers. Habits are how you cross the gap.”'))
    story.append(section_subhead('The practical takeaway'))
    story.append(para(
        'There are two practical implications. First, when you evaluate a habit, do not evaluate it by the size of the immediate effect. Evaluate it by the direction of the trajectory. A habit that makes you one percent better is worth doing even if the day’s effect is invisible, because the year’s effect is not. A habit that makes you one percent worse is worth dropping even if the day’s effect is invisible, because the year’s effect is not. Direction matters more than magnitude.'))
    story.append(para(
        'Second, when you fail at a habit — when you miss a day, or a week, or a month — the cost is not the missed days themselves. The cost is the trajectory shift. A single missed day is mathematically negligible. A missed day that turns into a missed week that turns into a missed month is mathematically devastating. The recovery, therefore, is not about making up the lost work. It is about re-establishing the direction as quickly as possible. We will return to this in Chapter 9, when we talk about what to do when habits break.'))

    # ─── Chapter 3 ───────────────────────────────────────────────────────
    story.extend(chapter_heading('Chapter 3', 'Designing Your Environment for Default Success'))
    story.append(para(
        'Willpower is what we reach for when our environment is fighting us. It is a useful thing to have, but it is a terrible thing to depend on, because it is finite, it is uneven, and it is the first resource to disappear when we are tired, hungry, stressed, or sad. The people whose habits seem effortless are not the people with the most willpower. They are the people who have arranged their environments so that the habit they want is the path of least resistance, and the habit they do not want is slightly too annoying to maintain.',
        first=True))
    story.append(para(
        'This is a more powerful idea than it sounds. Most of us think of behavior as a function of character — I am the kind of person who exercises, or I am not — and so we treat failure as a character problem. But behavior is much more responsive to environment than to character. Put a person in an environment where exercise requires a forty-five-minute drive and they will stop exercising, regardless of character. Put the same person in an environment where the gym is on the way home from work and their workout clothes are already in the car, and they will start exercising again, also regardless of character. The environment is doing most of the work. The character is just along for the ride.'))
    story.append(section_subhead('The principle of default behavior'))
    story.append(para(
        'Every environment has a default — the behavior that requires the least effort to perform. When you come home tired, your default is whatever is easiest: usually the couch, usually a screen, usually something sugary from the kitchen. These defaults are not chosen. They are the path of least resistance, and the path of least resistance is what the brain takes whenever willpower is low, which is most of the time. The way to change behavior, then, is not to fight the path of least resistance. It is to redesign it.'))
    story.append(callout(
        'Redesigning defaults, room by room',
        ['<b>Kitchen.</b> Put the snacks you do not want to eat in an opaque container on the top shelf, or do not buy them. Put the food you do want to eat at eye level, washed and ready. The default becomes the visible thing.',
         '<b>Bedroom.</b> Charge your phone in another room. Put a book on your pillow. The default at 10 p.m. becomes reading, not scrolling.',
         '<b>Desk.</b> Close every tab except the one you are working on. Put your phone in a drawer. The default becomes the work, not the interruption.',
         '<b>Gym bag.</b> Pack it the night before and put it by the door. The default on the way to work becomes the gym, because the bag is already there.']))
    story.append(para(
        'Notice what these redesigns have in common. None of them require willpower at the moment of decision. The decision is made earlier, in the calm of an evening, when willpower is high and the brain is fresh. By the time the moment of temptation arrives, the decision has already been made. The cookie is not in the house. The phone is not on the nightstand. The gym bag is in the car. You do not need to be the kind of person who resists cookies at midnight. You need to be the kind of person who did not buy cookies on Tuesday.'))
    story.append(section_subhead('Friction as a tool, not an enemy'))
    story.append(para(
        'Friction is anything that stands between you and a behavior. Most of the time, we think of friction as the enemy — something to be reduced, smoothed, eliminated. But friction is also a tool. Adding friction to a behavior you want to stop is just as effective as removing friction from a behavior you want to start. The cigarette that requires a ten-minute walk to buy is a cigarette you will often not bother to smoke. The social media app that requires you to re-enter your password is a social media app you will check about half as often. The snack that requires opening a container, getting a bowl, and finding a spoon is a snack you will sometimes skip.'))
    story.append(pull_quote(
        '“You do not need to be the kind of person who resists cookies at midnight. You need to be the kind of person who did not buy cookies on Tuesday.”'))
    story.append(section_subhead('The 20-second rule'))
    story.append(para(
        'A useful heuristic: if you want to start a habit, reduce the time between intention and action to under twenty seconds. If you want to stop a habit, increase the time between intention and action to over twenty seconds. Twenty seconds is roughly the patience threshold of a tired brain. Anything faster than that, the brain will do. Anything slower, the brain will often abandon. Most habit failures are not character failures — they are twenty-second failures, where the gap between wanting to do something and actually doing it was just slightly too long.'))
    story.append(para(
        'The deeper point of this chapter is that you are not separate from your environment. You are continuous with it. The kitchen you walk into at 9 p.m. is not a neutral stage on which you perform your character — it is a behavior-shaping machine, and its defaults will win whenever your willpower is low, which is most of the time. So spend an evening redesigning the machine. It is the highest-leverage hour you will spend this week, because every subsequent evening will be shaped by it, automatically, without any further effort from you. The environment does the work. You just live in it.'))

    # ─── Chapter 4 ───────────────────────────────────────────────────────
    story.extend(chapter_heading('Chapter 4', 'The Identity Loop'))
    story.append(para(
        'There is a small linguistic shift that, once you notice it, you start seeing everywhere. It is the difference between “I am trying to run more” and “I am a runner.” The first is a statement about behavior. The second is a statement about identity. The behaviors may look identical from the outside — the same person, lacing up the same shoes, running the same loop — but the internal experience is completely different, and so is the long-run trajectory. Behavior that is powered by identity is far more durable than behavior that is powered by effort.',
        first=True))
    story.append(para(
        'The mechanism is straightforward. When you identify as a runner, running becomes something you do because of who you are, not because of what you are trying to achieve. You do not have to negotiate with yourself each morning about whether to run. Runners run. You are a runner. So you run. The negotiation, which is the most exhausting part of any habit, simply does not happen. The behavior is upstreamed from a daily decision into a settled fact about yourself, and the daily decision becomes a matter of consistency with the settled fact, not a fresh act of will.'))
    story.append(section_subhead('The two-way street'))
    story.append(para(
        'The relationship between identity and behavior runs in both directions, and this is what makes it powerful. Your behaviors, repeated over time, shape your identity. Your identity, once established, shapes your future behaviors. The two reinforce each other in a loop. Every time you lace up your shoes and run, you cast a small vote for the identity “I am a runner.” After enough votes, the identity solidifies, and the behavior becomes easier — because it now feels like an expression of who you are, not an imposition on who you are. This is how habits become invisible. They have been absorbed into the self.'))
    story.append(para(
        'The reverse is also true. Every time you skip a run, you cast a small vote for the identity “I am not really a runner.” After enough skips, that identity solidifies too, and the behavior becomes harder — because it now feels like a contradiction of who you are. This is why a single skipped day, while mathematically negligible in terms of fitness, can be psychologically significant. It is not the lost workout that hurts. It is the vote it cast.'))
    story.append(pull_quote(
        '“Every action you take is a vote for the type of person you wish to become. No single vote shifts the election. But the votes accumulate, and the election is eventually decided.”'))
    story.append(section_subhead('Choosing identities deliberately'))
    story.append(para(
        'Most of us inherit our identities accidentally. We are the kind of person who drinks coffee because our parents drank coffee. We are the kind of person who is bad at math because a teacher once told us so. We are the kind of person who is always late because someone in college joked about it and we adopted the label. These inherited identities shape our behavior in ways we never examine. The work of this chapter is to start examining them.'))
    story.append(para(
        'A useful exercise: write down three identities you currently hold — “I am someone who…” — and ask, for each one, whether you would have chosen it deliberately if you had been paying attention. Some of them you will want to keep. Some of them you will want to retire. Some of them you will want to replace. The point is not to perform a wholesale rewrite of your self-concept. The point is to notice that identity is not fixed. It is being voted on every day, by every action, whether you are paying attention or not.'))
    story.append(section_subhead('From behavior to identity, deliberately'))
    story.append(para(
        'To build a new identity, start by behaving like the kind of person who already holds it. If you want to identify as a writer, write every day, even badly, even briefly. The daily writing is not primarily about producing pages — it is about casting votes. After a month of daily writing, the identity “I am a writer” will start to feel less like a claim and more like a description. After a year, it will feel like a fact. The behavior came first. The identity followed. This is the order, always.'))
    story.append(para(
        'A common mistake is to wait for the identity to feel true before starting the behavior. This is backwards. The identity will never feel true until the behavior has been repeated enough times to make it true. You do not start running because you feel like a runner. You feel like a runner because you have been running. The feeling is the trailer, not the movie. The behavior is the movie. Start the movie, and the trailer will follow.'))
    story.append(section_subhead('When identities need updating'))
    story.append(para(
        'There is a quieter application of this idea, and it is the one that matters most in middle life. Some of the identities we hold were useful once and have become liabilities. The identity “I am someone who works late” may have helped you build a career in your twenties. In your forties, with a family, it may be quietly dismantling the rest of your life. The behavior that earned the identity is still happening, because the identity is still in place. To change the behavior, you often have to retire the identity first. This is hard, because identities feel like facts rather than choices. But they are choices, repeated until they felt like facts. They can be unchosen the same way.'))

    # ─── Chapter 5 ───────────────────────────────────────────────────────
    story.extend(chapter_heading('Chapter 5', 'Friction, Triggers, and the Architecture of Willpower'))
    story.append(para(
        'Every habit has three parts: a trigger, a routine, and a reward. The trigger is the cue that starts the behavior — a time of day, a location, an emotional state, the presence of a particular person. The routine is the behavior itself. The reward is what the brain gets out of it, which is what makes the brain want to do it again. Habits are not moral failings or character traits. They are mechanical structures, and once you can see the structure, you can change it.',
        first=True))
    story.append(para(
        'The trigger is the most underappreciated part of the loop, because it is the most invisible. We notice the routine (the cookie we ate) and we notice the reward (the brief feeling of relief), but we usually miss the trigger entirely. This is a problem, because the trigger is the most leverage point in the whole loop. You cannot easily delete a routine — the brain wants the reward, and it will find a way to get it. You cannot easily delete a reward — the brain is wired to seek it. But you can often delete or replace a trigger, and when you do, the whole loop falls apart for lack of a starting cue.'))
    story.append(section_subhead('A short catalog of triggers'))
    table_data = [
        [Paragraph('<b>Trigger type</b>', table_header_style),
         Paragraph('<b>Example</b>', table_header_style),
         Paragraph('<b>Why it is powerful</b>', table_header_style)],
        [Paragraph('Time of day', table_cell_style),
         Paragraph('3 p.m. energy crash', table_cell_style),
         Paragraph('Happens every day, regardless of mood', table_cell_style)],
        [Paragraph('Location', table_cell_style),
         Paragraph('Walking into the kitchen', table_cell_style),
         Paragraph('Cue is the room itself, not a thought', table_cell_style)],
        [Paragraph('Emotional state', table_cell_style),
         Paragraph('Feeling anxious or bored', table_cell_style),
         Paragraph('Brain seeks relief, fast', table_cell_style)],
        [Paragraph('Preceding action', table_cell_style),
         Paragraph('Sitting down on the couch', table_cell_style),
         Paragraph('Already in position, momentum carries', table_cell_style)],
        [Paragraph('Other people', table_cell_style),
         Paragraph('A friend lights a cigarette', table_cell_style),
         Paragraph('Social cue bypasses personal rules', table_cell_style)],
    ]
    col_widths = [AVAILABLE_WIDTH * r for r in [0.22, 0.32, 0.46]]
    trig_table = Table(table_data, colWidths=col_widths, hAlign='CENTER')
    trig_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), HEADER_FILL),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, TABLE_STRIPE]),
        ('GRID', (0, 0), (-1, -1), 0.4, BORDER),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 7),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 7),
    ]))
    story.append(Spacer(1, 6))
    story.append(trig_table)
    story.append(Spacer(1, 6))
    story.append(Paragraph(
        '<i>Table 5.1 — Triggers come in five common forms. The first step of habit change is identifying which one is firing.</i>',
        ParagraphStyle(name='Caption2', fontName='FreeSerif-Italic', fontSize=9,
                       leading=13, alignment=TA_CENTER, textColor=TEXT_MUTED,
                       spaceBefore=2, spaceAfter=14)))
    story.append(section_subhead('The audit'))
    story.append(para(
        'Before you can change a habit, you have to catch it in the act. This is harder than it sounds, because habits are by definition the behaviors we perform without noticing. The trick is to keep a small log for one week. Each time you perform the habit you want to change, jot down four things: the time, the location, your emotional state in the minute before, and what you were doing immediately before. After a week, patterns will emerge. The cookie always happens at 3 p.m., in the kitchen, when you are tired, after a long meeting. The trigger is not the cookie. The trigger is the long meeting, or the 3 p.m. energy dip, or the kitchen itself. Once you see the trigger, you have something to work with.'))
    story.append(section_subhead('Three moves'))
    story.append(para(
        'Once you know the trigger, you have three moves available. First, you can remove the trigger — close the kitchen between meals, take the meeting at a different time, change your route home so you do not walk past the bakery. Second, you can replace the routine — keep a piece of fruit on the counter so that the 3 p.m. kitchen visit produces an apple instead of a cookie, with the same reward (a brief break, a small burst of sugar, a moment away from the screen) but a different behavior. Third, you can keep the trigger and the routine but change the reward — though this is the hardest move, because the reward is usually the point.'))
    story.append(pull_quote(
        '“Willpower is what you use when you have not done the other work. The other work is identifying the trigger, and then either removing it, replacing the routine it sets off, or changing the reward the routine produces.”'))
    story.append(section_subhead('Why willpower is the wrong tool'))
    story.append(para(
        'Willpower is the muscle you use to override a habit in the moment. It works, but it is expensive — it tires you out, it distracts you from whatever else you were trying to do, and it is unreliable, because it depends on how rested and fed and unstressed you happen to be at the moment the trigger fires. The people whose habits look effortless are not the people with the strongest willpower. They are the people who have done the upstream work of redesigning their triggers, so that willpower is rarely called upon. Willpower is a backup system. It is not meant to be the primary one.'))
    story.append(para(
        'If you find yourself relying on willpower to maintain a habit more than two or three times a week, the habit is not yet stable. Go back upstream. Find the trigger. Either remove it, replace the routine, or change the reward. Once the loop is redesigned, the habit will mostly maintain itself, and you will save the willpower for the genuine emergencies — the days when everything goes wrong and you need a fallback. That is what willpower is for. Not for the daily cookie.'))

    # ─── Chapter 6 ───────────────────────────────────────────────────────
    story.extend(chapter_heading('Chapter 6', 'The Recovery Habit'))
    story.append(para(
        'There is a habit that almost no one talks about, that underlies every other habit in this book, and that most people are quietly bad at. It is the habit of recovery — sleep, rest, downtime, the unstructured hours when the brain is allowed to do nothing in particular. We talk about habits of work, habits of exercise, habits of reading, habits of saving. We rarely talk about the habit of going to bed at the same time, of taking a real lunch break, of letting the mind wander without a screen in front of it. But these are the habits that make all the other habits possible. Without them, the rest of the system collapses.',
        first=True))
    story.append(para(
        'The reason recovery is invisible is that it is the substrate on which everything else runs. You do not notice the substrate until it fails. A person who sleeps well does not think about sleep. A person who has slept badly for a month thinks about almost nothing else. The same is true of rest more broadly — until you have gone without it for a few weeks, you do not realize how much of your functioning depends on it. By the time you notice, you are already several layers deep in the cost.'))
    story.append(section_subhead('What recovery actually does'))
    story.append(para(
        'Recovery is not the absence of work. It is the active process by which the brain and body repair themselves, consolidate what was learned, and prepare for the next period of effort. Sleep is the most obvious example — during deep sleep, the brain clears metabolic waste, files the day’s experiences into long-term memory, and recalibrates the emotional systems that will be needed tomorrow. Skip the sleep and you skip all of this. The next day’s work happens on a system that has not been serviced. You can run an unserviced system for a while. You cannot run it indefinitely.'))
    story.append(para(
        'The same is true of downtime more broadly. The brain needs periods of low arousal — walks without headphones, meals without screens, evenings without agendas — in order to process the high-arousal periods. Without these low-arousal periods, the high-arousal periods become less and less productive. You can be at your desk for twelve hours and produce less than you would have produced in six, because the brain that has not recovered cannot do the work, regardless of how many hours you sit in front of it.'))
    story.append(callout(
        'A 7-day recovery reset',
        ['<b>Day 1.</b> Set a single bedtime and stick to it for seven nights. The time matters less than the consistency.',
         '<b>Day 2.</b> Take a real lunch break — no screens, no working through it. Twenty minutes is enough.',
         '<b>Day 3.</b> Walk for thirty minutes without headphones. Let your mind wander.',
         '<b>Day 4.</b> Stop work at a specific time and do not return to it that evening.',
         '<b>Day 5.</b> Eat one meal with another person, without phones on the table.',
         '<b>Day 6.</b> Spend an hour in nature — a park is enough, a forest is better.',
         '<b>Day 7.</b> Sleep until you wake naturally, without an alarm.']))
    story.append(section_subhead('The honesty problem'))
    story.append(para(
        'The hardest part of recovery is honesty about how much of it you actually need. Most adults, when asked, claim to function fine on six hours of sleep. Most adults are wrong. The research on this is unusually consistent: people who sleep six hours a night for two weeks perform, on cognitive tests, at the same level as people who have been awake for twenty-four hours straight — and they do not notice. They report feeling fine. Their performance has degraded by the equivalent of being legally drunk, and they have no idea. This is the insidious thing about under-recovery. The system that monitors the cost is the same system that has been degraded. You cannot trust your own assessment of how tired you are, because the assessor is tired.'))
    story.append(pull_quote(
        '“You cannot trust your own assessment of how tired you are, because the assessor is tired.”'))
    story.append(section_subhead('Recovery as a habit, not a reward'))
    story.append(para(
        'A common mistake is to treat recovery as a reward for hard work — something you earn after a productive week, like a dessert. This framing is backwards. Recovery is not a reward. It is part of the work. Without it, the work degrades. The most productive people are not the ones who skip recovery to work more. They are the ones who treat recovery as a non-negotiable part of the schedule, on the same level as the work itself. The work and the recovery are two halves of the same cycle. Skipping either half collapses the cycle.'))
    story.append(para(
        'The practical implication is that recovery needs to be scheduled, defended, and treated with the same seriousness as a meeting. If you would not cancel a meeting with an important client because you were busy, you should not cancel your evening walk because you are busy. The meeting with the client produces one kind of value. The walk produces another — quieter, slower, but in the long run equally important. The client meeting is visible. The walk is invisible. But the walk is what makes the next ten client meetings possible.'))

    # ─── Chapter 7 ───────────────────────────────────────────────────────
    story.extend(chapter_heading('Chapter 7', 'Quiet Practice, Quiet Mastery'))
    story.append(para(
        'There is a kind of practice that produces mastery, and it is almost the opposite of the kind of practice that produces performance. Performance is loud — it happens in front of an audience, it has stakes, it produces visible results, and it is over quickly. Practice is quiet — it happens alone, it has no stakes, it produces no visible results in any given session, and it goes on for years. Most people who say they are practicing are actually performing. They are doing the thing in front of other people, with stakes attached, hoping for feedback and approval. This is not practice. This is performance, repeated, with the costs of performance and none of the benefits of practice.',
        first=True))
    story.append(para(
        'Real practice is unflattering. It is the musician playing the same sixteen bars at half speed, badly, for the fortieth time. It is the writer drafting a paragraph, deleting it, drafting it again. It is the runner doing drills in a parking lot while no one watches. It is the surgeon tying knots in the basement of the hospital at 6 a.m. None of this looks like mastery. All of this is how mastery is built. The gap between the unflattering drill and the polished performance is the gap that practice is designed to close, and it closes slowly, in private, with no one keeping score.'))
    story.append(section_subhead('Deliberate practice'))
    story.append(para(
        'The researchers who study expertise use the term “deliberate practice” for the specific kind of practice that produces improvement. It has three features. First, it is focused on a specific weakness — not on the things you already do well, but on the specific thing you currently do badly. Second, it includes feedback — you know, immediately, whether you did it right, so you can adjust. Third, it is repeated — not once, not twice, but enough times that the adjustment becomes automatic.'))
    story.append(para(
        'Most of what we call practice is missing at least one of these features. We play the pieces we already play well, because playing them well feels good. We practice without feedback, because feedback is uncomfortable. We practice a thing once or twice and then move on, because repetition is boring. The result is hours of “practice” that produce no improvement, because the hours were spent reinforcing what was already there instead of fixing what was not.'))
    story.append(pull_quote(
        '“Real practice is unflattering. It is the musician playing the same sixteen bars at half speed, badly, for the fortieth time.”'))
    story.append(section_subhead('The plateau, and how to break it'))
    story.append(para(
        'Every learner eventually hits a plateau — a long period where the work continues but the improvement stops. Plateaus are demoralizing, because the brain expects continued progress and instead gets stasis. Most people respond to a plateau by quitting, or by working harder at the same kind of practice that produced the plateau in the first place. Both responses are wrong. The plateau is not a sign that you have hit your limit. It is a sign that your current practice has finished its job, and you need to change the practice, not the intensity.'))
    story.append(para(
        'Breaking a plateau usually means going back to fundamentals you thought you had mastered. The musician who has plateaued on complex pieces often needs to return to scales and rhythm exercises. The writer who has plateaued on long essays often needs to return to single paragraphs. The runner who has plateaued on long distances often needs to return to short intervals. This feels like regression, because the fundamentals are easier than the current level. But the fundamentals, re-encountered at a higher level of awareness, are where the next layer of improvement lives. The plateau is the brain’s way of telling you that the foundations need re-laying before the next floor can be built.'))
    story.append(section_subhead('The patience of mastery'))
    story.append(para(
        'The final feature of mastery is patience, and patience is the hardest part, because it cannot be faked and it cannot be rushed. The people who become genuinely good at things are not the people with the most talent. They are the people who are willing to keep showing up to unflattering practice, in private, with no audience and no immediate reward, for years. The willingness is rare, because the practice is boring and the rewards are delayed. But the willingness is also learnable. You do not need to be a naturally patient person. You need to build the habit of patient practice, one session at a time, until the habit itself becomes the reward. At that point, mastery becomes almost inevitable, because you have removed the only thing that could have stopped you — the decision to quit.'))

    # ─── Chapter 8 ───────────────────────────────────────────────────────
    story.extend(chapter_heading('Chapter 8', 'The People Around Your Habits'))
    story.append(para(
        'You become, over time, a rough average of the people you spend the most time with. This is not a motivational poster. It is a finding from decades of research on social contagion — that habits, moods, weights, smoking status, and even subjective well-being all spread through social networks in patterns that look remarkably like the spread of viruses. The people around you are not neutral observers of your habits. They are active variables, shaping your defaults every day, mostly without anyone noticing.',
        first=True))
    story.append(para(
        'The mechanism is simple. We absorb, mostly unconsciously, the behaviors of the people we are close to. If your friends exercise, exercise becomes normal. If your friends drink heavily, heavy drinking becomes normal. If your friends read, reading becomes normal. If your friends complain, complaining becomes normal. None of this is moral. None of it requires anyone to be pressuring anyone else. The pressure is structural — it is the slow gravity of being around people whose behaviors set your default.'))
    story.append(section_subhead('A short catalog of relational archetypes'))
    table_data = [
        [Paragraph('<b>Archetype</b>', table_header_style),
         Paragraph('<b>Effect on your habits</b>', table_header_style),
         Paragraph('<b>What to do</b>', table_header_style)],
        [Paragraph('The quiet model', table_cell_style),
         Paragraph('Does the thing you want to do, without making a fuss', table_cell_style),
         Paragraph('Spend more time near them. The contagion is automatic.', table_cell_style)],
        [Paragraph('The enabler', table_cell_style),
         Paragraph('Makes the bad habit easier and the good habit harder', table_cell_style),
         Paragraph('Limit time, or meet in contexts that disable the habit.', table_cell_style)],
        [Paragraph('The accountability partner', table_cell_style),
         Paragraph('Checks in on your commitments, without judgment', table_cell_style),
         Paragraph('Pick one. Be honest. Reciprocate.', table_cell_style)],
        [Paragraph('The saboteur', table_cell_style),
         Paragraph('Openly mocks or undermines your attempts to change', table_cell_style),
         Paragraph('Distance yourself. This is rarely salvageable.', table_cell_style)],
        [Paragraph('The silent witness', table_cell_style),
         Paragraph('Neither helps nor hurts, just observes', table_cell_style),
         Paragraph('Fine to keep, but do not expect support.', table_cell_style)],
    ]
    col_widths = [AVAILABLE_WIDTH * r for r in [0.24, 0.42, 0.34]]
    arch_table = Table(table_data, colWidths=col_widths, hAlign='CENTER')
    arch_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), HEADER_FILL),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, TABLE_STRIPE]),
        ('GRID', (0, 0), (-1, -1), 0.4, BORDER),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 7),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 7),
    ]))
    story.append(Spacer(1, 6))
    story.append(arch_table)
    story.append(Spacer(1, 6))
    story.append(Paragraph(
        '<i>Table 8.1 — Five common relationship types and their effects on habit formation.</i>',
        ParagraphStyle(name='Caption3', fontName='FreeSerif-Italic', fontSize=9,
                       leading=13, alignment=TA_CENTER, textColor=TEXT_MUTED,
                       spaceBefore=2, spaceAfter=14)))
    story.append(section_subhead('The honesty problem'))
    story.append(para(
        'It is uncomfortable to look at one’s social circle through this lens, because the implication is that some of the people you love may be quietly bad for your habits, and some of the people who would be good for your habits are people you have not yet spent much time with. The honest version of this exercise usually produces two lists: a small set of people who make you better, and a small set of people who make you worse, with the bulk of your acquaintances somewhere in the neutral middle. The work is not to abandon the people in the second list — that is rarely either possible or desirable. The work is to be deliberate about how much time you spend in each group, and to ensure that the first group gets at least as much of you as the second.'))
    story.append(section_subhead('The deliberate community'))
    story.append(para(
        'The most useful application of this chapter is to build a small, deliberate community around the habit you are trying to establish. If you want to write, find two other people who are trying to write, and meet them once a week to share work. If you want to run, find a running group that meets at 6 a.m., and show up. If you want to cook, find a friend who cooks, and cook with them on Sundays. The community does three things at once: it makes the habit visible, it makes the habit social, and it makes the habit sustainable, because the cost of skipping is no longer just private guilt — it is a small social cost, which is often enough to get you out the door on the mornings when private guilt would not have.'))
    story.append(pull_quote(
        '“The cost of skipping is no longer just private guilt. It is a small social cost, which is often enough to get you out the door on the mornings when private guilt would not have.”'))
    story.append(section_subhead('The reverse responsibility'))
    story.append(para(
        'One final point, and it is the one that matters most in the long run. You are also part of other people’s social networks. The habits you practice are quietly shaping the defaults of the people around you — your partner, your children, your colleagues, your friends. This is not a responsibility you can decline. You are shaping them, whether you intend to or not. The only choice is whether to shape them well. The person who quietly exercises, quietly reads, quietly eats well, quietly handles stress without complaint — that person is doing more for the people around them than they realize. They are setting the default. They are being the quiet model. And the people around them, over years, are quietly absorbing the lesson. This may be the most important habit work you ever do — not for yourself, but for the people who are watching you without knowing they are watching.'))

    # ─── Chapter 9 ───────────────────────────────────────────────────────
    story.extend(chapter_heading('Chapter 9', 'When Habits Break'))
    story.append(para(
        'Every habit, no matter how well-designed, will eventually break. You will get sick, you will travel, you will move, you will change jobs, you will have a child, you will grieve, you will go through a period when nothing feels normal. The habit you carefully built will collapse, sometimes for a day, sometimes for a month, sometimes for a year. This is not a sign that the habit was fragile. It is a sign that you are a human being, living in a world that periodically disrupts even the best-laid routines. The question is not whether your habits will break. The question is what you do when they do.',
        first=True))
    story.append(para(
        'The most common response to a broken habit is shame. We treat the break as evidence of failure, as proof that we were never really the kind of person we were trying to become. Shame is a poor response, for two reasons. First, it is empirically wrong — every habit breaks, in everyone, eventually. The break is not evidence of failure. It is evidence of being alive. Second, shame is counterproductive. It makes the return to the habit harder, because the habit has now become associated with a bad feeling, and the brain avoids things associated with bad feelings. The shame does not motivate the return. It delays it.'))
    story.append(section_subhead('The “never miss twice” rule'))
    story.append(callout(
        'The single rule that saves most habits',
        ['<b>Never miss twice.</b>',
         'If you miss a day, that is fine. Miss two in a row, and you have started a new habit — the habit of missing. The rule is simple: whatever you missed yesterday, do today, even badly, even briefly. The point is not to do the full workout. The point is to cast a vote that the break was an exception, not a new trajectory.',
         'One missed day is mathematically negligible. Two missed days is the beginning of a trajectory. Three missed days is a trajectory. The rule intercepts the trajectory at the earliest possible moment, when the cost of interception is lowest.']))
    story.append(para(
        'The “never miss twice” rule works because it intercepts the trajectory at the moment when the cost of interception is lowest. The first missed day is free — you were sick, you were traveling, the day went sideways. The second missed day is the decision point. If you do the habit on the second day, even badly, you have signaled to yourself that the first miss was an exception. If you skip the second day, you have signaled that the first miss was the beginning of a new pattern, and the brain will start to treat the new pattern as the default. The work of recovery, therefore, is to never let the second miss happen. The first miss is forgivable. The second is the one that costs.'))
    story.append(section_subhead('The recovery curve'))
    story.append(para(
        'When you return to a habit after a break, the first few sessions will be worse than you remember. The runner who has missed a month will find the first run painful and slow. The writer who has missed a month will find the first sentences awkward and forced. The meditator who has missed a month will find the first session restless and noisy. This is not a sign that the habit has been lost. It is a sign that the habit was real — that the brain had actually adapted to it, and that the adaptation has faded slightly during the break. The good news is that the adaptation comes back faster than it took to build the first time. The brain remembers. The first few sessions are awkward. The next few are surprisingly close to where you left off. Within two weeks, the habit is usually re-established, and you are back to where you were before the break, often with a renewed appreciation for why you were doing it in the first place.'))
    story.append(pull_quote(
        '“Shame does not motivate the return. It delays it. The first missed day is free. The second missed day is the decision point.”'))
    story.append(section_subhead('When the break is long'))
    story.append(para(
        'Sometimes the break is not a few days or a few weeks. Sometimes it is a year, or five years, or a decade. The habit you once had is gone, and the identity that went with it is gone too. This is a different situation, and it requires a different response. You cannot simply resume the old habit, because the person who had the old habit is no longer the person you are. The life is different. The body is different. The schedule is different. The reasons may even be different.'))
    story.append(para(
        'In this situation, the work is not to recover the old habit. It is to start a new one, informed by the old one but not constrained by it. The runner who has not run in ten years should not try to run the miles they used to run. They should start where they are, today, with the body they have today, and build a new running habit from scratch. The old habit is a memory, not a starting point. The new habit is the only one that matters. This is humbling, but it is also liberating — it means that long breaks do not have to be permanent. The habit can always be rebuilt. The identity can always be re-chosen. The only thing that cannot be recovered is the time that has passed, and that time has already passed, so there is nothing to be gained by mourning it.'))
    story.append(section_subhead('The kindness principle'))
    story.append(para(
        'The deepest lesson of this chapter is that the way you treat yourself when a habit breaks determines, more than almost anything else, whether the habit will return. The people whose habits are most durable are not the people whose habits never break — those people do not exist. They are the people who treat the break with kindness rather than shame, who intercept the trajectory early, who return to the habit without drama, who accept that the first few sessions will be awkward, and who keep showing up until the habit is re-established. Kindness, in this context, is not soft. It is strategic. It is the response that most reliably produces the return. Shame is the response that most reliably prevents it.'))

    # ─── Chapter 10 ──────────────────────────────────────────────────────
    story.extend(chapter_heading('Chapter 10', 'Your Quiet Edge — A 90-Day Practice'))
    story.append(para(
        'We have spent nine chapters examining the mechanics of habits — why breakthroughs are mostly myths, how small things compound, how environments shape behavior, how identity loops work, how triggers and friction structure willpower, how recovery underlies everything, how quiet practice produces mastery, how the people around you shape your defaults, and what to do when habits break. This final chapter turns those mechanics into a plan. The plan is deliberately modest. It covers ninety days, not thirty. It asks for small commitments, not large ones. It assumes that you have a life, with constraints, and that any plan that does not account for those constraints will not survive the first week.',
        first=True))
    story.append(para(
        'The reason for ninety days, rather than the more familiar thirty, is that thirty days is enough time to start a habit but not enough time to stabilize one. At thirty days, the habit is still fragile — it depends on the novelty, the structure, and the external accountability that the thirty-day challenge provided. At ninety days, the habit has been through a normal range of life circumstances — a busy week, a bad cold, a social obligation, a travel day — and has either survived them or been recovered from them. The habit that survives ninety days is a habit that has been stress-tested. It is now actually yours.'))
    story.append(section_subhead('The 90-day progression'))
    table_data = [
        [Paragraph('<b>Phase</b>', table_header_style),
         Paragraph('<b>Days</b>', table_header_style),
         Paragraph('<b>Focus</b>', table_header_style),
         Paragraph('<b>Success criterion</b>', table_header_style)],
        [Paragraph('Foundation', table_cell_style),
         Paragraph('1–30', table_cell_center),
         Paragraph('Pick one habit. Make it small. Do it daily.', table_cell_style),
         Paragraph('Habit performed on ≥ 25 days', table_cell_style)],
        [Paragraph('Stabilization', table_cell_style),
         Paragraph('31–60', table_cell_center),
         Paragraph('Habit survives travel, illness, busy weeks.', table_cell_style),
         Paragraph('Habit performed on ≥ 25 days, including ≥ 1 hard day', table_cell_style)],
        [Paragraph('Integration', table_cell_style),
         Paragraph('61–90', table_cell_center),
         Paragraph('Habit becomes part of identity, no longer requires negotiation.', table_cell_style),
         Paragraph('Habit performed on ≥ 25 days, skipped days recovered within 1 day', table_cell_style)],
        [Paragraph('Continuation', table_cell_style),
         Paragraph('90+', table_cell_center),
         Paragraph('Habit is now a default. Optional: add a second habit.', table_cell_style),
         Paragraph('Habit maintained with minimal effort', table_cell_style)],
    ]
    col_widths = [AVAILABLE_WIDTH * r for r in [0.18, 0.12, 0.42, 0.28]]
    plan_table = Table(table_data, colWidths=col_widths, hAlign='CENTER')
    plan_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), HEADER_FILL),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, TABLE_STRIPE]),
        ('GRID', (0, 0), (-1, -1), 0.4, BORDER),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 7),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 7),
    ]))
    story.append(Spacer(1, 6))
    story.append(plan_table)
    story.append(Spacer(1, 6))
    story.append(Paragraph(
        '<i>Table 10.1 — A 90-day progression. Each phase has a single focus and a single success criterion. Anything more ambitious will probably fail.</i>',
        ParagraphStyle(name='Caption4', fontName='FreeSerif-Italic', fontSize=9,
                       leading=13, alignment=TA_CENTER, textColor=TEXT_MUTED,
                       spaceBefore=2, spaceAfter=14)))
    story.append(section_subhead('Choosing your one habit'))
    story.append(para(
        'The most common mistake at the start of a ninety-day plan is to choose too many habits. The plan calls for one. Choose one. The one you choose should meet three criteria. First, it should be small enough that you can do it on a bad day — a five-minute version, not a forty-five-minute version. Second, it should be a keystone habit, meaning a habit that tends to pull other good habits along with it. Exercise is the classic keystone habit — people who exercise regularly tend to also eat better, sleep better, and drink less, even when they do not explicitly try to. Sleep is another keystone. So is daily reading, for some people. So is a daily walk. Third, it should be a habit you actually want, not one you think you should want. The should-want gap is where most habits die. Choose the habit you would do even if no one were watching. That is the one that will survive ninety days.'))
    story.append(section_subhead('What to expect'))
    story.append(para(
        'In the first thirty days, the habit will feel novel and effortful. You will need reminders, environmental design, and possibly accountability. This is normal. The habit is not yet automatic; it is still being negotiated each day. By day thirty, the negotiation should be shorter — the habit is becoming a default, though a fragile one.'))
    story.append(para(
        'In the second thirty days, life will happen. You will travel, you will get sick, you will have a week from hell. This is the phase where most habits die, because the structure that supported them in the first thirty days is suddenly gone. The work of this phase is recovery — applying the “never miss twice” rule, returning to the habit without shame, accepting that some days will be five-minute versions rather than full sessions. If the habit survives this phase, it has been stress-tested.'))
    story.append(para(
        'In the third thirty days, something quieter happens. The habit stops feeling like a habit and starts feeling like a fact. You no longer negotiate with yourself about whether to do it. You no longer need reminders. The habit has been absorbed into your identity, and doing it has become an expression of who you are, not an imposition on who you are. This is the phase where the quiet edge becomes visible. Not to others, necessarily — often only to you. But you will notice. The day feels different when it starts with the habit. The week feels different when the habit has been done every day. The life, slowly, starts to feel different.'))
    story.append(pull_quote(
        '“The day feels different when it starts with the habit. The week feels different when the habit has been done every day. The life, slowly, starts to feel different.”'))
    story.append(section_subhead('A closing note'))
    story.append(para(
        'This book has made a single argument, repeated in ten variations: that the lives we admire are not built from breakthroughs. They are built from ordinary habits, repeated quietly, over years, until the habits become the life. The argument is not glamorous. It does not promise transformation in thirty days. It does not depend on motivation, willpower, or luck. It depends only on the willingness to choose one small thing, do it daily, recover from the inevitable breaks, and keep going.'))
    story.append(para(
        'If you do this — if you choose one habit, do it for ninety days, and then continue — you will, at the end of the ninety days, be a slightly different person. Not dramatically different. Slightly different. And in five years, you will be a substantially different person, in ways that you cannot now predict and that no one will mistake for a breakthrough. They will look, from the outside, like a quiet kind of success — the kind that does not announce itself, that does not require an audience, that does not depend on motivation. They will look like the kind of life that just seems to work. That is the quiet edge. It is available to anyone who is willing to do ordinary things, consistently, for longer than they feel like doing them. The pages ahead are blank. The next ninety days are yours.'))

    return story


# ──────────────────────────────────────────────────────────────────────────────
# Main
# ──────────────────────────────────────────────────────────────────────────────
def main():
    output_path = '/home/z/my-project/scripts/body.pdf'

    doc = TocDocTemplate(
        output_path,
        pagesize=A4,
        leftMargin=LEFT_MARGIN,
        rightMargin=RIGHT_MARGIN,
        topMargin=TOP_MARGIN,
        bottomMargin=BOTTOM_MARGIN,
        title='The Quiet Edge',
        author='Z.ai Press',
        creator='Z.ai',
        subject='A book on habits and quiet mastery',
    )

    story = build_story()
    doc.multiBuild(story, onFirstPage=draw_header_footer, onLaterPages=draw_header_footer)
    print(f'Body PDF generated: {output_path}')


if __name__ == '__main__':
    main()
