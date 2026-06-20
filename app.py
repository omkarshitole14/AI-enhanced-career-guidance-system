from flask import Flask, render_template, request
import os
import joblib
import pandas as pd
from resume_parser import extract_text_from_pdf
from skill_gap import find_missing_skills
from career_roadmap import get_roadmap

app = Flask(__name__)
os.makedirs("uploads/resumes", exist_ok=True)

UPLOAD_FOLDER = "uploads/resumes"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Load Trained Model
model = joblib.load("model/career_model.joblib")

# Skill Dictionary
ALL_SKILLS = [

    "Python",
    "Java",
    "SQL",
    "Machine Learning",
    "Deep Learning",
    "TensorFlow",
    "Pandas",
    "Statistics",
    "Power BI",
    "Excel",
    "Git",
    "GitHub",
    "DSA",
    "Linux",
    "Networking",
    "Security",
    "Communication"
]


def extract_skills(text):

    found_skills = []

    text = text.lower()

    for skill in ALL_SKILLS:

        if skill.lower() in text:
            found_skills.append(skill)

    return found_skills


def calculate_match_score(found_skills, missing_skills):

    total = len(found_skills) + len(missing_skills)

    if total == 0:
        return 0

    return round((len(found_skills) / total) * 100, 2)


@app.route("/")
def home():

    return render_template("index.html")


@app.route("/about")
def about():

    return render_template("about.html")


@app.route("/predict", methods=["POST"])
def predict():

    education = request.form["education"]

    specialization = request.form["specialization"]

    skills = request.form["skills"]

    certification = request.form["certification"]

    cgpa = float(request.form["cgpa"])

    resume_file = request.files["resume"]

    resume_text = ""

    detected_skills = []

    # Resume Upload
    if resume_file:

        filepath = os.path.join(
            app.config["UPLOAD_FOLDER"],
            resume_file.filename
        )

        resume_file.save(filepath)

        try:
            resume_text = extract_text_from_pdf(filepath)
            detected_skills = extract_skills(resume_text)
        except Exception as e:
            print("Resume parsing failed:", e)
            resume_text = ""
            detected_skills = []

    # User Input For Model
    input_data = {
        "Education Level": education,
        "Specialization": specialization,
        "Skills": skills,
        "Certifications": certification,
        "CGPA/Percentage": cgpa
    }
    #convert to DataFrame for model
    input_df = pd.DataFrame([input_data])

    print("Input Dataframe:")
    print(input_df)

    try:
        # predict career
        career = model.predict(input_df)[0]

        # Prediction Confidence
        confidence = round(
            max(model.predict_proba(input_df)[0]) * 100,
            2
        )
    except Exception as e:
        print("Prediction failed:", e)
        return render_template(
            "result.html",
            career="Unable to predict",
            confidence=0,
            score=0,
            skills=detected_skills,
            missing=[],
            roadmap=[]
        )

    print("Confidence:", confidence)
    # Missing Skills
    missing_skills = find_missing_skills(
        career,
        skills
    )

    # Match Score
    match_score = calculate_match_score(
        detected_skills,
        missing_skills
    )

    # Roadmap
    roadmap = get_roadmap(career)

    return render_template(
        "result.html",
        career=career,
        confidence=confidence,
        score=match_score,
        skills=detected_skills,
        missing=missing_skills,
        roadmap=roadmap
    )


if __name__ == "__main__":

    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000
    )
