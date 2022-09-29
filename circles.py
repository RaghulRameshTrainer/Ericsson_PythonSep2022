from math import pi

def circle_area(r):
    if r < 0:
        raise ValueError("Radius should be a positive number , greater than zero")
    if type(r) not in [int,float]:
        raise TypeError("Radius should be a number")
    return pi*r**2

# radius=[5,0,-3,2+6j,True,"chennai"]
#
# for r in radius:
#     print(f"radius:{r} , area:{circle_area(r)}")