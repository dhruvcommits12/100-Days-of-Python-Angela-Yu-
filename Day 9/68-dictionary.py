#Dictionary -> {Key : Value}

programming_dictionary = {
    "Bug":"An error in a program that prevents the program from running as expected",
    "Function":"A piece of code that you can easily call over again and again",
}

# print(programming_dictionary["Bug"])

#Adding data
programming_dictionary["Loop"] = "The action of doing something over and over again"

#Wipe an existing directory 

# programming_dictionary = {}

#Editing data
programming_dictionary["Bug"] = "A moth in your computer"

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

