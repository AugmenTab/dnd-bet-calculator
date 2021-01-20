#! python3

import math


def calculate_winnings(odds, wager):
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


def handle_odds():
    bets = int(input('How many bets on this ticket?: '))
    odds = 1
    i = 1
    while i <= bets:
        e = eval(input('Bet ' + str(i) + '. What are the odds?: '))
        e += 1
        odds *= e
        i += 1
    return odds


def program_start():
    odds = handle_odds()
    pp_wager = int(input('How many pp on the bet?: '))
    gp_wager = int(input('How many gp on the bet?: '))
    sp_wager = int(input('How many sp on the bet?: '))
    cp_wager = int(input('How many cp on the bet?: '))
    wager = (pp_wager * 1000) + (gp_wager * 100) + (sp_wager * 10) + cp_wager
    winnings = calculate_winnings(odds, wager)
    print(winnings)
    print('Your potential winnings are:')
    if winnings[0] != 0:
        print('   ' + str(winnings[0]) + ' pp')
    if winnings[1] != 0:
        print('   ' + str(winnings[1]) + ' gp')
    if winnings[2] != 0:
        print('   ' + str(winnings[2]) + ' sp')
    if winnings[3] != 0:
        print('   ' + str(winnings[3]) + ' cp')


if __name__ == "__main__":
    program_start()
