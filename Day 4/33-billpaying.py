import random

friends = ["David","Sam","Julie","Ethan","Maria"]

random_choice = random.randint(0,4)
print(friends[random_choice])

#Option 2

print(random.choice(friends))