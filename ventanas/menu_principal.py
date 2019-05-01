'''
Created on 29 ene. 2019

@author: formi
'''

import wx
import tablero
import tablero2
import boton
import VentanaPrincipal

class MenuPrincipal(wx.Frame):
    def __init__(self, parent, size, min_size, max_size, color):
        wx.Frame.__init__(self, parent)
        self.parent = parent
        self.set_minimum_size(min_size)
        self.set_maximum_size(max_size)
        self.create_panel()
        self.set_background_color(color)
        self.set_size(size)
        self.CenterOnScreen()
        self.create_buttons()
        #self.open_tablero()
    
    def create_panel(self):
        self.panel = wx.Panel(self)
        
    def set_size(self, size):
        self.size = size
        self.SetSize(0,0,size[0], size[1], wx.EXPAND | wx.ALL)
    
    def set_minimum_size(self, min_size):
        self.SetMinSize(min_size)
        
    def set_maximum_size(self, max_size):
        self.SetMaxSize(max_size)
        
    def set_background_color(self, color):
        self.panel.SetBackgroundColour(color) 
        
    def create_buttons(self):
        #self.boton1 = wx.Button(self.panel, -1, 'Login', pos =(50,50))
        self.botonTablero = boton.Boton(self.panel, self, 'Tablero', -1, 50, 3, False, False)
        self.botonTablero.CentreOnParent(wx.HORIZONTAL)
        self.botonTablero.Bind(wx.EVT_BUTTON, self.open_tablero)
        
        self.botonSalir = self.botonTablero = boton.Boton(self.panel, self, 'Salir', -1, 120, 3, False, False)
        self.botonTablero.CentreOnParent(wx.HORIZONTAL)
        self.botonTablero.Bind(wx.EVT_BUTTON, self.close)
        
    def open_tablero(self, event):
        self.panel.Freeze()      
        tablero.Tablero(self.panel)
        #self.ventana_principal = VentanaPrincipal.Principal(self.panel)
        self.Hide()
        
    def close(self, event):
        self.Destroy()
        self.Close()
