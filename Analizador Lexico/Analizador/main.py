import os
import AnalizadorLexico as l

script_dir = os.path.dirname(__file__)  # Get the script's directory
file_path = os.path.join(script_dir, 'ejemplo.txt')

try:
    with open(file_path, 'r') as file:
        cadena = file.read()
    print(cadena)
    analizador=l.AnalizadorLexico(cadena)
    analizador.lexico()
    analizador.imprimirCadenasTotales()
    input()
except FileNotFoundError:
    print(f"Error: File not found - {file_path}")

