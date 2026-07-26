### Importing dependecies
from pymongo import MongoClient
import os
from dotenv import load_dotenv

### loading environment variables

load_dotenv()

### Getting MongoDB URL From Environment Variables

def get_mongodb_url():
    if os.getenv("MONGODB_URL"):
        return os.getenv("MONGODB_URL")
    else:
        raise ValueError("Please Setup MongoDB URL.")

### Creating MongoDB Clients

def get_mongodb_client():
    MONGODB_URL = get_mongodb_url()
    if MONGODB_URL:
        MONGODB_CLIENT = MongoClient(MONGODB_URL)
        return MONGODB_CLIENT
    else:
        raise ValueError("MongoDB Client Intialization failed.")
    
### Getting Database details from MongoDB Client
    
def support_db_details():
    mongodb_client = get_mongodb_client()
    if mongodb_client is not None:
        support_db = mongodb_client["support_agent_db"]
        return support_db
    else:
        raise ValueError("Support Agent DB Not Found.")

### Getting orders collection details

def get_orders_collection():
    db_details = support_db_details()
    if db_details is not None:
        orders_collection = db_details["orders"]
        return orders_collection
    else:
        raise ValueError("Error while getting data from the orders Collection.")

### Getting customers collection details
def get_customers_collection():
    db_details = support_db_details()
    if db_details is not None:
        customers_collection = db_details["customers"]
        return customers_collection
    else:
        raise ValueError("Error while getting data from the customers collection.")


if __name__ == "__main__":
    db = support_db_details()
    db.client.admin.command("ping")
    print("Connected to Mongodb Successfully")