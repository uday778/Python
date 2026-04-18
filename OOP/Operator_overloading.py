# a=5
# b=6
# # c=a+b
# c= int.__add__(a,b)
# print(c)


class Account:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance

    def __str__(self):
        return f"Account name: {self.name}  balance is {self.balance}"
    def __add__(self,other):
        return Account("Combined",self.balance + other.balance)
    def __gt__(self, other):
        return self.balance > other.balance

user1= Account("Navin",1000)
user2= Account("Ravi",2000)
user3= Account("Uday",5000)

combined= user1 + user2

print(user1)
print(user2)
print(user3)
print(combined)

if user1 > user2:
    print("User1 has more balance")
else:    print("User2 has more balance")