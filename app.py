import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load API Key
load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

st.set_page_config(
    page_title="AI Code Explainer",
    page_icon="💻",
    layout="wide"
)

st.title("💻 AI Python Code Explainer")
st.write("Paste any Python code below and let Gemini explain it.")

code = st.text_area(
    "Paste Python Code",
    height=300,
    placeholder="Paste your Python code here..."
)

if st.button("Explain Code"):

    if code.strip() == "":
        st.warning("Please paste some code.")
    else:

        prompt = f"""
You are an expert Python mentor.

Analyze the following Python code.

Return the response in this format.

# 1. Summary
Explain what the program does in simple English.

# 2. Line-by-Line Explanation
Explain important sections.

# 3. Functions Used
Explain every function and its purpose.

# 4. Time Complexity
Mention complexity with explanation.

# 5. Bugs or Possible Errors
Mention any bugs.

# 6. Improvements
Suggest improvements.

# 7. Optimized Version
Rewrite the code using better Python practices.

Python Code:

{code}
"""

        with st.spinner("Analyzing..."):

            response = model.generate_content(prompt)

            st.success("Analysis Complete!")

            st.markdown(response.text)
