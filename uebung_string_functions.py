#string = "Das ist ein toller Satz."
# string = input("Gib einen tollen Satz ein:")
# string_big = string.upper()
# print(string_big)

# string = input("Gib einen tollen keinen Satz ein:")
# string_little = string.lower()
# print(string_little)

# string = "Das ist ein toller Satz."
# string_spit = string.split(' ')
# print(string_spit)

# string = "12345"
# bool_nurziffern = string.isdigit()
# print(f"Im string {string} gibt nur ziffern: {bool_nurziffern}")

# string = "Hallo ist der Präfix da?"
# praefix_string = "Hallo"
# bool_hatpraefix = string.startswith(praefix_string)
# print(f"Der string {string} hat den präfix {praefix_string}: {bool_hatpraefix}")

# string = "Das ist ein Zeichens strings"
# zeichen = "a"
# print(string)
# replaced_string = string.replace('s',zeichen)
# print(replaced_string)

# string = "-----------lauter lehrzeichen zu entfernen---------"
# print(f"*{string}*")
# strip_string = string.lstrip('-')
# print(f"*{strip_string}*")

# string = "Das ist ein | toller Satz."
# string_spit = string.split('|')
# print(string_spit)

# string = "Das ist ein besonders langer Text damit ich die ersten 20 Zeichen herausschneiden kann."
# string_20 = string[0:20:2]
# print(string_20)
# string_20 = string[:20]
# print(string_20)
# x = len(string)
# y = x - 20
# z = x - y
# a = z - x
# x_minus = x * -1
# print(a)
# print(x_minus)
# string_20_top = string[x_minus:a]
# print(string_20_top)

string = "Dieser Text enthält EINIGE Großbuchstaben und 1234 Zahlen 5"
# uppercase_count = sum(1 for char in string if char.isupper())

# list = [char for char in string if char.isupper()]
# list = [char for char in string if char.isdigit()]
# print(list)
# print(len(list))
# uppercase_count = sum()
# print(uppercase_count)

string = "python"
# string_first_three_chars = string[0:3]
string_first_three_chars = string[None:3]
string_first_three_chars = string[0:3]
string_first_three_chars = string[2:6]
print(string_first_three_chars)

