# Exercise 11
# Your solution comes here
s = int(input("enter the amt of money: "))
d500 = s // 500
d100 = (s % 500) // 100
d10 = (s % 100) // 10
d5 = (s % 10) // 5
d1 = (s % 2) // 1
print(d500, '(500)', d100, '(100)', d10, '(10)', d5, '(5)', d1, '(1)')
