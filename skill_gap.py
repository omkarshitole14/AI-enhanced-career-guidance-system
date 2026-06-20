career_skills = {

    "Software Engineer": [
        "Python",
        "Java",
        "SQL",
        "Git",
        "DSA"
    ],

    "Data Analyst": [
        "Python",
        "SQL",
        "Excel",
        "Power BI",
        "Statistics"
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

    "ML Engineer": [
        "Python",
        "Deep Learning",
        "Machine Learning",
        "TensorFlow",
        "Pandas"
    ],

    "Research Scientist": [
        "Python",
        "Statistics",
        "Machine Learning"
    ],

    "Marketing Executive": [
        "SEO",
        "Sales",
        "Communication",
        "Digital Marketing"
    ],

    "Financial Analyst": [
        "Finance",
        "Excel",
        "Accounting",
        "Financial Modeling"
    ],

    "Junior Accountant": [
        "Accounting",
        "Tally",
        "GST",
        "Excel"
    ],

    "School Counselor": [
        "Counseling",
        "Communication",
        "Teaching"
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
