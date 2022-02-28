# English to morse data 
from typing import List

ENGLISH_TO_MORSE = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
                    'H': '....',
                    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
                    'P': '.--.',
                    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--',
                    'X': '-..-',
                    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
                    '4': '....-',
                    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': ' '}

# Creating the english to morse dictionary
MORSE_TO_ENGLISH = dict()
for key in ENGLISH_TO_MORSE:
    MORSE_TO_ENGLISH[ENGLISH_TO_MORSE[key]] = key


# Encrypt
def encrpyt(english_str: str):
    datas: List[str] = [alphabet for alphabet in english_str.upper()]
    morse_data = str()  # to store the morse code
    for data in datas:
        morse_data += ENGLISH_TO_MORSE[data]
    return morse_data


# Decrypt - Creating  morse to english dictionary
def decrypt(morse_str: str):
    # after each alphabet give a space
    morse_str = morse_str.split()
    english_str = str()
    for morse_data in morse_str:
        english_str += MORSE_TO_ENGLISH[morse_data]
    return english_str


if __name__ == '__main__':
    while True:
        # User input
        print('''_____________MORSE CODE CONVERTER________________
    1) ENCRYPT : CONVERT TEXT TO MORSE CODE 
    2) DECRYPT : CONVERT MORSE CODE TO TEXT [ADD SPACE AFTER EACH ALPHABET]
    3) EXIT   
        ''')
        user_input = input('>> ').upper().strip()

        # Text to morse code
        if user_input == 'ENCRYPT':
            data = input('\nEnter the String:\n>> ')
            print(encrpyt(english_str=data))

        # Morse to Text code
        elif user_input == 'DECRYPT':
            datas = input('\nEnter the Code:\tAfter each entry keep a space\n>> ')
            decrypted_value = str()
            for data in datas.split():
                decrypted_value += decrypt(morse_str=data)
            print(decrypted_value)

        # Exit
        elif user_input == 'EXIT':
            print('Closing the program......................')
            break

        else:
            print('Wrong Input!!!')
