import streamlit as st
from pathlib import Path
import base64

st.set_page_config(
    page_title="PrediCareAI – AI-Powered Elderly Care Assistant",
    layout="wide",
)

# 1. Read the HTML file
html_file = Path("predicare.html")
html_content = html_file.read_text(encoding="utf-8")

# 2. Read and base64-encode the logo
logo_path = Path("logo.png")
logo_bytes = logo_path.read_bytes()
logo_b64 = base64.b64encode(logo_bytes).decode("utf-8")

# 3. Replace src="logo.png" in the HTML with an embedded data URL
html_content = html_content.replace(
    'src="logo.png"',
    f'src="data:image/png;base64,{logo_b64}"'
)

# 4. Render in Streamlit
st.components.v1.html(
    html_content,
    height=900,
    scrolling=True,
)
