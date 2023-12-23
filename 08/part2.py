import math


def parse(fp):
    steps = fp.readline().strip()
    mapping = {}
    for line in fp:
        if "=" not in line:
            continue
        line = line.replace("(", "").replace(")", "").strip()
        node = line.split("=")[0].strip()
        left = line.split("=")[1].split(",")[0].strip()
        right = line.split("=")[1].split(",")[1].strip()
        mapping[node] = (left, right)
    return steps, mapping


def apply_step(step_direction, node, mapping):
    if step_direction == "L":
        return mapping[node][0]
    else:
        return mapping[node][1]


with open("input.txt", "r") as fp:
    steps, mapping = parse(fp)


cur_states = list(filter(lambda x: x[-1] == "A", mapping.keys()))
print("Start", cur_states)

distance_to_z = []

for node in cur_states:
    count = 0
    done = False
    while not done:
        for step in steps:
            count += 1
            node = apply_step(step, node, mapping)
            if node[-1] == "Z":
                done = True
                break
    distance_to_z.append(count)

print(distance_to_z)
print(math.lcm(*distance_to_z))
