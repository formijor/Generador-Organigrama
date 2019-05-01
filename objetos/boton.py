'''
Created on 29 sep. 2018

@author: Jorge
'''

import wx
import objetoModulo

class Boton(wx.Button, objetoModulo.Objeto):
    '''Objeto del tipo boton'''
    def __init__(self, parent, frame, nombre, posX, posY, id_objeto, drag, conectar):
        self.parent = parent
        self.frame = frame
        wx.Button.__init__(self, parent= self.parent, id = -1, label= nombre, pos=(posX, posY), size= (120, 40))
        objetoModulo.Objeto.__init__(self, id_objeto, nombre)
        self.entro = False
        self.size = (120, 40)
        self.__crear_puertos()
        self.default_bind()
        self.set_draggable(drag)
        self.set_conectable(conectar)
        self.posicion_anterior = self.GetPosition()
        #self.orientacion = Orientacion(self.GetPosition())

    def default_bind(self):
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.onEraseBackground)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
    
    def set_draggable(self, drag):
        if drag:            
            self.Bind(wx.EVT_LEFT_DOWN, self.button_down)
            self.Bind(wx.EVT_LEFT_UP, self.button_up)
            self.Bind(wx.EVT_MOUSE_EVENTS, self.mover)
            self.parent.Bind(wx.EVT_MOUSE_EVENTS, self.mover)
        else:
            try:
                self.Unbind(wx.EVT_LEFT_DOWN, self.button_down)
                self.Unbind(wx.EVT_LEFT_UP, self.button_up)
                self.Unbind(wx.EVT_MOUSE_EVENTS, self.mover)
                self.parent.Unbind(wx.EVT_MOUSE_EVENTS, self.mover)
            except:
                print ('No seteado')
    
    def set_conectable(self, conectar):
        if conectar:
            self.Bind(wx.EVT_LEFT_DCLICK, self.on_doble_click)
    
    def on_doble_click(self, event):
        print ('Doble Click')
        self.frame.crear_conexion_cursor(self)
    
    def onEraseBackground(self, event):
        pass
    
    def OnPaint(self, event):
        pass 
    
    def __parientes(self):
        pass
        
    def get_size(self):
        return self.size
    
    def get_size_center(self):
        return (self.size[0] / 2, self.size[1] / 2)
    
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
    
    def Bind(self, *args, **kwargs):
        wx.Button.Bind(self, *args, **kwargs)
        
    def mover(self, e):
        e.Skip()  
        if self.entro:
            self.Raise()
            pos = self.GetPosition() 
            coordenadas = self.offset_coordenates(self.parent.ScreenToClient(wx.GetMousePosition()),self.calculate_coordenates())
            #self.orientacion_movimiento(0, 0)
            #pos_anterior = e.GetPosition()
            #self.SetPosition(self.parent.ScreenToClient(wx.GetMousePosition()))
            tup = (coordenadas[0] - 60 , coordenadas[1] - 20)
            diferencia =  ((tup[0] - pos[0]) / 5, (tup[1] - pos[1]) / 5)
            tup = (tup[0] - diferencia[0], tup[1] - diferencia[1])
            tup = self.limitar_movimiento(tup)
            #tup = self.limitador_velocidad_mouse(tup)
            self.SetPosition(tup)
            #self.limitador_velocidad_mouse(tup)
            
    "----------------------------------------------------Refactorizar"
    def limitar_movimiento(self, pos):
        center_x, center_y = self.get_size_center()
        panel_x, panel_y = self.parent.GetSize()
        if pos[0] < 121:
            pos = 121, pos[1]
            self.reposicionar_cursor(pos)
        elif pos[0] + 120 > self.__get_limite_pos(2):
            pos= 1484 - 120, pos[1]
            self.reposicionar_cursor(pos)
        elif pos[1] < 0:
            pos = pos[0], 0
            self.reposicionar_cursor(pos)
        elif pos[1] + (center_y * 2) > self.__get_limite_pos(3):
            pos = pos[0], panel_y - (center_y * 2)
            self.reposicionar_cursor(pos)
        return pos

    def __get_limite_pos(self, limite):
        "1 = y(0), 2 = x(>0), 3 = y(>0), 4 = x(0)"
        if limite == 2:
            return self.parent.GetSize()[0]
        elif limite == 3:
            return self.parent.GetSize()[1]
        else:
            return 0
    "---------------------------------------------------------------"

    def reposicionar_cursor(self, pos):
        centro_xy = self.get_size_center()
        self.parent.WarpPointer(pos[0] + centro_xy[0], pos[1] + centro_xy[1])
        
    def calculate_coordenates(self):
        panel_size = self.parent.GetSize()
        centro = (panel_size[0] / 2, panel_size[1] / 2)
        return centro
        
    def offset_coordenates(self, coordenadas, centro):
        #coordenadas = coordenadas * (1, 1)
        #print ('Coordenadas',coordenadas)
        #coordenadas2 = (centro - self.GetPosition()) + coordenadas 
        #print ('coor2', coordenadas2)
        return coordenadas[0] , coordenadas[1]
 
    def button_down(self, event):   
        self.entro = True
        self.mouse_pos = event.GetPosition()
        self.frame.is_click(self)
        self.Refresh()

    def button_up(self, event): 
        self.entro = False
        self.Refresh()

    def orientacion_movimiento(self, pos_anterior, pos_posterior): 
        mouse = wx.GetMouseState()
        #print (self.parent.ScreenToClient(wx.GetMousePosition()))





"-------------------------------TEST------------------------------------------"
class VentanaDibujo(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self,parent)
        self.panel = wx.Panel(self)
        self.boton = Boton(self.panel, 'Hola', 100, 100, 1)
        self.boton2 = Boton(self.panel, 'Chau', 100, 100, 2)
        self.boton.Bind(wx.EVT_BUTTON, self.SetPositionb) 
        #self.test_conexiones() 
        self.prueba()      
        self.Show()
    
    def test_conexiones(self):  
        print (self.boton.get_conexiones_puertos())    
        self.boton.set_conexion_puerto('abajo', 1)
        print (self.boton.get_conexiones_puertos())
        self.boton.delete_conexion_puerto('abajo', 1)
        print (self.boton.get_conexiones_puertos())
    
    def SetPositionb(self, e):
        punto= (200, 200)
        self.boton.SetPosition(punto)
        self.prueba()
        
    def prueba(self):
        print (self.boton.get_coordenadas_puertos(True))

"""app = wx.App()
frame = VentanaDibujo(None)
#frame.Show(1)
app.MainLoop() """       