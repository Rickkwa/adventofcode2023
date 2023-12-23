def get_gear_indices(grid, row):
    """Return a list of indices in the row where a gear occurs"""
    result = []
    for c in range(len(grid[row])):
        if grid[row][c] == "*":
            result.append(c)
    return result


total = 0
grid = []

with open("input.txt", "r") as fp:
    for line in fp:
        grid.append(line.strip() + ".")


gear_adjacent_count = {}


"""
gear_adjacent_count's keys are the coords of each gear. And value is a list of adjacent full numbers.

for each square on the grid:
    Building the full number
    if full number is finalized:
        find all gears adjacent to it
        for each of those gears:
            add this full number to their gear_adjacent_count list
"""

num_thus_far = ''
for r in range(len(grid)):
    for c in range(len(grid[r])):
        if grid[r][c].isdigit():
            if num_thus_far == "":
                start_col = c
            num_thus_far += grid[r][c]
        elif num_thus_far != "":
            end_col = c - 1
            # print("=============", num_thus_far, r, c)

            if r != 0:
                if gear_indices := list(filter(lambda x: start_col - 1 <= x <= end_col + 1, get_gear_indices(grid, r - 1))):
                    for gear_c in gear_indices:
                        gear_adjacent_count[r - 1] = gear_adjacent_count.get(r - 1, {})
                        gear_adjacent_count[r - 1][gear_c] = gear_adjacent_count[r - 1].get(gear_c, [])
                        gear_adjacent_count[r - 1][gear_c].append(int(num_thus_far))
                        # print("Add to {}, {} for finding {}".format(str(r - 1), str(gear_c), num_thus_far))
            if r + 1 < len(grid):
                if gear_indices := list(filter(lambda x: start_col - 1 <= x <= end_col + 1, get_gear_indices(grid, r + 1))):
                    for gear_c in gear_indices:
                        gear_adjacent_count[r + 1] = gear_adjacent_count.get(r + 1, {})
                        gear_adjacent_count[r + 1][gear_c] = gear_adjacent_count[r + 1].get(gear_c, [])
                        gear_adjacent_count[r + 1][gear_c].append(int(num_thus_far))
                        # print("Add to {}, {} for finding {}".format(str(r + 1), str(gear_c), num_thus_far))
            if gear_indices := list(filter(lambda x: start_col - 1 <= x <= end_col + 1, get_gear_indices(grid, r))):
                for gear_c in gear_indices:
                    gear_adjacent_count[r] = gear_adjacent_count.get(r, {})
                    gear_adjacent_count[r][gear_c] = gear_adjacent_count[r].get(gear_c, [])
                    gear_adjacent_count[r][gear_c].append(int(num_thus_far))
                    # print("Add to {}, {} for finding {}".format(str(r), str(gear_c), num_thus_far))

            # Reset num_thus_far after finishing parsing the found number
            num_thus_far = ''

print(gear_adjacent_count)

for r in gear_adjacent_count.keys():
    for c in gear_adjacent_count[r].keys():
        if len(gear_adjacent_count[r][c]) == 2:
            total += gear_adjacent_count[r][c][0] * gear_adjacent_count[r][c][1]
print("Total", total)
