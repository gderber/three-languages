#!/usr/bin/env python3

#-------------------------------------------------------------------------------
#
# Libraries
#
#-------------------------------------------------------------------------------
# System Libraries
import sys
import os
import argparse
import random

# local libraries
# home_dir=os.path.expanduser("~")
# sys.path.append(home_dir + "/bin/lib/")
# import libcolors

#-------------------------------------------------------------------------------
#
# Global Variables
#
#-------------------------------------------------------------------------------
command='dice'

#-------------------------------------------------------------------------------
#
# debug
#
# Adds evtra debugging informtion
#
#-------------------------------------------------------------------------------
def debug(filename,function,description,req_debug_level,debug_level):
    if req_debug_level <= debug_level:
        debug_filename = "DEBUG_" + filename
        print_string = debug_filename + " in function " + function + " " + description
        print(print_string)
        return 0

def printcolor(text,attribute,fgcolor,bgcolor):
    escape = '\033['

    # Attributes
    if attribute == 'reverse':
        atrnum='7'
    elif attribute == 'bold':
        atrnum='1'
    elif attribute == 'unk':
        atrnum='3'
    elif attribute == 'underline':
        atrnum='4'
    elif attribute == 'blink':
        atrnum='5'
    else:
        atrnum='0'

    # Colors
    if fgcolor == 'black':
        fgnum='30'
    elif fgcolor == 'red':
        fgnum='31'
    elif fgcolor == 'green':
        fgnum='32'
    elif fgcolor == 'yellow':
        fgnum='33'
    elif fgcolor == 'blue':
        fgnum='34'
    elif fgcolor == 'magenta':
        fgnum='35'
    elif fgcolor == 'cyan':
        fgnum='36'
    else:
        fgnum='37'

    # Colors
    if bgcolor == 'black':
        bgnum='40'
    elif bgcolor == 'red':
        bgnum='41'
    elif bgcolor == 'green':
        bgnum='42'
    elif bgcolor == 'yellow':
        bgnum='43'
    elif bgcolor == 'blue':
        bgnum='44'
    elif bgcolor == 'magenta':
        bgnum='45'
    elif bgcolor == 'cyan':
        bgnum='46'
    else:
        bgnum='47'


    defbg='40'
    
    beginsequence=escape + atrnum + ';' + fgnum + ';' + bgnum + 'm'
    endsequence=escape + '0' + ';' + '37' + ';' +  defbg + 'm'

    print(beginsequence + text + endsequence)
    return 0



def pick_cards(deck, pick_count,debug_level):
    function="pick_cards"
    debug (command, function,"Begin Function",7,debug_level)

    card=random.choice(deck)
    deck=[x for x in deck if x != card]
    denominator=card[:1]
    suit=card[1:2]

    debug (command, function,"Card:" + card,7,debug_level)

    if denominator == '0':
        denominator='10'

    if suit == "S":
        ucodesuit='\u2664 '
        suitcolor='white'
        cardstring=denominator + ucodesuit 
    elif suit == "H":
        ucodesuit='\u2665 '
        suitcolor="red"
        cardstring=denominator + ucodesuit 
    elif suit == "D":
        ucodesuit='\u2666 '
        suitcolor='red'
        cardstring=denominator + ucodesuit 
    elif suit == "C":
        ucodesuit='\u2667 '
        suitcolor='white'
        cardstring=denominator + ucodesuit 
    else:
        if denominator == "B":
            ucodesuit='\U0001F0CF '
            suitcolor='white'
            cardstring=ucodesuit 
        elif denominator == "W":
            ucodesuit='\U0001F0DF '
            suitcolor='white'
            cardstring=ucodesuit 
        else:
            ucodesuit='\U0001F0BF '
            cardstring=ucodesuit 
            suitcolor='white'

    printcolor(cardstring,'noatr',suitcolor,'black')

    pick_count = pick_count - 1
    if pick_count > 0:
        pick_cards(deck,pick_count,debug_level)
    else:
        return 0
    


def main():
    function="main"
    
    parser = argparse.ArgumentParser(description='Process parameters')
    parser.add_argument('-j','--jokers',help='Add Jokers to the deck',action='store_true')
    parser.add_argument('-n','--number',type=int,help='Number of cards to pick')
    parser.add_argument('--debug',type=int,help='Specify debugging level',nargs='?')
    parser.add_argument("number", type=int,nargs='?', help='Number of cards to pick')
   
    args = parser.parse_args()

    if args.debug is None:
        debug_level=6
    elif args.debug is not None:
        debug_level=args.debug
    else:
        debug_level=6

    if args.number is None:
        count=1
    elif args.number > 52:
        if args.jokers:
            if args.number > 55:
                count=55
            else:
                count=args.nummer
        else:
            count=52
    else:
        count=args.number

    debug (command, function,"Arguments Parsed",7,debug_level)

    # Create the Deck
    # To keep the cards to 2 characters, use 0 for 10
    deck_spades=['2S','3S','4S','5S','6S','7S','8S','9S','0S','JS','QS','KS','AS']
    deck_hearts=['2H','3H','4H','5H','6H','7H','8H','9H','0H','JH','QH','KH','AH']
    deck_dimnds=['2D','3D','4D','5D','6D','7D','8D','9D','0D','JD','QD','KD','AD']
    deck_clubs=['2C','3C','4C','5C','6C','7C','8C','9C','0C','JC','QC','KC','AC']

    deck=deck_spades + deck_hearts + deck_dimnds + deck_clubs

    if args.jokers:
        deck_jokers=['BJ','RJ','WJ']
        deck = deck + deck_jokers

    
    pick_cards(deck,count,debug_level)
    return 0

main()
