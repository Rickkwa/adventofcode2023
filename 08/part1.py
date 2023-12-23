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


with open("input.txt", "r") as fp:
    steps, mapping = parse(fp)


count = 0
cur_node = "AAA"

done = False
while not done:
    for step in steps:
        count += 1
        if step == "L":
            next_node = mapping[cur_node][0]
        else:
            next_node = mapping[cur_node][1]
        # print(next_node)
        if next_node == "ZZZ":
            done = True
            break
        cur_node = next_node

print(count)
