import streamlit as st
import google.generativeai as genai

# 1. Set up the web page layout
st.set_page_config(page_title="AI Diagram Generator", layout="centered")
st.title("📊 Auto-Infographic Generator")
st.write("Paste your raw notes below, and the AI will generate a visual diagram.")

# 2. Securely load your Gemini API key from Streamlit's hidden secrets
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-3.8-flash')

# 3. Create the text input box for the user
raw_text = st.text_area("Raw Data / Notes", height=200, placeholder="Paste raw notes, summaries, or tables here...")

# 4. The action button
if st.button("Generate Infographic"):
    if raw_text:
        with st.spinner("Analyzing data and drawing diagram..."):
            # The prompt that acts as your "Editor" and "Designer"
            prompt = f"""
            You are an expert data visualizer. Read the following raw text and extract the core process, hierarchy, or summary.
            Convert it into a Mermaid.js flowchart.
            Return ONLY the valid Mermaid code block, starting with ```mermaid and ending with ```. Do not add any other text.
            
            Raw text: {raw_text}
            """
            
            # Call Gemini and render the result
            response = model.generate_content(prompt)
            st.markdown(response.text) # Streamlit automatically turns Mermaid code into a visual graphic!
    else:
        st.warning("Please enter some text first.")