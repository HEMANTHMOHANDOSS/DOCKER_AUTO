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


STAGE 2:

Here is a **complete and detailed `README.md` file** for your **RAG Docker Automation with Observability** project. It walks through setup, architecture, tracing, metrics in rupees, and Grafana dashboards — step by step.

---

# 🧠 RAG Docker Automation with Observability (Python + LangChain + Grafana)

Automate Docker CLI operations using LLMs with Retrieval-Augmented Generation (RAG), while tracking token usage, cost (in ₹ INR), traces, and performance metrics. Visualize everything with Prometheus, Grafana, and Jaeger.

---

## 📚 Table of Contents

* [🔧 Features](#-features)
* [🖼️ Architecture](#️-architecture)
* [🧰 Tech Stack](#-tech-stack)
* [🚀 Getting Started](#-getting-started)

  * [1. Clone the Repository](#1-clone-the-repository)
  * [2. Create a Virtual Environment](#2-create-a-virtual-environment)
  * [3. Install Python Dependencies](#3-install-python-dependencies)
  * [4. Configure Environment Variables](#4-configure-environment-variables)
  * [5. Start Observability Tools](#5-start-observability-tools)
  * [6. Start the RAG Agent](#6-start-the-rag-agent)
* [📊 Grafana Dashboard Setup](#-grafana-dashboard-setup)
* [📈 Prometheus Metrics](#-prometheus-metrics)
* [📉 Cost Calculation (in ₹ INR)](#-cost-calculation-in--inr)
* [🧪 Tracing with Jaeger](#-tracing-with-jaeger)
* [🧼 Cleanup](#-cleanup)
* [📝 Future Improvements](#-future-improvements)
* [🙋 Support](#-support)

---

## 🔧 Features

✅ Automates Docker commands via LLM
✅ Retrieves relevant Docker documentation using ChromaDB
✅ Traces execution with OpenTelemetry and Jaeger
✅ Logs token usage and OpenAI cost
✅ Exposes Prometheus metrics
✅ Visualizes cost and usage in Grafana (INR currency)

---

## 🖼️ Architecture

```plaintext
+---------------------+
|    User Prompt      |
+---------------------+
           |
           v
+---------------------+
|  LangChain + LLM    |
+---------------------+
           |
           v
+---------------------------+
|  ChromaDB Vector Retriever|
+---------------------------+
           |
           v
+---------------------+
| Docker CLI Commands |
+---------------------+
           |
           v
+-----------------------------+
| Metrics + Traces + Logs     |
|   (Prometheus + Jaeger)     |
+-----------------------------+
           |
           v
+---------------------+
|   Grafana Dashboard |
+---------------------+
```

---

## 🧰 Tech Stack

* **LangChain** (agent and retriever logic)
* **OpenAI GPT-4 / GPT-3.5**
* **ChromaDB** for vector retrieval
* **Prometheus** for metrics
* **Grafana** for visualization
* **Jaeger** for tracing
* **OpenTelemetry** for instrumentation
* **Docker Compose** for orchestration

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourname/docker-automation-rag.git
cd docker-automation-rag
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### 3. Install Python Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file:

```env
# .env
OPENAI_API_KEY=your_openai_key
```

Replace `your_openai_key` with your actual key from [https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys)

---

### 5. Start Observability Tools (Grafana + Jaeger + Prometheus)

```bash
docker compose up -d
```

✅ This starts:

| Tool       | Port    | URL                                              |
| ---------- | ------- | ------------------------------------------------ |
| Grafana    | `3000`  | [http://localhost:3000](http://localhost:3000)   |
| Prometheus | `9090`  | [http://localhost:9090](http://localhost:9090)   |
| Jaeger     | `16686` | [http://localhost:16686](http://localhost:16686) |

---

### 6. Start the RAG Agent

```bash
python main.py
```

You'll see:

```
Enter your task:
```

Example:

```
Enter your task: list all running containers
```

---

## 📊 Grafana Dashboard Setup

1. Open [http://localhost:3000](http://localhost:3000)
2. Login with default: `admin / admin`
3. Add a new data source:

   * **Name**: Prometheus
   * **URL**: `http://prometheus:9090`
4. Import or create a dashboard

   * Add visualizations using metrics:

     * `input_tokens_total`
     * `output_tokens_total`
     * `total_tokens_total`
     * `total_cost_inr`
5. Set **Units**:

   * Use `Currency → ₹ INR` for cost
   * Use `Short` for token counts

---

## 📈 Prometheus Metrics

| Metric                | Description                       |
| --------------------- | --------------------------------- |
| `input_tokens_total`  | Number of input tokens used       |
| `output_tokens_total` | Number of output tokens generated |
| `total_tokens_total`  | Total (input + output) tokens     |
| `total_cost_inr`      | Total cost in INR ₹               |

---

## 📉 Cost Calculation (in ₹ INR)

We use OpenAI token pricing:

* GPT-4 8k: `$0.03 / 1k input`, `$0.06 / 1k output`
* GPT-3.5: lower rates

The cost in INR is calculated dynamically based on the token usage and USD→INR exchange rate:

```python
cost_usd = (input_tokens / 1000) * input_price + (output_tokens / 1000) * output_price
cost_inr = cost_usd * exchange_rate_inr  # e.g., 83.2
```

---

## 🧪 Tracing with Jaeger

To view traces:

1. Open [http://localhost:16686](http://localhost:16686)
2. Select service (like `docker-agent`)
3. Click **Find Traces**
4. Explore each trace span:

   * Task processing
   * Vector search
   * Token counting

---

## 🧼 Cleanup

Stop all containers and remove volumes:

```bash
docker compose down -v
```

---

## 📝 Future Improvements

* 🔄 Add local LLM support (e.g., Ollama, LLaMA.cpp)
* ⛓ Add Kubernetes support
* 🔐 Secure Grafana with auth + role-based access
* 🧠 Memory support for contextual task chaining

---

## 🙋 Support

Need help?

* 🧠 [LangChain Discord](https://discord.gg/langchain)
* 🔍 [OpenTelemetry Docs](https://opentelemetry.io/docs/)
* 🛠 [Grafana Docs](https://grafana.com/docs/)
* 💬 Raise an [issue here](https://github.com/yourname/docker-automation-rag/issues)

---

