"""
This method is based on a for loop and determining the maximum value
that leads to a remainder of zero for both numbers.
"""


def gcf(a, b):
    for i in range(max(a,b), 0, -1):
        if a % i == 0 and b % i == 0:
            return i


print(gcf(2025, 5625))
