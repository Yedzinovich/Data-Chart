import matplotlib.pyplot as plt
import numpy as np

test_1_grades = [90, 98, 85, 97,  80]
test_2_grades = [100, 85, 60, 90, 70]

plt.scatter(test_1_grades, test_2_grades)
plt.title("Axes are not comparable")
plt.xlabel("test 1 grade")
plt.ylabel("test 3 grade")
plt.show()