accountList = []

class account:
    name = ""
    balance = 0

def createAccount():
    print("---Skapa nytt konto---\n")
    print("Du har valt att skapa ett konto: \n")
    newAccount = account()
    newAccount = input("Ange konto namn-> ")
    if account.name in accountList:
        print("Kontot finns redan") 
    else:
        print("Kontot skapat")
        accountList.append(newAccount)

def loginAccount():
    print("---Logga in---")
    account.name = input("Ange konto namn-> ")
    if account.name in accountList:
        manageAccount(account)
    else:
        print("Kontot finns inte, skapa ett först")

def cashIn():
    amount = int(input("Hur mycket vill du sätta in-> "))
    account.balance+=amount
    print("Ditt saldo är nu: " , account.balance , "SEK") 

def cashOut():
    amount = int(input("Hur mycket vill du ta ut-> "))
    if amount > account.balance:
        print("Du kan inte ta ut mer än vad du har på kontot!")
    else:
        account.balance-=amount
        print("Ditt saldo är nu: " , account.balance , "SEK")

def showCash():
    print("Ditt saldo är: " , account.balance , "SEK")

def manageAccount(account): 
    while True:
        print("---Hantera Konto---\n") 
        print("1. Lägg till saldo")
        print("2. Ta ut saldo")
        print("3. Visa saldo")  
        print("4. Avsluta")  
        select = input("Välj ett alternativ: ")
        if select == '1':
            cashIn()
        elif select == '2':
            cashOut()
        elif select == '3':
            showCash()
        elif select == '4':
            break
        else:
            print("Fel inmatning, försök igen: ")

def mainMenu():
    while True:
        print("---Huvudmeny---\n")
        print("1. Skapa Konto")
        print("2. Logga in")
        print("3. Avsluta\n")
        select = input("Välj ett alternativ: ")
        if select == '1':
            createAccount()
        elif select == '2':
            loginAccount()
        elif select == '3':
            break

mainMenu()