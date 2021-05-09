import random as r
from playsound import playsound
from sendmail import sendemail
import datetime
import time
import itertools
username = str(input('please enter your name\n'))
while len(username) < 3:
    print('your username must be least 3 characters')
    username = str(input('please enter your name\n'))
while len(username) > 10:
    print('your username must be less than 11 characters')
    
class Quiz:
    quiz = None
    correct = None
    question1 = None
    list_operations = ['+', "*"]

    @classmethod
    def setoperations(cls, newoperations):
        cls.list_operations = newoperations
        
    @classmethod
    def ask(cls):
        from sampython import math
        randOperator = r.choice(cls.list_operations)
        
        def getrand():
            return r.randint(0, 100)

        if randOperator == "-": 
            rand1 = getrand()
            rand2 = getrand()
            firstNumber = max(rand1, rand2)
            secondNumber = min(rand2, rand1)
            cls.question1 = str(f"{firstNumber}{randOperator}{secondNumber}: ")
        
        elif randOperator == "/":
            secondNumber = getrand()
            randMultiplier = getrand()
            firstNumber = secondNumber * randMultiplier
            cls.question1 = str(f"{firstNumber}{randOperator}{secondNumber}")

        elif randOperator == "+":
            rand1 = getrand()
            rand2 = getrand()         
            cls.question1 =  str(f"{rand1}{randOperator}{rand2}")
        
        elif randOperator == "*": 
            rand1 = getrand()
            rand2 = getrand()          
            cls.question1 = str(f"{rand1}{randOperator}{rand2}")

        strask = cls.question1 + ': '
        cls.quiz = str(input(strask))
        cls.correct = str(math(cls.question1))

        if cls.correct != cls.quiz:
            print('your answer was wrong')
            playsound('audio/lose.wav')
            print('the correct answer was ', cls.correct)
            return False

        if cls.correct == cls.quiz:
            print('this is correct')
            playsound('audio/clap.wav')
            return True

iterable = 0
listquestions = []
listtime = []
listbool = []
listans = []
correcttotal = 0
while iterable < 3:
    start = time.perf_counter()
    ans = Quiz.ask()
    listquestions.append(Quiz.question1)
    if ans == True:
        correcttotal += 1
        end = time.perf_counter()
        totaltime = end - start
        listtime.append(totaltime)
        listbool.append("True")
        listans.append(Quiz.quiz)
        listquestions.append(Quiz.correct)
    else:
        correcttotal += 0
        end = time.perf_counter()
        totaltime = end - start
        listtime.append(totaltime)
        listbool.append("False")
        listans.append(Quiz.quiz)
        listquestions.append(Quiz.correct)
    iterable += 1

now = datetime.date.today()

subject = username + "'s quiz for " + str(now)
body = ""
# for i in listquestions:
#     for x in listtime:
#         for z in listbool:
for (i, x, z, m) in zip(listquestions, listtime, listbool, listans):
    body += f"{i}: input: {m}, in {x:0.2f} seconds, {z}.\n"

print(subject)
print(body)

sendemail(subject , body)

# sendemail(f"{username}'s quiz today:", finalans)

# EXPECTED OUTPUT
# subject: 'ddodo quix today'
# body: 
# "13*39: answer 3, in 18 seconds,  FALSE"
# "3+5: answer 8, in 2 seconds, TRUE"
# "5-2: answer 3, in 10 seconds TRUE"
# "this.correct : 2/3, total time: 30 seconds"