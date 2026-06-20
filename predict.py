import joblib
import pandas as pd

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

    input_df = pd.DataFrame([input_data])

    prediction = model.predict(input_df)

    return prediction[0]
