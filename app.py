import streamlit as st
from PIL import Image

st.set_page_config(page_title="BU Cyber Expo 2026", layout="centered")

# ตั้งค่า A4 Style
st.markdown("""
    <style>
    .a4-container {
        width: 794px;
        height: 1123px;
        padding: 40px;
        margin: auto;
        background-color: white;
        box-shadow: 0 0 10px rgba(0,0,0,0.2);
        font-family: Arial, sans-serif;
    }
    h1 {
        text-align: center;
        color: #0B3D91;
    }
    h2 {
        color: #C00000;
        margin-top: 20px;
    }
    p, li {
        font-size: 14px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="a4-container">', unsafe_allow_html=True)

st.markdown("<h1>BU Cyber Fortress Challenge & Career Expo 2026</h1>", unsafe_allow_html=True)

st.markdown("### 🏢 Company: A06 – SecureInfo Co., Ltd.")
st.markdown("**ประเภทองค์กร:** Cybersecurity & IT Security Solutions")

st.markdown("## 🛡 Company Insights")
st.markdown("""
- **ตำแหน่งงาน:** Cybersecurity Analyst, Security Engineer, SOC Analyst, Internship  
- **Skills ที่ต้องมี:** Network, Cybersecurity, Log Analysis, Problem Solving  
- **Tools:** Firewall, SIEM, IDS/IPS, Endpoint Security  
- **Certificate แนะนำ:** Security+, CEH, Network+  
- **คำแนะนำ:** ฝึก Lab จริง, ทำ Portfolio, พัฒนาทักษะวิเคราะห์
""")

st.markdown("## 📸 Evidence การเข้าร่วมงาน")

passport = Image.open("passport.jpg")
booth = Image.open("booth.jpg")

st.image(passport, caption="ภาพถ่ายคู่กับ Passport", use_container_width=True)
st.image(booth, caption="ภาพระหว่างสนทนากับพี่ในบูธ SecureInfo", use_container_width=True)

st.markdown("## 💡 Self-Reflection")
st.markdown("""
จากการเข้าร่วมงาน ทำให้เข้าใจว่า Cybersecurity ต้องมีพื้นฐาน Network ที่แข็งแรง  
และต้องฝึกวิเคราะห์ Log และ Incident จริง  

**สิ่งที่ต้องพัฒนาเพิ่มเติม**
- ฝึกทำ Lab Cybersecurity
- เรียนรู้ SIEM และ Log Analysis
- เตรียมสอบ Certificate
- พัฒนา Portfolio ด้าน Security
""")

st.markdown("</div>", unsafe_allow_html=True)
