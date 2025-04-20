import random 

def play():
    print("Welcome to Rock, Paper, Scissors!")
    print("What's your choice? ")
    user_input = input("r is for 'rock', p is for 'paper', s is for 'scissors': ")
    computer = random.choice(['r', 'p', 's'])

    if user_input == computer:
        return "It's a tie!"
    
    # r > s, s > p, p > r
    if is_win(user_input, computer):
        return "You win!"
    return "You lose!"

def is_win(player, component):
    if (player == 'r' and component == 's') or (player == 's' and component == 'p') or (player == 'p' and component == 'r'):
        return True
    return False

print(play())
