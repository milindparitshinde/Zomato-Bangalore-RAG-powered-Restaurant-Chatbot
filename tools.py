from langchain.tools import tool

#TOOL DEFINITION
@tool(response_format="content_and_artifact")
def retrieve_context(query: str, vector_store):
    """Retrieve information to help answer a query."""
    retrieved_docs = vector_store.similarity_search(query, k=2)
    serialized = "\n\n".join(
        (f"Source: {doc.metadata}\nContent: {doc.page_content}")
        for doc in retrieved_docs
    )

    return serialized, retrieved_docs