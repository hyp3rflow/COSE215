import re


def SSN_find(text):
    SSN = re.compile(
        "\\s((98 | 99 | 01)\
                (([0][13578] | [1][02])([0][1-9] | [12][0-9] | [3][01])\
                | ([0][469] | (11))([0][1-9] | [12][0-9] | (30))\
                | ((02)([0][1-9] | [1][0-9] | [2][0-8])))\
            | (00)\
                (([0][13578] | [1][02])([0][1-9] | [12][0-9] | [3][01])\
                | ([0][469] | (11))([0][1-9] | [12][0-9] | (30))\
                | ((02)([0][1-9] | [1][0-9] | [2][0-9]))))\
            [-][1-4]\\d{6}\\s", re.VERBOSE)

    # 1 3 5 7 8 10 12
    result = SSN.findall(text)
    return len(result)


def Email_find(text):
    Email = re.compile("\\s[0-9a-zA-Z]+[@][a-zA-Z]+(\\.ac\\.kr)\\s")

    result = Email.findall(text)
    return len(result)


if __name__ == "__main__":
    '''
    while True:
        data = input()

        print(SSN_find(data))
    '''

    f = open('./Assignment/classifier_IO.txt')
    data = f.read()

    print(SSN_find(data))
    print(Email_find(data))

    f.close()
