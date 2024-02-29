"""
>>> alphabet = semaphore_alphabet('alphabet.txt')
>>> alphabet['24']
'F6'
>>> alphabet['42']
'F6'
>>> alphabet['26']
'R'
>>> alphabet['44']
' '
>>> alphabet['10']
'#'
>>> alphabet['37']
Traceback (most recent call last):
KeyError: '37'

>>> epoch2semaphore('12:43')
'06'
>>> epoch2semaphore('05:17')
'42'
>>> epoch2semaphore('04:45')
'36'

>>> semaphore2epochs('06')
{'00:42', '00:43', '00:44', '00:45', '08:57', '08:58', '08:59', '09:00', '09:01', '09:02', '09:03', '11:42', '11:43', '11:44', '11:45', '11:46', '11:47', '11:48', '12:42', '12:43', '12:44', '12:45', '20:57', '20:58', '20:59', '21:00', '21:01', '21:02', '21:03', '23:42', '23:43', '23:44', '23:45', '23:46', '23:47', '23:48'}
>>> semaphore2epochs('36')
{'03:46', '03:47', '03:48', '04:42', '04:43', '04:44', '04:45', '04:46', '04:47', '04:48', '08:19', '08:20', '08:21', '08:22', '08:23', '08:24', '08:25', '08:26', '09:19', '09:20', '09:21', '09:22', '09:23', '09:24', '09:25', '09:26', '15:46', '15:47', '15:48', '16:42', '16:43', '16:44', '16:45', '16:46', '16:47', '16:48', '20:19', '20:20', '20:21', '20:22', '20:23', '20:24', '20:25', '20:26', '21:19', '21:20', '21:21', '21:22', '21:23', '21:24', '21:25', '21:26'}
>>> semaphore2epochs('42')
{'02:27', '02:28', '02:29', '02:30', '02:31', '02:32', '02:33', '03:27', '03:28', '03:29', '03:30', '03:31', '03:32', '03:33', '05:15', '05:16', '05:17', '05:18', '06:12', '06:13', '06:14', '06:15', '06:16', '06:17', '06:18', '14:27', '14:28', '14:29', '14:30', '14:31', '14:32', '14:33', '15:27', '15:28', '15:29', '15:30', '15:31', '15:32', '15:33', '17:15', '17:16', '17:17', '17:18', '18:12', '18:13', '18:14', '18:15', '18:16', '18:17', '18:18'}

>>> epoch2symbol('22:30', alphabet)
'C'
>>> epoch2symbol('12:07', alphabet)
'#'
>>> epoch2symbol('10:30', alphabet, digit_mode=True)
'3'
>>> epoch2symbol('12:15', alphabet, digit_mode=True)
'J'
>>> epoch2symbol('9:03', alphabet)
'P'
>>> epoch2symbol('12:08', alphabet)
'#'
>>> epoch2symbol('12:37', alphabet, digit_mode=True)
'0'
>>> epoch2symbol('15:13', alphabet)
Traceback (most recent call last):
AssertionError: invalid epoch

>>> clock_reading('17:55 01:59 22:29 03:03 21:01 12:08 00:38', alphabet)
'C3P0'
>>> clock_reading('17:55 01:59 22:29 21:01 00:38', alphabet)
'C3P0'
>>> clock_reading('10:02 22:37 14:41 13:30 18:28 19:56 16:46 17:32 19:16 22:47 19:25 06:06 23:12', alphabet)
'TIME IS MONEY'
>>> clock_reading('11:51 19:54 07:17 18:06 05:28 06:49 16:49 18:27 18:43 11:04 04:39 11:36', alphabet)
Traceback (most recent call last):
AssertionError: invalid epoch

"""


def semaphore_alphabet(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        alphabet = {}
        for line in file:
            k, v = line.rstrip('\n').split('\t')
            alphabet[k] = v
            alphabet[k[::-1]] = v
    return alphabet


def epoch2semaphore(epoch):
    h, m = epoch.split(':')
    h = int(h)
    m = int(m)
    a_h = 30 * (h % 12) + m / 2
    a_m = 6 * m

    p_h = round((a_h / 45) % 8) % 8
    p_m = round((a_m / 45) % 8) % 8
    return f'{p_h}{p_m}'


def semaphore2epochs(semaphore):
    results = set()
    for h in range(24):
        for m in range(60):
            e = f'{h:02d}:{m:02d}'
            sm = epoch2semaphore(e)
            if sm == semaphore or sm == semaphore[::-1]:
                results.add(e)
    return results


def epoch2symbol(epoch, alphabet, digit_mode=False):
    sm = epoch2semaphore(epoch)
    assert sm in alphabet, 'invalid epoch'
    s = alphabet[sm]
    if len(s) == 1:
        return s
    elif digit_mode:
        return s[1]
    else:
        return s[0]


def clock_reading(epochs, alphabet):
    result = []
    digit_mode = False
    for e in epochs.split():
        s = epoch2symbol(e, alphabet, digit_mode)
        if s == '#':
            digit_mode = True
        elif digit_mode and s == 'J':
            digit_mode = False
        else:
            result.append(s)
    return ''.join(result)
