def bitify(s):
    return ''.join(format(c, 'b') for c in bytearray(s, 'utf-8'))
