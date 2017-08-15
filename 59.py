from __future__ import print_function
from string import ascii_lowercase


def main(encrypted_codes):
    for char_0 in ascii_lowercase:
        for char_1 in ascii_lowercase:
            for char_2 in ascii_lowercase:
                decryption_key_codes = [ord(char_0), ord(char_1), ord(char_2)]
                decrypted_codes = [
                    encrypted_codes[i] ^ decryption_key_codes[i % 3]
                    for i in range(len(encrypted_codes))
                ]
                decrypted_message = ''.join(chr(o) for o in decrypted_codes)

                # Must have words
                if not ' ' in decrypted_message:
                    continue

                # By trialing different words here, eventually discovered the message is a bible verse or something
                if 'The Gospel of John' in decrypted_message:
                    return decrypted_message


with open('p059_cipher.txt', 'r') as f:
    encrypted_codes = [int(c) for c in f.readline().strip().split(',')]
message = main(encrypted_codes)
print(sum(ord(c) for c in message))
