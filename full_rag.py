from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
import ollama

embedding_model=HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

vectorstore=FAISS.load_local(
    "faiss_index",
    embedding_model,
    allow_dangerous_deserialization=True
)

query=input("ASK A QUESTION: ")

results=vectorstore.similarity_search(query,k=3)

context="\n\n".join([doc.page_content for doc in  results])

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
print("\nRetrieved Context:")
print(context)
print("-"*50)
print(response["message"]["content"])