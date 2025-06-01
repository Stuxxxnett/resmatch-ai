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

from nlp_utils import extract_skills

resume_skills = extract_skills(resume_text)
jd_skills = extract_skills(job_description)

match_score = round(len(set(resume_skills) & set(jd_skills)) / len(set(jd_skills)) * 100, 2)

st.subheader("🧠 Resume Skills Extracted")
st.write(resume_skills)

st.subheader("📌 Job Description Skills Required")
st.write(jd_skills)

st.success(f"✅ **Match Score: {match_score}%**")

missing = list(set(jd_skills) - set(resume_skills))
if missing:
    st.warning(f"⚠️ Missing Skills: {', '.join(missing)}")
else:
    st.info("All required skills matched!")

from parser_utils import get_text_from_file, extract_keywords

if uploaded_file is not None:
    resume_text = get_text_from_file(uploaded_file)
    st.text_area("Extracted Resume Text", resume_text, height=300)

    skills = extract_keywords(resume_text)
    st.subheader("Matched Skills:")
    st.write(", ".join(skills))

st.subheader("Paste the Job Description")
job_description = st.text_area("Job Description", height=200)

if job_description:
    jd_keywords = extract_keywords(job_description)
    st.subheader("Extracted JD Keywords:")
    st.write(", ".join(jd_keywords))

from parser_utils import calculate_similarity

if resume_text and job_description:
    score = calculate_similarity(skills, jd_keywords)
    st.subheader("Resume–JD Match Score:")
    st.success(f"{score} %")

    if score > 75:
        st.info("✅ Great Match! Your resume aligns well.")
    elif score > 50:
        st.warning("🟡 Partial Match – consider adding missing skills.")
    else:
        st.error("🔴 Low Match – tailor your resume better.")



