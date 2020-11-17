
def quick_sort(li, start, end):
    if start >= end:
        return 
    left = start
    right = end
    mid = li[left] 
    while left<right:
        while left < right and li[right] > mid:
            right -= 1
        li[left] = li[right]
        while left < right and li[left] < mid:
            left += 1
        li[right] = li[left]
    li[left] = mid
    quick_sort(li,start,left-1)
    quick_sort(li,left+1,end)
l = [int(x) for x in input().split(' ')]
quick_sort(l,0,len(l)-1)
print(l)