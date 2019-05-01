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
import cursor


class Tablero(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self,parent)
        self.SetBackgroundColour((50, 50, 50))
        self.SetMinSize((1500, 900))
        self.panel = wx.Panel(self)
        self.panel.SetSize(0, 0, 1024, 500)
        self.panel.SetBackgroundColour((150, 50, 50))
        #self.panel_menu = wx.Panel(self)
        self.Show()
        self.panel.SetDoubleBuffered(True)
        self.refrescado = False        
        self.mdc = None
        self.conectando = False
        self.crear_union_manager()
        self.crear_cursor()
        self.crear_menu()
        #---------------------------------Esto deberia ir en otra clase. Solo Prueba ahora
        self.crear_fondo()
        self.crear_objeto()
        self.crear_conexion(self.boton1,self.boton2)
        #--------------------------------------------------------------
        self.panel.Bind(wx.EVT_ERASE_BACKGROUND, self.__nada)
        self.panel.Bind(wx.EVT_PAINT, self.on_paint)
        self.panel.Bind(wx.EVT_SIZE, self.on_size)
        self.panel.Bind(wx.EVT_MOUSE_EVENTS, self.determinar_posicion)
    
    def crear_cursor(self):
        self.cursor = cursor.Puntero(self.panel, self, 999)
        
    def crear_fondo(self):
        self.fondo = FondoModulo.Cuadricula(self.panel)
    
    def crear_menu(self):
        self.menu = menuLateral.MenuLateral(self.panel, self, 1, 'Menu', 'Horizontal', (120, 250))
    
    def agregar_objeto(self, objeto):
        objeto.SetPosition((500, 500))
        objeto.Show()        
    
    def crear_objeto(self):
        self.boton1 = boton.Boton(self.panel, self, 'Login', 400, 400, 2, True, True)
        self.boton2 = boton.Boton(self.panel, self, 'Usuario', 250, 250, 3, True, True)
    
    def determinar_posicion(self, event):
        event.Skip()
        self.cursor.SetPosition(event.GetPosition())
        focus = self.menu.is_mouse_focus(event.GetPosition())
        if focus:
            #print ('Menu en Foco')
            self.panel.SetFocus()
            self.menu.mostrar()
            self.on_size(None)
        else:
            self.menu.ocultar()
            self.on_size(None)
            
    def is_click(self, objeto):
        if self.conectando:
            objeto1, objeto2 = self.uniones.get_union_objetos('cursor')
            self.crear_conexion(objeto1, objeto)
            self.eliminar_conexion_cursor()
          
    def crear_union_manager(self):
        self.uniones = unionesModulo.Uniones()
    
    def eliminar_conexion_cursor(self):
        self.uniones.eliminar_union('cursor') # id
        self.conectando = False
    
    def crear_conexion_cursor(self, objeto):
        self.conectando = True
        self.uniones.crear_union(self.panel, 'cursor', objeto, self.cursor)
    
    def crear_conexion(self, objeto1, objeto2):
        #union1 = unionesModulo.Union(self.panel, 'Libre', objeto1, objeto2)
        self.uniones.crear_union(self.panel, 'nodo', objeto1, objeto2)
        #union2 = unionesModulo.Union(self.panel, 'Libre', objeto2, objeto3)
        #self.uniones.crear_union(union2)
        #union3 = unionesModulo.Union(self.panel, 'Libre', objeto2, self.boton4)
        #self.uniones.crear_union(union3) 

    def __nada(self, event):
        pass
    
    def reposicionar_cursor(self, pos):
        self.WarpPointer(pos)
     
    def on_size(self, event):
        # re-create memory dc to fill window
        w, h = self.panel.GetClientSize()
        #w, h = self.GetSize()
        self.panel.SetSize(0, 0, w, h)
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