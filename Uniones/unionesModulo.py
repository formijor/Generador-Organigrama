'''
Created on 30 sep. 2018

@author: Jorge
'''

import objetoModulo
#import tablero
import wx

class Uniones():
    def __init__(self):
        self.lista_uniones = {}
    
    def crear_union(self, conexion): 
        #if     Agregar una forma de seleccionar tipo de conexion, o pasarle la conexion ya creada (MEJOR)?
        self.lista_uniones[conexion.get_id()] = conexion
    
    def actualizar_uniones(self, dc):
        for conexion in self.lista_uniones.values():
            conexion.crear_conexion()
            conexion.dibujar(dc)
            
        
class Union():
    def __init__(self, parent, objeto1, objeto2, tipo):
        #self.id_conexion = id_union
        self.objeto1 = objeto1
        self.objeto2 = objeto2
        self.generar_id()
        self.lista_puntos = []
        self.tipo = tipo
    
    def generar_id(self):
        self.id_conexion = (self.objeto1.get_id_objeto(), self.objeto2.get_id_objeto())
    
    def get_id(self):
        return self.id_conexion
    
    def get_objetos(self):
        return self.objeto1, self.objeto2
    
    def get_posicion_objetos(self):
        return [self.objeto1.GetPosition(), self.objeto2.GetPosition()]
    
    def get_size_objetos(self):
        return [self.objeto1.GetSize(), self.objeto2.GetSize()]


class Conexion(Union):
    def __init__(self, parent, tipo, objeto1, objeto2):
        Union.__init__(self, parent, objeto1, objeto2, tipo)
        self.parent = parent
        
    def dibujar(self, dc):
        dc.SetPen(wx.Pen("GREEN", 3))        
        for punto in self.lista_puntos:     
            dc.DrawLine(punto[0], punto[1])
          
    def crear_conexion(self):
        objeto1, objeto2 = self.get_objetos()
        puerto1, puerto2, diferencia = self.seleccionar_puertos(objeto1, objeto2)
        boton1_pos, boton2_pos = self.coordenadas_puertos(puerto1, puerto2)
        #boton1_pos = self.objeto1.get_coordenadas_puerto(puerto1)
        #boton2_pos = self.objeto2.get_coordenadas_puerto(puerto2)
               
        curva1 = (boton1_pos[0], boton1_pos[1] + diferencia)
        curva2 = (boton2_pos[0], curva1[1])
        self.lista_puntos = [boton1_pos, curva1], [curva1, curva2], [curva2, boton2_pos] 
    
    def coordenadas_puertos(self, puerto1, puerto2):
        boton1_pos = self.objeto1.get_coordenadas_puerto(puerto1)
        boton2_pos = self.objeto2.get_coordenadas_puerto(puerto2)
        return boton1_pos, boton2_pos
        
        
    def seleccionar_puertos(self, objeto1, objeto2):
        x1, y1 = self.objeto1.GetPosition()
        x2, y2 = self.objeto2.GetPosition()
        size1, size2 = self.get_size_objetos()       
        rango_especial = size1[1] * 2
        rango_especial2 = size1[0] * 2    
        pos_x = (x1 - x2) * -1
        pos_y = (y1 - y2) * -1
        puerto1, puerto2 = 'arriba', 'abajo'
        if pos_x >= 0 and pos_y >= 0:
            seccion = 4
        elif pos_x >= 0 and pos_y <= 0:
            seccion = 3
        elif pos_x <= 0 and pos_y >= 0:
            seccion = 1
        elif pos_x <= 0 and pos_y <= 0:
            seccion = 2        
        
        if seccion == 4 or seccion == 1:
            #diferencia = size1[1] / 2
            diferencia = (x1 - x2) / 2
            puerto1 = 'abajo'
            puerto2 = 'arriba'
        elif seccion == 3 or seccion == 2:
            diferencia = -((x1 - x2) / 2)
            #diferencia = -(size1[1] / 2)
            puerto1 = 'arriba'
            puerto2 = 'abajo'
        
        if (pos_y < 0):
            pos_y = pos_y * -1
        
        if pos_y < rango_especial:
            diferencia = 0
            if seccion == 4 or seccion == 3:
                puerto1 = 'derecha'
                #puerto2 = 'Izquierda'
            elif seccion == 1 or seccion == 2:
                #diferencia = -10
                puerto1 = 'izquierda'
                #puerto2 = 'Derecha'
                
        if pos_y < rango_especial * 0.5:
            diferencia = 0
            if seccion == 4 or seccion == 3:
                puerto2 = 'izquierda'
            elif seccion == 1 or seccion == 2:
                #diferencia = 10
                puerto2 = 'derecha'
            
        return puerto1, puerto2, diferencia