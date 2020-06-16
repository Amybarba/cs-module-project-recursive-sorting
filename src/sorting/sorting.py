# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(a, b):
    # merged = [0] * (len(a) + len(b))
    # merged = [0 for _ in range(len(a) + len(b))]

    merged = []
    # Your code here
    left = 0
    right = 0

    while left < len(a) and right < len(b):
        if a[left] < b[right]:
            merged.append(a[left])
            left += 1
        else:
            merged.append(b[right])
            right += 1
    while left < len(a):
        merged.append(a[left])
        left += 1
    while right < len(b):
        merged.append(b[right])
        right += 1

    return merged


# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) > 1:
        return arr
        left = merge_sort(arr[:len(arr) // 2])
        right = merge_sort(arr[len(arr) // 2:])
        return merge(left, right)

        return arr


# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
