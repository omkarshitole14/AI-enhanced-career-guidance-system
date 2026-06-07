roadmaps = {

    "Software Engineer": [

        "Learn Python",

        "Learn Data Structures",

        "Learn SQL",

        "Learn Git & GitHub",

        "Build Projects",

        "Apply for Jobs"
    ],

    "Data Scientist": [

        "Learn Python",

        "Learn Pandas",

        "Learn Statistics",

        "Learn Machine Learning",

        "Build ML Projects",

        "Apply for Data Science Roles"
    ],

    "Business Analyst": [

        "Learn Excel",

        "Learn SQL",

        "Learn Power BI",

        "Learn Data Visualization",

        "Create Dashboards",

        "Apply for BA Roles"
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