def leap():
    start = int(input("Mata in start år: "))
    end = int(input("Mata in slut år: "))

    for i in range(start, end):
#        print(i)
        if i % 4 == 0:
            print(i + 'Skottår')



leap()        