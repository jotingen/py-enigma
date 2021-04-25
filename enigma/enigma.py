"""
Enigma emulator

Type in message, get out encoded
Type in encoded, get out message

"""

import readchar # type: ignore

from .enigma_machine import Enigma


def main() -> None:
    """ main """

    e = Enigma()

    while True:
        char = readchar.readchar()
        # Handle traps
        if char in ("\x03", "\x04", "\x1a"):
            return
        # Handle newline
        elif char in ("\x0a", "\x0d"):
            print(char, flush=True)
        # Encode
        else:
            print(e.encode(char), end="", flush=True)


if __name__ == "__main__":
    main()
