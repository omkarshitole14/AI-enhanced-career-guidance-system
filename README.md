# AI-Enhanced Career Guidance System

An end-to-end Machine Learning web application that recommends careers across 10 categories based on a user's education, skills, certifications, and CGPA. Built with Python, Flask, and Scikit-Learn, and deployed on AWS EC2 with resume storage on Amazon S3.

## Features
- Predicts suitable career paths using a Random Forest Classifier (98.67% accuracy)
- Parses uploaded PDF resumes to detect skills automatically
- Performs skill-gap analysis and generates a personalized learning roadmap
- Stores uploaded resumes securely in an AWS S3 bucket
- Deployed live on AWS EC2 using Gunicorn as the production server

## Tech Stack
- **Backend:** Python, Flask
- **Machine Learning:** Scikit-Learn, Pandas, Joblib
- **Resume Parsing:** PyPDF2
- **Cloud Services:** AWS EC2 (hosting), AWS S3 (resume storage), IAM (access management)
- **Deployment:** Gunicorn, Ubuntu (Linux)

## Project Structure
├── app.py                  # Main Flask application
├── train_model.py          # Trains the Random Forest model
├── generate_dataset.py     # Generates the training dataset
├── predict.py              # Career prediction logic
├── resume_parser.py        # Extracts text from PDF resumes
├── skill_gap.py             # Identifies missing skills for a career
├── career_roadmap.py       # Provides a learning roadmap per career
├── requirements.txt        # Python dependencies
├── dataset/                # Generated training dataset
├── model/                  # Saved trained ML model
└── templates/               # HTML templates (Flask views)

## How It Works
1. User submits education, specialization, skills, certifications, CGPA, and optionally uploads a resume (PDF)
2. The resume is parsed to auto-detect additional skills, and also uploaded to an AWS S3 bucket for storage
3. The trained ML model predicts the most suitable career path
4. The app shows the predicted career, confidence score, missing skills, and a personalized roadmap

## AWS Deployment
This application is deployed on an AWS EC2 instance (Ubuntu, t3.micro) using Gunicorn as the production WSGI server. Uploaded resumes are stored in an Amazon S3 bucket for durable, scalable cloud storage. Access is secured using IAM users with limited S3 permissions, and EC2 access is controlled via Security Groups (SSH on port 22, application on port 5000).

## Setup Instructions
```bash
git clone https://github.com/omkarshitole14/AI-enhanced-career-guidance-system.git
cd AI-enhanced-career-guidance-system
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 generate_dataset.py
python3 train_model.py
export AWS_ACCESS_KEY_ID='your-access-key'
export AWS_SECRET_ACCESS_KEY='your-secret-key'
python3 app.py
```

## Model Performance
- **Accuracy:** 98.67% on held-out test data
- **Algorithm:** Random Forest Classifier
- **Dataset:** 3,000-row synthetic dataset across 10 career categories

## Author
Omkar Shirish Shitole
