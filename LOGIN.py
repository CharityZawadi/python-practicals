#program login
username=str(input("Enter username:"))
pwd=int(input("Enter password:"))
logins=["BSCIT-05-0212/20",123]
if username in logins and pwd in logins:
  print("login successful")
else:
  print("login not successful")