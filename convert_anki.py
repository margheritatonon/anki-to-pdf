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