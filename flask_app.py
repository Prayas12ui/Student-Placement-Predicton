import os
import pandas as pd
import joblib
from flask import Flask, request, jsonify, render_template

# PyCaret is loaded to ensure pipeline loads correctly.
from pycaret.classification import load_model, predict_model

app = Flask(__name__)

# --- Load Data & Model ---
MODEL_PATH = "best_automl_model.pkl"
FEATURES_PATH = "feature_names.pkl"
LEADERBOARD_PATH = "automl_leaderboard.csv"

# Global variables for model and features
model = None
expected_features = None
leaderboard_data = None

def init_app():
    global model, expected_features, leaderboard_data
    if os.path.exists(MODEL_PATH) and os.path.exists(FEATURES_PATH) and os.path.exists(LEADERBOARD_PATH):
        # load_model does not require .pkl
        model = load_model("best_automl_model")
        expected_features = joblib.load(FEATURES_PATH)
        leaderboard_data = pd.read_csv(LEADERBOARD_PATH)
        print("Model and features loaded successfully.")
    else:
        print("Warning: Model or required files not found. Run training first.")

# Initialize when the module loads
init_app()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/metrics", methods=["GET"])
def metrics():
    if leaderboard_data is None:
        return jsonify({"error": "Leaderboard not found."}), 404
    
    best_model_name = leaderboard_data['Best_Model_Type'].iloc[0]
    best_acc = leaderboard_data['Accuracy'].iloc[0]
    best_prec = leaderboard_data['Prec.'].iloc[0]
    best_rec = leaderboard_data['Recall'].iloc[0]
    
    return jsonify({
        "best_model": best_model_name,
        "accuracy": f"{best_acc*100:.2f}%",
        "precision": f"{best_prec*100:.2f}%",
        "recall": f"{best_rec*100:.2f}%"
    })

@app.route("/predict", methods=["POST"])
def predict():
    if model is None or expected_features is None:
        return jsonify({"error": "Model not loaded on server."}), 500
        
    try:
        data = request.json
        
        # Course Map and Degree Map
        course_map = {'BTech': 0, 'BCA': 1, 'MCA': 2, 'MTech': 3, 'MBA': 4, 'Others': 5}
        degree_map = {'UG': 0, 'PG': 1}
        
        input_data = {
            "Degree_Type": degree_map[data.get('Degree_Type', 'UG')],
            "Course": course_map[data.get('Course', 'Others')],
            "10th_Marks": float(data.get('10th_Marks', 0)),
            "12th_Marks": float(data.get('12th_Marks', 0)),
            "UG_CGPA": float(data.get('UG_CGPA', 0)),
            "PG_CGPA": float(data.get('PG_CGPA', 0)),
            "Programming_Skills": int(data.get('Programming_Skills', 0)),
            "Communication_Skills": int(data.get('Communication_Skills', 0)),
            "Internships": int(data.get('Internships', 0)),
            "Projects": int(data.get('Projects', 0)),
            "Backlogs": int(data.get('Backlogs', 0))
        }
        
        input_df = pd.DataFrame([input_data])
        # Ensure column order matches expected features
        for f in expected_features:
            if f not in input_df.columns:
                input_df[f] = 0.0 # fallback
                
        input_df = input_df[expected_features]
        
        # Predict using pycaret
        predictions_df = predict_model(model, data=input_df)
        prediction_label = str(predictions_df['prediction_label'].iloc[0])
        
        # Normalize prediction label
        if prediction_label == 'Placed' or prediction_label == '1':
            outcome = "Placed"
        else:
            outcome = "Not Placed"
            
        return jsonify({
            "success": True,
            "prediction": outcome
        })
        
    except Exception as e:
        return jsonify({"error": str(e), "success": False}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
