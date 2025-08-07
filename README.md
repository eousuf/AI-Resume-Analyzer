# AI-Based Resume Analyzer & Job Matcher

[cite_start]This project is an intelligent system that analyzes a user's resume and recommends relevant job opportunities[cite: 5]. [cite_start]It utilizes Natural Language Processing (NLP) and Machine Learning (ML) to make job matching more efficient[cite: 6].

## Project Structure

The project is organized into a modular structure for easier maintenance and scalability:

-   `app.py`: The main Streamlit application file for the user interface.
-   `modules/`: Contains the core Python logic separated into modules.
    -   [cite_start]`file_parser.py`: Functions to extract text from PDF and DOCX files[cite: 13].
    -   [cite_start]`text_processor.py`: Functions for text cleaning and skill extraction[cite: 16].
    -   [cite_start]`job_matcher.py`: The ML models for job-resume matching (TF-IDF and BERT)[cite: 19].
-   `data/`: Contains the job descriptions and skills lists.
-   `requirements.txt`: A list of all Python dependencies.

## Key Features

-   [cite_start]**Resume Upload & Parsing**: Supports PDF and DOCX formats[cite: 14].
-   [cite_start]**Skill Extraction**: Automatically identifies skills from the resume text[cite: 16, 18].
-   [cite_start]**Intelligent Job Matching**: Uses both keyword-based (TF-IDF) and semantic (BERT) models[cite: 21, 22].
-   [cite_start]**Match Score Display**: Shows top job matches with a percentage score and a skill breakdown[cite: 24, 25].

## Setup and Installation

1.  **Clone the repository.**

2.  **Install the required Python libraries:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Download NLP models:**
    ```bash
    python -m spacy download en_core_web_sm
    python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"
    ```

## How to Run the Application

1.  Ensure all dependencies and models are installed.
2.  Navigate to the root directory (`AI_Job_Matcher/`).
3.  Run the Streamlit application from your terminal:
    ```bash
    streamlit run app.py
    ```
4.  Your browser will open with the application running.