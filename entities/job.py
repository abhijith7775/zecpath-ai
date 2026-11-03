
from dataclasses import dataclass, field
from typing import Optional, List

from entities.skill import Skill


@dataclass
class Job:
    job_id: str
    job_title: str
    company: str
    job_type: str
    required_skills: List[Skill] = field(default_factory=list)
    preferred_skills: List[str] = field(default_factory=list)
    minimum_experience: float = 0
    maximum_experience: Optional[float] = None
    responsibilities: List[str] = field(default_factory=list)
    location: Optional[str] = None
    work_mode: Optional[str] = None
