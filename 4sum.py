arr = [1,0,-1,0,-2,2]
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        for k in range(j+1,len(arr)):
            for l in range(k+1,len(arr)):
                if arr[i]+arr[j]+arr[k]+arr[l]==0:
                    print(arr[i],arr[j],arr[k],arr[l],arr[i]+arr[j]+arr[k]+arr[l])
