# Given an array of integers and a positive integer k , determine the number of  pairs(i,j) where i<j and ar[i] + ar[j] is divisible by k.


# l = [1,2,3,4,5,6]
l=[1,3,2,6,1,2]
k = 3
l1=[]
low=-1
high=len(l)-1
for i in range(len(l)):
    low+=1
    high=len(l)-1
    while(low!=high):
        if((l[low]+l[high])%k==0):
            l1.append([l[low],l[high]])
        high-=1
print(l1)
print(len(l1))


# 2nd way            
l = [1,2,3,4,5,6]
# l = [1, 3, 2, 6, 1, 2]

k=5
p=0
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if((l[i]+l[j])%k==0):
            p+=1
print(p)


# chatgptcode!!!!!!!!!!!!!

# l = [1, 3, 2, 6, 1, 2]
# k = 3

# remainder_counts = {}
# total_pairs = 0

# for num in l:
#     remainder = num % k
#     complement = (k - remainder) % k
#     if complement in remainder_counts:
#         total_pairs += remainder_counts[complement]
#     remainder_counts[remainder] = remainder_counts.get(remainder, 0) + 1

# print(total_pairs)
