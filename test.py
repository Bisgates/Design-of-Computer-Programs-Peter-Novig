def instrument_fn(fn,*args):
    c.start, c.items = 0, 0
    result = fn(*args)
    print("%s got %s with %5d iters over %7d items"%(fn.__name__,result,c.start,c.items))


def c(sequence):
    c.start += 1
    for item in sequence:
        c.items += 1
        yield item



def test():
    for j in range(100):
        for i in c(range(100)):
            pass
    return True


instrument_fn(test)


#-----------------#-----------------#-----------------#-----------------


s = 'print("1+45")'

table = bytes.maketrans(b'ABC',b'123')

f = 'A+B==C'
eval(f.translate(table))

print("Swap vowels for numbers.".translate(str.maketrans('aeiou', '12345')))

print(tab)




intab = 'aeiou'
outtab = '12345'

s = 'this is string example....wow!!!'

print(s.translate({ord(x): y for (x, y) in zip(intab, outtab)}))



{x: y for (x, y) in zip(intab, outtab)}
