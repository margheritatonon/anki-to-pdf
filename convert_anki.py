import streamlit as st
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.pdfgen import canvas
import io

def parse_anki_file(file):
    """
    This parses an Anki deck txt file and extracts the flashcards.
    """
    pass