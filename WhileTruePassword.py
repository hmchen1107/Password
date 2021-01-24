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





