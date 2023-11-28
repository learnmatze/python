# arethmetische operatoren

# summand_groesse = 3
# summand_gewicht = 5
# summe = summand_groesse + summand_gewicht
# print(summe)

# minuend = 10
# subtrahend = 2
# differenz = minuend - subtrahend
# print(differenz)

# faktor_a = 3 
# faktor_b = 4
# produkt = faktor_a * faktor_b
# print(produkt)

# divident_gewicht = 75.0
# divosor_groesse = 1.73
# quotient_bmi = divident_gewicht / divosor_groesse**2
# print(quotient_bmi)

# divident = 75
# divosor = 2
# quotient = divident // divosor
# print(quotient)
# print(type(quotient))

# value = 3.5/1.2
# print(value)
# rounded_value = round(value, 3)
# print(rounded_value)

# zuweisungs operatoren

# a = 50
# print(a)
# a = a + 2
# a += 1
# print(a)
# a = a - 3
# a -= 3
# print(a)
# a = a * 2
# a *= 2
# print(a)
# a = a / 2
# a /= 2
# print(a)

# apfelsaft = f"apfel {10.5}"
# apfelsaft = f"apfel " + str(10.5)
# print(apfelsaft)

# multible_hallo = "hallo" * 4
# print(multible_hallo)

# zwei_hoch_drei = 3
# zwei_hoch_vier = 4
# potenziert = 2**(zwei_hoch_drei - zwei_hoch_vier)
# print(potenziert)

# neun = 9
# vier = 4
# value = neun // vier
# rest = neun % vier
# print(value)
# print(rest)

# vergleichs operatoren

# a = 'ca'
# b = 'bb'
# result = a == b
# print(f"a == b = {result}")
# result = a != b
# print(f"a != b = {result}")
# result = a < b
# print(f"a < b = {result}")
# result = a <= b
# print(f"a <= b = {result}")
# result = a > b
# print(f"a > b = {result}")
# result = a >= b
# print(f"a >= b = {result}")

# logische operatoren

#and - or - not
# result = "a" == "a" and 3 > 2
# print(result)

# result = 2 > 3 or 3 == 4
# print(result)

# result = "a" == "a" or 3 / 0
# print(result)

# result = True and 1 > 0 and 2 > 0
# print(result)

# result = not True
# print(result)
# result = not 3 > 2
# print(result)
# ergebnis_aus_rechnung_1 = bereche_spezialzahl1()
# ergebnis_aus_rechnung_2 = bereche_spezialzahl2()
# result = not ergebnis_aus_rechnung_1 != ergebnis_aus_rechnung_2
# result = not 1 <= 0
# 1 == 1
# 2 != 1
# 1 < 2
# 2 <= 2
# 2 > 1
# 2 >= 2

# result = 1 > 0 ^ 1 > 2
# print(result)

# bitoperatoren
a = 0b1101 # Binär 1101 (13)
b = 0b1010 # Binär 1010 (10)

# result = a & b
# print(f'{result} = {bin(result)}')
# result = a | b
# print(f'{result} = {bin(result)}')
# result = a ^ b
# print(f'{result} = {bin(result)}')
# result = ~a
# print(f'{result} = {bin(result)}')
# print(f'{a} = {bin(a)}')
# result = a << 1
# print(f'{result} = {bin(result)}')
# result = a >> 1
# print(f'{result} = {bin(result)}')
# binary_number = '1F'
# decimal_number = int(binary_number, 16)
# print(decimal_number)

result = 2 * 2 > 3 + 3 and 5 - 1 == 4 + 2
# result = 4 < 6
# result = True

a = 5
b = 10
c = 3
result = a > b or b >= c and not c == 3
result = False or True and not True
result = False or True and False
result = False or False
result = False
print(result)
result = (a > b or b >= c) and not c == 3
result = (False or True) and not c == 3
result = True and not True
result = True and False
result = False
print(result)

print(result)


