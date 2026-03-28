MORSE_MAP = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', ',': '--..--', '.': '.-.-.-', '?': '..--..',
    '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-'
}

TEXT_MAP = {morse: letter for letter, morse in MORSE_MAP.items()}


def convert_to_morse(text):
    """Takes regular text and spits out morse code"""
    result = []
    
    for char in text.upper():
        if char == ' ':
            result.append('/')
        elif char in MORSE_MAP:
            result.append(MORSE_MAP[char])
    
    return ' '.join(result)


def convert_to_text(morse_code):
    """Takes morse code and converts it back to readable text"""
    words = morse_code.split(' / ')
    decoded_words = []
    
    for word in words:
        letters = word.split()
        decoded_letters = []
        
        for code in letters:
            if code in TEXT_MAP:
                decoded_letters.append(TEXT_MAP[code])
            elif code == '/':
                decoded_words.append(''.join(decoded_letters))
                decoded_letters = []
        
        if decoded_letters:
            decoded_words.append(''.join(decoded_letters))
    
    return ' '.join(decoded_words)


def main():
    print("=" * 50)
    print("Welcome to Morse Code Translator!")
    print("=" * 50)
    
    while True:
        print("\nWhat would you like to do?")
        print("  1 - Turn text into morse code")
        print("  2 - Turn morse code into text")
        print("  3 - I'm done, exit")
        
        choice = input("\nYour choice: ").strip()
        
        if choice == '1':
            user_text = input("\nType something: ").strip()
            if user_text:
                morse_result = convert_to_morse(user_text)
                print(f"\nHere's your morse code:\n{morse_result}")
            else:
                print("\nYou didn't type anything!")
        
        elif choice == '2':
            print("\nPaste your morse code below.")
            print("(Tip: Use spaces between characters, ' / ' between words)")
            morse_input = input("> ").strip()
            
            if morse_input:
                text_result = convert_to_text(morse_input)
                print(f"\nDecoded message:\n{text_result}")
            else:
                print("\nNo morse code entered!")
        
        elif choice == '3':
            print("\nThanks for using the translator. Bye!")
            break
        
        else:
            print("\nHmm, that's not a valid option. Try 1, 2, or 3.")


if __name__ == "__main__":
    main()