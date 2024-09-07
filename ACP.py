def listLen(arr):
    if not arr: return 0
    return 1 + listLen(arr[1::2]) + listLen(arr[2::2])

myarr = [1, 4, 2, 3, 6, 5, 3, 2, 6]
print("List:")
print(myarr)
print("List size:", listLen(myarr))