
# Employee Salary Prediction

This project focuses on predicting employee salaries using machine learning. It takes user inputs such as years of experience and job rating to estimate a salary value. The model is deployed using a Streamlit web application for ease of access and interaction.

## 📌 Project Features
- Cleaned and preprocessed tabular dataset
- Machine Learning model (Linear Regression or KNN)
- Real-time prediction using a web app (Streamlit)
- Model serialization using `joblib`

## 📂 Project Structure
```
employee-salary-prediction/
├── notebook/ : Jupyter Notebook for model training
├── app/      : Streamlit app code
├── model/    : Saved machine learning model
├── images/   : Screenshots and visuals
├── README.md : Project documentation
```

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/employee-salary-prediction.git
cd employee-salary-prediction
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit App
```bash
streamlit run app/salary_prediction_app.py
```

## 🧠 Input Features
- `years`: Years of experience
- `job_rating`: A numerical score (e.g., 3.5) representing job performance or evaluation

## 📚 Requirements
Create a `requirements.txt` file with the following:
```
streamlit
pandas
numpy
scikit-learn
joblib
```


