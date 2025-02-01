import random

list = """rock paper scissors""".split()
computer_choice = random.choice(list)

if __name__ == '__main__':
    print('Welcome to Rock, Paper, Scissors Game!')
    print('Enter your choice: rock, paper or scissors')
    user_choice = input().lower()
    if user_choice not in list:
        print('Invalid choice!')
    elif user_choice == computer_choice:
        print(f'Computer chose {computer_choice}. It\'s a tie!')
    elif user_choice == 'rock':
        if computer_choice == 'paper':
            print(f'Computer chose {computer_choice}. You lose!')
        else:
            print(f'Computer chose {computer_choice}. You win!')
    elif user_choice == 'paper':
        if computer_choice == 'scissors':
            print(f'Computer chose {computer_choice}. You lose!')
        else:
            print(f'Computer chose {computer_choice}. You win!')
    elif user_choice == 'scissors':
        if computer_choice == 'rock':
            print(f'Computer chose {computer_choice}. You lose!')
        else:
            print(f'Computer chose {computer_choice}. You win!')
    exit()

