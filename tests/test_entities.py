
from entities.candidate import Candidate
from entities.job import Job
from entities.skill import Skill
from entities.experience import Experience


def test_candidate_creation():
    skill = Skill(
        skill_name="Python",
        category="technical",
        proficiency="Intermediate"
    )

    experience = Experience(
        company="ABC Technologies",
        designation="Python Developer"
    )

    candidate = Candidate(
        candidate_id="CAND001",
        full_name="Arun Kumar",
        email="arun@example.com",
        skills=[skill],
        experience=[experience]
    )

    assert candidate.full_name == "Arun Kumar"
    assert candidate.skills[0].skill_name == "Python"


def test_job_creation():
    job = Job(
        job_id="JOB001",
        job_title="Python Developer",
        company="Zecpath",
        job_type="full-time"
    )

    assert job.job_title == "Python Developer"
    assert job.company == "Zecpath"
