# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 13:04:37 2020

@author: WFH-PC19X0VM
"""

# Header Part of the Quiz
def header():
    
    print("Pinoy Trivia Quiz")
    
    Name = input("\nPlease enter your name: ").title()
    print(Name)

header()

#Quiz Items
def quiz():
    
    score = 0
    
    qa={"Which city is known as the 'Walled City?'?": "Intramuros",
        "Which country occupied the Philippines during World War II?": "Japan",
        "Philippines Independence Day is celebrated on what date?": "June 12",
        "Mayon Volcano is located in which province?": "Albay", 
        "Who was the first Filipina to win the Miss International beauty title in 1964?": "Gemma Cruz"}
    
    for q,a in qa.items():
        if input(q + '\nAnswer: ').title() == a:
            print('Correct!')
            score += 1
    
        else:
            print("Sorry. The correct answer is {}.".format(a))
        
    grade = score / len(qa)
    
    if grade > .70:
        print("Congratulations, you passed! Your grade is: {:.0%}".format(grade))
    else:
        print("Please try again. Your grade is {:.0%}".format(grade))

quiz()