class AnalizadorLexico:
    def __init__(self, string):
        self.string = string + '$'

    def lexico(self):
        id = ""
        numero = ""
        i = 0
        punto = False
        operadores = {
            "int": "tipo",
            "float": "tipo",
            "void": "tipo",
            "+": "opSuma",
            "-": "opResta",
            "*": "opMul",
            "/": "opDiv",
            "<": "opRelac",
            "<=": "opRelac",
            ">": "opRelac",
            ">=": "opRelac",
            "||": "opOr",
            "&&": "opAnd"
        }
        while i < len(self.string):
            char = self.string[i]
            next_char = self.string[i+1] if i+1 < len(self.string) else None

            if char == '$':
                break

            if char + next_char in operadores:
                if len(id) > 0:
                    print(id, "es un identificador")
                    id = ""
                if len(numero) > 0:
                    if punto:
                        print(numero, "es un número real")
                    else:
                        print(numero, "es un número entero")
                    numero = ""
                    punto = False
                print(char + next_char, "es un", operadores[char + next_char])
                i += 2
            elif char in operadores:
                if len(id) > 0:
                    print(id, "es un identificador")
                    id = ""
                if len(numero) > 0:
                    if punto:
                        print(numero, "es un número real")
                    else:
                        print(numero, "es un número entero")
                    numero = ""
                    punto = False
                print(char, "es un", operadores[char])
                i += 1
            elif char.isspace():
                i += 1
            elif (char.isalpha() and next_char.isalnum()) or (char.isdigit() and next_char.isdigit()):
                id += char
                i += 1
            elif char.isdigit():
                numero += char
                i += 1
            elif char == '.':
                if not punto:
                    numero += char
                    punto = True
                    i += 1
                else:
                    numero = ""
                    id = ""
                    punto = False
                    print("Token no válido")
                    break
            else:
                print("Token no válido")
                break

        if len(numero) > 0:
            if punto:
                print(numero, "es un número real")
            else:
                print(numero, "es un número entero")
        elif len(id) > 0:
            if id in operadores:
                print(id, "es un", operadores[id])
            else:
                print(id, "es un identificador")

cadena = input("Dame la cadena a probar: ")
AnalizadorLexico(cadena).lexico()
input()
