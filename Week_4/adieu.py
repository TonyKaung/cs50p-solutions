import inflect

p = inflect.engine()
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
if len(names) == 1:
    print(f"Adieu, adieu, to {names[0]}")
else:
    print("Adieu, adieu, to", p.join(names))
