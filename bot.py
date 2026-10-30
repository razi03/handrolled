replies = {
    "hi": "Hello!",
    "price": "Prices start at 50 lakh.",
    "location": "We're in DHA Phase 6, Lahore.",
    "hours": "We're open 10am to 7pm, Monday to Saturday."
}

name = input("What is your name? ")
print(f"Hello {name}!")
while True:
    ans = input("You: ").lower().strip()
    if ans == "quit":
        print(f"Goodbye {name}")
        break
    reply = replies.get(ans, "I don't understand that yet.")
    print(f"Bot: {reply}")
