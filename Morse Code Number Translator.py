print("========== MORSE CODE OF NUMBERS ==========")

morse = {
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----."
}

number = input("Enter a number: ")

print("\nMorse Code:")

for digit in number:
    print(morse[digit], end=" ")

print("\n\nThank you!")
