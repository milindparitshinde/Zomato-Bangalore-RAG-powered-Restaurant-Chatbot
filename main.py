from dotenv import load_dotenv
import os
import getpass
from langchain.chat_models import init_chat_model
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.agents import create_agent
# from RAG.structured_way.vector_store_mongodb import create_vector_store
from vector_store_chroma import create_chroma_vector_store
from document_indexing import create_indexing
# from tools import retrieve_context


# Load environment variables from .env file
load_dotenv('./.env')
# Claude for chat model
if not os.getenv("ANTHROPIC_API_KEY"):
    os.environ["ANTHROPIC_API_KEY"] = getpass.getpass("Enter your Claude API token: ")
# Hugging Face for embeddings
if not os.getenv("HUGGINGFACEHUB_API_TOKEN"):
    os.environ["HUGGINGFACEHUB_API_TOKEN"] = getpass.getpass("Enter your Hugging Face API token: ")

# Initialize the chat model
chat_model = init_chat_model("claude-3-haiku-20240307")
print("✅ Chat model initialized.")

# Embedding model initialization
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
print("✅ Embedding model initialized.")

db_path = "./chroma_langchain_db"
vector_store = create_chroma_vector_store(embeddings, db_path)

if len(os.listdir(db_path)) == 0:
    is_empty = True
else:
    is_empty = False

if is_empty:
    create_indexing(vector_store)
    print("👍 Indexing completed...")
else:
    print("⏭️ Vector store already has data. Skipping indexing...")

from langchain.tools import tool

@tool(response_format="content_and_artifact")
def retrieve_context(query: str):
    """
    Retrieve relevant information from the knowledge base to help answer a query.
    
    Args:
        query: The user's question or search query
        
    Returns:
        Formatted context and retrieved documents
    """
    retrieved_docs = vector_store.similarity_search(query, k=2)
    
    serialized = "\n\n".join(
        (f"Source: {doc.metadata}\nContent: {doc.page_content}")
        for doc in retrieved_docs
    )

    return serialized, retrieved_docs

tools = [
    retrieve_context
]
sys_prompt = (
    "You have access to a tool that retrieves context from a blog post. "
    "Use the tool to help answer user queries."
    "Answer ONLY using the provided documents."
    "If the information is not in the documents, say 'I don't have that information in my knwoledge base.'"
    "Do not use external knowledge."
)
agent = create_agent(chat_model, tools, system_prompt=sys_prompt)

#INTERACT WITH THE AGENT
print("⚠️ Type e to exit. ⚠️")
while True:
    query = input("How can I help you (type...): ")

    if query == "e":
        print("🚶‍➡️ Exiting...")
        break

    if query == "":
        print("☠️ Please enter a valid query. Try again...")
        continue

    # for event in agent.stream(
    #     {"messages": [{"role": "user", "content": query}]},
    #     stream_mode="values",
    # ):
    #     event["messages"][-1].pretty_print()
    response = agent.invoke({
        "messages": [{"role": "user", "content": query}]
    })

    print(response['messages'][-1].content)
