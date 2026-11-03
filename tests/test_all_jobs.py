
import json
from pathlib import Path
from jsonschema import validate


def test_all_job_descriptions():

    schema_path = Path("schemas/job_schema.json")
    job_folder = Path("data/raw/job_descriptions")

    with open(schema_path, "r", encoding="utf-8") as file:
        schema = json.load(file)

    job_files = list(job_folder.glob("JOB*.json"))

    assert len(job_files) == 10

    for job_file in job_files:
        with open(job_file, "r", encoding="utf-8") as file:
            job = json.load(file)

        validate(instance=job, schema=schema)
