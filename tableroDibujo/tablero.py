'''
Created on 30 sep. 2018

@author: Jorge
'''
import wx
import FondoModulo
import boton
import unionesModulo


class Tablero(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self,parent)
        self.SetBackgroundColour((255, 50, 50))
        self.SetMinSize((600, 200))
        self.panel = wx.Panel(self)
        self.panel.SetSize(0, 0, 500, 500,wx.EXPAND | wx.ALL)
        self.panel.SetBackgroundColour((50, 50, 50))
        self.SetDoubleBuffered(True)
        
        self.crear_union_manager()
        #---------------------------------Esto deberia ir en otra clase. Solo Prueba ahora
        self.crear_fondo()
        self.crear_objeto()
        self.crear_conexion(self.boton1,self.boton2)
        #--------------------------------------------------------------
        
        #self.dibujar(None)
        self.panel.Bind(wx.EVT_ERASE_BACKGROUND, self.dibujar)
        #self.panel.Bind(wx.EVT_PAINT, self.dibujar)
        self.panel.Bind(wx.EVT_SIZE, self.dibujar)
        self.Show()
        
       
    def crear_fondo(self):
        self.fondo = FondoModulo.Cuadricula(self.panel)
    
    def crear_objeto(self):
        self.boton1 = boton.Boton(self.panel, 'Hola', 400, 400, 1)
        self.boton2 = boton.Boton(self.panel, 'Chau', 250, 250, 2)
        
    def crear_union_manager(self):
        self.uniones = unionesModulo.Uniones()
        
    def crear_conexion(self, objeto1, objeto2):
        conexion = unionesModulo.Conexion('Libre', objeto1, objeto2)
        self.uniones.crear_union(conexion)        
    
    def __nada(self):
        pass
    
    def dibujar(self, e):
        dc = wx.ClientDC(self.panel)
        dc.Clear()
        self.fondo.dibujar(dc)
        #self.dibujar_uniones(dc)
        self.uniones.actualizar_uniones(dc)
       
    
        
        
app = wx.App()
frame = Tablero(None)
#frame.Show(1)
app.MainLoop()