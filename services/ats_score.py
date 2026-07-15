def calculate_ats_score(resume_text, job_description):
    resume_text = resume_text.lower()
    job_description = job_description.lower()

    keywords = job_description.split()
    matched_keywords = []

    for word in keywords:
        if word in resume_text and word not in matched_keywords:
            matched_keywords.append(word)

    if len(keywords) == 0:
        return 0, []

    score = int((len(matched_keywords) / len(set(keywords))) * 100)

    return min(score, 100), matched_keywords