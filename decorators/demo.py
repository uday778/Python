
def greater_first(func):
    def wrap(a,b):
        if a<b:
            a,b=b,a
            return func(a,b)
    return wrap


@greater_first
def subtract(a,b):
    return a-b


@greater_first
def divide(a,b):
    if a<b:
        a,b=b,a
    return a/b

sub=greater_first(subtract)
divi=greater_first(divide)

result=divide(2,4)
print(result)

result2=subtract(2,4)
print(result2)



def my_decorator(func):
    def wrapper():
        print("Something before the function.")
        func()
        print("Something after the function.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

# say_hello()
hi=my_decorator(say_hello)

