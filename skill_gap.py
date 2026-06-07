career_skills = {

    "Software Engineer": [
        "Python",
        "Java",
        "SQL",
        "Git",
        "DSA"
    ],

    "Data Scientist": [
        "Python",
        "Machine Learning",
        "Pandas",
        "Statistics",
        "SQL"
    ],

    "Business Analyst": [
        "Excel",
        "Power BI",
        "SQL",
        "Communication"
    ],

    "Cyber Security Analyst": [
        "Networking",
        "Linux",
        "Security",
        "Python"
    ],

    "AI Engineer": [
        "Python",
        "Deep Learning",
        "Machine Learning",
        "TensorFlow"
    ]
}


def find_missing_skills(career, user_skills):

    required = career_skills.get(career, [])

    user_skills = [
        skill.strip().lower()
        for skill in user_skills.split(",")
    ]

    missing = []

    for skill in required:

        if skill.lower() not in user_skills:
            missing.append(skill)

    return missing