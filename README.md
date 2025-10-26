AI Resume Screener

An end-to-end Streamlit web application that uses AI embeddings to evaluate how well a candidate’s resume matches a given job description.
This project applies Natural Language Processing (NLP) and semantic similarity modeling to automate resume screening 

#Features

Upload Resume (PDF) - Extracts text automatically using PyMuPDF  
Paste Job Description - Input any job posting text  
AI-Powered Matching – Uses SentenceTransformer (`all-MiniLM-L6-v2`) to compare resume and job description  
Match Score (%) - Displays similarity percentage between 0–100  
Smart Feedback– Categorizes results as Excellent, Good, or Needs Improvement 
Progress Spinner: Interactive, responsive Streamlit UI  
Deployable - Can be hosted on Streamlit Cloud or Hugging Face Spaces  


#Installation & Setup
1. Clone this repository
2. Create a virtual environment
conda create -n resume_screener python=3.12
conda activate resume_screener
3. Install dependencies
pip install -r requirements.txt
4. Run the Streamlit app
streamlit run app.py
