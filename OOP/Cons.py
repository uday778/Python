class ABC:
    def __new__(cls):
        print("new init method constructor is called")
        return super(ABC,cls).__new__(cls)
    def __init__(self):
        print("constructor is called")
    def show(self):
        print("this is in show method")

obj1= ABC()
obj1.show()

obj2=ABC.__new__(ABC)
obj2.show()