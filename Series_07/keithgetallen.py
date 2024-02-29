# https://dodona.be/nl/courses/2802/series/29673/activities/464622171


def keith_step(numbers):
    """
    >>> numbers = [1, 9, 7]
    >>> keith_step(numbers)
    [9, 7, 17]
    >>> numbers
    [9, 7, 17]
    >>> keith_step(numbers)
    [7, 17, 33]
    >>> keith_step(numbers)
    [17, 33, 57]
    >>> keith_step(numbers)
    [33, 57, 107]
    >>> keith_step(numbers)
    [57, 107, 197]
    >>> numbers
    [57, 107, 197]
    """
    numbers.append(sum(numbers))
    del numbers[0]
    return numbers


def keith_sequence(number, target=None):
    """
    >>> keith_sequence(3)
    [3]
    >>> keith_sequence(11)
    [8, 13]
    >>> keith_sequence(34)
    [29, 47]
    >>> keith_sequence(197)
    [57, 107, 197]
    >>> keith_sequence(1104, target=7000)
    [1104, 2128, 4102, 7907]
    >>> keith_sequence(3684, target=10000)
    [1910, 3684, 7100, 13685]
    """
    if target is None:
        target = number
    numbers = [int(digit) for digit in str(number)]

    while numbers[-1] < target:
        keith_step(numbers)
    return numbers


def iskeith(number, reverse=False):
    """
    >>> iskeith(3)
    False
    >>> iskeith(34, reverse=False)
    False
    >>> iskeith(197)
    True
    >>> iskeith(11)
    False
    >>> iskeith(2580, False)
    True
    >>> iskeith(86935)
    True
    >>> iskeith(174680)
    True
    >>> iskeith(5752090994058710841670361653731519, reverse=False)
    True
    >>> iskeith(9, True)
    False
    >>> iskeith(11, reverse=True)
    False
    >>> iskeith(12, True)
    True
    >>> iskeith(341, reverse=True)
    True
    >>> iskeith(5532, True)
    True
    >>> iskeith(5426705064, reverse=True)
    True
    """
    if number < 10:
        return False

    target = int(str(number)[::-1]) if reverse else number
    return target == keith_sequence(number, target)[-1]


