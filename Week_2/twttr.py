word = input("Input: ")
for i in word:
    if i.lower() in "aeiou":
        word = word.replace(i, "")
print("Output:", word)