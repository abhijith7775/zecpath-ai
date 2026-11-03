
import json
from pathlib import Path


def save_parsed_resume(result, output_dir="data/processed/resumes"):
    """
    Save extracted and cleaned resume data as JSON.
    """

    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    file_name = Path(result["file_name"]).stem + ".json"
    output_path = output_dir / file_name

    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(result, file, indent=4, ensure_ascii=False)

    return output_path


if __name__ == "__main__":
    from parsers.resume_parser import parse_resume

    resume_path = "data/raw/resumes/sample_resume.pdf"

    result = parse_resume(resume_path)
    saved_path = save_parsed_resume(result)

    print(f"Resume successfully saved: {saved_path}")
