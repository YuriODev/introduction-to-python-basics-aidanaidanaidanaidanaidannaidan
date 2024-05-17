# Exercise 3
# Your solution comes here
num = int(input("enter AN AMount of seconds"))
hours = str(num // 3600 % 24)
mins = str((num % 3600) // 60)
if int(mins) < 10:
    mins = "0" + str(mins)
else:
    pass
secs = str(num % 60)
if int(secs) < 10:
    secs = "0" + str(secs)
else:
    pass
print(hours + ":" + mins + ":" + secs)
