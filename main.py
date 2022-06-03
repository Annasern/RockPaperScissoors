import random

def play_game():
    choices = ['R', 'P', 'S']
    user = input("Player: What's Your choice? - 'R' for rock, 'P' for paper and 'S' for scissors: ")
    user = user.upper()
    while user not in choices:
        print('please enter a valid option')

    if user == 'R':
        user_choice_name = 'rock'
    elif user == "P":
        user_choice_name = 'paper'
    elif user == "s":
        user_choice_name = "scissors"

    computer = random.choice(choices)
    computer = computer.upper()
    if computer == 'R':
        computer_choice_name = 'rock'
    elif computer == "P":
        computer_choice_name = 'paper'
    elif computer == "s":
        computer_choice_name = "scissors"

    if user == computer:
        return play_game()
    if check_winner(user, computer):
        return "You won"

    return "You lost"

print(f"Player's choice was ('user_choice_name') : Computer's Choice was ('computer_choice_name')")


def check_winner(player, cpu):
    if (player == 'R' and cpu == 'S') or (player == 'P' and cpu == 'R') or (player == 'R' and cpu == 'P'):
        return True

print(play_game())