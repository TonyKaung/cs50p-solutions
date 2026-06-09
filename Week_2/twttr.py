word = input("Input: ")
result = []
for i in word:
    if i.lower() not in "aeiou":
        result.append(i)
print("Output:", "".join(result))