# after run this code. You will see positive if the string contain concecutive vowels like "soon","spoon","tail","people"
# but you will see negative if the string doesn't contain any concecutive vowels like "apple","person","anyone" 

word = input("Please enter a string: ")
word = word.lower()

vowels = ["a", "e", "i", "o", "u"]
exist = False

for i in range(len(word)-1):
  if word[i] in vowels:
    if word[i+1] in vowels:
      exist = True
      break
      
if exist:
  print("Positive")
else:
  print("Negative")
