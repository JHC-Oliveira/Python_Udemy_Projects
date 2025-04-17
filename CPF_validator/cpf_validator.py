# This is my own version of the solution.

"""
cpf: 746.824.890-70

* Take the first 9 numbers
* Multiply each one starting from 10 and decreasing, and sum by the end eg:

# 10  9  8  7 ........ 2
# 7   4  6  8 ........ 0
# 70  36 48 56 ....... 0  = SUM

*Take the sum and multiply by 10
*Obtain the rest of division by 11 from the previous step:
-if the result is bigger than 9:
    result = 0
-if not:
    result = operation value

*The first digit after "-" must be the result from the previous step (in this case 7).
"""

cpf = '746.824.890-70'

#TAKING OUT THE LAST PART AND ALSO THE '.' FROM THE CPF
cpf_splited = cpf.split('-')[0].split('.')


#LOOP TO GET ALL THE 9 DIGITS IN OLNY ONE STRING 
cpf_first_9_digit = ""
for three_nb in cpf_splited:
    for nb in three_nb:
        cpf_first_9_digit += nb       

#TAKING EACH INDEX AND MULTIPLYING STARTING FROM 10 DECREASINGLY
sum_of_digits = 0
counter = 0
for i in range(10, 2, -1):
    sum_of_digits += i * int(cpf_first_9_digit[counter])
    counter += 1

#MULTIPLYING BY 10
value_multiplied = int(sum_of_digits) * 10   

#REST OF DIVISION BY 11
rest_value = value_multiplied % 11

#FIRST VALUE AFTER "-"
first_digit = rest_value if rest_value <= 9 else 0

print(first_digit)