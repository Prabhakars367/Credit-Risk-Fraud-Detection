# 💳 Credit Risk & Fraud Detection App

This is a production-ready **Streamlit web application** that predicts the likelihood of a **credit card transaction being fraudulent** using a trained machine learning model. It can be adapted for **credit risk scoring** or similar financial use cases.

---

## 🚀 Live Demo (Optional)

👉 [Click to Launch App](https://your-huggingface-space-link)  
👉 [Watch Demo Video](https://your-youtube-link)

---

## 🧠 Project Overview

Financial institutions face growing challenges in identifying fraud in real-time. This project tackles that using:
- ✅ A robust classification model
- ✅ Streamlit interface for easy user interaction
- ✅ Instant predictions on uploaded transaction data

---

## 📊 Dataset

We use the popular **Kaggle Credit Card Fraud Detection Dataset**:
- 284,807 transactions
- 492 frauds (severely imbalanced dataset)
- Feature engineered using PCA
- [Dataset Link](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)

---

## 📦 Features

- Upload CSV of transaction records
- Predict fraud in real-time
- See prediction output directly in browser
- Built using Python, scikit-learn, Streamlit
- (Optional) Deployable on Hugging Face Spaces or AWS

---

## 📁 Folder Structure

```
credit-risk-detector/
├── app/
│   ├── main.py            # Streamlit UI
│   ├── model.pkl          # Trained ML model
├── data/
│   └── creditcard.csv     # Input dataset
├── notebooks/
│   └── eda_modeling.ipynb # Model training + EDA
├── requirements.txt
└── README.md
```

---

## 🧪 Tech Stack

- Python 🐍  
- scikit-learn  
- Pandas / NumPy  
- Streamlit  
- Joblib  
- (Optional: Docker, Hugging Face, AWS)

---

## 🛠️ How to Run Locally

1. Clone this repo  
```bash
git clone https://github.com/your-username/credit-risk-detector.git
cd credit-risk-detector
```

2. Install requirements  
```bash
pip install -r requirements.txt
```

3. Run the Streamlit app  
```bash
streamlit run app/main.py
```

4. Upload your transaction CSV file and get instant predictions.

---

## 📈 Model Details

- **Type**: Random Forest Classifier  
- **Handling Imbalance**: Class weights  
- **Evaluation**: Precision, Recall, F1-Score, ROC-AUC  
- **Performance**: Achieved F1-score ~0.92 on test data

---

## 🎯 Future Improvements

- Add SHAP-based interpretability  
- Extend to credit scoring use case  
- Real-time fraud stream monitoring  
- CI/CD pipeline + monitoring with Airflow/Grafana

---

## 🧑‍💼 Author

**Prabhakar Kumar Singh**  
📫 [LinkedIn](https://www.linkedin.com/in/prabhakars367/)  
📧 prabhakars367@gmail.com

---

## 🛡️ License

This project is open source under the MIT License.
