import sys
try:
    with open('days.txt','r') as fo:
        print(fo.read())
    res=100/2
    print("Result:",res)
    s=10+20
    #print(nums[-1])
    age=int(input("Please enter your age:"))
    if age < 0 or age >100:
        raise ValueError("Age should be between 0-100")
    print("Age by next year :", age+1)
except FileNotFoundError as e:
    #print("Received an error:",e)
    print("Since the file daysssssss.txt does not exists. Shown below the content from default file:")
    with open("days.txt","w+") as fo:
        fo.writelines(["Python\n","Spark"])
        fo.seek(0,0)
        print(fo.read())
except ZeroDivisionError as e:
    #print("Error:",e)
    res=100/1
    print("Result from EXCEPTION:",res)
except TypeError as e:
    print('Type Error Received.',e)
except ValueError as e:
    print("AGE ISSUE:",e)
except Exception as e:
    print("NEW ERROR:", e)
    #sys.exit(1)
print("Post file operation, started the reports generation")