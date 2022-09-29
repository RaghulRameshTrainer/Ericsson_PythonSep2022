from oops import Employee

class Manager():
    def __init__(self,fn,ln,sl):
        self.fname=fn
        self.lname=ln
        self.salary=sl

    def appraisal(self):
        self.salary = int(self.salary*2)
        return self.salary

class Developer(Employee,Manager):
    def __init__(self,fname,lname,pay,tech):
        self.tech=tech
        super().__init__(fname,lname,pay)

    # def fullname(self,title):
    #     return "{}.{} {}".format(title,self.fname,self.lname)
    #
    # def fullname(self,title,initial):
    #     return "{} {}.{}{}".format(title,initial,self.fname,self.lname)
    def fullname(self,*args):
        if len(args) == 2:
            return "{} {}.{}{}".format(args[0], args[1], self.fname, self.lname)
        return "{}.{} {}".format(args[0], self.fname, self.lname)

    def appraisal(self):
        #return Manager.appraisal(self)
        #return super(Employee,self).appraisal()
        return super().appraisal()

dev_1=Developer('Ram','Sankar',10000,'Java')
dev_2=Developer('Venkatesh','Babu',20000,'Python')

# print(dev_1.fullname('Mr'))
# print(dev_2.fullname('Mr'))

print(dev_1.salary)
dev_1.appraisal()
print(dev_1.salary)

print(dev_2.salary)
dev_2.appraisal()
print(dev_2.salary)
