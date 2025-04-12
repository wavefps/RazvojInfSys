import random
import string

text = input("Type something and I will remove some characters :) ")
removeList = []
for i in range(10):
    removeList.append(random.choice(string.ascii_letters))


new_text = [el for el in text if el not in removeList]
print("Modified text:", ''.join(new_text))

