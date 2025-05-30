import random
import sys




def uret(str):
    a=''
    b=0
    k = str[1]
    l = str[2]

    a = k.split('=')[1]
    b = l.split('=')[1]
    return a,b

x,y = uret(sys.argv)
print(x)
print(y)