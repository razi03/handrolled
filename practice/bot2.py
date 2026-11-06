# Rung 1 rewrite from memory (Thu 29 Oct 2026): terminal chat bot
#
# Requirements:
#   1. A dict of 4 known messages and their replies: hi, price, location, hours
#   2. Ask "What is your name? " and greet the user by name
#   3. Keep asking "YOU: " forever
#   4. Clean every message: ignore capitals and spaces at the edges
#   5. If the message is "quit", say goodbye by name and stop
#   6. If it's a known message, reply with its answer
#   7. Anything else, including an empty message: "I don't understand that yet."
#
# Test inputs and expected replies:
#   Razi          -> BOT: Hello Razi
#   hi / "  HI  " -> BOT: Hello!
#   price         -> BOT: Prices start at 50 lakh.
#   what's up     -> BOT: I don't understand that yet.
#   (empty)       -> BOT: I don't understand that yet.
#   "  QUIT "     -> BOT: Goodbye Razi  (program ends)
#
# Concepts practised:
#   - while True + break, with a guard clause for "quit"
#   - Clean input once at the source: input(...).strip().lower()
#   - Lookup with a fallback: replies.get(key, default)
#     (it replaces the `in` check; it doesn't go inside it)
#   - Constant data (the replies dict) defined once, outside the loop
#
# Mistakes made the first time: fell back to echoing the message ("You said ...")
# instead of a fallback reply; used in + [ ] + continue instead of .get();
# put .get() inside the `elif in` branch, where its default could never be used;
# same quotes inside an f-string (SyntaxError on Python 3.9) -> fix: get the
# value into a variable first, then print the variable.

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
