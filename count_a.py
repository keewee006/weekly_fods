names = input("Enter names separated by commas: ").split(',')
count = sum(name.lower().count('a') for name in names)
print("Total 'a' count:", count)
