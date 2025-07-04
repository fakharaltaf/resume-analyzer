import joblib
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Load model, vectorizer, and job database
model = joblib.load("resume_classifier_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")
jobs_df = pd.read_excel("all_jobs.xlsx")
jobs_df['cleaned_job'] = jobs_df['cleaned_description'].astype(str)
jobs_df['job_profile'] = jobs_df['title'] + " " + jobs_df['cleaned_job']

def clean_text(text):
    import re
    text = str(text).lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def classify_resume_and_recommend_jobs(resume_text):
    cleaned_resume = clean_text(resume_text)

    # Vectorized Resume
    resume_vec = vectorizer.transform([cleaned_resume])

    # Job matching using cosine similarity
    job_vecs = vectorizer.transform(jobs_df['job_profile'])
    similarity = cosine_similarity(resume_vec, job_vecs)
    top_indices = similarity[0].argsort()[-5:][::-1]

    top_jobs = jobs_df[['title', 'cleaned_description']].iloc[top_indices].to_dict('records')

    return top_jobs
