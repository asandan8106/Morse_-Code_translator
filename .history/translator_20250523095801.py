# 🧠 Secret Morse Code Translator by Asanda

# Dictionary to map letters and numbers to Morse Code
MORSE_CODE_DICT = {
    'A': '.-',    'B': '-...',  'C': '-.-.', 
    'D': '-..',   'E': '.',     'F': '..-.',
    'G': '--.',   'H': '....',  'I': '..',
    'J': '.---',  'K': '-.-',   'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',
    'P': '.--.',  'Q': '--.-',  'R': '.-.',
    'S': '...',   'T': '-',     'U': '..-',
    'V': '...-',  'W': '.--',   'X': '-..-',
    'Y': '-.--',  'Z': '--..',

    '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..',
    '9': '----.',

    ' ': '/',     ',': '--..--', '.': '.-.-.-',
    '?': '..--..', '!': '-.-.--', '-': '-....-',
    "'": '.----.', '/': '-..-.',  '(': '-.--.',
    ')': '-.--.-'
}
# Function to convert letters to Morse Code
def letters_to_morse(text):
    text = text.upper()
    morse_code = []

    for char in text:
        if char in MORSE_CODE_DICT:
            morse_code.append(MORSE_CODE_DICT[char])
        else:
            morse_code.append('?')  # Unknown character

    return ' '.join(morse_code)
