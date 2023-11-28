x = 12
y = 8
def change_y_local():  
    global x  
    y = 42
    y = y + 2
    print(f"y (local variable) in funktion change_y {y}")
    x = 13
    print(f"x (local variable) in funktion change_y {x}")    
    return y

print(f"y (global variable) {y}")
print(f"x (global variable) {x}")
y = change_y_local()
print(f"y (global variable) {y}")
print(f"x (global variable) {x}")

# def change_y_global():
#     global y
#     y = 42
#     y = y + 2
#     print(y)