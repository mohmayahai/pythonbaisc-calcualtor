fruits=['apple','banana','pineapple','cocounut']
vegetable = ['celelery', 'carrots','potatos']
meats =['chicken','fish','turkey']

groceries = [fruits,vegetable,meats]

print(groceries[2][2])

# for x in groceries:
#     print(x)
#     for y in x:
#         print(y)

questions = ('How many elements are in periodic table: ',
             'which animal lays the largest egg?: ',
             'what is the most abundnat gas in earth?: ',
             'how many bones in the humna body?: ',
             'which plane in the solar systme is the hottest?: ')

options=(('A. 1223,','B. 123','C . 116'),
         ('A. Ostrich','B Elephant', 'C. XYZ'),
         ('A. Oxygen', 'B. Nitrogen','C. CO2'),
         ('A. 206','B. 208', 'C. 209'),
         ('A . Mercury','B. Jupiter','C.Venus'))
                                         

answers=('C','A','B','A','A')
guess =[]
score =0
question_num = 0
for question in questions:
    print("---------------------------------------")
    print(question)

    for option in options[question_num]:
        print(option)

    guess =input("Enter options   ").upper()

    if guess == answers[question_num]:
        score+=1
        print('Correct')
    else:
        print('Incorrect')
        print(f'Correct answer is {answers[question_num]}')

    question_num+=1


print('-------*******---------********')
print(f'final score : {score}')
print('-------*******---------********')
print(question_num)