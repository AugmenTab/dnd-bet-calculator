#! python3

import math

def calculateWinnings(odds, wager):
    w = odds * wager
    e = str(int(w))
    pp = gp = sp = '0'
    cp = e[-1]
    if len(e) >= 4:
        pp = math.floor(w / 1000) or 0
    if len(e) >= 3:
        gp = e[-3]
    if len(e) >= 2:
        sp = e[-2]
    winnings = [pp, gp, sp, cp]
    return winnings

def handleOdds():
    bets = int(input('How many bets on this ticket?\n'))
    odds = 1
    i = 1
    while i <= bets:
        e = eval(input('Bet ' + str(i) + '. What are the odds?\n'))
        e += 1
        odds *= e
        i += 1
    return odds

def programStart():
    odds = handleOdds()
    ppWager = int(input('How many pp on the bet?\n'))
    gpWager = int(input('How many gp on the bet?\n'))
    spWager = int(input('How many sp on the bet?\n'))
    cpWager = int(input('How many cp on the bet?\n'))
    wager = (ppWager * 1000) + (gpWager * 100) + (spWager * 10) + cpWager
    winnings = calculateWinnings(odds, wager)
    print('Your potential winnings are ' + str(winnings[0]) + ' pp, ' + str(winnings[1]) + ' gp, ' + str(winnings[2]) + ' sp, ' + str(winnings[3]) + ' cp.')

if __name__ == "__main__":
    programStart()