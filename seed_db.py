import chromadb
from chromadb.config import Settings

client = chromadb.Client(Settings(chroma_db_impl="duckdb+parquet", persist_directory=".chroma"))
collection = client.get_or_create_collection("docker_commands")

collection.add(
    documents=[
        "docker run -it ubuntu",
        "docker build -t myimage .",
        "apt update && apt install -y curl",
        "docker ps -a",
        "docker exec -it <container> bash",
        "docker stop <container>",
        "docker rm <container>",
        "docker logs <container>"
    ],
    ids=[f"doc{i}" for i in range(8)]
)

print("[✓] ChromaDB seeded successfully.")
