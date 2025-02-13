from data import question_data
import random
class QuestionModel:
    def __init__(self):
        self.text = question_data
        self.question = {}
        self.answer = ""
        self.score = 0
        self.index = 1
        self.tof = "(True/False)"
        self.user_answer = ""
    def pick_random (self):
        self.question = random.choice(self.text)
        self.answer = self.question["answer"]
        self.user_answer = input(f"\nQ.{self.index}: " +
            self.question["text"]
            + f"{self.tof} ?: ")
        if self.user_answer == "end":
            return 1
        return 0
    def check_answer(self):
        if self.user_answer == self.answer:
            self.score += 1
            print("You got it right!")
            print(f"The correct answer was: {self.answer}.")
            print(f"Your current score is {self.score}/{self.index}.")
        else:
            print("That's wrong.")
            print(f"The correct answer was: {self.answer}.")
            print(f"Your current score is {self.score}/{self.index}.")
        self.index += 1
        self.text.remove(self.question)
        if not self.text:
            print("\nRan out of questions, Thanks for playing!")
            print(f"Your final score is {self.score}/{self.index - 1}.")
            return 1
        return 0