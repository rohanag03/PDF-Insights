# PDF Content Analyzer

This project utilizes the power of Google's Generative AI to analyze and answer questions about the content of PDF documents. It provides a user-friendly interface to upload PDFs and ask questions, receiving insightful answers generated by the Gemini AI model.

## Prerequisites

Make sure you have Python installed on your system. Additionally, install the required dependencies with the following command:

```bash
pip install -r requirements.txt
```

## Features

- Upload PDF documents for analysis.
- Ask questions about the uploaded PDF content.
- Utilize the Gemini AI model to generate answers.
- Streamlit-based web interface for ease of use.

## How to Use

1. Run the Streamlit app by executing the following command in your terminal:
```bash
streamlit run main.py
```
2. Upload a PDF document using the provided file uploader.
3. Enter your question about the PDF content in the text input field.
4. View the generated answers based on the PDF content.

## File Structure

- main.py: The main application script for the Streamlit interface.
- requirements.txt: A list of Python libraries required for the project.

## Usage Notes

- The application requires an API key from Google Generative AI, which should be kept confidential.
- The PDF content is processed and stored temporarily for analysis.

## Further Development

- Support for Large Documents: Future updates will aim to optimize the processing of large PDF documents to ensure efficient analysis without compromising performance.
