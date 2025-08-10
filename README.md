# diabetes-streamlit-app

Predict the likelihood of diabetes based on health indicators using a **Random Forest Classifier**, trained on the Pima Indians Diabetes Database and deployed via **Streamlit**.

---

##  Live Demo

[👉 Try it out on Streamlit!](https://gunjan712sehrawat-diabetes-streamlit-app-app-cgdfc8.streamlit.app/)

---

##  Dataset

- **Source:** Pima Indians Diabetes Dataset (UCI / Kaggle)
- **Features used:**
  - Pregnancies
  - Glucose
  - Blood Pressure
  - Skin Thickness
  - Insulin
  - BMI
  - Diabetes Pedigree Function
  - Age

---

##  Tech Stack

| Component        | Technology             |
|------------------|------------------------|
| Model            | Random Forest (Scikit-learn) |
| Preprocessing    | StandardScaler (Scikit-learn) |
| Imbalance Handling | SMOTE (imbalanced-learn) |
| Deployment       | Streamlit               |
| Model Persistence | Joblib                |

---

##  Model Performance (Example)

| Metric          | Value   |
|-----------------|---------|
| Accuracy        | XX.XX%  |
| ROC-AUC Score   | 0.XX    |

*(Replace with your actual evaluation results from Colab.)*

---

##  Screenshot

*(Add an image of your app here—take a screenshot of the running UI and save it as `screenshot.png` in your repo. It will render nicely below.)*

![App Screenshot](screenshot.png)

---

##  How to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/Gunjan712Sehrawat/diabetes-streamlit-app.git
   cd diabetes-streamlit-app
