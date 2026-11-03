
from dataclasses import dataclass, field
from typing import Optional, List

from entities.skill import Skill
from entities.experience import Experience


@dataclass
class Candidate:
    candidate_id: str
    full_name: str
    email: str
    phone: Optional[str] = None
    location: Optional[str] = None
    professional_summary: Optional[str] = None
    skills: List[Skill] = field(default_factory=list)
    education: List[dict] = field(default_factory=list)
    experience: List[Experience] = field(default_factory=list)
    certifications: List[dict] = field(default_factory=list)
    total_experience_years: Optional[float] = None
