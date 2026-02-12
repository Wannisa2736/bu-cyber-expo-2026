import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="BU Cyber Expo 2026",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
.main {
    background: linear-gradient(180deg, #0b1120 0%, #0f172a 100%);
    color: white;
}

h1 {
    text-align: center;
    color: #38bdf8;
}

.section-title {
    font-size: 28px;
    font-weight: bold;
    margin-top: 40px;
    margin-bottom: 20px;
    color: #22d3ee;
}

.card {
    background: rgba(255,255,255,0.05);
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0 0 20px rgba(0,255,255,0.15);
    margin-bottom: 20px;
}

.caption-center {
    text-align: center;
    font-size: 14px;
    color: #cbd5e1;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("""
<h1>BU Cyber Fortress Challenge & Career Expo 2026</h1>
""", unsafe_allow_html=True)

st.markdown("""
<div class='card'>
<h3>🏢 Company: A06 – SecureLine Co., Ltd.</h3>
บริษัทด้าน Cybersecurity ที่ให้บริการด้าน Network Security และ Cloud Security
</div>
""", unsafe_allow_html=True)

# ---------------- COMPANY INSIGHTS ----------------
st.markdown("<div class='section-title'>🔎 Company Insights</div>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("<div class='card'>🔐 Cybersecurity Solutions</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='card'>🌐 Network Security Systems</div>", unsafe_allow_html=True)

with col3:
    st.markdown("<div class='card'>☁️ Cloud Security Protection</div>", unsafe_allow_html=True)

# ---------------- EVIDENCE ----------------
st.markdown("<div class='section-title'>📸 Evidence การเข้าร่วมงาน</div>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.image("booth.jpg", use_container_width=True)
    st.markdown("<div class='caption-center'>บรรยากาศภายในงาน</div>", unsafe_allow_html=True)

with col2:
    st.image("passport.jpg", use_container_width=True)
    st.markdown("<div class='caption-center'>บูธของ SecureLine</div>", unsafe_allow_html=True)

# ---------------- REFLECTION ----------------
st.markdown("<div class='section-title'>💡 Self-Reflection</div>", unsafe_allow_html=True)

st.markdown("""
<div class='card'>
งานนี้ทำให้ได้เรียนรู้เกี่ยวกับสายงาน Cybersecurity มากขึ้น  
ได้เห็นบรรยากาศการทำงานจริงของบริษัทด้านความปลอดภัยไซเบอร์  
และเข้าใจทักษะที่ควรพัฒนาเพิ่มเติมในอนาคต เช่น  
- การพัฒนา Network Security  
- ความรู้ด้าน Cloud Infrastructure  
- การทำงานเป็นทีมในสายงาน IT
</div>
""", unsafe_allow_html=True)
