import joblib

# Load Model
model = joblib.load("model/career_model.joblib")


def predict_career(
        education,
        specialization,
        skills,
        certification,
        cgpa):

    input_data = {
        "Education Level": education,
        "Specialization": specialization,
        "Skills": skills,
        "Certifications": certification,
        "CGPA/Percentage": cgpa
    }

    prediction = model.predict([input_data])

    return prediction[0]