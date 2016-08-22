#A game of rock, paper, scissors

player1=int(raw_input("Player 1! Choose from the following: 1.Rock 2.Paper 3.Scissors \n"))  #prompt to player 1

while True:  #continuous loop to ensure that a valid option is selected
    if (player1==1 or player1==2 or player1==3):
        break
    else:
        player1=int(raw_input("Player 1! Choose from the following: 1.Rock 2.Paper 3.Scissors \n"))

player2=int(raw_input("Player 2! Choose from the following: 1.Rock 2.Paper 3.Scissors \n"))  #prompt to player 2

while True:   #continuous loop to ensure that a valid option is selected
    if (player2==1 or player2==2 or player2==3):
        break
    else:
        player2=int(raw_input("Player 2! Choose from the following: 1.Rock 2.Paper 3.Scissors \n"))        

if((player1==1 and player2==3) or (player1==2 and player2==1) or (player1==3 and player2==2)):
    print("Player 1 wins!")
elif(player1==player2):
    print("It's a draw!")
else:
    print("Player 2 wins!")