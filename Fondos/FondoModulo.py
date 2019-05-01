'''
Created on 30 sep. 2018

@author: Jorge
'''

import wx


#import tablero
class Fondo():
    def __init__(self, parent):
        self.parent = parent
        
    
class Cuadricula(Fondo):
    def __init__(self, parent):
        Fondo.__init__(self, parent)
        self.parent = parent
    
    def set_pos(self):
        pass
    
    def dibujar(self, dc):
        dc.SetPen(wx.Pen("Black", 1))
        separacion = self.parent.GetSize()[0] / (self.parent.GetSize()[0] / 32)
        #separacion = 50
        x1 = 10 #+ separacion
        y1 = 0 #+ separacion
        x2 = 10#+ separacion
        y2 = 0 #+ separacion
        ancho, alto = (self.parent.GetSize())
        cantidad_lineas_ancho = ancho / separacion
        cantidad_lineas_alto = alto / separacion
        while (cantidad_lineas_ancho + cantidad_lineas_alto) > 0:
            if cantidad_lineas_ancho > 0:
                self.dibujar_linea(x1, y1, x1, alto, dc)
                cantidad_lineas_ancho -= 1
                x1 += separacion               
            if cantidad_lineas_alto > 0:
                self.dibujar_linea(x2, y2, ancho, y2, dc)
                cantidad_lineas_alto -= 1
                y2 += separacion        
    
    def dibujar_linea(self, inicio_alto, ancho_alto, fin_alto, fin_ancho, dc):   
        imagenLinea(dc, self.parent, inicio_alto, ancho_alto, fin_alto, fin_ancho)

"---------------------------------------------------------------------------------"
  
class imagenLinea(object):
    def __init__(self, dc, panel, inicio_alto, ancho_alto, fin_alto, fin_ancho):
        #self.panel = panel
        self.dc = dc
        self.dibujar(inicio_alto, ancho_alto, fin_alto, fin_ancho)
    
    def dibujar(self, inicio_alto, ancho_alto, fin_alto, fin_ancho ):
        inicio = (inicio_alto, ancho_alto)
        fin = (fin_alto, fin_ancho)
        self.dc.DrawLine(inicio, fin)
      
