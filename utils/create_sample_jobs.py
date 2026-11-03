
import json
from pathlib import Path

OUTPUT_DIR = Path("data/raw/job_descriptions")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

jobs = [
    ("Python Developer", "Technical", ["Python", "Flask", "SQL"]),
    ("Data Scientist", "Technical", ["Python", "Machine Learning", "Pandas"]),
    ("ML Engineer", "Technical", ["Python", "TensorFlow", "PyTorch"]),
    ("Frontend Developer", "Technical", ["HTML", "CSS", "JavaScript", "React"]),
    ("Backend Developer", "Technical", ["Python", "Django", "REST API"]),
    ("HR Executive", "Non-technical", ["Recruitment", "Communication", "HRMS"]),
    ("Digital Marketing Executive", "Non-technical", ["SEO", "Google Analytics", "Social Media Marketing"]),
    ("Accountant", "Non-technical", ["Accounting", "Tally", "GST"]),
    ("Business Analyst", "Non-technical", ["SQL", "Power BI", "Excel"]),
    ("Sales Executive", "Non-technical", ["Negotiation", "Communication", "CRM"])
]

for index, (title, category, skills) in enumerate(jobs, start=1):

    job_id = f"JOB{index:03d}"

    job = {
        "job_id": job_id,
        "job_title": title,
        "company": "Zecpath",
        "department": category,
        "job_type": "full-time",
        "work_mode": "hybrid",
        "location": "Kochi, Kerala",
        "job_description": f"We are hiring a {title} to join our team.",
        "required_skills": [
            {
                "skill_name": skill,
                "category": "technical" if category == "Technical" else "domain",
                "is_mandatory": True
            }
            for skill in skills
        ],
        "preferred_skills": [],
        "experience_requirements": {
            "minimum_years": 1,
            "maximum_years": 4,
            "experience_level": "entry-level"
        },
        "education_requirements": [
            {
                "degree": "Bachelor's Degree",
                "field_of_study": None,
                "is_mandatory": True
            }
        ],
        "certifications": [],
        "responsibilities": [
            f"Perform professional responsibilities as a {title}",
            "Collaborate with team members",
            "Prepare regular work reports"
        ],
        "salary_range": None,
        "application_deadline": None
    }

    file_path = OUTPUT_DIR / f"{job_id}.json"

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(job, file, indent=4)

    print(f"Created {file_path}")

print("\n10 sample job descriptions generated.")
