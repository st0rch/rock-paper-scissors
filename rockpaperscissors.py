#!/usr/bin/env python3

import random
import sys
import time

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

"""The Player class is the parent class for all of the Players
in this game"""

moves = ['rock',  'paper',  'scissors']


def sprint(self, str):
    for c in str + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(3./90)


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class ReflectPlayer(Player):
    def __init__(self):
        self.score = 0
        self.move_temp = random.choice(moves)

    def learn(self, my_move, their_move):
        self.move_temp = my_move

    def move(self):
        return self.move_temp


class CyclePlayer(Player):
    def __init__(self):
        self.score = 0
        self.move_temp = random.choice(moves)

    def learn(self, my_move, their_move):
        if their_move == "rock":
            self.move_temp = "paper"
        if their_move == "paper":
            self.move_temp = "scissors"
        if their_move == "scissors":
            self.move_temp = "rock"

    def move(self):
        return self.move_temp


class DumbPlayer(Player):
    def __init__(self):
        self.score = 0

    def move(self):
        return "rock"


class RandomPlayer(Player):
    def __init__(self):
        self.score = 0

    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def __init__(self):
        self.score = 0

    def move(self):
        while True:
            choice = input("Do you choose Rock, Paper, or Scissors? ")
            if choice.lower() not in moves:
                print("Please choose either rock, paper, or scissors. \n")
            else:
                return (choice.lower())


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1.score = 0
        self.p2.score = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        sprint(self, f" You played {move1} \n Your opponent played {move2} \n")
        if move1 == move2:
            sprint(self,  "It's a tie!")
        elif beats(move1, move2) is True:
            self.p1.score += 1
            sprint(self, "***PLAYER ONE WINS***")
        else:
            sprint(self, "***PLAYER TWO WINS***")
            self.p2.score += 1
        self.p1.learn(move1, move2)
        self.p2.learn(move1, move2)
        print(f" Player 1: {self.p1.score} Points \n"
              f" Player 2: {self.p2.score} Points")

    def play_game(self):
        sprint(self, f"Let's Play! Winner is declared "
                     f"after three rounds!")
        for round in range(3):
            sprint(self, f"\n Round {round} ----")
            self.play_round()

        print(f"\n Game over! \n Final Scores -- "
              f"P1: {self.p1.score} Points -- "
              f"P2: {self.p2.score} Points")
        if self.p1.score > self.p2.score:
            sprint(self, "PLAYER ONE WON THE GAME!")
        elif self.p1.score < self.p2.score:
            sprint(self, "PLAYER TWO WON THE GAME!")
        else:
            sprint(self, "WOW! THIS GAME WAS A TIE!")
        while True:
            again = input(f"Type 'again' to keep going, or 'exit' to close: ")
            if again.lower() == "again":
                game.play_game()
            elif again.lower() == "exit":
                sprint(self, f"goodbye!")
                sys.exit(0)
            else:
                sprint(self, f"Please enter either 'again' or 'exit'")


if __name__ == '__main__':
    game = Game(HumanPlayer(), RandomPlayer())
    game.play_game()
