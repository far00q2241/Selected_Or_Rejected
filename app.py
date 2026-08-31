import streamlit as st
import pandas as pd
import joblib

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Candidate Selection Prediction",
    page_icon="🎓",
    layout="wide"
)

# --------------------------------------------------
# LOAD MODEL
# --------------------------------------------------
model = joblib.load("selected_or_rejected_model.pkl")
feature_columns = joblib.load("feature_columns.pkl")

country_freq = joblib.load("country_freq.pkl")
city_freq = joblib.load("city_freq.pkl")
preferred_location_freq = joblib.load("preferred_location_freq.pkl")
technical_skills_freq = joblib.load("technical_skills_freq.pkl")
programming_languages_freq = joblib.load("programming_languages_freq.pkl")
frameworks_freq = joblib.load("frameworks_freq.pkl")
databases_freq = joblib.load("databases_freq.pkl")
cloud_platform_freq = joblib.load("cloud_platform_freq.pkl")
previous_companies_freq = joblib.load("previous_companies_freq.pkl")

# --------------------------------------------------
# LISTS
# --------------------------------------------------
education_levels = [
    "High School","Diploma","Bachelor","Master","PhD"
]

universities = [
    "Carnegie Mellon University","ETH Zurich",
    "Georgia Institute of Technology","Harvard University",
    "Imperial College London",
    "Massachusetts Institute of Technology",
    "National University of Singapore",
    "Stanford University","Tsinghua University",
    "University of California, Berkeley",
    "University of Cambridge",
    "University of Oxford",
    "University of Toronto",
    "University of Washington"
]

fields = [
    "Computer Science","Cyber Security","Data Science",
    "Electrical Engineering","Information Systems",
    "Information Technology","Mathematics & Statistics",
    "Software Engineering"
]

job_titles = [
    "Backend Developer","Business Analyst","Cloud Engineer",
    "Cyber Security Analyst","Data Scientist",
    "Database Administrator","DevOps Engineer",
    "Entry Level / Unemployed","Frontend Developer",
    "Full Stack Developer","Machine Learning Engineer",
    "Mobile App Developer","QA Engineer",
    "Software Engineer","UI UX Designer"
]

job_roles = job_titles[:-1]

certification_columns = [
    "AWS Certified Developer",
    "AWS Certified Solutions Architect",
    "Certified Information Systems Security Professional (CISSP)",
    "Certified Kubernetes Administrator (CKA)",
    "Google Cloud Professional Data Engineer",
    "HashiCorp Certified: Terraform Associate",
    "Microsoft Certified: Azure Fundamentals",
    "Oracle Certified Professional Java SE",
    "Project Management Professional (PMP)",
    "TensorFlow Developer Certificate",
    "Not Applicable"
]

education_map = {
    "High School":0,
    "Diploma":1,
    "Bachelor":2,
    "Master":3,
    "PhD":4
}

availability_map = {
    "Immediate":0,
    "15 Days":1,
    "30 Days":2,
    "60 Days":3,
    "90 Days":4
}

# --------------------------------------------------
# TITLE
# --------------------------------------------------
st.title("🎓 Candidate Selection Prediction")
st.write("Enter candidate details below to predict whether the candidate is likely to be **Selected** or **Rejected**.")

# --------------------------------------------------
# PERSONAL INFORMATION
# --------------------------------------------------
st.header("👤 Personal Information")

c1,c2,c3 = st.columns(3)

with c1:
    age = st.number_input("Age",18,70,25)

with c2:
    gender = st.selectbox("Gender",["Female","Male","Other"])

with c3:
    country = st.selectbox(
        "Country",
        sorted(country_freq.index.tolist())
    )

c1,c2 = st.columns(2)

with c1:
    city = st.selectbox(
        "City",
        sorted(city_freq.index.tolist())
    )

with c2:
    preferred_location = st.selectbox(
        "Preferred Location",
        sorted(preferred_location_freq.index.tolist())
    )

# --------------------------------------------------
# EDUCATION
# --------------------------------------------------
st.header("🎓 Education")

c1,c2,c3 = st.columns(3)

with c1:
    highest_education = st.selectbox("Highest Education",education_levels)

with c2:
    university = st.selectbox("University",universities)

with c3:
    field_of_study = st.selectbox("Field of Study",fields)

c1,c2 = st.columns(2)

with c1:
    graduation_year = st.number_input("Graduation Year",1980,2035,2024)

with c2:
    cgpa = st.number_input("CGPA",0.0,10.0,7.5)

# --------------------------------------------------
# EXPERIENCE
# --------------------------------------------------
st.header("💼 Experience")

c1,c2,c3 = st.columns(3)

with c1:
    experience_years = st.number_input("Experience (Years)",0,50,2)

with c2:
    projects_completed = st.number_input("Projects Completed",0,100,5)

with c3:
    publications = st.number_input("Publications",0,50,0)

c1,c2 = st.columns(2)

with c1:
    current_job_title = st.selectbox("Current Job Title",job_titles)

with c2:
    job_role = st.selectbox("Job Role",job_roles)

# --------------------------------------------------
# SKILLS
# --------------------------------------------------
st.header("🛠️ Skills")

technical_skills = st.selectbox(
    "Technical Skills",
    sorted(technical_skills_freq.index.tolist())
)

programming_languages = st.selectbox(
    "Programming Languages",
    sorted(programming_languages_freq.index.tolist())
)

frameworks = st.selectbox(
    "Frameworks",
    sorted(frameworks_freq.index.tolist())
)

databases = st.selectbox(
    "Databases",
    sorted(databases_freq.index.tolist())
)

cloud_platform = st.selectbox(
    "Cloud Platform",
    sorted(cloud_platform_freq.index.tolist())
)

# --------------------------------------------------
# CERTIFICATIONS
# --------------------------------------------------
st.header("🏆 Certifications")

certifications = st.multiselect(
    "Select Certifications",
    certification_columns
)

# --------------------------------------------------
# SCORES
# --------------------------------------------------
st.header("📊 Candidate Scores")

communication_score = st.slider("Communication Score",0,100,70)
problem_solving_score = st.slider("Problem Solving Score",0,100,70)
technical_test_score = st.slider("Technical Test Score",0,100,70)
interview_score = st.slider("Interview Score",0,100,70)
aptitude_score = st.slider("Aptitude Score",0,100,70)
resume_quality_score = st.slider("Resume Quality Score",0,100,70)

# --------------------------------------------------
# RESUME
# --------------------------------------------------
st.header("📄 Resume Information")

resume_length = st.number_input("Resume Length",0,10000,1200)
keyword_match_percentage = st.slider("Keyword Match Percentage",0,100,75)
ats_score = st.slider("ATS Score",0,100,80)

# --------------------------------------------------
# JOB INFORMATION
# --------------------------------------------------
st.header("💰 Job Information")

expected_salary = st.number_input("Expected Salary",0,10000000,600000)

availability = st.selectbox(
    "Availability",
    list(availability_map.keys())
)

employment_type = st.selectbox(
    "Employment Type",
    ["Full-Time","Internship","Part-Time"]
)

remote_preference = st.selectbox(
    "Remote Preference",
    ["On-site","Remote"]
)

# --------------------------------------------------
# ADDITIONAL EXPERIENCE
# --------------------------------------------------
st.header("⭐ Additional Experience")

internship_experience = st.radio(
    "Internship Experience",
    ["Yes","No"]
)

leadership_experience = st.radio(
    "Leadership Experience",
    ["Yes","No"]
)

# --------------------------------------------------
# PREDICTION
# --------------------------------------------------
if st.button("🔮 Predict Candidate Selection", use_container_width=True):

    input_data = {}

    # Numeric
    input_data.update({
        "age": age,
        "highest_education": education_map[highest_education],
        "cgpa": cgpa,
        "graduation_year": graduation_year,
        "experience_years": experience_years,
        "projects_completed": projects_completed,
        "publications": publications,
        "communication_score": communication_score,
        "problem_solving_score": problem_solving_score,
        "technical_test_score": technical_test_score,
        "interview_score": interview_score,
        "aptitude_score": aptitude_score,
        "expected_salary": expected_salary,
        "availability": availability_map[availability],
        "resume_quality_score": resume_quality_score,
        "resume_length": resume_length,
        "keyword_match_percentage": keyword_match_percentage,
        "ats_score": ats_score,
        "full_name_freq":1,
        "country_freq": country_freq.get(country,0),
        "city_freq": city_freq.get(city,0),
        "preferred_location_freq": preferred_location_freq.get(preferred_location,0),
        "previous_companies_freq":0,
        "technical_skills_freq": technical_skills_freq.get(technical_skills,0),
        "programming_languages_freq": programming_languages_freq.get(programming_languages,0),
        "frameworks_freq": frameworks_freq.get(frameworks,0),
        "databases_freq": databases_freq.get(databases,0),
        "cloud_platform_freq": cloud_platform_freq.get(cloud_platform,0),
    })

    # Gender
    input_data["gender_Male"] = int(gender=="Male")
    input_data["gender_Other"] = int(gender=="Other")

    # University
    for uni in universities:
        input_data[f"university_{uni}"] = int(university==uni)

    # Field
    for field in fields:
        input_data[f"field_of_study_{field}"] = int(field_of_study==field)

    # Current Job
    for title in job_titles:
        input_data[f"current_job_title_{title}"] = int(current_job_title==title)

    # Job Role
    for role in job_roles:
        input_data[f"job_role_{role}"] = int(job_role==role)

    # Certifications
    for cert in certification_columns:
        input_data[cert] = int(cert in certifications)

    # Internship & Leadership
    input_data["internship_experience_Yes"] = int(internship_experience=="Yes")
    input_data["leadership_experience_Yes"] = int(leadership_experience=="Yes")

    # Employment
    for emp in ["Full-Time","Internship","Part-Time"]:
        input_data[f"employment_type_{emp}"] = int(employment_type==emp)

    # Remote
    input_data["remote_preference_On-site"] = int(remote_preference=="On-site")
    input_data["remote_preference_Remote"] = int(remote_preference=="Remote")

    # Match training columns
    input_df = pd.DataFrame([input_data]).reindex(
        columns=feature_columns,
        fill_value=0
    )

    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0]

    selected_prob = probability[1] * 100
    rejected_prob = probability[0] * 100

    st.divider()
    st.subheader("📊 Prediction Result")

    if prediction == 1:
        st.success("✅ Candidate is likely to be SELECTED")
    else:
        st.error("❌ Candidate is likely to be REJECTED")

    c1,c2 = st.columns(2)

    c1.metric("Selected Probability", f"{selected_prob:.2f}%")
    c2.metric("Rejected Probability", f"{rejected_prob:.2f}%")

    st.progress(int(selected_prob))
