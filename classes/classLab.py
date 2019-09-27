class person:
    def __init__(self, age, name, address, postnum):
        self.age = age
        self.name = name
        self.address = address
        self.postnum = postnum

    def whatName(self):
        self.name = input("Vad heter du: ")
        self.age = input("Hur gammal är du: ")

    def printAll(self):
        print(self.age)