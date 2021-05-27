"""
Enigma emulator

Type in message, get out encoded
Type in encoded, get out message

"""

import readchar  # type: ignore

from .enigma_machine import Enigma


def main() -> None:
    """ main """

    #e = Enigma(["I","II","III","IV"], "CT")
    e = Enigma(["I"], "CT")

    while True:
        char = readchar.readchar()
        #alpha characters
        if char.isalpha():
            print(e.encode(char.upper()), end="", flush=True)
        # Handle traps
        elif char in ("\x03", "\x04", "\x1a"):
            return
        # Handle newline
        elif char in ("\x0a", "\x0d"):
            print(char, flush=True)


if __name__ == "__main__":
    main()
