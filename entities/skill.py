
from dataclasses import dataclass
from typing import Optional


@dataclass
class Skill:
    skill_name: str
    category: str
    proficiency: Optional[str] = None
    years_of_experience: Optional[float] = None
