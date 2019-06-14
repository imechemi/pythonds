
def min(arr):
    min = arr[0]

    for i in range(1,len(arr)):
        if arr[i] < min:
            min = arr[i]
    return min 


def min1(arr):
    min = arr[0]
    for n in arr:
        for n2 in arr:
            if n2 < min:
                min = n2
    return min 

print(min1([4,5,1,3,4,9,2,1,4,9,2,1,2,4]))