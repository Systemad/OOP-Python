import random
lista = []
lista.append(random.randint(0, 101))

def Rand(lista1): 
    for i in lista: 
        if i % 3 == 0:
            lista1.append(i) 
    
    average = sum(lista1) / len(lista1)
    return average 
  
print(Rand(lista))
