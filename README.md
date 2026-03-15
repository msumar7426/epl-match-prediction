# EPL Match Result Prediction Web Application

## Project Link: https://msumar.pythonanywhere.com/

## Project Overview
This project is a machine learning-powered web application designed to predict the outcome of English Premier League (EPL) matches from the perspective of the **Home Team**. The application takes in-match statistics at half-time (or later) and predicts whether the home team will **WIN**, **DRAW**, or **LOSE**.

This repository contains both the model training pipeline (Jupyter Notebook) and the deployment-ready Flask web application.

## Repository Structure

```text
epl_webapp/
├── README.md                                  # Project documentation (this file)
├── EPL_Match_Result_Prediction (1).ipynb      # Jupyter Notebook with EDA and Model Training
├── backend.py                                 # Flask application serving the model
├── requirements.txt                           # Python dependencies
├── Trained Models/                            # Directory containing the saved ML model
│   └── svc_trained_model.pkl                  # Pickled Support Vector Classifier model
└── templates/                                 # Directory containing HTML templates
    └── index.html                             # The front-end user interface
```

## Features
- **Predictive Modeling**: Utilizes an extensively trained Support Vector Classifier (SVC) with a linear kernel to classify match outcomes.
- **Interactive Web Interface**: A beautifully designed, responsive UI built with HTML, CSS (Bootstrap 5), and custom styling.
- **Seamless Integration**: A lightweight Flask backend that efficiently loads the serialized model and processes form submissions to yield real-time predictions.

## Machine Learning Model
The classification model was built and evaluated using the provided Jupyter Notebook (`EPL_Match_Result_Prediction (1).ipynb`).
- **Features Used**: `HalfTimeHomeGoals`, `HalfTimeAwayGoals`, `HomeShotsOnTarget`, `AwayShotsOnTarget`, `HomeCorners`, `AwayCorners`.
- **Target Variable**: `Result` (WIN, DRAW, LOSS for the Home Team).
- **Algorithm**: Support Vector Machine (SVM) Classifier.

## Prerequisites
To run this project locally, ensure you have Python 3 installed on your machine.

## Setup and Installation

1. **Clone or Extract the Repository**
   Ensure you are in the `epl_webapp` directory.
   ```bash
   cd epl_webapp
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

## Running the Web Application

1. **Start the Flask Server**
   Run the backend script to start the local development server:
   ```bash
   python backend.py
   ```
   Alternatively, you can run:
   ```bash
   export FLASK_APP=backend:app  # On Windows CMD use: set FLASK_APP=backend:app
   flask run
   ```

2. **Access the Application**
   Open your preferred web browser and navigate to:
   `http://127.0.0.1:5000/`

## Usage
1. Open the web interface.
2. Input the match statistics for the both the Home and Away teams (Goals at Half Time, Shots on Target, and Corners).
3. Click the **"Predict Match Result"** button.
4. The predicted result (**WIN**, **DRAW**, or **LOSS**) will be displayed on the screen.

## Technologies Used
- **Backend / Machine Learning**: Python, Flask, Pandas, NumPy, Scikit-Learn
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Model Serialization**: Pickle

## Developer / Submission Information
- **Dataset**: Kaggle — English Premier League Results (2000–2022)
- **Deployment**: Can be easily deployed to platforms like PythonAnywhere, Heroku, or Render using the included WSGI configuration.
