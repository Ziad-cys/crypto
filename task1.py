import itertools
import string

def decrypt(ciphertext, key):
    alphabet = string.ascii_lowercase
    key_map = str.maketrans(key, alphabet)
    return ciphertext.translate(key_map)

def brute_force_decrypt(ciphertext):
    alphabet = string.ascii_lowercase
    possible_decryptions = []
    
    for perm in itertools.permutations(alphabet):
        key = ''.join(perm)
        decrypted_text = decrypt(ciphertext, key)
        possible_decryptions.append(decrypted_text)
    
    return possible_decryptions

if __name__ == "__main__":
    encrypted_message = input("Enter the encrypted message: ").lower()
    results = brute_force_decrypt(encrypted_message)
    
    print("Possible decrypted texts:")
    for text in results[:10]:  # Show top 10 results
        print(text)
