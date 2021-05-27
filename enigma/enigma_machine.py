"""
Enigma Machine
"""

from typing import List, Optional, Tuple

import string


class Rotor:
    """ Rotor """

    def __init__(
        self,
        name: str,
        wiring: str,
        turnover: List[str],
        starting_position: str,
    ) -> None:
        self.name = name
        self.wiring = wiring
        self.turnover = turnover
        self.position = starting_position[0]
        self.toggle_turnover = False

    def encode_in(self, c: str, turnover: bool) -> Tuple[str, bool]:
        """ encode_in """

        encoded = self.wiring[
            (string.ascii_lowercase.index(c.lower()) + ord(self.position) - ord("A")) % 26
        ]

        toggle_turnover = False
        if turnover:
            self.toggle_turnover = True
            if self.position in self.turnover:
                toggle_turnover = True


        # print(f"{self.name}: {c} -> {encoded}")
        return (encoded, toggle_turnover)

    def encode_out(self, c: str) -> str:
        """ encode_out """

        encoded = chr((self.wiring.index(c)-(ord(self.position) - ord("A")))%26+ord("A"))

        # print(f"{self.name}: {c} -> {encoded}")
        return encoded

    def do_turnover(self) -> None:
        """ do_turnover """

        if self.toggle_turnover:
            self.position = chr((((ord(self.position) + 1) - ord("A")) % 26) + ord("A"))
            self.toggle_turnover = False


class Reflector:
    """ Reflector """

    def __init__(
        self,
        name: str,
        wiring: str,
    ) -> None:
        self.name = name
        self.wiring = wiring

    def encode(self, c: str) -> str:
        """ encode """

        encoded = self.wiring[
            string.ascii_lowercase.index(c.lower())
        ]

        # print(f"{self.name}: {c} -> {encoded}")
        return encoded


ROTORS = {
    "I": Rotor("I", "EKMFLGDQVZNTOWYHXUSPAIBRCJ", ["Q"], "A"),
    "II": Rotor("II", "AJDKSIRUXBLHWTMCQGZNPYFVOE", ["E"], "A"),
    "III": Rotor("III", "BDFHJLCPRTXVZNYEIWGAKMUSQO", ["V"], "A"),
    "IV": Rotor("IV", "ESOVPZJAYQUIRHXLNFTGKDCMWB", ["J"], "A"),
    "V": Rotor("V", "VZBRGITYUPSDNHLXAWMJQOFECK", ["Z"], "A"),
    "VI": Rotor("VI", "JPGVOUMFYQBENHZRDKASXLICTW", ["Z", "M"], "A"),
    "VII": Rotor("VII", "NZJHGRCXMYSWBOUFAIVLPEKQDT", ["Z", "M"], "A"),
    "VIII": Rotor("VIII", "FKQHTLXOCBJSPDZRAMEWNIUYGV", ["Z", "M"], "A"),
}

REFLECTORS = {
    "Beta": Reflector("Beta", "LEYJVCNIXWPBQMDRTAKZGFUHOS"),
    "Gamma": Reflector("Gamma", "FSOKANUERHMBTIYCWLQPZXVGJD"),
    "A": Reflector("A", "EJMZALYXVBWFCRQUONTSPIKHGD"),
    "B": Reflector("B", "YRUHQSLDPXNGOKMIEBFZCWVJAT"),
    "C": Reflector("C", "FVPJIAOYEDRZXWGCTKUQSBNMHL"),
    "BT": Reflector("BT", "ENKQAUYWJICOPBLMDXZVFTHRGS"),
    "CT": Reflector("CT", "RDOBJNTKVEHMLFCWZAXGYIPSUQ"),
    "ETW": Reflector("ETW", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
}


class Enigma:
    """ Enigma """

    def __init__(
        self,
        rotors: List[str],
        reflector: str,
    ) -> None:
        self.rotors: List[Rotor] = []
        for rotor in rotors:
            self.rotors.append(ROTORS[rotor])
        self.reflector = REFLECTORS[reflector]

    def encode(self, raw_string: str) -> Optional[str]:
        """ encode """
        encoded_string = ""
        for c in raw_string:
            if c.isalpha():
                encoded = c
                # print()

                turnover = True
                for rotor in self.rotors:
                    (encoded, turnover) = rotor.encode_in(encoded, turnover)

                encoded = self.reflector.encode(encoded)

                for rotor in reversed(self.rotors):
                    encoded = rotor.encode_out(encoded)

                for rotor in self.rotors:
                    rotor.do_turnover()

                # for rotor in self.rotors:
                #     print(f"{rotor.name}:{rotor.position} ", end="")
                # print()

                encoded_string += encoded

        return encoded_string
