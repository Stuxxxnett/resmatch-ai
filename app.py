import streamlit as st
from parser_utils import get_text_from_file, extract_keywords, calculate_similarity
from nlp_utils import extract_skills
import plotly.graph_objects as go

st.title("📄 ResMatch AI - Resume Analyzer")

# --- Upload Resume ---
st.header("Upload Your Resume")
uploaded_file = st.file_uploader("Choose a PDF or DOCX resume", type=["pdf", "docx"])

# --- Job Description Input ---
st.header("Paste Job Description")
job_description = st.text_area("Enter the job description here", height=250)

# Only process when both are provided
if uploaded_file and job_description:
    resume_text = get_text_from_file(uploaded_file)
    jd_text = job_description

    # Show extracted text preview
    st.subheader("✅ Extracted Resume Text")
    st.write(resume_text[:1000] + "...")

    st.subheader("✅ Job Description Text")
    st.write(jd_text[:1000] + "...")

    # Extract skills
    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(jd_text)

    st.subheader("🧠 Resume Skills Extracted")
    st.write(resume_skills)

    st.subheader("📌 Job Description Skills Required")
    st.write(jd_skills)

    # Match Score (skill overlap)
    if jd_skills:
        match_score = round(len(set(resume_skills) & set(jd_skills)) / len(set(jd_skills)) * 100, 2)
        st.success(f"✅ **Match Score: {match_score}%**")

        missing_skills = list(set(jd_skills) - set(resume_skills))
        if missing_skills:
            st.warning(f"⚠️ Missing Skills: {', '.join(missing_skills)}")
        else:
            st.info("All required skills matched!")

    else:
        st.warning("No skills were extracted from the job description.")

    # Advanced Similarity
    resume_keywords = extract_keywords(resume_text)
    jd_keywords = extract_keywords(jd_text)

    score = calculate_similarity(resume_keywords, jd_keywords)
    st.subheader("🔍 Resume–JD Semantic Match Score")
    st.success(f"{score} %")

    if score > 75:
        st.info("✅ Great Match! Your resume aligns well.")
    elif score > 50:
        st.warning("🟡 Partial Match – consider adding missing skills.")
    else:
        st.error("🔴 Low Match – tailor your resume better.")

    # Visual Skill Comparison
    matched = list(set(resume_keywords) & set(jd_keywords))
    missing = list(set(jd_keywords) - set(resume_keywords))

    st.subheader("Matched Skills:")
    st.success(", ".join(matched) if matched else "None")

    st.subheader("Missing Skills from Resume:")
    st.error(", ".join(missing) if missing else "Great! You covered all keywords.")

    st.subheader("Match Percentage Visualization")
    st.progress(int(score))

    # Pie Chart
    labels = ['Match', 'Gap']
    values = [len(matched), len(missing)]
    fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])
    st.plotly_chart(fig)
