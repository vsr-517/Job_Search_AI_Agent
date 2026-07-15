from google import genai
from config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)

def get_resume_feedback(resume_text, job_description):
    prompt = f"""
Analyze this resume for the given job description.

Resume:
{resume_text[:4000]}

Job Description:
{job_description[:3000]}

Give feedback in short points:
1. Resume strengths
2. Missing skills
3. ATS improvement tips
4. Career advice
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text


def get_company_research(company_name, job_role):
    prompt = f"""
Give short company research for a job seeker.

Company: {company_name}
Job Role: {job_role}

Include:
1. Company overview
2. Skills needed for this role
3. Interview preparation tips
4. Why this company may be useful for career growth
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text