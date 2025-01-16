# Basic_LLM_ChatBot
This Python project is a simple demonstration of integrating the LangChain library and OpenAI's GPT models to create a conversational AI system. The program utilizes environment variables for API key management, ensuring secure and reusable code. The main purpose is to use the ChatOpenAI class to process a user query and provide a response based on OpenAI's GPT model.
Key Components
1. Environment Variable Management

    Why: Storing sensitive information like API keys directly in the code is insecure. Instead, this project uses environment variables to keep the OpenAI API key secure.
    How:
        The dotenv library is used to load environment variables from a .env file.
        find_dotenv() helps locate the .env file automatically, and override=True ensures that any existing environment variables are overwritten with the ones in the .env file.

2. OpenAI Integration with LangChain

    Library: langchain_openai
    Purpose: To interface with OpenAI's GPT-4 model (gpt-4o-mini) via the ChatOpenAI class.
    Functionality:
        The ChatOpenAI class simplifies the interaction with OpenAI's API by handling input prompts and returning model-generated responses.

3. Script Functionality

    The script fetches the OpenAI API key from the environment variables using:

open_ai_api_key = os.getenv("OPENAI_API_KEY")

It initializes an instance of ChatOpenAI with the model gpt-4o-mini:

llm = ChatOpenAI(model="gpt-4o-mini")

It processes a user query, in this case: "Who is the president of Nigeria".
The response from the model is printed to the console.


## VectorStore.py

### Legal Document AI Search Project

This project demonstrates how to leverage artificial intelligence for efficient document analysis and retrieval, specifically focusing on legal texts. The system is designed to streamline research by converting unstructured text from legal documents into vector embeddings, allowing for semantic similarity searches.

### Project Overview

This project processes a legal PDF file, splits its content into manageable chunks, and performs similarity searches on the text using vector embeddings. It is ideal for legal professionals, researchers, and students who need quick access to relevant information from lengthy documents.

### Features

PDF Processing: Load and parse legal documents from PDF files.

Text Chunking: Split text into smaller, overlapping chunks to preserve context.

AI-Powered Embeddings: Use OpenAI's embeddings model to convert text into vector representations.

In-Memory Vector Database: Store the embeddings and enable efficient similarity searches.

Semantic Search: Query the vector database to retrieve the most relevant sections of the document.

How It Works

1. PDF Loading

The project uses PyPDFLoader to load and parse the content of the PDF file.

loader = PyPDFLoader(file_path="PDF/Volume-4.pdf")
loaded_documents = loader.load()

2. Text Splitting

To handle large amounts of text, the RecursiveCharacterTextSplitter is used to divide the document into chunks with some overlap for contextual understanding.

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200, add_start_index=True)
splitted_docs = text_splitter.split_documents(documents=loaded_documents)

3. Embedding Generation

The text chunks are converted into vector embeddings using OpenAI's embedding model text-embedding-3-large.

embedding = OpenAIEmbeddings(model="text-embedding-3-large")

4. Vector Database Creation

The embeddings are stored in an in-memory vector database for quick and efficient similarity searches.

vector_store = InMemoryVectorStore(embedding=embedding)
vector_store.add_documents(splitted_docs)

5. Similarity Search

Users can query the vector database for specific information, and the system retrieves the most relevant chunks based on semantic similarity.

results = vector_store.similarity_search(query="Who published the Nigerian Banking Law Reports?")
print(results)

Technologies Used

LangChain: For text processing and document handling.

OpenAI: For generating text embeddings.

Python: Programming language for implementation.

PyPDFLoader: For loading PDF content.

InMemoryVectorStore: To store and query vector embeddings.