from mem0 import MemoryClient
import os
from dotenv import load_dotenv

load_dotenv()

def get_mem0_client():
    api_key = os.getenv("MEM0_API_KEY")
    if not api_key:
        raise ValueError("Please Setup MEM0_API_KEY")
    return MemoryClient(api_key=api_key)

### search memory function

def search_memory(query:str,customer_id:str):
    client = get_mem0_client()
    results = client.search(query=query,filters={"user_id":customer_id},limit=5) 
    return results

## add memry function

def add_memory(user_message : str, agent_response : str, customer_id : str):
    client = get_mem0_client()
    client.add(
        messages=[
            {"role" : "user","content":user_message},
            {"role" : "assistant","content":agent_response},
        ],
        user_id=customer_id,
    )


if __name__ == "__main__":
    client = get_mem0_client()
    print("Mem0 client created:", client)

    add_memory("I prefer email over phone calls.", "Noted, I'll use email for follow-ups.", "CUST001")
    print("Memory added")

    print(search_memory("how does the customer prefer contact", "CUST001"))