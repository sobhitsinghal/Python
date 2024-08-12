#To find out the sum of all elements in an array using recusrion
def array_sum(arr, n):
    # Base case: if the array is empty, return 0
    if n == 0:
        return 0
    else:
       # Recursive case: sum the current element with the sum of the rest of the array
       return arr[n - 1] + array_sum(arr,n - 1)

#Example usage
my_array  = [1,2,3,4,5]
array_length = len(my_array)

result = array_sum(my_array, array_length)

print("Array is:", my_array)
print(f"The sum of elements in the array is: {result}")

