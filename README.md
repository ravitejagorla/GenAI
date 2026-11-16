# GenAI – Generative AI Learning & Projects

A hands-on repository documenting my journey into Generative AI, Large Language Models (LLMs), LangChain, LangGraph, AI Agents, and Retrieval-Augmented Generation (RAG).

The repository contains practical Python examples, experiments, and AI-powered applications built while learning GenAI.

## Technologies

- Python
- LangChain
- LangGraph
- Groq API
- Google Gemini API
- OpenAI API
- Ollama
- Streamlit
- Pydantic
- SQLite
- Google Serper Search API

## Repository Structure

```text
GenAI/
├── apps/
│   ├── Chatbots
│   ├── Agents
│   ├── SQL Agent
│   └── Structured Output
├── notebooks/
├── requirements.txt
└── README.md
```

## Implemented Concepts

- LLM integration and API calls
- Chat model invocation and streaming
- Prompt templates
- LangChain Expression Language (LCEL)
- Output parsers
- Conversation history
- Streamlit chat applications
- Custom tools using `@tool`
- AI agents using `create_agent`
- Web search integration
- Structured output with Pydantic
- SQL database agents
- LangGraph checkpoint memory
- Local LLM integration using Ollama

## Applications

### 1. AI Chatbots

Chat applications using Groq and Google Gemini with Streamlit.

### 2. Search Agent

An AI agent capable of using Google search to retrieve information.

### 3. Mathematics Agent

A tool-calling agent that uses custom addition and multiplication tools.

### 4. Structured Output

Extracts structured information using Pydantic models.

### 5. SQL Task Management Assistant

A conversational AI application that manages tasks using SQLite and LangChain SQL tools.

## Installation

Clone the repository:

```bash
git clone https://github.com/ravitejagorla/GenAI.git
cd GenAI
```

Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Configure the API keys required by the application you want to run in a `.env` file.

Never commit API keys or personal credentials.

## Running Applications

Example:

```bash
streamlit run apps/chatbot.py
```

Run other Python examples:

```bash
python apps/groq_example.py
python apps/agent_search.py
```

## Learning Roadmap

- [x] LLM Fundamentals
- [x] LangChain Basics
- [x] Prompt Engineering Basics
- [x] Tool Calling
- [x] AI Agents
- [x] Structured Output
- [ ] LangGraph Advanced Workflows
- [ ] Embeddings and Vector Databases
- [ ] Retrieval-Augmented Generation (RAG)
- [ ] Advanced Agentic AI
- [ ] AI Application Deployment

## Objective

Build practical, reliable, and production-oriented Generative AI applications using Python and modern AI frameworks.

## Author

**Ravi Teja Gorla**

GitHub: [https://github.com/ravitejagorla](https://github.com/ravitejagorla)

LinkedIn: [https://www.linkedin.com/in/ravitejagorla/](https://www.linkedin.com/in/ravitejagorla/)
