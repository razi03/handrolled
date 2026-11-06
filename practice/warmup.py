# Warm-up 1 (Fri 30 Oct 2026): dict lookup with a fallback, counting
#
# Task A: Look up `message` in the `replies` dict.
#         If it isn't a key, reply with "I don't understand that yet."
#         Print the reply.
#         Expected output: I don't understand that yet.
#
# Task B: Count how many times each vote appears in `votes`.
#         Clean each vote with .strip().lower() first.
#         Print the counts.
#         Expected output: {'chips': 2, 'apple': 1}
#
# Concepts practised:
#   - Lookup with a fallback in one call: d.get(key, default)
#     (no loop needed to look up a single key)
#   - Counting pattern: counts[key] = counts.get(key, 0) + 1
#   - Cleaning input before using it as a key
#   - Using the right variable: check what each name holds before using it
#
# Mistakes made the first time: looped over the whole dict instead of looking up
# `message` once; in Task B used `val` (a leftover variable from Task A's loop)
# instead of the cleaned vote `act`; printed `act` (the last vote) instead of `counts`.

replies = {"hi" : "Hello!",
           "price" : "Prices start at 50 lakh."}
message = "weather"

reply = replies.get(message , "I don't understand that yet.")
print(reply)

votes = ["chips", "apple", "chips"]
counts = {}

for vote in votes:
    act = vote.strip().lower()
    counts[act] = counts.get(act , 0) + 1
print (counts)