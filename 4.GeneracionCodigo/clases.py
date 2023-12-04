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
        self.fuente = 'Definiciones'
        self.nodo = nodo

class Definicion:
    def __init__(self, defi, nodo):
        self.defi = defi
        self.fuente = 'Definicion'
        self.nodo = nodo

class DefVar:
    def __init__(self, tipo, identificador, listaVar, puntoyComa, nodo):
        self.tipo = tipo
        self.identificador =  identificador
        self.listaVar = listaVar
        self.puntoyComa = puntoyComa
        self.fuente = 'DefVar'
        self.nodo = nodo

class ListaVar8:
    def __init__(self, identificador, listaVar, nodo):
        self.identificador = identificador
        self.listaVar =  listaVar
        self.fuente = 'ListaVar'
        self.nodo = nodo

class DefFunc:
    def __init__(self, tipo, identificador, parA, parametros, parC, bloqFunc, nodo):
        self.tipo = tipo
        self.identificador = identificador
        self.parA = parA
        self.parametros = parametros
        self.parC = parC
        self.bloqFunc = bloqFunc
        self.fuente = 'DefFunc'
        self.nodo = nodo

class Parametros:
    def __init__(self, tipo, identificador, listaParam, nodo):
        self.tipo = tipo
        self.identificador =  identificador
        self.listaParam = listaParam
        self.fuente = 'Parametros'
        self.nodo = nodo

class ParametrosCon:
    def __init__(self, tipo, identificador, contexto, nodo):
        self.tipo = tipo
        self.identificador =  identificador
        self.contexto = contexto
        self.fuente = 'Parametros'
        self.nodo = nodo


class ListaParam:
    def __init__(self, tipo, identificador, listaParam, nodo):
        self.tipo = tipo
        self.identificador =  identificador
        self.listaParam = listaParam
        self.fuente = 'ListaParam'
        self.nodo = nodo

class BloqFunc:
    def __init__(self, parA, defLocales, parC, nodo):
        self.parA = parA
        self.defLocales =  defLocales
        self.parC = parC
        self.fuente = 'BloqFunc'
        self.nodo = nodo

class DefLocales16:
    def __init__(self, defLocal, defLoclales, nodo):
        self.defLocal = defLocal
        self.defLocales = defLoclales
        self.fuente = 'DefLocales'
        self.nodo = nodo

class DefLocal:
    def __init__(self, defSent, nodo):
        self.defSent = defSent
        self.fuente = 'DefLocal'
        self.nodo = nodo

class Sentencias20:
    def __init__(self, sentencia, sentencias, nodo):
        self.sentencia = sentencia
        self.sentencias = sentencias
        self.fuente = 'Sentencias'
        self.nodo = nodo


class Sentencia21:
    def __init__(self, identificador, op, expresion, puntoyComa, nodo):
        self.identificador = identificador
        self.op = op
        self.expresion = expresion
        self.puntoyComa = puntoyComa
        self.fuente = 'Sentencia'
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
        self.fuente = 'Sentencia'
        self.nodo = nodo

class Sentencia23:
    def __init__(self, whileV, parA, expresion, parC, bloque, nodo):
        self.whileV = whileV
        self.parA = parA
        self.expresion = expresion
        self.parC = parC
        self.bloque = bloque
        self.fuente = 'Sentencia'
        self.nodo = nodo

class Sentencia24:
    def __init__(self, returnV, valorR, puntoyComa, nodo):
        self.returnV = returnV
        self.valorR = valorR
        self.puntoyComa = puntoyComa
        self.fuente = 'Sentencia'
        self.nodo = nodo

class Sentencia25:
    def __init__(self, llamadaF, puntoyComa, nodo):
        self.llamadaF = llamadaF
        self.puntoyComa = puntoyComa
        self.fuente = 'Sentencia'
        self.nodo = nodo

class Otro27:
    def __init__(self, elseV, sentenciaB, nodo):
        self.elseV = elseV
        self.sentenciaB = sentenciaB
        self.fuente = 'Otro'
        self.nodo = nodo

class Bloque:
    def __init__(self, parA, sentencias, parC, nodo):
        self.parA = parA
        self.sentencias = sentencias
        self.parC = parC
        self.fuente = 'Bloque'
        self.nodo = nodo

class ValorRegresa:
    def __init__(self, expresion, nodo):
        self.expresion = expresion
        self.fuente = 'Valor Regresa'
        self.nodo = nodo

class Argumentos:
    def __init__(self, expresion, listaA, nodo):
        self.expresion = expresion
        self.listaA = listaA
        self.fuente = 'Argumentos'
        self.nodo = nodo

class ListaArgumentos:
    def __init__(self, comaV, expresion, listaA, nodo):
        self.comaV = comaV
        self.expresion = expresion
        self.listaA = listaA
        self.fuente = 'Lista Argumentos'
        self.nodo = nodo

class Termino35:
    def __init__(self, llamadaFunc, nodo):
        self.llamadaFunc = llamadaFunc
        self.fuente = 'Termino'
        self.nodo = nodo

class Termino:
    def __init__(self, dato, nodo):
        self.dato = dato
        self.fuente = 'Termino'
        self.nodo = nodo

class LlamadaFunc:
    def __init__(self, identificador, parA, argumentos, parC, nodo):
        self.identificador = identificador
        self.parA = parA
        self.argumentos = argumentos
        self.parC = parC
        self.fuente = 'Llamada Funcion'
        self.nodo = nodo

class SentenciaBloque:
    def __init__(self, senBlo, nodo):
        self.senBlo = senBlo
        self.fuente = 'Sentencia Bloque'
        self.nodo = nodo


class Expresion43:
    def __init__(self, parenA, expresion, parenC, nodo):
        self.parenA = parenA
        self.expresion = expresion
        self.parenC = parenC
        self.fuente = 'Expresion'
        self.nodo = nodo

class Expresion44:
    def __init__(self, op, expresion, nodo):
        self.op = op
        self.expresion = expresion
        self.fuente = 'Expresion'
        self.nodo = nodo

class Expresion46:
    def __init__(self, expresion1, op, expresion2, nodo):
        self.expresion1 = expresion1
        self.op = op
        self.expresion2 = expresion2
        self.fuente = 'Expresion'
        self.nodo = nodo

class Expresion52:
    def __init__(self, termino, nodo):
        self.termino = termino
        self.fuente = 'Expresion'
        self.nodo = nodo

class NoElim:
    def __init__(self, nume, fuente, nodo):
        self.nume = nume
        self.fuente = fuente
        self.nodo = nodo