
import json
from pathlib import Path
from jsonschema import validate


def test_all_resume_files():
    schema_path = Path("schemas/resume_schema.json")
    resume_folder = Path("data/raw/resumes")

    with open(schema_path, "r", encoding="utf-8-sig") as file:
        schema = json.load(file)

    resume_files = list(resume_folder.glob("CAND*.json"))

    assert len(resume_files) == 10, "Expected exactly 10 resumes"

    for resume_file in resume_files:
        with open(resume_file, "r", encoding="utf-8-sig") as file:
            resume = json.load(file)

        validate(instance=resume, schema=schema)
