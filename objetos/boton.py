'''
Created on 29 sep. 2018

@author: Jorge
'''
import wx
import objetoModulo

class Boton(wx.Button, objetoModulo.Objeto):
    '''Objeto del tipo boton'''
    def __init__(self, parent, nombre, posX, posY, id_objeto):
        wx.Button.__init__(self, parent= parent, id = -1, label= nombre, pos=(posX, posY), size= (120, 40))
        objetoModulo.Objeto.__init__(self, id_objeto, nombre)
        self.conexiones_puertos_init()
        self.parent = parent
        self.Bind(wx.EVT_LEFT_DOWN, self.mouse_entro)
        self.parent.Bind(wx.EVT_MOUSE_EVENTS, self.mover)
        
        
    def __parientes(self):
        pass
    
    def conexiones_puertos_init(self):
        self.conexiones_puertos = {'arriba': [], 'abajo': [], 'izquierda': [], 'derecha': []}
              
    def Bind(self, *args, **kwargs):
        wx.Button.Bind(self, *args, **kwargs)
        
    def mover(self, e): 
        if e.Dragging() and self.entro:      
            mouse_pos = e.GetPosition()
            self.SetPosition(mouse_pos)
        
    def mouse_entro(self, e):
        if e.ButtonDown():
            self.entro = True
            self.m_pos = e.GetPosition()
        else:
            self.entro = False
        
        
        
        
        
        
         
        
        
            
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