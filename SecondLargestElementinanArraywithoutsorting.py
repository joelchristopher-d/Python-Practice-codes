def sec_SmallLarge(arr,n):
    if n<2:return -1
    small = ssmall = float('inf')
    large = slarge = float('-inf')
    for i in arr:
        if i<small:
            ssmall = small
            small = i
        elif i<ssmall and i!=small:
            ssmall = i
            
        if i>large:
            slarge = large
            large = i
        elif i>slarge and i!=large:
            slarge = i
    return [slarge,ssmall]


arr = [10,9,8,7,6,5,4,3,2,1,12]
sec_SmallLarge(arr,len(arr))
