
from parsers.text_cleaner import clean_resume_text


def test_removes_extra_spaces():
    text = "Python     Developer"
    result = clean_resume_text(text)
    assert result == "Python Developer"


def test_normalizes_bullets():
    text = "• Python\n• Machine Learning"
    result = clean_resume_text(text)
    assert "- Python" in result
    assert "- Machine Learning" in result


def test_normalizes_headings():
    text = "technical skills\nPython, Java"
    result = clean_resume_text(text)
    assert result.startswith("SKILLS")


def test_preserves_technical_symbols():
    text = "C++ | C# | Node.js | Python"
    result = clean_resume_text(text)
    assert "C++" in result
    assert "C#" in result
    assert "Node.js" in result


def test_rejects_invalid_input():
    import pytest

    with pytest.raises(TypeError):
        clean_resume_text(123)
