import string
from collections import Counter

def frequency_analysis(ciphertext):
    letter_frequencies = {
        'e': 12.7, 't': 9.1, 'a': 8.2, 'o': 7.5, 'i': 7.0, 'n': 6.7, 's': 6.3,
        'h': 6.1, 'r': 6.0, 'd': 4.3, 'l': 4.0, 'c': 2.8, 'u': 2.8, 'm': 2.4,
        'w': 2.4, 'f': 2.2, 'g': 2.0, 'y': 2.0, 'p': 1.9, 'b': 1.5, 'v': 1.0,
        'k': 0.8, 'j': 0.2, 'x': 0.2, 'q': 0.1, 'z': 0.1
    }
    
    ciphertext = ciphertext.lower()
    counter = Counter(filter(str.isalpha, ciphertext))
    sorted_ciphertext_letters = [pair[0] for pair in counter.most_common()]
    sorted_english_letters = sorted(letter_frequencies, key=letter_frequencies.get, reverse=True)
    
    decryption_map = str.maketrans(''.join(sorted_ciphertext_letters), ''.join(sorted_english_letters))
    return ciphertext.translate(decryption_map)

if __name__ == "__main__":
    encrypted_message = input("Enter the encrypted message: ")
    decrypted_message = frequency_analysis(encrypted_message)
    
    print("Most likely decrypted text:")
    print(decrypted_message)
