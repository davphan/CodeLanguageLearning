import random as r

def merge_sort(arr: list):
    # recursive loop
    if len(arr) > 1:
        # split into left and right arrays
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        # recursive calls
        merge_sort(left)
        merge_sort(right)
        # set index counter for left, right, and main arrays
        i = j = k = 0
        # sort between both sides
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        # sort remaining elements of longer array
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

def quick_sort()

if __name__ == '__main__':
    array = []
    for i in range(20):
        array.append(r.randint(0, 50))
    print(f"og array: {array}")
    merge_sort(array)
    print(f"sorted array: {array}")