def find_smallest(arr):
    if len(arr) == 0:
        return None
    smallest = arr[0]
    for num in arr:
        if num < smallest:
            smallest = num
    return smallest


array = [200,240,220,380,42]
print("The smallest number in the array is:", find_smallest(array))
