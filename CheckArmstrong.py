def checkArmstrong(n):
    #write your code here !!!!!!!!!
    a=countdigits(n)
    temp=0
    j=n
    while n:
        temp += (n%10)**a
        n//=10
    return temp==j

def countdigits(n):
    a=0
    while n:
        n//=10
        a+=1
    return a
