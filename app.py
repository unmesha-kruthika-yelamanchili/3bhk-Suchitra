import streamlit as st
import base64
import os

# ---- PAGE CONFIG FOR MOBILE ----
st.set_page_config(
    page_title="Document Viewer",
    layout="wide"
)

# ---- MOBILE RESPONSIVE CSS ----
st.markdown("""
<style>
/* Remove side padding on mobile */
.main {
    padding-left: 0 !important;
    padding-right: 0 !important;
}

/* Make iframe/pdf viewer responsive */
iframe, .element-container, .stHtml {
    width: 100% !important;
    max-width: 100% !important;
    overflow: hidden !important;
}

/* full height fix */
html, body {
    margin: 0;
    padding: 0;
    width: 100%;
    overflow-x: hidden;
}
</style>
""", unsafe_allow_html=True)

# ---- TITLE ----
st.title("Document Viewer")

# ---- LOAD PDF ----
pdf_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "document.pdf")
with open(pdf_path, "rb") as f:
    pdf_bytes = f.read()

pdf_b64 = base64.b64encode(pdf_bytes).decode("utf-8")

# ---- LOAD HTML VIEWER ----
viewer_path = os.path.join(os.path.dirname(__file__), "pdfjs", "viewer.html")
with open(viewer_path, "r", encoding="utf-8") as f:
    html_template = f.read()

# ---- INJECT PDF ----
final_html = html_template.replace("{{BASE64PDF}}", pdf_b64)

# ---- DISPLAY EMBED ----
st.components.v1.html(final_html, height=900, scrolling=False)

# ---- HIDE STREAMLIT UI ----
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)
