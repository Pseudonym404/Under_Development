def main ():
#Introduction 
  print ("It was fun playing with you, maybe we will play \nagain later.")
print ("Hello adventurer, I am Taskmaster!") 
#Creating name input 
name = input ("What is your name?")
#Introduction to game
response = input (f"Would you like to play a game, {name}? (Yes or No) ")

#Game Begins
if response == ("Yes"):
    print (f"Welcome to choose your own adventure.")
    print (f"You are getting out of school and a stranger trys \n to talk to you.") 
    response = input (" What do you do?\n 1 Talk to them or 2 Don't talk to them. ")
elif response == ("No"):
  print (f"Maybe in the future we can play {name}.") 
else: 
  print("Choose 1 or 2")
#If talk or don't talk is chosen
if response == ("1"):
    print ("You failed the stranger danger test.") 
elif response == ("2"):
   print ('Congratulations,\nyou passed the stranger danger test!')
else: print ("Invalid answer try again. (1 or 2)")
#First scripture lesson
print(' \nEphesians 6:1-4 NIV [1] Children, obey your parents in \nthe Lord, for this is right. [2] “Honor your father and\nmother”—which is the first commandment with \na promise— [3] “so that it may go well with you and \nthat you may enjoy long life on the earth.” [4] Fathers, \ndo not exasperate your children; instead, bring them \nup in the training and instruction of the Lord. eph.6.1-4.NIV \n \nYou are leaving the schoolground walking home.')
#Second stranger test, the lost dog.
reponse = input ("As you are walking, you pass a park and someone\n asks you to help them find their dog.\n What do you do?\n 1. Help them or 2. Walk away. Choose '1 or 2'")
if reponse == ("1"):
  print("You were hurt when the dog bit you.\n When you get home you see your parents are mad at\n you. Matthew 15:27 'Yes, Lord,' she said, 'even\n the dogs eat the crumbs that fall from their\n master’s table.'")
elif response == ("2"):
  print ("You kept walking and made it home safely.") 
else: print ("Choose '1 or 2'.")
main()