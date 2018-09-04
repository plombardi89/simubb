from collections import namedtuple
from typing import List


class Pitch:

    def __init__(self, name: str, level: int, confidence: int, movement: int):
        self.name = name
        self.level = level
        self.confidence = confidence
        self.movement = movement


class Pitcher:

    def __init__(self, name: str, energy: int, confidence: int, pitches: List[Pitch]):
        self.name = name
        self.energy = energy
        self.confidence = confidence


class Bases:

    def __init__(self, first_base=None, second_base=None, third_base=None):
        self.first_base = first_base
        self.second_base = second_base
        self.third_base = third_base

    def advance_all_runners(self):
        runners_scored = []

        if self.third_base:
            runners_scored.append(self.third_base)
            self.third_base = None

        if self.second_base:
            self.third_base = self.second_base
            self.second_base = None

        if self.first_base:
            self.second_base = self.first_base
            self.first_base = None


class Game:

    def __init__(self):
        self.inning = 1
        self.bases = Bases()
        self.events = []

    def play(self):
        while True:
            break
