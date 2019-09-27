tal = []

amount = int(input("Hur många tal: "))

for i in range(amount):
    tal.append(int(input("Lägg till et tall: ")))

print(max(tal))