import streamlit as st
import pandas as pd
import ollama
from openai import OpenAI# Constants
CSV_FILE_PATH = 'input2.csv'  # Replace with your actual file path
IMAGE_PATH = 'VN-German-trade.jpg'  # Uploaded image path

# Function to load the HS code data
@st.cache_data
def load_hs_data():
    # Read the CSV file, skipping initial rows if necessary
    df = pd.read_csv(CSV_FILE_PATH, skiprows=4)  # Adjust skiprows based on your file's structure

    # Display the first few rows to understand its structure
    st.write("Preview of the loaded data:")
    st.write(df.head())

    # Check the number of columns
    num_columns = df.shape[1]

    # Define column names based on the number of columns
    if num_columns == 3:
        df.columns = ['HS Code', 'Description (Vietnamese)', 'Unused']
        # Drop the 'Unused' column
        df = df.drop(columns=['Unused'])
    elif num_columns == 2:
        df.columns = ['HS Code', 'Description (Vietnamese)']
    else:
        st.error(f"Unexpected number of columns: {num_columns}. Please check the CSV file.")
        return pd.DataFrame()  # Return an empty DataFrame in case of unexpected structure

    # Drop any completely empty rows
    df = df.dropna(subset=['HS Code', 'Description (Vietnamese)'], how='all')

    # Fill HS Code downward (some sub-rows may not have it)
    df['HS Code'] = df['HS Code'].fillna(method='ffill')

    return df

# LLM Query Function
def extract_hs_code(question, csv_data):
    prompt = f"""
    You are an expert in international trade classifications. Based on the following HS code data:

    {csv_data}

    Please provide the correct HS code for the following query:

    "{question}"

    Respond with only the HS code.
    """
    # response = ollama.chat(model='deepseek-r1:7b', messages=[{'role': 'user', 'content': prompt}])
    # return response['message']['content'].strip()
    # Query the GPT-4o model
    
    client=OpenAI()
    completion = client.chat.completions.create(
            model="o3-mini",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
    return completion.choices[0].message

# Page Setup
st.set_page_config(page_title="Vietnam-Germany HS Code Finder", layout="centered")

# Injecting Custom CSS
st.markdown("""
    <style>
    .main {
        background-color: #f4f7f9;
        padding: 2rem;
        font-family: 'Segoe UI', sans-serif;
    }
    h1, h2 {
        text-align: center;
        color: #202a44;
    }
    .stButton button {
        background-color: #202a44;
        color: white;
        font-weight: bold;
        border-radius: 0.5rem;
        padding: 0.5rem 1.5rem;
    }
    .stTextArea textarea {
        font-size: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# Display the image
st.image(IMAGE_PATH, use_column_width=True)

# Title and instructions
st.title("Vietnam-Germany HS Code Finder 🇩🇪🇻🇳")
st.subheader("🔍 Enter your trade question below to find the correct HS Code.")

# Load the data
hs_data = load_hs_data()

# Check if the data is loaded successfully
if not hs_data.empty:
    # Question Input
    question = st.text_area("✏️ Your trade-related query", height=120)

    # Button
    if st.button("🔎 Find HS Code"):
        if question:
            csv_text = hs_data.to_csv(index=False)
            hs_code = extract_hs_code(question, csv_text)
            st.success(f"✅ The correct HS code is: **{hs_code}**")
        else:
            st.warning("⚠️ Please enter a query to search for the HS code.")
else:
    st.error("Failed to load HS code data. Please check the CSV file.")
