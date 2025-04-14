set1 = {20, 40, 60}
set2 = {10, 20, 30, 40, 50, 60}

union_set = set1 | set2
print("Union length:", len(union_set))
print("Intersection:", set1 & set2)
print("Symmetric Difference:", set1 ^ set2)
set1.add(40)
print("Set1 after adding 40:", set1)
set2.discard(20)
print("Set2 after removing 20:", set2)
