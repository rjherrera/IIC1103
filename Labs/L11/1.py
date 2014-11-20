import sys

a = sys.stdin.readline().strip().split(' ')
a[0], a[1] = int(a[0]), int(a[1])


def mcd(n, i):
    if n < i:
        print(n, i)
    if i % n == 0:
        return n
    return mcd(i % n, n)


print(mcd(a[0], a[1]))
