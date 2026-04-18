from abc import  ABC,abstractmethod

class PaymentGateway(ABC):
    @abstractmethod
    def pay(self):
        pass

class Razorpay(PaymentGateway):
    def pay(self):
        print("Pay using Razorpay")

class Purchase:

    def __init__(self,gateway):
        self.gateway=gateway
    
    def checkout(self):
        print("checking out")
        self.gateway.pay()


gateway1=Razorpay()
purchase=Purchase(gateway1)

purchase.checkout()





