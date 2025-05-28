import chromadb

class ChromaClient:
    def __init__(self):
        self.client = chromadb.PersistentClient(path=".chroma")

    def get_or_create_collection(self, name: str):
        return self.client.get_or_create_collection(name=name)
