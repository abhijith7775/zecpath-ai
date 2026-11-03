
# Zecpath AI – Data Entity Design

## 1. Introduction

This document defines the standard data entities used in the Zecpath AI-powered recruitment platform.

The objective is to convert unstructured resumes and job descriptions into structured, AI-ready data.

## 2. Candidate Entity

The Candidate entity represents an individual applying for a job.

Attributes:
- candidate_id
- full_name
- email
- phone
- location
- professional_summary
- skills
- education
- experience
- certifications
- total_experience_years

## 3. Job Entity

The Job entity represents a job opportunity published by an organization.

Attributes:
- job_id
- job_title
- company
- job_type
- required_skills
- preferred_skills
- minimum_experience
- maximum_experience
- responsibilities
- location
- work_mode

## 4. Skill Entity

The Skill entity represents a candidate's professional capabilities or a job's skill requirements.

Attributes:
- skill_name
- category
- proficiency
- years_of_experience

## 5. Experience Entity

The Experience entity represents previous employment information.

Attributes:
- company
- designation
- employment_type
- start_date
- end_date
- is_current
- responsibilities

## 6. Data Sources

The system processes two primary data sources:

1. Candidate resumes in PDF or DOCX format.
2. Job descriptions containing employment requirements.

## 7. Data Processing Workflow

1. Collect raw resumes and job descriptions.
2. Extract relevant information.
3. Convert extracted information into structured JSON.
4. Validate the JSON against predefined schemas.
5. Store processed data.
6. Provide structured data to downstream AI modules.

## 8. AI Integration

The structured entities will support:

- Resume parsing
- Applicant tracking
- Skill matching
- Candidate screening
- Candidate scoring
- Automated interview workflows

## 9. Conclusion

Standardized data entities and JSON schemas provide a consistent foundation for the Zecpath AI recruitment platform.
