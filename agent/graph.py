### Importing Required Deps
from tools.customer_tool import get_customers_status
from tools.order_tool import get_order_status
from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from mem0 import MemoryClient

### Loading Environment variables

load_dotenv()

### Loading OpenAI API Key

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

### Loading Mem0 api key

MEM0_API_KEY = os.getenv("MEM0_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("Please set OPENAI_API_KEY in .env file.")

### llm setup
llm = ChatOpenAI(base_url=os.getenv("OPENAI_BASE_URL"),
                 api_key=OPENAI_API_KEY,
                 model=os.getenv("OPENAI_MODEL_NAME"))

### tools setup
tools = [get_order_status,get_customers_status]

### Agent
agent = create_agent(model=llm,tools=tools)

### creating agent function
def run_agent(user_message : str) -> str:
    response = agent.invoke({"messages" : [{"role" : "user","content" : user_message}]})
    final_message = response["messages"][-1] ### get last message which agent generated
    return final_message.content


### main block
if __name__ == "__main__":
    print(run_agent("What is the status of order ORD1001?"))
    print(run_agent("Can you tell me the billing status for customer CUST002?"))
    print(run_agent("What's the weather like today?"))