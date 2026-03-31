# To generate random numbers in Python Mersenne - Twister algo is used 
# module -> file containing python code which can be reused in other programs
# random module -> built in module which helps us generate random numbers

import random
import mymodule

random_int = random.randint(1,10)
print(random_int)

print(mymodule.myfavnum)

random_num_0_to_10 = random.random()*10
print(random_num_0_to_10)

random_float = random.uniform(1,10)
print(random_float)

#Heads n Tails

random_heads_or_tails = random.randint(0,1)

if random_heads_or_tails==0:
    print("Heads")
else:
    print("Tails")



