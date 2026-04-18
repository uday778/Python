import sys
from time import sleep

sys.setrecursionlimit(10)
# print(sys.getrecursionlimit())
# by default 1000


count=1

def greet():
    global count
    print("hello",count)
    count=count+1
    sleep(0.02)
    greet()


greet()