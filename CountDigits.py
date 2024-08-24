def countDigits(n: int) -> int:
    a=0
    temp=n
    while n:
        t=n%10
        n//=10
        if t!=0 and temp%t==0:        
            a+=1
    return a
