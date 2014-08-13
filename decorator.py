def outside():
    x = 5
    def printHam():
        print x
    return printHam

myFunc = outside()
print myFunc
myFunc()

