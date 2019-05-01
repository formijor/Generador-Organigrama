'''
Created on 1 may. 2019

@author: jor_l
'''
import wx
import objetoModulo

class Puntero(objetoModulo.Objeto):
    def __init__(self, parent, frame, id_objeto):
        objetoModulo.Objeto.__init__(self, id_objeto, 'cursor')
        self.parent = parent
        self.frame = frame
        self.pos = (100, 100)
        self.__crear_puertos()
        
    def SetPosition(self, pos):        
        self.pos = pos
        
    def GetSize(self):
        return 5, 5
        
    def GetPosition(self):
        return self.pos
    
    def reposicionar_cursor(self, pos):
        self.posicion = pos
        self.parent.WarpPointer(pos[0], pos[1])
        
    def __crear_puertos(self):
        size = self.GetSize()
        self.__arriba = size[0] / 2
        self.__abajo = size[0] / 2
        self.__izquierda = size[1] / 2
        self.__derecha = size[1] / 2
        self.puertos = {'arriba': self.__arriba, 'abajo': self.__abajo, 
                        'izquierda': self.__izquierda, 'derecha': self.__derecha}
        self.get_coordenadas_puertos(True)
    
    def get_coordenadas_puertos(self, relativo):       
        puertos = self.get_puertos()        
        pos = self.GetPosition()
        arriba = (pos[0] + puertos.get('arriba'), pos[1])
        abajo = (pos[0] + puertos.get('abajo'), pos[1] + self.GetSize()[1])
        izquierda = (pos[0], pos[1] + puertos.get('izquierda'))
        derecha = (pos[0]) + self.GetSize()[0], pos[1] + puertos.get('derecha')
        self.coordenadas_puertos = {'arriba' : arriba, 'abajo': abajo,
                                    'izquierda': izquierda, 'derecha': derecha}
        if relativo:
            return self.coordenadas_puertos
        elif not relativo:
            return puertos
    
    def get_coordenadas_puerto(self, puerto):
        self.get_coordenadas_puertos(True)
        return self.coordenadas_puertos[puerto]