'''
Created on 29 sep. 2018

@author: Jorge
'''
import wx
import objetoModulo

class Boton(wx.Button, objetoModulo.Objeto):
    '''Objeto del tipo boton'''
    def __init__(self, parent, nombre, posX, posY, id_objeto):
        self.parent = parent
        wx.Button.__init__(self, parent= self.parent, id = -1, label= nombre, pos=(posX, posY), size= (120, 40))
        objetoModulo.Objeto.__init__(self, id_objeto, nombre)
        self.entro = False
        self.r = False
        self.__crear_puertos()
        self.Bind(wx.EVT_LEFT_DOWN, self.button_down)
        self.Bind(wx.EVT_LEFT_UP, self.button_up)
        self.parent.Bind(wx.EVT_MOUSE_EVENTS, self.mover)
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.onEraseBackground)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
    
    def onEraseBackground(self, event):
        pass
    
    def OnPaint(self, event):
        pass 
    
    def __parientes(self):
        pass
    
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
              
    def Bind(self, *args, **kwargs):
        wx.Button.Bind(self, *args, **kwargs)
        
    def mover(self, e):
        e.Skip()       
        if e.Dragging() and self.entro:
            self.SetPosition(e.GetPosition())
        
    def button_down(self, event):        
        self.entro = True
        self.Refresh()
        
    def button_up(self, event):  
        self.entro = False
        self.Refresh()
           
        
        
            
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