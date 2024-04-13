# -*- coding: utf-8 -*-

# Dependencies

from secrets import choice
from typing import List, Dict

# Class Definition


class Transcriber(object):
    Mapper = {}

    def __init__(self, mapper: Dict[str, str]):
        """
        The function initializes a Transcriber object with a mapper dictionary.
        If the mapper is empty, a DeprecationWarning is raised indicating that
        creating an empty Transcriber doesn't make sense.

        Args:
          mapper (Dict[str, str]): A dictionary where both keys and values are strings.
            This dictionary is assigned to the `mapper` attribute of the class instance.
        """
        self.Mapper = mapper
        if not mapper:
            raise DeprecationWarning(
                "It makes no sense to create an empty Transcriber."
            )

    def Transcribe(self, text: str) -> str:
        """
        The `Transcribe` function takes a text input and replaces characters based on a mapping
        dictionary provided in `self.Mapper`.

        Args:
          text (str): The `Transcribe` method takes a `text` parameter as input, which is expected to be
        a string. The method then iterates over the keys in the `Mapper` dictionary (which is an
        attribute of the class instance) and replaces occurrences of those keys in the input `text` with

        Returns:
          The `Transcribe` method returns the text after replacing characters based on the mapping
        defined in `self.Mapper`.
        """
        for i in self.Mapper:
            text = text.replace(i, str(self.Mapper.get(i, i)))
        return text

    def ReverseTranscribe(self, text: str) -> str:
        """
        The function `ReverseTranscribe` takes a text string and replaces each occurrence of a value in
        a dictionary with its corresponding key, returning the modified text.

        Args:
          text (str): The `ReverseTranscribe` function takes a string `text` as input and performs a
        reverse transcription based on a mapping defined in `self.Mapper`. The function iterates over
        the values in the `Mapper` dictionary and replaces occurrences of those values in the input
        `text` with a randomly chosen key

        Returns:
          The `ReverseTranscribe` method is returning the reverse-transcribed version of the input
        `text` string. The method iterates over the values in the `Mapper` dictionary, and for each
        value found in the `text` string, it replaces it with a randomly chosen key from the `Mapper`
        dictionary that corresponds to that value. This process is repeated until all values in the
        `text`
        """
        for i in self.Mapper.values():
            while i in text:
                text = text.replace(
                    i, choice([j for j in self.Mapper.keys() if self.Mapper[j] == i]), 1
                )
        return text


class TranscriberUI(object):
    TranscriberList = []

    def __init__(self, transcriberList: List[Transcriber], style="auto"):
        self.TranscriberList = transcriberList


# Mapping
latinGreek = {
    "TH": "Θ",
    "Th": "Θ",
    "th": "θ",
    "A": "Α",
    "a": "α",
    "B": "Β",
    "b": "β",
    "C": "Ξ",
    "c": "ξ",
    "D": "Δ",
    "d": "δ",
    "E": "Ε",
    "e": "ε",
    "F": "Φ",
    "f": "φ",
    "G": "Γ",
    "g": "γ",
    "H": "Η",
    "h": "η",
    "I": "Ι",
    "i": "ι",
    "J": "Ψ",
    "j": "ψ",
    "K": "Κ",
    "k": "κ",
    "L": "Λ",
    "l": "λ",
    "M": "Μ",
    "m": "μ",
    "N": "Ν",
    "n": "ν",
    "O": "Ο",
    "o": "ο",
    "P": "Π",
    "p": "π",
    "Q": "Κ",
    "q": "κ",
    "R": "Ρ",
    "r": "ρ",
    "S": "Σ",
    "s": "σ",
    "T": "Τ",
    "t": "τ",
    "U": "Υ",
    "u": "υ",
    "V": "Ν",
    "v": "ν",
    "W": "Ω",
    "w": "ω",
    "X": "Χ",
    "x": "χ",
    "Y": "Υ",
    "y": "υ",
    "Z": "Ζ",
    "z": "ζ",
}

latinCyrillic = {
    "ZH": "Ж",
    "Zh": "Ж",
    "zh": "ж",
    "SH": "Ш",
    "Sh": "Ш",
    "sh": "ш",
    "CH": "Ч",
    "Ch": "Ч",
    "ch": "ч",
    "TS": "Ц",
    "Ts": "Ц",
    "ts": "ц",
    "YU": "Ю",
    "Yu": "Ю",
    "yu": "ю",
    "YA": "Я",
    "Ya": "Я",
    "ya": "я",
    "KH": "Х",
    "Kh": "Х",
    "kh": "х",
    "SHCH": "Щ",
    "Shch": "Щ",
    "shch": "щ",
    "Q": "КУ",
    "q": "ку",
    "A": "А",
    "a": "а",
    "B": "Б",
    "b": "б",
    "C": "С",
    "c": "с",
    "D": "Д",
    "d": "д",
    "E": "Е",
    "e": "е",
    "F": "Ф",
    "f": "ф",
    "G": "Г",
    "g": "г",
    "H": "Х",
    "h": "х",
    "I": "И",
    "i": "и",
    "J": "Й",
    "j": "й",
    "K": "К",
    "k": "к",
    "L": "Л",
    "l": "л",
    "M": "М",
    "m": "м",
    "N": "Н",
    "n": "н",
    "O": "О",
    "o": "о",
    "P": "П",
    "p": "п",
    # 'Q': 'КУ', 'q': 'ку',
    "R": "Р",
    "r": "р",
    "S": "С",
    "s": "с",
    "T": "Т",
    "t": "т",
    "U": "У",
    "u": "у",
    "V": "В",
    "v": "в",
    "W": "В",
    "w": "в",
    "X": "Х",
    "x": "х",
    "Y": "Ы",
    "y": "ы",
    "Z": "З",
    "z": "з",
}

latinArabic = {
    "A": "أ",
    "a": "أ",
    "B": "ب",
    "b": "ب",
    "C": "ج",
    "c": "ج",
    "D": "د",
    "d": "د",
    "E": "ه",
    "e": "ه",
    "F": "و",
    "f": "و",
    "G": "ز",
    "g": "ز",
    "H": "ح",
    "h": "ح",
    "I": "ط",
    "i": "ط",
    "J": "ي",
    "j": "ي",
    "K": "ك",
    "k": "ك",
    "L": "ل",
    "l": "ل",
    "M": "م",
    "m": "م",
    "N": "ن",
    "n": "ن",
    "O": "س",
    "o": "س",
    "P": "ع",
    "p": "ع",
    "Q": "ق",
    "q": "ق",
    "R": "ر",
    "r": "ر",
    "S": "س",
    "s": "س",
    "T": "ت",
    "t": "ت",
    "U": "ؤ",
    "u": "ؤ",
    "V": "ث",
    "v": "ث",
    "W": "و",
    "w": "و",
    "X": "خ",
    "x": "خ",
    "Y": "ي",
    "y": "ي",
    "Z": "ز",
    "z": "ز",
}

latinHebrew = {
    "X": "קס",
    "x": "קס",
    "A": "א",
    "a": "א",
    "B": "ב",
    "b": "ב",
    "C": "ג",
    "c": "ג",
    "D": "ד",
    "d": "ד",
    "E": "ה",
    "e": "ה",
    "F": "ו",
    "f": "ו",
    "G": "ז",
    "g": "ז",
    "H": "ח",
    "h": "ח",
    "I": "י",
    "i": "י",
    "J": "י",
    "j": "י",
    "K": "כ",
    "k": "כ",
    "L": "ל",
    "l": "ל",
    "M": "מ",
    "m": "מ",
    "N": "נ",
    "n": "נ",
    "O": "ו",
    "o": "ו",
    "P": "פ",
    "p": "פ",
    "Q": "ק",
    "q": "ק",
    "R": "ר",
    "r": "ר",
    "S": "ס",
    "s": "ס",
    "T": "ת",
    "t": "ת",
    "U": "ו",
    "u": "ו",
    "V": "ו",
    "v": "ו",
    "W": "ו",
    "w": "ו",
    # 'X': 'קס', 'x': 'קס',
    "Y": "י",
    "y": "י",
    "Z": "ז",
    "z": "ז",
}

latinSanskrit = {
    "A": "अ",
    "a": "अ",
    "B": "ब",
    "b": "ब",
    "C": "च",
    "c": "च",
    "D": "द",
    "d": "द",
    "E": "ए",
    "e": "ए",
    "F": "फ",
    "f": "फ",
    "G": "ग",
    "g": "ग",
    "H": "ह",
    "h": "ह",
    "I": "इ",
    "i": "इ",
    "J": "ज",
    "j": "ज",
    "K": "क",
    "k": "क",
    "L": "ल",
    "l": "ल",
    "M": "म",
    "m": "म",
    "N": "न",
    "n": "न",
    "O": "ओ",
    "o": "ओ",
    "P": "प",
    "p": "प",
    "Q": "क्",
    "q": "क्",
    "R": "र",
    "r": "र",
    "S": "स",
    "s": "स",
    "T": "त",
    "t": "त",
    "U": "उ",
    "u": "उ",
    "V": "व",
    "v": "व",
    "W": "व",
    "w": "व",
    "X": "क्स",
    "x": "क्स",
    "Y": "य",
    "y": "य",
    "Z": "ज",
    "z": "ज",
}

latinTibetan = {
    "A": "ཨ",
    "a": "ཨ",
    "B": "བ",
    "b": "བ",
    "C": "ཀ",
    "c": "ཀ",
    "D": "ད",
    "d": "ད",
    "E": "ཾ",
    "e": "ཾ",
    "F": "ཕ",
    "f": "ཕ",
    "G": "ག",
    "g": "ག",
    "H": "ཧ",
    "h": "ཧ",
    "I": "ཨ",
    "i": "ཨ",
    "J": "ཇ",
    "j": "ཇ",
    "K": "ཀ",
    "k": "ཀ",
    "L": "ལ",
    "l": "ལ",
    "M": "མ",
    "m": "མ",
    "N": "ན",
    "n": "ན",
    "O": "ཨ",
    "o": "ཨ",
    "P": "པ",
    "p": "པ",
    "Q": "ཁ",
    "q": "ཁ",
    "R": "ར",
    "r": "ར",
    "S": "ས",
    "s": "ས",
    "T": "ཏ",
    "t": "ཏ",
    "U": "ཨ",
    "u": "ཨ",
    "V": "ཝ",
    "v": "ཝ",
    "W": "ဝ",
    "w": "ဝ",
    "X": "ཁ",
    "x": "ཁ",
    "Y": "ཡ",
    "y": "ཡ",
    "Z": "ཛ",
    "z": "ཛ",
}


# Define Default Transcribers

LatinGreekTranscriber = Transcriber(latinGreek)
LatinCyrillicTranscriber = Transcriber(latinCyrillic)
LatinArabicTranscriber = Transcriber(latinArabic)
LatinHebrewTranscriber = Transcriber(latinHebrew)
LatinSanskritTranscriber = Transcriber(latinSanskrit)
LatinTibetanTranscriber = Transcriber(latinTibetan)
DefaultTranscribers = [
    LatinGreekTranscriber,
    LatinCyrillicTranscriber,
    LatinArabicTranscriber,
    LatinHebrewTranscriber,
    LatinSanskritTranscriber,
    LatinTibetanTranscriber,
]

# Mainloop: Interactive Shell

if __name__ == "__main__":
    print("Welcome to CrazyTranscription!")
    print("Version 2.2.1.2 (Arctic Wolf), made with love by Shining Yang")
    print(
        "Visit https://github.com/ShiningYangYXN/CrazyTranscription for project updates."
    )
    while True:
        mode = ""
        print("Please select a mode:")
        print("    [1] Transcription")
        print("    [2] Reverse Transcription")
        print("    [#] Exit")
        mode = input("Mode: ")
        if mode == "1":
            mode = ""
            modeNames = {
                "1": "Greek",
                "2": "Cyrillic",
                "3": "Arabic",
                "4": "Hebrew",
                "5": "Sanskrit",
                "6": "Tibetan",
            }
            while mode != "#":
                print("Transcription mode. Please select a target:")
                print("    [1] Latin to Greek")
                print("    [2] Latin to Cyrillic")
                print("    [3] Latin to Arabic")
                print("    [4] Latin to Hebrew")
                print("    [5] Latin to Sanskrit")
                print("    [6] Latin to Tibetan")
                print("    [#] Exit")
                mode = input("Mode: ")
                if mode in ["1", "2", "3", "4", "5", "6"]:
                    selectedTranscriber = DefaultTranscribers[int(mode) - 1]
                    text = ""
                    print(
                        f"Latin to {modeNames[mode]} Mode selected. Type '#' to exit."
                    )
                    while text != "#":
                        text = input("Input your text to be transcribed:\n")
                        print(f"---BEGIN {modeNames[mode].upper()} TRANSCRIPTION---")
                        print(selectedTranscriber.Transcribe(text))
                        print(f"---END {modeNames[mode].upper()} TRANSCRIPTION---")
                    print("OK,thanks. Goodbye.")
                elif mode == "#":
                    print("OK,thanks. Goodbye.")
                else:
                    print("Invalid input. Please try again.")

        elif mode == "2":
            print("Reverse Transcription Mode. Type'#' to exit.")
            text = ""
            while text != "#":
                text = input("Input your text to be reverse transcribed:\n")
                print("---BEGIN REVERSE TRANSCRIPTION---")
                for t in DefaultTranscribers:
                    text = t.ReverseTranscribe(text)
                print(text)
                print("---END REVERSE TRANSCRIPTION---")
        elif mode == "#":
            print("OK,thanks. Goodbye.")
            break
        else:
            print("Invalid input. Please try again.")
