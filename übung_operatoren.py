# result = (8 - 5)**(27 // 9)
# result = 3 ** 3
# result = 27

result = 5 + 3 - 2
print(result)
result = 10 * 2 / 5
print(result)
result = (5 + 3) * 2
print(result)
result = 2**3
print(result)
zwei_mal_zehn_result = (2 * 10)
result = zwei_mal_zehn_result % 3
print(result)
zehn_mod_3_result = (10 % 3)
result = zehn_mod_3_result * 2
print(result)
# result = 5 + 3 & 2
# result = 6 and 5

# result = (5 < 3) & 2
# result = 5 > 3 and 2

# result = 8 > 2 == 1
# result = 8 > 2 == 1
# result = 1 == 1
# result = True

result = (5 + 3) * (2 - 1) / 2**2
result = 8 * 1 / 2**2
result = 8 * 1 / 4
result = 8 / 4
result = 2

result = 10 + 3 << 2
result = 13 << 2

result = bin(~5)
result = ~5 + 3
result = -6 + 3
result = -3

result = "Hallo " + "Welt!"

# numbers = [1, 2, 3, 4, 5]
# squared = [x ** 2 for x in numbers]
# add_two = [x + 2 for x in numbers]

# result = True and False or True

#result = 5 < 10 and 10 == 10
result = True and False or True and False
result = (True and False) or (True and False)

result = not not not True

result = not True or False and not False
result = False or False and True
result = False or False
result = False

result = 5 > 2 and 3 != 7 or not (True and False)
result = 5 > 2 and 3 != 7 or not False
result = True and True or not False
result = True and True or True
result = True or True
result = True

result = not (5 == 2 or (not False and 3 < 7))
result = not (5 == 2 or (not False and True))
result = not (5 == 2 or (True and True))
result = not (5 == 2 or True)
result = not (False or True)
result = not True
result = False

result = not not (True or False)
result = not not True
result = not False
result = True

result = True and (False or not (True and False)) or False
result = True and (False or not False) or False
result = True and (False or True) or False
result = True and True or False
result = True or False
result = True

result = not not not not not (True or False)
result = not not not not not True
result = not not not not False
result = not not not True
result = not not False
result = not True
result = False

result = (5 + 3 > 2 * 2 and not (10 % 3 == 0 or 2**2 < 5)) or True
result = (5 + 3 > 2 * 2 and not (10 % 3 == 0 or 4 < 5)) or True
result = (5 + 3 > 2 * 2 and not (1 == 0 or 4 < 5)) or True
result = (5 + 3 > 2 * 2 and not (False or True)) or True
result = (5 + 3 > 2 * 2 and not True) or True
result = (8 > 4 and not True) or True
result = (True and not True) or True
result = (True and False) or True
result = False or True
result = True

rechnung = "(2 * 3.5 + 3)**2"
result = eval(rechnung)
print(result)

# zahl1 = input('Bitte geben sie Zahl 1 ein:')
# type_zahl1 = type(zahl1)
# zahl2 = input('Bitte geben sie Zahl 2 ein:')
# arethmetischer_operator = input('Bitte geben sie einen operator ein:')
# type_zahl2 = type(zahl2)
# eval_string = f"{zahl1} {arethmetischer_operator} {zahl2}"
# # result = int(zahl1) - int(zahl2)
# result = eval(eval_string)
# print(result)

import math

ausdruck = "import math\nresult=math.sqrt(10)"
global_value = {}
local_value = {}
exec(ausdruck, global_value, local_value)
result = local_value.get('result', None)
# sqrt_result = math.sqrt(10)
print(result)
print('ende')




