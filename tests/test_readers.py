
import pymupdf as fitz
from docx import Document

from parsers.pdf_reader import extract_pdf_text
from parsers.docx_reader import extract_docx_text


def test_pdf_reader(tmp_path):
    pdf_path = tmp_path / "sample_resume.pdf"

    # Create sample PDF
    pdf = fitz.open()
    page = pdf.new_page()
    page.insert_text(
        (50, 50),
        "Arun Kumar\nPython Developer\nSkills: Python, SQL"
    )
    pdf.save(pdf_path)
    pdf.close()

    # Extract text
    result = extract_pdf_text(pdf_path)

    assert result["file_type"] == "pdf"
    assert result["page_count"] == 1
    assert "Arun Kumar" in result["raw_text"]
    assert "Python" in result["raw_text"]


def test_docx_reader(tmp_path):
    docx_path = tmp_path / "sample_resume.docx"

    # Create sample DOCX
    document = Document()

    document.add_heading("Arun Kumar", level=1)
    document.add_paragraph("Python Developer")
    document.add_paragraph("Skills: Python, SQL")

    # Add sample table
    table = document.add_table(rows=1, cols=2)
    table.cell(0, 0).text = "Education"
    table.cell(0, 1).text = "B.Tech"

    document.save(docx_path)

    # Extract text
    result = extract_docx_text(docx_path)

    assert result["file_type"] == "docx"
    assert "Arun Kumar" in result["raw_text"]
    assert "Python" in result["raw_text"]
    assert "B.Tech" in result["raw_text"]

