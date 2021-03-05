# switch the first element with the last element in a given array

def switch_first_with_last(arr):
    temp = arr[0]
    arr[0] = arr[-1]
    arr[-1] = temp
    return arr

arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(switch_first_with_last(arr))