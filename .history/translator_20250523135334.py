# Morse code dictionary
morse_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
    'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', ' ': '/', '-': '-....-',
    '!': '-.-.--', '.': '.-.-.-', '?': '..--..',
}

# Function to translate English to Morse code
def to_morse(text):
    return ' '.join(morse_dict.get(char.upper(), '?') for char in text)

# Main menu loop
while True:
    print("\n=== Morse Code Translator ===")
    print("1. Translate English to Morse")
    print("2. Exit")

    choice = input("Choose an option (1 or 2): ")

    if choice == "1":
        message = input("Enter your message: ")
        print("Morse Code:", to_morse(message))

    elif choice == "2":
        print("Goodbye, Asanda!")
        break

    else:
        print("Invalid option. Please choose 1 or 2.")
