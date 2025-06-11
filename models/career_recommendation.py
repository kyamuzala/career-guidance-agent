from pydantic import BaseModel
from typing import List

class CareerRecommendation(BaseModel):
    career_path: str
    description: str
    required_skills: List[str]
    market_demand: str
    salary_range: str
    growth_potential: str
    
    class Config:
        schema_extra = {
            "example": {
                "career_path": "Software Engineer",
                "description": "Design and develop software applications using various programming languages and frameworks",
                "required_skills": [
                    "Programming",
                    "Problem Solving",
                    "Team Collaboration",
                    "System Design",
                    "Version Control"
                ],
                "market_demand": "High",
                "salary_range": "$70,000 - $120,000",
                "growth_potential": "Excellent"
            }
        } 