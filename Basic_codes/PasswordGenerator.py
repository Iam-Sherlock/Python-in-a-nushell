import random
lst=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
num=['1','2','3','4','5','6','7','8','9','0']
spl=['!','@','$','%','&','(',')','^']
emp=[]
for i in range(6):
    emp.append(random.choice(lst))
for i in range(2):
    emp.append(random.choice(num))
for i in range(1):
    emp.append(random.choice(spl))
for i in range(1):
    emp.append(random.choice(lst).capitalize())


#print(emp)
random.shuffle(emp)
#print(emp)
str1="".join(emp)
print(str1)

'''password=str1
if (len(password)>=8) and any(p.isdigit() for p in password) and any(p.isalpha() for p in password) and any(p.isupper() for p in password):
    print("This is a strongest password")
else:
    print("Not a strongest password")
'''