import random
import string

letters=string.ascii_letters
specialCharacters = ['$', '#', '@', '!', '*','_']
word=[]
for i in range(int(input("Enter how many letters you need\n"))):
    word+=[random.choice(letters)]
for i in range(int(input("Enter how many number's you need\n"))):
    word+=[random.choice("0123456789")]
for i in range(int(input("Enter how many specials?\n"))):
    word+=[random.choice(specialCharacters)]
print(word)
random.shuffle(word)
print("".join(word))
saves=input("Enter servise name or just skip this by enter\n")
if (saves):
    with open("This_is_not_secure.txt","a") as f:
        f.write(f"Service name:{saves} "+"security: "+"".join(word)+"\n")
        
