from pathlib import Path
from parsers.pdf_reader import extract_pdf_text
from parsers.docx_reader import extract_docx_text
from parsers.text_cleaner import clean_resume_text
def parse_resume(file_path):
    """
    Extract and clean text from PDF or DOCX resumes.
    """

    file_path = Path(file_path)

    extension = file_path.suffix.lower()

    if extension not in [".pdf", ".docx"]:
        raise ValueError("Only PDF and DOCX files are supported.")

    if not file_path.exists():
        raise FileNotFoundError(f"Resume not found: {file_path}")

    if extension == ".pdf":
        extraction_result = extract_pdf_text(file_path)

    else:
        extraction_result = extract_docx_text(file_path)

    raw_text = extraction_result["raw_text"]
    cleaned_text = clean_resume_text(raw_text)

    return {
        "file_name": file_path.name,
        "file_type": extension.replace(".", ""),
        "raw_text": raw_text,
        "cleaned_text": cleaned_text,
        "warnings": extraction_result.get("warnings", [])
    }
