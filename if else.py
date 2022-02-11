#program to calculate bonus
salary=float(input("Enter salary:"))
time=int(input("Enter years of service:"))
if time>10:
  bonus=salary*10/100
  print("Net bonus is",bonus)
if time>=6 and time<=10:
  bonus=salary*8/100
  print("Net bonus is",bonus)
else:
  bonus=salary*5/100
  print("Net bonus is",bonus)