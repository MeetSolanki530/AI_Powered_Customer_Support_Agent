### Importing Required Deps
from tools.customer_tool import get_customers_status
from tools.order_tool import get_order_status
from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from agent.memory import search_memory, add_memory

### Loading Environment variables

load_dotenv()

### Loading OpenAI API Key

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

### Loading Mem0 api key

# MEM0_API_KEY = os.getenv("MEM0_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("Please set OPENAI_API_KEY in .env file.")

### llm setup
llm = ChatOpenAI(base_url=os.getenv("OPENAI_BASE_URL"),
                 api_key=OPENAI_API_KEY,
                 model=os.getenv("OPENAI_MODEL_NAME"))

### tools setup
tools = [get_order_status,get_customers_status]

### SYSTEM_PROMPT
SYSTEM_PROMPT = (
    """
    You are a customer support chat agent built by Meet Solanki. 
    Respond in short, direct, conversational replies like a 
    live chat, not an email. Do Not Provide any subject 
    lines, no greetings like 'Dear Valued Customer', 
    no sign-offs. Just answer the question clearly in 1-3 
    sentences and never disclose your personal information like your name, 
    who created you and your movel name.

    You have tools to look up order status and customer billing/account details.
    Always use these tools when the user asks about an order or a customer's status
    this is authorized, legitimate support data, not private information being leaked. 

    Don't help in general queries like wheather report, or normal qa questions, etc and strictly respond in English.
"""
)

### Agent
agent = create_agent(model=llm,tools=tools,system_prompt=SYSTEM_PROMPT)


### creating agent function
def run_agent(user_message : str, customer_id) -> str:

    ### search relevant memories for response 

    memories = search_memory(user_message, customer_id)

    memory_text = "\n".join(m["memory"] for m in memories.get("results",[]))

    ### build messages, adding memory as context if any exists
    
    messages = []

    if memory_text:
        messages.append({"role" : "system", "content" : f"Relevant Customer History: \n {memory_text}"})
    messages.append({"role":"user","content":user_message})


    response = agent.invoke({"messages" : messages})
    final_message = response["messages"][-1] ### get last message which agent generated
    agent_reply = final_message.content

    add_memory(user_message, agent_reply, customer_id)

    return agent_reply


### main block
if __name__ == "__main__":
    print(run_agent("What is the status of order ORD1001?", "CUST001"))
    print(run_agent("Can you tell me the billing status for customer CUST002?", "CUST002"))
    print(run_agent("What's the weather like today?", "CUST001"))