import pandas as pd
import random

careers = {
    "Software Engineer": {
        "specializations": ["Computer Science", "Information Technology"],
        "skills": ["Python", "Java", "SQL", "Git", "DSA"],
        "certifications": ["AWS", "Azure", "Python Certification"]
    },

    "ML Engineer": {
        "specializations": ["Computer Science", "Data Science", "AI"],
        "skills": ["Python", "Machine Learning", "Deep Learning", "TensorFlow", "Pandas"],
        "certifications": ["Machine Learning Certification", "AWS"]
    },

    "Data Analyst": {
        "specializations": ["Data Science", "Statistics"],
        "skills": ["SQL", "Excel", "Power BI", "Python", "Statistics"],
        "certifications": ["Google Data Analytics"]
    },

    "Business Analyst": {
        "specializations": ["Business Analytics", "Management"],
        "skills": ["Excel", "SQL", "Power BI", "Communication"],
        "certifications": ["Google Data Analytics"]
    },

    "Research Scientist": {
        "specializations": ["Research", "Stastistics"],
        "skills": ["Python", "Statistics", "Machine Learning", "Research"],
        "certifications": ["Research science Certification"]
    },

    "Marketing Executive": {
        "specializations": ["Marketing"],
        "skills": ["SEO", "Sales", "Communication", "Digital Marketing"],
        "certifications": ["Digital Marketing Certification"]
    },

    "Financial Analyst": {
        "specializations": ["Finance"],
        "skills": ["Finance", "Excel", "Accounting", "Financial Modeling"],
        "certifications": ["Financial Analysis Certification"]
    },

    "Junior Accountant": {
        "specializations": ["Commerce"],
        "skills": ["Accounting", "Tally", "GST", "Excel"],
        "certifications": ["Tally Certification"]
    },

    "School Counselor": {
        "specializations": ["Psychology"],
        "skills": ["Counseling", "Communication", "Teaching"],
        "certifications": ["Counseling Certification"]
    },

    "Cyber Security Analyst": {
        "specializations": ["Cyber Security"],
        "skills": ["Networking", "Linux", "Security", "Ethical Hacking"],
        "certifications": ["CCNA"]
    }
}

education_levels = [
    "Bachelor's",
    "Master's",
    "PhD"
]

rows = []

for career, info in careers.items():

    for _ in range(300):

        education = random.choice(education_levels)

        specialization = random.choice(
            info["specializations"]
        )

        selected_skills = random.sample(
            info["skills"],
            min(4, len(info["skills"]))
        )

        certification = random.choice(
            info["certifications"]
        )

        cgpa = round(
            random.uniform(6.5, 9.8),
            2
        )

        rows.append([
            education,
            specialization,
            ", ".join(selected_skills),
            certification,
            cgpa,
            career
        ])

df = pd.DataFrame(
    rows,
    columns=[
        "Education Level",
        "Specialization",
        "Skills",
        "Certifications",
        "CGPA/Percentage",
        "Recommended Career"
    ]
)

df.to_csv(
    "career_dataset_realistic.csv",
    index=False
)

print("Dataset Generated Successfully")
print("Rows:", len(df))