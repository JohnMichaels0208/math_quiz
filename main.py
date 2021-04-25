import random as r
import sampython as calculator
from playsound import playsound
# username = str(input('please enter your name\n'))
# while len(username) < 3:
#     print('your username must be least 3 characters')
#     username = str(input('please enter your name\n'))
# while len(username) > 10:
#     print('your username must be less than 11 characters')
# password = int(input('please enter your password\n'))
# while type(password) == str:
#     print('your password must contain numbers')
#     password = int(input('please enter your password\n'))
# mylist = [
# {username: password}
# ]
list_operations = ['+', '-']
question = '{}{}{}'.format(r.randint(0, 100), r.choice(list_operations), r.randint(0, 100))
question1 = ''
for i in question:
    question1 += i
quiz = str(input(question1))
calculator.math(question)
correct = str(calculator.math(question))

while correct != quiz:
    print('your answer was wrong')
    playsound('audio/lose.wav')
    quiz = str(input(question1))
if correct == quiz:
    print('correct')
    playsound('audio/clap.wav') 

    
    
