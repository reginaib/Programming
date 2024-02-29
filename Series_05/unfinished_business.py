def forward_sequence(word_seq):
    return word_seq.replace(' ', '').replace(',', '').lower()


def backward_sequence(word_seq):
    return forward_sequence(word_seq)[::-1]


def common_sequence(word_seq):
    forward = forward_sequence(word_seq)
    backward = backward_sequence(word_seq)

    for i in range(len(forward), 0, -1):
        prefix = backward[:i]
        suffix = forward[-i:]
        if prefix == suffix:
            return prefix
    return ''

    # alternatively:
    # determine the longest common suffix/prefix
    # length = 1
    # while not backward.startswith(forward[length:]):
    # length += 1
    # return forward[length:]


def missing_word(word_seq):
    backward = backward_sequence(word_seq)
    prefix = common_sequence(word_seq)

    return backward[len(prefix):].capitalize()
