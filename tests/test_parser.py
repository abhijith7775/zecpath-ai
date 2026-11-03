
def test_candidate_score():
    technical_score = 80
    experience_score = 70

    final_score = (
        technical_score * 0.7 +
        experience_score * 0.3
    )

    assert final_score == 77


def test_candidate_name():
    candidate = {
        "name": "Arun",
        "skills": ["Python", "Machine Learning"]
    }

    assert candidate["name"] == "Arun"
    assert "Python" in candidate["skills"]
