def search(arr, x):
  
    for i in range(len(arr)):
  
        if arr[i] == x:
            return i
  
    return -1

arr=list(map(int,input().split()))
x=int(input())
if(search(arr,x) >0):
    print("Element Found")
else:
    print("Element not found")
