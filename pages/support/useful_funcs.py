import string
import platform 

def caesar(plaintext, shift):
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    print(shifted_alphabet)
    table = str.maketrans(alphabet, shifted_alphabet)
    return plaintext.translate(table)

def tax(x):
    if x <= 18_200:
        return 0
    elif 18_201 <= x <= 45_000:
        return 0.19*(x-18_200)
    elif 45_001 <= x <= 120_000:
        return 5_092 + 0.325*(x-45_000)
    elif 120_001 <= x <= 180_000:
        return 29_467 + 0.37*(x-120_000)
    elif 180_001 <= x:
        return 51_667 + 0.45*(x-180_000)

def hecs(x):
    if x < 48_361:
        return 0
    elif 48_361 <= x <= 55_836:
        return x* 0.01
    elif 55_837 <= x <= 59_186:
        return x* 0.02
    elif 59_187 <= x <= 62_738:
        return x* 0.025
    elif 62_739 <= x <= 66_502:
        return x* 0.03
    elif 66_503 <= x <= 70_492:
        return x* 0.035
    elif 70_493 <= x <= 74_722:
        return x* 0.04
    elif 74_723 <= x <= 79_206:
        return x* 0.045
    elif 79_207 <= x <= 83_958:
        return x* 0.05
    elif 83_959 <= x <= 88_996:
        return x* 0.055
    elif 88_997 <= x <= 94_336:
        return x* 0.06
    elif 94_337 <= x <= 99_996:
        return x* 0.065
    elif 99_997 <= x <= 105_996:
        return x * 0.07
    elif 105_997 <= x <= 112_355:
        return x* 0.075
    elif 112_356 <= x <= 119_097:
        return x* 0.08
    elif 119_098 <= x <= 126_243:
        return x* 0.085
    elif 126_244 <= x <= 133_818:
        return x* 0.09
    elif 133_819 <= x <= 141_847:
        return x* 0.095
    elif 141_848 <= x:
        return x * 0.1

def encrypt(x):

    letters = list(string.ascii_uppercase)

    lookup = {letters[i] : i+1 for i in range(len(letters))}

    name = platform.node().upper()

    shift_val = sum(lookup[l] for l in name)

    output = caesar(x,shift_val)

    return output

print(encrypt('hi'))











