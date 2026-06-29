import streamlit as st
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.pdfgen import canvas
import io

def parse_anki_file(file):
    """
    This parses an Anki deck txt file and extracts the flashcards.
    """
    cards = []
    for line in file:
        line = line.decode("utf-8").strip()
        if not line.strip() or line.startswith('#'):
            continue #we skip empty lines and commments
        parts = line.strip().split("\t")
        if len(parts) >= 2:
            front = parts[0].replace('<br>', '\n').replace('&nbsp;', ' ')
            back = parts[1].replace('<br>', '\n').replace('&nbsp;', ' ')
            cards.append({'front': front, 'back': back})
    return cards  

def draw_card(c, x, y, width, height, text):
    """
    Draws a single flashcard.
    """

    c.setStrokeColor(colors.lightgrey)
    c.setLineWidth(1)
    c.rect(x, y, width, height, stroke=1, fill=0)

    c.setFillColor(colors.black)
    c.setFont("Helvetica", 12)

    lines = text.split('\n')
    line_height = 14
    total_text_height = len(lines) * line_height
    start_y = y + (height / 2) + (total_text_height / 2) - line_height

    for i, line in enumerate(lines):
        current_y = start_y - (i * line_height)
        if current_y > y + 5:
            c.drawCentredString(x + (width / 2), current_y, line.strip())


