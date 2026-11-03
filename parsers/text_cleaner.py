
import re


def clean_resume_text(raw_text):
    """
    Clean and normalize extracted resume text.
    """

    if not isinstance(raw_text, str):
        raise TypeError("Input must be a string.")

    # Normalize line endings
    text = raw_text.replace("\r\n", "\n").replace("\r", "\n")

    # Normalize bullet symbols
    text = re.sub(r"[•●▪◦‣]", "-", text)

    # Remove unwanted special characters while preserving
    # common technical symbols and punctuation
    text = re.sub(r"[^\w\s@.+#/\-(),:%&]", " ", text)

    # Remove extra spaces
    text = re.sub(r"[ \t]+", " ", text)

    # Remove excessive blank lines
    text = re.sub(r"\n\s*\n+", "\n\n", text)

    # Normalize section headings
    heading_mapping = {
        "professional summary": "PROFESSIONAL SUMMARY",
        "career objective": "PROFESSIONAL SUMMARY",
        "work experience": "WORK EXPERIENCE",
        "professional experience": "WORK EXPERIENCE",
        "technical skills": "SKILLS",
        "skills": "SKILLS",
        "education": "EDUCATION",
        "academic qualifications": "EDUCATION",
        "certifications": "CERTIFICATIONS",
        "projects": "PROJECTS",
        "personal details": "PERSONAL DETAILS"
    }

    normalized_lines = []

    for line in text.split("\n"):
        stripped_line = line.strip()

        if not stripped_line:
            normalized_lines.append("")
            continue

        heading_key = stripped_line.lower().rstrip(":").strip()

        if heading_key in heading_mapping:
            normalized_lines.append(heading_mapping[heading_key])
        else:
            normalized_lines.append(stripped_line)

    text = "\n".join(normalized_lines)

    # Remove leading and trailing whitespace
    return text.strip()
