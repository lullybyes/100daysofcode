print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? "))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, 15, 20? "))
tip_amount = (total_bill * tip_percentage) / 100
total = tip_amount + total_bill
people = int(input("How many people to split the bill? "))
split = total / people
print(f"Each person should pay: ${round(split, 2)}")