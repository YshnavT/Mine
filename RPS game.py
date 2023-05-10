from random import choice

op = ['Rock','Paper','Scissor']
user_W = 0
comp_W = 0

while True:
    print('''1. Rock
2. Paper
3. Scissor
4. Quit''')
    user_I = int(input('Choose an option(1/2/3/4) : '))
    comp_I = choice(op)

    if user_I in [1,2,3]:
        print('You chose ',op[user_I-1])
        print('Computer chose ',comp_I)
    elif user_I == 4:
        print('You scored ',user_W)
        print('Computer scored ',comp_W)
        break
    else:
        print('Choose a valid option ')
        continue
     
    if user_I == 1 and comp_I == 'Scissor':
        print('You WON')
        user_W+=1
    elif user_I == 2 and comp_I == 'Rock':
        print('You WON')
        user_W+=1
    elif user_I == 3 and comp_I == 'Paper':
        print('You WON')
        user_W+=1
    elif op[user_I-1] == comp_I:
        print('Draw...No points')
    else:
        print('Computer WON')
        comp_W+=1
print('Thank you for playing..')