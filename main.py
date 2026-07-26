from agent.graph import run_agent

if __name__ == "__main__":
    print("Customer Support Agent - type 'exit' to quit")

    while True:
        user_input = input("You: ")

        if user_input.strip().lower() == "exit":
            print("Goodbye.")
            break

        response = run_agent(user_input)
        print(f"Agent: {response}")