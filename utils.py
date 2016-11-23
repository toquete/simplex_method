def multiply_array_by_scalar(arr, s):
    return [x * s for x in arr]

def divide_array_by_scalar(arr, s):
    return [x / s for x in arr]

def sum_arrays(arr1, arr2):
    return [x + arr2[i] for i, x in enumerate(arr1)]