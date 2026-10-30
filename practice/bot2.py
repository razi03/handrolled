replies: dict = {
    "hi" : "Hello!",
    "price" : "Prices start at 50 lakh.",
    "location" : "We're in DHA Phase 6, Lahore.",
    "hours" : "We're open 10am to 7pm, Monday to Saturday."
}

name: str = input("What is your name? ")
print(f"BOT: Hello {name}")

while True:
    response = input("YOU: ").strip().lower()
    if response == "quit":
        print(f"BOT: Goodbye {name}")
        break
    reply = replies.get(response, "I don't understand that yet.")
    print(f"BOT: {reply}")
