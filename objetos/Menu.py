'''
Created on 27 ene. 2019

@author: formi
'''
import objetoModulo
import wx


class MenuPrincipal(objetoModulo.Objeto):
    def __init__(self, parent, id_objeto, nombre):
        objetoModulo.Objeto.__init__(self, id_objeto, nombre)
        self.parent = parent
        self.pos = []
        self.set_tamanio([0,0,200,0])
        self.calcular_coordenadas
        
    def set_posicion(self, pos):
        self.pos = pos
        
    def set_tamanio(self, coordenadas):
        self.tamanio = (coordenadas)
    
    def calcular_coordenadas(self):
        x,y = self.parent.GetSize()
        inicio = list(self.tamanio[0:2])
        fin = [self.tamanio[2], y]
        self.tamanio = (inicio + fin )

    def dibujar(self, dc):
        self.calcular_coordenadas()
        dc.SetPen(wx.Pen("GREY", 5))
        dc.DrawRectangle(self.tamanio)
        
        

class VentanaDibujo(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent)
        self.panel = wx.Panel(self) 
        self.prueba()
        self.SetDoubleBuffered(True)
        self.panel.Bind(wx.EVT_ERASE_BACKGROUND, self.__nada)
        self.panel.Bind(wx.EVT_PAINT, self.on_paint)
        self.panel.Bind(wx.EVT_SIZE, self.on_size)     
        self.Show()
        
    def prueba(self):
        self.menu = MenuPrincipal(self.panel, 1, 'Menu')
       
    def on_size(self, event):
        # re-create memory dc to fill window
        w, h = self.panel.GetClientSize()
        self.mdc = wx.MemoryDC(wx.Bitmap(w, h))
        self.redraw() 
    
    def __nada(self, event):
        pass
    
    def redraw(self):
        # do the actual drawing on the memory dc here
        self.refrescado = True
        dc = self.mdc
        w, h = dc.GetSize()
        dc.SetBackground(wx.Brush((50, 50, 50)))
        dc.Clear()
        self.menu.dibujar(dc)
        #self.fondo.dibujar(dc)
        #self.uniones.actualizar_uniones(dc)
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
        dc.Blit(0, 0, w, h, self.mdc, 0, 0)
    

"""app = wx.App()
frame = VentanaDibujo(None)
#frame.Show(1)
app.MainLoop() """       