from abc import ABC , abstractmethod
class Car(ABC):
    @abstractmethod
    def breaks(self):
        pass
    @abstractmethod
    def wheel(self):
        pass
    @abstractmethod
    def mirror(self):
        pass
    @abstractmethod
    def engine(self):
        pass
    def price(self,model):
        if model=="EcoSport":
            print("Price:1600000")
        elif model=="Figo":
            print("Price:800000")
        elif model=="Aspire":
            print("Price:900000")
        else:
            print("Please check at showrooms")

class MyCar(Car):
    def __init__(self,make,model):
        self.make=make
        self.model=model
    def breaks(self):
        self.status="Applied"
    def wheel(self):
        self.count=6
    def mirror(self):
        self.mirror_status="Fitted"
    def engine(self):
        self.type="Powerstain"
    def info(self):
        print("EcoSport is 8 seater and with XUV model")

c1=MyCar("Ford","EcoSport")
c1.price("Fiesta")
c1.info()