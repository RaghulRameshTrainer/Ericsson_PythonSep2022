class Employee():
    hike=1.15
    def __init__(self,fname,lname,pay):
        self.fname=fname
        self.lname=lname
        self.salary=pay
        self.email=self.fname+'.'+self.lname+'@ericsson.com'

    def fullname(self):
        return "{} {}".format(self.fname,self.lname)

    def appraisal(self):
        self.salary=int(self.salary*self.hike)
        return self.salary

    @classmethod
    def create_object(cls,emp_info):
        fn,ln,sal=emp_info.split("-")
        return cls(fn,ln,int(sal))     #Employee('Malini','Sekar',100000)

    @staticmethod
    def is_workingday(dt):
        if dt.weekday()==5 or dt.weekday()==6:
            return "Holiday!"
        return "Working Day"

    def __add__(self,other):
        return self.salary+other.salary

    def __len__(self):      #DUNDER method
        return len(self.fullname())
    
    def __mul__(self, other):
        return self.salary*other.salary

    
str1='Malini-Sekar-100000'
str2="Tharani-Siva-200000"

emp_1=Employee.create_object(str1)   #Employee('Malini','Sekar',100000)
emp_2=Employee.create_object(str2)   #Employee('Tharani','Siva',200000)

#print(emp_1+emp_2)
# print(len(emp_2))
print(emp_1*emp_2)
# import datetime
# tday=datetime.date(2022,9,25)
# print(Employee.is_workingday(tday))
# fn,ln,sl=str1.split("-")
# emp_1=Employee(fn,ln,int(sl))
#
# fn,ln,sl=str2.split("-")
# emp_2=Employee(fn,ln,int(sl))

# print(emp_1.email)
# print(emp_2.email)
#
# emp_1=Employee('Raghul','Ramesh',50000)
# emp_2=Employee('Levin','Lenus',60000)

# emp_1.hike=1.2
# print(emp_1.salary)
# emp_1.appraisal()
# print(emp_1.salary)
# print("="*15)
# print(emp_2.salary)
# emp_2.appraisal()
# print(emp_2.salary)






# print(emp_1.email)
# print(emp_2.email)

# print(emp_1.fullname())
# print(emp_2.fullname())

#OOPS

# Abstract      5%
# Inheritance   90%
# Polymorphism
# Encapsulation

