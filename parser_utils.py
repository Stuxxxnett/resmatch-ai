# parser_utils.py

from PyPDF2 import PdfReader
import docx

def extract_text_from_pdf(file):
    reader = PdfReader(file)
    return "\n".join([page.extract_text() for page in reader.pages])

def extract_text_from_docx(file):
    doc = docx.Document(file)
    return "\n".join([para.text for para in doc.paragraphs])

def get_text_from_file(uploaded_file):
    if uploaded_file.name.endswith(".pdf"):
        return extract_text_from_pdf(uploaded_file)
    elif uploaded_file.name.endswith(".docx"):
        return extract_text_from_docx(uploaded_file)
    else:
        return "Unsupported file type"

# parser_utils.py

import PyPDF2

def get_text_from_file(uploaded_file):
    text = ""
    try:
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        for page in pdf_reader.pages:
            text += page.extract_text() + "\n"
        return text.strip()
    except Exception as e:
        return f"Error reading file: {e}"

import spacy

# Load spaCy model globally
nlp = spacy.load("en_core_web_sm")

# Define basic skill keywords (can be expanded later)
SKILL_KEYWORDS = [
    "python", "c++", "java", "machine learning", "deep learning",
    "public speaking", "teamwork", "communication", "data analysis",
    "problem solving", "sql", "pandas", "numpy", "linux"
]

def extract_keywords(text):
    doc = nlp(text.lower())
    extracted_skills = set()

    for token in doc:
        if token.text in SKILL_KEYWORDS:
            extracted_skills.add(token.text)

    return list(extracted_skills)

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(resume_keywords, jd_keywords):
    if not resume_keywords or not jd_keywords:
        return 0.0

    text_data = [" ".join(resume_keywords), " ".join(jd_keywords)]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(text_data)
    similarity_score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]

    return round(similarity_score * 100, 2)  # return as percentage


