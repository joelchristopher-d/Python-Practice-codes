def findlargest(ind,arr,curr):
    if ind==len(arr):return curr
    return findlargest(ind+1,arr,max(curr,arr[ind]))
    
    
arr = [10,9,8,7,6,5,4,3,2,1,12]
curr = findlargest(0,arr,arr[0])
print(curr)
