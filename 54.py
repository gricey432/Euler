from __future__ import print_function
from typing import List
from collections import Counter

RANK_ORDER = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']


class Card(object):
    SUIT_DIAMONDS = 'D'
    SUIT_HEARTS = 'H'
    SUIT_SPADES = 'S'
    SUIT_CLUBS = 'C'

    RANK_ACE = 14
    RANK_KING = 13
    RANK_QUEEN = 12
    RANK_JACK = 11
    RANK_TEN = 10

    suit = None  # type: str
    rank = None  # type: int

    def __init__(self, str_repr):
        self.suit = str_repr[1]

        rank_str = str_repr[0]
        if rank_str == 'A':
            self.rank = self.RANK_ACE
        elif rank_str == 'K':
            self.rank = self.RANK_KING
        elif rank_str == 'Q':
            self.rank = self.RANK_QUEEN
        elif rank_str == 'J':
            self.rank = self.RANK_JACK
        elif rank_str == 'T':
            self.rank = self.RANK_TEN
        else:
            self.rank = int(rank_str)


class Hand(object):
    cards = None  # type: List[Card]

    def __init__(self, cards):
        # type: (List[Card]) -> None
        self.cards = cards

    @property
    def rank_counts(self):
        ranks = [c.rank for c in self.cards]
        return Counter(ranks)

    @property
    def suit_counts(self):
        suits = [c.suit for c in self.cards]
        return Counter(suits)

    @property
    def ordered_ranks(self):
        # Gets all the rank values from high to low
        return sorted([c.rank for c in self.cards], reverse=True)

    def _get_rank_with_count(self, count):
        # type: (int) -> int
        for rank, rank_count in self.rank_counts.items():
            if count == rank_count:
                return rank

    @property
    def score(self):
        # type: () -> int

        # Type and modifier
        if self.is_royal_flush:
            score = 1000
            # no modifier

        elif self.is_straight_flush:
            score = 900
            # modifier is high card sorting

        elif self.is_four_of_a_kind:
            score = 800
            score += self._get_rank_with_count(4)

        elif self.is_full_house:
            score = 700
            score += self._get_rank_with_count(3)

        elif self.is_flush:
            score = 600
            # modifier is high card sorting

        elif self.is_straight:
            score = 500
            # modifier is high card sorting

        elif self.is_three_of_a_kind:
            score = 400
            score += self._get_rank_with_count(3)

        elif self.is_two_pairs:
            score = 300
            high_pair_rank = 0
            for rank, rank_count in self.rank_counts.items():
                if rank_count == 2:
                    high_pair_rank = max(rank, high_pair_rank)
            score += high_pair_rank

        elif self.is_one_pair:
            score = 200
            score += self._get_rank_with_count(2)

        else:
            # High card, modifier is just the high card sorting below
            score = 100

        # Highest cards
        for rank in self.ordered_ranks:
            score *= 100
            score += rank

        return score

    @property
    def is_royal_flush(self):
        # type: () -> bool
        return self.is_straight and self.is_flush and 'A' in [c.rank for c in self.cards]

    @property
    def is_straight_flush(self):
        # type: () -> bool
        return self.is_straight and self.is_flush

    @property
    def is_four_of_a_kind(self):
        # type: () -> bool
        for v in self.rank_counts.values():
            if v == 4:
                return True
        return False

    @property
    def is_full_house(self):
        # type: () -> bool
        return self.is_three_of_a_kind and self.is_one_pair

    @property
    def is_flush(self):
        # type: () -> bool
        return len(self.suit_counts) == 1

    @property
    def is_straight(self):
        # type: () -> bool
        ordered_ranks = self.ordered_ranks
        for i in range(len(ordered_ranks) - 1):
            if ordered_ranks[i] - ordered_ranks[i+1] != 1:
                return False
        return True

    @property
    def is_three_of_a_kind(self):
        # type: () -> bool
        for v in self.rank_counts.values():
            if v == 3:
                return True
        return False

    @property
    def is_two_pairs(self):
        # type: () -> bool
        num_pairs = 0
        for v in self.rank_counts.values():
            if v == 2:
                num_pairs += 1
        return num_pairs == 2

    @property
    def is_one_pair(self):
        # type: () -> bool
        for v in self.rank_counts.values():
            if v == 2:
                return True
        return False


with open('p054_poker.txt', 'r') as f:
    player_1_wins = 0

    for l in f:
        cards = [Card(cs) for cs in l.strip().split(' ')]
        hand_1 = Hand(cards[0:5])
        hand_2 = Hand(cards[5:10])

        if hand_1.score > hand_2.score:
            player_1_wins += 1

print(player_1_wins)
