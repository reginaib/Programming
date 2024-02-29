def toothpicks(expression):

    # intialise total number of toothpicks and number of toothpicks in the 
    # current sequence to zero
    used_toothpicks, sequence = 0, 0
    
    # intialise formatted and integer expression to empty string
    integer_expression, formatted_expression = '', ''
    
    # traverse all characters from the given expression
    for character in expression:
        
        if character == '|':
            
            # append vertical toothpick to the formatted expression and
            # increment total number of toothpicks and number of toothpicks in 
            # the current sequence
            formatted_expression += '|'
            used_toothpicks += 1
            sequence += 1
            
        elif not character.isspace():  # whitespace characters are ignored

            # all operators are formed using two toothpicks
            used_toothpicks += 2
            
            # append number of toothpicks of finished sequence to the integer
            # expression and initialize a new sequence of toothpicks
            if sequence:
                integer_expression += str(sequence)
                sequence = 0
                
            # append operator to formatted and integer expression
            formatted_expression += ' {} '.format(character)
            integer_expression += '*' if character == 'x' else character
            
    # append number of toothpicks of final sequence to the integer expression
    # and initialize a new sequence of toothpicks
    if sequence:
        integer_expression += str(sequence)
    
    # return formatted expression, together with the integer result and the
    # total number of toothpicks used
    return '{} = {} ({} toothpicks)'.format(
        formatted_expression, 
        eval(integer_expression), 
        used_toothpicks
    )

# generate formatted output for the given input
print(toothpicks(input()))