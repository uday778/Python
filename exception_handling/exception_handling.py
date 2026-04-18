


from unittest import result


a=5
b=0
try:
    result=a/b

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

print(result)

