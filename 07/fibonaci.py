def fibb(a, b):
    if b > 100:
        return
    print(a)
    fibonacci(b, a + b)

def fibb_iter(n):
    pref = 0
    next = 1
    for i in range(n):
        print(pref)
        tmp = pref
        pref = next
        next = tmp + pref

fibb_iter(20)

