def main():
    d = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla": 2.00}
    
    menu(d)
        
def menu(d):
    total = 0
    while True:
        try:
            order = input("Item: ").title()
            if order in d:
                total += d.get(order)
                print(f"Total: ${total:.2f}")
        except EOFError:
            break

main()