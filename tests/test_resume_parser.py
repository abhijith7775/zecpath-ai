
import pytest

from parsers.resume_parser import parse_resume


def test_parse_pdf():
    result = parse_resume("data/raw/resumes/sample_resume.pdf")

    assert result["file_type"] == "pdf"
    assert result["raw_text"]
    assert result["cleaned_text"]


def test_parse_docx():
    result = parse_resume("data/raw/resumes/sample_resume.docx")

    assert result["file_type"] == "docx"
    assert result["raw_text"]
    assert result["cleaned_text"]


def test_unsupported_file():
    with pytest.raises(ValueError):
        parse_resume("sample.txt")


def test_missing_file():
    with pytest.raises(FileNotFoundError):
        parse_resume("missing_resume.pdf")
