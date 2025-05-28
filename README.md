# Docker_Rag
# 🧠 RAG Docker Automation Agent

This is an intelligent agent that uses Retrieval-Augmented Generation (RAG) to understand natural language commands and automatically run relevant Docker commands. It uses:

- 🧠 OpenAI GPT-4 (via official OpenAI SDK)
- 📦 ChromaDB for vector storage
- 🐳 Docker for executing system-level commands

---

## 🛠 Features

- Accepts natural language tasks like:  
  _"Run a Docker container that prints 'Hello from RAG'"_
- Retrieves relevant context from ChromaDB
- Uses GPT-4 to generate Docker commands
- Executes the commands directly in your terminal
- Handles exceptions and errors

---

## 📁 Project Structure

rag_docker_agent/
│
├── agents/
│ └── command_agent.py # The main agent logic
│
├── execution/
│ └── docker_executor.py # Handles Docker command execution
│
├── retrieval/
│ └── retriever.py # Pulls context from ChromaDB
│
├── utils/
│ └── exception_handler.py # Error handling wrappers
│
├── vectorstore/
│ └── chromadb_client.py # Direct access to ChromaDB
│
├── .env # OpenAI API Key
├── requirements.txt
└── main.py # Entry point


---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/rag_docker_agent.git
cd rag_docker_agent

2. Create and activate virtual environment

# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
3. Install dependencies

pip install -r requirements.txt
4. Set your OpenAI API Key
Create a .env file in the root directory:


OPENAI_API_KEY=your_openai_api_key_here
✅ Run the agent

python main.py
