#This game is to make a game about rock,paper,and scissors. It is a very popular game. 
import random 
# This list is used to give the user the choices for the options of the game, which is 'Rock, Paper, Scissors'
list = ["rock","paper","scissors"]
#This function tells when you win the game and how you win the game 
def game_win(user_op,cpu_op):
    #if your input and the randomly chosen computer answer were the same, than the game would end in a tie 
    if user_op == cpu_op:
        return "Both the computer and you have selected",user_choice,". It's a tie!"
    #if the user has chosen rock, than this would part of the function would check with what the computer has got and determines who won 
    elif user_op == "ROCK":
        if cpu_op == "SCISSORS":
            return" Rock beats scissors! You win! The computer loses."
        else:
            return "Paper beats rock! You lose. The computer wins!"
  #if the user has chosen paper, than this would part of the function would check with what the computer has got and determines who won 
    elif user_op == "PAPER":
        if cpu_op == "ROCK":
            return "Paper beats rock! You win! The computer loses."
        else:
            return "Scissors beats paper! You lose. The computer wins!"
    #if the user has chosen scissors, than this would part of the function would check with what the computer has got and determines who won 
    elif user_op == "SCISSORS":
        if cpu_op == "PAPER":
            return "Scissors beats paper! You win! The computer loses."
        else:
            return "Rock beats scissors! You lose. The computer wins!"
    else:
        return "Invalid Choice . Plese try again. You chose",user_choice,"this was an invalid input."

while True:
    print("These are your choices for the game:", list)
    user_choice = input("What is your choice?\n").upper()    
    cpu_choice = random.choice(list).upper()
    print("You chose {}, while the computer has chosen {}.".format(user_choice, cpu_choice))
    print(game_win(user_choice, cpu_choice))
    play_again = input("Do you want to play again? (Yes or NO)\n").lower()
    if play_again == "no":
        print("Thanks for playing! Better luck next time!")
        break