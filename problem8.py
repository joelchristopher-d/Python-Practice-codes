

# hackerrank link: https://www.hackerrank.com/challenges/angry-professor/problem?isFullScreen=true

for i in range(int(input("enter class count: "))):
    total = int(input("enter students count: "))
    atleast = int(input("enter minimum: "))
    a = list(map(int, input("enter student timing: ").rstrip().split()))
    at = 0
    for j in a:
        if j<=0:
            at+=1
    if(at>=atleast):
        print("NO")
    else:
        print("YES")


    # using list comprhension
        
def check_attendance(atleast):
    total_students = int(input("enter students count: "))
    a = list(map(int, input("enter student timing: ").rstrip().split()))
    on_time = sum(1 for timing in a if timing <= 0)  
    return "NO" if on_time >= atleast else "YES"

class_count = int(input("enter class count: "))
for _ in range(class_count):
    min_attendance = int(input("enter minimum: "))
    print(check_attendance(min_attendance))
