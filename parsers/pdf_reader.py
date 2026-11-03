
import pymupdf as fitz
from pathlib import Path


def extract_pdf_text(file_path):
    """
    Extract text from a PDF resume using PyMuPDF.

    Returns extracted text, metadata and extraction warnings.
    """

    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(f"PDF not found: {file_path}")

    if file_path.suffix.lower() != ".pdf":
        raise ValueError("Expected a PDF file")

    extracted_pages = []
    warnings = []

    with fitz.open(file_path) as pdf:

        for page_number, page in enumerate(pdf, start=1):

            # Extract text in approximate reading order
            page_text = page.get_text("text", sort=True)

            extracted_pages.append({
                "page": page_number,
                "text": page_text
            })

            if not page_text.strip():
                warnings.append(
                    f"Page {page_number} contains no extractable text. "
                    "It may require OCR."
                )

        full_text = "\n\n".join(
            page["text"] for page in extracted_pages
        )

        result = {
            "file_name": file_path.name,
            "file_type": "pdf",
            "page_count": len(pdf),
            "raw_text": full_text,
            "pages": extracted_pages,
            "warnings": warnings
        }

    return result


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python -m parsers.pdf_reader <resume.pdf>")
    else:
        result = extract_pdf_text(sys.argv[1])
        print(result["raw_text"])
        print("\nPages:", result["page_count"])
        print("Warnings:", result["warnings"])
