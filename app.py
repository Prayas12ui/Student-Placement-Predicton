import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
import os

# PyCaret is loaded to ensure pipeline loads correctly, though joblib loading usually works.
from pycaret.classification import load_model, predict_model

# --- Page Configuration ---
st.set_page_config(page_title="Student Placement Dashboard", layout="wide", page_icon="🎓")

st.title("🎓 Student Performance & Placement Analytics")
st.markdown("""
This dashboard provides insights into student performance data and predicting placement outcomes using Machine Learning.
""")

# --- Load Data & Model Check ---
DATA_PATH = "student_data.csv"
MODEL_PATH = "best_automl_model.pkl"
FEATURES_PATH = "feature_names.pkl"
LEADERBOARD_PATH = "automl_leaderboard.csv"

if not os.path.exists(DATA_PATH) or not os.path.exists(MODEL_PATH) or not os.path.exists(LEADERBOARD_PATH):
    st.warning("Data or model not found. Please run `python generate_data.py` and `python train_model.py` first.")
    st.stop()

@st.cache_data
def load_data():
    return pd.read_csv(DATA_PATH)

@st.cache_data
def load_leaderboard():
    return pd.read_csv(LEADERBOARD_PATH)

@st.cache_resource
def get_model():
    # PyCaret's load_model appends .pkl automatically, so remove the extension for the argument
    return load_model("best_automl_model")

df = load_data()
model = get_model()
expected_features = joblib.load(FEATURES_PATH)
leaderboard = load_leaderboard()

# --- Sidebar for Navigation ---
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Data Overview & EDA", "AutoML Metrics", "Predict Placement"])

if page == "Data Overview & EDA":
    st.header("📊 Data Overview")
    st.dataframe(df.head(10))

    st.subheader("Key Statistics")
    st.write(df.describe())

    st.header("📈 Exploratory Data Analysis (EDA)")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Placement Distribution")
        fig, ax = plt.subplots()
        sns.countplot(data=df, x="Placement_Status", palette="Set2", ax=ax)
        st.pyplot(fig)

        st.subheader("UG CGPA vs Programming Skills")
        fig, ax = plt.subplots()
        sns.scatterplot(data=df, x="UG_CGPA", y="Programming_Skills", hue="Placement_Status", palette="Set1", ax=ax)
        st.pyplot(fig)

    with col2:
        st.subheader("UG CGPA by Placement")
        fig, ax = plt.subplots()
        sns.boxplot(data=df, x="Placement_Status", y="UG_CGPA", palette="Set3", ax=ax)
        st.pyplot(fig)

        st.subheader("Degree Type by Placement")
        fig, ax = plt.subplots()
        sns.countplot(data=df, x="Degree_Type", hue="Placement_Status", palette="viridis", ax=ax)
        st.pyplot(fig)

elif page == "AutoML Metrics":
    st.header("🤖 AutoML Model Evaluation")
    st.markdown("We trained and compared multiple machine learning algorithms simultaneously using PyCaret. Below is the final leaderboard ranked by Accuracy.")
    
    best_model_name = leaderboard['Best_Model_Type'].iloc[0]
    best_acc = leaderboard['Accuracy'].iloc[0]
    best_prec = leaderboard['Prec.'].iloc[0]
    best_rec = leaderboard['Recall'].iloc[0]
    
    st.success(f"**Winner Selected:** The best performing algorithm was **{best_model_name}** with an accuracy of **{best_acc*100:.2f}%**.")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Top Model Accuracy", f"{best_acc*100:.2f}%")
    col2.metric("Top Model Precision", f"{best_prec*100:.2f}%")
    col3.metric("Top Model Recall", f"{best_rec*100:.2f}%")
    
    st.subheader("Complete Model Leaderboard")
    # Hide the custom metadata column we added
    display_df = leaderboard.drop(columns=['Best_Model_Type'])
    # Make accuracy and metrics percentages for easy reading
    cols_to_format = ['Accuracy', 'AUC', 'Recall', 'Prec.', 'F1', 'Kappa', 'MCC']
    for c in cols_to_format:
        if c in display_df.columns:
            display_df[c] = display_df[c].apply(lambda x: f"{x*100:.2f}%")
            
    st.dataframe(display_df, use_container_width=True)

    st.markdown("---")
    st.subheader("📊 Top Model Diagnostics")
    st.markdown("Here we visually prove how our best model handles the classes, explicitly relying on SMOTE (Synthetic Minority Over-sampling) if any imbalance existed.")
    
    diag1, diag2 = st.columns(2)
    with diag1:
        if os.path.exists('plots/confusion_matrix.png'):
            st.image('plots/confusion_matrix.png', caption="Confusion Matrix")
        else:
            st.warning("Confusion Matrix image not found.")
            
    with diag2:
        if os.path.exists('plots/class_report.png'):
            st.image('plots/class_report.png', caption="Classification Report")
        else:
            st.warning("Classification Report image not found.")


elif page == "Predict Placement":
    st.header("🔮 Placement Predictor")
    st.markdown("Enter the student's details below to securely run the top-performing AutoML pipeline.")
    
    # Display the current active model silently
    best_model_name = leaderboard['Best_Model_Type'].iloc[0]
    st.caption(f"Currently scoring using: **{best_model_name}**")

    # Top level dynamic choices
    degree_type = st.radio("Degree Level", ["UG", "PG"], horizontal=True)
    
    if degree_type == "UG":
        course_opts = ["BTech", "BCA", "Others"]
    else:
        course_opts = ["MCA", "MTech", "MBA", "Others"]
        
    course_str = st.selectbox("Select Course", course_opts)
    
    display_course = course_str
    if course_str == "Others":
        custom_course = st.text_input("Specify your Course Name", placeholder="e.g. BSc Computer Science")
        if custom_course:
            display_course = custom_course

    col1, col2 = st.columns(2)

    with col1:
        tenth = st.number_input("10th Marks (%)", min_value=0.0, max_value=100.0, value=75.0)
        twelfth = st.number_input("12th Marks (%)", min_value=0.0, max_value=100.0, value=75.0)
        
        # Dynamic CGPA Label logic
        if degree_type == "UG":
            ug_cgpa_label = f"{display_course} CGPA (0-10)"
        else:
            ug_cgpa_label = "Past UG Degree CGPA (0-10)"
            
        ug_cgpa = st.number_input(ug_cgpa_label, min_value=0.0, max_value=10.0, value=7.5)
        
        if degree_type == "PG":
            pg_cgpa = st.number_input(f"Current {display_course} CGPA (0-10)", min_value=0.0, max_value=10.0, value=8.0)
        else:
            pg_cgpa = 0.0

    with col2:
        prog_skills = st.slider("Programming Skills Score", 0, 100, 70)
        comm_skills = st.slider("Communication Skills Score", 0, 100, 70)
        internships = st.selectbox("Internships Completed", [0, 1, 2, 3])
        projects = st.selectbox("Number of Projects", [0, 1, 2, 3, 4, 5])
        backlogs = st.number_input("Active Backlogs", min_value=0, max_value=10, value=0)

    submit = st.button("Predict Placement", type="primary", use_container_width=True)

    if submit:
        # Construct input dataframe
        course_map = {'BTech': 0, 'BCA': 1, 'MCA': 2, 'MTech': 3, 'MBA': 4, 'Others': 5}
        degree_map = {'UG': 0, 'PG': 1}
        
        input_data = {
            "Degree_Type": degree_map[degree_type],
            "Course": course_map[course_str],
            "10th_Marks": tenth,
            "12th_Marks": twelfth,
            "UG_CGPA": ug_cgpa,
            "PG_CGPA": pg_cgpa,
            "Programming_Skills": prog_skills,
            "Communication_Skills": comm_skills,
            "Internships": internships,
            "Projects": projects,
            "Backlogs": backlogs
        }
        
        input_df = pd.DataFrame([input_data])
        input_df = input_df[expected_features]

        # Use Pycaret predict_model
        # predict_model returns a dataframe with 'prediction_label' and 'prediction_score'
        predictions_df = predict_model(model, data=input_df)
        prediction_label = predictions_df['prediction_label'].iloc[0]

        # Pycaret returns string labels because the target in the dataset is a string.
        if str(prediction_label) == 'Placed' or str(prediction_label) == '1':
            st.success(f"🎉 **Prediction: Placed!** This profile looks strong for placement.")
            st.balloons()
        else:
            st.error(f"⚠️ **Prediction: Not Placed.** Based on the input data, this profile may face challenges in placement.")
            
            # Generate dynamic suggestions
            suggestions = []
            weak_areas = []
            
            if tenth < 70:
                suggestions.append("Improve your 10th marks baseline or compensate heavily with advanced tech skills.")
                weak_areas.append("10th Marks")
            if twelfth < 70:
                suggestions.append("Focus on strong current academics to offset lower 12th marks.")
                weak_areas.append("12th Marks")
            if degree_type == "UG" and ug_cgpa < 7.0:
                suggestions.append("Improve your UG CGPA to at least 7.0+ to meet minimum cutoffs for most companies.")
                weak_areas.append("UG CGPA")
            elif degree_type == "PG":
                if pg_cgpa < 7.0:
                    suggestions.append("Improve your PG CGPA to at least 7.0+ to increase your competitiveness.")
                    weak_areas.append("PG CGPA")
                if ug_cgpa < 7.0:
                    suggestions.append("Improve your past UG CGPA perception with strong PG projects/certifications.")
                    weak_areas.append("UG CGPA")
            if prog_skills < 60:
                suggestions.append("Enhance your programming skills by practicing on platforms like LeetCode or HackerRank.")
                weak_areas.append("Programming Skills")
            if comm_skills < 60:
                suggestions.append("Work on your communication skills through mock interviews and group discussions.")
                weak_areas.append("Communication Skills")
            if internships == 0:
                suggestions.append("Try to complete at least one internship. Practical experience is highly valued.")
                weak_areas.append("No Internships")
            if projects < 2:
                suggestions.append("Build more academic or personal projects to showcase practical application of your skills.")
                weak_areas.append("Few Projects")
            if backlogs > 0:
                suggestions.append("Clear your active backlogs before placement season begins.")
                weak_areas.append("Active Backlogs")
                
            st.markdown("### Areas to Improve")
            
            if suggestions:
                st.warning(f"**Main weak areas:** {', '.join(weak_areas)}")
                for s in suggestions:
                    st.info(f"💡 {s}")
            else:
                st.info("💡 Your profile is well-rounded, but the competition is high. Consider gaining advanced certifications.")
                
            st.caption("_Focus on these improvements to increase placement chances._")
