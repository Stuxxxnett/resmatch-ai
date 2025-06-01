# nlp_utils.py

import spacy

nlp = spacy.load("en_core_web_sm")

# Add more skills to this as needed
SKILLS_DB = [
    "python", "c++", "machine learning", "data analysis", "communication",
    "problem solving", "sql", "excel", "pandas", "deep learning",
    "tensorflow", "teamwork", "presentation", "project management"
]

def extract_skills(text):
    doc = nlp(text.lower())
    tokens = [token.text for token in doc if not token.is_stop and not token.is_punct]

    extracted = set()
    for skill in SKILLS_DB:
        if skill.lower() in tokens or skill.lower() in text.lower():
            extracted.add(skill.lower())

    return list(extracted)
