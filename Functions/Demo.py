import math 

print('hello world')
def add(a,b,c):
    return a+b+c

print(add(10,20,30))



num=25
res=math.sqrt(num)
print(res)
print(math.ceil(res))
print(math.floor(69.9))
print(math.pow(2,3))
print(math.pi)

def add(num1,num2=0): #default Arguments
    return num1+num2

def add(*args): #Variable length Arguments
    return sum(args)

def person(**kwargs):
    for key,value in kwargs.items():
        print(f'{key}: {value}')
   

print(add(10,20,30,40,50,60,70,80,90,100))

person(name='Alice',age=30,loc="pune",tech="python") 