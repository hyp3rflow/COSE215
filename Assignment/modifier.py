import re


def SSN_modifier(text):
    text = " " + text + " "
    SSN = re.compile(
        "\\s(?P<open>((98 | 99 | 01)\
                (([0][13578] | [1][02])([0][1-9] | [12][0-9] | [3][01])\
                | ([0][469] | (11))([0][1-9] | [12][0-9] | (30))\
                | ((02)([0][1-9] | [1][0-9] | [2][0-8])))\
            | (00)\
                (([0][13578] | [1][02])([0][1-9] | [12][0-9] | [3][01])\
                | ([0][469] | (11))([0][1-9] | [12][0-9] | (30))\
                | ((02)([0][1-9] | [1][0-9] | [2][0-9]))))\
            [-][1-4])\\d{6}\\s", re.VERBOSE)

    if bool(SSN.match(text)):
        print(re.sub(SSN, '\g<open>XXXXXX', text))


def email_modifier(text):
    text = " " + text + " "
    email = re.compile(
        "\\s(?P<id>[0-9a-zA-Z]+[@])[a-zA-Z]+(?P<footer>\\.ac\\.kr)\\s")

    if bool(email.match(text)):
        print(re.sub(email, '\g<id>XXXX\g<footer>', text))


if __name__ == "__main__":
    f = open("./Assignment/classifier_IO.txt")
    data = f.read()

    data = data.split(" ")

    for word in data:
        SSN_modifier(word)
        email_modifier(word)

    f.close()
