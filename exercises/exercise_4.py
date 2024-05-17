# Exercise 4
# Your solution comes here
num = str(input("enter a number no more than 4 digits: "))
if int(num) < 1000:
    num = "0" + num
elif int(num) < 100:
    num = "00" + num
elif int(num) < 10:
    num = "000" + num
else:
    pass
if num[0:2] == num[-1:-3:-1]:
    print("1")
else:
    print("0")
