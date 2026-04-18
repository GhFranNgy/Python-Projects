nums = [4, 7, 2, 9, 1, 6, 8, 3, 5]
print(nums)

# Slicing
print(nums[:4])
print(nums[-3:])
print(nums[::-1])

# Loop
even_Nums = []
sum_even_Nums = 0
for num in nums: 
    if num % 2 == 0: 
        even_Nums.append(num) 
        sum_even_Nums += num 

print(even_Nums)
print(sum_even_Nums)

# List Comprehension
#                         |IF                        |LOOP
squared_nums_above_five = [num**2 if num > 5 else num for num in nums]
print(squared_nums_above_five)

# Mutation
nums.remove(9)
nums.insert(2, 10)
print(nums)

# Find largest number
largest_num = nums[0]

for num in nums:
    if num > largest_num:
        largest_num = num

print(largest_num)

# Filter nums using another list
other = [2, 3, 5, 7]
#                  |LOOP           |IF    
allowed_nums = [num for num in nums if num in other]

print(allowed_nums)