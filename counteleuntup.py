t=[10,20,30,40,50,(60,61,61,66),70,80]
count=0
for i in t:
    if isinstance(i,tuple):
        break
    count+=1
print(count)
