---
title: EPL Match Prediction
emoji: ⚽
colorFrom: green
colorTo: gray
sdk: docker
pinned: false
---

# EPL Match Result Prediction | AI Engine

**Live Demo:** [https://huggingface.co/spaces/msumar2011/EPL_match_prediction](https://huggingface.co/spaces/msumar2011/EPL_match_prediction)

## Project Overview
This project is an elite machine learning-powered web application designed to predict the outcome of English Premier League (EPL) matches from the perspective of the **Home Team**. The application takes in-match statistics at half-time (or later) and predicts whether the home team will **WIN**, **DRAW**, or **LOSE**.

This repository contains both the model tuning pipeline (Jupyter Notebook) and a deployment-ready, highly optimized Flask web application featuring a premium "AI Sports Command Center" interface.

## Repository Structure

```text
epl_match_prediction/
├── README.md                                  # Project documentation (this file)
├── EPL_SVM_GridSearchCV_Tuning.ipynb          # Jupyter Notebook with EDA and Model Tuning
├── backend.py                                 # Flask application serving the model
├── requirements.txt                           # Python dependencies
├── Dockerfile                                 # Docker configuration for Hugging Face deployment
├── trained_models/                            # Directory containing the saved ML models
│   ├── svc_tuned_model.pkl                    # Pickled tuned Support Vector Classifier model
│   └── scaler.pkl                             # Pickled StandardScaler for feature normalization
└── templates/                                 # Directory containing HTML templates
    └── index.html                             # The premium AI Command Center UI
```

## Features
- **Predictive Modeling**: Utilizes an extensively tuned Support Vector Classifier (SVC) with a linear kernel. User input is dynamically scaled using a fitted `StandardScaler` to ensure maximum prediction accuracy.
- **Elite Visual Identity**: A beautifully designed, cinematic AI sports dashboard featuring matte black aesthetics, tactical grid overlays, and dynamic sports glow effects based on the match prediction.
- **Seamless Integration**: A lightweight Flask backend that efficiently loads the serialized models and processes form submissions to yield real-time predictions.

## Machine Learning Model
The classification model was built and evaluated using the provided Jupyter Notebook (`EPL_SVM_GridSearchCV_Tuning.ipynb`).
- **Features Used**: `HalfTimeHomeGoals`, `HalfTimeAwayGoals`, `HomeShotsOnTarget`, `AwayShotsOnTarget`, `HomeCorners`, `AwayCorners`.
- **Target Variable**: `Result` (WIN, DRAW, LOSS for the Home Team).
- **Algorithm**: Support Vector Machine (SVM) Classifier mapped with robust feature scaling.

## Prerequisites
To run this project locally, ensure you have Python 3 installed on your machine.

## Setup and Installation

1. **Clone the Repository**
   Ensure you are in the project directory.
   ```bash
   cd epl_match_prediction
   ```

2. **Create a Virtual Environment (Optional but Recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install Dependencies**
   Install the required Python packages using `pip`:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Web Application Locally

1. **Start the Flask Server**
   Run the backend script to start the local development server (configured to port 5005 to avoid macOS port conflicts):
   ```bash
   python backend.py
   ```

2. **Access the Application**
   Open your preferred web browser and navigate to:
   `http://127.0.0.1:5005/`

## Deploying to Hugging Face Spaces

This application is configured for seamless deployment to Hugging Face Spaces using the included `Dockerfile`.

1. Create a new **Docker** Space on Hugging Face.
2. Upload the `backend.py`, `requirements.txt`, `Dockerfile`, `templates/`, and `trained_models/` directly into your Hugging Face Space.
3. Hugging Face will automatically build the Docker container and deploy the app.

## Technologies Used
- **Backend / Machine Learning**: Python, Flask, Pandas, Scikit-Learn
- **Frontend**: HTML5, CSS3 (Custom Elite UI), Google Fonts (Bebas Neue, Oswald, Inter)
- **Deployment**: Docker, Gunicorn (Hugging Face Spaces)
