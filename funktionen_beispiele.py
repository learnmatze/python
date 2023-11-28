def calculate_average(numbers):
    total = sum(numbers)
    lenght = len(numbers)
    average = total / lenght
    return average

liste_nummern = [10, 20, 30, 40, 50]
average = calculate_average(liste_nummern)
# print(f"Der Durchschnitt der Liste: {liste_nummern} ist {average}")

def read_file(file_name):
    with open(file_name, 'r') as file:
        content = file.read()
    return content

def write_file(file_name, data):
    with open(file_name, 'w') as file:
        file.write(data)
    return True

def delete_file_data(file_name):
    with open(file_name, 'w') as file:
        file.write('')
    return True

file_name = "text.txt"
data_to_write = "Das sind sehr wichtige Daten die wir in einen File speichern."
write_file(file_name, data_to_write)
data_to_read = read_file(file_name)
print(f"Gelesene Daten aus file {file_name}: {data_to_read}")
delete_file_data(file_name)
print('Fertig')


