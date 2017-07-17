def decode_morse(s):
    table = dict(zip(' .- -... -.-. -.. . ..-. --. .... .. .--- -.- .-..'
                     ' -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --..'.split(' '),
                     ' abcdefghijklmnopqrstuvwxyz'))
    return ''.join([table[sign] for sign in s.split(' ')])

# print(decode_morse('.... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--'))
