import streamlit as st
import pandas as pd
import joblib
import io
from docx import Document
import pdfplumber

# Load model and get expected features
model = joblib.load("model.pkl")
expected_features = list(model.feature_names_in_)

st.title("📁 Fraud Detection App: Multi-Format Upload")

uploaded_file = st.file_uploader("Upload a CSV, Excel, PDF, or Word file", type=["csv", "xlsx", "xls", "pdf", "docx"])

def parse_file(file):
    if file.name.endswith(".csv"):
        return pd.read_csv(file)
    elif file.name.endswith((".xlsx", ".xls")):
        return pd.read_excel(file)
    elif file.name.endswith(".pdf"):
        with pdfplumber.open(file) as pdf:
            all_text = []
            for page in pdf.pages:
                table = page.extract_table()
                if table:
                    df = pd.DataFrame(table[1:], columns=table[0])
                    all_text.append(df)
            return pd.concat(all_text, ignore_index=True) if all_text else None
    elif file.name.endswith(".docx"):
        doc = Document(file)
        all_tables = []
        for table in doc.tables:
            data = [[cell.text for cell in row.cells] for row in table.rows]
            df = pd.DataFrame(data[1:], columns=data[0])  # header = first row
            all_tables.append(df)
        return pd.concat(all_tables, ignore_index=True) if all_tables else None
    else:
        return None

if uploaded_file:
    try:
        input_df = parse_file(uploaded_file)
        if input_df is None:
            st.error("❌ Could not parse file. Ensure it contains a readable table.")
        else:
            st.write("📄 Parsed Table Preview", input_df.head())

            missing = [col for col in expected_features if col not in input_df.columns]
            if missing:
                st.error(f"⚠️ Missing features: {missing}")
            else:
                X = input_df[expected_features]
                preds = model.predict(X)
                input_df["Prediction"] = preds
                st.success("✅ Prediction Done")
                st.write("🔍 Results", input_df)

                csv_out = input_df.to_csv(index=False).encode("utf-8")
                st.download_button("📥 Download Result CSV", csv_out, file_name="results.csv")
    except Exception as e:
        st.error(f"❌ Error: {e}")
