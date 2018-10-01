from random import randint
print("______________________________________________________________________________________________________")
print("______________________________________________________________________________________________________")


print("........................WELCOME TO SHELDON'S ROCK_PAPER_SCISSOR_LIZARD_SPOCK GAME..........................")
print("______________________________________________________________________________________________________")
print("______________________________________________________________________________________________________")

print(":RULES GOES AS FOLLOWS :\nScissors cuts Paper\nPaper covers Rock\nRock crushes Lizard\nLizard poisons Spock\nSpock smashes Scissors\nScissors decapitates Lizard\nLizard eats Paper\nPaper disproves Spock\nSpock vaporizes Rock\n(and as it always has) Rock crushes Scissors")

print("______________________________________________________________________________________________________")
print("______________________________________________________________________________________________________")
while True:
    player = input( "Enter (rock(r)/paper(p)/scissor(s)/lizard(l)/spock(sp) : " )
    computer = randint( 1, 5 )
    if computer == 1:
        computer = 'r'
    elif computer == 2:
        computer = 'p'
    elif computer == 3:
        computer = 's'
    elif computer == 4:
        computer = 'l'
    elif computer == 5:
        computer = 'sp'

    print( player, 'vs', computer )

    if player == computer:
        print( "...D R A W..." )

    elif player == 'p' and computer == 'r':
        print( "...WINNER..." )

    elif player == 'p' and computer == 'sp':
        print( "...WINNER..." )

    elif player == 'p' and computer == 's':
        print( "...LOOSER..." )

    elif player == 'p' and computer == 'l':
        print( "...LOOSER..." )

    elif player == 'r' and computer == 'l':
        print( "...WINNER..." )

    elif player == 'r' and computer == 's':
        print( "...WINNER..." )

    elif player == 'r' and computer == 'p':
        print( "...LOOSER..." )

    elif player == 'r' and computer == 'sp':
        print( "...LOOSER..." )


    elif player == 's' and computer == 'p':
        print( "...WINNER..." )
    elif player == 's' and computer == 'l':
        print( "...WINNER..." )
    elif player == 's' and computer == 'sp':
        print( "...LOOSER..." )
    elif player == 's' and computer == 'r':
        print( "...LOOSER..." )


    elif player == 'l' and computer == 'p':
        print( "...WINNER..." )
    elif player == 'l' and computer == 'sp':
        print( "...WINNER..." )
    elif player == 'l' and computer == 's':
        print( "...LOOSER..." )
    elif player == 'l' and computer == 'r':
        print( "...LOOSER..." )

    elif player == 'sp' and computer == 'r':
        print( "...WINNER..." )
    elif player == 'sp' and computer == 's':
        print( "...WINNER..." )
    elif player == 'sp' and computer == 'l':
        print( "...LOOSER..." )
    elif player == 'sp' and computer == 'p':
        print( "...LOOSER..." )




