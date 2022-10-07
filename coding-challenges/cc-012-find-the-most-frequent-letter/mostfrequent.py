words = []
letter_count = {}


while True:
    string = input("enter a string: ")
    string = string.lower()
    if string != "exit":
        words.append(string)
    else:
        break
concate = ''.join(words)


for i in concate:
    if i in letter_count:
        letter_count[i] += 1
    else:
        letter_count[i] = 1

new_value = max(letter_count, key=letter_count.get)
print(new_value,":",letter_count[new_value])

print({k: v for k, v in sorted(letter_count.items(), key=lambda item: item[1])})

