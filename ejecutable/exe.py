'''
Created on 29 ene. 2019

@author: formi
'''
import wx
import menu_principal

app = wx.App()
frame = menu_principal.MenuPrincipal(None, (300, 500),(300, 500), (300, 500), (253,253,253))
frame.Show()
app.MainLoop()