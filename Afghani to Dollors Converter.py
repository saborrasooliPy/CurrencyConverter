print("Welcome To Python Exchange")
print("You Want to Change Dollor to Af or Af Dollor, Type 1. $ to AF, Type 2.AF to $")
Dollor_cost = 74
Afghani_cost = 74
given = input("   Enter ::     ")
if given == "1":
    Dollors = input("Enter Your Balance:  ")
    comes_in_Afghanis = int((Dollor_cost*(Dollors)))
    print("It`s in Afghanis " + comes_in_Afghanis)
elif given == "2":
    Afghanis = input("Enter Your Balance: ")
    comes_in_Dollors = int(((Afghanis)/74))
    print("It`s in Dollors : " + comes_in_Dollors)