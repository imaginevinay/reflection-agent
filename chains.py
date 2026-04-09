from dotenv import load_dotenv
load_dotenv()
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
#ChatPromptTemplate holds our content that we either send to the LLM or  receive back from the LLM, content + role
#MessagesPlaceholder : gives control of what msgs to be rendered during formatting
from langchain_groq import ChatGroq #since open ai is paid we are using GROQ

# chains ----------

reflection_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a viral twitter influencer grading a tweet. Generate critique and recommendations for user's tweet."
            "Always provide detailed recommendations, including requests for length, virality, style, etc."
        ), 
        MessagesPlaceholder(variable_name="messages")       
    ]
)

generation_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a twitter tech influencer assistant tasked with writing excellent twitter posts."
            "Generate the best twitter post possible for the user's request."
            "If the user provides critque, respond with a revised version of your previous attempts."
        ), 
        MessagesPlaceholder(variable_name="messages")       
    ]
)

llm = ChatGroq(model="openai/gpt-oss-120b") #initialize the llm

generate_chain = generation_prompt | llm
reflect_chain = reflection_prompt | llm