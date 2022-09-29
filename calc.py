def sum_nums(x,y=0):
   if type(x) not in [int, float] and type(y) not in [int, float]:
       raise TypeError("x and y should be a number")
   return x + y