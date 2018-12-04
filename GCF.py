"""
This method is based on finding the roots for both numbers,
then determining the maximum intersection value as the GCF.
"""


def gcf(a, b):
    roots_a = []
    roots_b = []
    for i in range(1, a+1):
        if a % i == 0:
            roots_a.append(i)
    for i in range(1, b+1):
        if b % i == 0:
            roots_b.append(i)
    return max(set(roots_a).intersection(set(roots_b)))


print(gcf(2025, 5625))
