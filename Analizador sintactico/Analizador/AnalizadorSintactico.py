import os
script_dir = os.path.dirname(__file__) 
compilador_path = os.path.join(script_dir, 'compilador.lr')
try:
    with open(compilador_path,'r') as compilador:
        #comp=compilador.read()
        lineasCompilador=compilador.readlines()

except FileNotFoundError:
    print(f"Error: File not found - {file_path}")

#for linea in lineas:
    #print(linea)


class AnalizadorSintactico():
    class Regla:
        def __init__(self, num, num2, elem, valor):
            self.num = num
            self.num2 = num2
            self.elem = elem
            self.valor = valor

    class ElementoPila:
        def __init__(self, valor):
            self.valor = valor

    class Terminal(ElementoPila):
        def __init__(self, valor, tipo):
            super().__init__(valor)
            self.tipo = tipo

    class NoTerminal(ElementoPila):
        def __init__(self, valor):
            super().__init__(valor)

    class Estado(ElementoPila):
        def __init__(self, valor):
            super().__init__(valor)
    
    def __init__(self,tokensF):
        self.tokens=tokensF
        self.pila=[] # Pila utilizada en el analisis
        self.lr=[] # Tabla LR para el analisis sintactico
        self.reglas=[] # Reglas de produccion gramatical
        self.data=[] # Almacenamiento de información sobre el análisis

    def leerReglas(self):
        # Metodo para leer las reglas gramaticales y construir la tabla LR
        reg=0
        num=0
        for linea in lineasCompilador:
            linea = linea.rstrip()
            linea = linea.split("\t")
            if (reg == 1):
                self.lr.append(linea)
                for i in range(len(self.lr)):
                    for j in range(len(self.lr[i])):
                        self.lr[i][j] = int(self.lr[i][j])
            if (linea[0]=='52'):
                continue
            if (linea[0]=='95'):
                reg = 1
            if (reg == 0):
                num += 1
                obj = self.Regla(num, int(linea[0]), int(linea[1]), linea[2])
                self.reglas.append(obj)

    def sintactico(self):

        # Inicializacion de la pila con el simbolo de fin de entrada y el estado inicial
        print("\nAnalisis sintactico:")
        self.pila.append(self.Terminal("$",100))
        self.pila.append(self.Estado(0))
        i=0
        pilaS = ""

        # Llamada para leer las reglas gramaticales y construir la tabla LR
        self.leerReglas()
        while True:
            obj=self.tokens[i]
            fila=self.pila[-1]
            columna=obj.tipo
            accion= self.lr[fila.valor][columna]
            
            if(accion==0):
                # No hay accion definida en la tabla LR
                break
            
            elif(accion>0):
                # Desplazamiento: se agrega un terminal y un estado a la pila
                i+=1
                acc = "d"+str(accion)
                self.pila.append(self.Terminal(obj.valor, obj.tipo))
                self.pila.append(self.Estado(accion))

            elif (accion == -1):
                # Reduccion: se aplica una regla de produccion
                acc = "r0(acept)"
                break

            else:

                # Reduccion: se aplica una regla de produccion específica
                acc = "r"+str(abs(accion+1))
                for obj2 in self.reglas:
                    if (accion == (obj2.num + 1)*-1):
                        acc = "r"+str(obj2.num)
                        accion = self.lr[fila.valor][obj2.num2]
                        if obj2.elem !=0:

                            # Eliminar elementos de la pila segun la regla de produccion
                            elim = obj2.elem*2
                            while elim !=0:
                                self.pila.pop()
                                elim -=1
                            fila = self.pila[-1]
                            accion = self.lr[fila.valor][obj2.num2]
                            # Agregar elementos de la regla a la pila
                            self.pila.append(obj2)
                            self.pila.append(self.Estado(accion))
                        else:
                            self.pila.append(obj2)
                            self.pila.append(self.Estado(accion))
                        break
            
            # Almacenar informacion sobre la iteracion actual
            for p in self.pila:
                pilaS += str(p.valor)
            self.data.append([pilaS, obj.valor, acc])
            pilaS = ""

        # Imprimir la información recopilada durante el análisis
        for d in self.data:
            print(d)