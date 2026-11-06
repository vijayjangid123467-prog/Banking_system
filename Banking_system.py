print("Welcome to Banking system")

balance=float(input("Enter bank balance:"))

print("(1).Check bank balance")
print("(2).Deposite amount")
print("(3).Withdraw amount")
print("(4).Exit")

for a in range(1,5):
    a=int(input("Enter your choice in number:"))
    if a==1:
        print("Balance=",balance)
    elif a==2:
        i=float(input("Enter amount to deposite:"))
        balance +=i
        print("Total amount after deposite:",balance)
    elif a==3:
        i=float(input("Enter amount to withdraw:"))
        if i<=balance:
            balance-=i
            print("Total amount after withdraw:",balance)
        else:
            print("Not enough balance")
    else:
        print("Thank you")
        break