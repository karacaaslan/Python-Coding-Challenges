String_Input = input ("Please enter a string: ")
vowels = ["a","e","i","o","u"]
index_list = []

for i in String_Input:
    if i in vowels:
        index_number=vowels.index(i)
        index_list.append(index_number)
print(index_list)

if index_list == sorted(index_list):
    print("Positive")
else:
    print("Negative")
