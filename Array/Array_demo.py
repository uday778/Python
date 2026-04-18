from array import *
arr1=array('i',[1,2,3,4,5])
arr2=array('d',[1.5,2.5,3.5,4.5,5.5])
# for n in arr1:
#     print(n)
# print(arr1.buffer_info())

# print(type(arr1))
# print(arr1.tolist())


arr1.append(6)
arr1.buffer_info()
print(arr1.buffer_info())
print(arr1.reverse())
print(arr1.count(1))
print(arr1.index(3))
print(arr1)
print(arr1.pop())
print(arr1)

print(arr1.insert(2,10))
print(arr1)
