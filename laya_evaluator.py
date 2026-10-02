from laya import Router


router = Router()


def evaluate_resume(resume_text, requirements):

    questions = {}

    # -------------------------
    # Skills
    # -------------------------

    skills = requirements.get("skills", [])

    for index, skill in enumerate(skills):

        question_id = f"skill_{index}"

        questions[question_id] = {
            "type": "choice",

            "instructions": (
                f"Does the candidate have experience with {skill}?"
            ),

            "criteria": {
                "yes": (
                    f"The resume clearly provides evidence "
                    f"of experience with {skill}."
                ),

                "no": (
                    f"The resume does not provide evidence "
                    f"of experience with {skill}."
                )
            }
        }

    # -------------------------
    # Requirements
    # -------------------------

    job_requirements = requirements.get(
        "requirements",
        []
    )

    for index, requirement in enumerate(job_requirements):

        question_id = f"requirement_{index}"

        questions[question_id] = {
            "type": "score",

            "instructions": (
                f"How strongly does the candidate satisfy "
                f"this job requirement:\n{requirement}"
            ),

            "criteria": [
                "No evidence",
                "Weak evidence",
                "Partial evidence",
                "Strong evidence",
                "Very strong evidence"
            ]
        }

    # -------------------------
    # Laya input
    # -------------------------

    state = {
        "body": resume_text
    }

    result = router.predict(
        state=state,
        questions=questions
    )

    return result