def count_case(s):
    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    return upper, lower

# Test
s = input("Enter a string: ")
u, l = count_case(s)
print("Uppercase letters:", u)
print("Lowercase letters:", l)