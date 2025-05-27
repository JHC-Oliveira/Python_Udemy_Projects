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
    print(f'Question: {question['Question']}')
    print('Options:')
    
    #Using enumerate and the dictionary value to print the options
    for option_number, option_answers in enumerate(question['Options']):
        print(f'{option_number}) {option_answers}')
    print()
    
   
    answer = input('Answer: ')
    
    #Variables to store an int number, and check if it is the right answer
    int_answer = None
    right_answer = False
    
    #Storing the variable in case it's a digit
    if answer.isdigit():
        int_answer = int(answer)
    
    #Checking if it's not a digit, and if it's not in the range of the questions   
    if int_answer is not None:  
        if int_answer >= 0 and int_answer < len(question['Options']): 
            if question['Options'][int_answer] == question['Answer']:
                right_answer = True
                right_answers_total += 1                    
    else:
        print("You should provide a valid option")
    
    #Outputs   
    if right_answer:
        print(f'{question["Answer"]}, Right answer! ✅\n')
    else:
        print('Wrong answer! ❌\n')

#Showing the outcome of total right answers       
print(f'You got {right_answers_total} out of {len(questions)} questions right ')