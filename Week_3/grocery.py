from collections import Counter

item = []
while True:
    try:
        item.append(input("Item: ").lower().strip())
    except EOFError:
        break

counts = Counter(item)
for item, count in sorted(counts.items()):
    print(f"{count} {item.upper()}")