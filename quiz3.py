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
        if i>=38:
            t=i//5
            if (t*5)-i!=0:
                if ((t+1)*5)-i <3:
    #                 print(t)
                    l1.append(((t+1)*5))
                else:
    #                 print(i)
                    l1.append(i)
            else:
                l1.append(i)
        else:
            l1.append(i)
        
    print(l1)


if __name__=="__main__":
    grades = [73,67,38,33]
    Grade(grades)
