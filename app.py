import pathlib
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="AI Pitch Deck Generator", page_icon="📊", layout="wide")

st.markdown(
    """
    <div style="padding: 1.2rem; border-radius: 14px;
         background: linear-gradient(135deg,#667eea 0%,#764ba2 100%); color:#fff;">
      <h1 style="margin:0;">AI Pitch Deck Generator</h1>
      <p style="margin:.2rem 0 0;opacity:.95;">Client-side app (PPTX/PDF export)</p>
    </div>
    """,
    unsafe_allow_html=True,
)

html_path = pathlib.Path(__file__).parent / "static" / "index.html"
html = html_path.read_text(encoding="utf-8")

# Render full HTML app (all logic is client-side)
components.html(html, height=2200, scrolling=True)
