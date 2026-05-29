import inflect

p = inflect.engine()
count = 0
names = []
# get multiple names
while True:
    try:
        name = input("Name: ").title()
        names.append(name)
        count += 1
    except EOFError:
        print()
        break

# check number of names
if count == 1:
    print(f"Adieu, adieu, to {names[0]}")
else:
    print("Adieu, adieu, to", p.join(names))
