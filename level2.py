from string import maketrans   # Required to call maketrans function.

input = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
input2 = "map.html"
#output=input.replace("K","M")
#output=input.replace("O","Q")
#output=input.replace("E","G")
#output=input.replace("m","k")
#output=input.replace("q","o")
#output=input.replace("g","e")




intab = "abcdefghijklmnopqrstuvwxyz"
outtab = "cdefghijklmnopqrstuvwxyzab"
trantab = maketrans(intab, outtab)

print input.translate(trantab)
print input2.translate(trantab)
print "jvon".translate(trantab)



#print (input)
#print (output)
