def calculate_score(
    laya_result,
    number_of_skills,
    number_of_requirements
):

    answers = laya_result["answers"]

    skill_scores = []
    requirement_scores = []

    # -------------------------
    # Skills
    # -------------------------

    for i in range(number_of_skills):

        key = f"skill_{i}"

        answer = answers[key]

        if answer["choice"] == "yes":
            score = 100
        else:
            score = 0

        skill_scores.append(score)

    # -------------------------
    # Requirements
    # -------------------------

    for i in range(number_of_requirements):

        key = f"requirement_{i}"

        answer = answers[key]

        raw_score = answer["score"]

        score = (raw_score / 4) * 100

        requirement_scores.append(score)

    # -------------------------
    # Category scores
    # -------------------------

    skills_score = (
        sum(skill_scores) / len(skill_scores)
        if skill_scores
        else 0
    )

    requirements_score = (
        sum(requirement_scores) / len(requirement_scores)
        if requirement_scores
        else 0
    )

    # -------------------------
    # Final score
    # -------------------------

    final_score = (
        skills_score * 0.60
        +
        requirements_score * 0.40
    )

    return {
        "final_score": round(final_score, 2),
        "skills_score": round(skills_score, 2),
        "requirements_score": round(
            requirements_score,
            2
        ),
        "skill_scores": skill_scores,
        "requirement_scores": requirement_scores
    }