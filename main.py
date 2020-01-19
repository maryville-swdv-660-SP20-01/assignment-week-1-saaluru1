# importing "random" for random operations 
import random
from addition.add import add
from random_word import RandomWords
ran = RandomWords()

# using randrange() to generate in range from 1 to 100 
print ("Selecting two random numbers from 1 to 100 : ")
r1 = random.randrange(1,100)
print (r1)
r2 = random.randrange(1,100)
print (r2)
print ("Calculating sum of the above two random numbers using 'math-addition' package : ")
print(add(r1,r2))
print ("Generating random words using 'Random-Word' package : ")
print(ran.get_random_words())
input("Press ENTER to continue!")

