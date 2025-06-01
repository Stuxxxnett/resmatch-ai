# app.py

import streamlit as st
from parser_utils import get_text_from_file

st.title("📄 ResMatch AI - Resume Analyzer")

# --- Resume Upload ---
st.header("Upload Your Resume")
resume_file = st.file_uploader("Choose a PDF or DOCX resume", type=["pdf", "docx"])

# --- Job Description Input ---
st.header("Paste Job Description")
job_description = st.text_area("Enter the job description here", height=250)

# --- Trigger Text Extraction ---
if resume_file and job_description:
    resume_text = get_text_from_file(resume_file)

    st.subheader("✅ Extracted Resume Text")
    st.write(resume_text[:1000] + "...")  # Show first 1000 chars

    st.subheader("✅ Job Description Text")
    st.write(job_description[:1000] + "...")
