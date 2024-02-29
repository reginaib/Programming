def rotation(letter, n):
    
    """
    Returns the letter that results after a rotation over 
    n positions to the right.
    """
    
    if letter.isalpha():
        ref = ord('a') if letter.islower() else ord('A')            
        return chr((ord(letter) - ref + n) % 26 + ref)
    else:
        return letter
    
def encode(sentence, n):
    
    """
    Returns the encrypted sentence that results after 
    performing a Caesar rotation over n positions.
    """
    
    return ''.join(rotation(letter, n) for letter in sentence)

def decode(sentence, n):
    
    """
    Returns the plain text of a given sentence that is
    encrypted according to a Caesar rotation over n positions.
    """
    
    return encode(sentence, -n)

# read number of rotation positions and encrypted sentence
n, sentence = int(input()), input()

# compute and print plain text sentence
print(decode(sentence, n))