# 🎯 SponsorFit

A small Streamlit web app that compares a CV with a job description and shows which technical skills from the job description appear in the CV, and which do not.

> **Status: early prototype (in progress).** See [Current limitations](#current-limitations) and [Roadmap](#roadmap).

## What it does

1. You upload your CV as a **Word (.docx)** file.
2. You paste a job description.
3. The app extracts the text from your CV and checks both texts for a fixed list of technical skills.
4. It shows two lists:
   - ✅ **Evidence found in CV** – skills the job asks for that also appear in your CV
   - ⚠️ **Skills mentioned in JD but not found in CV** – your gaps for this job

Skills currently checked: AWS, Azure, Linux, Python, Docker, Kubernetes, Terraform, Jenkins, Git, GitHub, CI/CD, PostgreSQL, MongoDB, OpenStack, Ceph, networking, Ansible.

## Tech stack

- Python
- [Streamlit](https://streamlit.io/) – web interface
- [python-docx](https://python-docx.readthedocs.io/) – reading text from Word CVs

## Run it locally

```bash
git clone <this-repo-url>
cd sponsorfit
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

Then open the address Streamlit prints (usually http://localhost:8501).

## Current limitations

- **DOCX only.** The upload box accepts PDF, but PDF reading is not built yet; the app asks you to upload a DOCX instead.
- **Simple keyword matching.** A skill counts as "found" if its name appears anywhere in the text, so short names can give false matches (for example `git` also matches inside `github`).
- **Fixed skill list.** Only the 17 skills above are checked.
- **No project recommendations yet**, even though this is the long-term goal (see below).

## Roadmap

- [ ] Read PDF CVs
- [ ] Match whole words only, to avoid false matches
- [ ] Load the skill list from a file in `data/` instead of hard-coding it
- [ ] Suggest a practical project for each missing skill
- [ ] Add unit tests in `tests/`
- [ ] Deploy to the cloud

## Author

Janvi Patel – [GitHub](https://github.com/janvipatel1910)
