# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, low, high, target):
    # Your code here
    if high >= low:

        mid = (high + low) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] > target:
            return binary_search(arr, low, mid - 1, target)

        else:
            return binary_search(arr, mid + 1, high, target)

    else:
        return -1


arr = [2, 3, 4, 10, 40]
target = 10

result = binary_search(arr, 0, len(arr) - 1, target)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
# def agnostic_binary_search(arr, target, low, high):
# Your code here
# middle = (low+high) // 2

# if len(arr) == 0:
# return -1
