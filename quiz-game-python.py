#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Test - Quiz Game

class Question:
   def __init__(self, text, choices, answer):
       self.text = text
       self.choices = choices
       self.answer = answer

   def check_answer(self, user_answer):
       return user_answer == self.answer

class Quiz:
   def __init__(self, questions):
       self.questions = questions
       self.score = 0
       self.question_index = 0

   def display_question(self):
       current_question = self.questions[self.question_index]
       print(f"Question {self.question_index + 1}: {current_question.text}")
       for i, choice in enumerate(current_question.choices, start=1):
           print(f"{i}. {choice}")

   def next_question(self):
       self.question_index += 1

   def run_quiz(self):
       for question in self.questions:
           self.display_question()
           user_input = input("Enter the number of your answer: ")
           if user_input.isdigit():
               user_answer = int(user_input) - 1
               if 0 <= user_answer < len(question.choices):
                   if question.check_answer(user_answer):
                       print("You got the correct answer!\n")
                       self.score += 1
                   else:
                       print(f"Wrong. The correct answer was {question.choices[question.answer]}\n")
                   self.next_question()
               else:
                   print("Invalid choice. Try again.\n")
           else:
               print("Invalid input. Please enter a number.\n")

       print(f"Quiz completed! Your score is {self.score}/{len(self.questions)}.")

# List of Questins
q1 = Question("How many Apollo missions landed on the moon?", ["One (1)", "Four (4)", "Six (6)", "Eight (8)"], 2)
q2 = Question("Which country is the Taj Mahal in?", ["Sri Lanka", "Bangladesh", "Philippines", "India"], 3)
q3 = Question("How many bits make one byte?", ["8", "15", "100", "1"], 0)


questions = [q1, q2, q3]

# Call the function
quiz = Quiz(questions)
quiz.run_quiz()


# In[ ]:




