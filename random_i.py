import numpy as np

array = np.random.randint(1, 100, 12)
print("Original Array:", array)

sorted_array = np.sort(array)
print("Sorted Array:", sorted_array)

reshaped_matrix = sorted_array.reshape(3, 4)
print("Reshaped Matrix (3x4):\n", reshaped_matrix)
