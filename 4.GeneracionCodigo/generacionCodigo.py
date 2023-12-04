import os
from anytree import Node, RenderTree, PreOrderIter,LevelOrderIter

class generacionCodigo():

    def __init__(self,arbol,tablaVariables):
        self.arbol=arbol
        self.tablaVariables=tablaVariables
        self.arbolV=[]
        self.variables={}
        self.valorVariables={}
        self.aux=[]
        self.operacion=""
    
    def generar(self):
        with open("codigo.asm", "w") as codigo:
            codigo.write('.Model\n')
            codigo.write('.stack\n')
            codigo.write('.data\n')
            codigo.write('res dw 0\n')
            codigo.write('decm db 0\n')
            codigo.write('unim db 0\n')
            codigo.write('cen db 0\n')
            codigo.write('dece db 0\n')
            codigo.write('uni db 0\n')
            codigo.write("msg3 db 10,13,17,'El resultado es:','$'\n")

        for node in LevelOrderIter(self.arbol):
            self.arbolV.append(node.name)
            if node.name == 'Sentencia':
                self.aux=[]
                ban=True
                for nodeH in LevelOrderIter(node):
                    if(nodeH.name=='Sentencia'):
                        continue
                    elif(nodeH.name=='Expresion'):
                        continue
                    elif(nodeH.name=='Termino'):
                        continue
                    elif(nodeH.name==';'):
                        continue
                    self.aux.append(nodeH.name)
                    if nodeH.name == '+':
                        self.operacion="operacionSuma"
                        ban=False
                    elif nodeH.name == '-':
                        self.operacion="operacionResta"
                        ban=False
                    else:
                        if(ban):
                            self.operacion='declaracion'
                #self.aux.append(self.operacion)
                self.aux.insert(0,self.operacion)
                for lista in self.tablaVariables:
                    if self.aux[1]==lista[1]:
                        self.variables[self.aux[1]]=self.aux

        for clave, valor in self.variables.items():
            #print(f'Clave: {clave}, Valor: {valor}')
            if 'declaracion' in valor:
                self.valorVariables[clave]=valor[3]
            if 'operacionSuma' in valor:
                self.generarSuma(clave)
            elif 'operacionResta' in valor:
                print("generar resta")
 
    def generarSuma(self,it):
        lista=self.variables[it]
        with open("codigo.asm", "a") as codigo:
            codigo.write(f"{lista[1]} dw 0\n")
            codigo.write(f"{lista[4]} dw {self.valorVariables[lista[4]]}\n")
            codigo.write(f"{lista[5]} dw {self.valorVariables[lista[5]]}\n")
            codigo.write(".code\nmov ax,data\nmov ds,ax\nmov ah,09h\nmov ax,0\nmov bx,0\n")
            codigo.write(f"mov ax,[{lista[4]}]\n")
            codigo.write(f"mov bx,[{lista[5]}]\n")
            codigo.write(f"add ax,bx\nmov {lista[1]},ax\n")
            codigo.write(f"jmp imprimir\nimprimir:\nmov ah,09h\nlea dx,msg3\nint 21h\nmov ax,0\nmov ax,{lista[1]}")
            imprimir="""
mov bx,2710h
xor dx,dx
div bx
mov decm,al
mov ax,dx
mov bx,1000
xor dx,dx
div bx
mov unim,al
mov ax,dx
mov bx,100
xor dx,dx
div bx
mov cen,al
mov ax,dx
mov bx,10
xor dx,dx
div bx
mov dece,al
mov uni,dl
;Imprimimos
mov ah,02h
mov dl,decm
add dl,30h
int 21h
mov ah,02h
mov dl,unim
add dl,30h
int 21h
mov ah,02h
mov dl,cen
add dl,30h
int 21h
mov dl,dece
add dl,30h
int 21h
mov dl,uni
add dl,30h
int 21h
mov ah,04ch
int 21h
end
            """
            codigo.write(imprimir)
        print("\nCodigo generado en asm:")
        with open('codigo.asm','r') as codigo:
            contenido=codigo.read()
        print(contenido)

        