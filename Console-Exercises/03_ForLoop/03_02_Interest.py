capital = float(input("Capital in $: \n"))
interestRate = float(input("Interest rate in %: \n"))
years = int(input("Years: \n"))


rate = interestRate / 100 # Convert percentage to decimal

# Simple Interest
print("\n====================Simple Interest====================\n")

simple_total = capital

for year in range(1, years + 1):
    interest = capital * rate
    simple_total += interest
    print(f"Year {year}:    Interest = ${interest:.2f}, Total = ${simple_total:.2f}")

# Compound Interest
print("\n===================Compound Interest===================\n")

compound_total = capital

for year in range(1, years + 1):
    interest = compound_total * rate
    compound_total += interest
    print(f"Year {year}:    Interest = ${interest:.2f}, Total = ${compound_total:.2f}")

input("Press anything to close")