import re


def parse(line):
    """ Return a cuple of (card_num, [winning_nums], [numbers_you_have]) """
    line = re.sub(" +", " ", line)
    card_num = int(re.sub("[^0-9]", "", line.split(":")[0]))
    winning_nums = line.split(":")[1].split("|")[0].strip().split(" ")
    your_nums = line.split(":")[1].split("|")[1].strip().split(" ")
    return card_num, winning_nums, your_nums


total = 0
with open("input.txt", "r") as fp:
    for line in fp:
        card_num, winning_nums, your_nums = parse(line)
        count_match = len(set(winning_nums).intersection(set(your_nums)))
        if count_match > 0:
            score = 2**(count_match - 1)
            total += score
print(total)
