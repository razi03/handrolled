# Warm-up 2 (Sat 31 Oct 2026): lists of dicts, quotes vs variables, counting
#
# Given a list of bikes, where each bike is a dictionary with "name" and "color":
#
# Task A: Count how many bikes there are of each colour and print the counts.
#         Expected output: {'red': 2, 'blue': 1}
#
# Task B: Print only the names of the red bikes, one per line.
#         Expected output:
#         Comet
#         Nova
#
# Concepts practised:
#   - Read a dict value with square brackets and a quoted fixed key: bike["color"]
#     (not bike.color, since dot notation is for objects, not dicts)
#   - Counting pattern: counts[key] = counts.get(key, 0) + 1   (use =, not +=)
#   - Quotes vs variables: fixed text gets quotes ("color", "red"),
#     values that change with the data come from variables (bike, counts)
#   - Filter pattern: loop, if, then act on the matching items
#
# Mistakes made the first time: bike.color (dot notation), += instead of =,
# bikes.get (the list) instead of counts.get (the tally dict).

bikes = [
    {"name": "Comet", "color": "red"},
    {"name": "Bolt", "color": "blue"},
    {"name": "Nova", "color": "red"},
]
counts = {}

for bike in bikes:
    if not bike["color"]:
        continue
    counts[bike["color"]] = counts.get(bike["color"],0) + 1
print(counts)

for bike in bikes:
    if bike["color"] == "red":
        print(bike["name"])