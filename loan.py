#string formatting

loan = float(input("Enter the loan amount: "))
years = int(input("Enter the number of years: "))

month = years * 12
principal = loan / month
rem_bal = loan
print("|Month \t\t| Payment \t\t| Interest \t\t| Principal \t\t| Remaining Balance\t|")
for x in range(1, month + 1):
    rem_bal -= principal
    loan_interest = rem_bal * 0.00256
    month_payment = loan_interest + principal 
    print(f"|{x}\t\t|{round(month_payment, 2)}\t\t\t|\t\t{round(loan_interest, 2)}\t|\t\t{round(principal, 2)}\t|\t\t{round(rem_bal, 2)}\t|")