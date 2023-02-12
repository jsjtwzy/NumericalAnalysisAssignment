a = range(40)
def gen():
    res = yield from a
    return res
print(sum(gen()))