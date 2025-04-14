numbers = list(map(int, input("Enter integers separated by space: ").split()))
filtered = [n for n in numbers if 1 <= n <= 100]
print("Filtered list:", filtered)

