__author__ = 'Rafayel Gardishyan'

'''
To create your simple survey you should fill out some fields:
QUESTIONS: QUESTIONS = {"Your question":[your, answer, possibilities], "Your second question":[your, second, answer, possibilities]}
SUPERANSWERS: SUPERANSWERS = ["Your superanswers for 1st question", "Your super answers for 2nd question"]
DICT: DICT = {'points': 0, 'maxpoints': (the max of the points for your survey), 'eachquestion': (the points you get for every question if the answer == the superanswer), 'minpercent': (the minimum to get a success message)}

Then save the program and run it.

If you want to remove the watermark or add some other functionality please contact me at rowafean@gmail.com!
Thanks for using my software! Rafayel Gardishyan
'''




#questions: (question : awnsers, ...)
QUESTIONS = {"How old are you":[6,7,8,9,10,11,12,13,14,15,16,17,18,19,">19"], "Your gender":["male", "female"], "Your weight":["<50", ">50"]}
#super answers: (["19", "male", ">50"])
SUPERANSWERS = [19, "male", ">50"]
#point parameters
DICT = {'points': 0, 'maxpoints': 15, 'eachquestion' : 5, 'minpercent': 60}

count = 0

#init a question and get answer 
class QuestionInitAndActions:
    Question = ""
    Answers = []
    SuperAnswer = ""
    Points = 0
    
    def __init__(self, question, answers, superanswer, points):
        self.Question = question
        self.Answers = answers
        self.SuperAnswer = str(superanswer)
        self.SuperAnswer = self.SuperAnswer.lower()
        self.Points = points
        
    def getAnswer(self):
        self.getInput = input(self.Question + " You can choose the folowing answers:" + str(self.Answers)+"\n")
        if self.getInput.lower() == self.SuperAnswer:
            if DICT['points'] < DICT['maxpoints']:
                DICT['points'] += self.Points


#get the questions and init the objects
for key in QUESTIONS:
    question = QuestionInitAndActions(key, QUESTIONS[key], SUPERANSWERS[count], DICT['eachquestion'])
    question.getAnswer()
    count += 1

if DICT['points'] < DICT['maxpoints']:
    percent = (DICT['points'] * 100) / DICT['maxpoints']
else:
    percent = 100

#success or failure message
if percent >= DICT['minpercent']:
    print("Success, you have: " + str(DICT['points']) + " points of " + str(DICT['maxpoints']) + "! \n\nThis survey is created with a free software by Rafayel Gardishyan")    
else:
    print("Failure, you have: " + str(DICT['points']) + " points of " + str(DICT['maxpoints']) + ". \nThat is not enough \n\nThis survey is created with a free software by Rafayel Gardishyan")    

exit = input()