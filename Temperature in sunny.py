print("Temperature in celsius and comments")
temperature = int(input("Enter temperature around you: "))
if temperature >= 45:
    print("Exterme heat")
    print("Stay indoor and drink alot of water")
elif temperature >= 35:
    print("very hot day")
    print("Ice cream time")
elif temperature >= 30:
    print("warm and sunny weather")
    print("Go for a warm walk")
elif temperature >= 25:
    print("Pleasant weather")
    print("maybe its time to drink something warm")
elif temperature >= 15:
    print("its a bit cold")
    print("Maybe its time to turnoff fans")
elif temperature > 0:
    print("Freezing temperature")
    print("always have a hot drink, stay home with heaters")
elif temperature < 0:
    print("Ice weather")