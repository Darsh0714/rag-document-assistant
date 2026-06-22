from sentence_transformers import SentenceTransformer
from loader import load_pdf
from chuncking import split_documents

model=SentenceTransformer("BAAI/bge-small-en-v1.5")

docs=load_pdf("data/sample.pdf")
chunks=split_documents(docs)

embeddings=model.encode(
    [chunk.page_content for chunk in chunks]
)

print("Number of chunks:",len(chunks))
print("Embeddings dimensions:",len(embeddings[0]))
print("First 10 values:")
print(embeddings[0][:10])