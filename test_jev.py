from laya import Router


router = Router()


state = {
    "body": """
    Hemant is a Data Engineer.

    He has experience with Python, SQL, AWS and PySpark.

    He has built ETL pipelines using PySpark and AWS.
    """
}


questions = {

    "python": {
        "type": "choice",
        "instructions": "Does the candidate have Python experience?",
        "criteria": {
            "yes": "The resume clearly provides evidence of Python experience.",
            "no": "The resume does not provide evidence of Python experience."
        }
    },

    "aws": {
        "type": "choice",
        "instructions": "Does the candidate have AWS experience?",
        "criteria": {
            "yes": "The resume clearly provides evidence of AWS experience.",
            "no": "The resume does not provide evidence of AWS experience."
        }
    },

    "kafka": {
        "type": "choice",
        "instructions": "Does the candidate have Kafka experience?",
        "criteria": {
            "yes": "The resume clearly provides evidence of Kafka experience.",
            "no": "The resume does not provide evidence of Kafka experience."
        }
    },

    "etl": {
        "type": "score",
        "instructions": (
            "How strongly does the candidate satisfy "
            "the requirement of building ETL pipelines?"
        ),
        "criteria": [
            "No evidence",
            "Weak evidence",
            "Partial evidence",
            "Strong evidence",
            "Very strong evidence"
        ]
    }
}


result = router.predict(
    state=state,
    questions=questions
)


print(result)