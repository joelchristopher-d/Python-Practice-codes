def fun(num):
    
    total = 0

    for n in num:
        if n & 1 ==0:
            print(n)
            total+=n
    return total


if __name__=="__main__":
    num = [0,1,2,3,4]

    print(fun(num))