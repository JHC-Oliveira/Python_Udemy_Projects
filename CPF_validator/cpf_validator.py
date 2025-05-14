# This is my own version of the solution.

"""
cpf: 746.824.890-70

*1- Take the first 9 numbers
*2- Multiply each one starting from 10 and decreasing, and sum by the end eg:

# 10  9  8  7 ........ 2
# 7   4  6  8 ........ 0
# 70  36 48 56 ....... 0  = SUM

*3- Take the sum and multiply by 10
*4- Obtain the rest of division by 11 from the previous step:
-if the result is bigger than 9:
    result = 0
-if not:
    result = operation value

*The first digit after "-" must be the result from the previous step (in this case 7).

*For the second digit after "-" you should repeat the same logic but on step 2 now it will start with 11 and in the last part should include the first digit, eg: 

# 11  10  9  8 ........ 2
# 7   4  6  8 ........ first digit (7)
# 70  36 48 56 ....... 14  = SUM
"""

import re
import sys

cpf = input('CPF ex:[746.824.890-70]: ')

#USING REGULAR EXPRESSION TO TAKE ANY SPECIAL CHARACTERE THAT IS NOT A NUMBER
cpf_given = re.sub(
    r'[^0-9]',
    '',
    cpf
)

#CHECKING IF THE NUMBER ARE NOT SEQUENTIAL
sequencial_input = cpf == cpf[0] * len(cpf)
if sequencial_input:
    print('You digited sequential data')
    sys.exit()

#-----------------------------FIRST DIGIT-----------------------------------------

#GET ALL THE 9 DIGITS IN OLNY ONE STRING 
cpf_9_digit = cpf_given[:9]      


#TAKING EACH INDEX AND MULTIPLYING STARTING FROM 10 DECREASINGLY
sum_first_digits = 0
counter = 10
for number in cpf_9_digit:
    sum_first_digits += int(number) * counter
    counter -= 1

#MULTIPLYING BY 10
value_multiplied = sum_first_digits * 10   

#REST OF DIVISION BY 11
rest_value = value_multiplied % 11

#FIRST VALUE AFTER "-"
first_digit = rest_value if rest_value <= 9 else 0


#-----------------------------SECOND DIGIT-----------------------------------------

cpf_10_digits = cpf_9_digit + str(first_digit)

#DIFFERENT LOGIC FROM THE PREVIOUS ONE
counter = 11
sum_second_digits = 0
for number in cpf_10_digits:
    sum_second_digits += int(number) * counter
    counter -= 1

value_multiplied = sum_second_digits * 10
rest_value = value_multiplied % 11
second_digit = rest_value if rest_value <= 9 else 0

cpf_generated = f'{cpf_9_digit}{first_digit}{second_digit}'

if cpf_given == cpf_generated:
    print('Valid CPF')
else:
    print('Invalid CPF')