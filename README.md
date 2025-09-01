# Resume & Skill Gap Analyzer

A Flask-based machine learning web app that classifies resumes and recommends jobs based on skill matching using cosine similarity and NLP.

---

## Features

- Upload and analyze resume text
- Predict the category (e.g., Aviation, Software)
- Recommend matching job descriptions
- Built using Flask, scikit-learn, and pandas

---

## Folder Structure

resume-skill-gap-analyzer/
├── app.py
├── model_logic.py
├── proj.ipynb
├── resume_classifier_model.pkl
├── tfidf_vectorizer.pkl
├── Resume.csv (ignored)
├── all_jobs.xlsx (ignored)
├── requirements.txt
├── README.md
├── .gitignore
├── templates/
│ ├── index.html
│ └── result.html
└── venv/ (ignored)


---

## Setup Instructions

1. Clone this repository:

```bash
git clone https://github.com/AliRash33d/ResumeAnalyzer.git
cd resume-skill-gap-analyzer

---

2. Create and activate virtual environment:
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

---

3. Install dependencies:
```bash
pip install -r requirements.txt

---

4. Add missing files manually (not tracked by Git):
Resume.csv

all_jobs.xlsx

resume_classifier_model.pkl

tfidf_vectorizer.pkl

---

5. Run the Flask app:
```bash
python app.py

---


6. Visit: http://127.0.0.1:5000
