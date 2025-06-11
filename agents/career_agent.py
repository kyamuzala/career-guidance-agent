from typing import List, Dict, Any
import openai
import os
from ..models.student_profile import StudentProfile
from ..models.career_recommendation import CareerRecommendation

class CareerGuidanceAgent:
    def __init__(self):
        self.openai_client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        
    async def analyze_profile(self, profile: StudentProfile) -> List[CareerRecommendation]:
        """
        Analyze student profile and generate career recommendations based on interests
        """
        # Create a prompt for the AI model
        prompt = self._create_analysis_prompt(profile)
        
        # Get AI response
        response = await self._get_ai_recommendations(prompt)
        
        # Process and structure the recommendations
        recommendations = self._process_recommendations(response)
        
        return recommendations
    
    def _create_analysis_prompt(self, profile: StudentProfile) -> str:
        """
        Create a detailed prompt for the AI model based on student interests and profile
        """
        prompt = f"""
        Analyze the following student profile and provide career recommendations focusing on their interests and aspirations:
        
        Name: {profile.name}
        Major: {profile.major}
        Year: {profile.year}
        
        General Interests:
        {', '.join(profile.interests)}
        
        Technical Interests:
        {', '.join(profile.technical_interests) if profile.technical_interests else 'Not specified'}
        
        Soft Skills:
        {', '.join(profile.soft_skills) if profile.soft_skills else 'Not specified'}
        
        Career Goals:
        {', '.join(profile.career_goals) if profile.career_goals else 'Not specified'}
        
        Please provide detailed career recommendations including:
        1. Career paths that align with their interests and goals
        2. How their current interests can be leveraged in each career path
        3. Required technical and soft skills for each path
        4. Market demand and salary expectations
        5. Growth potential and career progression
        6. Recommended next steps to pursue each path
        7. Potential challenges and how to overcome them
        """
        return prompt
    
    async def _get_ai_recommendations(self, prompt: str) -> str:
        """
        Get recommendations from OpenAI API
        """
        try:
            response = await self.openai_client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a career guidance expert helping university students find their career paths based on their interests and aspirations. Focus on matching their interests with potential career paths and provide actionable advice."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=1500
            )
            return response.choices[0].message.content
        except Exception as e:
            raise Exception(f"Error getting AI recommendations: {str(e)}")
    
    def _process_recommendations(self, ai_response: str) -> List[CareerRecommendation]:
        """
        Process AI response and convert to structured recommendations
        """
        # TODO: Implement proper parsing of AI response
        # For now, return a sample recommendation
        return [
            CareerRecommendation(
                career_path="Software Engineer",
                description="Design and develop software applications with focus on AI and web technologies",
                required_skills=[
                    "Programming",
                    "Problem Solving",
                    "Team Collaboration",
                    "AI/ML Knowledge",
                    "Web Development"
                ],
                market_demand="High",
                salary_range="$70,000 - $120,000",
                growth_potential="Excellent"
            )
        ]
    
    async def get_skills_assessment(self) -> List[Dict[str, Any]]:
        """
        Generate a skills assessment questionnaire focused on interests and aspirations
        """
        return [
            {
                "id": 1,
                "question": "What type of work environment do you prefer?",
                "options": ["Team-based", "Independent", "Mixed", "Not sure"]
            },
            {
                "id": 2,
                "question": "How do you feel about taking on leadership roles?",
                "options": ["Very interested", "Somewhat interested", "Not interested", "Not sure"]
            },
            {
                "id": 3,
                "question": "What type of problems do you enjoy solving?",
                "options": ["Technical challenges", "People/communication issues", "Business problems", "Creative challenges"]
            },
            {
                "id": 4,
                "question": "How do you prefer to learn new things?",
                "options": ["Hands-on practice", "Reading/Research", "Group learning", "Mentorship"]
            },
            {
                "id": 5,
                "question": "What motivates you the most in your work?",
                "options": ["Technical innovation", "Helping others", "Financial success", "Creative expression"]
            }
        ]
    
    async def get_career_paths(self) -> List[str]:
        """
        Get list of available career paths
        """
        return [
            "Software Engineering",
            "Data Science",
            "Business Analytics",
            "Product Management",
            "UX/UI Design",
            "Digital Marketing",
            "Finance",
            "Consulting",
            "Research & Development",
            "Entrepreneurship",
            "Technical Leadership",
            "Project Management",
            "DevOps Engineering",
            "AI/ML Engineering",
            "Cloud Architecture"
        ] 