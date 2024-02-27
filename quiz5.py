#  Given an array of integers representing the color of each sock, 
# determine how many pairs of socks with matching colors there are.

ar=[10,10,20,20,20,20,90]
c=0
k=""
a=0
for i in sorted(ar):
    c=0
    for j in sorted(ar):
        if i==j:
            c+=1
#             ar.remove(j)
    if c>=2:
#         ar.remove(i)
#         print(i,c//2)
        f=i
    if k!=f:
        k=f
        a+=c//2
print(a)