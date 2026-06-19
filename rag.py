from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

embedding_model=HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)
vectorstore=FAISS.load_local(
    "faiss_index",
    embedding_model,
    allow_dangerous_deserialization=True
)
query="What is the timeline"
results=vectorstore.similarity_search_with_score(query,k=3)

for i,(doc,score) in enumerate(results,start=1):
    print(f"\nResult {i}")
    print("-"*50)
    print(f"Similarity Score: {score}")
    print("\nMetadata:")
    print(doc.metadata)
    print("\nContent:")
    print(doc.page_content[:400])
