'''
Jag bjöd dig in på nytt efersom jag skapade en ny repo, filen ligger i /projects.
https://github.com/Systemad/OOP-Python/invitations
'''
accountList = []

class account:
    name = ""
    balance = 0

def createAccount():
        print("---Skapa nytt konto---\n")
        print("Du har valt att skapa ett konto: \n")
        newAccount = account()
        newAccount.name = input("Konto namn: ")
        if newAccount.name in accountList:
            choice = input("Kontot finns redan, vill du logga in? (j/N) ")
            if choice == 'j':
                loginAccount()
            else:
                createAccount()
        else:
            print("Kontot skapat, vängligen logga in\n")
            accountList.append(newAccount.name)


def loginAccount():
        print("---Logga in---")
        print("Du har valt att logga in:")
        accountNumber = input("Ange Konto namn: ")
        if accountNumber not in accountList:
            choice = input("Konton finns inte, vill du skapa ett (j/N) ")
            if choice == 'j':
                createAccount()
            else:
                print("Försök igen")
                loginAccount()
        else:
            print("Loggar in...")
            manageAccount()



def cashIn():
    amount = int(input("Hur mycket vill du sätta in: "))
    account.balance+=amount
    print("Ditt saldo är nu: " , account.balance , "SEK") 
    return account.balance

def cashOut():
    amount = int(input("Hur mycket vill du ta ut: "))
    account.balance-=amount
    print("Ditt saldo är nu: " , account.balance , "SEK") 
    return account.balance

def showCash():
    print("Ditt saldo är: " , account.balance , "SEK") 

def manageAccount(): 
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
            mainMenu()
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
            exit()
            break
        else:
            print("Felaktig inmatning, försök igen")
            mainMenu()

mainMenu()
