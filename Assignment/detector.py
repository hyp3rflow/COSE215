import re


def cellphone_detector(text):
    cellphone = re.compile("\\s(010)[-]\\d{4}[-]\\d{4}\\s")

    result = re.findall(cellphone, text)
    return(len(result))


def card_detector(text):
    card = re.compile("\\s\\d{4}[-]\\d{4}[-]\\d{4}[-]\\d{4}\\s")

    result = re.findall(card, text)
    return(len(result))


if __name__ == "__main__":
    f = open('./Assignment/classifier_IO.txt')

    data = f.read()

    print(cellphone_detector(data))
    print(card_detector(data))
