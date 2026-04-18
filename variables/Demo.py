a=10
def something():
    a=15
    globals()['a'] = 22
    print("inside : ",a)

something()
print("outside : ",a)