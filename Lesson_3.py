


def search(pattern,text):
    "Return True if pattern appears anywhere in text."
    if pattren.startswith('^'):
        return match(pattern[1:],text)
    else:
        return match('.*'+parrern,text)

def match(pattern,text):
    "Return True if pattern appears at the start of text."

    if pattern == '':
        return True
    elif pattern == '$':
        return (text == '')
    elif len(pattern) > 1 and pattern[1] in '*?':
        p, op, pat = pattern[0], pattern[1], pattern[2:]
        if op == '*':
            return match_star(p, pat, text)
        elif op == '?':
            if match1(p, text) and match(pat, text[1:]):
                return True
            else:
                return match(pat, text)
    else:
        return (match1(pattern[0], text) and
                match(             ,           )) # fill in this line




def test():
    assert search('baa*!','Sheep said baaaa!')
    assert search('baa!','Sheep said baaaa!') == False
    assert match('baa*!','Sheep said baaa!') == False
    assert match('baa*!','baaaaaaa! said the sheeep')
    assert search('def','abcdefg')
    assert search('def$','fdsdef')
    assert search('def$','fdsdefd') == False
    assert search('^start','not the start') == False
    assert match('start','not the start') == False
    assert match('a*b*c*','just anything')
    assert match('x?','test')
    assert match('text?','text')
    assert match('text?','tex')

    def words(test):
        return text.split()
    assert all(match('aa*bb*cc*$',s) for s in words('abc aabbcc aaaaabccccc'))
    assert not any(match('aa*bb*cc*$',s) for s in words('ac aabbccd aaaaa-b-ccccc'))
    assert all(search('^ab.*aca.*a$',s) for s in words('abracadabra abacaa about-acacia-f'))
    assert all(search('t.p',s) for s in words('tip top tap atypical tepid stop .top'))
    assert not any(search('t.p',s) for s in words('TYPE teepee tp'))
    return 'test passes'
