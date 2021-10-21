class BinarySearch:
    # pre : takes a list of integers and a target integer to search for
    # post: returns the index of the target integer if in the list, 
    #       otherwise returns -1
    def search(list, target):
        min = 0
        max = len(list) - 1
        while max > min:
            mid = (max + min) // 2
            if list[mid] == target:
                return mid
            elif list[mid] > target:
                max = mid - 1
            else:
                min = mid + 1
        return -1


list = [0, 2, 4, 5, 6, 8, 11, 14, 16, 19]
target1 = 4
target2 = 16
target3 = 12
print(BinarySearch.search(list, target3))

