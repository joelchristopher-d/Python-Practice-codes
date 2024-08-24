def sumOfAllDivisors(n: int) -> int:
    vector = []
    for j in range(1,n+1):
        for i in range(1,square(j)+1):
            if j%i==0:
                vector.append(i)
                if i!=j//i:
                    vector.append(j//i)
    return sum(vector)


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
