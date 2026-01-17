print("Quadratische gleichung a*x^2 + b*x + c = 0")
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

x1 = 0;
x2 = 0;

#-b+-sgrt(b*b - 4*a*c) / 2*a
#Calculation for x1

discriminants = b**2 - 4 * a * c

x1 -= b
x1 += discriminants ** 0.5
x1 /= 2 * a

x2 -= b
x2 -= discriminants ** 0.5
x2 /= 2 * a

print(f"x1 : {x1}, x2 : {x2}")