for a in range (1,6):
    for b in range(a): 
        print("*" , end= "" )
    print()
print()

for g in range (6,0,-1):
    for h in range(g):
        print("*", end="")
    print()
    
print()
c= 6
for d in range(c):
    for e in range(1,c-d):
        print(" " , end="")
    for f in range (0,d+1):
        print("*" , end="")
    print()
print()

i= 6
for j in range(i):
    for k in range(j):
        print(" " , end="")
    for l in range (i,j,-1):
        print("*" , end="")
    print()
print()

m=6
for n in range(1,m+1):
    for o in range(m-n):
        print(" " , end="")
    for p in range (2*n-1):
        print("*", end="")
    print()

q=5
for r in range(1,q+1):
    for s in range(r-1):
        print(" ", end= "")
    for s in range(2*(q-r)+1):
        print("*", end="")
    print()


u = 5

for v in range(1, u+1):
    # printing spaces
    for x in range(v-1):
        print(' ', end='')
    # printing stars
    for x in range(2*(u-v)+1):
        print('*', end='')
    print()
