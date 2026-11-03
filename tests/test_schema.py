
import json
from jsonschema import validate

def test_resume_schema():
    with open("schemas/resume_schema.json", "r") as file:
        schema = json.load(file)

    sample_resume = {
        "candidate_id": "CAND001",
        "personal_information": {
            "full_name": "Arun Kumar",
            "email": "arun@example.com"
        },
        "skills": [],
        "education": [],
        "experience": [],
        "certifications": []
    }

    validate(instance=sample_resume, schema=schema)
