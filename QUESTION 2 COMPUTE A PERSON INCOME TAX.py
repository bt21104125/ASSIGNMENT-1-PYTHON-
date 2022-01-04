#PROGRAM TO CALCULATE THE INCOME TAX OF PERSON AFTER SEVERAL DEDUCTION OF MONEY
gross_income=int(input("Please Enter the Gross Income:$ "))
numberofdependents=int(input("Please Enter the number of dependents: "))
#deduction1=Standard Deduction
deduction1=10000
#deduction2=Dependent Deduction
deduction2=int(3000*numberofdependents)
Taxable_income=int(gross_income)-int(deduction1)-int(deduction2)
Tax_rate=.20*Taxable_income
Tax=Taxable_income+Tax_rate
print("The total income tax of a person: " , Tax)


                       
