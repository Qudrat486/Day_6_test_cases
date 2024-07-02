def bubble_sort(arr):
    """
    Sorts a list of numbers in ascending order using the bubble sort algorithm.

    Parameters:
    arr (list): A list of numbers to be sorted.

    Returns:
    list: The sorted list in ascending order.
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Test cases for bubble_sort
print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))  # Expected output: [11, 12, 22, 25, 34, 64, 90]
print(bubble_sort([5, 3, 8, 4, 2]))               # Expected output: [2, 3, 4, 5, 8]
print(bubble_sort([1]))                           # Expected output: [1]
print(bubble_sort([]))                            # Expected output: []

