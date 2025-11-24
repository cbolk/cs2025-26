ALPHALEN = 26   # ord('z') - ord('a')

def caesar_cipher(word, shift):
    result = ""
    for char in word:
        if 'a' <= char <= 'z':
            # Convert character to a number (0-25)
            char_num = ord(char) - ord('a')
            # Shift
            shifted_num = (char_num + shift) % ALPHALEN + ord('a')
            # Convert back to character
            shifted_char = chr(shifted_num)
            result += shifted_char
        else:
            # If character is not in the alphabet, leave it unchanged
            result += char
    return result

# Get input from the user
word = input("Enter a word (lowercase letters only): ")
number = int(input("Enter a number to shift by: "))

# Call the function and print the result
encoded = caesar_cipher(word, number)
print("Encoded word:", encoded)
