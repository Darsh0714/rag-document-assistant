from langchain_community.document_loaders import PyPDFLoader
def load_pdf(file_path):
     loader=PyPDFLoader(file_path)
     documents=loader.load()
     return documents

if __name__=="__main__":
     docs=load_pdf("data/sample.pdf")
     print("Total pages loaded:", len(docs))
     print("\n---First page preview---\n")
     print(docs[0].page_content[:500])