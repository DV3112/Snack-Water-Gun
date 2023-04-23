'''
Hey Floks I'm Devansh from this side 

-> Here's the Game of Snack-Water-Gun , which we used to play in our childhood 

-> I was learning python from  one man army ("CODE WITH HARRY") And this is the part of my learing 
so I thought let's upload it with comments on github , so that others can easily understand it

***Hope You''ll like it and enjoy it****

'''
import random

# creating the function
def gameWin(comp, you):
    if comp == you:
        return None
    elif comp == "s":  # if random slect snack
        if you == "w":
            return False
        elif you == 'g':
            return True
    elif comp == "w":  # if random slect Water
        if you == "s":
            return True
        elif you == 'g':
            return False
    elif comp == "g":  # if random slect Gun
        if you == "s":
            return False
        elif you == 'w':
            return True

# Taking the input from computer by random function
print("Computer Turn: snack(s)  Water(s) Or Gun(g)?")
randNO = random.randint(1, 3)

# storing the value in varriable
if randNO == 1:
    comp = 's'
elif randNO == 2:
    comp = 'w'
elif randNO == 3:
    comp = 'g'

# taking the input from user
you = input("your Turn: snack(s)  Water(s) Or Gun(g)?")

a = gameWin(comp, you)  # Run the Function

print(f"Computer chose :- {comp}")
print(f"you chose :- {you}")


# check the both iuput and Give the results
if a == None:
    print("the game is tie")
elif a:
    print("***you win***")
else:
    print("!!you lose!!")
