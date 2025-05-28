from dotenv import load_dotenv
import os
from agents.command_agent import CommandAgent
from vectorstore.chromadb_client import ChromaClient
from retrieval.retriever import Retriever

# Load environment variables from .env file
load_dotenv()

# Check if OpenAI API key is set
if not os.getenv("OPENAI_API_KEY"):
    raise EnvironmentError("❌ OPENAI_API_KEY not set in environment or .env file.")

# Initialize components
chroma = ChromaClient()              # vector DB
retriever = Retriever(chroma)        # wraps chroma with retrieval logic
agent = CommandAgent(retriever)      # LLM + executor logic

# Prompt user
task = input("Enter your task: ")
agent.run(task)
