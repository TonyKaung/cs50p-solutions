camel_input = input("camelCase: ")
for i in camel_input:
    if i.isupper():
        camel_input = camel_input.replace(i, "_" + i.lower())
print("snake_output:", camel_input)