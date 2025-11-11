def caesar_cipher(word, shift):
    ALPHABET = "abcdefghijklmnopqrstuvwxyz"
    ALPHALEN = len(ALPHABET)
    result = ""

    for char in word:
        # Find the index of the character 
        i = 0
        while i < ALPHALEN and ALPHABET[i] != char:
            i += 1

        if i < ALPHALEN:
            # Apply the shift and wrap around
            shifted_i = (i + shift) % ALPHALEN
            result += ALPHABET[shifted_i]
        else:
            # If character is not in the alphabet, leave it unchanged
            result += char

    return result

# Get input from the user
word = input("Enter a word: ").lower()
number = int(input("Enter a number to shift by: "))

# Call the function and print the result
encoded = caesar_cipher(word, number)
print("Encoded word:", encoded)
