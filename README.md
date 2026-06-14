# 🏥 Medical Insurance Cost Prediction Application

An end-to-end Machine Learning application that predicts medical insurance costs based on user demographics and health-related information. The project combines a **Streamlit frontend** for user interaction, a **FastAPI backend** for serving predictions, and **Docker** for containerization.

## 🚀 Features

* Interactive Streamlit Web Application
* FastAPI REST API Backend
* Machine Learning-Based Insurance Cost Prediction
* Data Preprocessing and Feature Engineering
* Model Training and Evaluation
* Swagger API Documentation
* Docker Containerization
* Modular Project Structure

## 🛠️ Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* FastAPI
* Streamlit
* Uvicorn
* Docker
* Jupyter Notebook

## 🏗️ System Architecture

```text
Streamlit Frontend
        │
        ▼
FastAPI Backend
        │
        ▼
 Machine Learning Model
        │
        ▼
 Insurance Cost Prediction
```

## 📂 Project Structure

```text
medical_insurance_ml_fastapi/
│
├── app.py
├── frontend.py
├── Dockerfile
├── requirements.txt
├── insurance-2.csv
├── ml_model.ipynb
│
├── model/
│   ├── predict.py
│   └── model.pkl
│
└── schema/
    ├── user_input.py
    └── prediction_response.py
```

## 📊 Input Features

| Feature  | Description           |
| -------- | --------------------- |
| age      | Age of the individual |
| sex      | Gender                |
| bmi      | Body Mass Index       |
| children | Number of dependents  |
| smoker   | Smoking status        |
| region   | Residential region    |

## 🔌 API Endpoint

### POST /predict

Example Request:

```json
{
  "age": 28,
  "sex": "male",
  "bmi": 22.0,
  "children": 2,
  "smoker": "yes",
  "region": "northwest"
}
```

Example Response:

```json
{
  "predicted_charges": 18654.73
}
```

## ▶️ Running the Application

### 1. Clone Repository

```bash
git clone https://github.com/Divyjain88/medical_insurance_ml_fastapi.git
cd medical_insurance_ml_fastapi
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Start FastAPI Backend

```bash
uvicorn app:app --reload
```

FastAPI Documentation:

```text
http://127.0.0.1:8000/docs
```

### 4. Start Streamlit Frontend

```bash
streamlit run frontend.py
```

Streamlit Application:

```text
http://localhost:8501
```

## 🐳 Docker

### Build Docker Image

```bash
docker build -t medical-insurance-app .
```

### Run Docker Container

```bash
docker run -p 8000:8000 medical-insurance-app
```

## 📈 Machine Learning Workflow

1. Data Collection
2. Data Cleaning
3. Exploratory Data Analysis (EDA)
4. Feature Engineering
5. Model Training
6. Model Evaluation
7. FastAPI Integration
8. Streamlit Integration
9. Docker Containerization

## 🔮 Future Improvements

* CI/CD using GitHub Actions
* AWS Deployment
* Model Monitoring
* User Authentication
* Enhanced UI/UX
* Automated Retraining Pipeline

🔗 Connect With Me
LinkedIn: www.linkedin.com/in/divyjain24
GitHub: https://github.com/Divyjain88
Docker: https://hub.docker.com/u/divyjain88

## 👨‍💻 Author

**Divy Jain**

### ⭐ If you found this project useful, consider starring the repository.
