nums = [12,7,5,18,3,10,2]
sorted_Dict = {}

for number in nums:
    if number % 2 == 0: 
        if "even" not in sorted_Dict:
            sorted_Dict["even"] = []
        sorted_Dict["even"].append(number)

        if "sum_even" not in sorted_Dict:
            sorted_Dict["sum_even"] = 0
        sorted_Dict["sum_even"] += number

    else:
        if "odd" not in sorted_Dict:
            sorted_Dict["odd"] = []
        sorted_Dict["odd"].append(number)

        if "sum_odd" not in sorted_Dict:
            sorted_Dict["sum_odd"] = 0
        sorted_Dict["sum_odd"] += number

print(sorted_Dict)