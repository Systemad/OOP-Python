## Only print odd numbers 
'''
tal = [3, 2, 8, 9, 7, 2]

odd = [num for num in tal if num % 2 == 1] 

print(odd)
'''
productList = []

class kop:
    product = ""
    price = 0
    productNumber = ""

amount = int(input("Hur många varor: "))

for i in range(amount):
    prod = input("vilken product? ")
    pric = int(input("Vad kostar det? "))
    productNum = int(input("Product nummer? "))

#kop.product = prod
#kop.price = pric
#kop.productNumber = productNum

productList.append(prod)
productList.append(pric)
productList.append(productNum)

print(productList)
#("Din product är: " , kop.product) #
#
#print("Din product kostar: " , kop.price)
#print("Produkt nummer är: " , kop.productNumber)
