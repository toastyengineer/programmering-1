
NUMS = [3, 7, 14, 19, 21, 40, 47, 47, 69, 72, 83, 87, 94, 101]


def binary_search(arr, request):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if request == arr[mid]:
            return mid
        elif request > arr[mid]:
            start = mid + 1
        elif request < arr[mid]:
            end = mid - 1
    return False


USER_NUM = int(input("Enter number you want to search for: "))

print(f"Your number was found at index: {binary_search(NUMS, USER_NUM) + 1}")
