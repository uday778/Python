from functools import reduce



# filter(function,iterator)
nums=[1,2,3,4,5,6,7,8,9,0]
evens= list(filter(lambda x:x%2==0,nums))
print(evens)



# map(function,iterator)
# def doubleIt(n):
#     return n*2
doubles=tuple(map(lambda n:n*2,evens))
print(doubles)


# Reduce
sumOfDoubles=reduce(lambda x,y:x+y,doubles)
print(sumOfDoubles)