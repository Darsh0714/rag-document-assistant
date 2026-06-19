from langchain_text_splitters import RecursiveCharacterTextSplitter
from loader import load_pdf
def split_documents(docs):
    splitter=RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )
    chunks=splitter.split_documents(docs)
    return chunks

if __name__=="__main__":
    docs=load_pdf("data/sample.pdf")
    chunks=split_documents(docs)
    print(f"Total chunks created: {len(chunks)}")

for i, chunk in enumerate(chunks[:5]):
    print("\n" + "="*60)
    print(f"CHUNK {i}")
    print("="*60)
    print(chunk.page_content)
