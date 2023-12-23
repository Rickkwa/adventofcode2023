def parse(fp):
    """
    Return [seeds], [mapping_sequence], {mapping}
    Where [mapping_sequence] will be like ["seeds", "soil", "fertilizer", ..., "location"]
    and {mapping} like {"seeds": [{"dest": n, "source": n, "range": n}], "soil": [{"dest": n, "source": n, "range": n}], ...}
    """

    seeds_before_pair = fp.readline().strip().split(":")[1].strip().split(" ")
    seeds_before_pair = [int(x) for x in seeds_before_pair]
    seeds = list(zip(seeds_before_pair[::2], seeds_before_pair[1::2]))

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
    return seeds, sequence, mapping


def check_overlap(a_start, a_length, b_start, b_length):
    """ Return tuple (overlap_start, overlap_length) or False if no overlap """
    if a_start > b_start:
        a_start, b_start = b_start, a_start
        a_length, b_length = b_length, a_length
    a_end = a_start + a_length - 1
    b_end = b_start + b_length - 1
    # print(a_start, a_end, b_start, b_end)
    if b_start <= a_end and b_end >= a_end and a_start <= b_start:
        # print("Case A")
        return (b_start, a_end - b_start + 1)
    elif b_start >= a_start and b_end <= a_end:
        # print("Case B")
        return (b_start, b_length)
    return False


def split_segment(range_start, range_length, overlap_start, overlap_length):
    """
    I have a range, and I have a subset of the range where an overlap happened.
    Return the segments of the range that are before & after the overlapping area.
    """
    before_segment = None
    after_segment = None
    a_end = range_start + range_length - 1
    overlap_end = overlap_start + overlap_length - 1

    if range_start < overlap_start:
        before_segment = (range_start, overlap_start - range_start)
    if a_end > overlap_end:
        after_segment = (overlap_end + 1, a_end - overlap_end)
    return before_segment, after_segment


def split_and_translate(cur_range_pair: (int, int), list_range_mapping: list):
    stack = [cur_range_pair]
    translated_result = []
    while len(stack) > 0:
        # print(stack)
        range_start, range_length = stack.pop()
        range_end = range_start + range_length - 1
        """
        for item in list_range_mapping:
            dest_start, source_start, length = explode(item)
            if stack item overlaps with source_start+length:
                split to segment before overlap, overlap, segment after overlap
                translate overlapping part and add to translated_result
                add segment before/after to stack
                break
        if nothing in list_range_mapping matched, translate 1:1 by adding it to translated_result as-is
        """
        overlap = False
        for item in list_range_mapping:
            dest_start, source_start, length = item["dest"], item["source"], item["range"]
            if overlap := check_overlap(range_start, range_length, source_start, length):
                # print("Overlap at", overlap)
                # Translate from source to dest of the overlapping segment
                translated_result.append((dest_start + (overlap[0] - source_start), overlap[1]))
                # print("translated result", (dest_start + (overlap[0] - source_start), overlap[1]))

                before, after = split_segment(range_start, range_length, overlap[0], overlap[1])
                if before:
                    stack.append(before)
                    # print("before", before)
                if after:
                    stack.append(after)
                    # print("after", after)
                break
        if not overlap:
            translated_result.append((range_start, range_length))
    # print("Translated resultS:", translated_result)
    return translated_result


with open("input.txt", "r") as fp:
    seeds, sequence, mapping = parse(fp)

processables = seeds
next_processables = []
for i in range(len(sequence)):
    print("====================", sequence[i], len(processables))
    for item in processables:
        next_processables.extend(split_and_translate(item, mapping[sequence[i]]))
        # print(sequence[i], mapping[sequence[i]])
    processables = next_processables
    # print(processables)
    next_processables = []
# print(processables)
# print(len(processables))

print(min(processables, key = lambda t: t[0])[0])
