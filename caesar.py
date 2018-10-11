cipher   = raw_input("enter cipher text: ")
alpha    = 'abcdefghijklmnopqrstuvwxyz'
cList    = [b for b in cipher]
aList    = [d for d in alpha]
plain    = ''

for j in range(0,26):
   for c in cList:
      if c in aList:
         index    = aList.index(c)
         pIndex   = (index - j) % 26
         plain    += aList[pIndex]
      else:
         plain    += c
   print "plain [ " + str(j) +" shifted ] : " + plain + "\r\n"
   plain = ''
