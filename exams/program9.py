#To implement Bubble Sort
def bubble_sort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in  range(n):
     #Last i elements are already in place, so we don't need to check them
    for j in range(0, n-i-1):
      # Swap if the element found is greater than the next element
          if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1]. arr[j]

#Example usage
my_list = [64,34,25,12,22,11,90]
print("Before use Bubble_sort:", my_list)
bubble_sort(my_list)

print("Sorted array:", my_list)