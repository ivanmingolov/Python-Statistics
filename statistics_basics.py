import math
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
    variance_value = sum(difference_to_mean_squared) / (len(args) - 1) # sum all difference_to_mean_squared values and divides by the length - 1
    return variance_value

# Standard deviation : Square root of the variance, because variance gives extra weight to outliers because of the squared values
def standard_deviation(*args):
    return math.sqrt(variance(*args))

# Coefficient of variation : Used to compare different data sets
def coefficient_of_variation(*args):
    return standard_deviation(*args) / mean(*args)


# Covariance : Tells us if two values are moving in the same direction
# Constraint : the lists should be of the same size
def covariance(x, y):
    mean_fist_list = mean(*x)
    mean_second_list = mean(*y)
    difference_to_mean_first_list = list(map(lambda x : x - mean_fist_list, x))
    difference_to_mean_second_list = list(map(lambda y : y - mean_second_list, y))
    products = [i * j for i, j in zip(difference_to_mean_first_list, difference_to_mean_second_list)]
    return sum(products) / (len(x) - 1)

# Correlation coefficient : Adjust covariance to see relationships
def correlation_coefficient(x, y):
    return covariance(x, y) / (standard_deviation(*x) * standard_deviation(*y))

if __name__ == '__main__':
    print(f'Mean of [1, 2, 3, 4, 5] is {mean(1, 2, 3, 4, 5)}')

    print (f'Median of [1, 2, 3, 4, 5] is {median(1, 2, 3, 4, 5)}')
    print (f'Median of [1, 2, 3, 4, 5, 6] is {median(1, 2, 3, 4, 5, 6)}')

    print (f'Mode of [1, 2, 3, 4, 5, 5, 4] is {mode(1, 2, 3, 4, 5, 5, 4)}')

    print (f'Variance of [4, 6, 3, 5, 2] is {variance(4, 6, 3, 5, 2)}')

    print (f'Standard deviation of [4, 6, 3, 5, 2] is {standard_deviation(4, 6, 3, 5, 2)}')

    coefficient_of_variation_miles = coefficient_of_variation(3, 4, 4.5, 3.5)
    coefficient_of_variation_kilometers = coefficient_of_variation(4.828, 6.437, 7.242, 5.632)

    print(f"Coefficient of Variation (miles): {coefficient_of_variation_miles}")
    print(f'Coefficient of Variation (kilometers): {coefficient_of_variation_kilometers}')
    print(f'Compare if the values are close: {math.isclose(coefficient_of_variation_miles, coefficient_of_variation_kilometers, rel_tol= 1 ** -6, abs_tol= 1 ** -6)}')

    market_cap_values = [1532, 1488, 1343, 928, 615]
    earnings_values = [58, 35, 75, 41, 17]
    print(f'Covariance of {market_cap_values} and {earnings_values} is {covariance(market_cap_values, earnings_values):.1f} and should be 5803.2')

    print(f'Correlation coefficient of {market_cap_values} and {earnings_values} is {correlation_coefficient(market_cap_values, earnings_values):.4f} and should be 0.6601')