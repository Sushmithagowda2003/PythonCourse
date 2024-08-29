##welcome to the tip calculator
##What was the total bill?$124.56
##How much tip would you like to give ? 10, 12, or 15?12
##How many people to split the bill?7
##Each person should pay:$19.93
print("welcome to the tip calculator")
bill=float(input("enter the total bill:"))
tip=int(input("How much tip wpuld you like to give 10,12 or 15:"))
persons=int(input("how many to split with:"))
tip=tip/100
print(tip)
total=bill*tip
total+=bill
print(total)
amount=total/persons
amount=round(amount,2)
print(f"each person have to pay {amount}")