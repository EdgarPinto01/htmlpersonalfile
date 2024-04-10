print("Welcomw to the tip calculator")
bill = float(input("what is the total bill?"))
people = int(input("how many to split the bill with?"))
tip = int(input("what percentage tip would you like to give?"))
billwtip = tip / 100 * bill + bill
eachpp = billwtip / people
print(billwtip)
print(eachpp)