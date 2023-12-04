import os
import AnalizadorLexico as l

script_dir = os.path.dirname(__file__) 
file_path = os.path.join(script_dir, 'ejemplo.txt')

try:
    with open(file_path, 'r') as entrada:
        cadena = entrada.read()
    print("\nCodigo:")
    print(cadena+'\n')
    analizador=l.AnalizadorLexico(cadena)
    analizador.lexico()
    analizador.imprimirCadenasTotales()
    input()
except FileNotFoundError:
    print(f"Error: File not found - {file_path}")

