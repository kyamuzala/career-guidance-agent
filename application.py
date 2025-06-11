from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv
from typing import List

from models import StudentProfile, CareerRecommendation
from agents import CareerGuidanceAgent

# Load environment variables
load_dotenv()

app = FastAPI(
    title="Career Guidance Agent System",
    description="An intelligent system for providing career guidance to university students",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize the career guidance agent
career_agent = CareerGuidanceAgent()

@app.get("/")
async def root():
    return {"message": "Welcome to the Career Guidance Agent System"}

@app.post("/analyze-profile", response_model=List[CareerRecommendation])
async def analyze_student_profile(profile: StudentProfile):
    """
    Analyze student profile and provide career recommendations
    """
    try:
        recommendations = await career_agent.analyze_profile(profile)
        return recommendations
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/career-paths")
async def get_career_paths():
    """
    Get list of available career paths
    """
    try:
        career_paths = await career_agent.get_career_paths()
        return {"career_paths": career_paths}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/skills-assessment")
async def get_skills_assessment():
    """
    Get skills assessment questionnaire
    """
    try:
        assessment = await career_agent.get_skills_assessment()
        return {"questions": assessment}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 