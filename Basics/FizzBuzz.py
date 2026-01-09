#===Variables===
#===Start Message===
print("Welcome to FizzBuzz!")
runLength = int(input("Enter the length of the FizzBuzz sequence: "))
#===FizzBuzz Logic===
for i in range(1, runLength + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)