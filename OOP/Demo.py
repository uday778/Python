


class computer:

    brand="HP"
    def __init__(self,cpu,ram,hdd):
        print("This is a constructor")
        self.cpu=cpu
        self.ram=ram
        self.hdd=hdd
        
    def config(self):
        print("config is : ",self.cpu,self.ram,self.hdd)
    def show(self):
        print("This is a computer")

    @classmethod    
    def info(cls):
        return cls.brand
    
    @staticmethod
    def gb_to_bytes(gb):
        return gb*(1024 **3)



comp1= computer("i7","16GB","1TB")
comp1.config()
comp2= computer("i5","8GB","500GB")
comp2.config()

print(computer.info())
print(computer.gb_to_bytes(10))
print(comp1.info())








