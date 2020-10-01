def quiz():
    
    import pickle    
    print("Pinoy Trivia Quiz") 
 
    player_list = {} 
    playagain = ''


    while playagain.lower() != 'no':
    
        name = input("\nPlease enter your name: ").title()
        print(name.title())

        #Quiz items
        qafile = open('qa.pkl', 'rb')
        updated_qa = pickle.load(qafile)
        qafile.close()
        
        score = 0
  
        for q,a in updated_qa.items():
            if input(q + " \nAnswer: ").title() == a:
                score += 1
                print("Correct!")
            else:
                print("Sorry. The correct answer is {}.".format(a))

        grade = (score / len(updated_qa))

        if grade > .70:
            print("Congratulations, you passed! Your grade is: {:.0%}".format(grade))
        else:
            print("Please try again. Your grade is {:.0%}".format(grade))
            
        player_list[name] = score
    
        playagain = input("\nPlay again? 'Yes' or 'No': ").title()
        print()
    
    else:
        print(player_list)
        
        
quiz()


def add_question():
    
    import pickle
    
    qafile = open('qa.pkl', 'rb')
    updated_qa = pickle.load(qafile)
    qafile.close()
        
    question = input("Please input your additional question: ")
    answer = input("Please input the corresponding answer: ")
    updated_qa[question] = answer
    
    qafile = open('qa.pkl', 'wb')
    pickle.dump(updated_qa, qafile)
    qafile.close()
    print("Congratulations! You have successfully added a question!")
    
add_question()

def delete_question():
    
    from time import sleep
    import pickle
    
    qafile = open('qa.pkl', 'rb')
    updated_qa = pickle.load(qafile)
    qafile.close()
    
    print("Question Masterfile: \n")
    
    i = 1
    for q,a in updated_qa.items():
        print("\nQuestion %d : %s" % (i, q ))
        i = i+1
        
    delete = input("Which question do you want to be deleted?\nPlease copy & paste the entire question: ")
    
    del updated_qa[delete]
    
    sleep(1)
    
    qafile = open('qa.pkl', 'wb')
    pickle.dump(updated_qa, qafile)
    qafile.close()
    
    print("\nCongratulations! You have successfully deleted a question!")
    
    sleep(1)
    
    print("\nQuestion Masterfile: \n")
    
    i = 1
    for q,a in updated_qa.items():
        print("\nQuestion %d : %s" % (i, q ))
        i = i+1
    
delete_question()
    
    
    