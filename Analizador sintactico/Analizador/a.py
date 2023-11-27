import os
script_dir = os.path.dirname(__file__) 
compilador_path = os.path.join(script_dir, 'compilador.lr')
try:
    with open(compilador_path,'r') as compilador:
        comp=compilador.read()
        lineas=compilador.readlines()

except FileNotFoundError:
    print(f"Error: File not found - {file_path}")
print(comp)

