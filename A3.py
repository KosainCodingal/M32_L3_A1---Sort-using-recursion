def listMax(arr):
    l = len(arr)
    if l == 1: return arr[0]
    if l == 0: return 0

    return max(arr[0], listMax(arr[1:]))

a = [1, 3, 6, 4]
print(listMax(a))