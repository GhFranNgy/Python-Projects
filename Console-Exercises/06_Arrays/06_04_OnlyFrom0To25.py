list = []
end_list = []

print("press enter to finisch entering numbers")

while True:

    user_input = input("Enter a number: ")

    if user_input == "":
        break

    try:
        user_input = int(user_input)
    except ValueError:
        print("Not a valid number")
        continue

    list.append(user_input)
# clear list of unallowed numbers
for value in list:
    if 0 <= value <= 25:
        end_list.append(value)
# square remaining numbers
for i in range(len(end_list)):
    end_list[i] = end_list[i] ** 2

print(end_list)