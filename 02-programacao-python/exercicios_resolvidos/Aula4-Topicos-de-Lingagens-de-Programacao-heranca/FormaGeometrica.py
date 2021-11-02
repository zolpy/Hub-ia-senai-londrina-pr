# Limpa Tela (CTRL+L) ou (CLEAR) ou 
import os
os.system('cls' if os.name == 'nt' else 'clear')

import math
import matplotlib.pyplot as plt


############################################
"""
1. `FormaGeometrica`:
  * Atributos `x` e `y` que marcam a posição inicial da forma geométrica
  * Método `desenhe()` que deve mostrar o texto: 
   
  > Forma Geométrica Centrada em (`x`,`y`)
"""

class FormaGeometrica:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.nomeclasse = self.__class__.__name__
        print(f'Nome da classe: ({self.nomeclasse})\n')
        
    def desenhe(self):
        print(f'{self.nomeclasse} está centrada em ({self.x},{self.y})\n')
  
############################################
"""
1. `Forma2D`
  * Superclasse: `FormaGeometrica`;
"""        

class Forma2d(FormaGeometrica):
    
    def __init__(self, x, y, largura=None, comprimento=None):
        super().__init__(x,y)
        if largura != None:
            self.largura = largura
            if comprimento > largura:
               self.figura = 'Retângulo'
            else:
               self.figura = 'Quadrado'  
        if comprimento != None:
            self.comprimento = comprimento
            if comprimento > largura:
               self.figura = 'Retângulo'
            else:
               self.figura = 'Quadrado'  
        else:
            self.comprimento = largura


############################################
"""
1. `Forma3D`
  * Superclasse: `FormaGeometrica`
"""
class Forma3D(FormaGeometrica):
    
    def __init__(self, x, y, z, raio = None, lado = None):
        super().__init__(x,y)
        self.z = z
        if raio != None:
            self.raio = raio
            
        if lado != None:
            self.lado = lado
                        
    def desenhe(self):
        print(f'A classe {self.nomeclasse} tem suas coordenadas centrada em: é: ({self.x},{self.y},{self.z})')

############################################
"""
1. `Poligono`
  * Superclasse: `Forma2D`

Implemente operações que calculem a **área**, **perímetro** e **volume** das
formas quando cabível.  
"""
class Poligono(Forma2d):

    def Area(self):
        self.area = self.largura * self.comprimento
        return self.area
    
    def Perimetro(self):
        self.perimetro = (2*self.comprimento) + (2*self.largura)
        return self.perimetro
    
    def desenhe(self):
        print(f'Classe {self.nomeclasse}\n  # Perimetro: ({round(self.Perimetro())} uni)\n  # Área: ({round(self.Area())} u²)\n  # Figura: {self.figura}\n')
        
############################################
"""
1. `Retangulo`
  * Superclasse: `Poligono`
"""
class Retangulo(Poligono):
    def desenhe(self):
        print(f'Classe {self.nomeclasse}\n  # Perímetro: ({round(self.Perimetro())} unidades)\n  # Área: ({round(self.Area())} u²)\n  # Figura: {self.figura}\n')

    pass


############################################
"""
1. `Quadrado`
  * Superclasse: `Retangulo`
"""
class Quadrado(Retangulo):
    def desenhe(self):
        print(f'Classe {self.nomeclasse}\n  # Perímetro: ({self.Perimetro()} unidades)\n  # Área: ({self.Area()} u²)\n  # Figura: {self.figura}\n')

    pass

############################################
"""
1. `Circulo`
  * Superclasse: `Forma2D`
"""

class Circulo(Forma2d):
    def __init__(self, x, y, raio):
        super().__init__(x,y)
        self.raio = raio
      
    def Area(self):
        self.area = math.pi * (self.raio ** 2)
        return self.area
    
    def Comprimento_circunferencia(self):
        self.comprimento_circunferencia = 2 * math.pi * self.raio
        return self.comprimento_circunferencia
    
    def desenhe(self):
        print(f'Classe {self.nomeclasse}\n  # Comprimentro da Circunferência: ({round(self.Comprimento_circunferencia())} unidades)\n  # Área: ({round(self.Area())} u²)\n  # Figura: {self.nomeclasse}\n')


        fig, ax = plt.subplots()
        ax.add_patch(plt.Circle((self.x, self.y), 0.1, color='r', alpha=0.5))
        ax.set_aspect('equal', adjustable='datalim')
        ax.plot()   #Causes an autoscale update.
        plt.show()
############################################
"""
1. `Esfera`
  * Superclasse: `Forma3D`
"""
class Esfera(Forma3D):
    
    def __init__(self, x, y, z, raio):
        super().__init__(x,y,z)
        self.raio = raio
    
    def Area(self):
        self.area_esfera = 4*  math.pi * (self.raio ** 2)
        return self.area_esfera
    
    def Volume(self):
        self.volume_esfera = (4/3) * math.pi * (self.raio **3)
        return self.volume_esfera
    
    def desenhe(self):
        print(f'Classe {self.nomeclasse}\n  # Centrada nas coordenadas: ({self.x},{self.y},{self.z})\n  # Raio: ({self.raio} unidades)\n  # Área: ({round(self.Area())} u²)\n  # Volume: ({round(self.Volume())} u³)\n')

############################################
"""
1. `Cubo`
  * Superclasse: `Forma3D`
"""
class Cubo(Forma3D):
    def __init__(self, x, y, z, aresta):
        super().__init__(x, y, z)
        self.aresta = aresta
    
    def Area(self):
        self.area = 6 * (self.aresta**2)
        return self.area
    
    def Perimetro(self):
        self.perimetro = 12 * self.aresta
        return self.perimetro

    def Volume(self):
        self.volume = self.aresta**3
        return self.volume

    def desenhe(self):
        print(f'Classe {self.nomeclasse}\n Centrado nas coordenadas: ({self.x},{self.y},{self.z})\n  # Aresta mede: ({self.aresta} unidades)\n  # Perímetro: ({round(self.Perimetro())} unidades)\n  # Área: ({round(self.Area())} u²)\n  # Volume: ({round(self.Volume())} u³)\n')

############################################
"""
1. `Cilindro`
  * Superclasse: `Forma3D`
"""
class Cilindro(Forma3D): 

    def __init__(self, x, y, z, raio, altura):
        super().__init__(x, y, z)
        self.raio = raio
        self.altura = altura

    #Area total = Area Lateral + Area dos 2 circulos (Tampa de cima e base)    
    def Area(self):
        self.area = 2 * (math.pi * self.raio**2) + (2 * math.pi * self.raio * self.altura)
        return self.area

    def Perimetro(self):
        self.perimetro = (2 * self.raio) * math.pi
        return self.perimetro    

    def Volume(self):
        self.volume = math.pi * self.raio**2 * self.altura
        return self.volume

    def desenhe(self):
        print(f'Classe {self.nomeclasse}\n  # Centrado nas coordenadas: ({self.x},{self.y},{self.z})\n  # Raio: ({self.raio} unidades)\n  # Altura: ({self.altura} unidades)\n  # Perimetro: ({round(self.Perimetro())} unidades)\n  # Área: ({round(self.Area())} u²)\n  # Volume: ({round(self.Volume())} u³)\n')

############################################
"""
Criar uma nova classe chamada `Quadro`. Essa classe deve ter, como atributo,
uma lista de figuras geométricas chamada `figuras_geometricas`. 

Implemente o método `desenhe()` na classe `Quadro`. Esse método deve chamar a
função `desenhe()` de todos os objetos contidos na lista armazenada em `Quadro`

Adicionar métodos para \textbf{incluir} uma nova figura e \textbf{remover} uma
figura armazenada em uma dada posição da lista. 

"""
class Quadro:
    
    def __init__(self,figuras_geometricas: list):
        self.figuras_geometricas = figuras_geometricas

    def listaFiguras(self):
        if len(self.figuras_geometricas) != 0:
            for index, figura in enumerate(self.figuras_geometricas):
                print("{} -> {}".format(index, figura))
        else:
            print("Tá vázio!")    
    def Incluir(self, figura):
        self.figuras_geometricas.append(figura)
        return self.figuras_geometricas

    def removerIndex(self, index):
        try:
            self.figuras_geometricas.pop(index)
        except(IndexError):
            print("Indice fornecido não existe")  

    def removerFigura(self, figura):
        if figura in self.figuras_geometricas:
            self.figuras_geometricas.remove(figura)
        else:
            print("Forma não encontrada")         

    def desenhe(self):
        if len(self.figuras_geometricas) != 0:
            for index, figura in enumerate(self.figuras_geometricas):
                print("( {} ) ".format(index), end='')
                figura.desenhe()
        else:
           print("O quadro está vazio.")     

        
#(1)###########################################
print('#'*50)
fg=FormaGeometrica(0,0)
print('#'*50)
fg.desenhe()

#(2)############################################
print('#'*50)
fg2d=Forma2d(0,0, 2, 8)
fg2d.desenhe()

#(3)############################################
print('#'*50)
poligono=Poligono(0,0,16,16)
poligono.desenhe()

#(4)############################################
print('#'*50)
retangulo=Retangulo(0,0,8,16)
retangulo.desenhe()

#(5)############################################
print('#'*50)
quadrado=Quadrado(0,0,3,8)
quadrado.desenhe()

#(6)############################################
print('#'*50)
circulo=Circulo(4,0,8)
circulo.desenhe()

#(7)############################################
print('#'*50)
esfera=Esfera(0,0,0,5)
esfera.desenhe()

#(8)############################################
print('#'*50)
cubo=Cubo(0,0,0,5)
cubo.desenhe()

#(9)############################################
print('#'*50)
cilindro=Cilindro(0,0,0,3,5)
cilindro.desenhe()
print('#'*50)

############################################
print("QUADRO\n  # Incluir")
quadro = Quadro([fg])
quadro.Incluir(esfera)
quadro.Incluir(cubo)
quadro.Incluir(cilindro)
quadro.Incluir(fg2d)
quadro.Incluir(poligono)
quadro.Incluir(retangulo)
quadro.Incluir(quadrado)
quadro.Incluir(circulo)
quadro.desenhe()

print('#'*50)
print("Listar figuras\n")
print(quadro.listaFiguras())
print('#'*50)
print("Mais figuras\n")
quadro.Incluir(quadrado)
quadro.Incluir(cubo)
quadro.desenhe()
print("Listar figuras\n")
print(quadro.listaFiguras())

print('#'*50)
print("Rermover figuras\n")
quadro.removerFigura(quadrado)
quadro.desenhe()
print("Listar figuras\n")
print(quadro.listaFiguras())

print('#'*50)
print("Rermover por Index: index 5\n")
quadro.removerIndex(5)
quadro.desenhe()
print("Listar figuras\n")
print(quadro.listaFiguras())

