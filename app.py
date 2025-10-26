import streamlit as st
import fitz  # PyMuPDF for PDF text extraction
from sentence_transformers import SentenceTransformer, util

# Must be the first Streamlit command
st.set_page_config(page_title="AI Resume Screener", layout="wide")

# Load model (cached so it doesn't reload every time)
@st.cache_resource
def load_model():
    return SentenceTransformer('all-MiniLM-L6-v2')

model = load_model()

# Page Title and Instructions
st.title("🤖 AI Resume Screener")
st.write("Upload your resume and a job description to check how well they match.")

# Upload resume PDF and job description input
uploaded_resume = st.file_uploader("📄 Upload your Resume (PDF only)", type=["pdf"])
job_description = st.text_area("💼 Paste the Job Description here")

# Analyze button
if st.button("Analyze Match"):
    if uploaded_resume is not None and job_description.strip() != "":
        with st.spinner("Analyzing your resume... Please wait ⏳"):
            # Extract text from PDF
            pdf = fitz.open(stream=uploaded_resume.read(), filetype="pdf")
            resume_text = "".join(page.get_text() for page in pdf)

            # Encode both texts
            resume_emb = model.encode(resume_text, convert_to_tensor=True)
            job_emb = model.encode(job_description, convert_to_tensor=True)

            # Calculate similarity
            similarity = util.pytorch_cos_sim(resume_emb, job_emb)
            score = float(similarity.item()) * 100

        # Display the result
        st.subheader(f"✅ Resume Match Score: {score:.2f}%")
        if score > 80:
            st.success("Excellent Match! Your resume strongly aligns with the job description.")
        elif score > 60:
            st.info("Good Match! You meet many of the job's requirements.")
        else:
            st.warning("Weak Match. Consider tailoring your resume to this job.")
    else:
        st.error("⚠️ Please upload a resume and paste a job description.")
