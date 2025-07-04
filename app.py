
from flask import Flask, render_template, request
from model_logic import classify_resume_and_recommend_jobs
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        experience = request.form.get('experience')
        skills = request.form.get('skills')
        resume_text = request.form.get('resume')

        if not resume_text.strip():
            return render_template('index.html', error="Please enter your resume.")

        try:
            top_jobs = classify_resume_and_recommend_jobs(resume_text)
            return render_template(
                'result.html',
                name=name,
                email=email,
                experience=experience,
                skills=skills,
                jobs=top_jobs
            )
        except Exception as e:
            return render_template('index.html', error=f"Error: {str(e)}")

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, port=port)