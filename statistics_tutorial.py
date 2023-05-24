import sys
import math
import numpy




# Mean
def mean(*args):
    sum_of_args = sum(args)
    return sum_of_args / len(args)

# Median
def median(*args):
    if len(args) % 2 == 1: # length is odd
        i = round(len(args) / 2)
        return args[i]
    else: # length is even
        i = round((len(args) + 1) / 2)
        j = i - 1
        return (args[i] + args[j]) / 2

# Mode

# Variance

# Standard deviation

# Coefficient of variation

# Covariance

# Correlation coefficient


# Main

print(f'Mean of [1, 2, 3, 4, 5] is {mean(1, 2, 3, 4, 5)}')

print (f'Median of [1, 2, 3, 4, 5] is {median(1, 2, 3, 4, 5)}')
print (f'Median of [1, 2, 3, 4, 5, 6] is {median(1, 2, 3, 4, 5, 6)}')