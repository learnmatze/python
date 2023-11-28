import dis

file_path = "add.py"
code = ""

try:
    with open(file_path, 'r') as file:
        code = file.read()  
    print(f"The following python source Code: \n {code} ")   
    print("")         
    print(f"Was transformed to the following bytecode:")
    compiled_code = compile(code,'<string>','exec')    
    dis.dis(compiled_code)

except FileNotFoundError:
    print(f'File not found {file_path}')
except Exception as e:
    print(f"Exception {str(e)} occured")
