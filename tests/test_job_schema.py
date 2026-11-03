
import json
from jsonschema import validate


def test_job_schema():

    with open("schemas/job_schema.json", "r") as file:
        schema = json.load(file)

    sample_job = {
        "job_id": "JOB001",
        "job_title": "Python Developer",
        "company": "Zecpath",
        "job_type": "full-time",
        "required_skills": [
            {
                "skill_name": "Python",
                "category": "technical",
                "is_mandatory": True
            }
        ],
        "experience_requirements": {
            "minimum_years": 1,
            "maximum_years": 3,
            "experience_level": "entry-level"
        },
        "responsibilities": [
            "Develop Python applications",
            "Maintain backend services"
        ]
    }

    validate(instance=sample_job, schema=schema)
