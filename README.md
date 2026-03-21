# House Price Prediction - End-to-End MLOps Project

## Overview
This project demonstrates a complete **end-to-end MLOps pipeline** for predicting house prices using machine learning. It covers the entire lifecycle from data preprocessing and model training to deployment and CI/CD automation.
The system is designed to be modular, scalable, and production-ready.

---

## Objective
- Build and compare multiple regression models
- Track experiments using MLflow
- Develop a prediction API using FastAPI
- Containerize the application using Docker
- Deploy the application on Hugging Face Spaces
- Implement CI/CD pipeline using GitHub Actions

---

## Tech Stack

- **Programming Language:** Python  
- **Libraries:** pandas, numpy, scikit-learn  
- **Experiment Tracking:** MLflow  
- **API Framework:** FastAPI  
- **Containerization:** Docker  
- **Deployment Platform:** Hugging Face Spaces  
- **CI/CD:** GitHub Actions  

---

## 📂 Project Structure
MLOps_Lab_7/
│
├── configs/ # Configuration files
│
├── models/ # Saved models & preprocessing objects
│ ├── best_model.pkl
│ ├── scaler.pkl
│ ├── columns.json
│ └── num_cols.json
│
├── notebooks/ # Experimentation & development
│ ├── 00_data_splits.ipynb
│ ├── 01_EDA_cleaning.ipynb
│ ├── 02_feature_eng_encoding.ipynb
│ ├── 03_model_training_mlflow.ipynb
│ ├── mlruns/ # MLflow experiment logs
│ └── mlflow.db
│
├── src/ # Production-level code
│ ├── api/ # FastAPI application
│ │ └── main.py
│ │
│ ├── inference_pipeline/ # Prediction logic
│ │ └── predict.py
│ 

│
├── Dockerfile # API container
├── requirements.txt # Dependencies
├── .github/workflows/ci.yml # CI/CD pipeline
└── README.md



---

## Workflow

### Data Processing
- Dataset loaded and cleaned
- No missing values found
- Target variable: `price`

### Feature Engineering
- Categorical variables encoded
- Numerical features scaled
- Consistent preprocessing pipeline created

### Model Training
Models used:
- Linear Regression  
- Ridge Regression  
- Decision Tree  
- Random Forest  
- Gradient Boosting  

Evaluation Metric:
- RMSE (Root Mean Squared Error)

---

### MLflow Tracking
- Logs parameters, metrics, and models
- Enables comparison of multiple runs
- Stores artifacts in `mlruns/`

---

### Inference Pipeline
- Input → preprocessing → scaling → prediction
- Ensures same transformations as training

---

### FastAPI Development

Endpoints:
- `GET /` → Health check  
- `POST /predict` → Predict house price  

---

### Docker Containerization

```bash
docker build -t house-price-app .
docker run -p 8000:8000 house-price-app

### HuggingFace Link
https://saniyasawal-house-price-predictor.hf.space/docs

##CI/CD Pipeline
Implemented using GitHub Actions
Automates:
         Dependency installation
         Code validation
         Docker build

---------------------------------------------------------------------------------

# How to Run Locally

##Clone the Repository
```bash
git clone <your-repo-link>
cd MLOps_Lab_7

#Create Virtual Environment
python -m venv venv

#Activate Environment
Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

#Install Dependencies
pip install --upgrade pip
pip install -r requirements.txt

#Run MLflow (Experiment Tracking)
cd notebooks
mlflow ui

#Run FastAPI Server
Go back to root folder:
cd ..

Run API:
uvicorn src.api.main:app --reload

Open Swagger UI:

http://127.0.0.1:8000/docs

#Test Prediction API
Use /predict endpoint with sample input:

{
  "area": 7420,
  "bedrooms": 4,
  "bathrooms": 2,
  "stories": 3,
  "mainroad": "yes",
  "guestroom": "no",
  "basement": "no",
  "hotwaterheating": "no",
  "airconditioning": "yes",
  "parking": 2,
  "prefarea": "yes",
  "furnishingstatus": "furnished"
}

#Run with Docker
Build Docker Image
docker build -t house-price-app .
Run Container
docker run -p 8000:8000 house-price-app
