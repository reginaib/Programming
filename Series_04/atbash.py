plaintext = input()

cybertext = ''

for character in plaintext:
    if character.isalpha():
        if character.islower():
            cybertext += chr(ord('z') - (ord(character) - ord('a')))
        else:
            cybertext += chr(ord('Z') - (ord(character) - ord('A')))

    else:
        cybertext += character

print(cybertext)
