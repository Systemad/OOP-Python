password = input("Mata in ett lösenord: ")

def isValidPassword(password):

    nejOrd=['hej', 'lösen', 'hopp']
    specialTecken =['@', '$', '%', '#'] 

    val = True

    if len(password) <= 8:
        print("Lösenordet måste vara minst 8 tekken") 
        val = False

    if not any(char.isupper() for char in password): 
        print("Lösen ordet måste innehålla minst 2 stora boksäver") 
        val = False
          
    if not any(char.islower() for char in password): 
        print('Lösen ordet måste innehålla minst 2 små boksäver') 
        val = False

    if any(char in nejOrd for char in password): 
        print(f"DU får inte använda orden: {nejOrd}")
        val = False

    if not any(char in specialTecken for char in password): 
        print('Password should have at least one of the symbols $@#') 
        val = False
    if val:
        return val


if (isValidPassword(password)):
    print("True")
else:
    print("False")

