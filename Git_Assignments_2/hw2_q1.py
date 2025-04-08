import os
from pathlib import Path

MORSE_CODE = {'A': '.-',     'B': '-...',   'C': '-.-.',
              'D': '-..',    'E': '.',      'F': '..-.',
              'G': '--.',    'H': '....',   'I': '..',
              'J': '.---',   'K': '-.-',    'L': '.-..',
              'M': '--',     'N': '-.',     'O': '---',
              'P': '.--.',   'Q': '--.-',   'R': '.-.',
              'S': '...',    'T': '-',      'U': '..-',
              'V': '...-',   'W': '.--',    'X': '-..-',
              'Y': '-.--',   'Z': '--..',

              '0': '-----',  '1': '.----',  '2': '..---',
              '3': '...--',  '4': '....-',  '5': '.....',
              '6': '-....',  '7': '--...',  '8': '---..',
              '9': '----.',

              '.': '.-.-.-', ',': '--..--', ':': '---...',
              "'": '.----.', '-': '-....-',
              }


def english_to_morse(
    input_file: str = "lorem.txt",
    output_file: str = "lorem_morse.txt"
):
    """Convert an input text file to an output Morse code file.

    Notes
    -----
    This function assumes the existence of a MORSE_CODE dictionary, containing a
    mapping between English letters and their corresponding Morse code.

    Parameters
    ----------
    input_file : str
        Path to file containing the text file to convert.
    output_file : str
        Name of output file containing the translated Morse code. Please don't change
        it since it's also hard-coded in the tests file.
    """
    # Read the input file
    with open(input_file, "r") as f:
        text = f.read()

    # Convert to uppercase and translate to Morse code
    morse_code = ' '.join(MORSE_CODE[char] for char in text.upper() if char in MORSE_CODE)

    # Write the Morse code to the output file
    with open(output_file, "w") as f:
        f.write(morse_code)

if __name__ == "__main__":
    os.chdir(Path(__file__).parent)
    input_file = 'lorem.txt'
    with open(input_file, 'r') as file:
        text = file.read()

    # print("Original text:")
    # print(text)
    output_file = 'lorem_morse.txt'
    # print("\nMorse code:")
    english_to_morse(input_file, output_file)