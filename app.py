import streamlit as st
import pandas as pd
import joblib


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Candidate Selection Prediction",
    page_icon="🎓",
    layout="wide"
)


# =========================================================
# LOAD MODEL AND FILES
# =========================================================

model = joblib.load("selected_or_reject_model.pkl")

feature_columns = joblib.load("feature_columns.pkl")

country_freq = joblib.load("country_freq.pkl")
city_freq = joblib.load("city_freq.pkl")
previous_companies_freq = joblib.load(
    "previous_companies_freq.pkl"
)
technical_skills_freq = joblib.load(
    "technical_skills_freq.pkl"
)
programming_languages_freq = joblib.load(
    "programming_languages_freq.pkl"
)
frameworks_freq = joblib.load(
    "frameworks_freq.pkl"
)
databases_freq = joblib.load(
    "databases_freq.pkl"
)
cloud_platform_freq = joblib.load(
    "cloud_platform_freq.pkl"
)
preferred_location_freq = joblib.load(
    "preferred_location_freq.pkl"
)


# =========================================================
# TITLE
# =========================================================

st.title("🎓 Candidate Selection Prediction")

st.write(
    "Enter the candidate details below to predict whether "
    "the candidate is likely to be Selected or Rejected."
)

st.divider()


# =========================================================
# PERSONAL INFORMATION
# =========================================================

st.header("👤 Personal Information")

col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input(
        "Age",
        min_value=18,
        max_value=70,
        value=25,
        step=1
    )

with col2:
    gender = st.selectbox(
        "Gender",
        ["Female", "Male", "Other"]
    )

with col3:
    country = st.text_input(
        "Country",
        value="India"
    )

col1, col2 = st.columns(2)

with col1:
    city = st.text_input(
        "City",
        value="Hyderabad"
    )

with col2:
    preferred_location = st.text_input(
        "Preferred Location",
        value="Flexible"
    )


# =========================================================
# EDUCATION
# =========================================================

st.header("🎓 Education")

col1, col2, col3 = st.columns(3)

with col1:
    highest_education = st.selectbox(
        "Highest Education",
        [
            "High School",
            "Diploma",
            "Bachelor",
            "Master",
            "PhD"
        ]
    )

with col2:
    field_of_study = st.selectbox(
        "Field of Study",
        [
            "Computer Science",
            "Cyber Security",
            "Data Science",
            "Electrical Engineering",
            "Information Systems",
            "Information Technology",
            "Mathematics & Statistics",
            "Software Engineering"
        ]
    )

with col3:
    graduation_year = st.number_input(
        "Graduation Year",
        min_value=1980,
        max_value=2030,
        value=2024,
        step=1
    )

cgpa = st.number_input(
    "CGPA",
    min_value=0.0,
    max_value=10.0,
    value=7.0,
    step=0.1
)


# =========================================================
# EXPERIENCE
# =========================================================

st.header("💼 Experience")

col1, col2, col3 = st.columns(3)

with col1:
    experience_years = st.number_input(
        "Experience (Years)",
        min_value=0,
        max_value=50,
        value=2,
        step=1
    )

with col2:
    projects_completed = st.number_input(
        "Projects Completed",
        min_value=0,
        max_value=100,
        value=5,
        step=1
    )

with col3:
    publications = st.number_input(
        "Publications",
        min_value=0,
        max_value=100,
        value=0,
        step=1
    )

col1, col2 = st.columns(2)

with col1:
    current_job_title = st.selectbox(
        "Current Job Title",
        [
            "Backend Developer",
            "Business Analyst",
            "Cloud Engineer",
            "Cyber Security Analyst",
            "Data Scientist",
            "Database Administrator",
            "DevOps Engineer",
            "Entry Level / Unemployed",
            "Frontend Developer",
            "Full Stack Developer",
            "Machine Learning Engineer",
            "Mobile App Developer",
            "QA Engineer",
            "Software Engineer",
            "UI UX Designer"
        ]
    )

with col2:
    job_role = st.selectbox(
        "Job Role",
        [
            "Backend Developer",
            "Business Analyst",
            "Cloud Engineer",
            "Cyber Security Analyst",
            "Data Scientist",
            "Database Administrator",
            "DevOps Engineer",
            "Frontend Developer",
            "Full Stack Developer",
            "Machine Learning Engineer",
            "Mobile App Developer",
            "QA Engineer",
            "Software Engineer",
            "UI UX Designer"
        ]
    )


# =========================================================
# SKILLS
# =========================================================

st.header("🛠️ Skills")

technical_skills = st.text_input(
    "Technical Skills",
    value="Python"
)

programming_languages = st.text_input(
    "Programming Languages",
    value="Python"
)

frameworks = st.text_input(
    "Frameworks",
    value="Scikit-learn"
)

databases = st.text_input(
    "Databases",
    value="MySQL"
)

cloud_platform = st.text_input(
    "Cloud Platform",
    value="AWS"
)


# =========================================================
# CERTIFICATIONS
# =========================================================

st.header("🏆 Certifications")

certifications = st.multiselect(
    "Select Certifications",
    [
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
)


# =========================================================
# PROFESSIONAL SCORES
# =========================================================

st.header("📊 Candidate Scores")

col1, col2, col3 = st.columns(3)

with col1:
    communication_score = st.number_input(
        "Communication Score",
        min_value=0.0,
        max_value=100.0,
        value=70.0
    )

with col2:
    problem_solving_score = st.number_input(
        "Problem Solving Score",
        min_value=0.0,
        max_value=100.0,
        value=70.0
    )

with col3:
    technical_test_score = st.number_input(
        "Technical Test Score",
        min_value=0.0,
        max_value=100.0,
        value=70.0
    )

col1, col2, col3 = st.columns(3)

with col1:
    interview_score = st.number_input(
        "Interview Score",
        min_value=0.0,
        max_value=100.0,
        value=70.0
    )

with col2:
    aptitude_score = st.number_input(
        "Aptitude Score",
        min_value=0.0,
        max_value=100.0,
        value=70.0
    )

with col3:
    resume_quality_score = st.number_input(
        "Resume Quality Score",
        min_value=0.0,
        max_value=100.0,
        value=70.0
    )


# =========================================================
# RESUME INFORMATION
# =========================================================

st.header("📄 Resume Information")

col1, col2, col3 = st.columns(3)

with col1:
    resume_length = st.number_input(
        "Resume Length",
        min_value=0,
        max_value=10000,
        value=1000,
        step=1
    )

with col2:
    keyword_match_percentage = st.number_input(
        "Keyword Match Percentage",
        min_value=0.0,
        max_value=100.0,
        value=70.0
    )

with col3:
    ats_score = st.number_input(
        "ATS Score",
        min_value=0.0,
        max_value=100.0,
        value=70.0
    )


# =========================================================
# JOB INFORMATION
# =========================================================

st.header("💰 Job Information")

col1, col2 = st.columns(2)

with col1:
    expected_salary = st.number_input(
        "Expected Salary",
        min_value=0.0,
        value=50000.0,
        step=1000.0
    )

with col2:
    availability = st.selectbox(
        "Availability",
        [
            "Immediate",
            "15 Days",
            "30 Days",
            "60 Days",
            "90 Days"
        ]
    )

col1, col2 = st.columns(2)

with col1:
    employment_type = st.selectbox(
        "Employment Type",
        [
            "Full-Time",
            "Internship",
            "Part-Time"
        ]
    )

with col2:
    remote_preference = st.selectbox(
        "Remote Preference",
        [
            "On-site",
            "Remote"
        ]
    )


# =========================================================
# EXPERIENCE FLAGS
# =========================================================

st.header("⭐ Additional Experience")

col1, col2 = st.columns(2)

with col1:
    internship_experience = st.selectbox(
        "Internship Experience",
        ["Yes", "No"]
    )

with col2:
    leadership_experience = st.selectbox(
        "Leadership Experience",
        ["Yes", "No"]
    )


# =========================================================
# ENCODING
# =========================================================

education_map = {
    "High School": 0,
    "Diploma": 1,
    "Bachelor": 2,
    "Master": 3,
    "PhD": 4
}

availability_map = {
    "Immediate": 0,
    "15 Days": 1,
    "30 Days": 2,
    "60 Days": 3,
    "90 Days": 4
}


# =========================================================
# PREDICTION
# =========================================================

st.divider()

if st.button(
    "🔮 Predict Candidate Selection",
    use_container_width=True
):

    # ---------------------------------------------
    # Frequency encoding
    # ---------------------------------------------

    country_frequency = country_freq.get(country, 0)
    city_frequency = city_freq.get(city, 0)

    previous_companies_frequency = (
        previous_companies_freq.get("", 0)
    )

    technical_skills_frequency = (
        technical_skills_freq.get(
            technical_skills,
            0
        )
    )

    programming_languages_frequency = (
        programming_languages_freq.get(
            programming_languages,
            0
        )
    )

    frameworks_frequency = (
        frameworks_freq.get(
            frameworks,
            0
        )
    )

    databases_frequency = (
        databases_freq.get(
            databases,
            0
        )
    )

    cloud_platform_frequency = (
        cloud_platform_freq.get(
            cloud_platform,
            0
        )
    )

    preferred_location_frequency = (
        preferred_location_freq.get(
            preferred_location,
            0
        )
    )


    # ---------------------------------------------
    # Create initial input dictionary
    # ---------------------------------------------

    input_data = {

        "age": age,

        "highest_education":
            education_map[highest_education],

        "cgpa": cgpa,

        "graduation_year":
            graduation_year,

        "experience_years":
            experience_years,

        "projects_completed":
            projects_completed,

        "publications":
            publications,

        "communication_score":
            communication_score,

        "problem_solving_score":
            problem_solving_score,

        "technical_test_score":
            technical_test_score,

        "interview_score":
            interview_score,

        "aptitude_score":
            aptitude_score,

        "expected_salary":
            expected_salary,

        "availability":
            availability_map[availability],

        "resume_quality_score":
            resume_quality_score,

        "resume_length":
            resume_length,

        "keyword_match_percentage":
            keyword_match_percentage,

        "ats_score":
            ats_score,

        "full_name_freq": 1,

        "country_freq":
            country_frequency,

        "city_freq":
            city_frequency,

        "previous_companies_freq":
            previous_companies_frequency,

        "technical_skills_freq":
            technical_skills_frequency,

        "programming_languages_freq":
            programming_languages_frequency,

        "frameworks_freq":
            frameworks_frequency,

        "databases_freq":
            databases_frequency,

        "cloud_platform_freq":
            cloud_platform_frequency,

        "preferred_location_freq":
            preferred_location_frequency
    }


    # ---------------------------------------------
    # Certification columns
    # ---------------------------------------------

    certification_columns = [
        "AWS Certified Developer",
        "AWS Certified Solutions Architect",
        "Certified Information Systems Security Professional (CISSP)",
        "Certified Kubernetes Administrator (CKA)",
        "Google Cloud Professional Data Engineer",
        "HashiCorp Certified: Terraform Associate",
        "Microsoft Certified: Azure Fundamentals",
        "Not Applicable",
        "Oracle Certified Professional Java SE",
        "Project Management Professional (PMP)",
        "TensorFlow Developer Certificate"
    ]

    for cert in certification_columns:

        input_data[cert] = (
            1 if cert in certifications else 0
        )


    # ---------------------------------------------
    # Gender
    # ---------------------------------------------

    input_data["gender_Male"] = (
        1 if gender == "Male" else 0
    )

    input_data["gender_Other"] = (
        1 if gender == "Other" else 0
    )


    # ---------------------------------------------
    # University columns
    # ---------------------------------------------

    university_columns = [
        "Carnegie Mellon University",
        "ETH Zurich",
        "Georgia Institute of Technology",
        "Harvard University",
        "Imperial College London",
        "Massachusetts Institute of Technology",
        "National University of Singapore",
        "Stanford University",
        "Tsinghua University",
        "University of California, Berkeley",
        "University of Cambridge",
        "University of Oxford",
        "University of Toronto",
        "University of Washington"
    ]

    # University was not included as an input above.
    # Therefore all university columns are initialized to 0.

    for university in university_columns:

        column_name = (
            "university_" + university
        )

        input_data[column_name] = 0


    # ---------------------------------------------
    # Field of study
    # ---------------------------------------------

    field_columns = [
        "Computer Science",
        "Cyber Security",
        "Data Science",
        "Electrical Engineering",
        "Information Systems",
        "Information Technology",
        "Mathematics & Statistics",
        "Software Engineering"
    ]

    for field in field_columns:

        column_name = (
            "field_of_study_" + field
        )

        input_data[column_name] = (
            1 if field_of_study == field else 0
        )


    # ---------------------------------------------
    # Current Job Title
    # ---------------------------------------------

    job_title_columns = [
        "Backend Developer",
        "Business Analyst",
        "Cloud Engineer",
        "Cyber Security Analyst",
        "Data Scientist",
        "Database Administrator",
        "DevOps Engineer",
        "Entry Level / Unemployed",
        "Frontend Developer",
        "Full Stack Developer",
        "Machine Learning Engineer",
        "Mobile App Developer",
        "QA Engineer",
        "Software Engineer",
        "UI UX Designer"
    ]

    for title in job_title_columns:

        column_name = (
            "current_job_title_" + title
        )

        input_data[column_name] = (
            1 if current_job_title == title else 0
        )


    # ---------------------------------------------
    # Job Role
    # ---------------------------------------------

    role_columns = [
        "Backend Developer",
        "Business Analyst",
        "Cloud Engineer",
        "Cyber Security Analyst",
        "Data Scientist",
        "Database Administrator",
        "DevOps Engineer",
        "Frontend Developer",
        "Full Stack Developer",
        "Machine Learning Engineer",
        "Mobile App Developer",
        "QA Engineer",
        "Software Engineer",
        "UI UX Designer"
    ]

    for role in role_columns:

        column_name = (
            "job_role_" + role
        )

        input_data[column_name] = (
            1 if job_role == role else 0
        )


    # ---------------------------------------------
    # Internship and Leadership
    # ---------------------------------------------

    input_data[
        "internship_experience_Yes"
    ] = (
        1 if internship_experience == "Yes"
        else 0
    )

    input_data[
        "leadership_experience_Yes"
    ] = (
        1 if leadership_experience == "Yes"
        else 0
    )


    # ---------------------------------------------
    # Employment Type
    # ---------------------------------------------

    input_data[
        "employment_type_Full-Time"
    ] = (
        1 if employment_type == "Full-Time"
        else 0
    )

    input_data[
        "employment_type_Internship"
    ] = (
        1 if employment_type == "Internship"
        else 0
    )

    input_data[
        "employment_type_Part-Time"
    ] = (
        1 if employment_type == "Part-Time"
        else 0
    )


    # ---------------------------------------------
    # Remote Preference
    # ---------------------------------------------

    input_data[
        "remote_preference_On-site"
    ] = (
        1 if remote_preference == "On-site"
        else 0
    )

    input_data[
        "remote_preference_Remote"
    ] = (
        1 if remote_preference == "Remote"
        else 0
    )


    # =========================================================
    # CREATE DATAFRAME
    # =========================================================

    input_df = pd.DataFrame([input_data])


    # =========================================================
    # ENSURE EXACT TRAINING COLUMNS
    # =========================================================

    input_df = input_df.reindex(
        columns=feature_columns,
        fill_value=0
    )


    # =========================================================
    # PREDICTION
    # =========================================================

    prediction = model.predict(input_df)[0]

    probability = model.predict_proba(
        input_df
    )[0]


    selected_probability = probability[1] * 100
    rejected_probability = probability[0] * 100


    # =========================================================
    # DISPLAY RESULT
    # =========================================================

    st.subheader("📊 Prediction Result")

    if prediction == 1:

        st.success(
            "✅ Candidate is likely to be SELECTED"
        )

    else:

        st.error(
            "❌ Candidate is likely to be REJECTED"
        )


    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Selected Probability",
            f"{selected_probability:.2f}%"
        )

    with col2:

        st.metric(
            "Rejected Probability",
            f"{rejected_probability:.2f}%"
        )


    st.progress(
        int(selected_probability)
    )
