# Corinne Dumais, Jérémi Lesage
# Mr & Mrs Curie

import string

alphabet = dict(zip(string.ascii_uppercase, range(0, 26)))
alphabet_reverse = dict(zip(range(0, 26), string.ascii_uppercase))

message = '''NRUWJXXNAJ BTWP GZY YMJ HFJXFW HNUMJW NX STY XJHZWJ JSTZLM KTW HQFXXNKNJI
YWFSXRNXXNTSX
YMJ WJFQ RJXXFLJ NX NSHQZIJI GJQTB FSI BFX JSHWDUYJI ZXNSL F ANLSJWJ HNUMJW BNYM PJDBTWI
MFHPFYMTS
VZZI PGPWAZL AWNQ YXKEFNT NQ ZHL OQHHXGRBWP YLT MCQ BK QSJGDNFBGZ SVI YFQ VGAQLHY
RTBFS JCTW'''

for step in range(27):
    print(step)
    deciphered_message = []
    for car in message:
        if car == ' ':
            deciphered_message.append(' ')

        elif car == '\n':
            deciphered_message.append('\n')

        else:
            number = alphabet[car]
            number += step
            new_letter = alphabet_reverse[number % 26]
            deciphered_message.append(new_letter)

    print("".join(deciphered_message))
    print()
    print()

# The step used for encryption is 21

# IMPRESSIVE WORK BUT THE CAESAR CIPHER IS NOT SECURE ENOUGH FOR CLASSIFIED
# TRANSMISSIONS
# THE REAL MESSAGE IS INCLUDED BELOW AND WAS ENCRYPTED USING A VIGNERE CIPHER WITH KEYWORD
# HACKATHON

super_secret_message = '''QUUDKBKRVUGVRILTSFZAIOILUCGJLCCSBMWRKTGOHXLWFLNEBYIAWBUNQDTALQBVLGCTMOWANEXOR'''


def vignere_decoding(message, key):
    """
    Function used to decipher a message encrypted with Vignere encryption
    """
    decoded_message = ""

    for index in range(len(message)):

        if index >= len(key):
            index_cle = index % len(key)
            difference = (alphabet[message[index]] - alphabet[key[index_cle]])

        else:
            difference = (alphabet[message[index]] - alphabet[key[index]])

        if difference < 0:
            difference = difference % 26

        decoded_message += alphabet_reverse[difference]

    return decoded_message


print(vignere_decoding(super_secret_message, 'HACKATHON'))

# JUST KIDDING THIS MESSAGE IS NOT CLASSIFIED TEEHEE IS ENCRYPTION NOT THE COOLEST THING EVER
