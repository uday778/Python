# class A:
#     def f1(self):
#         print("F1 working")
#     def f2(self):
#         print("F2 working") 
#     def show(self):
#         print("in A show")         
# class B:
#     def show(self):
#         print("in B show")  
#     def f3(self):
#         print("F3 working")
#     def f4(self):
#         print("F4 working") 

# class C(A,B):
#     # def show(self):
#     #     print("in C show")  
#     def f5(self):
#         print("F5 working")

# obj1=C()
# # obj1.show()  new style 
# B.show(obj1)
# 
# 




class A:
    def __init__(self):
        print("in A init ")
    def f1(self):
        print("F1 working")

class B(A):
    def __init__(self):
        super().__init__()
        print("in B init ")

    def f2(self):
        
        print("F2 working")



obj1=B()
obj1.f1()





