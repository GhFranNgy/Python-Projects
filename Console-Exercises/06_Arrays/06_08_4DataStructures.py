data = ["apple", "banana", "apple", "orange", "banana", "kiwi"]

# remove duplicates (use set for efficiency)
seen = set()
data_list = []
for item in data:
    if item not in seen:
        data_list.append(item)
        seen.add(item)

# keeps only unique items (no duplicates, no order)
data_set = set(data)

# structure can not change
data_tuple = tuple(data)
# NO data_tuple[0] = Cherry

# count frequency of items
data_dict = {}
for item in data:
    if item in data_dict:
        data_dict[item] += 1
    else:
        data_dict[item] = 1

print(f" Data: {data} \n Seen(Set): {seen} & List: {data_list} \n Set: {data_set} \n Tuple: {data_tuple} \n Dict: {data_dict}")