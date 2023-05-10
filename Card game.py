deck = list(range(1,53))
print('''Game: the players take turns pulling cards from the
deck until there are no more cards left. 
The player who pulls the last card wins the game''')

print(deck)
play = (input('Do you want to play the card game(Yes or no): ')).lower()

if play == 'yes':
    while len(deck)>0:
            
        P1 = int(input('How many cards do you want pull(1 to 6) player_1: '))
        for i in range(P1):
            deck.pop()
        print(len(deck),'card remaining.')
        if len(deck)==0:
            print('Game Over Player_1 wins.')
            break

        P2 = int(input('How many cards do you want pull(1 to 6) player_2: '))
        for i in range(P2):
            deck.pop()
        print(len(deck),'card remaining.')
        if len(deck)==0:
            print('Game Over Player_2 wins.')

else:
    print('Quiting')