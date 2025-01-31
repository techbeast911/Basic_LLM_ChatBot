import os
from  langchain_openai import ChatOpenAI
from dotenv import load_dotenv, find_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_core.runnables import RunnablePassthrough

load_dotenv(find_dotenv(),override=True)

if __name__ == "__main__":
    file_path= "PDF/Volume-4.pdf"
    loader = PyPDFLoader(file_path=file_path)
    loaded_documents= loader.load()
    # for document in loaded_documents:
    #     print(document.metadata)
    #     print(document.page_content)

    #SPLITTING AND CHUNCKING
    text_splitter = RecursiveCharacterTextSplitter(chunk_size= 1000,chunk_overlap = 200, add_start_index= True)

    splitted_docs= text_splitter.split_documents(documents=loaded_documents)

    ## Embedding to convert text into vectors
    embedding = OpenAIEmbeddings(model= "text-embedding-3-large")

    # Create VectorDB
    vector_store = InMemoryVectorStore(embedding=embedding)
    vector_store.add_documents(splitted_docs)

    # Perform Similarity search
    results= vector_store.similarity_search(query= "Who published the nigerian banking law reports?")
    print(results[0].page_content)

    # Retriever
    retriever= vector_store.as_retriever(search_type='similarity',search_kwargs={"k":1})

    llm=ChatOpenAI(model="gpt-4o-mini")

    message="""
                Answer the following questions using context only.If you do not know the answer say you do not 
                know, do not make anything up:

                {question}

                Context:
                {context}
    
                """
    
    prompt= ChatPromptTemplate.from_messages([("humam",message)])
    rag_chain = {"context":retriever, "question":RunnablePassthrough} | prompt | llm

    response= rag_chain.invoke("Who published the nigerian banking law reports?")

    print(f"this is from the llm \n{response.content}")