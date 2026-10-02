import streamlit as st
from dotenv import load_dotenv

from resume_parser import extract_resume_text
from llm_analyzer import analyze_job_description
from laya_evaluator import evaluate_resume
from scoring import calculate_score


load_dotenv()


st.set_page_config(
    page_title="Resume Scanner",
    page_icon="📄"
)


st.title("📄 Resume Scanner")

st.write(
    "Upload your resume and paste a job description "
    "to calculate your resume match score."
)


# --------------------------------
# Resume
# --------------------------------

resume_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)


# --------------------------------
# Job Description
# --------------------------------

job_description = st.text_area(
    "Paste Job Description",
    height=300
)


# --------------------------------
# Analyze
# --------------------------------

if st.button("Analyze Resume"):

    if resume_file is None:

        st.error("Please upload your resume.")

        st.stop()

    if not job_description.strip():

        st.error("Please enter a job description.")

        st.stop()

    with st.spinner("Reading resume..."):

        resume_text = extract_resume_text(
            resume_file
        )

    with st.spinner(
        "Analyzing job description..."
    ):

        requirements = analyze_job_description(
            job_description
        )

    with st.spinner(
        "Comparing resume with requirements..."
    ):

        laya_result = evaluate_resume(
            resume_text,
            requirements
        )

    score = calculate_score(

        laya_result,

        len(requirements.get(
            "skills",
            []
        )),

        len(requirements.get(
            "requirements",
            []
        ))
    )

    # --------------------------------
    # Result
    # --------------------------------

    st.success("Analysis complete!")

    st.metric(
        "Resume Match Score",
        f"{score['final_score']}%"
    )

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Skills Match",
            f"{score['skills_score']}%"
        )

    with col2:

        st.metric(
            "Requirements Match",
            f"{score['requirements_score']}%"
        )

    # --------------------------------
    # Details
    # --------------------------------

    with st.expander(
        "View Extracted Job Requirements"
    ):

        st.json(requirements)

    with st.expander(
        "View Laya Evaluation"
    ):

        st.json(laya_result)