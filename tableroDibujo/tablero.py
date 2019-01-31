'''
Created on 30 sep. 2018

@author: Jorge
'''
import time

import wx
import FondoModulo
import boton
import unionesModulo
import Menu


class Tablero(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self,parent)
        self.SetBackgroundColour((50, 50, 50))
        self.SetMinSize((800, 500))
        self.panel = wx.Panel(self)
        self.panel.SetSize(0, 0, 1024, 500,wx.EXPAND | wx.ALL)
        self.panel.SetBackgroundColour((50, 50, 50))
        self.Show()
        self.panel.SetDoubleBuffered(True)
        self.refrescado = False
        
        self.mdc = None
        self.crear_union_manager()
        #---------------------------------Esto deberia ir en otra clase. Solo Prueba ahora
        self.crear_fondo()
        self.crear_objeto()
        self.crear_conexion(self.boton1,self.boton2, self.boton3)
        #--------------------------------------------------------------
        self.panel.Bind(wx.EVT_ERASE_BACKGROUND, self.__nada)
        self.panel.Bind(wx.EVT_PAINT, self.on_paint)
        self.panel.Bind(wx.EVT_SIZE, self.on_size)
        self.panel.Bind(wx.EVT_MOUSE_EVENTS, self.determinar_posicion)

        
    def crear_fondo(self):
        self.fondo = FondoModulo.Cuadricula(self.panel)
    
    def crear_objeto(self):
        self.menu = Menu.Menu(self.panel, 1, 'Menu', 'Horizontal', (600, 60))
        self.boton1 = boton.Boton(self.panel, 'Login', 400, 400, 2, True)
        self.boton2 = boton.Boton(self.panel, 'Usuario', 250, 250, 3, True)
        self.boton3 = boton.Boton(self.panel, 'Rol1', 400, 250, 4, True)
        self.boton4 = boton.Boton(self.panel, 'Rol2', 560, 300, 5, True)
    
    def determinar_posicion(self, event):
        event.Skip()
        focus = self.menu.is_mouse_focus(event.GetPosition())
        if focus:
            print ('Menu en Foco')
            self.menu.mostrar()
            self.on_size(None)
        else:
            self.menu.ocultar()
            self.on_size(None)
        
    def crear_union_manager(self):
        self.uniones = unionesModulo.Uniones()
        
    def crear_conexion(self, objeto1, objeto2, objeto3):
        conexion = unionesModulo.Conexion('Libre', self.panel, objeto1, objeto2)
        self.uniones.crear_union(conexion)
        conexion = unionesModulo.Conexion('Libre', self.panel, objeto2, objeto3)
        self.uniones.crear_union(conexion)
        conexion = unionesModulo.Conexion('Libre', self.panel, objeto2, self.boton4)
        self.uniones.crear_union(conexion) 
            
    
    def __nada(self, event):
        pass
     
    def on_size(self, event):
        # re-create memory dc to fill window
        w, h = self.panel.GetClientSize()
        self.mdc = wx.MemoryDC(wx.Bitmap(w, h))
        self.redraw() 
       
    def redraw(self):
        # do the actual drawing on the memory dc here
        self.refrescado = True
        dc = self.mdc
        dc.SetBackground(wx.Brush((50, 50, 50)))
        dc.Clear()
        self.fondo.dibujar(dc)        
        self.uniones.actualizar_uniones(dc)
        self.menu.dibujar(dc)
        self.panel.Refresh()
        
    def on_paint(self, event):
        # just blit the memory dc
        dc = wx.BufferedPaintDC(self.panel)
        if not self.mdc:
            return
        w, h = self.mdc.GetSize()
        if self.refrescado == False:
            self.redraw()
        else: 
            self.refrescado = False 
        time.sleep(0.006)  
        dc.Blit(0, 0, w, h, self.mdc, 0, 0)
        
        
"""app = wx.App()
frame = Tablero(None)
frame.Show()
app.MainLoop()"""