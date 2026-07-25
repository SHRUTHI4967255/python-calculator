print("           Planets and their gravity                 ")
print("This project has gravity details in m/s^2, g and number of moons")
planet = input("Enter the Planet name: ").capitalize()

if planet == "Mercury":
    print("Gravity[m/s^2] - 3.70")
    print("gravity[g] - 0.38")
    print("number of moons - 0")
elif planet == "Venus":
    print("Gravity[m/s^2] - 8.87")
    print("gravity[g] - 0.90")
    print("number of moons - 0")
elif planet == "Earth":
    print("Gravity[m/s^2] - 9.81")
    print("gravity[g] - 1.00")
    print("number of moons - 1")
elif planet == "Mars":
    print("Gravity[m/s^2] - 3.71")
    print("gravity[g] - 0.38")
    print("number of moons - 2")
elif planet == "Jupiter":
    print("Gravity[m/s^2] - 24.79")
    print("gravity[g] - 2.53")
    print("number of moons - 95")
elif planet == "Saturn":
    print("Gravity[m/s^2] - 10.44")
    print("gravity[g] - 1.07")
    print("number of moons - 146")
elif planet == "Uranus":
    print("Gravity[m/s^2] - 8.69")
    print("gravity[g] - 0.89")
    print("number of moons - 28")
elif planet == "Neptune":
    print("Gravity[m/s^2] - 11.15")
    print("gravity[g] - 1.14")
    print("number of moons - 16")
else:
    print("Sorry couldn't find, Try correctly")
    
print("Press enter to exit")