from question_model import QuestionModel

print("Welcome to Quiz Brain")
game = QuestionModel()
while 1:
    if game.pick_random():
        print("Thanks for playing!")
        break
    if game.check_answer():
        break
