def addOne(myFunc):
    def addOneInside(*args,**kwargs):
        return myFunc(*args,**kwargs) + 1
    return addOneInside

@addOne
def oldFunc(x = 3245):
    return x


#oldFunc =  addOne(oldFunc)

print oldFunc(34)
