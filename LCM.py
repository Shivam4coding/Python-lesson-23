
numberlargest = int(input("Enter largest number: "))
numbersmallest = int(input("Enter smallest number: "))

a = numberlargest
b = numbersmallest

while numbersmallest > 0:
    remainder = numberlargest % numbersmallest
    numberlargest = numbersmallest
    numbersmallest = remainder

hcf = numberlargest
lcm = (a * b) // hcf

print("LCM of two numbers is:", lcm)
