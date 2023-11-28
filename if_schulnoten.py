# Wir wollen ein programm schreiben das Schulnoten verbalisiert
# 1 - sehr gut, 2 - gut, 3 - befriedigend, 4 - genügend, 5 - nicht genügend

alter = 20
if (alter >= 18):
    print("Du bist volljährig")
    print("Du bist da")
    if (alter >= 100):
        print("Du bist aber alt")
        print("ende inneres if")
print("ende äußeres if")



# if note == "1":
#     note_verbal = "sehr gut"
#     print(f"Ihre Note ist eine {note} das entspricht einem {note_verbal}")
# elif note == "2":
#     note_verbal = "gut"
#     print(f"Ihre Note ist eine {note} das entspricht einem {note_verbal}")
# elif note == "3":
#     note_verbal = "befriedigend"
#     print(f"Ihre Note ist eine {note} das entspricht einem {note_verbal}")
# elif note == "4":
#     note_verbal = "genügend"
#     print(f"Ihre Note ist eine {note} das entspricht einem {note_verbal}")
# elif note == "5":
#     note_verbal = "nicht genügend"
#     print(f"Ihre Note ist eine {note} das entspricht einem {note_verbal}")
# else:
#     print(f"Für ihre Note {note} gibt es keine verbale beurteilung.")

noten_mapping = {
    1: "sehr gut",
    2: "gut",
    3: "begriedigend",
    4: "genügend",
    5: "nicht genügend"
}
note_verbal = noten_mapping.get(int(note),"unknown")
if note_verbal != "unknown":
    print(f"Ihre Note ist eine {note} das entspricht einem {note_verbal}")  
elif note_verbal == "unknown":
    print(f"Für ihre Note {note} gibt es keine verbale beurteilung.")
# else:
#     print(f"Für ihre Note {note} gibt es keine verbale beurteilung.")

print('Programm ende')