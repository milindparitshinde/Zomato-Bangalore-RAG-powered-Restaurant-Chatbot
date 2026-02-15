from langchain_chroma import Chroma

def create_chroma_vector_store(embeddings, PERSIST_DIRECTORY):
    COLLECTION_NAME = "example_collection"

    vector_store = Chroma(
        collection_name=COLLECTION_NAME,
        embedding_function=embeddings,
        persist_directory=PERSIST_DIRECTORY,  # Where to save data locally, remove if not necessary
    )
    print("Chroma vector store created.")

    return vector_store