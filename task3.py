import string

def generate_playfair_matrix(keyword):
    keyword = keyword.lower().replace("j", "i")
    seen = set()
    matrix = []
    
    for char in keyword + string.ascii_lowercase:
        if char not in seen and char != 'j':
            seen.add(char)
            matrix.append(char)
    
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def find_position(matrix, letter):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == letter:
                return row, col

def encrypt_pair(matrix, a, b):
    row1, col1 = find_position(matrix, a)
    row2, col2 = find_position(matrix, b)
    
    if row1 == row2:
        return matrix[row1][(col1+1) % 5] + matrix[row2][(col2+1) % 5]
    elif col1 == col2:
        return matrix[(row1+1) % 5][col1] + matrix[(row2+1) % 5][col2]
    else:
        return matrix[row1][col2] + matrix[row2][col1]

def decrypt_pair(matrix, a, b):
    row1, col1 = find_position(matrix, a)
    row2, col2 = find_position(matrix, b)
    
    if row1 == row2:
        return matrix[row1][(col1-1) % 5] + matrix[row2][(col2-1) % 5]
    elif col1 == col2:
        return matrix[(row1-1) % 5][col1] + matrix[(row2-1) % 5][col2]
    else:
        return matrix[row1][col2] + matrix[row2][col1]

def prepare_text(text):
    text = text.lower().replace("j", "i")
    text = ''.join(filter(str.isalpha, text))
    prepared = ""
    i = 0
    while i < len(text):
        if i == len(text) - 1 or text[i] == text[i + 1]:
            prepared += text[i] + "x"
            i += 1
        else:
            prepared += text[i] + text[i + 1]
            i += 2
    return prepared

def encrypt(text, matrix):
    text = prepare_text(text)
    return ''.join(encrypt_pair(matrix, text[i], text[i+1]) for i in range(0, len(text), 2))

def decrypt(text, matrix):
    return ''.join(decrypt_pair(matrix, text[i], text[i+1]) for i in range(0, len(text), 2))

if __name__ == "__main__":
    keyword = input("Enter the keyword: ")
    matrix = generate_playfair_matrix(keyword)
    for row in matrix:
        print(" ".join(row))
    
    choice = input("Do you want to (e)ncrypt or (d)ecrypt? ").lower()
    text = input("Enter the text: ")
    
    if choice == "e":
        print("Encrypted text:", encrypt(text, matrix))
    elif choice == "d":
        print("Decrypted text:", decrypt(text, matrix))