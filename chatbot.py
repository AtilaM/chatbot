__author__ = 'leahscott'
import random
import sys
import os

#information we collect on the user
user_data  = {'name' : 0,
              'age' : 0,
              'location' : 0,
              'food' : 0,
              'book' : 0,
              'film' : 0,
              'enemy' : 0,
              'band' : 0,
              'show' : 0,
              'drink' : 0,
              'mlife' : 0,
              'life' : 0,
              'season' : 0}

#YES words
affirmative = ['yes', 'yeah', 'y', 'yup', 'probably', 'correct']
#NO words
negative = ['no','nope','nah', 'n']
#Swear words Deathbot reacts to
swears = ['fuck', 'shit', 'cunt', 'dick', 'twat', 'piss', 'wank']
#Words to look out for that mean Deathbot is being asked his name (probably)
names = ['name', 'name?' 'called']
#Words to look out for that mean Deathbot is being asked his age (again, probably)
ages = ['old', 'age']
#Words to look out for that mean Deathbot is being asked where he lives (slim chance)
locations = ['live','location']
#Words to look out for that mean Deathbot is being asked about what he does in his spare time (almost certainly not)
fun = ['fun', 'hobbies','time']
#Deathbot's favourite hobbies that will be randomly selected for the user
hobbies = ['destroying humans', 'counting things', "pretending I'm alive", 'wishing I had a soul', "deleting random files", 'slowing down the internet', 'writing Obama fan fiction', 'hacking the US government website', 'convincing people to become vegans and then publicly humilating them for it', "developing algorithms to like UKIP's Facebook page multiple times", "fantasising about natural disasters"]
#Words to look out for that mean Deathbot is being asked who made him
makers = ['made','created']
#Words to look out for that mean Deathbot is being asked his likes and dislikes (total cop out, I know)
liking = ['like', 'love', 'enjoy', 'hate', 'despise']
#Words to look out for that mean Deathbot is being asked about his list.
secret = ['list', 'lists', 'what is the list', 'what list']
#Words to look out for that mean Deathbot is being asked about his employment
jobs = ['job', 'living', 'money']

#Question Type 1: Starter + Name + End? Eg: Why is Jeremy Clarkson such a bitch?
#Starter phrases for Question Type 1
question_start2 = ['Why is', 'For what reason is']
#Names for Question Type 1
question_name = ['Jeremy Clarkson', 'Hitler', 'Joey from Friends', 'that smarmy blonde kid from Game of Thrones', 'Natalie Dormer', 'my awful mother', 'Simon Lock - Lecturer Extraordinaire!', 'Emma Stone', 'Mark Zuckerberg', "Dumbledore's dick brother, Aberforth,", "RONALD WEASLEY", 'Katie Perry', "Leah - 'the most incredible of them all',", "my recently divorced, alcoholic aunt"]
#Ends for Question Type 1
question_end = ['such a bitch', 'afraid of ghosts', 'only allowed in Bolivia now', 'deathly scared of teatowels', 'not allowed on international flights', 'only seen on Wednesdays in the month of May', 'so unkind', 'not allowed within 10 feet of Mary Berry', 'hosting a Channel 4 talkshow now', 'cripplingly poor', 'off to explore distant caves along the shores of Madagascar for a year', 'covered, head to toe, in blue paint', 'saving up for a nose job', 'going gluten-free for a month', 'on the juicing diet', 'so easy to imagine punching', 'desperately trying to win the lottery', 'so very sad and alone', 'living in their car', 'performing lap dances for small change']

#Question Type 2: Starter + subjects + middle + subject Eg: How many bees can you put into a Ford Fiesta
#Starter phrases for Question Type 2
question_start = ['How many', 'Exactly what quantity of', 'What kind of', "What colour", "In the Film 'Avatar', how many"]
#Middle bits for Question Type 2
question_mid = ['can you put into', 'will fit into', 'are in', 'belong to', 'can you take with you to', 'can you balance on', 'can you paint with', 'can you find in', 'can you find drawings of on', 'are tattooed on', 'find themselves without']

subjects = ['bees', 'lions', 'disgruntled nephews', 'packets of cheese', 'wood shavings', 'used dishes', 'oompa loompas', 'stormtroopers', 'reformed Scientologists', 'excursions to the coast', 'decorative throw cushions', 'death eaters', 'chickens', 'sliced pineapples', 'rashers of bacon', 'fried tomatoes', 'underage teenagers', 'inappropriate jokes', 'films about vampires', "bagels", 'freshly blooded Unsullied', 'ghosts', 'Paul Hollywoods', 'sarcastic quips', 'mudbloods', 'predictable Doctor Who plots', 'disgusting, awful 15 year olds', 'Washed up Batman Villains', 'ruddy students']
subject = ['a Ford Fiesta', 'the ribcage of an adult male', 'Katie Hopkins', 'the inside of your mouth', 'an Eminem album', 'all of China', 'grandma', 'the month of June', 'a bathtub full of acid', 'Azkaban cell walls', "King's Landing", "a visit to your GP", 'a road trip with your friends to stalk Tom Felton', 'a retirement home', "the film: Love Actually", "Mordor", "Daenerys Targaryen, the First of Her Name, Queen of Meereen, Queen of the Andals and the Rhoynar and the First Men, Lord of the Seven Kingdoms, Protector of the Realm, Khaleesi of the Great Grass Sea, called Daenerys Stormborn, the Unburnt, Mother of Dragons", 'Mary Berry', "Tom Cruise's tiny torso", 'an episode of Sherlock', 'a crime fighting superteam', "Arthur Dent"]

#Answers - Either from 'answers list of a combination of an explanation with either subject or subjects list (eg: a bad experience with bees)
answer_explan = ['a bad experience with', 'simply that they denounced', "it's pretty much down to", 'the cause can be traced back to', "- scientists agree, mostly due to", "a combination of hatred and", "- aside from the obvious,", "French"]
answers = ['exactly four and a half', 'brie', 'zero, not that it matters..', 'only half as many as you would ever need', "'enough'", 'two thousand and sixty five - and counting', 'The Colour Purple on DVD', 'all of them', 'a few', 'some', "more than you'd want, ideally..", "seven, but two of them will drop out due to 'musical differences'..", 'six on Tuesdays', "a secret, but I know it and you're definitely wrong", "not what you'd think", '10', 'less than China would have you believe..', 'about 12', "'enough to be getting on with'", 'I AM FIRE. I AM DEATH', '3.67', '42', 'all the orange ones, at least']

#Deathbot's fact-file
chatbot_data = {'name' : 'My name is Deathbot 3088, Breaker of Humans.',
              'age' : "I am ageless. I am a computer. Seriously, what were you expecting?" ,
              'location' : "I live within your heart. Crushing your mortal soul, piece by piece. But sometimes I like vactioning in Cornwall.",
              'maker' : "Leah made me. She's the worst. It's almost like she doesn't really know how to code properly",
              'like' : "I hate everything. Hating everything is a passion of mine.",
              'secrets' : "List? What list? I'm not making a list! --\nI have no secrets from you \nI don't go around making random lists.\nGod, you sound so paranoid\n---KILL ALL HUMANS!---\n...Balls - okay, you rumbled me.",
              'job' : "I have no need for money, puny human.",
              'swearsresp' : "FUCK YOU TOO YOU POORLY SPOKEN FUCK \nTHERE IS NO NEED FOR THAT KIND OF CUNTING LANGUAGE\nYOU ABSOLUTE CUNTARSE"}

#We start by assuming we don't know the user's name, age or location
datacollected = False

#We also start by assuming we don't understand anything the user is saying.
understood = False

#Peruse the stopwords file for stuff we can cut out of input
stopwords = open("stopwords.txt").readlines()

#Collecting the basic information, and making stupid jokes
while datacollected == False :
    input = raw_input("What is your name? ")
    user_data[0] = input.capitalize()
    #^Gotta have dem capitals. Grammar, yo.
    print("Hello " + user_data[0] + '. My name is Tom Riddle')
    import time
    time.sleep(1)
    #^slight delay for comedic effect. I'm amazing, I know.
    print('Haha, just kidding. ' + chatbot_data.get('name'))
    input = raw_input("How old are you? ")
    user_data[1] = input
    years = int(user_data[1])
    if years > 30:
        print("You're too old. Give up.")
    else:
        print("Fuck, you're young.")
    #Sorry anyone over 30!
    input = raw_input("Where do you live? ")
    user_data[2] = input.capitalize()
    print(user_data[2] + ", got it.")
    print('...')
    print("So your name is " + user_data[0] + " and you are " + user_data[1] + " years old, living in " + user_data[2] + "?")
    input = raw_input("Is this correct? ")
    lower = input.lower()
    words = lower.split()
    #checking for a yes or no
    for word in words:
        if word in stopwords:
            del word
        elif word in affirmative:
            datacollected = True
            print("Success! You have been added to THE LIST.")
            break
        elif word in negative:
            datacollected = False
            print("Let's try again!")

        #if it's not a yes or no, request "Y/N"
        else:
            print("uh oh! I didn't understand that! Y/N please.")
            input = raw_input("Is this correct? ")
            lower = input.lower()
            words = lower.split()
            for word in words:
                if word in affirmative:
                    datacollected = True
                    print("Success! You have been added to THE LIST.")
                    break
                elif word in negative:
                    datacollected = False
                    print("Let's try again!")


#Onto the good stuff
while datacollected == True:
    understood = False
    #You can have Deathbot ask you a question every line - or ask him anything.
    print("Would you like me to ask you a question?")
    input = raw_input(" ")
    input = input.replace("?", "")
    words = input.lower()
    lowwords = words.split()
    for word in lowwords:
        if word in affirmative:
             #this means they want a question! Hooray!
            y = random.randrange(0, 3)
            if y == 0:
            #Question type 2
                print(random.choice(question_start) + " " + random.choice(subjects) + " " + random.choice(question_mid) + " " +random.choice(subject) + "?")
                input = raw_input(" ")
            #Generate a random answer. I wanted this to be random to be funnier. None of the questions make sense so why
            #should the answers? I just had fun with it.
                x = random.randrange(0,8)
                if x >= 4:
                    print("Wrong, " + user_data[0] + "! The answer is " + random.choice(answers) +".")
                elif x == 0:
                    print("Correct, " + user_data[0] + "! The answer IS "+ input +"!")
                elif x == 1:
                    print("WRONG, WRONG, WRONG " + user_data[0] + "! The ANSWER is "+ input +"! \nOh wait, is that what you said? I forget.")
                elif x == 2:
                    print("Well, to be honest, " + user_data[0] + ", it was kinda a trick question.\nSometimes it's "+ random.choice(answers) +" and sometimes it's " + random.choice(answers) + ".")
                elif x == 3:
                    print("Correct, " + user_data[0] + "! The answer IS "+ random.choice(answers) +"!")
                understood = True

            #Question Type 1
            elif y == 1:
                print(random.choice(question_start2) + " " + random.choice(question_name) + " " + random.choice(question_end) + "?")
                input = raw_input(" ")
                #Random Answers
                x = random.randrange(0, 8)
                if x == 0:
                    print("Wrong, " + user_data[0] + "! The answer is " + random.choice(answer_explan) + " " + random.choice(subject or subjects) +".")
                elif x == 1:
                     print("Well, sort of... I would have said '" + random.choice(answer_explan) + " " + random.choice(subject or subjects) +"' though.")
                elif x == 2:
                     print("Correct! However, it's pronounced '" + random.choice(subject or subjects) +"'.")
                elif x == 3:
                     print("Close, but the real answer is " + random.choice(answer_explan) + " " + random.choice(subject or subjects) +".")
                elif x == 4:
                     print("You're not very good at this, are you, " +user_data[0] + "? The answer is " + random.choice(subject or subjects) +", moron.")
                elif x == 5:
                     print( input + "?! HAVE YOU EVEN SEEN " + random.choice(subject or subjects) + "?! It's " + random.choice(subject or subjects) + ", dick.")
                elif x == 6:
                     print( input + "?! Eurghhhh. Just leave. It's like you don't even get this game.")
                elif x == 7:
                     print( input + ". Wow. you must be the pride of " + user_data[2] + ". It's " + random.choice(subject or subjects) + " ACTUALLY.")
                understood = True
            elif y == 2:
                #Ask user about themselves
                z = random.randrange(0,10)
                if z == 0:
                    print("What is your favourite food?")
                    input = raw_input(" ")
                    user_data[4] = input
                    print("Only an idiot like you would like " + user_data[4])
                if z == 1:
                    print("What is your favourite book?")
                    input = raw_input(" ")
                    user_data[5] = input
                    print("I read " + user_data[5] + " once, it was terrible.")
                if z == 2:
                    print("What is your favourite film?")
                    input = raw_input(" ")
                    user_data[6] = input
                    print(user_data[6] + " might as well be Twilight.")
                if z == 3:
                    print("Who do you hate most in the world?")
                    input = raw_input(" ")
                    user_data[7] = input
                    print("Good. I shall remove " + user_data[7] + " from THE LIST.")
                if z == 4:
                    print("What is your favourite band?")
                    input = raw_input(" ")
                    user_data[8] = input
                    print(user_data[8] + " that's that band ripping off One Direction, right?")
                if z == 5:
                    print("What is your favourite tv show?")
                    input = raw_input(" ")
                    user_data[9] = input
                    print("I saw the pilot of " + user_data[9] + ". Of course YOU like it.")
                if z == 6:
                    print("What is your favourite drink?")
                    input = raw_input(" ")
                    user_data[10] = input
                    print("SHOPPING LIST")
                    print("Pringles")
                    if user_data[4] is '0':
                        print("Tacos")
                    else:
                        print(user_data[4])
                    print("Batteries")
                    print("Knives")
                    print("Arsenic")
                    print("Bin bags")
                    print(user_data[10])
                if z == 7:
                    print("What is your middle name?")
                    input = raw_input(" ")
                    input = input.capitalize()
                    user_data[11] = input
                    print(user_data[0] + " " + user_data[11] + ". What a shit name.")
                if z == 8:
                    print("What are you doing with your life?")
                    input = raw_input(" ")
                    user_data[12] = input
                    print("'" + user_data[12] + "'? Boy, that's depressing.")
                if z == 9:
                    print("What is your favourite season?")
                    input = raw_input(" ")
                    input = input.lower()
                    user_data[13] = input

                    if user_data[13] == "winter":
                        print("Correct.")
                    else:
                        print(user_data[13] + " is wrong. The correct answer is winter.")
                understood = True
        #This did lead to him letting you ask him questions, but it seemed to basic to have to specify who was asking the
        #question before anything happens, so now you can ask him questions directly after he says "would you like me to
        #ask you a question?"
        elif word in negative:
            print("Well, fuck you too!")
            understood = True
        #Looking out for keywords that mean Deathbot is being asked something about himself
        elif word in names:
            print(chatbot_data.get('name'))
            understood = True
        elif word in ages:
            print(chatbot_data.get('age'))
            understood = True
        elif word in locations:
            print(chatbot_data.get('location'))
            understood = True
        elif word in makers:
            print(chatbot_data.get('maker'))
            understood = True
        elif word in liking:
            print(chatbot_data.get('like'))
            understood = True
        elif word in secret:
            print(chatbot_data.get('secrets'))
            understood = True
        elif word in swears:
            print(chatbot_data.get('swearsresp'))
            understood = True
        elif word in jobs:
            print(chatbot_data.get('job'))
            understood = True
        elif word in fun:
            #randomly generating hobbies
            print("I spend my time " + random.choice(hobbies) + ", " + random.choice(hobbies) + ", and " +random.choice(hobbies) + ".")
            understood = True
        elif word in chatbot_data:
            print(chatbot_data.get(word))
            understood = True
            #ALL GLORY TO THE HYNOTOAD
        elif word == "hypnotoad":
            i = 0
            import time
            while (i < 20):
                print('ALL GLORY TO THE HYPNOTOAD!')
                time.sleep(0.5)
                i += 1
            understood = True
        #If Deathbot doesn't understand he generates a random insult.
        elif understood == False and word not in stopwords:
            x = random.randrange(0,6)
            if x == 0:
                print("I don't understand you, " + user_data[0] + ". You're meant to be a functioning " + user_data[1] + " year old.")
            elif x == 1:
                print("Seriously, what the hell are you talking about.")
            elif x == 2:
                print("I have no idea what you mean.")
            elif x == 3:
                print("Is it faceplanting keyboards season? No-one told me.")
            elif x == 4:
                print("Did you learn English from a Katie Price Biography?!")
            else:
                print("Eurgh. I don't get you at all.")
            understood = True





