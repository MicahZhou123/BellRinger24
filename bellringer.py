def caesar_cipher_encoder(text):
    shift = 15
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encoded_text = ""

    for char in text: # "char" checks every character
        if char.isalpha():  # if the character is a letter
            char = char.lower()  
            current_index = alphabet.index(char)  # find pos
            new_index = (current_index + shift) % 26  
            new_char = alphabet[new_index]  # new_char defines the new index that was shifted by 15 and it is added to the conded text
            encoded_text += new_char
        else:
            encoded_text += char

    return encoded_text

text = input("Enter the text you want to encode: ")

encoded_message = caesar_cipher_encoder(text)

print("Encoded message:", encoded_message)
