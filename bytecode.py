import dis

code = """
def add(a, b):
    return a + b
result = add(3, 4)
print(result)
"""
compiled_code = compile(code,'<string>','exec')
dis.dis(compiled_code)
