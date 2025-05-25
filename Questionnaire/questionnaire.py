#List of questionnaire with dictionary inside
questions = [
    {
        'Question' : 'Which programming language is that?',
        'Options' : ['Java', 'Python', 'C#', 'Ruby'],
        'Answer' : 'Python'
    },
    {
        'Question' : 'What is my name?',
        'Options' : ['Pedro', 'Can', 'João', 'Kaleb'],
        'Answer' : 'João'
    },
    {
        'Question' : 'Which year was I born?',
        'Options' : ['1996', '2000', '1992', '1994'],
        'Answer' : '1994'
    },
    {
        'Question' : 'Where do I live?',
        'Options' : ['Dublin', 'Brazil', 'Izmir', 'Lisbon'],
        'Answer' : 'Dublin'
    },
]

#Variable to store the total of right answers
right_answers_total = 0

#First for to take the question
for question in questions:
    print(f'Question: {question['Question']}\n')
    print('Options:')
    
    #Using enumerate and the dictionary value to print the options
    for option_number, option_answers in enumerate(question['Options']):
        print(f'{option_number}) {option_answers}')
    print()
    
    #Reading answer and converting it to int to check the value index in the options list
    #If it's right it shows right and add to right answers otherwise it says wrong answer
    answer = int(input('Answer: '))    
    if question['Options'][answer] == question['Answer']:
        print(f'{question["Answer"]}, Right answer! ✅\n')
        right_answers_total += 1
    else:
        print(f'{question["Options"][answer]}, Wrong answer! ❌\n')

#Showing the outcome of total right answers       
print(f'You got {right_answers_total} out of {len(questions)} questions right ')   