import os

filePath = r"C:\Users\Dan\Documents\A CODE\OOP-python\files\accounts.txt";
if os.path.exists(filePath):
    os.remove(filePath)

with open("accounts.txt", "w") as accoountFiles:
    username = input("Username: ")
    password = input("Choose a password: ")
        
    accoountFiles.write(username+":"+password)
    accoountFiles.write("\n")

accoountFiles.close() 

while True:
    login1 = input("Login: ")
    login2 = input("Password: ")
    with open("accounts.txt", "r") as accoountFiles:
        if login1+":"+login2 == username+":"+password:
            print("Welcome")
            accoountFiles.close()
            break
        else:
            print("Incorrect username or password.")
