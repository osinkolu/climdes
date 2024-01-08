# -*- coding: utf-8 -*-
"""
@author: Professor
"""

"""
    {
    "GPA": 3.88,
    "Skills": 5,
    "Education_Level": "High School",
    "Test_Score": 66,
    "Continent": "South America",
    "Internship_Type": "Frontend",
    "Farm_Experience": 9,
    "Research_Publications": 4
    }

"""

from flask import Flask, request, jsonify
import pickle
import pandas as pd
with open('catboost_internship_model.pkl', 'rb') as model_file:
    loaded_model = pickle.load(model_file)



application = Flask(__name__)
@application.route('/')
def index():
    return("Welcome, please smile more.😉 - Note: Source codes belong to Olufemi Victor (AKA Professor). This was created for the CLIMDES Internship, the /predict endpoint works")

@application.route("/predict", methods=["GET", "POST"])
def predict():
    try:
        # Get the JSON data from the request
        data = request.get_json(force=True)

        # Map the received JSON data to the model's input format
        model_input = {
            'GPA': data['GPA'],
            'Skills': data['Skills'],
            'Test_Score': data['Test_Score'],
            'Farm_Experience': data['Farm_Experience'],
            'Research_Publications': data['Research_Publications'],
            'Education_Level_High School': 1 if data['Education_Level'] == 'High School' else 0,
            'Education_Level_Masters': 1 if data['Education_Level'] == 'Masters' else 0,
            'Education_Level_PhD': 1 if data['Education_Level'] == 'PhD' else 0,
            'Continent_Asia': 1 if data['Continent'] == 'Asia' else 0,
            'Continent_Australia': 1 if data['Continent'] == 'Australia' else 0,
            'Continent_Europe': 1 if data['Continent'] == 'Europe' else 0,
            'Continent_North America': 1 if data['Continent'] == 'North America' else 0,
            'Continent_South America': 1 if data['Continent'] == 'South America' else 0,
            'Internship_Type_Frontend': 1 if data['Internship_Type'] == 'Frontend' else 0,
            'Internship_Type_Machine Learning': 1 if data['Internship_Type'] == 'Machine Learning' else 0
        }

        # Make predictions using the loaded model and mapped data
        prediction = loaded_model.predict(pd.DataFrame([model_input]))

        # Return the prediction as a response
        return jsonify({'prediction': int(prediction[0])})  # Convert prediction to int

    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ =="__main__":
    application.run(host='0.0.0.0', port=8080)