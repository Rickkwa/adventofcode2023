def parse(fp):
    """
    Return [seeds], [mapping_sequence], {mapping}
    Where [mapping_sequence] will be like ["seeds", "soil", "fertilizer", ..., "location"]
    and {mapping} like {"seeds": [{"dest": n, "source": n, "range": n}], "soil": [{"dest": n, "source": n, "range": n}], ...}
    """

    seeds = fp.readline().strip().split(":")[1].strip().split(" ")
    sequence = []
    mapping = {}
    for line in fp:
        line = line.strip()
        if line == "":
            continue
        if ":" in line:
            # add to sequence, and initilize mapping[] = []
            seq = line.split("-")[0]
            sequence.append(seq)
            mapping[seq] = []
        else:
            # read 3 nums and append to mapping[sequence[-1]] (default [])
            mapping[sequence[-1]] = mapping.get(sequence[-1], [])
            dest, source, range_len = line.split(" ")
            mapping[sequence[-1]].append({"dest": int(dest), "source": int(source), "range": int(range_len)})
    return [int(x) for x in seeds], sequence, mapping


def get_mapping(cur_id, dest_range, source_range, range_len):
    """ Return None if no mapping, else return the mapping. """
    if not(source_range <= cur_id < source_range + range_len):
        return None
    return cur_id - source_range + dest_range

with open("input.txt", "r") as fp:
    seeds, sequence, mapping = parse(fp)

# import json
# print(json.dumps(mapping, indent=2))
print(seeds)

results = []
for seed in seeds:
    cur_seq_id = seed
    for seq in sequence:
        for range_obj in mapping[seq]:
            next_seq_id = get_mapping(cur_seq_id, range_obj["dest"], range_obj["source"], range_obj["range"])
            if next_seq_id is not None:
                cur_seq_id = next_seq_id
                break
    results.append(int(cur_seq_id))
print(min(results))

"""
results = []
for seed in seeds:
    seq_id = seed
    for seq in sequence:
        if current seq_id is in in a range of mapping[seq]:
            seq_id = whatever the mapping is
        else:
            pass # do nothing, cuz seq_id is mapped to same id
    results.append(int(seq_id))  # ie. the seq_id is corresponding to location
print(min(results))
"""
