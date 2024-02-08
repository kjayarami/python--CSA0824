def find_greatest(arr):
    if len(arr) == 0:
        return None
    greatest = arr[0]
    for num in arr:
        if num > greatest:
            greatest = num
    return greatest


array = [200,240,220,380,42]
print("The greatest number in the array is:", find_greatest(array))
