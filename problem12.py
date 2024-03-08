# hackerrank link: https://www.hackerrank.com/challenges/circular-array-rotation/problem?isFullScreen=true

def rotation(a,count,q):
    for i in range(count):
        first = 0
        temp=a[-1]
        while(first!=len(a)):
            a[first],temp=temp,a[first]
            first+=1   
    for j in q:
        print(a[j])
     
if __name__ == "__main__":
    rotation([3,4,5],2,[1,2])