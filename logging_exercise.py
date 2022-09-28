import logging

log_format="%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename="result.out",
    level=logging.DEBUG,
                    format=log_format)
log=logging.getLogger()
def addition(x,y):
    try:
        return x+y
    except Exception as e:
        log.error(f"""Error when performing addition of a number with string. 
                Addition of {x} and {y} caused an issue.Please check""")

def subraction(x,y):
    return x-y

def division(x,y):
    if y==0:
        log.warning("Cannot divide by ZERO")
        return None
    return x/y

def multiplication(x,y):
    return x*y

# a,b=10,20
# res=addition(a,b)
# log.info(f"Sum of {a} ,{b} is {res}")
# res=subraction(a,b)
# log.info(f"Difference of {a} ,{b} is {res}")
# res=division(a,b)
# log.info(f"Division of {a} ,{b} is {res}")
# res=multiplication(a,b)
# log.info(f"Product of {a} ,{b} is {res}")

# a,b=10,0
# res=division(a,b)
# log.info(f"Division of {a} ,{b} is {res}")

a=10
b="twenty"
res=addition(a,b)
log.info(f"Sum of {a} ,{b} is {res}")
# res=subraction(a,b)
# log.info(f"Difference of {a} ,{b} is {res}")
# res=division(a,b)
# log.info(f"Division of {a} ,{b} is {res}")
# res=multiplication(a,b)
# log.info(f"Product of {a} ,{b} is {res}")