import os
from anytree import Node, RenderTree, PreOrderIter
import generacionCodigo as gc
script_dir = os.path.dirname(__file__) 
compilador_path = os.path.join(script_dir, 'compilador.lr')
try:
    with open(compilador_path,'r') as compilador:
        lineasCompilador=compilador.readlines()

except FileNotFoundError:
    print(f"Error: File not found - {file_path}")

ParamList = []
ParamCList = []
TermList = []
ExpList = []
ConList = []
RetList = []
TermCList = []
SenList = []
CallList = []
objetoL=[]
VarList = []
ListaVarList =[]
ErrorList=[]
OpList=[]
contexto=""
root = Node("Arbol Sintactico:")
root2=Node("lex")

class variable:
    def __init__(self, tipo, id, contexto):
        self.tipo = tipo
        self.id = id
        self.contexto = contexto

class retorno:
    def __init__(self, cad, tipo, context):
        self.cad = cad
        self.tipo = tipo
        self.context = context

class Programa:
    def __init__(self, definiciones, nodo):
        self.definiciones =  definiciones
        self.valor = 'Programa'
        self.nodo = nodo
class Variables:
    def __init__(self, cad, contexto):
        self.cad = cad
        self.contexto = contexto
    def __repr__(self):
        aux = ("Variable: "+str(self.cad)+" contexto: "+str(self.context))
        return aux
class Definiciones3:
    def __init__(self, definicion, definiciones, nodo):
        self.definicion = definicion
        self.definiciones =  definiciones
        self.valor = 'Definiciones'
        self.nodo = nodo

class Definicion:
    def __init__(self, defi, nodo):
        self.defi = defi
        self.valor = 'Definicion'
        self.nodo = nodo

class DefVar:
    def __init__(self, tipo, identificador, listaVar, puntoyComa, nodo):
        self.tipo = tipo
        self.identificador =  identificador
        self.listaVar = listaVar
        self.puntoyComa = puntoyComa
        self.valor = 'DefVar'
        self.nodo = nodo

class ListaVar8:
    def __init__(self, identificador, listaVar, nodo):
        self.identificador = identificador
        self.listaVar =  listaVar
        self.valor = 'ListaVar'
        self.nodo = nodo

class DefFunc:
    def __init__(self, tipo, identificador, parA, parametros, parC, bloqFunc, nodo):
        self.tipo = tipo
        self.identificador = identificador
        self.parA = parA
        self.parametros = parametros
        self.parC = parC
        self.bloqFunc = bloqFunc
        self.valor = 'DefFunc'
        self.nodo = nodo

class Parametros:
    def __init__(self, tipo, identificador, listaParam, nodo):
        self.tipo = tipo
        self.identificador =  identificador
        self.listaParam = listaParam
        self.valor = 'Parametros'
        self.nodo = nodo

class ParametrosCon:
    def __init__(self, tipo, identificador, contexto, nodo):
        self.tipo = tipo
        self.identificador =  identificador
        self.contexto = contexto
        self.valor = 'Parametros'
        self.nodo = nodo


class ListaParam:
    def __init__(self, tipo, identificador, listaParam, nodo):
        self.tipo = tipo
        self.identificador =  identificador
        self.listaParam = listaParam
        self.valor = 'ListaParam'
        self.nodo = nodo

class BloqFunc:
    def __init__(self, parA, defLocales, parC, nodo):
        self.parA = parA
        self.defLocales =  defLocales
        self.parC = parC
        self.valor = 'BloqFunc'
        self.nodo = nodo

class DefLocales16:
    def __init__(self, defLocal, defLoclales, nodo):
        self.defLocal = defLocal
        self.defLocales = defLoclales
        self.valor = 'DefLocales'
        self.nodo = nodo

class DefLocal:
    def __init__(self, defSent, nodo):
        self.defSent = defSent
        self.valor = 'DefLocal'
        self.nodo = nodo

class Sentencias20:
    def __init__(self, sentencia, sentencias, nodo):
        self.sentencia = sentencia
        self.sentencias = sentencias
        self.valor = 'Sentencias'
        self.nodo = nodo


class Sentencia21:
    def __init__(self, identificador, op, expresion, puntoyComa, nodo):
        self.identificador = identificador
        self.op = op
        self.expresion = expresion
        self.puntoyComa = puntoyComa
        self.valor = 'Sentencia'
        self.nodo = nodo
        self.listateraux = list()

class Sentencia22:
    def __init__(self, ifV, parA, expresion, parC, sentenciaB, otro, nodo):
        self.ifV = ifV
        self.parA = parA
        self.expresion = expresion
        self.parC = parC
        self.sentenciaB = sentenciaB
        self.otro = otro
        self.valor = 'Sentencia'
        self.nodo = nodo

class Sentencia23:
    def __init__(self, whileV, parA, expresion, parC, bloque, nodo):
        self.whileV = whileV
        self.parA = parA
        self.expresion = expresion
        self.parC = parC
        self.bloque = bloque
        self.valor = 'Sentencia'
        self.nodo = nodo

class Sentencia24:
    def __init__(self, returnV, valorR, puntoyComa, nodo):
        self.returnV = returnV
        self.valorR = valorR
        self.puntoyComa = puntoyComa
        self.valor = 'Sentencia'
        self.nodo = nodo

class Sentencia25:
    def __init__(self, llamadaF, puntoyComa, nodo):
        self.llamadaF = llamadaF
        self.puntoyComa = puntoyComa
        self.valor = 'Sentencia'
        self.nodo = nodo

class Otro27:
    def __init__(self, elseV, sentenciaB, nodo):
        self.elseV = elseV
        self.sentenciaB = sentenciaB
        self.valor = 'Otro'
        self.nodo = nodo

class Bloque:
    def __init__(self, parA, sentencias, parC, nodo):
        self.parA = parA
        self.sentencias = sentencias
        self.parC = parC
        self.valor = 'Bloque'
        self.nodo = nodo

class ValorRegresa:
    def __init__(self, expresion, nodo):
        self.expresion = expresion
        self.valor = 'Valor Regresa'
        self.nodo = nodo

class Argumentos:
    def __init__(self, expresion, listaA, nodo):
        self.expresion = expresion
        self.listaA = listaA
        self.valor = 'Argumentos'
        self.nodo = nodo

class ListaArgumentos:
    def __init__(self, comaV, expresion, listaA, nodo):
        self.comaV = comaV
        self.expresion = expresion
        self.listaA = listaA
        self.valor = 'Lista Argumentos'
        self.nodo = nodo

class Termino35:
    def __init__(self, llamadaFunc, nodo):
        self.llamadaFunc = llamadaFunc
        self.valor = 'Termino'
        self.nodo = nodo

class Termino:
    def __init__(self, dato, nodo):
        self.dato = dato
        self.valor = 'Termino'
        self.nodo = nodo

class LlamadaFunc:
    def __init__(self, identificador, parA, argumentos, parC, nodo):
        self.identificador = identificador
        self.parA = parA
        self.argumentos = argumentos
        self.parC = parC
        self.valor = 'Llamada Funcion'
        self.nodo = nodo

class SentenciaBloque:
    def __init__(self, senBlo, nodo):
        self.senBlo = senBlo
        self.valor = 'Sentencia Bloque'
        self.nodo = nodo

class Expresion43:
    def __init__(self, parenA, expresion, parenC, nodo):
        self.parenA = parenA
        self.expresion = expresion
        self.parenC = parenC
        self.valor = 'Expresion'
        self.nodo = nodo

class Expresion44:
    def __init__(self, op, expresion, nodo):
        self.op = op
        self.expresion = expresion
        self.valor = 'Expresion'
        self.nodo = nodo

class Expresion46:
    def __init__(self, expresion1, op, expresion2, nodo):
        self.expresion1 = expresion1
        self.op = op
        self.expresion2 = expresion2
        self.valor = 'Expresion'
        self.nodo = nodo

class Expresion52:
    def __init__(self, termino, nodo):
        self.termino = termino
        self.valor = 'Expresion'
        self.nodo = nodo

class NoElim:
    def __init__(self, nume, valor, nodo):
        self.nume = nume
        self.valor = valor
        self.nodo = nodo

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
        self.tablaVariables=[]

        self.VarFlag=0
        self.ambito=''
        self.CallFlag=0
        self.tiporetorno=""
        self.printV=''
        self.PrintFlag=0
        self.callFunc=0

    def remplazar(self, elim, num, flagR):
        while elim !=0:
            if flagR == 1:
                flagR = 0   
                objetoL.append(self.pila[-1])
            else:
                flagR = 1
            self.pila.pop()
            elim -=1
        for elem in objetoL:
            #print(elem.valor)
            pass
        if num == 1: 
            obj = Programa(objetoL[0], Node('Programa', parent=root))
            obj.definiciones.nodo.parent = obj.nodo
        elif num == 2:
            obj = NoElim(num, "Definiciones", Node('Definiciones', parent=root))
        elif num == 3:
            obj = Definiciones3(objetoL[1], objetoL[0], Node('Definiciones', parent=root))
            obj.definicion.nodo.parent = obj.nodo
            obj.definiciones.nodo.parent = obj.nodo
        elif num == 4 or num == 5:
            obj = Definicion(objetoL[0], Node('Definicion', parent=root))
            obj.defi.nodo.parent = obj.nodo
        elif num == 5:
            obj = NoElim(num, "Definicion", Node('Definicion', parent=root))
        elif num == 6:
            obj = DefVar(objetoL[3], objetoL[2], objetoL[1], objetoL[0],Node('DefVar', parent=root))
            Node(objetoL[3].valor, parent = obj.nodo)
            Node(objetoL[2].valor, parent = obj.nodo)
            obj.listaVar.nodo.parent = obj.nodo
            Node(objetoL[0].valor, parent = obj.nodo)
            self.VarFlag+=1
            if obj.listaVar.__class__.__name__ == 'NoElim':
                obj.listaVar = self.ambito
                if obj.listaVar == '':
                    obj.listaVar = 'Main'
            VarList.append(obj)
            if len(ListaVarList)!=0:
                for i in range(len(ListaVarList)):
                    auxiliar = ListaVarList.pop(0)
                    auxiliar.tipo = objetoL[3]
                    auxiliar.listaVar = objetoL[1]
                    ListaVarList.append(auxiliar)
                    VarList.append(auxiliar)
        elif num == 7:
            obj = NoElim(num, "ListaVar", Node('ListaVar', parent=root))
        elif num == 8:
            obj = ListaVar8(objetoL[1], objetoL[0], Node('ListaVar', parent=root))
            Node(objetoL[1].valor, parent = obj.nodo)
            obj.listaVar.nodo.parent = obj.nodo
            ListaVarList.append(DefVar('Tipo', objetoL[1], objetoL[0],None,None))
        elif num == 9:
            obj = DefFunc(objetoL[5], objetoL[4], objetoL[3], objetoL[2], objetoL[1], objetoL[0], Node('DefFunc', parent=root))
            Node(objetoL[5].valor, parent = obj.nodo)
            Node(objetoL[4].valor, parent = obj.nodo)
            Node(objetoL[3].valor, parent = obj.nodo)
            obj.parametros.nodo.parent = obj.nodo
            Node(objetoL[1].valor, parent = obj.nodo)
            obj.bloqFunc.nodo.parent = obj.nodo
            aux=self.ambito
            self.ambito=''
            if self.tiporetorno != objetoL[5].valor:
                if self.tiporetorno =='':
                    pass
                else:
                    ErrorList.append('Error en la funcion ' + aux)
            
            self.tiporetorno=""
            OpList.clear()
        elif num == 10:
            obj = NoElim(num, "Parametros", Node('Parametros', parent=root))
        elif num == 11:
            obj = Parametros(objetoL[2], objetoL[1], objetoL[0], Node('Parametros', parent=root ))
            Node(objetoL[2].valor, parent = obj.nodo)
            Node(objetoL[1].valor, parent = obj.nodo)
            obj.listaParam.nodo.parent = obj.nodo
            self.parametro=obj
            ParamList.append(obj)
            contexto = ''
            i = 0
            posi =2
            posfi = 6
            if self.pila[2].valor=='Definicion':
                while i == 0: 
                    posi = posi +2
                    if self.pila[posi].valor == 'Definicion':
                        posfi = posfi +2
                    else:
                        contexto =self.pila[posfi].valor
                        i = 1
                        break
            else:
                contexto= self.pila[4].valor
            ParamCList.append(ParametrosCon(objetoL[2], objetoL[1], contexto, Node('ParametrosCon', parent=root2) ))
        elif num == 12:
            obj = NoElim(num, "ListaParam", Node('ListaParam', parent=root))
        elif num == 13:
            obj = ListaParam(objetoL[2], objetoL[1], objetoL[0], Node('ListaParam', parent=root))
            Node(objetoL[2].valor, parent = obj.nodo)
            Node(objetoL[1].valor, parent = obj.nodo)
            obj.listaParam.nodo.parent = obj.nodo
            self.parametro=obj
            ParamList.append(obj)
            contexto = ''
            i = 0
            posi =2
            posfi = 6
            if self.pila[2].valor=='Definicion':
                while i == 0: 
                    posi = posi +2
                    if self.pila[posi].valor == 'Definicion':
                        posfi = posfi +2
                    else:
                        contexto =self.pila[posfi].valor
                        i = 1
                        break
            else:
                contexto= self.pila[4].valor
            ParamCList.append(ParametrosCon(objetoL[2], objetoL[1], contexto,  Node('ParametrosCon', parent=root2) ))
        elif num == 14:
            obj = BloqFunc(objetoL[2], objetoL[1], objetoL[0], Node('BloqFunc', parent=root))
            Node(objetoL[2].valor, parent = obj.nodo)
            obj.defLocales.nodo.parent = obj.nodo
            Node(objetoL[0].valor, parent = obj.nodo)
            TermList.clear()
        elif num == 15:
            obj = NoElim(num, "DefLocales", Node('DefLocales', parent=root))
        elif num == 16:
            obj = DefLocales16(objetoL[1], objetoL[0], Node('DefLocales', parent=root))
            obj.defLocal.nodo.parent = obj.nodo
            obj.defLocales.nodo.parent = obj.nodo
        elif num == 17 or num == 18:
            obj = DefLocal(objetoL[0], Node('DefLocal', parent=root))
            obj.defSent.nodo.parent = obj.nodo
            if len(ListaVarList)!=0:
                ListaVarList.pop(0)
        elif num == 18:
            obj = NoElim(num, "DefLocal", Node('DefLocal', parent=root))
        elif num == 19:
            obj = NoElim(num, "Sentencias", Node('Sentencias', parent=root))
        elif num == 20:
            obj = Sentencias20(objetoL[1], objetoL[0], Node('Sentencias', parent=root))
            obj.sentencia.nodo.parent = obj.nodo
            obj.sentencias.nodo.parent = obj.nodo
            SenList.append(obj)
            CallList.clear()
        elif num == 21:
            objS = Sentencia21(objetoL[3], objetoL[2], objetoL[1], objetoL[0], Node('Sentencia', parent=root))
            Node(objetoL[3].valor, parent = objS.nodo)
            Node(objetoL[2].valor, parent = objS.nodo)
            objS.expresion.nodo.parent = objS.nodo
            Node(objetoL[0].valor, parent = objS.nodo)
            SenList.append(objS)
            cont = 0
            ExpList.clear()
            anadidos = 0
            x = 0
            partederecha = 0
            if ExpList!=0:
                for obj in VarList:

                    if objetoL[3].valor == obj.identificador.valor and obj.listaVar == self.ambito:
                        aux= obj.tipo.valor
                        aux2 = obj
                        cont = 0
                        while x < anadidos:
                            ErrorList.pop()
                            x+=1
                        break
                    else:
                        if cont ==0:
                            cont = 1
                            #ErrorList.append('Error al asignar ' + str(objetoL[3].valor) +' Variable no existe o no en este contexto')
                            aux = 'mmm'
                            aux2 = 'mmm'
                            anadidos +=1
                        else:
                            pass

                for obj in TermList:
                    objS.listateraux.append(obj)
                i =0
                coincidencias = len(objS.listateraux)
                coincidenciasobj = 0
                variables = list()
                bandera = 0
                correcto = 0
                largo = len(VarList)
                for obj in VarList:
                    if bandera == 1:
                        break
                    if coincidenciasobj == coincidencias:
                        break
                    for obj2 in objS.listateraux:
                        if obj.identificador.valor == objS.listateraux[i].valor:

                            bandera = 0
                            correcto = 1
                            coincidenciasobj +=1
                            if obj.tipo.valor != aux:
                                if cont ==0:
                                    ErrorList.append('Error al asignar ' + str(aux2.identificador.valor) +' tipos de datos diferentes')
                                    bandera = 1
                                    cont+=1
                            else:

                                pass

                        else:
                            largo -=1
                            correcto =0
                            pass                       
                                
                        i +=1

                    i=0
                if largo <=0 and correcto == 0 and coincidenciasobj != coincidencias:
                    if len(VarList)==0:
                        ErrorList.append('Error al asignar ' + str(objetoL[3].valor) +' No existe o no dentro de este contexto')
                        cont+=1
                    else:
                        bandera =1
                contador = 0
                esparametro= 0
                if bandera ==1:
                    if obj2.tipo == 2:
                        obj2.tipo = 'float'
                    elif obj2.tipo == 1:
                        obj2.tipo = 'int'
                    elif obj2.tipo == 0:
                        esparametro= 1
                        for objeto in ParamCList:
                            if objeto.identificador.valor == objS.listateraux[contador].valor:
                                obj2.tipo = objeto.tipo.valor
                                break
                            else: 
                                pass
                                
                    if obj2.tipo != aux:

                        if self.CallFlag!=0:
                            pass
                        else:
                            if cont ==0:
                                ErrorList.append('Error al asignar ' + str(aux2.identificador.valor) +' tipos de datos diferentes')
                                cont+=1
                    else:
                        if len(OpList)==0:
                            if self.callFunc == 0:
                                if esparametro== 0:
                                    pass 
                                else:
                                    pass
                            else:
                                self.callFunc=0
                        else:
                            pass
                        
                if cont ==0 and len(OpList)!=0:
                    for obj5 in TermList:
                        variables.append(Variables(obj5.valor, self.ambito))
                    partederecha = len(variables)
                    if OpList[0] == '+' or OpList[0] == '*':
                        pass
                for ter in TermList:
                    TermCList.append(ter)
                TermList.clear()
                OpList.clear()
                self.CallFlag=0
                if self.PrintFlag==1:                
                    pass
                self.PrintFlag=0
                self.printV=''
            else:
                pass
            aux = 'Sentencia'
            objetoL.clear()
            return objS
        elif num == 22:
            obj = Sentencia22(objetoL[5], objetoL[4], objetoL[3], objetoL[2], objetoL[1], objetoL[0], Node('Sentencia', parent=root))
            Node(objetoL[5].valor, parent = obj.nodo)
            Node(objetoL[4].valor, parent = obj.nodo)
            obj.expresion.nodo.parent = obj.nodo
            Node(objetoL[2].valor, parent = obj.nodo)
            obj.sentenciaB.nodo.parent = obj.nodo
            obj.otro.nodo.parent = obj.nodo
            TermCList.clear()
            ConList.append(obj)
        elif num == 23:
            obj = Sentencia23(objetoL[4], objetoL[3], objetoL[2], objetoL[1], objetoL[0], Node('Sentencia', parent=root))
            Node(objetoL[3].valor, parent = obj.nodo)
            Node(objetoL[2].valor, parent = obj.nodo)
            obj.expresion.nodo.parent = obj.nodo
            Node(objetoL[1].valor, parent = obj.nodo)
            obj.bloque.nodo.parent = obj.nodo
        elif num == 24:
            obj = Sentencia24(objetoL[2], objetoL[1], objetoL[0], Node('Sentencia', parent=root))
            Node(objetoL[2].valor, parent = obj.nodo)
            obj.valorR.nodo.parent = obj.nodo
            Node(objetoL[0].valor, parent = obj.nodo)
            TermList.pop()
            SenList.append(obj)
        elif num == 25:
            obj = Sentencia25(objetoL[1], objetoL[0], Node('Sentencia', parent=root))
            obj.llamadaF.nodo.parent = obj.nodo
            Node(objetoL[0].valor, parent = obj.nodo)
        elif num == 26:
            obj = NoElim(num, "Otro", Node('Otro', parent=root))
        elif num == 27:
            obj = Otro27(objetoL[1], objetoL[0], Node('Otro', parent=root))
            Node(objetoL[1].valor, parent = obj.nodo)
            obj.sentenciaB.nodo.parent = obj.nodo
            ConList.append(obj)
        elif num == 28:
            obj = Bloque(objetoL[2], objetoL[1], objetoL[0], Node('Bloque', parent=root))
            Node(objetoL[2].valor, parent = obj.nodo)
            obj.sentencias.nodo.parent = obj.nodo
            Node(objetoL[0].valor, parent = obj.nodo)
        elif num == 29:
            obj = NoElim(num, "ValorRegresa", Node('ValorRegresa', parent=root))
        elif num == 30:
            obj = ValorRegresa(objetoL[0], Node('ValorRegresa', parent=root))
            obj.expresion.nodo.parent = obj.nodo
            tipo = ''
            contexto = ''
            i = 0
            posi =2
            posfi = 6
            if self.pila[2].valor=='Definicion':
                while i == 0: 
                    posi = posi +2
                    if self.pila[posi].valor == 'Definicion':
                        posfi = posfi +2
                    else:
                        contexto =self.pila[posfi].valor
                        i = 1
                        break
            else:
                contexto= self.pila[4].valor
            if TermList[-1].tipo == 2:
                tipo = 'float'
            elif TermList[-1].tipo == 1:
                tipo = 'int'
            elif TermList[-1].tipo == 0:
                for obj in ParamCList:
                    if TermList[-1].valor == obj.identificador.valor and contexto == obj.contexto:
                        tipo = obj.tipo
                if tipo == '':
                    for obj in VarList:
                        if TermList[-1].valor == obj.identificador.valor and contexto == obj.listaVar:
                            tipo = obj.tipo.valor
                            break
            else:
                tipo = TermList[-1].tipo
                print(tipo)
            self.tiporetorno=obj.tipo.valor

            variables = list()
            if len(OpList)!=0:
                for obj5 in TermList:
                    variables.append(Variables(obj5.valor, self.ambito))
                partederecha = len(variables)
                OpList.clear()
            else:
                pass
            RetList.append(retorno(TermList[-1].valor, tipo, contexto))
        elif num == 31:
            obj = NoElim(num, "Argumentos", Node('Argumentos', parent=root))
        elif num == 32:
            obj = Argumentos(objetoL[1], objetoL[0], Node('Argumentos', parent=root))
            obj.expresion.nodo.parent = obj.nodo
            obj.listaA.nodo.parent = obj.nodo
        elif num == 33:
            obj = NoElim(num, "ListaArgumentos", Node('ListaArgumentos', parent=root))
        elif num == 34:
            obj = ListaArgumentos(objetoL[2], objetoL[1], objetoL[0], Node('ListaArgumentos', parent=root))
            Node(objetoL[2].valor, parent = obj.nodo)
            obj.expresion.nodo.parent = obj.nodo
            obj.listaA.nodo.parent = obj.nodo
        elif num == 35:
            obj = Termino35(objetoL[0], Node('Termino', parent=root))
            obj.llamadaFunc.nodo.parent = obj.nodo
            CallList.append('Llamada')
        elif num == 36 or num == 37 or num == 38 or num == 39:
            obj = Termino(objetoL[0], Node('Termino', parent=root))
            Node(objetoL[0].valor, parent=obj.nodo)
            if num == 36:
                i =0
                largo = len(VarList)
                correcto = 0
                while i< self.VarFlag:
                    if objetoL[0].valor == VarList[i].identificador.valor:
                        correcto = 1
                        contexto = VarList[i].listaVar
                        tipo = VarList[i].tipo
                        break
                    i+=1
                    largo-=1
                    correcto = 0
                flagencontrado = 0
                if largo <=0 and correcto == 0:
                    for objP in ParamCList:
                        if objP.identificador.valor == objetoL[0].valor:
                            flagencontrado = 0
                            break
                        else: 
                            flagencontrado = 1
                if flagencontrado==1:
                    ErrorList.append('Error en la variable ' + str(objetoL[0].valor) +' No existe')
                try:
                    if self.pila[-2].valor=='return' or self.pila[16].valor=='return':
                        contexto =""
                        i = 0
                        posi =2
                        posfi = 6
                        if self.pila[2]=='Definicion':
                            while i == 0: 
                                posi = posi +2
                                if self.pila[posi] == 'Definicion':
                                    posfi = posfi +2
                                else:
                                    contexto =self.pila[posfi].valor
                                    i = 1
                                    break
                        else:
                            contexto= self.pila[4].valor
                        obj.contexto = 'Retorno'+contexto
                    else:
                        obj.contexto = contexto
                except:
                    obj.contexto = contexto
                    pass
                TermList.append(objetoL[0])
            elif num == 37 or num == 38:  
                obj.contexto=self.ambito
                try:
                    if self.pila[14].valor=='return':

                        i = 0
                        contexto = ''
                        posi =2
                        posfi = 6
                        if self.pila[2]=='Definicion':
                            while i == 0: 
                                posi = posi +2
                                if self.pila[posi] == 'Definicion':
                                    posfi = posfi +2
                                else:
                                    contexto =self.pila[posfi].valor
                                    i = 1
                                    break
                            obj.contexto = 'Retorno'+contexto
                        else:
                            obj.contexto = 'Retorno'+self.pila[4].valor

                    else:
                        obj.contexto = obj.contexto
                except:
                    obj.contexto = obj.contexto
                TermList.append(objetoL[0])
        elif num == 40:
            objS = LlamadaFunc(objetoL[3], objetoL[2], objetoL[1], objetoL[0], Node('LlamadaFunc', parent=root))
            Node(objetoL[3].valor, parent=objS.nodo)
            Node(objetoL[2].valor, parent=objS.nodo)
            objS.argumentos.nodo.parent = objS.nodo
            Node(objetoL[0].valor, parent=objS.nodo)
            bandera = 0
            bandera2 =0
            bandera3 = 0
            contexto  = ''
            i = 0
            posi =2
            posfi = 6
            if self.pila[2].valor=='Definicion':
                while i == 0: 
                    posi = posi +2
                    if self.pila[posi].valor == 'Definicion':
                        posfi = posfi +2
                    else:
                        contexto =self.pila[posfi].valor
                        i = 1
                        break
            else:
                contexto= self.pila[4].valor
            entre = 0
            if len(ParamCList)!=0:
                for obj in ParamCList:
                    if objetoL[3].valor == obj.contexto:
                        try:
                            pass
                        except:
                            bandera=1
                            break
                        for obj2 in VarList:

                            if TermList[-1].valor == obj2.identificador.valor and obj2.listaVar == contexto:

                                if obj.tipo.valor == obj2.tipo.valor:
                                    bandera = 0
                                    bandera2=0
                                    if entre ==0:
                                        entre+=1
                                    
                                    if bandera3 ==0:
                                        bandera3+=1
                                    else:
                                        pass
                                    num = ParamCList.index(obj)
                                    TermList.pop()
                                    break
                                else:
                                    bandera = 1

                            else:
                                bandera2=1
                        
                        if bandera2 ==1:
                            tipo = ''
                            if TermList[-1].tipo == 1:
                                tipo = 'int'
                            elif TermList[-1].tipo == 2:
                                tipo = 'float'
                            if tipo == obj.tipo.valor:
                                break
                            else:
                                bandera = 1
                                

                        else:
                            pass

                    else:
                        pass
                tipo = ''
                tipo2 = ''
                if len(RetList)>0:
                    for obj in RetList:
                        if objS.identificador.valor == obj.context:
                            tipo = obj.tipo
                else:
                    tipo = 'void'

                for obj in VarList:
                    if obj.identificador.valor == self.pila[-4].valor and obj.listaVar == contexto:
                        tipo2 = obj.tipo.valor
                if tipo != tipo2:
                    if tipo == 'void':
                        pass
                    else:
                        ErrorList.append('Retorno ' + objetoL[3].valor + ' O tipos de datos diferentes')

                if bandera == 1:
                    ErrorList.append('Error en la llamada a la funcion ' + objetoL[3].valor + ' O tipos de datos diferentes')
                
                self.CallFlag=1
            objetoL.clear()
            return objS
        elif num == 41 or num == 42:
            obj = SentenciaBloque(objetoL[0], Node('SentenciaBloque', parent=root))
            obj.senBlo.nodo.parent = obj.nodo
        elif num == 43:
            obj = Expresion43(objetoL[2], objetoL[1], objetoL[0], Node('Expresion', parent=root))
            Node(objetoL[2].valor, parent=obj.nodo)
            obj.expresion.nodo.parent = obj.nodo
            Node(objetoL[0].valor, parent=obj.nodo)
        elif num == 44 or num == 45:
            obj = Expresion44(objetoL[1], objetoL[0], Node('Expresion', parent=root))
            Node(objetoL[1].valor, parent=obj.nodo)
            obj.expresion.nodo.parent = obj.nodo
        elif num == 46 or num == 47 or num == 48 or num == 49 or num == 50 or num == 51:
            obj = Expresion46(objetoL[2], objetoL[1], objetoL[0], Node('Expresion', parent=root))
            obj.expresion1.nodo.parent = obj.nodo
            Node(objetoL[1].valor, parent=obj.nodo)
            obj.expresion2.nodo.parent = obj.nodo
            if num == 46:
                TermCList.clear()
                OpList.append('*')
                ExpList.append(obj)
            elif num == 47:
                TermCList.clear()
                OpList.append(self.pila[-4].valor)
                ExpList.append(obj)
            elif num == 48:
                TermCList.clear()
                ExpList.append(obj)
            elif num == 49:
                TermCList.clear()
                ExpList.append(obj)
        elif num == 52:
            obj = Expresion52(objetoL[0], Node('Expresion', parent=root))
            obj.termino.nodo.parent = obj.nodo
            ExpList.append(obj)
        else:
            obj = Termino("Hola")
        objetoL.clear()
        return obj

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
        
        self.pilaNodo=[]

        # Llamada para leer las reglas gramaticales y construir la tabla LR
        self.leerReglas()
        while True:
            obj=self.tokens[i]
            fila=self.pila[-1]
            columna=obj.tipo
            accion= self.lr[fila.valor][columna]
            
            if obj.valor == "print":
                i+=1
                obj = self.tokens[i]
                while obj.valor != ')':
                    i+=1
                    obj = self.tokens[i]
                i+=1
                obj=self.tokens[i]

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

                            flagR=0
                            obj3=self.remplazar(elim,obj2.num,flagR)
                            fila = self.pila[-1]
                            accion = self.lr[fila.valor][obj2.num2]
                            self.pila.append(obj3)
                            self.pilaNodo.append(obj3)
                            self.pila.append(self.Estado(accion))
                            
                        else:
                            if obj2.num==10:
                                ambito=self.pila[-4].valor
                            elif obj2.num == 12:
                                z = 0
                                posi =2
                                posfi = 6
                                if self.pila[2]=='Definicion':
                                    while z == 0: 
                                        posi = posi +2
                                        if self.pila[posi] == 'Definicion':
                                            posfi = posfi +2
                                        else:
                                            ambito=self.pila[posfi].valor
                                            z = 1
                                            break
                                else:
                                    ambito= self.pila[4].valor
                            obj3 = self.remplazar(0, obj2.num, 0)
                            self.pila.append(obj3)
                            self.pilaNodo.append(obj3)
                            self.pila.append(self.Estado(accion))
                        break
            
            for p in self.pila:
                pilaS += str(p.valor)
            self.data.append([pilaS, obj.valor, acc])
            pilaS = ""

        for d in self.data:
            print(d)
        print("")
        for pre, fill, node, in RenderTree(root):
            print("%s%s" % (pre, node.name))
        
        semantico=analizadorSemantico().recorrer(root)

        for obj in VarList:
            self.tablaVariables.append([obj.tipo.valor, obj.identificador.valor, obj.listaVar])
        
        print("\nTabla de variables:")
        for v in self.tablaVariables:
            print(v)
        
        if len(ErrorList)!=0:
            for obj in ErrorList:
                print(obj)

        generador=gc.generacionCodigo(root,self.tablaVariables)
        generador.generar()

        

class analizadorSemantico:
    def __init__(self):
        self.tablaSimbolos = {}
    
    def recorrer(self, arbol):
        for node in PreOrderIter(arbol):

            if node.name == 'DefFunc':
                self.defFunc(node)
            elif node.name == 'LlamadaFunc':
                self.llamadaFunc(node)
            
    def defVar(self, node):
        tipo = node.children[0].name
        print('TIPO', tipo)
        if tipo not in ["int", "void", "float","string"]:
            raise ValueError(f"Error tipo de dato invalido en la variable {node.children[1].name}")
        
        if node.children[1].name not in self.tablaSimbolos:
            self.tablaSimbolos[node.children[1].name] = tipo

    def defFunc(self, node):  
        if node.children[1].name not in self.tablaSimbolos:
            self.tablaSimbolos[node.children[1].name] = 'funcion'

    def llamadaFunc(self, node):
        if node.children[0].name not in self.tablaSimbolos:
            ErrorList.append("Error la funcion "+node.children[0].name + " no ha sido definida")

