def reverseArray(arr):
    # Write your code here
    resarr=[]
    for i in range (len(arr)-1,-1,-1):
        resarr.append(arr[i])
    return resarr