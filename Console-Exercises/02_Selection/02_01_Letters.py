print("gramm in g        20      50      100     250     500     1000")
print("Dollar in $       1,00    1,70    2,40    3,20    4,00    4,80")
weight = float(input("How much does your Letter weigh in g(gram)? \n"))
cost = 0

if(weight > 1000):
    cost = 4.80
elif(weight > 500):
    cost = 4,00
elif(weight > 250):
    cost = 3.20
elif(weight > 100):
    cost = 2.40
elif(weight > 50):
    cost = 1.70
else:
    cost = 1.00

print(f"Price: {cost}$")