import random
random_num=random.randint(0,2)
rps=['rock','paper','scissors']
def win_check(player1,player2):
	if player1[0]=='r' and player2[0]=='s':
		print('player1 wins!')
	elif player1[0]=='r' and player2[0]=='p':
		print('player2 wins!')
	elif player1[0]=='p' and player2[0]=='s':
		print('player2 wins!')
	elif player1[0]=='p' and player2[0]=='r':
		print('player1 wins!')
	elif player1[0]=='s' and player2[0]=='p':
		print('player1 wins!')
	elif player1[0]=='s' and player2[0]=='r':
		print('player2 wins!')
	elif player1[0]=='s' and player2[0]=='s':
		print('it is a tie!')
	elif player1[0]=='r' and player2[0]=='r':
		print('it is a tie!')
	elif player1[0]=='p' and player2[0]=='p':
		print('it is a tie!')




print('welcome to rock paper scissors')
game=input('1 player or 2 players?\n')
if game[0]=='2':
	while True:
		player1=input('player 1 choose\n')
		player2=input('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nplayer 2 choosen\n')
		if player1[0] in ['r','p','s'] and player2[0] in ['r','p','s']:
			win_check(player1,player2)
			break
		else:
			print('\n please enter rock, paper, or scissors!')
			continue

		

elif game[0]=='1':
	while True:
		
		player=input('please choose\n')
		computer=rps[random_num]
		if player[0] in ['r','p','s']:
			print(f'computer: {computer}')
			win_check(player,computer)
			break
		else:
			print('\n please enter rock, paper, or scissors!')
			continue

		