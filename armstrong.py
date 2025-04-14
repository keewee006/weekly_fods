def is_armstrong(n):
    num_str = str(n)
    power = len(num_str)
    total = sum(int(d)**power for d in num_str)
    return total == n

# test
n = int(input("Enter a number: "))
print("Armstrong?" , is_armstrong(n))
