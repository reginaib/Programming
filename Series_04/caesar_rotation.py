plaintext = 'VENI, VIDI, VICI'
rotation = 3

cybertext = ''
for character in plaintext:
    if character.isalpha():
        # calculate the new character after applying the Caesar cipher
        cybertext += chr((ord(character) - ord('A') + rotation) % 26
                         + ord('A'))
    else:
        cybertext += character

print(cybertext)
