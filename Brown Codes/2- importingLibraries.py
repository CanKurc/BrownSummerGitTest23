import math
import random

result_1 = math.pow(2, 4) #2^4
print("Result 1 is: " , result_1)

result_2 = math.sqrt(16) #square root of 16
print("Result 2 is: ", result_2)

result_3 = random.randint(0, 100) #random integer from 0 and 100
print("Result 3 is: ", result_3)

names = ["Amaryllis", "Godson", "Reina", "Derin", "Elena", "Inacio"]
print("Original names: ", names)

random.shuffle(names) #shuffles the elements in the array
print("Names after shuffling: ", names)

result_4 = random.choice(names) #randomly selects an element in the array
print("Result 4 is: ", result_4)