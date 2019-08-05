from matplotlib import pyplot as plt
from collections import Counter

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
