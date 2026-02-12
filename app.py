import streamlit as st
from PIL import Image

st.set_page_config(page_title="BU Cyber Expo 2026", layout="wide")

# ----- Header -----
st.markdown("<h1 style='text-align: center;'>BU Cyber Fortress Challenge & Career Expo 2026</h1>", unsafe_allow_html=True)

st.markdown("### 🏢 Company: A06 – SecureLine Co., Ltd.")

st.divider()

# ----- Company Insights -----
st.subheader("💡 Company Insights")

st.markdown("""
- เป็นบริษัทด้าน Cybersecurity
- ทำงานเกี่ยวกับ Network Security และ Cloud Security
- มีการพัฒนาเครื่องมือด้านความปลอดภัยของข้อมูล
""")

st.divider()

# ----- Evidence Section -----
st.subheader("📸 Evidence การเข้าร่วมงาน")

col1, col2 = st.columns(2)

with col1:
    st.image("booth.jpg", use_container_width=True)

with col2:
    st.image("passport.jpg", use_container_width=True)

st.divider()

# ----- Reflection -----
st.subheader("💭 Self-Reflection")

st.markdown("""
งานนี้ทำให้ได้เรียนรู้เกี่ยวกับสายงาน Cybersecurity มากขึ้น  
ได้เห็นบรรยากาศการทำงานจริง  
และเข้าใจทักษะที่ควรพัฒนาเพิ่มเติม
""")
