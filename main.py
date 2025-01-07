import os
from  langchain_openai import ChatOpenAI
from dotenv import load_dotenv, find_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage

load_dotenv(find_dotenv(),override=True)

if __name__ == "__main__":
    open_ai_api_key= os.getenv("OPENAI_API_KEY")
    llm = ChatOpenAI(
    model="gpt-4o-mini")
    # PROMPT TEMPLATE
    # messages = [
    #     SystemMessage("You are a doctor recommend a Treatment for this illness"),
    #     HumanMessage("HBV")
    # ]
    # answer = llm.invoke(messages)
    # print(answer.content)
    prompt_template=ChatPromptTemplate.from_messages([("system","Translate the following from English to{language}"),
    ("user","{text}")])
    prompt= prompt_template.invoke({"language":"chinese","text":"My name is teejay"})
    result = llm.invoke(prompt)
    print(result.content)


















# if __name__ == "__main__":
#     # Fetch the OpenAI API key from environment variables
#     open_ai_api_key = os.getenv("OPENAI_API_KEY")
#     print(f"API Key: {open_ai_api_key}")


#     # Ensure the API key is set
#     if not open_ai_api_key:
#         print("Error: OPENAI_API_KEY environment variable is not set.")
#     else:
#         # Initialize the LLM
#         llm = ChatOpenAI(
#             model="gpt-4o-mini",
#             openai_api_key=open_ai_api_key  # Pass the API key explicitly
#         )

#         # Ask a question
#         try:
#             question = llm.invoke("Who is the president of Nigeria?")
#             print(question)
#         except Exception as e:
#             print(f"An error occurred: {e}")