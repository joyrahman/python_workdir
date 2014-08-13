##################################
##	HW 8
##	author 	: Joy Rahman & Mark Apple By
##  version	: 1
##	Date	: 27 Mar 2014
## 	contact	: joyrahman@gmail.com
## 	Language: python
##	compatibility : Python 3 (will run in Python 2.7 with some minor issue with print function)
##	OS 		: Any OS with python binary (Cloud | Linux | macos | Windows )
## 	Platform: x86_64 (32bit or 64bit)
##  Source 	: main.py
## 	Input	: File (example.txt)
## 	Output	: stdout
## 	Running the program : python main.py
##################################
import sys


######### function to compute cost of substitution ######
def costWithSub(a,b):
    #do the comparision
	cost = 0
	for i in range(0,len(a)):
		if(a[i]!=b[i]):
			cost+=1
	return cost

######### function to reverse a string ########
def reverse(a):
	return a[::-1]


######### Main Function ########

#Start File Read
f = open('example.txt')					# input file located inside same directory
input       = f.readlines()
firstLine   = input[0].split(' ',1)
secondLine  = input[1].split(' ',1)
f.close()
# End of File Read

src     =  firstLine[1].strip()			# the source string
trg     =  secondLine[1].strip()		# the target string

N       = len(src)+1 					# No of items
minimalCost = [0]*N 					# array containing the cost 

for i in range(1,N):
	minimum = 100000					# vary large value to facilitate initial comparision
	for j in range(0,i):
		costWithFlip 	=  1 + costWithSub(src[j:i],reverse(trg[j:i])) + minimalCost[j]		#cost for flip & substitute
		costWithoutFlip	=	costWithSub(src[j:i],trg[j:i]) + minimalCost[j]					#cost for substitute only
		minimum = min(minimum,costWithFlip,costWithoutFlip)									#Find minimum between all the choices
	minimalCost[i] = minimum 																#store the result

print ("Minimum Number of Operations: ",minimalCost[len(src)])





