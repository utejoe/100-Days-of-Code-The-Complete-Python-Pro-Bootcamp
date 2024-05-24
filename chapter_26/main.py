# If the bill was $150.00 split between 5 people, with 12% tip
# Each person should pay (150.0 /5) * 1/12 = 33.6
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip will you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill?"))
bill_with_tip = tip/100 * bill + bill
print(bill_with_tip)

