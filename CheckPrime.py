n=int(input())
def square(n):
    low=0
    high=n
    while(low<=high):
        mid=(low+high)//2
        if mid*mid==n:
            return mid
        if mid*mid > n:
            high = mid-1
        else:
            low = mid+1
    return high

vector=[]
for i in range(1,square(n)+1):
    if n%i==0:
        vector.append(i)
        if i!=n//i:
            vector.append(n//i)
print("YES" if len(vector)==2 else "NO")
