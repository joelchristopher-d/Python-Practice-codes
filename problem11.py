# Hackerrank link: https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem?isFullScreen=true

def climbingLeaderboard(ranked, player):
    ranked = sorted(set(ranked), reverse=True)
    j = len(ranked)
    rank = []
    for i in player:
        while(j>0 and i>=ranked[j-1]):
            j-=1
        rank.append(j+1)
    return rank


if __name__ == "__main__":
    ranked = [100,100,50,40,40,20,10]
    player = [5,25,50,121]
    print(climbingLeaderboard(ranked,player))