### Importing required dependencies

from db.connection import get_customers_collection
from langchain_core.tools import tool


### Fetching customers collections details.

customers_collection = get_customers_collection()

### Defining the tool function block

@tool
def get_customers_status(customer_id : str) -> str:

    """
    This function retrieves the current customers details 
    based on the customers_id and returns a string response.

    Use this when you want any customer's details. Requires the exact 'customer_id'
    (e.g. "CSTM578").
    """

    result  = customers_collection.find_one({"customer_id" : customer_id})

    if result:
        result.pop("_id",None) #The None default means it won't error even if _id somehow isn't present.
        return str(result)
    else:
        return f"No customer found with ID {customer_id}."


if __name__ == "__main__":
    print(get_customers_status.invoke({"customer_id" : "CUST001"}))