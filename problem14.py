# Hackerranklink: https://www.hackerrank.com/challenges/the-hurdle-race/problem?isFullScreen=true

def hurdleRace(k, height):
    if(max(height)-k > 0):
        return max(height)-k
    else:
        return 0
    
    
    
if __name__ == "__main__":
    print(hurdleRace(5,[1,2,3,4,5]))   