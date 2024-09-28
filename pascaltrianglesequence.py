def fact(n):
    if n<=1:
        return n
    return n*fact(n-1)
# fact(5)
def cnr(r,c):
    r-=1
    c-=1
    num = fact(r)
    den = fact(c)*fact(r-c)
#     print(den)
    if den==0:return 1
    return num//den
# print(cnr(1,1))

n=7
for i in range(1,n):
    print((n-i)*" ",end="")
    for j in range(1,i+1):
        print(cnr(i,j),end=" ")
    print()



# ------------------------
def ncr(n,r):
    n-=1
    r-=1
    res = 1
    for i in range(r):
        res*=(n-i)
        res//=(i+1)
    return res
ncr(6,1)




# ---------------

r = 3
n=1
for i in range(1,r+1):
    print(n,end=" ")
    n = n*(r-i)
    n = n//i
