fruits = ["apple", "banana", "apple", "orange", "banana", "kiwi", "apple"]
fruit_kinds = set(fruits)
fruit_counter = {}
fruit_common = None
highest_count = 0

for fruit in fruits:
    if fruit in fruit_counter:
        fruit_counter[fruit] += 1
    else:
        fruit_counter[fruit] = 1

for fruit in fruit_counter:
    if fruit_counter[fruit] > highest_count:
        highest_count = fruit_counter[fruit]
        fruit_common = fruit

print(f"List of all fruits: {fruits}")
print(f"List of fruit kinds: {fruit_kinds}")
print(f"List of fruits counted: {fruit_counter}")
print(f"Most common fruit: {fruit_common}")
