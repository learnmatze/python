import fitness

name = "Timmi"
gewicht = 82
groesse = 1.87
print(f"Das Gewicht von {name} ist {gewicht}")
bmi = fitness.bmi(gewicht, groesse)
print(f"BMI von {name} ist {bmi}")
gewicht = fitness.abnehmen(gewicht, 10)
print(f"Das neue Gewicht von {name} ist {gewicht}")
gewicht = fitness.zunehmen(gewicht, 25)
print(f"Das ganz neue Gewicht von {name} ist {gewicht}")
fitness.sag_gewicht(name)


