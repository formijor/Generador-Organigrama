'''
Created on 28 abr. 2019

@author: jor_l
'''
import wx
import tablero2
import Menu

class Principal(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent)
        self.SetBackgroundColour((250, 250, 50))
        self.SetMinSize((1500, 900))
        self.Show()
        #self.crear_sizer()        
        #self.crear_menu()
        self.crear_tablero()
        #self.Bind(wx.EVT_ERASE_BACKGROUND, self.__nada)
        #self.Bind(wx.EVT_PAINT, self.on_paint)
        #self.Bind(wx.EVT_SIZE, self.on_size)
        #self.Bind(wx.EVT_MOUSE_EVENTS, self.on_size)

    def __nada(self, event):
        pass
    
    def on_paint(self, event):
        self.menu_panel.on_paint(None)
        self.tablero.on_paint(None)
    
    def on_size(self, event):
        print ('pintando')
        #self.menu_panel.on_size(None)
        self.tablero.on_size(None)
    
    def agregar_objeto_sizer(self, objeto):
        self.sizer.Add(objeto)

    def crear_sizer(self):
        self.sizer = wx.BoxSizer( wx.HORIZONTAL)
        self.SetSizer(self.sizer)

    def crear_menu(self):
        self.menu_panel = Menu.Menu_panel(self,(120, 500), (0,0))
        #self.agregar_objeto_sizer(self.menu_panel)

    def crear_tablero(self):
        self.tablero = tablero2.Tablero(self, (150, 0))
        #self.agregar_objeto_sizer(self.tablero)
