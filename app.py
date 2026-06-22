import streamlit as st
from full_rag import ask_question

st.set_page_config(
    page_title="RAG Document Assistant",
    page_icon="📄"
)

st.title("📄 RAG Document Assistant")

query = st.text_input(
    "Ask a question about the document"
)

if st.button("Submit"):

    if query:

        with st.spinner("Searching document..."):

            result = ask_question(query)
            answer, context, document_name, page_number = ask_question(query)

            st.write(
                f"📄 Document: {document_name} | Page: {page_number + 1}"
            )

            st.subheader("Answer")
            st.write(answer)

        with st.expander("Retrieved Context"):
            st.write(context)