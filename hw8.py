import sys

f = open('example.txt')
a = f.readlines()
src = a[0].split(' ',1)
trg = a[1].split(' ',1)
f.close()
#print (a[0], a[1])
print(src[1].strip(),trg[1].strip())
