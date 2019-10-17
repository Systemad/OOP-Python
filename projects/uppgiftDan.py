accountList = []

class account:
    name = ""
    balance = 0

def createAccount():
    print("---Create new account---\n")
    print("You have chosen to create an account: \n")
    newAccount = account()
    newAccount.name = input("Name:")
    print("Account created!\n")
    return newAccount

def logIn():
    print("---Log in---")
    n = 1
    for accounts in accountList:
        print(f"{n} : {accounts.name}")
        n = n + 1
    acc = int(input("Choose account: "))
    return accountList[acc-1]

def manageAccount(account):
    while True:
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Show balance")
        print("4. Exit")
        selection = input("Choose option: ")
        if selection == "1":
            amount = int(input("How much to deposit: "))
            account.balance+=amount
            print("Your balance is now: " , account.balance , "SEK")

        elif selection == "2":
            amount = int(input("How much to withdraw: "))
            if amount > account.balance:
                print("You can't withdraw more than you have on your account!\n")
            else:
                account.balance-=amount
                print("Your balance is now: " , account.balance , "SEK\n")

        elif selection == "3":
            print("Your balance is: " , account.balance , "SEK\n")
            
        elif selection == "4":
            break

while True:
    print("1. New Account")
    print("2. Log in")
    print("3. Exit\n")
    option = input("Choose option: ")
    if option == "1":
        accountList.append(createAccount())
    elif option == "2":
        updateAccount = logIn()
        manageAccount(updateAccount)
    elif option == "3":
        break
