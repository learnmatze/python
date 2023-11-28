import string_manipulation as strm

string = "Python"
reverse_string = strm.umkehren(string)
count_string = strm.count(string)
upper_string = strm.upper(string)
lower_string = strm.lower(string)
print(f"Der string {string}, reverse {reverse_string}, count {count_string}, upper {upper_string}, lower {lower_string}")

print(f"In hauptprogramm Variable __name__: {__name__}")

def berechnen(a, b):
    return a + b

def main():
    print("Hauptpogramm Ausgeführt als hauptprogramm")

def imported():
    print("Hauptpogramm Ausgeführt als importiertes Skript")

if __name__ == '__main__':
    main()
else:
    imported()