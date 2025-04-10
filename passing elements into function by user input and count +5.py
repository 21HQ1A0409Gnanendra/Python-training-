def name(lst):
    lst2=[]
    count =0
    for i in lst:
        if len(i)>=5:
           lst2.append(i)
           count = count+1
        else:
           continue

    return lst2,count


lst=[]
for i in range (0,10):
    x=(input("Enter a name "))
    lst.append(x)
print(lst)

lst2,count=name(lst)
print ("Name greater than 5 letter or equals  ",lst2)
print ("Total number of person  ",count)
