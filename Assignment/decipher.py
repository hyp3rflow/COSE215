import re

morse_code = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",

    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",

    "&": ".-...",
    "'": ".----.",
    "@": ".--.-.",
    ")": "-.--.-",
    "(": "-.--.",
    ":": "---...",
    ",": "--..--",
    "=": "-...-",
    "!": "-.-.--",
    ".": ".-.-.-",
    "-": "-....-",
    "+": ".-.-.",
    '"': ".-..-.",
    "?": "..--..",
    "/": "-..-.",
}


def str2pattern(string):
    result = "\\s"
    prev = string[0]
    cnt = 1
    for curr in string[1:]:
        if prev == curr:
            cnt += 1
        else:
            if cnt == 1:
                result += f"[{prev}]"
            else:
                result += f"[{prev}]{{{cnt}}}"
            prev = curr
            cnt = 1

    if cnt == 1:
        result += f"[{prev}]"
    else:
        result += f"[{prev}]{{{cnt}}}"

    return result + "(?=\\s)"


morse_pattern = {re.compile(str2pattern(v)): k for k, v in morse_code.items()}


def morse_decipher(text):
    result = f" {text} "

    for (pattern, value) in morse_pattern.items():
        result = pattern.sub(f' {value} ', result)

    return result


if __name__ == "__main__":
    while True:
        data = input()
        result = morse_decipher(data)
        print(str.lower(result.replace(" ", "")))
