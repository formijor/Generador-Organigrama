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
import menuLateral


class Tablero(wx.Panel):
    def __init__(self, parent, pos):
        wx.Panel.__init__(self, parent)
        self.SetPosition(pos)
        self.SetSize(0, 0, 1024, 500)
        self.SetBackgroundColour((50, 50, 50))
        #self.panel_menu = wx.Panel(self)
        self.Show()
        self.SetDoubleBuffered(True)
        self.refrescado = False        
        self.mdc = None
        self.crear_union_manager()
        #---------------------------------Esto deberia ir en otra clase. Solo Prueba ahora
        self.crear_fondo()
        self.crear_objeto()
        self.crear_conexion(self.boton1,self.boton2, self.boton3)
        #--------------------------------------------------------------
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.__nada)
        self.Bind(wx.EVT_PAINT, self.on_paint)
        self.Bind(wx.EVT_SIZE, self.on_size)
        self.Bind(wx.EVT_MOUSE_EVENTS, self.on_size)
        
    def crear_fondo(self):
        self.fondo = FondoModulo.Cuadricula(self)

    
    def crear_objeto(self):
        #self.menu = menuLateral.MenuLateral(self, 1, 'Menu', 'Horizontal', (120, 250))
        self.boton1 = boton.Boton(self, 'Login', 400, 400, 2, True)
        self.boton2 = boton.Boton(self, 'Usuario', 250, 250, 3, True)
        self.boton3 = boton.Boton(self, 'Rol1', 400, 250, 4, True)
        #self.boton4 = boton.Boton(self.panel, 'Rol2', 560, 300, 5, True)
    
    def determinar_posicion(self, event):
        event.Skip()
        focus = self.menu.is_mouse_focus(event.GetPosition())
        if focus:
            #print ('Menu en Foco')

            #self.menu.mostrar()
            self.on_size(None)
        else:
            #self.menu.ocultar()
            self.on_size(None)
        
    def crear_union_manager(self):
        self.uniones = unionesModulo.Uniones()
        
    def crear_conexion(self, objeto1, objeto2, objeto3):
        union1 = unionesModulo.Union(self, 'Libre', objeto1, objeto2)
        self.uniones.crear_union(union1)
        #union2 = unionesModulo.Union(self.panel, 'Libre', objeto2, objeto3)
        #self.uniones.crear_union(union2)
        #union3 = unionesModulo.Union(self.panel, 'Libre', objeto2, self.boton4)
        #self.uniones.crear_union(union3) 

    def __nada(self, event):
        pass
     
    def on_size(self, event):
        # re-create memory dc to fill window
        w, h = self.GetClientSize()
        #w, h = self.GetSize()
        self.SetSize(0, 0, w, h)
        #self.menu.SetSize(0,0,120,h)
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
        #self.menu.dibujar(dc)
        self.Refresh()
        
    def on_paint(self, event):
        # just blit the memory dc
        dc = wx.BufferedPaintDC(self)
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