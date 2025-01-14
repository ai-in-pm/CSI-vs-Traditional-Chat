# Conversational Swarm Intelligence (CSI) Platform

A platform that simulates Conversational Swarm Intelligence using AI agents for collaborative brainstorming.

## Features

- **Multiple AI Agents**: Seven specialized AI agents working together:
  - Creative Thinker: Generates innovative ideas
  - Data Analyst: Provides data-driven insights
  - Risk Assessor: Identifies potential challenges
  - Mediator: Balances conflicting opinions
  - Strategist: Develops action plans
  - Facilitator: Guides discussions
  - Innovator: Explores cutting-edge solutions

- **Real-time Interaction**: Built with Streamlit for seamless user experience
- **Dynamic Visualization**: Network graphs showing agent interactions
- **Metrics Dashboard**: Track engagement and productivity

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/csi-platform.git
cd csi-platform
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory with your API keys:
```
OPENAI_API_KEY=your_openai_key
ANTHROPIC_API_KEY=your_anthropic_key
MISTRAL_API_KEY=your_mistral_key
GROQ_API_KEY=your_groq_key
GEMINI_API_KEY=your_gemini_key
COHERE_API_KEY=your_cohere_key
EMERGENCE_API_KEY=your_emergence_key
```

## Usage

Run the application:
```bash
streamlit run app.py
```

The web interface will open automatically in your default browser.

## Architecture

- `app.py`: Main Streamlit application
- `agents.py`: AI agent implementations
- `simulation.py`: CSI simulation logic
- `visualization.py`: Network and metrics visualization
- `utils.py`: Helper functions

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- OpenAI GPT-4 for Creative Thinking and Risk Assessment
- Anthropic Claude for Data Analysis
- Mistral AI for Strategic Planning
- Groq for Mediation
- Google Gemini for Innovation
- Cohere for Facilitation
