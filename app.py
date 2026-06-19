import streamlit as st
import pandas as pd
import joblib

# Page Config
st.set_page_config(
    page_title="Employee Attrition Prediction",
    page_icon="🧑‍💼",
    layout="centered"
)

# Load Model
@st.cache_resource
def load_model():
    model = joblib.load("attrition_model_3_.pkl")
    return model

model = load_model()

# Categorical Encoding Maps
# (Same as sklearn LabelEncoder would produce - alphabetical order)
business_travel_map = {
    "Non-Travel": 0,
    "Travel_Frequently": 1,
    "Travel_Rarely": 2
}

department_map = {
    "Human Resources": 0,
    "Research & Development": 1,
    "Sales": 2
}

education_field_map = {
    "Human Resources": 0,
    "Life Sciences": 1,
    "Marketing": 2,
    "Medical": 3,
    "Other": 4,
    "Technical Degree": 5
}

gender_map = {
    "Female": 0,
    "Male": 1
}

job_role_map = {
    "Healthcare Representative": 0,
    "Human Resources": 1,
    "Laboratory Technician": 2,
    "Manager": 3,
    "Manufacturing Director": 4,
    "Research Director": 5,
    "Research Scientist": 6,
    "Sales Executive": 7,
    "Sales Representative": 8
}

marital_status_map = {
    "Divorced": 0,
    "Married": 1,
    "Single": 2
}

overtime_map = {
    "No": 0,
    "Yes": 1
}

education_levels = {
    1: "Below College",
    2: "College",
    3: "Bachelor",
    4: "Master",
    5: "Doctor"
}

satisfaction_levels = {
    1: "Low",
    2: "Medium",
    3: "High",
    4: "Very High"
}

worklife_levels = {
    1: "Bad",
    2: "Good",
    3: "Better",
    4: "Best"
}

performance_levels = {
    1: "Low",
    2: "Good",
    3: "Excellent",
    4: "Outstanding"
}

# Title
st.title("🧑‍💼 Employee Attrition Prediction")
st.markdown(
    "Employee ki details bharo, model predict karega ki employee "
    "**company chhodega ya nahi (Attrition)**."
)
st.divider()

# Input Form
with st.form("attrition_form"):

    st.subheader("📋 Personal Details")
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.number_input("Age", min_value=18, max_value=60, value=30)
    with col2:
        gender = st.selectbox("Gender", list(gender_map.keys()))
    with col3:
        marital_status = st.selectbox("Marital Status", list(marital_status_map.keys()))

    col1, col2 = st.columns(2)
    with col1:
        distance_from_home = st.number_input("Distance From Home (km)", min_value=0, max_value=50, value=5)
    with col2:
        education = st.selectbox(
            "Education Level",
            options=list(education_levels.keys()),
            format_func=lambda x: f"{x} - {education_levels[x]}"
        )

    education_field = st.selectbox("Education Field", list(education_field_map.keys()))

    st.divider()
    st.subheader("💼 Job Details")
    col1, col2 = st.columns(2)
    with col1:
        department = st.selectbox("Department", list(department_map.keys()))
    with col2:
        job_role = st.selectbox("Job Role", list(job_role_map.keys()))

    col1, col2, col3 = st.columns(3)
    with col1:
        job_level = st.number_input("Job Level", min_value=1, max_value=5, value=1)
    with col2:
        business_travel = st.selectbox("Business Travel", list(business_travel_map.keys()))
    with col3:
        overtime = st.selectbox("OverTime", list(overtime_map.keys()))

    col1, col2 = st.columns(2)
    with col1:
        num_companies_worked = st.number_input("Num Companies Worked", min_value=0, max_value=15, value=1)
    with col2:
        total_working_years = st.number_input("Total Working Years", min_value=0, max_value=40, value=5)

    col1, col2, col3 = st.columns(3)
    with col1:
        years_at_company = st.number_input("Years At Company", min_value=0, max_value=40, value=3)
    with col2:
        years_in_current_role = st.number_input("Years In Current Role", min_value=0, max_value=20, value=2)
    with col3:
        years_with_curr_manager = st.number_input("Years With Curr Manager", min_value=0, max_value=20, value=2)

    years_since_last_promotion = st.number_input("Years Since Last Promotion", min_value=0, max_value=20, value=1)
    training_times_last_year = st.number_input("Training Times Last Year", min_value=0, max_value=10, value=2)

    st.divider()
    st.subheader("💰 Compensation")
    col1, col2 = st.columns(2)
    with col1:
        monthly_income = st.number_input("Monthly Income", min_value=1000, max_value=50000, value=5000, step=100)
    with col2:
        monthly_rate = st.number_input("Monthly Rate", min_value=1000, max_value=30000, value=15000, step=100)

    col1, col2, col3 = st.columns(3)
    with col1:
        daily_rate = st.number_input("Daily Rate", min_value=100, max_value=1500, value=800)
    with col2:
        hourly_rate = st.number_input("Hourly Rate", min_value=10, max_value=100, value=50)
    with col3:
        percent_salary_hike = st.number_input("Percent Salary Hike", min_value=0, max_value=50, value=15)

    stock_option_level = st.number_input("Stock Option Level", min_value=0, max_value=3, value=0)

    st.divider()
    st.subheader("😊 Satisfaction & Performance")
    col1, col2 = st.columns(2)
    with col1:
        environment_satisfaction = st.selectbox(
            "Environment Satisfaction",
            options=list(satisfaction_levels.keys()),
            format_func=lambda x: f"{x} - {satisfaction_levels[x]}"
        )
    with col2:
        job_satisfaction = st.selectbox(
            "Job Satisfaction",
            options=list(satisfaction_levels.keys()),
            format_func=lambda x: f"{x} - {satisfaction_levels[x]}"
        )

    col1, col2 = st.columns(2)
    with col1:
        relationship_satisfaction = st.selectbox(
            "Relationship Satisfaction",
            options=list(satisfaction_levels.keys()),
            format_func=lambda x: f"{x} - {satisfaction_levels[x]}"
        )
    with col2:
        job_involvement = st.selectbox(
            "Job Involvement",
            options=list(satisfaction_levels.keys()),
            format_func=lambda x: f"{x} - {satisfaction_levels[x]}"
        )

    col1, col2 = st.columns(2)
    with col1:
        work_life_balance = st.selectbox(
            "Work Life Balance",
            options=list(worklife_levels.keys()),
            format_func=lambda x: f"{x} - {worklife_levels[x]}"
        )
    with col2:
        performance_rating = st.selectbox(
            "Performance Rating",
            options=list(performance_levels.keys()),
            format_func=lambda x: f"{x} - {performance_levels[x]}"
        )

    submitted = st.form_submit_button("🔮 Predict Attrition", use_container_width=True)

# Prediction
if submitted:

    # IMPORTANT: column order must exactly match model.feature_names_in_
    input_dict = {
        "Age": age,
        "BusinessTravel": business_travel_map[business_travel],
        "DailyRate": daily_rate,
        "Department": department_map[department],
        "DistanceFromHome": distance_from_home,
        "Education": education,
        "EducationField": education_field_map[education_field],
        "EnvironmentSatisfaction": environment_satisfaction,
        "Gender": gender_map[gender],
        "HourlyRate": hourly_rate,
        "JobInvolvement": job_involvement,
        "JobLevel": job_level,
        "JobRole": job_role_map[job_role],
        "JobSatisfaction": job_satisfaction,
        "MaritalStatus": marital_status_map[marital_status],
        "MonthlyIncome": monthly_income,
        "MonthlyRate": monthly_rate,
        "NumCompaniesWorked": num_companies_worked,
        "OverTime": overtime_map[overtime],
        "PercentSalaryHike": percent_salary_hike,
        "PerformanceRating": performance_rating,
        "RelationshipSatisfaction": relationship_satisfaction,
        "StockOptionLevel": stock_option_level,
        "TotalWorkingYears": total_working_years,
        "TrainingTimesLastYear": training_times_last_year,
        "WorkLifeBalance": work_life_balance,
        "YearsAtCompany": years_at_company,
        "YearsInCurrentRole": years_in_current_role,
        "YearsSinceLastPromotion": years_since_last_promotion,
        "YearsWithCurrManager": years_with_curr_manager,
    }

    input_df = pd.DataFrame([input_dict])

    # Ensure exact column order expected by the model
    try:
        expected_cols = list(model.feature_names_in_)
        input_df = input_df[expected_cols]
    except AttributeError:
        # Older sklearn models without feature_names_in_ - order already matches
        pass

    prediction = model.predict(input_df)[0]
    proba = model.predict_proba(input_df)[0]

    st.divider()
    st.subheader("📊 Prediction Result")

    if prediction == 1:
        st.error(f"⚠️ Employee ke **Attrition (Job chhodne)** ki sambhavna hai!")
        st.metric("Attrition Probability", f"{proba[1]*100:.2f}%")
    else:
        st.success(f"✅ Employee ke **company me bane rehne** ki sambhavna hai.")
        st.metric("Retention Probability", f"{proba[0]*100:.2f}%")

    col1, col2 = st.columns(2)
    with col1:
        st.write("**Stay Probability:**", f"{proba[0]*100:.2f}%")
    with col2:
        st.write("**Leave Probability:**", f"{proba[1]*100:.2f}%")

    st.progress(float(proba[1]))

st.divider()
st.caption("Model: Random Forest Classifier | Trained on IBM HR Analytics Employee Attrition dataset")
