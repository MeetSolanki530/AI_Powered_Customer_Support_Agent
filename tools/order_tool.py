### Importing required dependencies

from db.connection import get_orders_collection
from langchain_core.tools import tool


### Fetching Orders collections details.

orders_collection = get_orders_collection()

### Defining the tool function block

@tool
def get_order_status(order_id : str) -> str:

    """
    This function retrieves the current order status 
    based on the order_id and returns a string response.

    Use this when a customer asks about the status, shipping, or
    delivery of a specific order. Requires the exact 'order_id'
    (e.g. "ORD1001"). Do not use this for billing or payment questions.
    """

    result  = orders_collection.find_one({"order_id" : order_id})

    if result:
        result.pop("_id",None) #The None default means it won't error even if _id somehow isn't present.
        return str(result)
    else:
        return f"No order found with ID {order_id}."


if __name__ == "__main__":
    print(get_order_status.invoke({"order_id" : "ORD1001"}))