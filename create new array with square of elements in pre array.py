from array import*
k=array('i',[5,6,8,2,7])
newArr=array(k.typecode,(a*a for a in k))
for e in newArr:
    print(e)
