This is a customer support chat agent that looks up order status and billing details, and remembers past conversations using long term memory. It combines tool calling, agentic reasoning, and a real backend service rather than a notebook demo.

The agent uses Groq for fast responses, LangChain for the tool calling loop, MongoDB for customer and order records, and Mem0 for memory that persists across sessions. A FastAPI backend exposes a chat endpoint, and a small HTML frontend lets you test it in the browser.

To run it locally, set up a virtual environment, install requirements, add your API keys and MongoDB URL to a .env file, then run uvicorn main:app --reload and open http://127.0.0.1:8000.