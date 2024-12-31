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
