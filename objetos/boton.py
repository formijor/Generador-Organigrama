'''
Created on 29 sep. 2018

@author: Jorge
'''
import wx

class Boton(wx.Button):
    '''Objeto del tipo boton'''
    def __init__(self, parent, label, posX, posY):
        wx.Button.__init__(self, parent= parent, id = -1, label= label, pos=(posX, posY), size= (120, 40))
        self.__crear_puertos()
        self.__conexiones_puertos = {}
     
    def __crear_puertos(self):
        size = self.GetSize()
        self.__arriba = size[0] / 2
        self.__abajo = size[0] / 2
        self.__izquierda = size[1] / 2
        self.__derecha = size[1] / 2
    
    def __get_puertos(self):
        return {'arriba' : self.__arriba, 'abajo': self.__abajo,
                'izquierda': self.__izquierda, 'derecha': self.__derecha}
        
    def __parientes(self):
        pass
    
    def __conexiones_puertos_init(self):
        self.__conexiones_puertos = {'arriba': [], 'abajo': [], 'izquierda': [], 'abajo': []}
    
    def set_conexiones_puertos(self, puerto, objeto_id):
        self.__conexiones_puertos(puerto).values().append[objeto_id]
    
    def get_conexiones_puertos(self):
        self.__conexiones_puertos
            
    def get_coordenadas_puertos(self, relativo):        
        puertos = self.__get_puertos()
        if relativo:
            pos = self.GetPosition()
            arriba = (pos[0] + puertos.get('arriba'), pos[1])
            abajo = (pos[0] + puertos.get('abajo'), pos[1] + self.GetSize()[1])
            izquierda = (pos[0], pos[1] + puertos.get('izquierda'))
            derecha = (pos[0]) + self.GetSize()[0], pos[1] + puertos.get('derecha')
            return {'arriba' : arriba, 'abajo': abajo,
                    'izquierda': izquierda, 'derecha': derecha}
        elif not relativo:
            return puertos
    
    def SetPosition(self, *args, **kwargs):
        wx.Button.SetPosition(self, *args, **kwargs)
        
        
           
        
"-------------------------------------------------------------------------"
class VentanaDibujo(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self,parent)
        self.panel = wx.Panel(self)
        self.boton = Boton(self.panel, 'Hola', 100, 100)
        self.boton.Bind(wx.EVT_BUTTON, self.SetPositionb)  
        self.prueba()      
        self.Show()

    def SetPositionb(self, e):
        punto= (200, 200)
        self.boton.SetPosition(punto)
        self.prueba()
        
    def prueba(self):
        print (self.boton.get_coordenadas_puertos(True))

app = wx.App()
frame = VentanaDibujo(None)
#frame.Show(1)
app.MainLoop()        