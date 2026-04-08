import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import joblib

# AutoML Imports
from pycaret.classification import setup, compare_models, pull, save_model, get_config

def run_analysis_and_training(data_path="student_data.csv"):
    if not os.path.exists(data_path):
        print(f"Error: {data_path} not found. Please run generate_data.py first.")
        return

    # 1. Load Data
    df = pd.read_csv(data_path)
    print("Dataset Loaded Successfully.")
    
    # 2. Data Analysis & Visualizations
    os.makedirs("plots", exist_ok=True)
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x='UG_CGPA', y='Programming_Skills', hue='Placement_Status', data=df)
    plt.title('UG CGPA vs Programming Skills by Placement Status')
    plt.savefig('plots/cgpa_vs_skills.png')
    plt.close()

    plt.figure(figsize=(8, 6))
    sns.boxplot(x='Placement_Status', y='UG_CGPA', data=df)
    plt.title('UG CGPA Distribution by Placement Status')
    plt.savefig('plots/cgpa_vs_placement.png')
    plt.close()

    plt.figure(figsize=(8, 6))
    sns.boxplot(x='Placement_Status', y='Programming_Skills', data=df)
    plt.title('Programming Skills by Placement Status')
    plt.savefig('plots/skills_vs_placement.png')
    plt.close()

    print("Visualizations saved in 'plots/' directory.")

    # 3. Drop Identifier
    df_for_model = df.drop(columns=['Student_ID'])
    
    # Label Encode Course and Degree_Type (Pycaret can sometimes handle categorical natively, but we explicit it to match old Streamlit logic)
    df_for_model['Degree_Type'] = df_for_model['Degree_Type'].map({'UG': 0, 'PG': 1})
    df_for_model['Course'] = df_for_model['Course'].map({'BTech': 0, 'BCA': 1, 'MCA': 2, 'MTech': 3, 'MBA': 4, 'Others': 5})
    # Fill any NaNs safely
    df_for_model['Course'] = df_for_model['Course'].fillna(5)
    
    features = df_for_model.drop(columns=['Placement_Status'])

    print("\n--- Starting PyCaret AutoML Pipeline ---")
    
    # 4. PyCaret Setup
    # PyCaret automatically handles missing value imputation, one-hot encoding internally if needed.
    # We pass the full clean dataframe
    clf_setup = setup(
        data=df_for_model, 
        target='Placement_Status', 
        session_id=42,
        fix_imbalance=True, # Applied SMOTE
        verbose=False, # Reduce terminal spam
        html=False
    )
    
    # 5. Compare Models
    # Let PyCaret run through ~14 different algorithms
    print("Comparing models... this might take a minute.")
    best_model = compare_models(exclude=['dummy'], n_select=1, cross_validation=True, sort='Accuracy')
    
    # 6. Extract Leaderboard
    leaderboard = pull()
    print("\n--- Leaderboard ---")
    print(leaderboard[['Accuracy', 'AUC', 'Recall', 'Prec.', 'F1']].head(5))
    
    # Rename index to Model_Name for easier display in Streamlit
    leaderboard.reset_index(inplace=True)
    leaderboard.rename(columns={'index': 'Model', 'Model': 'Model_Name'}, inplace=True)
    
    # Extract Best Model Name programmatically
    best_model_name = getattr(best_model, "__class__", None)
    if best_model_name:
         best_model_name_str = best_model.__class__.__name__
    else:
         best_model_name_str = "Selected AutoML Model"
    
    # We will write the name manually into the CSV for streamlit
    leaderboard['Best_Model_Type'] = best_model_name_str
    
    leaderboard.to_csv('automl_leaderboard.csv', index=False)
    print("Leaderboard saved to automl_leaderboard.csv")

    # 7. Generate Diagnostic visuals
    from pycaret.classification import plot_model
    try:
        print("\nGenerating Diagnostic Plots...")
        plot_model(best_model, plot='confusion_matrix', save=True)
        plot_model(best_model, plot='class_report', save=True)
        if os.path.exists('Confusion Matrix.png'):
            os.replace('Confusion Matrix.png', 'plots/confusion_matrix.png')
        if os.path.exists('Class Report.png'):
            os.replace('Class Report.png', 'plots/class_report.png')
        print("Safely saved Confusion Matrix and Class Report to plots/")
    except Exception as e:
        print("Notice: Error generating plots:", str(e))

    # 8. Save the pipeline and best model
    # PyCaret will save this as 'best_automl_model.pkl' automatically
    save_model(best_model, 'best_automl_model')
    print("Best model pipeline saved as 'best_automl_model.pkl'")
    
    # Save the order of features to be safe for Streamlit
    joblib.dump(list(features.columns), 'feature_names.pkl')
    print("Feature names saved as 'feature_names.pkl'")

if __name__ == "__main__":
    run_analysis_and_training()
