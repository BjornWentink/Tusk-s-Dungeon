# This program is a comedic CYOA game.
# The user will be able to choose which path they'd like venture.
# To win, the user must choose one of the correct paths and complete a challenge.

def main():
    # Manage saved game (if applicable).
    checkPoint = CheckForSavedGame()
    checkPoint = AskForReset(checkPoint)

    # Declare local variables.
    dec_1A = 'undef'
    dec_2B = 'undef'
    userName = 'Michael Scott'
    brankruptcy = True
 
    # Path 1A: Game start
    if checkPoint == 'null':
        WelcomeUser()
        BeginNarrationSequence()
        checkPoint = SaveCheckPoint('1A', userName)
    if checkPoint == '1A':
        dec_1A = GetDecision_1A()

    # Path 2A: *DEAD END*
    if dec_1A == 'Path_2A':
        UserDies_2A()

    # Path 2B: Enter dungeon
    if dec_1A == 'Path_2B':
        checkPoint = SaveCheckPoint('2B', userName)
    if checkPoint == '2B':
        NarratePath_2B()
        userName = GetUserName()
        dec_2B = GetDecision_2B()

    # Path 3A: Left tunnel
    if dec_2B == 'Path_3A':
        checkPoint = SaveCheckPoint('3A', userName)
    if checkPoint == '3A':
        NarratePath_3A()
        PickNumbChallenge()

    # Path 3B: Right tunnel
    if dec_2B == 'Path_3B':
        checkPoint = SaveCheckPoint('3B', userName)
    if checkPoint == '3B':
        NarratePath_3B()
        B_BallChallenge()        
# End of main().

# Save game functions...
checkPointLibrary = ['1A', '2B', '3A', '3B']

def SaveCheckPoint(checkPoint, userName):
    saveGameFile = open('Tusks Dungeon Saved Game', 'w')
    saveGameFile.write(checkPoint + '\n')
    saveGameFile.write(userName + '\n')
    saveGameFile.close()
    if checkPoint != 'null':
        print('\nCHECKPOINT REACHED! GAME SAVED.')
        return checkPoint

def CheckForSavedGame():
    saveGameFile = open('Tusks Dungeon Saved Game', 'a')
    saveGameFile.write('')
    saveGameFile.close()

    saveGameFile = open('Tusks Dungeon Saved Game', 'r')
    checkPoint = saveGameFile.readline()
    checkPoint = checkPoint.rstrip('\n')
    saveGameFile.close()
    if checkPoint in checkPointLibrary:
        return checkPoint
    else:
        return 'null'

def AskForReset(checkPoint):
    if checkPoint in checkPointLibrary:
        answer = input('\nPrevious game detected. Continue from last checkpoint?' +
                       '\nEnter y/n:  ')
        while answer != 'y' and answer != 'n':
            answer = input('Invalid response. Please enter "y" or "n":  ')
        if answer == 'y':
            print('\nContinuing from last saved checkpoint...\n')
            return checkPoint
        if answer == 'n':
            print('\nStarting new game...\n')
            return 'null'
    return 'null'

# Path 1A functions...
def WelcomeUser():
    input   ('Welcome to Tusk\'s Dungeon' +
            '\nPress ENTER to begin your quest...  ')

def BeginNarrationSequence():
    input   ('\nNARRATOR: "You are a knight on a royal mission given by princess Pear ' +
            'to search for ancient, mystical artifacts that will protect ' +
            'your humble kingdom..."\n(Press ENTER to continue)  ')
    
    input   ('\n"It is well known that the ruined lands of former Natas ' +
             'contain many such treasures. There are artifacts with powers that were ' +
             'used to defeat enormous armies. Despite the vast dangers of this region ' +
             'you decide that is where you will make your search. For country, and for ' +
             'honor..."\n(Press ENTER to continue)  ')

    input   ('\n"You spend 4 days turning over every rock and ruin only to gather a ' +
             'collection of unremarkable fruits, Roobles, and rusty knives. With tear ' +
             'soaked eyes you rage and start stomping and pumping your fists in ' +
             'frustration swearing you \'quit.\'\n(Press ENTER to continue)  ')

def GetDecision_1A():
    answer = input  ('\n"In your fit a Bananza is dislodged from your inventory ' +
                     'unnoticed. You trip and tumble into a dead tree which gives on ' +
                     'impact. Underneath where the dead tree once stood is a trap door."' +
                     '\n\n    Your reaction is...\n    1: "I don\'t like the looks of ' +
                     'this. It\'s time to go home."\n    2: "Sweet, a secret entrance. ' +
                     'There\'s bound to be something valueble down there."' +
                     '\n\nType "1" or "2" to choose then hit ENTER:  ')

    while answer != '1' and answer != '2':
        answer = input      ('\nInvalid response, you dingus. Try again and this time ' +
                             'follow directions.\nType "1" or "2" to choose then ' +
                             'hit ENTER:  ')
    if answer == '1':
        return 'Path_2A'
    if answer == '2':
        return 'Path_2B'

# Path 2A function...
def UserDies_2A():
    input   ('\nNARRATOR: Uh, okay. Weird choice but I guess it\'s my fault for making ' +
             'it an option. "Despite your previous relentless devotoion to your mission ' +
             'you\'ve had enough. You\'re tired, you\'re hungry, and ready to head ' +
             'toward the nearest Inn. Wiping your tears you grab a bananza from your ' +
             'inventory and take a bite. Something tastes off about this fruit.' +
             '\n\nYou die of dysentary two days later. GAME OVER' +
             '\n(Press ENTER to restart game in disgrace)  ')
    main()

# Path 2B function...
def NarratePath_2B():
    input   ('\n"You climb down a ladder leading from the trap door. The way is cold ' +
             'and dark but you finally feel your feet touch the floor. You find a torch ' +
             'and light it. From the shaddows a hooded figure appears."' +
             '\n(Press ENTER to continue)  ')

    input   ('\nTUSK: \"Greetings, traveler. My name is Sir Johnson but you may call me ' +
             'Tusk, the dungeon master. These walls talk to me and I know you have ' +
             'taveled long and hard in search for treasure."\n(Press ENTER to continue)  ')

def GetUserName():
    userName = input('\n"I have good news for you. But firt, may I ask, what is your name?"' +
                     '\nType your name and hit ENTER:  ')
    while userName == '':
        userName = input('\nToo shy to give me a response, eh? Don\'t worry, I only need it ' +
                         'to sign up for a new credit card.' +
                         '\nType your name and hit ENTER:  ')

    saveGameFile = open('Tusks Dungeon Saved Game', 'w')
    saveGameFile.write('2B\n')
    saveGameFile.write(userName + '\n')
    saveGameFile.close()
    
    input   ('\nTUSK: "' + userName + '" Ha! Parents had a sense of humor I see? Well ' +
             userName + ' the good news is your search is over. Down here there are items ' +
             'powerful beyond measure. All you must do is prove yourself worthy."' +
             '\n(Press ENTER to continue)  ')
    return userName

def GetDecision_2B():
    answer = input('\n"As you can see there are two diverging paths from this point. ' +
                   'For your first trial you will choose a direction to travel."' +
                   '\n\nNARRATOR: "You notice the (1)path to your left is dark and creepy. ' +
                   'Bats fly from the narrow entrance and startle you. ' +
                   'The (2)path to your right looks more welcoming. It\'s wider ' +
                   'and appears more travelled.\n\n    I want to...' +
                   '\n    1) "Go down the path less travelled. I\'m not like those basic ' +
                   'knights after all."\n    2) "I\'ve seen Indiana Jones. The nicer ' +
                   'choice is the wiser choice."\n\nType "1" or ' +
                   '"2" to choose then hit ENTER:  ')

    while answer != '1' and answer != '2':
        answer = input('\n\n"K\'mon, lets stop playing games..."' +
                       '\nType "1" or "2" to choose then hit ENTER:  ')
    if answer == '1':
        return 'Path_3A'
    if answer == '2':
        return 'Path_3B'

# Path 3A functions...
def NarratePath_3A():
    input   ('\nNARRATOR: "Heart pounding you bravely go down the scary tunnel. No ' +
             'mountain too high, no valley too low, and certainly no cave long enough ' +
             'to keep you from getting to your bounty."\n(Press ENTER to continue)  ')

    saveGameFile = open('Tusks Dungeon Saved Game', 'r')
    skipLine = saveGameFile.readline()
    userName = saveGameFile.readline()
    userName = userName.rstrip('\n')      
    saveGameFile.close()

    input   ('\n"You reach the end of the tunnel to find a room with a frog resting ' +
             'on a pedestal. An opening in the ceiling allows a beam of moonlight to ' +
             'draw focus on it. Obviously the frog is part of the test."' +
             '\n\n    What do you do?...\n    1: "I know what this is. Time to ' +
             'pucker up."\n    2: "' + userName + ' smash!"\n\nType "1" or "2" ' +
             'to choose then hit ENTER:  ')

    input   ('\nNARRATOR: \"You reach for the frog but before making contact a ' +
             'booming voice comes from the ceiling, \'I know your sins, my child. ' +
             'Pray to me so your heart may be pure enough to weild the Holy Talisman.' +
             '\n\n    Your response is...\n    1: "I\'m Budhist."\n    2: "Can\'t there ' +
             'be some other way?"\n\nPress "1" or "2" to choose then hit ENTER:  ')

def PickNumbChallenge():
    usersGuess = input('\nHmm, I suppose you can guess what number I\'m thinking of ' +
                       'instead. The number is between 1 and 10. I\'ll give you 3 ' +
                       'chances."\nType your guess then hit ENTER:  ')
    usersGuess = GetValidResponse(usersGuess)
    
    import random
    answer = random.randint(1,10)
    chances = ['SECOND', 'LAST']

    for chancesLeft in chances:
        if usersGuess > answer:
            usersGuess = input('\n\"Your guess is too high and mighty. Just like me. ' +
                               'Guess lower."\nType your ' +
                               chancesLeft + ' guess and hit ENTER:  ')
            usersGuess = GetValidResponse(usersGuess) 

        elif usersGuess < answer:
            usersGuess = input('\n"Your guess is too low. You need to go higher."' +
                               '\nType your ' + chancesLeft + ' guess and hit ENTER:  ')
            usersGuess = GetValidResponse(usersGuess)

        elif usersGuess == answer:
            ShowWinOutcome()

    if usersGuess == answer:
        ShowWinOutcome()

    answer = str(answer)
    input('\n"You have chosen... poorly. The number was ' + answer +
          '."\n\nNARRATOR: A mystical wind swoops in and ' +
          'causes you to lose all control of your bowels. You die of dysentary. ' +
          'GAME OVER\n\n(Press ENTER to restart game in disgrace)  ')
    main()

def GetValidResponse(usersGuess):
    validResponses = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    while usersGuess not in validResponses:
        usersGuess = input('\nStop testing my patience.\nGuess a valid number:  ')
    return int(usersGuess)

def ShowWinOutcome():
    input('\nThat\'s right! Jesus me, how\'d you know? Deal\'s a deal, I guess, ' +
                  'so here\'s your Talisman!\nNARRATOR: "You got an artifact. YOU WIN!"' +
                  '\n(Press ENTER to close the game like a CHAMPION)  ')
    sys.exit()

# Path 3B functions...
def NarratePath_3B():
    input   ('\nNARRATOR: "Feeling self-assured about your choice you confidently ' +
             'pace down the second tunnel. As you near the end, the sound of a crowd\'s ' +
             'roar echoes through the walls and becomes louder as you advance. ' +
             'You are reminded of your days as a jouster but this crowd seems larger and ' +
             'more sinister."\n(Press ENTER to continue)  ')

    input   ('\n"As you approach the colosseum an other-worldly music reverberates, \'Come ' +
             'on and SLAM! And welcome to the JAM! Come and SLAM! If you wanna JAM...\' ' +
             'You are mortified by the threats and over stimulation but your mission ' +
             'compels you to proceed."\n(Press ENTER to continue)  ')

def B_BallChallenge():
    riskLvl = input('\n"You enter the arena to find a tall man holding an orange ball ' +
                    'standing next to a raised hooped structure."\n' +
                    '\nFRIAR JORDAN: \"You who have enetered my temple. Defeat me at a ' +
                    'game of 1V1 and I shall reward you with the Shoes of Flight."\n' +
                    '\n    What is your strategy?...\n    1: Go for the lay-up (low risk)' +
                    '\n    2: Go for the 3-pointer (medium risk)\n    3: DUNK IT! (high risk)' +
                    '\n    4: Go for the cheap shot (???)\n\nType 1,2,3, or 4 to select ' +
                    'your choice and press ENTER:  ')
    validResponses = ['1', '2', '3', '4']
    while riskLvl not in validResponses:
        riskLvl = input('Invalid response. Get your head in the game:  ')
    riskLvl = int(riskLvl)

    success = False
    import random
    chanceOfSucess = random.randint(1,(2 * riskLvl))
    winCondition = random.randint(1,(2 * riskLvl))
    if chanceOfSucess == winCondition:
        success = True

    if success and riskLvl == 1:
        input   ('\nNARRATOR: "You descide to play it safe. You dribble down the ' +
                 'court with haste. Friar Jordan tries to block your advance but you ' +
                 'psyche him out with a fake toss to the face. He falls backwards and ' +
                 'your path is clear to make your shot next to the hoop. The crowd cheers ' +
                 'in amusment."\n\nFIAR JORDAN: "I did not see that coming. A worthy ' +
                 'prize for a worthy apponent. "\n\n\"Friar Jordan hands you the Shoes ' +
                 'of Flight. Your princess will be pleased. YOU WIN!\n\n(Press ENTER ' +
                 'to close game as the new "Rookie of the Year")  ')
        sys.exit()
    elif success == False and riskLvl == 1:
        input('\nNARRATOR: "You descide to play it safe. You attempt to dribble but ' +
              'your laces are undone. Your heavy armor makes a loud noise as you fall ' +
              'flat on the wooden floor. Friar Jordan didn\'t even have to move. The ' +
              'crowd laughs and you literally die of embarrassment." GAME OVER' +
              '\n\n(press ENTER to restart game in disgrace)  ')
        main()

    if success and riskLvl == 2:
        input('\nNARRATOR: "You think this guy is probably too skilled to go around ' +
              'so you descide to throw the ball over him. However, this strategy ' +
              'agaisnt a near giant won\'t be an easy task. Luckily, you remember ' +
              'an ancient spell taught to you by the royal mage. As you sling the ' +
              'ball you chant \'KOBE!\' and it follows your focus. ' +
              'It\'s good!"\n\nFRIAR JORDAN: "I\'m not sure how you ' +
              'made that shot but a deal\'s a deal."\n\nNARRATOR: "Fiar Jordan hands ' +
              'you the Shoes of Flight. YOU WIN!\n\n(press ENTER to close the game like ' +
              'an ALL-STAR)  ')
        sys.exit()
    elif success == False and riskLvl == 2:
        input('\nNARRATOR: "You think this guy is probably too skilled to go around so ' +
              'you descide to throw the ball over him. You aim as best as you\'re able ' +
              'but Friar Jordan is too tall and manages to swat the ball from mid-air. ' +
              'It comes flying down at great velocity and hits you in the gut. You die ' +
              'of dysentary." GAME OVER\n\n(press ENTER to restart game in disgrace)  ')
        main()

    if success and riskLvl == 3:
        input('\nNARRATOR: \"Winning with points is only half the game. You know from ' +
              'your jousting days a true victor wins the hearts of the crowd. You ' +
              'charge Jordan straight on. Right as he leans to swat the ball you jump ' +
              'and use his head to launch your self towards the hoop. Your body performs ' +
              'a front flip before you extend your arm and deliver the sweetest slam ' +
              'dunk anyone has ever seen. THE CROWD GOES WILD!!!"\n\nFIAR JORDAN: How ' +
              'did you do that!? I\'m not worthy. Take these shoes and be gone.' +
              '\n\nNARRATOR: "Friar Jordan gives you the Shoes of Flight. YOU WIN!"' +
              '\n\n(press ENTER to close game as the GOAT!)  ')
        sys.exit()
    elif success == False and riskLvl == 3:
        input('\nNARRATOR: \"Winning with points is only half the game. You know from ' +
              'your jousting days a true victor wins the hearts of the crowd. You ' +
              'dribble straight for the hoop and calculate where you need to jump ' +
              'to dunk but your heavy armor prevents you from going higher than a few ' +
              'inches. It looks pathetic."\n\n FRIAR JORDAN: "Unworthy!"\n\n"Jordan\'s ' +
              'eyes illuminate to a bright blue. You spontaneously combust. GAME OVER' +
              '\n\n(press ENTER to restart game in disgrace)  ')
        main()

    if riskLvl == 4:
        input('\nNARRATOR: \"You may be a knight but you also know honor only feels good ' +
              'if you win. As soon as Jordan passes you the ball you toss it back with ' +
              'full might at his sensitive region. While he\'s left in fetal possition ' +
              'you make a beeline for the magic shoes. The crowd boos as you fly away to ' +
              'your kingdom. YOU WIN, YOU FILTHY CHEAT!' +
              '\n\n(press ENTER to close the game with no honor)  ')
        sys.exit()
               
# Call main.   
main()
