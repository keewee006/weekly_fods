def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): return a / b
def trunc_div(a, b): return a // b
def mod(a, b): return a % b
def exp(a, b): return a ** b
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print("Add:", add(a, b))
print("Sub:", sub(a, b))
print("Mul:", mul(a, b))
print("Div:", div(a, b))
print("Trunc Div:", trunc_div(a, b))
print("Mod:", mod(a, b))
print("Exp:", exp(a, b))