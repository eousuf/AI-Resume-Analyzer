from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer, util

# Load the model only once
model = SentenceTransformer('all-MiniLM-L6-v2')

def tfidf_matching(resume_text, job_descriptions):
    """Matches resume to jobs using TF-IDF and Cosine Similarity."""
    vectorizer = TfidfVectorizer(stop_words='english')
    # Combine resume and job descriptions for a shared vocabulary
    all_texts = [resume_text] + job_descriptions
    tfidf_matrix = vectorizer.fit_transform(all_texts)
    # Calculate similarity between the resume (first doc) and all jobs (the rest)
    cosine_sim = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:])
    return cosine_sim.flatten()

def semantic_matching(resume_text, job_descriptions):
    """Matches resume to jobs using Sentence Transformers for semantic similarity."""
    resume_embedding = model.encode(resume_text, convert_to_tensor=True)
    job_embeddings = model.encode(job_descriptions, convert_to_tensor=True)
    cosine_scores = util.pytorch_cos_sim(resume_embedding, job_embeddings)
    return cosine_scores.flatten().cpu().numpy()