# string = "Hallo Python"
# list = [1,2,3]
# string_length = len(string)
# list_length = len(list)
# string_type = type(string)
# list_type = type(12.5)
# print(f"Der string: {string} hat eine länge von {string_length}")

# string = "Hallo Python 123!"
# string_upper = string.upper()
# print(f"Der string: {string} mit Großbuchstaben ist: {string_upper}")

# string = "Hallo Python 123!"
# string_lower = string.lower()
# print(f"Der string: {string} mit Kleinbuchstaben ist: {string_lower}")

# list_1 = ['Hello', 'world', '!', 'This', 'is', 'Python'] 
# separator = '-' 
# string_kombiniert = separator.join(list_1) 

# string_ersterteil = "Hallo Python!"
# string_zweiterteil = "1"
# string_kombiniert = string_ersterteil + string_zweiterteil
# string_kombiniert = string_ersterteil.join(string_zweiterteil)
# print(f"{string_kombiniert}")

# string = '12.5'
# string_list = string.split(' ')
# print(string_list)
# is_alphanumeric = string.isalpha()
# is_digit = string.isdigit()
# is_numeric = string.isnumeric()
# is_decimal = string.isdecimal()
# print(f'Nur buchstaben in string {string}? {is_alphanumeric}')
# print(f'Nur zahlen in string {string}? {is_digit}')
# print(f'is numeric {string}? {is_numeric}')
# print(f'is decimal {string}? {is_decimal}')

# string = " repeat "
# repeat_string = string * 3
# print(f"string {string} * 3 = {repeat_string}")

# verzierungs_character = "*"
# ein_verzierter_string = "| Ein verzierter string |"
# ein_sehr_schoen_verzierter_string = "| Ein sehr schön verzierter string |"

# lenght_ein_verzierter_string =  len(ein_verzierter_string)
# print(f"länge von {ein_verzierter_string}: {lenght_ein_verzierter_string}")
# repeat_schoen_string = verzierungs_character * lenght_ein_verzierter_string
# print(repeat_schoen_string)
# print(ein_verzierter_string)
# print(repeat_schoen_string)

# lenght_ein_schoen_verzierter_string =  len(ein_sehr_schoen_verzierter_string)
# print(f"länge von {ein_sehr_schoen_verzierter_string}: {lenght_ein_schoen_verzierter_string}")
# repeat_schoen_string = verzierungs_character * lenght_ein_schoen_verzierter_string
# print(repeat_schoen_string)
# print(ein_sehr_schoen_verzierter_string)
# print(repeat_schoen_string)

# string = "hallo python ist super"
# title_string = string.capitalize()
# print(f"{string}.titel() => {title_string}")

# string = "hallo super ist super"
# find_string = 'super'
# lenght_of_find_string = len(find_string)
# found_string_index = string.find(find_string)
# print(found_string_index)
# found_string_index = string.index(find_string)
# print(found_string_index)
# r_found_string_index = string.rfind(find_string)
# print(r_found_string_index)
# r_found_string_index = string.rindex(find_string)
# print(r_found_string_index)
# found_string = string[found_string_index:found_string_index + lenght_of_find_string]
# print(f"{string}.find({find_string}) at index: {found_string_index} => {found_string}")

# string = "hallo super python ist super python ist super"
# starts_with = string.startswith("Hallo".lower())
# starts_with = string.startswith("Hallo")
# starts_with = string.startswith("python")

# ends_with = string.endswith("python")
# ends_with = string.endswith("Python")
# ends_with = string.endswith("super")
# ends_with = string.endswith("Super")

# string = "python ist eine schlechte programmiersprache"
# replace_string = string.replace("schlechte","spitzen")
# print(string)
# print(replace_string)

# string = "thas ist ein sample satz mit vielen wörtern."
# print(string)
# string = string.replace("sample", "replacement").replace("vielen", "verschiedenen")
# print(string)

# string = "1000.10"
# print(string)
# string = string.zfill(20)
# print(string)

# string = "        ich habe vergessen alle lehrzeichen zu entfernen        "
# print(f"-{string}-")
# strip = string.strip()
# print(f"-{strip}-")

# rstrip_string = string.replace('alle', 'vorne')
# rstip  = rstrip_string.rstrip()
# print(f"-{rstip}-")

# lstrip_string = string.replace('alle', 'hinten')
# lstrip = lstrip_string.lstrip()
# print(f"-{lstrip}-")

# rstrip_string = string.replace('alle','vorne')
# rstrip = rstrip_string.rstrip()
# print(f"-{rstrip}-")
# lstrip_string = string.replace('alle','hinten')
# lstrip = lstrip_string.lstrip()
# print(f"-{lstrip}-")

string = input("Geben sie einen satz ein:")
print(string)
print('')
print(())

