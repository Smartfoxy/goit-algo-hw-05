import math


def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    count = 0
    upper_bound = None
 
    while low <= high:
        count += 1
        mid = (high + low) // 2
 
        if arr[mid] < x:
            low = mid + 1
 
        elif arr[mid] > x:
            high = mid - 1
            upper_bound = arr[mid]

        else:
            upper_bound = arr[mid]
            return(count, upper_bound)          
 
    return (count, upper_bound)

arr = [1.1, 3.5, 5.7, 8.6, 10.5, 12.7, 15.22, 18.23, 20.45, 22, 24]
print(binary_search(arr, 15.22))
print(binary_search(arr, 18.23))

print(binary_search(arr, 12.7))
print(binary_search(arr, 5.70))

print(binary_search(arr, 15.2))
print(binary_search(arr, 18.33))

print(binary_search(arr, 100))
