weight = input("Weight into Kilograms:")
unit = input("(T)on[metric] or (G)ram or (M)illigram or (U)microgram or (S)tone or (N)US ton or (O)unce or (L)bs: ")
if unit.upper() == "L":
    converted = float(weight) * 0.45
    print("Weight in Kg: " + str(converted))
elif unit.upper() == "O":
       converted = float(weight) * 0.028
       print("Weight in Kg: " + str(converted))
elif unit.upper() == "N":
      converted = float(weight) * 907.18
      print("Weight in Kg: " + str(converted))
elif unit.upper() == "S":
      converted = float(weight) * 6.35
      print("Weight in Kg: " + str(converted))
elif unit.upper() == "U":
      converted = float(weight) / 1000000000
      print("Weight in Kg: " + str(converted))
elif unit.upper() == "M":
      converted = float(weight) / 1000000
      print("Weight in Kg: " + str(converted))
elif unit.upper() == "G":
      converted = float(weight) / 1000
      print("Weight in Kg: " + str(converted))
elif unit.upper() == "T":
      converted = float(weight) * 1000
      print("Weight in Kg: " + str(converted))