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
    
    def crear_union(self, parent, tipo_conexion, objeto1, objeto2): 
        #if     Agregar una forma de seleccionar tipo de conexion, o pasarle la conexion ya creada (MEJOR)?
        union = Union(parent, tipo_conexion, objeto1, objeto2)
        self.lista_uniones[union.get_id()] = union
    
    def actualizar_uniones(self, dc):
        for conexion in self.lista_uniones.values():
            conexion.actualizar_union()
            conexion.dibujar(dc)
        
    def get_union(self, id_union):
        return self.lista_uniones[id_union]
    
    def get_union_objetos(self, id_union):
        return self.lista_uniones[id_union].get_objetos()
    
    def eliminar_union(self, id_union):
        self.lista_uniones.pop(id_union)
        
        
class Union():
    def __init__(self, parent, tipo, objeto1, objeto2):
        self.parent = parent
        self.tipo = tipo
        self.objeto1 = objeto1
        self.objeto2 = objeto2
        self.objeto1_pos = ()
        self.objeto2_pos = ()
        self.generar_id()
        self.lista_puntos = []
        
        #self.pos_anterior_objeto1 = ''
        #self.pos_anterior_objeto2 = ''
    
    def generar_id(self):
        if self.tipo == 'cursor':
            self.id_union = 'cursor'
        else:
            self.id_union = (self.objeto1.get_id_objeto(), self.objeto2.get_id_objeto())
    
    def get_id(self):
        return self.id_union
    
    def get_objetos(self):
        return self.objeto1, self.objeto2
    
    def get_posicion_objetos(self):
        return self.objeto1.GetPosition(), self.objeto2.GetPosition()
    
    def get_size_objetos(self):
        return [self.objeto1.GetSize(), self.objeto2.GetSize()]
    
    def actualizar_posicion_objetos(self):
        self.objeto1_pos = self.objeto1.GetPosition()
    
    def cambios_posicion(self):
        if self.objeto1.cambio_posicion(self.objeto1_pos) or self.objeto2.cambio_posicion(self.objeto2_pos):
            return True
        else:
            return False

    """def crear_conexion_old(self):
        #self.objeto1_pos, self.objeto2_pos = self.get_posicion_objetos()
        objeto1, objeto2 = self.get_objetos()
        self.actualizar_nueva_posicion()
        puerto1, puerto2, diferencia = self.seleccionar_puertos2(objeto1, objeto2)
        boton1_pos, boton2_pos = self.get_coordenadas_puertos(puerto1, puerto2)        
        #self.pos_anterior_objeto1 = self.objeto1_pos
        #self.pos_anterior_objeto2 = self.objeto2_pos       
        curva1 = (boton1_pos[0], boton1_pos[1] + diferencia)
        curva2 = (boton2_pos[0], curva1[1])
        self.lista_puntos = [boton1_pos, curva1], [curva1, curva2], [curva2, boton2_pos]
    """
    def crear_conexion(self):
        self.actualizar_nueva_posicion()
        objeto1_puerto, objeto2_puerto= self.seleccionar_puertos2()
        coordenadas = self.get_coordenadas_puertos(objeto1_puerto, objeto2_puerto)
        self.lista_puntos = coordenadas
    
    def actualizar_nueva_posicion(self):
        self.objeto1_pos = self.objeto1.GetPosition()
        self.objeto2_pos = self.objeto2.GetPosition()
    
    """def actualizar_union_old(self):
        #self.get_posicion_objetos()
        if self.cambios_posicion():
            puerto1, puerto2, diferencia = self.seleccionar_puertos2()
            boton1_pos, boton2_pos = self.get_coordenadas_puertos(puerto1, puerto2)
            self.actualizar_nueva_posicion()
            curva1 = (boton1_pos[0], boton1_pos[1] + diferencia)
            curva2 = (boton2_pos[0], curva1[1] )
            self.lista_puntos = [boton1_pos, curva1], [curva1, curva2], [curva2, boton2_pos]
    """
    def actualizar_union(self):
        if self.cambios_posicion():
            self.actualizar_nueva_posicion()
            objeto1_puerto, objeto2_puerto, resultado= self.seleccionar_puertos()
            coordenadas = self.get_coordenadas_puertos(objeto1_puerto, objeto2_puerto)
            curva1, curva2 = self.__calcular_curvas(resultado, coordenadas)
            
            self.lista_puntos = [coordenadas[0], curva1],[curva1,curva2],[curva2,coordenadas[1]]           
    
    def get_coordenadas_puertos(self, puerto1, puerto2):
        boton1_coordenadas = self.objeto1.get_coordenadas_puerto(puerto1)
        boton2_coordenadas = self.objeto2.get_coordenadas_puerto(puerto2)
        return boton1_coordenadas, boton2_coordenadas
    
    """def seleccionar_puertos(self):
        (x1, y1), (x2, y2) = self.get_posicion_objetos()
        size1, size2 = self.get_size_objetos()       
        rango_especial = size1[1] * 2
        rango_especial2 = size1[0] * 2  
        pos_x = (x1 - x2) * -1
        pos_y = (y1 - y2) * -1
        #puerto1, puerto2 = 'arriba', 'abajo'
        if pos_x >= 0 and pos_y >= 0:
            seccion = 4
        elif pos_x >= 0 and pos_y <= 0:
            seccion = 3
        elif pos_x <= 0 and pos_y >= 0:
            seccion = 1
        elif pos_x <= 0 and pos_y <= 0:
            seccion = 2        
        
        if seccion == 4 or seccion == 1:
            diferencia = size1[1] / 2
            #diferencia = (x1 - x2) / 2
            puerto1 = 'abajo'
            puerto2 = 'arriba'
        elif seccion == 3 or seccion == 2:
            #diferencia = -((x1 - x2) / 2)
            diferencia = -(size1[1] / 2)
            puerto1 = 'arriba'
            puerto2 = 'abajo'
        
        if (pos_y < 0):
            pos_y = pos_y * -1
        
        "El numero a multiplicar determina separacion entre norte y este y oeste etc"
        if pos_y < rango_especial * 2: 
            diferencia = 0
            if seccion == 4 or seccion == 3:
                puerto1 = 'derecha'
                #puerto2 = 'izquierda'
            elif seccion == 1 or seccion == 2:
                #diferencia = -10
                puerto1 = 'izquierda'
                #puerto2 = 'derecha'
        
        "Determina si esta mas cerca un objeto de otro en el eje Y"    
        if pos_y < rango_especial * 0.5:
            diferencia = 0
            if seccion == 4 or seccion == 3:
                puerto2 = 'izquierda'
            elif seccion == 1 or seccion == 2:
                #diferencia = 10
                puerto2 = 'derecha'
        return puerto1, puerto2, diferencia       
    """  
    def seleccionar_puertos(self):
        (x1, y1), (x2, y2) = self.get_posicion_objetos()
        size1, size2 = self.get_size_objetos()
        ancho_max_y = self.__determinar_ancho_max_eje_y(size1[1])
        ancho_min_y = self.__determinar_ancho_min_eje_y(size1[1])
        (objeto1_puerto, objeto2_puerto), resultado = self.__determinar_posicion_relativa(x1, x2, y1, y2, ancho_max_y, ancho_min_y)
        return objeto1_puerto, objeto2_puerto, resultado   
    
    def __determinar_ancho_max_eje_y(self, size_eje_y):
        return size_eje_y * 5 
        
    def __determinar_ancho_min_eje_y(self, size_eje_y):
        return size_eje_y * 2.5
    
    def __determinar_posicion_relativa(self, x1, x2, y1, y2, ancho_max_y, ancho_min_y):
        especial = self.__determinar_posicion_especial(y1, y2, ancho_max_y, ancho_min_y)
        eje_y = self.__determinar_posicion_norte_sur(y1, y2)
        eje_x  = self.__determinar_posicion_este_oeste(x1, x2)
        resultado = (eje_y * 10) + eje_x
        return self.__determinar_orientacion(resultado, especial, eje_x, eje_y), (especial*100) + resultado
        
    def __determinar_orientacion(self, resultado, especial, eje_x, eje_y):
        if resultado in (17, 13, 10):
            orientacion = ['abajo', 'arriba']
        elif resultado in (57,53,50):
            orientacion = ['arriba', 'abajo']
        if especial == 1 :
            if eje_x == 7:
                orientacion = ['derecha', 'izquierda']
            elif eje_x == 3:
                orientacion = ['izquierda', 'derecha']
        elif especial == 2:
            if eje_x == 7:
                orientacion[1] = 'izquierda'
            elif eje_x == 3:
                orientacion[1] = 'derecha'
        return orientacion
            
    def __determinar_posicion_especial(self, y1, y2, ancho_max_y, ancho_min_y):
        if y2 >= (y1 - ancho_min_y) and y2 <=(y1 + ancho_min_y):
            return 1
        elif y2 >= (y1 - ancho_max_y) and y2 <=(y1 + ancho_max_y):
            return 2
        else:
            return 0

    def __determinar_posicion_este_oeste(self, x1, x2):
        if x1 < x2:
            return 7
        else:
            return 3
        
    def __determinar_posicion_norte_sur(self, y1, y2):
        if y1 < y2:
            return 1
        else:
            return 5     
        
    def __calcular_curvas(self, resultado, coordenadas):
        dif_x = (coordenadas[0][0] - coordenadas[1][0]) / 2
        dif_y = (coordenadas[0][1] - coordenadas[1][1]) / 2
        if resultado in (17,13):
            curva1 = coordenadas[0][0], coordenadas[0][1] - dif_y
            curva2 = coordenadas[1][0], coordenadas[1][1] + dif_y
        elif resultado in (57,53):
            curva1 = coordenadas[0][0], coordenadas[0][1] - dif_y
            curva2 = coordenadas[1][0], coordenadas[1][1] + dif_y
        elif resultado in (117, 113, 157, 153):
            curva1 = coordenadas[0][0] - dif_x, coordenadas[0][1]
            curva2 = coordenadas[1][0] + dif_x, coordenadas[1][1]
        elif resultado in (217, 213, 257, 253):
            curva1 = coordenadas[0][0] , coordenadas[0][1] - dif_y*2
            curva2 = coordenadas[1][0] + dif_x * 2, coordenadas[1][1]        
        
        else:
            curva1 = coordenadas[0]
            curva2 = coordenadas[1]            
              
        return curva1, curva2
        
        """Se separaran la orientacion espacial de un objeto en
            1: norte
            2: noreste
            3: este
            4: sureste
            5: sur
            6: suroeste
            7: oeste
            8: noroeste
            """
            
    def dibujar(self, dc):
        dc.SetPen(wx.Pen("GREEN", 3)) 
        #print (self.lista_puntos)       
        for punto in self.lista_puntos: 
            #print (punto[0], punto[1])    
            dc.DrawLine(punto[0], punto[1])
        #dc.DrawLine(self.lista_puntos[0], self.lista_puntos[1]) #temporal usar forma anterior
          
    
        
    