import numpy as np

user_input = input("Enter at least 10 numbers separated by spaces: ")
numbers = list(map(int, user_input.split()))

if len(numbers) < 10:
    print("Please enter at least 10 numbers.")
else:
    array = np.array(numbers)
    sorted_array = np.sort(array)

    print("Sorted Array:", sorted_array)
    print("Elements from index 2 to 5:", sorted_array[2:6])
    print("Elements from index 5 to 8:", sorted_array[5:9])
    print("Elements from index 2 to 9:", sorted_array[2:10])
