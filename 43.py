import itertools

def sect_divisby(sect, start, divisby):
    return int(sect[start-1:start+3-1]) % divisby == 0

def has_property(s):
    return sect_divisby(s, 8, 17)\
           and sect_divisby(s, 7, 13)\
           and sect_divisby(s, 6, 11)\
           and sect_divisby(s, 5, 7)\
           and sect_divisby(s, 4, 5)\
           and sect_divisby(s, 3, 3)\
           and sect_divisby(s, 2, 2)

print sum(int(s) for s in [''.join(x) for x in itertools.permutations("0123456789")] if has_property(s))

