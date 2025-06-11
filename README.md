# Career Guidance Agent System

An intelligent agent system designed to provide personalized career guidance for university students. The system helps students explore career paths, get personalized recommendations, and access relevant resources based on their interests, skills, and academic background.

## Features

- Career path exploration
- Personalized career recommendations
- Skill assessment and gap analysis
- Industry trend insights
- Resume and interview preparation guidance
- Internship and job opportunity matching

## Setup Instructions

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory and add your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

4. Run the application:
```bash
uvicorn main:app --reload
```

## Project Structure

- `main.py`: FastAPI application entry point
- `agents/`: Contains different agent implementations
- `models/`: Data models and schemas
- `services/`: Business logic and external service integrations
- `database/`: Database models and connection handling
- `utils/`: Utility functions and helpers

## API Documentation

Once the application is running, visit `http://localhost:8000/docs` for the interactive API documentation. 