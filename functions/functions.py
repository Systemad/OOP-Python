'''
def percentage(decimal):
    if tal > 1.0 or tal < 0.0:
        raise ValueError("felaktigt tal")
    return decimal * 100


while True:
    tal = float(input("iput deminal between 0-1.0"))
'''    


def addString(s1,s2, addSpace = False):
    if addSpace:
        return s1 + "" + s2
    return s1+s2


print (addString("Dan", "Hej", True))
print (addString("Dan", "Hej"))