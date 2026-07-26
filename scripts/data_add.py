"""
Run this to insert test documents into the customers and orders
collections.
"""

from db.connection import get_orders_collection, get_customers_collection

orders_collection = get_orders_collection()
customers_collection = get_customers_collection()

customers = [
    {
        "customer_id": "CUST001",
        "name": "Aarav Shah",
        "billing_status": "active",
        "plan": "pro",
    },
    {
        "customer_id": "CUST002",
        "name": "Priya Mehta",
        "billing_status": "past_due",
        "plan": "basic",
    },
    {
        "customer_id": "CUST003",
        "name": "Rohan Patel",
        "billing_status": "active",
        "plan": "enterprise",
    },
]

orders = [
    {
        "order_id": "ORD1001",
        "customer_id": "CUST001",
        "item": "Wireless Mouse",
        "status": "shipped",
    },
    {
        "order_id": "ORD1002",
        "customer_id": "CUST002",
        "item": "Mechanical Keyboard",
        "status": "processing",
    },
    {
        "order_id": "ORD1003",
        "customer_id": "CUST003",
        "item": "USB-C Hub",
        "status": "delivered",
    },
]

if __name__ == "__main__":
    # clear existing test docs
    # customers_collection.delete_many({"customer_id": {"$in": [c["customer_id"] for c in customers]}})
    # orders_collection.delete_many({"order_id": {"$in": [o["order_id"] for o in orders]}})

    customers_collection.insert_many(customers)
    orders_collection.insert_many(orders)

    print(f"Inserted {len(customers)} customers and {len(orders)} orders.")