'''
Created on 30 ene. 2019

@author: formi
'''
import wx
import time

USE_BUFFERED_DC = True

class Nodo(wx.Control):
    def __init__(self, parent, id=wx.ID_ANY, label="BOTON", pos=wx.DefaultPosition,
                 size=wx.DefaultSize, style=wx.NO_BORDER, validator=wx.DefaultValidator,
                 name="Nodo"):
        wx.Control.__init__(self, parent, id, pos, size, style, validator, name)
        self.__init__variables()
        self.SetLabel(label)
        self.parent = parent
        
        #self.SetInitialSize(size)
        self.default_binds()
        self.default_configuration()
        
        
        self.Size = size
       
        #self.InheritAttributes()

    
    def __init__variables(self):
        self.__Focus = False
        self.drag = False
        self.hover_mouse = False
        
    def default_configuration(self):
        self.SetCanFocus(True)
        self.SetBackgroundColour((200,200,200))
        self.SetHoverColour((80,175,30))
        self.SetForegroundColour(wx.BLACK)
           
    def default_binds(self):
        self.Bind(wx.EVT_ENTER_WINDOW, self.OnHover)
        self.Bind(wx.EVT_LEAVE_WINDOW, self.OnHover)
        self.Bind(wx.EVT_LEFT_DOWN, self.OnMouseClick)
        self.Bind(wx.EVT_LEFT_UP, self.OnMouseUnClick)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_MOUSE_EVENTS, self.Dragging)
        self.parent.Bind(wx.EVT_MOUSE_EVENTS, self.Dragging)
        #self.Bind(wx.EVT_KILL_FOCUS, self.OnKillFocus)
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        
    def SetLabel(self, label):
        wx.Control.SetLabel(self, label)
        self.Refresh()
    
    def SetFont(self, font):
        output = wx.Control.SetFont(self, font)
        self.Refresh()
        return output
    
    def SetOwnFont(self, font):
        return wx.Control.SetOwnFont(self, font)
    
    def SetForegroundColour(self, colour):
        """ Overridden base class virtual. """
        wx.Control.SetForegroundColour(self, colour)
        self.Refresh()
    
    def SetBackgroundColour(self, colour):
        """ Overridden base class virtual. """
        self.BackgroundColour = colour
        wx.Control.SetBackgroundColour(self, colour)
        self.Refresh()
        
    def GetBackgroundColour(self):
        return wx.Control.GetBackgroundColour(self)
    
    def GetHoverColour(self):
        return list(self.HoverColour)
     
    def SetHoverColour(self, colour):
        self.HoverColour = colour
        self.Refresh()
        
    def Enable(self, enable):
        wx.Control.Enable(self, enable)
        self.Refresh()
           
    def Disable(self, disable):
        wx.Control.Enable(self, disable)
        self.Refresh()        
    
    def SetTransparent(self, alpha):
        return wx.Control.SetTransparent(self, alpha)
    
    def SplitToRGB(self, colour):
        return colour[0], colour[1], colour[2]
    
    def SplitArray(self, array):
        return list(array)
    
    def ArrayRest(self, array1, array2):
        pass
    
    def OnHover(self, event):
        self.hover_mouse = not self.hover_mouse
        backColour = self.GetBackgroundColour()
        hoverColour = self.GetHoverColour()
        if self.hover_mouse:
            self.SetBackgroundColour(hoverColour)
                        
        else:
            self.SetBackgroundColour(backColour) 
        self.HoverColour = backColour
        self.BackgroundColour = hoverColour

    def SetCanFocus(self, canFocus):
        wx.Control.SetCanFocus(self, canFocus)
      
    def AcceptsFocus(self):
        return True
    
    def HasFocus(self):
        return self._Focus
    
    def OnPaint(self, event):
        w, h = self.parent.GetClientSize()
        dc = wx.BufferedPaintDC(self)
        #dc = wx.BufferedPaintDC(self)
        self.Draw(dc)
        
    def Draw(self, dc):
        w, h = self.GetClientSize()
        #if not width or not height:
            # Nothing to do, we still don't have dimensions!
        #    return
        #backColour = self.GetBackgroundColour()
        #backBrush = wx.Brush(wx.RED, wx.SOLID)
        #dc.SetBackground(backBrush)
        dc.Clear()

        dc.SetBrush(wx.Brush(wx.GREEN, wx.SOLID))
        b = 10
        dc.SetPen(wx.Pen(wx.BLACK, b))        
        #dc.DrawRectangle(100 , 100 , 500, 70)
        #dc.DrawLine(100, 100, 200, 70)
        self.DrawText( dc)        
    
    def DrawText(self, dc):
        lengt, height = dc.GetTextExtent(self.GetLabel())
        l, h = self.GetSize()
        Ldif = abs(l - lengt) / 2
        Hdif = abs(h - height) / 2
        dc.DrawText(self.GetLabel(), Ldif, Hdif )           
    
    def OnMouseClick(self, event):
        self.drag = True
        #if not self.IsEnabled():
            # Nothing to do, we are disabled
            #return

    def OnMouseUnClick(self, event):
        self.drag = False
    
    def Dragging(self, event):
        event.Skip()
        if self.drag:
            self.Raise()
            pos = self.GetPosition() 
            coordenadas = self.parent.ScreenToClient(wx.GetMousePosition())
            #self.orientacion_movimiento(0, 0)
            #pos_anterior = e.GetPosition()
            #self.SetPosition(self.parent.ScreenToClient(wx.GetMousePosition()))
            tup = (coordenadas[0] - 60 , coordenadas[1] - 20)
            diferencia =  ((tup[0] - pos[0]) / 5, (tup[1] - pos[1]) / 5)
            tup = (tup[0] - diferencia[0], tup[1] - diferencia[1])
            self.SetPosition(tup)
    
    def OnSetFocus(self, event):
        self.__Focus = True
        self.Refresh()
        
    def OnKillFocus(self, event):
        self.__Focus = False
        self.Refresh()
    
    def OnEraseBackground(self, event):
        pass
    


class VentanaDibujo(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self,parent)
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour((175,100,50))    
        self.Show()
        self.boton = Nodo(self.panel, pos=(100, 50), size = (100, 50))
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        #self.boton = CustomCheckBox.CustomCheckBox(self, pos=(100, 50), size = (100, 50))
        #self.boton.OnPaint(None)

    def OnEraseBackground(self, event):
        pass
        
        
app = wx.App()
frame = VentanaDibujo(None)
#frame.Show(1)
app.MainLoop() 