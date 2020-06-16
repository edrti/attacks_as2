import math

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

def co_variance_calculation(a, b, mean_a, mean_b):
    covariance = 0
    for idx in range(len(a)):
        covariance = (a[idx] - mean_a) * (b[idx] - mean_b)
    return covariance / len(a)


def pearson_corr_coef(a, b):
    mean_a = mean_calculation(a)
    var_a = variance_calculation(a, mean_a)
    mean_b = mean_calculation(b)
    var_b = variance_calculation(b, mean_b)
    cov = co_variance_calculation(a, b, mean_a, mean_b)
    return cov / math.sqrt(var_a * var_b)