from numpy import*
arr1=array([2,5,4,7,6])
arr2=arr1.copy()
arr1[2]=9
print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))
