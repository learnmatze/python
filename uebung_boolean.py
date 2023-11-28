# eingabe = input('Ist die lampe an? (1/0):')
# print(eingabe)
# print(bool(int(eingabe)))
# lampe_an = bool(int(eingabe))
# output = "Lampe ist an." if lampe_an == False else "Lampe ist aus."
# print(f"Wie ist die Lampe? {output}")

# output = {
#     True: "Lampe ist an.",
#     False: "Lampe ist aus."
# }.get(lampe_an)
# print(f"Wie ist die Lampe? {output}")

# eingabe = input('Wie alt sind sie?:')
# print(eingabe)
# print(int(eingabe))
# eintritt_erlaubt = int(eingabe) >= 18
# print(f"Sie dürfen in den Club: {eintritt_erlaubt}")

username = "mathiass"
eingabe_username = input('Bitte geben Sie ihren usernamen ein:')
password = "secure"
eingabe_password = input('Bitte geben Sie ihr passwort ein:')
# username_and_password_ok = 
print(f"Der von ihnen eingegebene username und das passwort stimmen: {password == eingabe_password and username == eingabe_username}")



