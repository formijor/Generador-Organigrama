

import wx

class ReglasManager():
    def __init__(self):
        pass
    
    
    
class ReglaLibre(ReglasManager):
    def __init__(self):
        pass




class Niveles(object):
    def __init__(self):
        self.lista_niveles = {}
        
    def agregar_nivel(self, nivel):
        self.lista_niveles[nivel.get_id()] = nivel
        
class Nivel(object):
    def __init__(self, id_nivel):
        self.id_nivel = id_nivel
        self.lista_objetos = []
        self.frame_size = ""
        
        
    def actualizar_posicion_objetos(self):
        for objeto in self.lista_niveles:
            pos = objeto.GetPosition()
            
            
    def columnas(self):
        pass
        
    
    
    