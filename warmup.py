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