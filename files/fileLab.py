import os
import os.path
#Print text in odd lines
'''
with open("hej.txt", "r") as file:
    i = 0
    for line in file:
        if i % 2 == 1: #Checks if odd line
            print(line)
        i += 1

### Should read files from the list (filenames) and write odd numbers in a new file
filenames = ['hej.txt', 'hej2.txt']

for filename in filenames:
    with open(filename, 'r') as input_file:

        with open('output_%s' % filename, 'w') as output_file:
            i = 0
            for line in filenames:
                if i & 2 == 1: 
                    print(line)
                i += 1


#with open('hej.txt', 'r') as file1, open('hej2.txt', 'r') as file2:
#with open(files, "r") as file:
#    i = 0
#        for line in file:
#        if i & 2 == 1: 
#            print(line)
#        i += 1
'''
## add line number in start of each line to output.txt
with open('hej.txt', 'r') as program:
    data = program.readlines()

with open('output.txt', 'w') as program:
    for (number, line) in enumerate(data):
        program.write('%d  %s' % (number + 1, line))