camel_input = input("camelCase: ")
result = []
for i in camel_input:
    if i.isupper():
        result.append("_" + i.lower())
    else:
        result.append(i)
print("snake_case:", "".join(result))