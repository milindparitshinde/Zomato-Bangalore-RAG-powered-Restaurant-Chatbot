import pandas as pd
import sys
import csv
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter


def create_indexing(vector_store):
    CHUNK_SIZE = 1000
    CHUNK_OVERLAP = 200 # 10% - 20% of chunk size
    BATCH_SIZE = 100  # Add documents in batches of 100

    # ========== INCREASE CSV LIMIT ==========
    max_int = sys.maxsize
    while True:
        try:
            csv.field_size_limit(max_int)
            break
        except OverflowError:
            max_int //= 2

    #Loading
    df = pd.read_csv('./../zomato.csv')
    documents = [
        Document(
            page_content=row.to_string(), 
            metadata={"source": "data.csv", "row": i}#{"row": i}
        )
        for i, row in df.iterrows()
    ]
    print(f"Loaded {len(documents)} documents from the CSV file -> pandas df.")

    #Spliting
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE, 
        chunk_overlap=CHUNK_OVERLAP
    )
    splits = splitter.split_documents(documents)
    print(f"Split blog post into {len(splits)} sub-documents.")

    #Storing
    # vector_store.add_documents(documents=all_splits)
    # print("Documents added to vector store.")

    # ========== ADD DOCUMENTS IN BATCHES ==========
    print(f"\nAdding {len(splits)} documents in batches of {BATCH_SIZE}...")

    total_batches = (len(splits) + BATCH_SIZE - 1) // BATCH_SIZE
    successful = 0
    failed = 0

    for batch_num in range(1, total_batches + 1):
        start_idx = (batch_num - 1) * BATCH_SIZE
        end_idx = min(batch_num * BATCH_SIZE, len(splits))
        batch = splits[start_idx:end_idx]
        
        try:
            vector_store.add_documents(batch)
            successful += len(batch)
            progress = (successful / len(splits)) * 100
            print(f"✅ Batch {batch_num}/{total_batches}: Added {len(batch)} docs "
                f"({progress:.1f}% complete)")
        except Exception as e:
            failed += len(batch)
            print(f"❌ Batch {batch_num} FAILED: {e}")

    # ========== RESULTS ==========
    print(f"\n{'='*60}")
    print(f"COMPLETED!")
    print(f"{'='*60}")
    print(f"✅ Successfully added: {successful} documents")
    if failed > 0:
        print(f"❌ Failed: {failed} documents")
    print(f"Total: {successful + failed}/{len(splits)}")

    # ========== VERIFY ==========
    print(f"\n{'='*60}")
    print("VERIFICATION")
    print(f"{'='*60}")
