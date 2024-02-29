# https://dodona.be/nl/courses/2802/series/29675/activities/1921947075


def read_lexicon(location):
    """
    >>> lexicon = read_lexicon('lexicon.txt')
    >>> lexicon['🔧']
    'wrench'
    >>> lexicon['🐜']
    'ant'
    >>> lexicon['🐩']
    'poodle'
    >>> lexicon['📦📦']
    'boxes'
    """
    lexicon = {}
    with open(location, 'r', encoding='utf-8') as file:
        return dict(line.split() for line in file)


def edit(word: str, action: str):
    """
    >>> edit('wrench', '+a')
    'wrencha'
    >>> edit('ant', 'mi+')
    'miant'
    >>> edit('poodle', 'le=y')
    'poody'
    >>> edit('boxes', '-s')
    'boxe'
    """
    if action.startswith('+'):
        return word + action[1:]
    elif action.endswith('+'):
        return action[:-1] + word
    elif action.startswith('-'):
        return word.replace(action[1:], '', 1)
    elif '=' in action:
        return word.replace(*action.split('='), 1)


def part(pattern, rep_lexicon):
    """
    >>> part('📦📦 -s x=h', lexicon)
    'bohe'
    >>> part('🐜 mi+ -t', lexicon)
    'mian'
    >>> part('🔧 +a -w -enc', lexicon)
    'rha'
    >>> part('🐩 le=y o=s', lexicon)
    'psody'
    >>> part('🔥👅 c=et p=oc', lexicon)
    'society'
    """
    emo, *actions = pattern.split()
    word = rep_lexicon[emo]
    for act in actions:
        word = edit(word, act)
    return word


def rebus(rep_rebus, rep_lexicon):
    """
    >>> rebus([['📦📦 -s x=h', '🐜 mi+ -t'], ['🔧 +a -w -enc', '🐩 le=y o=s']], lexicon)
    'bohemian rhapsody'
    >>> rebus([['🏨'], ['🐈 t=l', '📯 h=if', '🐈 c=i -t']], lexicon)
    'hotel california'
    >>> rebus([['🧂 a=u', '🐜🐜 -t'], ['🐂 x=f'], ['💍 r=sw']], lexicon)
    'sultans of swing'
    """
    return ' '.join(''.join(part(x, rep_lexicon) for x in parts) for parts in rep_rebus)
