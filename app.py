import streamlit as st
from docx import Document

def extract_docx_text(uploaded_file):
    document = Document(uploaded_file)

    paragraphs = []

    for paragraph in document.paragraphs:
        text = paragraph.text.strip()

        if text:
            paragraphs.append(text)

    return "\n".join(paragraphs)

def find_skills(text):
    skills = [
        "aws",
        "azure",
        "linux",
        "python",
        "docker",
        "kubernetes",
        "terraform",
        "jenkins",
        "git",
        "github",
        "ci/cd",
        "postgresql",
        "mongodb",
        "openstack",
        "ceph",
        "networking",
        "ansible",
    ]

    text_lower = text.lower()
    found_skills = []

    for skill in skills:
        if skill.lower() in text_lower:
            found_skills.append(skill)

    return found_skills


st.set_page_config(
    page_title="SponsorFit",
    page_icon="🎯",
    layout="wide",
)

st.title("🎯 SponsorFit")

st.subheader("Find your gaps. Build the evidence. Apply stronger.")

st.write(
    "Compare your CV with a job description, understand your skill gaps, "
    "and get practical project recommendations to strengthen your evidence."
)

st.divider()

with st.form("job_analysis_form"):

    cv_file = st.file_uploader(
        "Upload your CV",
        type=["pdf", "docx"],
    )

    job_description = st.text_area(
        "Paste the job description",
        height=300,
        placeholder="Paste the full job description here...",
    )

    analyse_button = st.form_submit_button("Analyse Job")


if analyse_button:

    if cv_file is None:
        st.warning("Please upload your CV.")

    elif not job_description.strip():
        st.warning("Please paste a job description.")

    else:
        if cv_file.name.lower().endswith(".docx"):

            cv_text = extract_docx_text(cv_file)
            cv_skills = find_skills(cv_text)
            jd_skills = find_skills(job_description)
   
            matched_skills = [
                skill for skill in jd_skills
                if skill in cv_skills
            ] 

            missing_skills = [
                skill for skill in jd_skills
                if skill not in cv_skills
            ]    



            st.success(
                "CV and job description received successfully."
            )

            st.subheader("CV text extracted")

            with st.expander("View extracted CV"):
                st.text(cv_text)
            st.divider()
            st.subheader("Skill Match")

            col1, col2 = st.columns(2)

            with col1:
                st.markdown("### ✅ Evidence found in CV")

                if matched_skills:
                    st.markdown(
                        "<br>".join(
                            f"• {skill}" for skill in matched_skills
                        ),
                        unsafe_allow_html=True,
                    )
                else:
                    st.write("No matching skills found.")

            with col2:
                st.markdown(
                    "### ⚠️ Skills mentioned in JD but not found in CV"
                )

                if missing_skills:
                    st.markdown(
                        "<br>".join(
                            f"• {skill}" for skill in missing_skills
                        ),
                        unsafe_allow_html=True,
                    )
                else:
                    st.write("No missing skills found.")

        else:
            st.warning(
                "PDF reading will be added next. "
                "For now, please upload a DOCX CV."
            )
