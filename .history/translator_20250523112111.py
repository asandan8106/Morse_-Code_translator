# 🧠 Secret Morse Code Translator by Asanda

def to_morse(text):
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
        '!': '-.-.--'
    }

    return ' '.join(morse_dict.get(char.upper(), '?') for char in text)

# 🧠 Main part that runs
while True:
    print("\n=== Morse Code Translator ===")
    text = input("Type your message (or type 'exit' to quit): ")

    if text.lower() == "exit":
        print("Goodbye!")
        break

    print("Morse Code:", to_morse(text))
