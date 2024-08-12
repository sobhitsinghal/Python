#To merge two 3d arrays
from typing import List


def merge_3d_arrays(arr1, arr2):
    if len(arr1) != len(arr2) or len(arr1[0]) != len(arr2[0]) or len(arr1[0][0]) != len(arr2[0][0]):
        print("Error: Arrays should have the same dimensions for merging.")
        return None

    merged_array = []

    for i in range(len(arr1)):
        merged_array.append([])
        for j in range(len(arr1[0])):
            merged_array[i].append([])
            for k in range(len(arr1[0][0])):
                merged_array[i][j].append(arr1[i][j][k])

    for i in range(len(arr2)):
        for j in range(len(arr2[0])):
            for k in range(len(arr2[0][0])):
                merged_array[i][j].append(arr2[i][j][k])  # Append to inner list

    return merged_array

#Example usage:
if __name__ == "__main__":
    #Create two 3D arrays
    array1 = [[[1,2,3], [4,5,6]], [[7,8,9], [10,11,12]]]
    array2 = [[[13,14,15], [16,17,18]], [[19,20,21], [22,23,24]]]

    # Merge the two 3D arrays
    merged_result = merge_3d_arrays(array1,array2)

    #Display the original arrays and the merged result
    print("Array1:")
    for row in  array1:
        print(row)
    print("\nArray 2:")
    for row in array2:
        print(row)
    print("\nMerged Result:")
    for row in merged_result:
        print(row)
