'''
Created on 27 ene. 2019

@author: formi
'''
import objetoModulo
import wx


class Menu(objetoModulo.Objeto):
    def __init__(self, parent, id_objeto, nombre, orientacion, min_size):
        objetoModulo.Objeto.__init__(self, id_objeto, nombre)
        self.parent = parent
        self.pos = []
        self.estado = True
        self.set_orientacion(orientacion)
        self.set_tamanio()
        self.set_min_size(min_size)
        #self.calcular_coordenadas
    
    def set_orientacion(self, orientacion):
        self.orientacion = orientacion
    
    def get_orientacion(self):
        return self.orientacion
    
    def set_min_size(self, min_size):
        self.min_size = min_size
     
    def set_posicion(self, pos):
        self.pos = pos
    
    def is_mouse_focus(self, coordenadas):
        resultado = True
        x1 = coordenadas[0] - self.tamanio[0]
        x2 = self.min_size[0] + self.tamanio[0] - coordenadas[0]
        y1 = coordenadas[1] - self.tamanio[1]
        y2 = self.min_size[1] - coordenadas[1]
        print ('focus', x1,x2,y1,y2)
        print ('tamanio', self.tamanio)
        for numero in [x1, x2, y1, y2]:
            if numero < 0:
                resultado = False
                break
        return resultado
        
    def set_tamanio(self):
        x, y = self.parent.GetSize()
        if self.orientacion == 'Vertical':
            self.tamanio = ([0,0,120,y])
        else:
            self.tamanio = ([0,0,x,70])
        
    def get_tamanio(self):
        return self.tamanio
    
    def calcular_coordenadas_2(self): #Separar menu en otro objeto con este comportamiento
        x,y = self.parent.GetSize()
        inicio = list(self.tamanio[0:2])
        if self.orientacion == 'Vertical':            
            fin = [self.tamanio[2], y]            
        else:
            fin = [x, self.tamanio[3]]
        self.tamanio = (inicio + fin )
    
    def calcular_coordenadas(self):
        x, y = self.parent.GetSize()
        if self.orientacion == 'Vertical':
            center_y = y / 2
            #inicio = self.min
        else:
            center_x = x / 2
            inicio = ((center_x - (self.min_size[0] / 2)), 0)
            fin = (self.min_size[0], self.min_size[1])
        self.tamanio = (inicio + fin)  
    
    def mostrar(self):
        self.estado = True
    
    def ocultar(self):
        self.estado = False
        #self.tamanio = (self.min_size[0] /2)
    
    def dibujar(self, dc):
        self.calcular_coordenadas()
        if self.estado == True:
            #self.tamanio = (self.tamanio[0] * -1, 0, self.tamanio[2] * -1, self.tamanio[3] * -1)
            dc.SetBrush(wx.Brush((253, 86, 51), wx.SOLID))
     
            dc.DrawRectangle(self.tamanio)
            dc.SetPen(wx.Pen((150, 50, 20), 1))
            #dc.DrawLine(self.parent.GetSize()[0]/2,0,self.parent.GetSize()[0]/2,self.parent.GetSize()[1])

        
        
"---------------------------------------------------------------------------------------"
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
        self.menu = Menu(self.panel, 1, 'Menu')
       
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