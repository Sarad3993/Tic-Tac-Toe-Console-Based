# Tic Tac Toe game using python:

# In this simple project i have tried to explain each and every steps in the best possible way
# i have used lots of comment so that everybody can understand the game logic
# so let's start building tic tac toe from scratch

# first let's define the rules of the game inside a function
# for this i have created a function which can be invoked in required position

def game_rules():
    print("----- GAME RULES -----\n")
    print('1. Tic Tac Toe has simple game rules')
    print('2. It is played between two players on a 3x3 field as seen below\n')
    game_board(cell)  # game_board() is called so that board displays on console
    print("\n3. One of the players plays as 'X', and other player plays as 'O' ")
    print("4. There are total 9 valid moves in the game")
    print("5. The first player that is able to write 3 'X' or 3 'O'\n"
          "   in straight rows, columns or diagonals WINS the game")
    print("6. If all cells are occupied and neither player has won the game\n"
          "   then its a DRAW or TIE\n")
    print(f"Player1 : {name1}")
    print(f"Player2 : {name2}\n")
    print(f"Hey, {name1} and {name2} be ready, the game is about to begin !!! ")


# Now we try to create a empty game board to display on the console when game starts
# for this first we must create a list having 9 elements as blank spaces
# later we can access each element of that list one by one

cell = [" " for _ in range(10)]
# creates a list ---> cell of 9 blank spaces

#function for creating empty game board from above list
def game_board(cell):
    # accessing elements of the list ---> cell one by one through indexing
    # here we start indexing from 1 and not 0 so that we don't get confuse while playing game
    # index [1] represents 1st row;1st column and so on

    print(f' {cell[1]} | {cell[2]} | {cell[3]}')

    print('---+---+---')

    print(f' {cell[4]} | {cell[5]} | {cell[6]}')

    print('---+---+---')

    print(f' {cell[7]} | {cell[8]} | {cell[9]}')


# We have completed 1st step of building this game
# now lets create function for checking condition of wins
# there are 8 total conditions of winning the game
# if any of these condition is true; whole statement becomes true
# so we have used or operator to handle this case
# Each row, column or diagonal element is compared
# with the character passed inside this function(i.e either 'X' or 'O')
# if any of this condition exactly matches with the character passed then there is a win

def winner(cell,char):

    return (
        cell[1] == cell[2] == cell[3] == char
        or cell[4] == cell[5] == cell[6] == char
        or cell[7] == cell[8] == cell[9] == char
        or cell[1] == cell[4] == cell[7] == char
        or cell[2] == cell[5] == cell[8] == char
        or cell[3] == cell[6] == cell[9] == char
        or cell[1] == cell[5] == cell[9] == char
        or cell[3] == cell[5] == cell[7] == char
    )


# Now lets create a function to check for draw or tie :
# the logic behind it is we create a counter and each time a player enters a position
# counter increases simultaneously and when count reaches 9 we can say that it's a draw or tie
# because if we want to win the game count never reaches 9 i.e least moves to win the game is 8
def check_tie(cell):
    count = sum(1 for i in range(10) if cell[i] in ['X', 'O'])
    return count == 9


# Now lets create a function that accepts player's name

def player_name():
    pass
# since nothing is to be returned so pass is used

name1 = input("\nEnter 1st player's name: ")
name2 = input("Enter 2nd player's name: ")
player_name()


# moving forward now lets create a function
# that asks player to choose the character as per their wish (i.e either 'X' or 'O')
def player_character():

    player1 = ''
    # keeps asking the player until the player types 'X' or 'O' correctly
    # if player types anything beside those letters ; it prompts until it gets 'X' or 'O'
    while player1 not in {'X', 'O'}:
        print(f"{name1} , do you want to be play as 'X' or 'O' ? ")
        player1 = input().upper()
        # upper() functions converts char into uppercase if user enters in lowercase
    print(f"Looks like {name1} wants to play as: {player1}\n")

    # we must create a condition that if player1 chooses 'X' then player2 should play with 'O'
    # or if player1 chooses 'O' then player2 should play with 'X'

    player2 = ''
    player2 = 'O' if player1 =='X' else 'X'
    print(f"Hey, {name2} , {player1} is already chosen so you must play as: {player2} \n")
    return [player1,player2]
    # list is returned as : ['X','O'] if player1 chooses 'X' first..here index[0] = 'X' and index[1] = 'Y'
    # else if player1 chooses 'O'  list is returned as : ['O','X'] i.e just reverse of above
    # later in main function it is accessed through indexing


# Now lets create a function that prompts user to enter the position in the board for playing game:

def player_moves():
    valid_moves = [str(i) for i in range(10)]
    # now we must establish a condition to check whether user entered valid moves or not
    # if player enters other number/character beside those inside the list then
    # player is prompted with a message to enter no again
    move = 0
    while move not in valid_moves:
        print("Please! enter valid position between(1-9) ")
        move = input()
    return int(move)
    # converting string into integer since inside valid_moves , moves are in string format


# We have now come to an end of basic game criteria
# The main game logic starts from here
# lets create a function to write the game logic

def main_game():
    print("\n************  Welcome To Tic Tac Toe  **************")
    print("        -----  Developed by: Sarad  -----\n\n")
    game_rules()
    print("")

    character = player_character()
    turn = 'first_player_turn' # just created to know that game begins with 1st player
    #list returned above is now accessed through indexing
    player1_choice = character[0]
    player2_choice = character[1]
    game_board(cell)
    print("\nLets begin the game!!!")

# now we must establish a condition for loop running continuously until game ends
# for this we simply use while loop with its boolean value True
# so loop keeps running until it finds something to stop
    while True:

        if check_tie(cell):
            print("\nThe game is a DRAW/TIE")
            print(f"Well played !!! {name1} and {name2}\n")
            break

        elif turn =='first_player_turn':
            print(f"\n{name1} it's your turn ")
            # now lets call a function from above which lets to enter the position we want to play
            moves = player_moves()
            cell[moves] = player1_choice
            game_board(cell) # game board is called each and every time as there is some changes in it
            # if it is not called next player cannot see what move to make next

            # now we have to check the condition for win
            # so we simply call the function from above
            # that checks all 8 conditions and determines if 1st player has won
            if (winner(cell,player1_choice)):
                print(f"\nCongrats! {name1} you have WON the game\n")
                break
            # break is used to exit from the loop as 1st player has won already

            else:
                turn = 'second_player_turn'
            # but if the game is still going on turn is now shifted to 2nd player


        # Now we use the same logic for 2nd player too
        elif turn =='second_player_turn':
            print(f"\n{name2} it's your turn: ")
            moves = player_moves()
            cell[moves] = player2_choice
            game_board(cell)

            if (winner(cell,player2_choice)):
                print(f"\nCongrats! {name2} you have WON the game\n")
                break #breaks from the loop immediately after 2nd player wins the game
            else:
                turn = 'first_player_turn'
                # if game is still going on turn rotates to player1 now


# Now lets call our main_game() function inside this main() function
if __name__ == '__main__':
    while True:
        main_game()

        # Now lets create a condition if user wants to replay the game
        cell = [' ' for _ in range(10)]
        # if this list is not defined here there will be a problem
        # ie. when game is replayed empty board won't appear on the console

        play_again = input("Do u want to play the game again (Y/N)? ").upper()
        if play_again == 'Y':
            continue
        print("\nThank you for playing the game...Hope u enjoyed it !!! ")
        break
            # if user enters anything other than 'Y' loop stops
            # and above message is displayed on console



