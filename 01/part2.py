mapping = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}
total = 0
with open("input.txt", "r") as fp:
    for line in fp:
        line = line.strip()
        line_num = 0
        # Scan from the left until any digit (word or num) is found
        for i in range(len(line)):
            if line[i] in '0123456789':
                line_num += int(line[i]) * 10
                break
            elif len(f := list(filter(lambda w: line[i:].startswith(w), mapping.keys()))) > 0:
                line_num += int(mapping[f[0]]) * 10
                break
        # Scan from the right until any digit (word or num) is found
        for i in range(len(line) - 1, -1, -1):
            if line[i] in '0123456789':
                line_num += int(line[i])
                break
            elif len(f := list(filter(lambda w: line[i:].startswith(w), mapping.keys()))) > 0:
                line_num += int(mapping[f[0]])
                break
        total += line_num
print(total)

