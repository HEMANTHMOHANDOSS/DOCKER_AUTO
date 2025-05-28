class Retriever:
    def __init__(self, chroma):
        self.collection = chroma.get_or_create_collection(name="command-memory")

    def get_relevant_docs(self, query: str):
        results = self.collection.query(
            query_texts=[query],
            n_results=3
        )
        return results["documents"]
