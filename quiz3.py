# Sample Input 0

# 4
# 73
# 67
# 38
# 33
# Sample Output 0

# 75
# 67
# 40
# 33

# https://www.hackerrank.com/challenges/grading/problem?isFullScreen=true

def Grade(grades):           
    l1=[]
    for i in grades:
        if i>=38 and i%5>=3:
            i = i+(5-(i%5))
        l1.append(i)
        
    print(l1)


if __name__=="__main__":
    grades = [73,67,38,33]
    Grade(grades)
