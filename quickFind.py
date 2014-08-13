class QuickFind:
	
	#constructor to initialize the array
	id = []
	def __init__(self,N):
		for i in range(N):
			self.id.append(i)
			#print (self.id[i])
	#this method verifies whether p and q already connected or not
	def connected(self,p,q):
		if(self.id[p]==self.id[q]):
			return 0
		else :
			return 1	
	#this method connects two compontent p and q by copying the value of q to p
	def union(self,p,q):
		pid = self.id[p]
		qid = self.id[q]
		for i in range (len(self.id)):
			if (self.id[i] == pid):
				self.id[i] = qid
	# this would 			
	def print_graph(self):
		for i in range(len(self.id)):
			print("Node " + str(i)+":" + str(self.id[i]))
					
try:
	with open("tinyUF.txt") as f:
		N = int(f.readline())
		objQF = QuickFind(N)
		for eachline in f:
			(p,q) =  eachline.split()
			if (objQF.connected(int(p),int(q))):
				objQF.union(int(p),int(q))
				#print(p+ " "+ q)
		print ("printing the graph")
		objQF.print_graph()
except IOError as ioerr:
	print (str(ioerr))

					
