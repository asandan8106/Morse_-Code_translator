import tkinter as tk
from tkinter import messagebox

# Morse Code Dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.', ' ': '/',
    '!': '-.-.--', ',': '--..--', '?': '..--..', '.': '.-.-.-'
}

def translate_to_morse(message):
    return ' '.join(MORSE_CODE_DICT.get(char.upper(), '?') for char in message)

def on_translate():
    text = entry.get()
    if text.strip() == "":
        messagebox.showwarning("Warning", "Please enter a message.")
        return
    result = translate_to_morse(text)
    output_label.config(text=f"Morse Code:\n{result}")

# GUI setup
root = tk.Tk()
root.title("Morse Code Translator")

tk.Label(root, text="Enter Message:").pack(pady=5)

entry = tk.Entry(root, width=40)
entry.pack(pady=5)

tk.Button(root, text="Translate", command=on_translate).pack(pady=5)

output_label = tk.Label(root, text="", wraplength=300, justify="left")
output_label.pack(pady=10)

root.mainloop()
