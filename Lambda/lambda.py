

# def fun(num):
#     return  num*num


fun=lambda num:num*num




result= fun(5)
print(result)



nums=[1,2,3,4,5,6,7,8,9]
evens=list(filter(lambda x:x%2==0,nums))
print(evens)


sums=  (lambda a,b:a+b)
print(sums(10,80))


print((lambda a,b:a+b)(11,22))