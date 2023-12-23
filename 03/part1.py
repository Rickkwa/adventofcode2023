def get_symbol_indices(grid, row):
    """Return a list of indices in the row where a symbol occurs"""
    result = []
    for c in range(len(grid[row])):
        if not grid[row][c].isdigit() and grid[row][c] != ".":
            result.append(c)
    return result


total = 0
grid = []

with open("input.txt", "r") as fp:
    for line in fp:
        grid.append(line.strip() + ".")


num_thus_far = ''
for r in range(len(grid)):
    for c in range(len(grid[r])):
        if grid[r][c].isdigit():
            if num_thus_far == "":
                start_col = c
            num_thus_far += grid[r][c]
        elif num_thus_far != "":
            end_col = c - 1
            # print(num_thus_far)

            # Check if we should add this number to total
            adjacent_part = False
            if r > 0 and any([start_col - 1 <= x <= end_col + 1 for x in get_symbol_indices(grid, r - 1)]):
                adjacent_part = True
            if r + 1 < len(grid) and any([start_col - 1 <= x <= end_col + 1 for x in get_symbol_indices(grid, r + 1)]):
                adjacent_part = True
            if any([start_col - 1 <= x <= end_col + 1 for x in get_symbol_indices(grid, r)]):
                adjacent_part = True
            if adjacent_part:
                total += int(num_thus_far)
                print(num_thus_far, "is adjacent")

            # Reset num_thus_far after finishing parsing the found number
            num_thus_far = ''
print("Total", total)

"""
num_thus_far = ''
for each row:
    for each col:
        if cur char is digit:
            num_thus_far += cur char
            if first digit in num_thus_far, record col
        elif not digit, or end of row (to not handle the special case of end of row, maybe add a "." sentinel at end of each line):
            record col of last digit (so we know both col of start/end of num)
            get list of indices of non digit/non periods in current row, previous row, next row
            if those any of those indices are between start_col - 1 and end_col + 1, then this part number is valid
                Add number to total
            reset num_thus_far to ''
"""
