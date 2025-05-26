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

# Reverse dictionary
reverse_morse_dict = {v: k for k, v in morse_dict.items()}

# Function to translate English to Morse
def to_morse(text):
    return ' '.join(morse_dict.get(char.upper(), '?') for char in text)

# Function to translate Morse to English
def from_morse(code):
    return ''.join(reverse_morse_dict.get(symbol, '?') for symbol in code.split())

# Main loop
while True:
    print("\n=== Morse Code Translator ===")
    print("1. Translate English to Morse")
    print("2. Translate Morse to English")
    print("3. Exit")

    choice = input("Choose an option (1, 2 or 3): ")

    if choice == "1":
        message = input("Enter your message in English: ")
        print("Morse Code:", to_morse(message))

    elif choice == "2":
        morse = input("Enter Morse Code (separate each letter with space, use / for space): ")
        print("Translated Text:", from_morse(morse))

    elif choice == "3":
        print("Goodbye, Asanda!")
        break

    else:
        print("Invalid option. Please choose 1, 2 or 3.")
