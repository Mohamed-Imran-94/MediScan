import streamlit as st
import requests
from pdf2image import convert_from_bytes
import time

# ✅ Updated Poppler path
POPPLER_PATH = r"C:/poppler-24.08.0/Library/bin"
URL = "http://127.0.0.1:8000/extract_from_doc"

st.set_page_config(page_title="Medi Scan", layout="wide")
st.title("🩺 Medi Scan - PDF Text Extractor")

file = st.file_uploader("📄 Upload a medical PDF file", type="pdf")

col3, col4 = st.columns(2)

with col3:
    file_format = st.radio(
        label="Select the document type:",
        options=["prescription", "patient_details"],
        horizontal=True
    )

with col4:
    if file and st.button("📤 Upload PDF", type="primary"):
        bar = st.progress(50)
        time.sleep(1.5)
        bar.progress(100)

        payload = {'file_format': file_format}
        files = {'file': file.getvalue()}

        try:
            response = requests.post(URL, data=payload, files=files)
            if response.status_code == 200:
                data = response.json()
                for key, value in data.items():
                    st.session_state[key] = value
            else:
                st.error("❌ Failed to extract data from backend.")
        except Exception as e:
            st.error(f"⚠️ Request failed: {e}")

if file:
    pages = convert_from_bytes(file.getvalue(), poppler_path=POPPLER_PATH)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📑 Uploaded PDF Preview")
        st.image(pages[0], caption="Page 1 Preview")

    with col2:
        if st.session_state:
            st.subheader("🧾 Extracted Details")
            if file_format == "prescription":
                name = st.text_input("👤 Name", value=st.session_state.get("patient_name", ""))
                address = st.text_input("🏠 Address", value=st.session_state.get("patient_address", ""))
                medicines = st.text_input("💊 Medicines", value=st.session_state.get("medicines", ""))
                directions = st.text_input("📋 Directions", value=st.session_state.get("directions", ""))
                refill = st.text_input("🔁 Refill", value=st.session_state.get("refill", ""))

            elif file_format == "patient_details":
                name = st.text_input("👤 Name", value=st.session_state.get("patient_name", ""))
                phone = st.text_input("📞 Phone No.", value=st.session_state.get("phone_no", ""))
                vacc_status = st.text_input("💉 Hepatitis B Vaccination Status", value=st.session_state.get("vaccination_status", ""))
                med_problems = st.text_input("🧠 Medical Problems", value=st.session_state.get("medical_problems", ""))
                has_insurance = st.text_input("💼 Insurance Status", value=st.session_state.get("has_insurance", ""))

            if st.button("✅ Submit", type="primary"):
                for key in ["patient_name", "patient_address", "medicines", "directions", "refill",
                            "phone_no", "vaccination_status", "medical_problems", "has_insurance"]:
                    st.session_state.pop(key, None)
                st.success("✔️ Details successfully recorded.")
