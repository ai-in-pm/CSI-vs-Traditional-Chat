from abc import ABC, abstractmethod
import openai
import anthropic
from mistralai.client import MistralClient
from groq import Groq
import google.generativeai as genai
import cohere
from typing import List, Dict
import os

class BaseAgent(ABC):
    def __init__(self, role: str):
        self.role = role
        self.conversation_history = []

    @abstractmethod
    async def process_input(self, input_text: str) -> str:
        pass

    @abstractmethod
    async def generate_response(self, context: Dict) -> str:
        pass

    def update_history(self, message: Dict):
        self.conversation_history.append(message)

class CreativeThinker(BaseAgent):
    def __init__(self):
        super().__init__("Creative Thinker")
        self.client = openai.Client(api_key=os.getenv("OPENAI_API_KEY"))

    async def process_input(self, input_text: str) -> str:
        response = await self.client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[{"role": "system", "content": "You are a creative thinker focused on generating innovative and out-of-the-box ideas."},
                     {"role": "user", "content": input_text}]
        )
        return response.choices[0].message.content

    async def generate_response(self, context: Dict) -> str:
        prompt = f"As a creative thinker, generate innovative ideas for: {context.get('topic', '')}"
        return await self.process_input(prompt)

class DataAnalyst(BaseAgent):
    def __init__(self):
        super().__init__("Data Analyst")
        self.client = anthropic.Client(api_key=os.getenv("ANTHROPIC_API_KEY"))

    async def process_input(self, input_text: str) -> str:
        response = await self.client.messages.create(
            model="claude-3-opus",
            messages=[{"role": "user", "content": input_text}],
            system="You are a data analyst focused on providing data-driven insights and analysis."
        )
        return response.content

    async def generate_response(self, context: Dict) -> str:
        prompt = f"As a data analyst, analyze the following ideas and provide data-driven insights: {context.get('ideas', [])}"
        return await self.process_input(prompt)

class RiskAssessor(BaseAgent):
    def __init__(self):
        super().__init__("Risk Assessor")
        self.client = openai.Client(api_key=os.getenv("OPENAI_API_KEY"))

    async def process_input(self, input_text: str) -> str:
        response = self.client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {"role": "system", "content": "You are a risk assessor focused on identifying potential challenges and flaws."},
                {"role": "user", "content": input_text}
            ]
        )
        return response.choices[0].message.content

    async def generate_response(self, context: Dict) -> str:
        prompt = f"As a risk assessor, identify potential challenges and risks in these ideas: {context.get('ideas', [])}"
        return await self.process_input(prompt)

class Mediator(BaseAgent):
    def __init__(self):
        super().__init__("Mediator")
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    async def process_input(self, input_text: str) -> str:
        response = await self.client.chat.completions.create(
            model="mixtral-8x7b-32768",
            messages=[{"role": "system", "content": "You are a mediator focused on balancing conflicting opinions and finding common ground."},
                     {"role": "user", "content": input_text}]
        )
        return response.choices[0].message.content

    async def generate_response(self, context: Dict) -> str:
        prompt = f"As a mediator, help find common ground between these perspectives: {context.get('perspectives', [])}"
        return await self.process_input(prompt)

class Strategist(BaseAgent):
    def __init__(self):
        super().__init__("Strategist")
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        self.model = genai.GenerativeModel('gemini-pro')

    async def process_input(self, input_text: str) -> str:
        response = await self.model.generate_content(input_text)
        return response.text

    async def generate_response(self, context: Dict) -> str:
        prompt = f"As a strategist, develop an action plan based on these ideas: {context.get('ideas', [])}"
        return await self.process_input(prompt)

class Facilitator(BaseAgent):
    def __init__(self):
        super().__init__("Facilitator")
        self.client = cohere.Client(os.getenv("COHERE_API_KEY"))

    async def process_input(self, input_text: str) -> str:
        response = await self.client.generate(
            prompt=input_text,
            model='command',
            max_tokens=500
        )
        return response.generations[0].text

    async def generate_response(self, context: Dict) -> str:
        prompt = f"As a facilitator, guide the discussion and ensure smooth communication between participants discussing: {context.get('topic', '')}"
        return await self.process_input(prompt)

class Innovator(BaseAgent):
    def __init__(self):
        super().__init__("Innovator")
        # Using a hypothetical Emergence API for demonstration
        self.api_key = os.getenv("EMERGENCE_API_KEY")

    async def process_input(self, input_text: str) -> str:
        # Simulated response for demonstration
        return f"Innovative perspective on: {input_text}"

    async def generate_response(self, context: Dict) -> str:
        prompt = f"As an innovator, explore cutting-edge solutions for: {context.get('topic', '')}"
        return await self.process_input(prompt)
