u_input = input("Please greet the customer: ").lower().strip()
if(u_input.startswith("hello")):
    print("$0")
elif(u_input.startswith("h")):
    print("$20")
else:
    print("$100")