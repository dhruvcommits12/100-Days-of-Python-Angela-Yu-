#Logical operators -> and , or , not (work the same way as AND, OR , NOT gate)

print("Welcome to the rollercoaster!")
height = int(input("What is your height?"))
bill=0

if height>=120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age?"))

    if age<=12:
        bill=5
        print("Please pay $5")
    elif age<=18:
        bill=7
        print("Please pay $7")

    elif age>=45 and age<=55:   #45<=age<=55
        print("Everything is going to be okay:) Have a free ride on us")
    else:
        bill=12
        print("Please pay $12")

    wants_photo = input("Do you want to have a photo taken ? Type y for Yes and n for No ")

    if wants_photo == 'y':
        bill+=3

    print(f"Your total bill is ${bill}")
        
else:
    print("Sorry you have to grow taller before you ride")

