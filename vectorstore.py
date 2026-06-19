from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

from loader import load_pdf
from chuncking import split_documents

docs=load_pdf("data/sample.pdf")
chunks=split_documents(docs)

embedding_model=HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

vectorstore=FAISS.from_documents(
    documents=chunks,
    embedding=embedding_model
)

vectorstore.save_local("faiss_index")

print("FAISS index created successfully")
print("Number of chunks stored:",len(chunks))