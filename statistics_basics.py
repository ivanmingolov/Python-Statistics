import sys
import math
import numpy
from functools import reduce

# Mean : Average of the data set
def mean(*args):
    sum_of_args = sum(args)
    return sum_of_args / len(args)

# Median : Number at the center of the data set
def median(*args):
    if len(args) % 2 == 1: # length is odd
        i = round(len(args) / 2) # Middle element
        return args[i]
    else: # length is even
        i = round((len(args) + 1) / 2)
        j = i - 1
        return (args[i] + args[j]) / 2

# Mode : Number that occurs most often in the data set
def mode(*args):
    values_count = {i: args.count(i) for i in args} # Dictionary where the keys are all different values and values are the count of each value
    max_count = max(values_count.values())
    max_values = [key for key, value in values_count.items() if value == max_count] # All values that occur 'max' number of times
    return max_values

# Variance : How is the data spread around the mean
def variance(*args):
    mean_value = mean(*args)
    difference_to_mean_squared = list(map(lambda x : (x - mean_value) ** 2, args)) # map to every element the difference to the mean and squared it
    variance_value = reduce(lambda x, y : x + y, difference_to_mean_squared) / (len(args) - 1) # sum all difference_to_mean_squared values and divides by the length - 1
    return variance_value

# Standard deviation : Square root of the variance, because variance gives extra weight to outliers because of the squared values
def standard_deviation(*args):
    return math.sqrt(variance(*args))

# Coefficient of variation

# Covariance

# Correlation coefficient


# Main
print(f'Mean of [1, 2, 3, 4, 5] is {mean(1, 2, 3, 4, 5)}')

print (f'Median of [1, 2, 3, 4, 5] is {median(1, 2, 3, 4, 5)}')
print (f'Median of [1, 2, 3, 4, 5, 6] is {median(1, 2, 3, 4, 5, 6)}')

print (f'Mode of [1, 2, 3, 4, 5, 5, 4] is {mode(1, 2, 3, 4, 5, 5, 4)}')

print (f'Variance of [4, 6, 3, 5, 2] is {variance(4, 6, 3, 5, 2)}')

print (f'Standard deviation of [4, 6, 3, 5, 2] is {standard_deviation(4, 6, 3, 5, 2)}')