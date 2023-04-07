
import random
def asci(a):
    if a==1:
        print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
        ''')
    elif a==2:
        print('''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
''')
    elif a==3:
        print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')
for i in range(3):
    r1=random.randint(1,3)
    turn=int(input("1 for stone, 2 for paper, 3 for scissor\n"))
    asci(r1)
    if turn==1:
        if r1==1:
            print("Draw")
        elif r1==2:
            print("you lose")
        else:
            print("win")
    elif turn==2:
        if r1==1:
            print("You win")
        elif r1==2:
            print("Draw")
        else:
            print("You lose")
    elif turn ==3:
        if r1==1:
            print("You Lose")
        elif r1==2:
            print("You Win")
        else:
            print("Draw")