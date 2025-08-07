import streamlit as st
import pandas as pd

# Import functions from your modules
from modules.file_parser import extract_text_from_pdf, extract_text_from_docx
from modules.text_processor import preprocess_text, extract_skills, load_skills
from modules.job_matcher import tfidf_matching, semantic_matching

# --- Page Configuration ---
st.set_page_config(
    page_title="AI Job Matcher",
    page_icon="🤖",
    layout="wide"
)

# --- Load Data ---
@st.cache_data
def load_data():
    """Loads jobs and skills data."""
    jobs_df = pd.read_csv('data/jobs.csv')
    skills_list = load_skills('data/skills.txt')
    return jobs_df, skills_list

jobs_df, SKILLS_DB = load_data()

# --- Streamlit App Interface ---
st.title("🤖 AI-Powered Resume Analyzer & Smart Job Matcher")
st.markdown("""
Welcome to the smart job matching tool! This system analyzes your resume, identifies your skills, and recommends the most suitable job opportunities from our database.
Upload your resume below to get started.
""")

st.sidebar.header("Controls")
st.sidebar.info("This project uses Machine Learning (ML) and Natural Language Processing (NLP) to bridge the gap between job seekers and recruiters.")

# --- 1. Resume Upload ---
st.header("1. Upload Your Resume")
uploaded_file = st.file_uploader(
    "Choose a file (PDF or DOCX)",
    type=['pdf', 'docx'],
    help="Upload your resume to have it analyzed."
)

if uploaded_file is not None:
    # Extract text based on file type
    if uploaded_file.type == "application/pdf":
        resume_text = extract_text_from_pdf(uploaded_file)
    else:
        resume_text = extract_text_from_docx(uploaded_file)

    # --- 2. Resume Analysis ---
    st.header("2. Resume Analysis")
    with st.expander("View Extracted Resume Text"):
        st.text_area("Extracted Resume Content", resume_text, height=200, label_visibility="collapsed")

    preprocessed_resume = preprocess_text(resume_text)
    extracted_skills = extract_skills(resume_text, SKILLS_DB)
    st.write("**Your Extracted Skills:**")
    st.info(", ".join(extracted_skills) if extracted_skills else "No specific skills from our database were found.")

    # --- 3. Job Matching ---
    st.header("3. Job Matching Results")
    matching_method = st.sidebar.radio(
        "Choose a Matching Algorithm:",
        ('BERT Semantic Similarity', 'TF-IDF with Cosine Similarity'),
        help="BERT understands context better (recommended), while TF-IDF is faster and keyword-based."
    )

    # Preprocess job descriptions for TF-IDF
    job_descriptions_list = jobs_df['Description'].tolist()
    preprocessed_jobs = [preprocess_text(desc) for desc in job_descriptions_list]

    if matching_method == 'TF-IDF with Cosine Similarity':
        scores = tfidf_matching(preprocessed_resume, preprocessed_jobs) #
    else: # BERT Semantic Similarity
        scores = semantic_matching(preprocessed_resume, job_descriptions_list) #

    jobs_df['Match Score'] = scores
    # Convert score to a more intuitive percentage for display
    jobs_df['Match Percentage'] = (jobs_df['Match Score'] * 100).round(2)

    # Display top recommended jobs
    recommended_jobs = jobs_df.sort_values(by='Match Score', ascending=False).head(5)

    st.write(f"**Top {len(recommended_jobs)} Recommended Jobs (using {matching_method}):**")

    for index, row in recommended_jobs.iterrows():
        st.subheader(f"{row['Job Title']} - Match: {row['Match Percentage']}%")
        with st.expander("See Job Details & Skill Match Analysis"):
            st.markdown(f"**Description:** {row['Description']}")

            job_skills = extract_skills(row['Description'], SKILLS_DB)

            # Optional skill match breakdown
            matched_skills = list(set(extracted_skills) & set(job_skills))
            missing_skills = list(set(job_skills) - set(extracted_skills))

            st.markdown("**Skill Analysis:**")
            st.success(f"**✅ Your Matched Skills:** {', '.join(matched_skills) if matched_skills else 'None'}")
            st.warning(f"**❌ Skills You're Missing:** {', '.join(missing_skills) if missing_skills else 'None'}")

else:
    st.info("Please upload a resume to see job recommendations.")