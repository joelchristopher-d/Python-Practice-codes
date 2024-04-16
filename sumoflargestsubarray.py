nums = [-2,1,-3,4,-1,2,1,-5,4]
# nums=[1]
nums = [5,4,-1,7,8]
target=23
low=0
high=len(nums)-1
while(True):
    if low>high:
        low+=1
        high=len(nums)-1
    else:
        a=[nums[i] for i in range(low,high+1)]
#         print(a)
        if sum(a)==target:
            print(a)
            break
    high-=1
