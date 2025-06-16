list = [1, 5, 3, 6, 2, 4] 
l= len(list) 
list.sort() 

if l % 2 == 0: 
    median1 = list[l//2] 
    median2 = list[l//2 - 1] 
    median = (median1 + median2)/2
else: 
    median = list[n//2] 
print("Median is: " + str(median))
