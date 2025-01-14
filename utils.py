import os
from dotenv import load_dotenv

def load_env_vars():
    """Load environment variables from .env file"""
    load_dotenv()
    
    required_vars = [
        "OPENAI_API_KEY",
        "ANTHROPIC_API_KEY",
        "MISTRAL_API_KEY",
        "GROQ_API_KEY",
        "GEMINI_API_KEY",
        "COHERE_API_KEY",
        "EMERGENCE_API_KEY"
    ]
    
    missing_vars = [var for var in required_vars if not os.getenv(var)]
    
    if missing_vars:
        raise EnvironmentError(
            f"Missing required environment variables: {', '.join(missing_vars)}\n"
            "Please add them to your .env file."
        )
