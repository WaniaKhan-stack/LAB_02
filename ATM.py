
def Withdraw(balance , money):


    if (money > balance or money <= 0):
        print("Insufficient Balance")
    else :
        balance = balance - money
        print("You have withdrawn : ", money)
        print ("Your remaining balance is : ", balance)
    return balance

def CheckBalance(balance) :
    print ("Your account balance is : ", balance)

def Deposit(balance, money) :
    if ( money <= 0):
        print("Invalid Amount")
    else:
        balance = balance + money
        print("You have deposited : ", money)
        print ("Your updated balance is : ", balance)
    return balance



print ("Welcome to the ATM Machine")

MyAccount = 50000

print ("ATM Menu")
print ("1. Withdraw")
print ("2. Check Balance")
print ("3. Deposit")
print ("4. Exit")

choice = 0 

while (choice != 4):
    choice = int(input("Enter your choice : "))
    

    if (choice == 1):
        money = int(input("Enter the amount :"))
        MyAccount = Withdraw(MyAccount, money)
    elif (choice == 2):
        
        CheckBalance(MyAccount)
    elif (choice == 3):
        money = int(input("Enter the amount :"))
        MyAccount = Deposit(MyAccount, money)
    elif (choice == 4):
        print ("Thank you for using the ATM Machine")



