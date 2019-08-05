from matplotlib import pyplot as plt
from collections import Counter
import math

num_friends = [100, 49, 40, 25, 18, 30, 29, 89]

friend_counts = Counter(num_friends)
xs = range(101)
ys = [friend_counts[x] for x in xs]
plt.bar(xs, ys)
plt.axis([0, 101, 0, 25])
plt.title("Histogram of Frind Counts")
plt.xlabel("# of friends")
plt.ylabel("# pf people")
plt.show()

num_points = len(num_friends)

largest_value = max(num_friends)
smallest_value = min(num_friends)

sorted_values = sorted(num_friends)
smallest_value = sorted_values[0]
second_smallest_value = sorted_values[1]
second_largest_value = sorted_values[-2]

def median(v):

  n = len(v)
  sorted_v = sorted(v)
  midpoint = n//2

  if n % 2 == 1:
    return sorted_v[midpoint]
  else:
    lo = midpoint - 1
    li = midpoint
    return(softed_v[lo] + sorted_v[hi])/2

def mean(x):
  return sum(x) / len(x)

def dot(v, w):
 return sum(v_i * w_i
 for v_i, w_i in zip(v, w))
  
def sum_of_squares(v):
  return dot(v, v)


def quantile(x, p):
  p_index = int(p * len(x))
  return sorted(x)[p_index]  

print(quantile(num_friends, 0.10)) 

def mode(x):
  counts = Counter(x)
  max_count = max(counts.values())
  return [x_i for x_i, count in counts.items() if count == max_count]

print(mode(num_friends))

def data_range(x):
  return max(x) - min(x)

def de_mean(x):
  x_bar = mean(x)
  return [x_i - x_bar for x_i in x]

def variance(x):
  n = len(x)
  deviations = de_mean(x)  
  return sum_of_squares(deviations) / (n - 1)

def standard_deviation(x):
  return math.sqrt(variance(x))

def interquartile_range(x):
  return quantile(x, 0.75) - quantile(x, -0.25)

def covariance(x, y):
  n = len(x)
  return dot(de_mean(x), de_mean(y)) / (n - 1)

def correlation(x, y):
  stdev_x = standard_deviation(x)
  stdev_y = standard_deviation(y)

  if(stdev_x > 0 and stdev_y > 0):
    return covariance(x, y)/ stdev_x / stdev_y
  else:
    return 0;

outlier = num_friends.index(100)

num_friends_good = [x for i, x in enumerate(num_friends) if i != outlier]

daily_minutes = [20, 30, 40, 50, 60, 12, 25, 19]

daily_minutes_good = [x for i, x in enumerate(daily_minutes) if i != outlier]

correlation(num_friends_good, daily_minutes_good)




