from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
import ollama
import os
embedding_model=HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en-v1.5"
)

vectorstore=FAISS.load_local(
    "faiss_index",
    embedding_model,
    allow_dangerous_deserialization=True
)
def ask_question(query):
    print("NEW VERSION OF FULL_RAG IS RUNNING")
    results=vectorstore.similarity_search(query,k=3)
    print("\nMETADATA:")
    print(results[0].metadata)
    context="\n\n".join(
        [doc.page_content for doc in results]
    )
    results = vectorstore.similarity_search(query, k=3)
    print(results[0].metadata)
    document_name = os.path.basename(
    results[0].metadata.get("source", "Unknown Document")
)
    page_number = results[0].metadata.get("page", 0)
    prompt = f"""
You are a document assistant.

Answer ONLY from the context provided below.

If the answer is not present in the context, say:
'I could not find the answer in the document.'

Context:
{context}

Question:
{query}

Answer:
"""
    response=ollama.chat(
      model="phi3:mini",
      messages=[
        {
            "role":"user",
            "content":prompt
        }
      ]
    )
    return (
        response["message"]["content"],
        context,
        document_name,
        page_number
    )