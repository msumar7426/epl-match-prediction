import os
import pickle

import pandas as pd
from flask import Flask, render_template, request


app = Flask(__name__)


# ---------------------------------------------------------------------------
# Model path — works both locally and on PythonAnywhere.
# BASE_DIR resolves to the folder that contains this backend.py file,
# so the path below will always be correct regardless of where you deploy.
# ---------------------------------------------------------------------------
BASE_DIR   = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "trained_models", "svc_tuned_model.pkl")
SCALER_PATH = os.path.join(BASE_DIR, "trained_models", "scaler.pkl")


def load_assets():
    """Load the trained SVC model and scaler from disk."""
    with open(MODEL_PATH, "rb") as f:
        model_obj = pickle.load(f)
    with open(SCALER_PATH, "rb") as f:
        scaler_obj = pickle.load(f)
    return model_obj, scaler_obj


# Load model and scaler once at startup for efficiency
model, scaler = load_assets()


# ---------------------------------------------------------------------------
# Mapping from encoded label (as produced by LabelEncoder) to readable text.
# LabelEncoder was fitted on ['DRAW', 'LOSS', 'WIN'] (alphabetical order),
# which gives: DRAW -> 0, LOSS -> 1, WIN -> 2
# ---------------------------------------------------------------------------
LABEL_MAP = {
    0: "DRAW",
    1: "LOSS",
    2: "WIN",
}


@app.route("/", methods=["GET", "POST"])
def index():
    prediction    = None
    error_message = None

    if request.method == "POST":
        try:
            # Read and validate form inputs
            ht_home_goals = int(request.form.get("HalfTimeHomeGoals", "").strip())
            ht_away_goals = int(request.form.get("HalfTimeAwayGoals", "").strip())
            home_shots    = int(request.form.get("HomeShotsOnTarget",  "").strip())
            away_shots    = int(request.form.get("AwayShotsOnTarget",  "").strip())
            home_corners  = int(request.form.get("HomeCorners",        "").strip())
            away_corners  = int(request.form.get("AwayCorners",        "").strip())

            # Build feature vector DataFrame exactly as in the notebook
            user_input = pd.DataFrame(
                {
                    "HalfTimeHomeGoals": [ht_home_goals],
                    "HalfTimeAwayGoals": [ht_away_goals],
                    "HomeShotsOnTarget": [home_shots],
                    "AwayShotsOnTarget": [away_shots],
                    "HomeCorners":       [home_corners],
                    "AwayCorners":       [away_corners],
                }
            )

            # Scale the features
            user_input_scaled = scaler.transform(user_input)

            # Make prediction using the loaded tuned model
            encoded_pred     = model.predict(user_input_scaled)[0]
            encoded_pred_int = int(encoded_pred)
            prediction       = LABEL_MAP.get(encoded_pred_int, "UNKNOWN")

        except Exception as exc:  # pylint: disable=broad-except
            error_message = f"Unable to make prediction: {exc}"

    return render_template("index.html", prediction=prediction, error_message=error_message)


if __name__ == "__main__":
    # For local testing only.
    # On PythonAnywhere the WSGI config imports 'app' from this module directly.
    app.run(debug=True, port=5005)
