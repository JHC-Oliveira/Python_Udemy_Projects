
import random

#THIS PROGRAM GENERATES 9 RANDOM NUMBERS AND FOLLOWING THE CPF LOGIC IT CREATES THE LAST 2 DIGITS


#9 DIGITS FOR CPF NUMBER
cpf_9_digit = "" 

#GENERATING 9 RANDOM NUMBERS
while len(cpf_9_digit) < 9:
    cpf_9_digit += str(random.randint(0,9))


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

print(cpf_generated)