#  Personalized insult generator that asks the users name and then returns a random insult from the available list that includes their name in the insult.
def insult(myname):
    print(myname + ', if you aren\'t an idiot, you made a world-class effort at simulating one.')
    print(myname + ' has the personality of wallpaper.')
    print('I will never get over the embarrassment of belonging to the same species as ' + myname + '.')
    print(myname + ' has bad breath!')
    print('Someday ' + myname + ' will go far. I hope they stay there forever.')
    print(myname + ', I have neither the time nor the crayons to explain this to you.')


print('Hi, what\'s your name?')

myName = input()  # get name from user

insult(myName)
