def square(num):
    return num*num
def cube(num):
    return num*num*num
def operate(num,operation):
    return operation(num) #square(num)



value=5
result=operate(value,square)
print(result)