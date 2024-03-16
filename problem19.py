


# Hackerrank assesment










def minTime(l,d,o):
    temp=0
    for i in range(o):
        for j in range(len(l)):
            if l[j]%d==0:
                l[j]//=d
                break
    return sum(l)



minTime([3,2,5,5],5,2)