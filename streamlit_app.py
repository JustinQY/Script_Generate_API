import streamlit as st
import requests

st.title("LLaMA2 TV Script Generator")
prompt = st.text_area("Enter your prompt:")

if st.button("Generate"):
    with st.spinner("Generating..."):
        response = requests.post(
            "http://localhost:8000/generate",
            json={"prompt": prompt}
        )

        if response.ok:
            st.markdown("### Output")
            st.write(response.json()["generated_script"])
        else:
            st.error("Something went wrong.")
