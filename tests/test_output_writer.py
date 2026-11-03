
import json
from pathlib import Path

from parsers.output_writer import save_parsed_resume


def test_save_parsed_resume(tmp_path):
    sample_result = {
        "file_name": "sample_resume.pdf",
        "file_type": "pdf",
        "raw_text": "Python Developer",
        "cleaned_text": "Python Developer",
        "warnings": []
    }

    output_path = save_parsed_resume(
        sample_result,
        output_dir=tmp_path
    )

    assert output_path.exists()
    assert output_path.name == "sample_resume.json"

    with open(output_path, "r", encoding="utf-8") as file:
        saved_data = json.load(file)

    assert saved_data["raw_text"] == "Python Developer"
    assert saved_data["cleaned_text"] == "Python Developer"
    assert saved_data["file_type"] == "pdf"
