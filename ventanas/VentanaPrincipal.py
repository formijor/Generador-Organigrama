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
        self.SetBackgroundColour((50, 50, 50))
        self.SetMinSize((1500, 900))
        self.Show()
        self.crear_menu()
        self.crear_tablero()
        
    def crear_menu(self):
        self.menu_tablero = Menu.Menu_panel(self,(120, 300), (0,0))
    
    def crear_tablero(self):
        self.tablero = tablero2.Tablero(self, (120, 0))