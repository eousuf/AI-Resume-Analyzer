import re
import spacy
import nltk
import os

# --- START: New Hybrid Logic ---
# Define the path for the bundled NLTK data
_nltk_data_path = os.path.join(os.getcwd(), "nltk_data")

# Check if the bundled data exists. If so, add its path to NLTK.
if os.path.exists(_nltk_data_path):
    nltk.data.path.append(_nltk_data_path)
# If it doesn't exist (failsafe for cloud environment), download it.
else:
    nltk.download('punkt')
    nltk.download('stopwords')
# --- END: New Hybrid Logic ---

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# The rest of your code remains unchanged
nlp = spacy.load('en_core_web_sm')
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    """Cleans and preprocesses the text."""
    text = re.sub(r'[^a-zA-Z\s]', '', text, re.I | re.A)
    text = text.lower()
    tokens = word_tokenize(text)
    filtered_tokens = [word for word in tokens if word not in stop_words]
    return " ".join(filtered_tokens)

def extract_skills(text, skills_list):
    """Extracts skills from text based on a predefined list."""
    found_skills = set()
    for skill in skills_list:
        if " " in skill and re.search(r'\b' + re.escape(skill) + r'\b', text.lower()):
            found_skills.add(skill)
    doc = nlp(text.lower())
    for token in doc:
        if token.text in skills_list:
            found_skills.add(token.text)
    return list(found_skills)

def load_skills(skills_file_path):
    """Loads skills from a text file."""
    with open(skills_file_path, 'r') as f:
        skills = [line.strip().lower() for line in f]
    return skills