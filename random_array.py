import numpy as np

a = int(input("Enter number of rows: "))
b = int(input("Enter number of columns: "))

random_array = np.random.rand(a, b)
print("Random Array:\n", random_array)
print("Average of Array:", np.mean(random_array))
