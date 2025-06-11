from pydantic import BaseModel
from typing import List, Optional

class StudentProfile(BaseModel):
    name: str
    major: str
    year: int
    interests: List[str]
    technical_interests: Optional[List[str]] = None
    soft_skills: Optional[List[str]] = None
    career_goals: Optional[List[str]] = None
    
    class Config:
        schema_extra = {
            "example": {
                "name": "John Doe",
                "major": "Computer Science",
                "year": 3,
                "interests": [
                    "Artificial Intelligence",
                    "Web Development",
                    "Data Science",
                    "Problem Solving",
                    "Team Projects"
                ],
                "technical_interests": [
                    "Machine Learning",
                    "Full Stack Development",
                    "Cloud Computing"
                ],
                "soft_skills": [
                    "Leadership",
                    "Communication",
                    "Project Management"
                ],
                "career_goals": [
                    "Become a Software Engineer",
                    "Work in AI Research",
                    "Lead Technical Teams"
                ]
            }
        } 