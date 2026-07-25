print("Blood Group data")
print("This project is about Blood Group who Can Donate To and who Can Receive From")
group = input("Enter the blood group: ").upper()
if group == "O-":
    print("donate to - Everyone")
    print("receives - O-")
elif group == "O+":	
    print("donate to - O+, A+, B+, AB+")
    print("receives - O+, O-")
elif group == "A-":
    print("donate to - A-, A+, AB-, AB+")
    print("receives - A-, O-")
elif group == "A+":
    print("donate to - A+, AB+")
    print("receives - A+, A-, O+, O-")
elif group == "B-":
    print("donate to - B-, B+, AB-, AB+")
    print("receives - B-, O-")
elif group == "B+":
    print("donate to - B+, AB+")
    print("receives - B+, B-, O+, O-")
elif group == "AB-":
    print("donate to - AB-, AB+")
    print("receives - AB-, A-, B-, O-")
elif group == "AB+":
    print("donate to - Everyone (Plasma differs)")
    print("receives - Everyone")

print("Press Enter to exit")
