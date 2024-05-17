import streamlit as st
import PyPDF2
import os
import google.generativeai as generativeai

API_KEY = "AIzaSyD0IfrdxVDYjuvYL_A24546Y2lF0WbNaFM"
generativeai.configure(api_key=API_KEY)

pdf_file = st.file_uploader("Upload PDF")

def generate_gemini_content(prompt, input_text):
  model = generativeai.GenerativeModel("gemini-pro")
  response = model.generate_content(prompt + input_text)
  return response.text

if pdf_file is not None:
  try:
    with open("temp.pdf", "wb") as f:
      f.write(pdf_file.read())
    with open("temp.pdf", "rb") as f:
      pdf_reader = PyPDF2.PdfReader(f)
      pdf_text = ""
      for page in pdf_reader.pages:
        pdf_text += page.extract_text()

    os.remove("temp.pdf")
  except Exception as e:
    st.error(f"Error reading PDF: {e}")
    st.stop()

  question = st.text_input("Ask a question about the PDF:")
  model = generativeai.GenerativeModel("gemini-pro")
  if question:
    try:
      input_text = pdf_text
      prompt = question
      answer = generate_gemini_content(prompt, input_text)
      answers = answer.split("\n")
      if not answers:
        st.warning("No response generated. Check prompt feedback for details.")
      else:
        st.write(f"Answer: {answers}")
    except Exception as e:
      st.error(f"Error calling API: {e}")
