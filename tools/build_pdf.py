"""Build the technical documentation PDF from its Markdown source.

Supports the headings, paragraphs, images, lists and tables used in this
repository. No spatial analysis or model simulation is performed.
"""
from pathlib import Path
import re
from xml.sax.saxutils import escape
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.utils import ImageReader
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'docs/technische-dokumentation.md'
OUTPUT = SOURCE.with_suffix('.pdf')


def build():
    fontdir = Path('/usr/share/fonts/truetype/dejavu')
    if (fontdir / 'DejaVuSans.ttf').exists():
        for name, file in [('Body', 'DejaVuSans.ttf'), ('BodyBold', 'DejaVuSans-Bold.ttf')]:
            pdfmetrics.registerFont(TTFont(name, str(fontdir / file)))
        pdfmetrics.registerFontFamily('Body', normal='Body', bold='BodyBold', italic='Body', boldItalic='BodyBold')
        normal, bold = 'Body', 'BodyBold'
    else:
        normal, bold = 'Helvetica', 'Helvetica-Bold'
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle('BodyDoc', fontName=normal, fontSize=9.3, leading=14, spaceAfter=8))
    styles.add(ParagraphStyle('TitleDoc', fontName=bold, fontSize=23, leading=29, textColor=colors.HexColor('#465e36'), spaceAfter=15))
    styles.add(ParagraphStyle('Chapter', fontName=bold, fontSize=14, leading=19, textColor=colors.HexColor('#465e36'), spaceBefore=16, spaceAfter=9, keepWithNext=True))
    styles.add(ParagraphStyle('Sub', fontName=bold, fontSize=11, leading=15, spaceBefore=10, spaceAfter=6, keepWithNext=True))
    styles.add(ParagraphStyle('Cell', fontName=normal, fontSize=8, leading=11))
    styles.add(ParagraphStyle('Caption', fontName=normal, fontSize=8, leading=11, textColor=colors.HexColor('#666666'), spaceAfter=12))
    width = A4[0] - 100

    def inline(s):
        s = escape(s)
        s = re.sub(r'`([^`]+)`', r'<font color="#465e36">\1</font>', s)
        s = re.sub(r'\*\*([^*]+)\*\*', r'<b>\1</b>', s)
        # Preserve Markdown link labels, keeping URLs in the source documentation.
        s = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'\1', s)
        return s

    lines = SOURCE.read_text(encoding='utf-8').splitlines()
    story, i = [], 0
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue
        image_match = re.fullmatch(r'!\[([^\]]*)\]\(([^)]+)\)', line)
        if image_match:
            caption, file = image_match.groups()
            imagepath = SOURCE.parent / file
            iw, ih = ImageReader(str(imagepath)).getSize()
            scale = min(width / iw, 245 / ih)
            story.append(Image(str(imagepath), width=iw*scale, height=ih*scale))
            story.append(Paragraph(inline(caption), styles['Caption']))
            i += 1
            continue
        if line.startswith('|'):
            rows = []
            while i < len(lines) and lines[i].strip().startswith('|'):
                parts = [x.strip() for x in lines[i].strip().strip('|').split('|')]
                if not all(re.fullmatch(r':?-+:?', x) for x in parts):
                    rows.append([Paragraph(inline(x), styles['Cell']) for x in parts])
                i += 1
            n = len(rows[0])
            table = Table(rows, colWidths=[width/n]*n, repeatRows=1, hAlign='LEFT')
            table.setStyle(TableStyle([
                ('BACKGROUND',(0,0),(-1,0),colors.HexColor('#e7eddc')),
                ('VALIGN',(0,0),(-1,-1),'TOP'),
                ('GRID',(0,0),(-1,-1),0.35,colors.HexColor('#bdc5b4')),
                ('LEFTPADDING',(0,0),(-1,-1),7),('RIGHTPADDING',(0,0),(-1,-1),7),
                ('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6),
            ]))
            story += [table, Spacer(1,10)]
            continue
        if line.startswith('# '):
            story.append(Paragraph(inline(line[2:]), styles['TitleDoc']))
        elif line.startswith('## '):
            story.append(Paragraph(inline(line[3:]), styles['Chapter']))
        elif line.startswith('### '):
            story.append(Paragraph(inline(line[4:]), styles['Sub']))
        else:
            chunks = [line]
            # Consecutive list lines remain individual paragraphs.
            if not re.match(r'^(\d+\. |[-*] )', line):
                while i+1 < len(lines) and lines[i+1].strip() and not re.match(r'^(#|\||!\[|\d+\. |[-*] )', lines[i+1].strip()):
                    i += 1
                    chunks.append(lines[i].strip())
            story.append(Paragraph(inline(' '.join(chunks)), styles['BodyDoc']))
        i += 1

    def page(canvas, doc):
        canvas.setTitle('Tegel-Modell - Technische Dokumentation')
        canvas.setAuthor('Tegel im Tausch')
        canvas.setStrokeColor(colors.HexColor('#bdc5b4'))
        canvas.line(50, A4[1]-35, A4[0]-50, A4[1]-35)
        canvas.setFont(normal,7.5)
        canvas.setFillColor(colors.HexColor('#666666'))
        canvas.drawString(50,23,'Tegel-Modell | Technische Dokumentation')
        canvas.drawRightString(A4[0]-50,23,str(doc.page))

    SimpleDocTemplate(str(OUTPUT), pagesize=A4, rightMargin=50, leftMargin=50,
                      topMargin=48, bottomMargin=45).build(story, onFirstPage=page, onLaterPages=page)
    print(OUTPUT)


if __name__ == '__main__':
    build()
