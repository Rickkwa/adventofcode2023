import re


def parse(line):
    """ Return a cuple of (card_num, [winning_nums], [numbers_you_have]) """
    line = re.sub(" +", " ", line)
    card_num = int(re.sub("[^0-9]", "", line.split(":")[0]))
    winning_nums = line.split(":")[1].split("|")[0].strip().split(" ")
    your_nums = line.split(":")[1].split("|")[1].strip().split(" ")
    return card_num, winning_nums, your_nums


cards = {}
with open("input.txt", "r") as fp:
    for line in fp:
        card_num, winning_nums, your_nums = parse(line)
        cards[card_num] = (winning_nums, your_nums)

piles = {}
for card in cards.keys():
    piles[card] = 1

for card in sorted(cards.keys()):
    winning_nums, your_nums = cards[card]
    count_match = len(set(winning_nums).intersection(set(your_nums)))
    for i in range(count_match):
        piles[card + i + 1] += 1 * piles[card]
    # print("After card", card, piles)
print(sum(piles.values()))
