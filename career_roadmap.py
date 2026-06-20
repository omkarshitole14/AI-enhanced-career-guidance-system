roadmaps = {

    "Software Engineer": [
        "Learn Python",
        "Learn Data Structures",
        "Learn SQL",
        "Learn Git & GitHub",
        "Build Projects",
        "Apply for Jobs"
    ],

    "ML Engineer": [
        "Learn Python",
        "Learn Pandas",
        "Learn Statistics",
        "Learn Machine Learning & Deep Learning",
        "Build ML Projects",
        "Apply for ML Engineer Roles"
    ],

    "Data Analyst": [
        "Learn Excel",
        "Learn SQL",
        "Learn Power BI",
        "Learn Statistics",
        "Create Dashboards",
        "Apply for Data Analyst Roles"
    ],

    "Business Analyst": [
        "Learn Excel",
        "Learn SQL",
        "Learn Power BI",
        "Learn Data Visualization",
        "Create Dashboards",
        "Apply for BA Roles"
    ],

    "Research Scientist": [
        "Learn Python",
        "Learn Statistics",
        "Learn Machine Learning",
        "Read & Reproduce Research Papers",
        "Publish or Present Findings",
        "Apply for Research Roles"
    ],

    "Marketing Executive": [
        "Learn Digital Marketing Basics",
        "Learn SEO",
        "Learn Sales & Communication",
        "Run Sample Campaigns",
        "Build a Portfolio",
        "Apply for Marketing Roles"
    ],

    "Financial Analyst": [
        "Learn Excel",
        "Learn Accounting Basics",
        "Learn Financial Modeling",
        "Practice Valuation Case Studies",
        "Get Certified (e.g. Financial Modeling)",
        "Apply for Analyst Roles"
    ],

    "Junior Accountant": [
        "Learn Accounting Fundamentals",
        "Learn Tally",
        "Learn GST & Taxation Basics",
        "Learn Excel",
        "Get Certified (Tally)",
        "Apply for Accountant Roles"
    ],

    "School Counselor": [
        "Learn Counseling Fundamentals",
        "Develop Communication Skills",
        "Learn Child Psychology Basics",
        "Get Certified in Counseling",
        "Gain Internship Experience",
        "Apply for Counselor Roles"
    ],

    "Cyber Security Analyst": [
        "Learn Networking",
        "Learn Linux",
        "Learn Security Fundamentals",
        "Practice Ethical Hacking (Labs/CTFs)",
        "Get Certified (e.g. CCNA, CEH)",
        "Apply for Security Analyst Roles"
    ]
}


def get_roadmap(career):

    return roadmaps.get(
        career,
        [
            "Learn domain fundamentals",
            "Build practical projects",
            "Gain certifications",
            "Develop communication skills",
            "Apply for internships and jobs"
        ]
    )
