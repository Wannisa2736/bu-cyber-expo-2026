import streamlit as st
from PIL import Image, ImageOps

st.set_page_config(page_title="BU Cyber Expo 2026", layout="wide")

# --------- CUSTOM CSS ----------
st.markdown("""
<style>
body {
    background-color: #0b1120;
}
.main {
    background: linear-gradient(180deg, #0b1120 0%, #0f172a 100%);
    color: white;
}
.card {
    background: rgba(255,255,255,0.05);
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0 0 20px rgba(0,255,255,0.2);
    margin-bottom: 20px;
}
.section-title {
    font-size: 28px;
    font-weight: bold;
    margin-top: 30px;
    margin-bottom: 15px;
    color: #38bdf8;
}
</style>
""", unsafe_allow_html=True)

def load_image(path):
    img = Image.open(path)
    img = ImageOps.exif_transpose(img)
    return img

# --------- HEADER ----------
st.markdown("<h1 style='text-align:center; color:#38bdf8;'>BU Cyber Fortress Challenge & Career Expo 2026</h1>", unsafe_allow_html=True)

st.markdown("<div class='card'><h3>🏢 Company: A06 – SecureLine Co., Ltd.</h3></div>", unsafe_allow_html=True)

# --------- COMPANY INSIGHTS ----------
st.markdown("<div class='section-title'>🔎 Company Insights</div>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("<div class='card'>🔐 Cybersecurity</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='card'>🌐 Network Security</div>", unsafe_allow_html=True)

with col3:
    st.markdown("<div class='card'>☁️ Cloud Security</div>", unsafe_allow_html=True)

# --------- EVIDENCE ----------
st.markdown("<div class='section-title'>📸 Evidence การเข้าร่วมงาน</div>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.image(load_image("booth.jpg"), use_container_width=True)
    st.caption("บรรยากาศภายในงาน")

with col2:
    st.image(load_image("passport.jpg"), use_container_width=True)
    st.caption("บูธของ SecureLine")

# --------- REFLECTION ----------
st.markdown("<div class='section-title'>💡 Self-Reflection</div>", unsafe_allow_html=True)

st.markdown("""
<div class='card'>
งานนี้ทำให้ได้เรียนรู้เกี่ยวกับสายงาน Cybersecurity มากขึ้น  
ได้เห็นการทำงานจริงของบริษัทด้านความปลอดภัยไซเบอร์  
และเข้าใจทักษะที่ควรพัฒนาเพิ่มเติมในอนาคต
</div>
""", unsafe_allow_html=True)
