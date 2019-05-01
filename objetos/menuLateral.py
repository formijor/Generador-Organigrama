'''
Created on 28 abr. 2019

@author: jor_l
'''

import wx
import objetoModulo
import boton

class MenuLateral(objetoModulo.Objeto):
    def __init__(self, parent, frame, id_objeto, nombre, orientacion, min_size):
        objetoModulo.Objeto.__init__(self, id_objeto, nombre)
        self.parent = parent
        self.frame = frame
        self.pos = []
        self.estado = True
        self.set_orientacion(orientacion)
        self.set_min_size(min_size)
        self.set_tamanio()
        self.lista_objetos = []
        self.agregar_objeto_menu(boton.Boton(self.parent, self, 'Agregar Nodo', 400, 400, 2, False, False))
    
    def agregar_objeto_menu(self, objeto):
        objeto.Bind(wx.EVT_BUTTON, self.agregar_objeto_tablero )
        self.lista_objetos.append(objeto)
        self.calcular_separacion()

    def agregar_objeto_tablero(self, event):
        boton1 = boton.Boton(self.parent, self.frame, 'Login', 400, 400, 4, True, True)
        #boton1.Hide()
        self.frame.agregar_objeto(boton1)

    def calcular_separacion(self):
        self.separacion = 20
        x = 0
        y = self.separacion
        for objeto in self.lista_objetos:
            objeto.SetPosition((x, y))
            y = y + objeto.get_size()[1] + self.separacion

    def set_orientacion(self, orientacion):
        self.orientacion = orientacion

    def get_orientacion(self):
        return self.orientacion

    def set_min_size(self, min_size):
        self.min_size = min_size

    def set_posicion(self, pos):
        self.pos = pos

    def is_mouse_focus(self, coordenadas):
        return True
  
    def set_tamanio(self):
        x, y = self.parent.GetSize()
        self.tamanio = ([0,0,self.min_size[0], y])

    def get_tamanio(self):
        return self.tamanio

    def calcular_coordenadas(self):
        x, y = self.parent.GetSize()
        self.tamanio = (0, 0, self.min_size[0], y ) 
    
    def mostrar(self):
        self.estado = True
    
    def ocultar(self):
        self.estado = False
        #self.tamanio = (self.min_size[0] /2)
    
    def dibujar(self, dc):
        self.calcular_coordenadas()
        if self.estado == True:
            #self.tamanio = (self.tamanio[0] * -1, 0, self.tamanio[2] * -1, self.tamanio[3] * -1)
            dc.SetBrush(wx.Brush((210, 110, 60), wx.SOLID))
            dc.SetPen(wx.Pen((210, 110, 60), 1))
            dc.DrawRoundedRectangle(self.tamanio, 5)
            #dc.DrawRoundedRectangle(250,50, 300, 70, 28)
            #dc.DrawLine(self.parent.GetSize()[0]/2,0,self.parent.GetSize()[0]/2,self.parent.GetSize()[1])