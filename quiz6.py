



# Given an integer, 
# for each digit that makes up the integer determine whether it is a divisor. 
# Count the number of divisors occurring within the integer.







i = int(input())
j=i
c=0

while(i):
    r = i%10
    i=i//10
#     print(r)
    if(r!=0 and j%r==0):
        c+=1
print(c)