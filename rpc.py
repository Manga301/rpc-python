import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


# create computer list - we can randomly generate numbers from this list
computer_list = [rock, paper, scissors]
computer_name_list = ['rock','paper','scissors']

# use random.randint() to generate the random number from the list
comp_random_select = random.randint(0, len(computer_list) - 1)

# computer input
computer_random_item = computer_list[comp_random_select]
computer_random_num = computer_name_list[comp_random_select]

# user select 'rock', 'paper' or 'scissors'
user_input = input("Type 'rock', 'paper' or 'scissors': ").lower()
user_rpc = [rock, paper, scissors]

# lets work out the logic 
if user_input == 'rock' and computer_random_num == 'scissors':
  # you win
  print(f"you: {user_input} | computer: {computer_random_num}")
  print("you win, rock beats scissors!")
elif user_input == 'scissors' and computer_random_num == 'rock':
  # computer wins
  print(f"you: {user_input} | computer: {computer_random_num}")
  print("computer win, rock beats scissors!")
elif user_input == 'paper' and computer_random_num == 'scissors':
  # computer wins
  print(f"you: {user_input} | computer: {computer_random_num}")
  print("computer wins, scissors beats paper")
elif user_input == 'scissors' and computer_random_num == 'paper':
  # you win
  print(f"you: {user_input} | computer: {computer_random_num}")
  print("you wins, scissors beats paper")
elif user_input == 'paper' and computer_random_num == 'rock':
  # you win
  print(f"you: {user_input} | computer: {computer_random_num}")
  print("you wins, paper beats rock")
elif user_input == 'rock' and computer_random_num == 'paper':
  # computer wins
  print(f"you: {user_input} | computer: {computer_random_num}")
  print("computer wins, paper beats rock")
else:
  print(f"you: {user_input} | computer: {computer_random_num}")
  print("draw!!!")