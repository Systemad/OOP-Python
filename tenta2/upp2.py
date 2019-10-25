tal = int(input("Mata in ett tal tex 522: "))

def plussa(split):

    split = [int(x) for x in str(tal)] 
    return sum(split)

print(plussa(tal)) 