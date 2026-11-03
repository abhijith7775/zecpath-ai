
import json
from pathlib import Path
from collections import Counter
from statistics import mean

RESUME_DIR = Path("data/raw/resumes")
OUTPUT_DIR = Path("data/processed/resumes")

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

resumes = []

# Load all resume JSON files
for file_path in RESUME_DIR.glob("CAND*.json"):
    with open(file_path, "r", encoding="utf-8-sig") as file:
        resumes.append(json.load(file))

# Initialize counters
skill_counter = Counter()
designation_counter = Counter()
education_counter = Counter()
certification_counter = Counter()
experience_values = []

for resume in resumes:

    # Skills
    for skill in resume.get("skills", []):
        skill_counter[skill["skill_name"]] += 1

    # Designations
    for experience in resume.get("experience", []):
        designation_counter[experience["designation"]] += 1

    # Education
    for education in resume.get("education", []):
        education_counter[education["degree"]] += 1

    # Certifications
    for certification in resume.get("certifications", []):
        certification_counter[certification["name"]] += 1

    # Total experience
    years = resume.get("total_experience_years")
    if years is not None:
        experience_values.append(years)


# Generate analysis report
report = {
    "total_candidates": len(resumes),

    "skill_distribution": dict(skill_counter.most_common()),

    "designation_distribution": dict(designation_counter),

    "education_distribution": dict(education_counter),

    "certification_distribution": dict(certification_counter),

    "experience_analysis": {
        "average_years": round(mean(experience_values), 2)
        if experience_values else 0,
        "minimum_years": min(experience_values)
        if experience_values else 0,
        "maximum_years": max(experience_values)
        if experience_values else 0
    }
}

# Save report
output_file = OUTPUT_DIR / "resume_analysis.json"

with open(output_file, "w", encoding="utf-8") as file:
    json.dump(report, file, indent=4)

# Display results
print("\n========== RESUME DATA ANALYSIS ==========")

print("\nTotal Candidates:", len(resumes))

print("\nSkill Distribution:")
for skill, count in skill_counter.most_common():
    print(f"{skill}: {count}")

print("\nDesignation Distribution:")
for designation, count in designation_counter.items():
    print(f"{designation}: {count}")

print("\nEducation Distribution:")
for degree, count in education_counter.items():
    print(f"{degree}: {count}")

print("\nExperience Analysis:")
print(report["experience_analysis"])

print("\nAnalysis saved to:", output_file)
