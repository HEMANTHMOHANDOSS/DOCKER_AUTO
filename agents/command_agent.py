import re
from openai import OpenAI
from execution.docker_executor import DockerExecutor
from utils.exception_handler import safe_execute

class CommandAgent:
    def __init__(self, retriever):
        self.retriever = retriever
        self.executor = DockerExecutor()
        self.client = OpenAI()  # expects OPENAI_API_KEY in env

    def run(self, task: str):
        print(f"\n Task received: {task}")

        docs = self.retriever.get_relevant_docs(task)
        try:
            context = "\n".join(doc.page_content for doc in docs)
        except AttributeError:
            context = "\n".join(
                str(doc) if isinstance(doc, str) else " ".join(doc)
                for doc in docs
            )

        messages = [
            {
                "role": "system",
                "content": "You are a helpful assistant that generates safe Docker CLI commands based on user tasks."
            },
            {
                "role": "user",
                "content": f"Task: {task}\nContext:\n{context}"
            }
        ]

        print("\n Querying OpenAI...")
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=messages
        )

        full_command = response.choices[0].message.content.strip()
        print(f"\n Suggested Command: {full_command}")

        # Extract the Docker command from triple backticks or after 'Command:'
        match = re.search(r"```(?:bash)?\n(.+?)```", full_command, re.DOTALL)
        if match:
            command = match.group(1).strip()
        else:
            # Remove 'Command:' prefix if present
            command = re.sub(r"^Command:\s*", "", full_command).strip()

        print(f"\n Executing cleaned command:\n{command}")

        safe_execute(self.executor.run_command, command)
