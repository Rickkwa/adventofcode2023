import math


def parse(fp):
    time = list(filter(lambda x: x.isnumeric(), fp.readline().strip().split(" ")))
    distance = list(filter(lambda x: x.isnumeric(), fp.readline().strip().split(" ")))
    return [int(x) for x in time], [int(x) for x in distance]


with open("input.txt", "r") as fp:
    time, distance = parse(fp)

"""
T = total time of race (known value)
d = distance to beat (known value)
x = hold time (value to solve for)

- x**2 + T*x - d > 0

Parabola equation. Wolfram alpha simplifies it as:

1/2 (T - sqrt(T*T - 4d))
< x <
1/2 (sqrt(T*T - 4d) + T)
"""

product = 1

for T, d in zip(time, distance):
    x1 = math.ceil(1 / 2 * (T - math.sqrt(T * T - 4 * d)))
    x2 = math.floor(1 / 2 * (math.sqrt(T * T - 4 * d) + T))

    diff = abs(x1 - x2) + 1
    print(f"{T} time; {d} to beat: Got {x1} and {x2} for a diff of {diff}")
    product = product * diff

print("Final", product)
