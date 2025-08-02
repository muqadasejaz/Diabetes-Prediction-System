# 🩺 Diabetes Prediction System

The Diabetes Prediction System is a machine learning-powered tool designed to assist in the early detection of diabetes based on diagnostic medical parameters.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 🔍 Project Overview

**Diabetes Prediction System** is a machine learning-based application that predicts whether a person is diabetic based on key medical attributes. This tool is designed to assist in early detection using an easy-to-use graphical interface powered by **Streamlit**.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 🚀 Project Features

- 📊 **Predictive Model** trained on the Pima Indians Diabetes Dataset.
  
- 🧠 Uses **Support Vector Machine (SVM)** for binary classification.
  
- 📈 **Data preprocessing & scaling** using StandardScaler.
  
- 🧪 Real-time predictions via **interactive Streamlit GUI**.
  
- 💾 Model persistence using **Joblib**.
  
- 🔁 Allows **multiple predictions** through clean user inputs.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 📂 Dataset

- **Name:** [Diabetes Dataset](https://www.kaggle.com/datasets/muqaddasejaz/diabetes-dataset)
  
- **Source:** UCI Machine Learning Repository / Kaggle
  
- **Attributes:**
  - Pregnancies
  - Glucose
  - Blood Pressure
  - Skin Thickness
  - Insulin
  - BMI
  - Diabetes Pedigree Function
  - Age
  - Outcome (Label: 1 = Diabetic, 0 = Not Diabetic)

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 📊 Results

- **Model Used:** SVM (Linear Kernel)
- **Accuracy:** ~78% on test split
- **Performance Metrics:**
  
- Accuracy, Classification Report:

  <img width="801" height="199" alt="classification_report" src="https://github.com/user-attachments/assets/6611cf85-6c31-4b0b-8c4b-0d3dc097d0ad" />

- Confusion Matrix:
  
  <img width="365" height="317" alt="image" src="https://github.com/user-attachments/assets/baf5082b-d2e4-453a-9738-02e7b9c96e97" />

- Predictions:
  
<img width="806" height="409" alt="predictions" src="https://github.com/user-attachments/assets/6edd2e1e-7431-4ab4-82c9-ed499f039923" />

<img width="772" height="437" alt="prediction" src="https://github.com/user-attachments/assets/a9b9211b-7e69-4680-a705-ad2eee34faf2" />


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 🧰 Tools & Technologies

- **Python** 🐍
- **Pandas** for data manipulation
- **Scikit-learn** for machine learning
- **Streamlit** for GUI/web interface
- **Joblib** for saving/loading model and scaler

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 💻 Graphical User Interface (GUI)

- Built using **Streamlit**.
- Takes user inputs for 8 health metrics.
- Predicts and displays whether the user is **Diabetic** or **Not Diabetic**.
- Can be launched locally with one command:
  ```bash
  streamlit run app.py

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 📚 References

-  Diabetes Database: [Dataset](https://www.kaggle.com/datasets/muqaddasejaz/diabetes-dataset)

- https://pmc.ncbi.nlm.nih.gov/articles/PMC10107388/

- https://www.nature.com/articles/s41598-024-51438-4

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 👤 Author

Muqadas Ejaz

BS Computer Science (AI Specialization)

Machine Learning & Computer Vision Enthusiast

📫 Connect with me on [LinkedIn](https://www.linkedin.com/in/muqadasejaz/)  

🌐 GitHub: [github.com/muqadasejaz](https://github.com/muqadasejaz)

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 📎 License

This project is open-source and available under the [MIT License](LICENSE).
