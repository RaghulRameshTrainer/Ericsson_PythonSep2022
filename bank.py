class Account():
    def __init__(self,name,age,gender,pancard,amount):
        self.name=name
        self.age=age
        self.gender=gender
        self.pan=pancard
        self._balance=amount
        self.userid=name.replace(' ','_')+'@123'
        self.password=self.pan[:4]+self.name[-4:]

    def getBalance(self):
        return self._balance
    def setBalance(self,depoit_amount):
        self._balance=self._balance+depoit_amount
        return self._balance