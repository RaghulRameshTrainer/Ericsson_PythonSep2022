from bank import Account

acc=Account('Raghul Ramesh',38,'M','ALNPR7676R',5000)
print("USERID:", acc.userid)
print("PASSWORD:",acc.password)

print("Current Balance:",acc.getBalance())
acc.setBalance(10000000)
print("New Balance:",acc.getBalance())
