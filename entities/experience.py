
from dataclasses import dataclass, field
from typing import Optional, List


@dataclass
class Experience:
    company: str
    designation: str
    employment_type: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    is_current: bool = False
    responsibilities: List[str] = field(default_factory=list)
