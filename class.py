class pet:
    number_of_legs = 0

    def sleep(self):
        print "zzz"
    

    def count_legs(self):
        print "I have {} legs:".format(self.number_of_legs)

class fish(pet):
    def swim(self):
        print "swimming"

'''
    main function
'''

dog = pet()
dog.number_of_legs = 5
dog.sleep()
dog.count_legs()
cat = pet()
cat.number_of_legs = 3
animals = [dog, cat]
for item in animals:
    print item.count_legs()


nemo = fish()
nemo.swim()
nemo.sleep()
nemo.number_of_legs = 4
nemo.count_legs()
