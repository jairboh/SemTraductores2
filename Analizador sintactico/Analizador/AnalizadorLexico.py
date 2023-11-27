import AnalizadorSintactico as s
class AnalizadorLexico():
    
    class Cadena:
        def __init__(self,token,tipo):
            self.cadena=token;
            self.tipo=tipo;
            #self.simbolo=simb
       
    class Token:
        def __init__(self,simbolo,tipo,valor):
            self.simbolo=simbolo;
            self.tipo=tipo;
            self.valor=valor;

    def __init__(self,entrada):
        self.cadenasTotales=[]
        self.tokensF=[]
        self.entrada=entrada+'$'
        #self.length=len(entrada)
        self.reserevados = {
            "int": 4,
            "float": 4,
            "void": 4,
            "string":4,
            "+": 5,
            "-": 5,
            "*": 6,
            "/": 6,
            "<": 7,
            "<=": 7,
            ">": 7,
            ">=": 7,
            "||": 8,
            "&&": 9,
            "!": 10,
            "==": 11,
            "!=": 11,
            ";": 12,
            ",": 13,
            "(": 14,
            ")": 15,
            "{": 16,
            "}": 17,
            "=": 18,
            "if": 19,
            "while": 20,
            "return": 21,
            "else": 22,
            "$": 23,
        }
        self.tipoDatos={
            -1:"Error",
            0:"identificador",
            1:"entero",
            2:"real",
            3:"cadena",
            4:"tipo",
            5:"opSuma",
            6:"opMul",
            7:"opRelac",
            8:"opOr",
            9:"opAnd",
            10:"opNot",
            11:"opIgualdad",
            12:";",
            13:",",
            14:"(",
            15:")",
            16:"{",
            17:"}",
            18:"=",
            19:"if",
            20:"while",
            21:"return",
            22:"else",
            23:"$",

        }
        
    def lexico(self):
        token=""
        aux=False;
        #print(self.entrada)
        for caracter in self.entrada:
            if(aux):
                #se cerro el contenido de la string
                if(caracter=='"'):
                    aux=False
                    c=self.Cadena(token+'"',3)
                    self.cadenasTotales.append(c)
                    token=""
                #significa que no se cerro el contenido de la string
                elif(caracter=='$'):
                    aux=False
                    c=self.Cadena(token,-1)
                    self.cadenasTotales.append(c)
                    token=""
                else:
                    #agrega caracter al valor de la string
                    token+=caracter

            #termino la entrada?
            elif caracter == '$':
                #
                if(token!=""):
                    tipo=self.verificarToken(token);
                    c=self.Cadena(token,tipo)
                    self.cadenasTotales.append(c)
                    token=""
                else:
                    tipo=self.verificarToken(caracter);
                    c=self.Cadena(caracter,tipo)
                    self.cadenasTotales.append(c)
                    break
            
            #verifica el salto de linea o espacio
            elif caracter == ' ' or caracter == '\n':
                if token != "":
                    tipo=self.verificarToken(token);
                    c=self.Cadena(token,tipo)
                    self.cadenasTotales.append(c)
                    token="";

            #termino linea de codigo
            elif caracter == ';':
                if token != "":
                    tipo=self.verificarToken(token);
                    c=self.Cadena(token,tipo)
                    self.cadenasTotales.append(c)
                    token="";
                tipo=self.verificarToken(caracter);
                c=self.Cadena(caracter,tipo)
                self.cadenasTotales.append(c)

                #empieza el contenido de la string
            elif caracter == '"':
                aux=True
                token=""
                token+=caracter
            else:
                #checa si el caracter esta en la lista de reservados como (){}
                if(caracter in self.reserevados):
                    if(token!=""):
                        tipo=self.verificarToken(token);
                        c=self.Cadena(token,tipo)
                        self.cadenasTotales.append(c)
                        token="";
                    c=self.Cadena(caracter,self.reserevados[caracter])
                    self.cadenasTotales.append(c)
                
                else:
                    #agrega contenido al token, es decir va i ... in ... int 
                    token+=caracter
                #print(token)
    
    def verificarToken(self,token):
        punto=False
        if(token in self.reserevados):
            return self.reserevados[token]
        elif((65 <= ord(token[0]) <= 90) or (97 <= ord(token[0]) <= 122)):
            for caracter in token:
                if (48 <= ord(caracter) <= 57) or (65 <= ord(caracter) <= 90) or (97 <= ord(caracter) <= 122):
                    return 0
        elif(token.isdigit()):
            return 1 
        for i in token:
            if i == '.':
                punto = True
            elif not i.isdigit() and not punto:
                return -1  # El token contiene caracteres no numéricos
            elif not i.isdigit() and punto:
                return 2  # El token contiene caracteres no numéricos después del punto decimal
        return 2 if punto else 1

    def imprimirCadenasTotales(self):
        for cadena_obj in self.cadenasTotales:
            #print(f"Valor: {cadena_obj.cadena} \tTipo: {cadena_obj.tipo} \tSimbolo: {self.tipoDatos[cadena_obj.tipo]}")
            aux=self.Token(self.tipoDatos[cadena_obj.tipo],cadena_obj.tipo,cadena_obj.cadena);
            self.tokensF.append(aux);
            #print(f"Valor: {cadena_obj.cadena} \tTipo: {cadena_obj.tipo}")
        print("\nAnalisis Lexico:")
        for t in self.tokensF:
            print(f"Valor: {t.valor} \tTipo: {t.tipo} \tSimbolo: {t.simbolo}")

        analizador=s.AnalizadorSintactico(self.tokensF)
        analizador.sintactico()
