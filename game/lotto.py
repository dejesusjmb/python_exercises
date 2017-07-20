from random import randint


class Lotto(object):
    def play(self, bet, guess):
        winnings = [0, 1, 5, 10]
        print "Bet ", bet
        print "Guess: ", guess
        draw = [randint(1, 10), randint(1, 10), randint(1, 10)]
        print "Draw: ", draw
        success = [num for num in guess if num in draw]
        print "Success: ", success
        return winnings[len(success)] * bet

if __name__ == "__main__":
    win = Lotto().play(10, [1, 2, 3])
    print "Win: ", win
