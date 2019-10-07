class friends:
    def __init__(self, namn, postNum, postOrt, address):
        self.namn = namn
        self.postNum = postNum
        self.postOrt = postOrt
        self.address = address

    def allInfo(self):
        return '{} {} {} {}'.format(self.namn, self.postNum, self.postOrt, self.address)


friend1 = friends('Dan', 'Hejhe', '2121', 'Hejgatan')

print(friend1.allInfo())

