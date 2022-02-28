ENGLISH_TO_MORSE = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
                    'H': '....',
                    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
                    'P': '.--.',
                    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--',
                    'X': '-..-',
                    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
                    '4': '....-',
                    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': ' '}

MORSE_TO_ENGLISH = dict()

for key in ENGLISH_TO_MORSE:
    MORSE_TO_ENGLISH[ENGLISH_TO_MORSE[key]] = key


# Encrypt
def encrpyt(english_str: str):
    datas = [alphabet for alphabet in english_str.upper()]
    morse_data = str()  # to store the morse code
    for data in datas:
        morse_data += ENGLISH_TO_MORSE[data]
    return morse_data


# Decrypt
def decrpyt(morse_str: str):
    # Creating  morse to english dictionary
    # after each alphabet give a space
    morse_str = morse_str.split()
    english_str = str()
    for morse_data in morse_str:
        english_str += MORSE_TO_ENGLISH[morse_data]
    return english_str


if __name__ == '__main__':
    print(encrpyt(english_str='My name is Nilay'))
    print(decrpyt(morse_str='-- -.--'))
