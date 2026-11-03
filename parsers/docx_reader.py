
from pathlib import Path

from docx import Document
from docx.text.paragraph import Paragraph
from docx.table import Table


def extract_docx_text(file_path):
    """
    Extract text from a DOCX resume.

    Extracts paragraphs and tables in document order.
    """

    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(f"DOCX not found: {file_path}")

    if file_path.suffix.lower() != ".docx":
        raise ValueError("Expected a DOCX file")

    document = Document(file_path)

    extracted_blocks = []
    warnings = []

    # Iterate through paragraphs and tables in document order
    for element in document.element.body.iterchildren():

        if element.tag.endswith("}p"):
            paragraph = Paragraph(element, document)
            text = paragraph.text.strip()

            if text:
                extracted_blocks.append({
                    "type": "paragraph",
                    "text": text
                })

        elif element.tag.endswith("}tbl"):
            table = Table(element, document)

            for row in table.rows:
                row_text = [
                    cell.text.strip().replace("\n", " ")
                    for cell in row.cells
                ]

                if any(row_text):
                    extracted_blocks.append({
                        "type": "table_row",
                        "text": " | ".join(row_text)
                    })

    # Extract headers
    for section in document.sections:
        header_text = "\n".join(
            p.text.strip()
            for p in section.header.paragraphs
            if p.text.strip()
        )

        if header_text:
            extracted_blocks.insert(0, {
                "type": "header",
                "text": header_text
            })

        # Extract footers
        footer_text = "\n".join(
            p.text.strip()
            for p in section.footer.paragraphs
            if p.text.strip()
        )

        if footer_text:
            extracted_blocks.append({
                "type": "footer",
                "text": footer_text
            })

    full_text = "\n".join(
        block["text"] for block in extracted_blocks
    )

    if not full_text.strip():
        warnings.append(
            "No extractable text found in the DOCX document."
        )

    result = {
        "file_name": file_path.name,
        "file_type": "docx",
        "raw_text": full_text,
        "blocks": extracted_blocks,
        "warnings": warnings
    }

    return result


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python -m parsers.docx_reader <resume.docx>")
    else:
        result = extract_docx_text(sys.argv[1])
        print(result["raw_text"])
        print("Warnings:", result["warnings"])
