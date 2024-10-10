#-------------------------
def new_game():
    guesses = []
    score=0
    question_num=0

    for key in questions:
        print('#------------------------')
        print(key)
        for option in options[question_num]:
            print(option)

        ans=input("enter the option   :").upper()
        guesses.append(ans)
        score=score+check_ans(questions.get(key),ans)

        
        question_num+=1
    display_score(guesses,score)
    play_again()

   




#-----------------------------


def check_ans(getans,ans):
    if ans==getans:
        print('correct answer')
        return 1
    else:
        print(f'wrong answer :, correct anser is {getans}')
        return 0

    pass

#-----------------------------
def display_score(gues,score):
    print('#------------------------')
    print(score) 
    print('#------------------------')
    for i in gues:
        print(i+" ",end='')
    print ('orgingal answer')
    print('#------------------------')
    for x in questions:
        print(questions.get(x)+ " ",end='')


#------------------------------

def play_again():
     again=input('Do you want to play the game again(Y/N) :').upper()

     if again=='Y':
         new_game()
     else:
         print('thanks for playing')
    




questions={'what is the capital of India?: ': 'A'
           ,"what is the capital of karnataka?" : 'C',
           'What is the capital of AP?'  : 'B',
           'What is the capital of UP?' : 'A'}

options = [["A. Japan", 'B. Russia','C. Delhi']
           ,["A. Kormanagla ", 'B. Bellary','C. Banglore']
           ,["A. Tamil nadu", 'B. Hyderabad','C. Delhi']
           ,["A. Kanpur", 'B. Russia','C. Delhi']]




new_game()
    