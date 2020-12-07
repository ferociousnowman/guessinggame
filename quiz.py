import random
 
hidden = random.randrange(1, 9)

 
guess = int(input("Please enter your guess: "))
 
if guess == hidden:
    print ("correct")
elif guess < hidden:
    print ("wrong guess,guess a smaller number")
else:
    print ("wrong guess,guess a higher number")