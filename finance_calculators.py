#Capstone Project 1.
#A program that allows the user to calculate their interest on an investment or calculate the amount that should be repaid on a home loan each month.

#Allowing the user to enter either Investment or Bond from the selection.
print("Choose either \'investment\' or \'bond\' from the menu below to proceed: \n")
print("Investment \t - To calculate the amount of interest you'll earn on interest")
print("Bond \t \t - To calculate the amount you'll have to pay on a home loan \n")
interest = input("investment or bond: ").capitalize()
print("\n")

#Calculation if 'Investment' was selected.
if interest == "Investment":
    print("Investment selected \n")
    amount = (float(input("Please enter the amount that you will be depositing: ")))
    interest_rate = (float(input("Please enter the interest rate (only insert the number): ")))
    period = (float(input("Please enter the period(in years) that you will be investing for: ")))
    
    #User to select 'Simple interest' or 'Compound interest'.
    interest1 = input("Please select which interest you would like to use: (simple or compound)").capitalize()
    if interest1 == "Simple":
        interest2 = (float(amount)*(1+((interest_rate/100)*period)))
        interest = round(interest2,2)
        print("")
        print("The investment of R{} over {} years = R{} at an interest rate of {}%" .format(amount,period,interest,interest_rate))

    elif interest1 == "Compound":
        x = (1+(interest_rate/100))
        y = x**period
        interest2 = (float(amount)*y)
        interest = round(interest2,2)
        print("")
        print("The investment of R{} over {} years = R{} at an interest rate of {}%" .format(amount,period,interest,interest_rate))


#Calculation if 'Bond' was selected.          
elif interest == "Bond":
    print("Bond selected \n")
    amount = (float(input("Please enter the present value of the house (E.g. 100000): ")))
    interest_rate = (float(input("Please enter the Interest rate (only insert the number): ")))
    period = (float(input("Please enter the number of months you plan to repay the bond (E.g. 120): ")))
    sum1 = ((interest_rate/100)/12)
    sum2 = (1 + sum1)
    sum3 = sum2**period
    sum4 = sum1*sum3
    sum5 = float(amount*sum4) 
    sum6 = sum3-1
    sum7 = sum5/sum6
    sum8 = (round(sum7,2))
    print("\n")
    print("The monthly repayment on a bond of R {} over {} months = R {} at an interest rate of {}%" .format(amount,period,sum8,interest_rate))

#If the user doesn’t type in a valid input, an appropriate error message will appear.
else:
    print("Oops, something went wrong! please try again.")
