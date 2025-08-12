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

# Diabetes Risk Prediction 

# Purpose
It provides an easy-to-use AI-ML web application that predicts the likelihood of diabetes based on user-provided health indicators. It demonstrates how ***machine learning models*** can be integrated into interactive web apps for real-time health risk assessment.

# Importance
***Early detection***: Supports timely medical consultation and preventive action.

***Accessibility***: Allows anyone with internet access to check their diabetes risk.

***Educational value***: Illustrates end-to-end ML project workflow — from preprocessing and modeling to deployment.

# Dataset Used
Source: Pima Indians Diabetes Dataset

Features:
Pregnancies
Glucose
Blood Pressure
Skin Thickness
Insulin
BMI
Diabetes Pedigree Function
Age

 # Methodology
Data Cleaning & Preprocessing: Missing values handled; features scaled using StandardScaler.

Class Imbalance Handling: Applied SMOTE to balance diabetic/non-diabetic cases.

Model Selection: Chose Random Forest for its robustness and interpretability.

Model Training: Performed training with hyperparameter tuning.

Model Saving: Saved trained model and scaler using Joblib for reuse.

Deployment: Built an interactive UI in Streamlit for predictions.

6. Implementation & Tech Stack
Component	Technology
Model	Random Forest (Scikit-Learn)
Preprocessing	StandardScaler (Scikit-Learn)
Imbalance Handling	SMOTE (imbalanced-learn)
Persistence	Joblib
Deployment UI	Streamlit
Language	Python

7. Model Performance & Evaluation
Accuracy: ~0.81

ROC-AUC Score: ~0.90

Confusion Matrix:  [[78 22]
                   [16 84]]

Classification Report: Precision, Recall, and F1-score. 

       precision    recall  f1-score   support

           0       0.83      0.78      0.80       100
           1       0.79      0.84      0.82       100

    accuracy                           0.81       200
   macro avg       0.81      0.81      0.81       200
weighted avg       0.81      0.81      0.81       200

Cross-validation: 0.82

10. How to Run Locally
bash
Copy
Edit
# Clone repository
git clone https://github.com/Gunjan712Sehrawat/diabetes-streamlit-app.git
cd diabetes-streamlit-app

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py
11. Results
The app allows users to enter their health parameters and instantly receive a prediction of diabetes risk. Model evaluation shows good performance on test data, with strong ROC-AUC and balanced accuracy across classes.


12. Conclusion
The Diabetes Risk Prediction app successfully integrates a machine learning model with a user-friendly web interface. While it performs well on the dataset used, real-world deployment would require validation with more diverse, recent data and possible integration with medical guidelines.


