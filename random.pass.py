import random
numbers="0123456789"
specialcharacters="!@#$%^&*()"
characters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

#input password length based on the user choice
n=int(input("enter number of numbers"))
s=int(input("enter number of special charaters"))
c=int(input("enter number of characters"))

password=" "
for i in range(n):
    password +=random.choice(numbers)

for j in range(s):
    password +=random.choice(specialcharacters)

for k in range(c):
    password +=random.choice(characters)

import string
a=['0','1','2','3','4','5','6','7','8','9']
b=['!','@','#','$','%','^','&','*','(',')''_']
c=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
d=['A','B','C','D','E','F','G','H','L','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
Mylist=[a,b,c,d]
password=""
pwd_size=int(input("enter size"))
for i in range(pwd_size):
     rand_array = random.choice(Mylist)
     password+=random.choice(rand_array)
print(password)
