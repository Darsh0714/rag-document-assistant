from langchain_community.document_loaders import PyPDFLoader
import os
def load_pdf(file_path):
     loader=PyPDFLoader(file_path)
     documents=loader.load()
     filename=os.path.basename(file_path)
     for doc in documents:
          doc.metadata["filename"]=filename
     return documents

if __name__=="__main__":
     docs=load_pdf("data/sample.pdf")
     print("Total pages loaded:", len(docs))
     print("\n---First page preview---\n")
     print(docs[0].page_content[:500])