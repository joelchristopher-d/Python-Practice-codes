
# Hackerrank link: https://www.hackerrank.com/challenges/utopian-tree/problem?isFullScreen=true

def utopianTree(n):
    a=1
    for i in range(1,n+1):
        if i%2 == 0:
            a+=1
        else:
            a*=2
#             print(a)
    print(a)
            
    
    
if __name__ == "__main__":
    for i in range(int(input())):
        utopianTree(int(input()))