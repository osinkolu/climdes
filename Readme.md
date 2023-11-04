# Internship Success Prediction

This project is part of the CLIMDES internship application and aims to predict the success of internship applicants using a machine learning model. The project includes data simulation, preprocessing, model building, hyperparameter tuning, and the deployment of a Flask API for making predictions.

## Approach

- **Data Simulation and Preprocessing**:
  - 📊 Simulated a dataset containing features like GPA, skills, education level, test scores, continent, internship type, farm experience, and research publications.
  - 🧩 Transformed the data to match the model's input format with dummy variables.

- **Model Building**:
  - 🛠 Built a machine learning model using CatBoost to predict internship success.
  - 📈 Evaluated and compared the model's performance with other algorithms like LightGBM, Random Forest, and XGBoost.

- **Hyperparameter Tuning**:
  - 🔍 Used Optuna for hyperparameter optimization to improve the model's performance.

- **Model Deployment**:
  - 🚀 Deployed the CatBoost model as a Flask API on AWS Elastic Beanstalk to make predictions.

## Challenges Faced

- **Data Simulation**: Generating a realistic synthetic dataset can be challenging, especially to mimic real-world data distribution accurately.

- **Hyperparameter Tuning**: Finding the right hyperparameters for the model was a bit time-consuming, and the optimal settings may vary based on the dataset.

- **Deployment**: Deploying a machine learning model as an API on a cloud platform like AWS Elastic Beanstalk involves various configurations. It's always a hassle for folks like me that don't deploy often, but as usual, I figured it out.

## Feature Descriptions

- **GPA (Grade Point Average)**: 📚 Grade Point Average on a 5.0 scale.
- **Skills**: 💻 Number of programming languages known.
- **Internship_Success**: 📊 Binary target variable (1 for success, 0 for failure).
- **Education_Level**: 🎓 Education level of the applicant (High School, Bachelors, Masters, PhD).
- **Test_Score**: 📝 Test score on a scale of 0-100.
- **Continent**: 🌍 Continent of the applicant.
- **Internship_Type**: 💼 Type of internship (Backend, Frontend, Machine Learning).
- **Farm_Experience**: 🌾 Years of farm-related experience.
- **Research_Publications**: 📰 Number of research publications authored.

## Dependencies

- Python 3.x
- Pandas
- NumPy
- Scikit-learn
- CatBoost (or the chosen machine learning library)
- Optuna (for hyperparameter tuning)
- Flask (for the API)
- AWS Elastic Beanstalk (for deployment)

## Usage

1. Training and Hyperparameter Tuning: 
   - Run Jupyter Notebook or Python scripts for data simulation, preprocessing, model building, and hyperparameter tuning.

2. Model Deployment:
   - Deploy the model using Flask on a cloud platform (e.g., AWS Elastic Beanstalk).

3. Making Predictions:
   - Use the API endpoint (e.g., `/predict`) to send JSON data for predictions.

## API Endpoint

- Endpoint: http://climdesmltaskx.us-east-1.elasticbeanstalk.com/predict
- HTTP Method: POST
- Input Format: JSON with features like GPA, skills, education level, test scores, continent, internship type, farm experience, and research publications.

Sample JSON Input:
```json
{
    "GPA": 3.88,
    "Skills": 5,
    "Internship_Success": 1,
    "Education_Level": "High School",
    "Test_Score": 66,
    "Continent": "South America",
    "Internship_Type": "Frontend",
    "Farm_Experience": 9,
    "Research_Publications": 4
}
```

Sample JSON Output:
* 1 - Accepted
* 0 - Not Accepted

```json
{
    "prediction": 1
}
```
## Music and Vibes

I listened to these songs while working on this task:
 - 🎶 "I'm Not Afraid" by Eminem
 - 🎶 "Asiwaju" by Rugger
