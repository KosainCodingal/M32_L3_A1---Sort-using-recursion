def isSorted(arr):
    l = len(arr)
    if l in (0, 1): return True
    #if l == 0 or l == 1: return 1

    return arr[0] <= arr[1] and isSorted(arr[1:])


a = [1, 2, 3, 4, 5]
b = [3, 6, 5, 2, 1]

print(isSorted(a))
print(isSorted(b))

input()
