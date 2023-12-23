import re

def parse(line):
    """ Return tuple of (game id, [sets of (r, g, b)]) """
    game_id = int(re.sub("[^0-9]", "", line.split(":")[0]))
    sets = []
    for set_str in line.split(":")[1].split(";"):
        if r := re.search("([0-9]+) red", set_str):
            r = int(r.group(1))
        if g := re.search("([0-9]+) green", set_str):
            g = int(g.group(1))
        if b := re.search("([0-9]+) blue", set_str):
            b = int(b.group(1))
        sets.append((r or 0, g or 0, b or 0))
    return game_id, sets



AVAIL_RED = 12
AVAIL_GREEN = 13
AVAIL_BLUE = 14

total = 0
with open("input.txt", "r") as fp:
    for line in fp:
        game_id, sets = parse(line)
        if all([r <= AVAIL_RED and g <= AVAIL_GREEN and b <= AVAIL_BLUE for r, g, b in sets]):
            total += game_id

print(total)
