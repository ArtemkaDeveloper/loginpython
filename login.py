login1 = "github"
pass1 = "000"
login2 = "github1"
pass2 = "111"
login = input("login: ")
password = input("password: ")
if login == "github" and password == "000":
    print("hi, github")
    input("Press Enter for exit...")
elif login == "github1" and password == "111":
    print("hi, github1")
    input("Press Enter for exit...")
else:
    print("wrong login or password")
    input("Press Enter for exit...")


