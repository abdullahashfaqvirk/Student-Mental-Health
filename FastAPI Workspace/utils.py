import pandas as pd


def get_input_features(x1, x2, x3):
    """
    x1 -> Personal Info
    x2 -> Educational Info
    x3 -> Stress Info
    """
    data = {
        "Gender": x1.gender,
        "Age": x1.age,
        "Degree Level": x2.degree_level,
        "Year": x2.year,
        "CGPA": x2.cgpa,
        "Residential Status": x2.residential_status,
        "Campus Mistreat": x2.mistreat,
        "Sports": x1.sports,
        "Sleep": x1.sleep,
        "Field Satisfaction": x2.field_satisfaction,
        "Uni Workload": x2.workload,
        "Academic Pressure": x2.academic_pressure,
        "Financial Pressure": x3.financial_pressure,
        "Campus Networking": x2.campus_networking,
        "Anxiety": x3.anxiety,
        "Isolation": x3.isolation,
        "Future Insecurity": x3.future_insecurity,
        "Stress Score": x3.stress_score
    }

    return pd.DataFrame(data, index=[0])
