#Input from user 
m = float(input("Enter mass in kilogram: "))

#constant value for speed of light in m/s
c = 299792458

#calculating energy using einstein's equation
energy = m * c ** 2

#displaying the result 
print(f"The energy equivalent to {m} kg of mass is {energy} joules")