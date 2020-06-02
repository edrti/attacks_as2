def mean_calculation(arr):
    sum = 0
    for num in arr:
        sum += num
    return sum / len(arr)

def variance_calculation(arr, mean):
    variance = 0
    for num in arr:
        variance += (num-mean) ** 2
    return variance / len(arr)
