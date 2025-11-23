import streamlit as st
import base64
import os

st.set_page_config(page_title="Document Viewer", layout="wide")

st.title("Document Viewer")

# read pdf
pdf_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "document.pdf")
with open(pdf_path, "rb") as f:
    pdf_bytes = f.read()

pdf_b64 = base64.b64encode(pdf_bytes).decode("utf-8")

# load viewer.html
viewer_path = os.path.join(os.path.dirname(__file__), "pdfjs", "viewer.html")
with open(viewer_path, "r", encoding="utf-8") as f:
    html_template = f.read()

# inject pdf
final_html = html_template.replace("{{BASE64PDF}}", pdf_b64)

# display
st.components.v1.html(final_html, height=900, scrolling=False)

# Hide Streamlit UI elements
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)