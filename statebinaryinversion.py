m=[[1,1,0],[0,0,1]]
m=[[1,0,1],[1,1,0],[0,1,1],[1,1,1]]
for i in range(len(m)):
    m[i]=m[i][::-1]
for i in range(len(m)):
    for j in range(len(m[i])):
        if m[i][j]==0:
            m[i][j]=1
        else:
            m[i][j]=0
            
print(m)
