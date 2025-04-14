dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}
nums = {**dic1, **dic2, **dic3}

nums[7] = 70
nums[3] = 80
nums.pop(3)  
print("Sum:", sum(nums.values()))
product = 1
for v in nums.values(): product *= v
print("Product:", product)
print("Max:", max(nums.values()))
print("Min:", min(nums.values()))
