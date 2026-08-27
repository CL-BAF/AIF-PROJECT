#!/usr/bin/env python3
"""Render the AIF portfolio Markdown to one submission-ready .docx (stdlib only).

No pandoc or python-docx on this host, so this hand-writes the OOXML parts.
Supports the subset of markdown used in this repo: #/##/### headings, paragraphs,
**bold**/*italic*, pipe tables, > blockquotes, - / 1. lists, --- rules.
"""
import glob, os, re, zipfile

ROOT = os.path.dirname(os.path.abspath(__file__))

def esc(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

def plain(text):
    """Keep link labels in Word; URLs remain available in the Markdown record."""
    return re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', text)

def runs(text):
    """Convert **bold** / *italic* markdown to w:r runs."""
    text = plain(text)
    out, pos = [], 0
    for m in re.finditer(r'\*\*(.+?)\*\*|\*(.+?)\*', text):
        if m.start() > pos:
            out.append(f'<w:r><w:t xml:space="preserve">{esc(text[pos:m.start()])}</w:t></w:r>')
        if m.group(1) is not None:
            out.append(f'<w:r><w:rPr><w:b/></w:rPr><w:t xml:space="preserve">{esc(m.group(1))}</w:t></w:r>')
        else:
            out.append(f'<w:r><w:rPr><w:i/></w:rPr><w:t xml:space="preserve">{esc(m.group(2))}</w:t></w:r>')
        pos = m.end()
    if pos < len(text):
        out.append(f'<w:r><w:t xml:space="preserve">{esc(text[pos:])}</w:t></w:r>')
    return ''.join(out)

def para(text, style=None, ind=None):
    props = []
    if style: props.append(f'<w:pStyle w:val="{style}"/>')
    if ind: props.append(f'<w:ind w:left="{ind}"/>')
    ppr = '<w:pPr>' + ''.join(props) + '</w:pPr>' if props else ''
    return f'<w:p>{ppr}{runs(text)}</w:p>'

def cell(text, bold=False):
    rendered = runs(f'**{plain(text)}**') if bold else runs(text)
    return ('<w:tc><w:tcPr><w:tcMar>'
            '<w:top w:w="60" w:type="dxa"/><w:left w:w="100" w:type="dxa"/>'
            '<w:bottom w:w="60" w:type="dxa"/><w:right w:w="100" w:type="dxa"/>'
            '</w:tcMar></w:tcPr>'
            f'<w:p>{rendered}</w:p></w:tc>')

def table(rows):
    borders = ('<w:tblBorders>'
               + ''.join(f'<w:{s} w:val="single" w:sz="4" w:color="999999"/>'
                         for s in ('top', 'left', 'bottom', 'right', 'insideH', 'insideV'))
               + '</w:tblBorders>')
    width = '<w:tblW w:w="5000" w:type="pct"/>'
    trs = []
    for i, row in enumerate(rows):
        trs.append('<w:tr>' + ''.join(cell(c, bold=(i == 0)) for c in row) + '</w:tr>')
    return '<w:tbl><w:tblPr>' + width + borders + '</w:tblPr>' + ''.join(trs) + '</w:tbl>'

def split_row(line):
    return [c.strip() for c in line.strip().strip('|').split('|')]

def render(md_text):
    parts, lines = [], md_text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i].rstrip()
        if not line.strip():
            i += 1
            continue
        if line.startswith('|'):
            rows = []
            while i < len(lines) and lines[i].strip().startswith('|'):
                if not re.match(r'^\s*\|[\s\-:|]+\|\s*$', lines[i]):  # skip separator row
                    rows.append(split_row(lines[i]))
                i += 1
            parts.append(table(rows))
            continue
        if line.startswith('### '):
            parts.append(para(line[4:], style='Heading3'))
        elif line.startswith('## '):
            parts.append(para(line[3:], style='Heading2'))
        elif line.startswith('# '):
            parts.append(para(line[2:], style='Title'))
        elif line.strip() == '---':
            parts.append('<w:p><w:pPr><w:pBdr><w:bottom w:val="single" w:sz="6" w:color="AAAAAA"/></w:pBdr></w:pPr></w:p>')
        elif line.startswith('> '):
            quote = []
            while i < len(lines) and lines[i].startswith('>'):
                quote.append(lines[i].lstrip('> ').rstrip())
                i += 1
            parts.append(''.join(para(q, style='Quote', ind=430) for q in quote if q))
            continue
        elif re.match(r'^\s*[-*] ', line):
            parts.append(para('•  ' + re.sub(r'^\s*[-*] ', '', line), ind=360))
        elif re.match(r'^\s*\d+\. ', line):
            parts.append(para(re.sub(r'^\s*(\d+)\. ', r'\1.  ', line), ind=360))
        else:
            parts.append(para(line))
        i += 1
    return ''.join(parts)

def styles_xml():
    grid = ('<w:style w:type="table" w:styleId="TableGrid"><w:name w:val="Table Grid"/>'
            '<w:tblPr><w:tblBorders>'
            + ''.join(f'<w:{s} w:val="single" w:sz="4" w:color="999999"/>'
                      for s in ('top', 'left', 'bottom', 'right', 'insideH', 'insideV'))
            + '</w:tblBorders></w:tblPr></w:style>')
    return ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
        '<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
        '<w:docDefaults><w:rPrDefault><w:rPr>'
        '<w:rFonts w:ascii="Calibri" w:hAnsi="Calibri" w:cs="Calibri"/>'
        '<w:sz w:val="22"/><w:szCs w:val="22"/>'
        '</w:rPr></w:rPrDefault>'
        '<w:pPrDefault><w:pPr><w:spacing w:after="160" w:line="276" w:lineRule="auto"/></w:pPr></w:pPrDefault>'
        '</w:docDefaults>'
        '<w:style w:type="paragraph" w:default="1" w:styleId="Normal"><w:name w:val="Normal"/></w:style>'
        '<w:style w:type="paragraph" w:styleId="Title">'
        '<w:name w:val="Title"/><w:basedOn w:val="Normal"/>'
        '<w:pPr><w:spacing w:after="240"/></w:pPr>'
        '<w:rPr><w:b/><w:sz w:val="40"/><w:szCs w:val="40"/></w:rPr></w:style>'
        '<w:style w:type="paragraph" w:styleId="Heading2">'
        '<w:name w:val="heading 2"/><w:basedOn w:val="Normal"/>'
        '<w:pPr><w:keepNext/><w:spacing w:before="240" w:after="120"/></w:pPr>'
        '<w:rPr><w:b/><w:sz w:val="28"/><w:szCs w:val="28"/></w:rPr></w:style>'
        '<w:style w:type="paragraph" w:styleId="Heading3">'
        '<w:name w:val="heading 3"/><w:basedOn w:val="Normal"/>'
        '<w:pPr><w:keepNext/><w:spacing w:before="200" w:after="100"/></w:pPr>'
        '<w:rPr><w:b/><w:sz w:val="24"/><w:szCs w:val="24"/></w:rPr></w:style>'
        '<w:style w:type="paragraph" w:styleId="Quote">'
        '<w:name w:val="Quote"/><w:basedOn w:val="Normal"/>'
        '<w:rPr><w:i/><w:color w:val="444444"/></w:rPr></w:style>'
        + grid + '</w:styles>')

def write_docx(md_path, out_path):
    write_docx_text(open(md_path, encoding='utf-8').read(), out_path)

def write_docx_text(md_text, out_path):
    body = render(strip_meta(md_text))
    document = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
        '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
        '<w:body>' + body +
        '<w:sectPr><w:pgSz w:w="11906" w:h="16838"/>'
        '<w:pgMar w:top="1440" w:right="1440" w:bottom="1440" w:left="1440" '
        'w:header="708" w:footer="708" w:gutter="0"/></w:sectPr>'
        '</w:body></w:document>')
    content_types = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
        '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
        '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
        '<Default Extension="xml" ContentType="application/xml"/>'
        '<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>'
        '<Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>'
        '</Types>')
    rels = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
        '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>'
        '</Relationships>')
    doc_rels = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
        '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>'
        '</Relationships>')
    with zipfile.ZipFile(out_path, 'w', zipfile.ZIP_DEFLATED) as z:
        z.writestr('[Content_Types].xml', content_types)
        z.writestr('_rels/.rels', rels)
        z.writestr('word/document.xml', document)
        z.writestr('word/_rels/document.xml.rels', doc_rels)
        z.writestr('word/styles.xml', styles_xml())
    # sanity: every part parses as XML
    import xml.dom.minidom
    with zipfile.ZipFile(out_path) as z:
        for name in z.namelist():
            if name.endswith('.xml') or name.endswith('.rels'):
                xml.dom.minidom.parseString(z.read(name))
    print('wrote', os.path.relpath(out_path, ROOT))

META_RE = re.compile(r'^\s*\*\(\s*(AT2|Portfolio item).*\)\s*$', re.S)

def strip_meta(md_text):
    """Remove working notes (word-count markers, total lines, italic meta notes)
    that belong to the markdown working copy, not the teacher-facing document."""
    kept = []
    for line in md_text.splitlines():
        s = line.strip()
        if s.startswith('*(') and s.endswith(')*'):
            continue  # word-count marker or intro meta note
        if s.startswith('**Total:'):
            continue  # self-audit line
        kept.append(line)
    return '\n'.join(kept)

def main():
    # AT1 portfolio only. AT2 progress checks remain separate Markdown drafts so
    # the portfolio appendix cannot be mistaken for part of AT2's word count.
    order = [
        'portfolio.md',
        'learning-goal-and-plan.md',
        'strategy-tracking.md',
        'feedback-and-perspectives.md',
        'reflection-sheet.md',
        'sources.md',
        'expert-outreach.md',
        'evidence-extracts.md',
    ]
    combined = ['# Kobald — AIF Portfolio\n',
                'SACE Stage 2 Activating Identities and Futures\n',
                'Evidence record updated 27 August 2026\n---\n']
    for filename in order:
        md = os.path.join(ROOT, 'portfolio', filename)
        text = strip_meta(open(md, encoding='utf-8').read())
        # Keep the document title unique; later top-level Markdown headings are
        # section headings in the compiled portfolio.
        if filename != 'portfolio.md':
            text = re.sub(r'^# ', '## ', text, count=1, flags=re.M)
        combined.append(text)
        combined.append('\n---\n')
    write_docx_text('\n'.join(combined), os.path.join(ROOT, 'AIF-Portfolio.docx'))

if __name__ == '__main__':
    main()
