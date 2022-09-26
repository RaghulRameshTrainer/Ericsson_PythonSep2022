#while loop
'''
x=0

while x<=10:
    print(x)
    x=x+1
print("The value of x: {} , Hence came out of the loop".format(x))

x=0
while x<=100:
    print(x)
    x=x+5


city=['Chennai','Bangalore',200,'Pune','Gurgoan']

for x in city:
    print(x)

# Break and Continue

x=0

while x<=10:
    print(x)
    if x==5:
        break
    x=x+1

print("I am out of the loop in the program")
'''

x=0

while x<=10:
    x=x+1
    if x==5:
        continue
    print(x)   #1,2,3,4,6,7,8,9,10,11