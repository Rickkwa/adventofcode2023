total = 0
with open("input.txt", "r") as fp:
    for line in fp:
        digits = list(filter(lambda c: c in '0123456789', line))
        total += int(digits[0] + digits[-1])
print(total)
