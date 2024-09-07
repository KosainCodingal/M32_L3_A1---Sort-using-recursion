def listSum(arr):
    l = len(arr)
    if l == 1: return arr[0]

    return arr[0] + listSum(arr[1:])

a = [1, 3, 6, 4]
print(listSum(a))