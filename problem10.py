# hackerranlink: https://www.hackerrank.com/challenges/cats-and-a-mouse/problem?isFullScreen=true


def catAndMouse(x, y, z):
#     l = ["Cat A" if(abs(x-z)< abs(y-z)) else "Cat B" if (abs(x-z)> abs(y-z)) else "Mouse C"]
    return "Cat A" if(abs(x-z)< abs(y-z)) else "Cat B" if (abs(x-z)> abs(y-z)) else "Mouse C"
    

if __name__ == "__main__":
    print(catAndMouse(2,5,4))
    print(catAndMouse(1,2,3))
    print(catAndMouse(1,3,2))