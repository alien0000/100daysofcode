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
img=[rock, paper,scissors]
youre_choice=int(input("What do you choose? Type 0 for rock, 1 for paper and 2 foe scissors\n"))
print(img[youre_choice])
comp_choice=random.randint(0,1)
print("computer chose:")
print(img[comp_choice])


if youre_choice>=3 or youre_choice<0:
  print("You typr an invalid number, You lose!!!")
elif youre_choice==0 and comp_choice==2:
  print("You Win")
elif comp_choice==0 and youre_choice==2:
  print("You lose!!")
elif comp_choice>youre_choice:
  print("You Lose")
elif youre_choice>comp_choice:
  print("You Win")
elif youre_choice==comp_choice:
  print("The game id tie!!")