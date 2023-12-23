from enum import Enum


class Card():
    FACES = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]

    def __init__(self, face):
        if face not in self.FACES:
            raise Exception("Invalid card value")
        self.value = face

    def __str__(self):
        return self.value

    def __lt__(self, other_card):
        return self.FACES.index(self.value) < self.FACES.index(other_card.value)

    def __eq__(self, other_card):
        return self.FACES.index(self.value) == self.FACES.index(other_card.value)


class HandType(Enum):
    FIVEOFAKIND = 7
    FOUROFAKIND = 6
    FULLHOUSE = 5
    THREEOFAKIND = 4
    TWOPAIR = 3
    ONEPAIR = 2
    HIGHCARD = 1

    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented


class Hand():
    def __init__(self, card_list: list[Card], bid: int):
        if len(card_list) != 5:
            raise Exception(f"Invalid length of card list for hand. Expecting 5, got {len(card_list)}.")
        self.cards = card_list
        self.type = self.determine_type(self.cards)
        self.bid = bid

    def __str__(self):
        return ", ".join([str(x) for x in self.cards])

    @staticmethod
    def determine_type(card_list) -> HandType:
        """ Determine what type of hand this is. Return HandType. """

        face_count = len(Card.FACES) * [0]
        for card in card_list:
            face_count[Card.FACES.index(card.value)] += 1

        # Check if 5 of a kind
        if 5 in face_count:
            return HandType.FIVEOFAKIND
        # Check if 4 of a kind
        if 4 in face_count:
            return HandType.FOUROFAKIND
        # Check if full house
        if 3 in face_count and 2 in face_count:
            return HandType.FULLHOUSE
        # Check if 3 of a kind
        if 3 in face_count:
            return HandType.THREEOFAKIND
        # Check if 2 pair
        if face_count.count(2) == 2:
            return HandType.TWOPAIR
        # Check if 1 pair
        if 2 in face_count:
            return HandType.ONEPAIR
        # else high card
        return HandType.HIGHCARD
    
    def __lt__(self, other_hand) -> bool:
        """ Return true if this hand is less valuable than other hand """
        if self.type == other_hand.type:
            for i in range(5):
                if self.cards[i] == other_hand.cards[i]:
                    continue
                return self.cards[i] < other_hand.cards[i]
        return self.type < other_hand.type


hand_list = []
with open("input.txt", "r") as fp:
    for line in fp:
        faces, bid = line.strip().split(" ")
        cards = []
        for face in faces:
            cards.append(Card(face))
        hand_list.append(Hand(cards, int(bid)))


sorted_hand_list = sorted(hand_list)

total = 0
for i in range(len(sorted_hand_list)):
    hand = sorted_hand_list[i]
    rank = i + 1
    print(str(hand), hand.bid, hand.type)
    total += rank * hand.bid

print(total)
