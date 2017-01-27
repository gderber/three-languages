#!/usr/bin/env python3

###########################################################
#
# Dice
# dice
#
# The scores should distribute evenly, assuming RANDOM is random. 
# With $MAXTHROWS at 600, all should cluster around 100, 
# + plus-or-minus 20 or so. 
#
# # Keep in mind that RANDOM is a ***pseudorandom*** generator, 
# + and not a spectacularly good one at that. 
# Randomness is a deep and complex subject. 
# Sufficiently long "random" sequences may exhibit 
# + chaotic and other "non-random" behavior. 
# Exercise (easy): 
# --------------- 
# Rewrite this script to flip a coin 1000 times. 
# Choices are "HEADS" and "TAILS."
#
#
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
#
# Libraries
#
#-------------------------------------------------------------------------------
# System Libraries
import sys
import argparse
import random

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

#-------------------------------------------------------------------------------
#
# print_unicode
#
#-------------------------------------------------------------------------------
def print_unicode(roll,debug_level):
    function="print_unicode"
    debug (command, function,"Begin Function",7,debug_level)
    if roll == 1:
        unicode_roll='\u2680'
    elif roll == 2:
        unicode_roll='\u2681'
    elif roll == 3:
        unicode_roll='\u2682'
    elif roll == 4:
        unicode_roll='\u2683'
    elif roll == 5:
        unicode_roll='\u2684'
    else:
        unicode_roll='\u2685'

    return unicode_roll


#-------------------------------------------------------------------------------
#
# rolldice
#
#-------------------------------------------------------------------------------
def rolldice(pips,debug_level):
    function="rolldice"
    debug (command, function,"Begin Function",7,debug_level)
    roll=random.randint(1,pips)
    return roll

#-------------------------------------------------------------------------------
#
# main
#
#-------------------------------------------------------------------------------
def main():
    function="main"
    
    parser = argparse.ArgumentParser(description='Process parameters')
    parser.add_argument('-d','--dice',type=int,help='Number of Dice to throw')
    parser.add_argument('--pips',type=int,help='Number of sides on the dice')
    parser.add_argument('--count', help='Print summary',action='store_true')
    parser.add_argument('--debug',type=int,help='Specify debugging level',nargs='?')
    parser.add_argument("dice", type=int,nargs='?', help='Number of Dice to Throw')
   
    args = parser.parse_args()

    if args.debug is None:
        debug_level=6
    elif args.debug is not None:
        debug_level=args.debug
    else:
        debug_level=6

        debug (command, function,"Arguments Parsed",7,debug_level)

    if args.dice is None:
        dice=1
    else:
        dice=args.dice

    if args.pips is None:
        pips=6
    else:
        pips=args.pips

    debug (command, function,"Variables Processed",7,debug_level)

    roll_count=0

    if args.count:
        summary={"{}".format(i): 0 for i in range(pips)}
        print(summary)
        
    while roll_count < dice:
        roll=rolldice(pips,debug_level)
        roll_count=roll_count+1
        if pips <= 6:
            unicode_roll=print_unicode(roll,debug_level)
            print('{0} {1}'.format('Roll is:',unicode_roll))
        else:
            print('{0} {1}'.format('Roll is:',roll))
                
        if args.count:
            row=roll-1
            row_string=str(row)
            summary[row_string]=summary[row_string] + 1
        
    debug (command, function,"Dice Rolled",7,debug_level)

    if args.count:
        key=0
        while key < pips:
            if pips == 2:
                key_string=str(key)
                if key == 0:
                    print_key='heads'
                else:
                    print_key='tails'
            else:
                print_key=key+1
                key_string=str(key)
            print(print_key, ' => ', summary[key_string])
            key = key + 1

    return 0


main()
