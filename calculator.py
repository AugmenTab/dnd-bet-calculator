#! python3

def calculateWinnings(odds, wager):
    pass

def programStart():
    odds = eval(input('What are the odds?\n')) + 1
    ppWager = int(input('How many pp on the bet?\n'))
    gpWager = int(input('How many gp on the bet?\n'))
    spWager = int(input('How many sp on the bet?\n'))
    cpWager = int(input('How many cp on the bet?\n'))
    wager = (ppWager * 1000) + (gpWager * 100) + (spWager * 10) + cpWager
    calculateWinnings(odds, wager)

if __name__ == "__main__":
    programStart()