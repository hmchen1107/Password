#Pls input your name ultimately
#When name is q, the system break

# By myself
p = 1
n = 2
while p < 4 and n >= 0:
    pwd = input('Please input your password : ')
    if pwd != 'a123456':
        print('Wrong passwrod ! You still have', str(n) , "chance")
    else:
        print("Login successfully")
        break
    p=p+1
    n=n-1


# By teacher
password = "a123456"
i = 3
while True:
    pwd = input('Please input your passwrod : ')
    if pwd == password:
        print("Login succesfully")
        break
    else:
        i=i-1
        print("Wrong password! You still have", i, "chance")


# By teacher
password = "a123456"
i = 3
while i>0:
    i=i-1
    pwd = input('Please input your passwrod : ')
    if pwd == password:
        print("Login succesfully")
        break
    else:
        print("Wrong password")
        if i>0:
        print("You still have", i, "chance")




