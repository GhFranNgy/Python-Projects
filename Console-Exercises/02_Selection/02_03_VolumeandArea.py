import math

print("Calculation of Volume and Area from Body")
print("Please choose between (Z)lynder, (C)ube, (Cu)boid, (Co)ne and (S)phere")
geoSolidType = input("Your choice: ")
area = 0
volume = 0
height = 0

#Calculation of area and volume
if(geoSolidType.lower() == "c"):
    edgeLengtha = float(input("Edge/Radius (a or r) length in cm: "))
    area = 6 * edgeLengtha**2
    volume = edgeLengtha**3

elif(geoSolidType.lower() == "s"):
    edgeLengtha = float(input("Edge/Radius (a or r) length in cm: "))
    area = 4 * math.pi * edgeLengtha**2
    volume = 4/3 * math.pi * edgeLengtha**3

elif(geoSolidType.lower() == "z"):
    edgeLengtha = float(input("Radius (r) length in cm: "))
    height = float(input("Height (h) in cm: "))
    area = edgeLengtha + height
    area *= 2 * math.pi * edgeLengtha
    volume = math.pi * edgeLengtha**2 * height
    
elif(geoSolidType.lower() == "co"):
    edgeLengtha = float(input("Radius (r) length in cm: "))
    height = float(input("Height (h) in cm: "))
    L = (edgeLengtha**2 + height**2) ** 0.5
    area = math.pi * edgeLengtha**2 + math.pi * edgeLengtha * L
    volume = 1/3 * math.pi * edgeLengtha**2 * height

elif(geoSolidType.lower() == "cu"):
    edgeLengtha = float(input("Edge (a) length in cm: "))
    edgeLengthb = float(input("Edge (b) length in cm: "))
    edgeLengthc = float(input("Edge (c) length in cm: "))

    area = 2*(edgeLengtha * edgeLengthb + edgeLengthb * edgeLengthc + edgeLengthc * edgeLengtha)
    volume = edgeLengtha * edgeLengthb * edgeLengthc

else:
    print("========================================================================")
    print("!!!Geometric solid not found!!!")

print("========================================================================")
print(f"Area: {area} cm^2, Volume: {volume} cm^3")
input("Press anything to close")