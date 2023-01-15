a0 = 0.05
a1 = 15
def iter1(a):
    return lambda i0, n: -a *i0 +1 /n
def iter2(a):
    return lambda i1, n: (-i1 +1 /n) /a
def main():
    i00 = 3.04452
    i01 = 0.06454
    i100 = 1
    i101 = 0.00600
    it = iter1(a0)
    for i in range(1,11):
        i00 = it(i00, i)
        print()
        i01 = it(i01, i)
        print('ia0', i, ':', i00, 'ia1', i, ':', i01)
    it = iter2(a1)
    for i in reversed(range(1,11)):
        i100 = it(i100, i)
        print()
        i101 = it(i101, i)
        print('ia0', i, ':', i100, 'ia1', i, ':', i101)
main()