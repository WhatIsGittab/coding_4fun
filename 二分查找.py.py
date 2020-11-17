l = [int(x) for x in input().split(' ')]

def binary_search(arr,x):
    l,r = 0,len(arr)-1
    while r >= l:
        mid = (l+r)//2
        if arr[mid] == x:
            return mid
        if arr[mid] > x:
            r = mid
        else:
            l = mid
    else:
        return -1

x = int(input())
print(binary_search(l,x))
