print("Welcome to the tip calculator")
bill = float(input("What was the total bill : $"))

tip = int(input("What percentage of tip would you like to give:"))

people = int(input("How many people to split the bill:"))

amount = (bill + tip*bill/100)/people
final_amount = round(amount,2)

print(f"Each person will pay ${final_amount}")

