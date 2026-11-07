numberlargest = int(input("Enter largest number: "))
numbersmallest = int(input("Enter smallest number: "))
while numbersmallest > 0:
    numbersmallest = numberlargest % numbersmallest
    numberlargest = numbersmallest 
    hcf = numberlargest
print("HCF of two numbers is:", hcf)
    
