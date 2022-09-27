import csv

# with open(r"C:\Users\RaghulRamesh\Downloads\events.csv.csv","r") as fo:
#     data=csv.reader(fo)
#     for line in data:
#         print(line[0],line[-1])

with open('customer.csv','w',newline='') as csvfo:
    fo=csv.writer(csvfo)
    fo.writerow(["custid","custname","city","gender","age"])
    fo.writerow([1000,"Prakash","Hyderabad","M",40])
    fo.writerow([1001,"Aveek","Delhi","M",50])
    fo.writerow([1002,"Tharani","Chennai","F",35])