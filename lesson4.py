class pet:
    number_of_legs = 0
    def sleep(self):
        print "ZZZ"
    def count_legs(self):
        print ("I have %s legs" %self.number_of_legs)
    def set_legs(self,N):
        self.number_of_legs = N

class dog(pet):
	def bark(self):
		print "woof"
		


    

doug = pet() #instance of a cllass
doug.sleep()
doug.set_legs(5)
doug.count_legs()

doug = dog()
doug.bark()
doug.count_legs()
#doug.number_of_legs = 4


#print ("doug has %s legs" %doug.number_of_legs) 


