import random
class Question:
    def __init__(self,text,choices,answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def chechAnswer(self, answer):
        if answer not in self.choices:
            raise ValueError("Hatalı bir giriş yaptınız.")
        else:
            return self.answer == answer

    
class Quiz:
    def __init__(self,questions) :
        self.questions =random.sample(questions, len(questions))
        self.questionsIndex = 0
        self.score = 0


    def getQuestions(self):
        return self.questions[self.questionsIndex]
    
    def displayQuestion(self):
        self.displayProgress()
        question = self.getQuestions()
        print(f"Soru {self.questionsIndex+1}: {question.text}")
        for q in question.choices:
            print("-" + q)

        answer = input("Cevap :")
        if answer == question.answer:
            self.score +=1

        self.questionsIndex += 1

        if len(self.questions) == self.questionsIndex:
            print(f"Test Sonucunuz : {self.displayScore()}")
        else:
            self.displayQuestion()

    def displayScore(self):
        questionsScore = 100/len(self.questions)
        score = questionsScore * self.score
        return score
        
    def displayProgress(self):
        progress = f"{len(self.questions)} sorunun {self.questionsIndex+1}. sorusundasınız."
        print(progress)


    def loadQuestion(self):
        return self.displayQuestion()

        


        
    

q1 = Question("en iyi programlama dili hangisidir?",["python","c#","java","dart"],"python")
q2 = Question("en popüler programlama dili hangisidir?",["python","java","c#","dart"],"python")
q3 = Question("en çok kazandıran programlama dili hangisidir?",["python","java","dart","c#"],"python")
q4 = Question("en farklı kazandıran programlama dili hangisidir?",["python","java","dart","c#"],"python")

questions = [q1,q2,q3]

quiz = Quiz(questions)


quiz.loadQuestion()