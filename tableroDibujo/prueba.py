'''
Created on 27 ene. 2019

@author: formi
'''
import wx

class Frame(wx.Frame):
    def __init__(self):
        super(Frame, self).__init__(None, -1, 'CursorTracker')
        self.mdc = None # memory dc to draw off-screen
        self.Bind(wx.EVT_SIZE, self.on_size)
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.on_erase)
        self.Bind(wx.EVT_PAINT, self.on_paint)
        w, h = wx.GetDisplaySize()
        w, h = w * 3 / 4, h * 3 / 4
        self.SetSize((w, h))
        self.Center()
    
    def on_size(self, event):
        # re-create memory dc to fill window
        print ('SIZE')
        w, h = self.GetClientSize()
        self.mdc = wx.MemoryDC(wx.Bitmap(w, h))
        self.redraw()
    
    def on_erase(self, event):
        pass # don't do any erasing to avoid flicker
    
    def on_paint(self, event):
        # just blit the memory dc
        print ('PAINT')
        dc = wx.PaintDC(self)
        if not self.mdc:
            return
        w, h = self.mdc.GetSize()
        dc.Blit(0, 0, w, h, self.mdc, 0, 0)
       
    def redraw(self):
        # do the actual drawing on the memory dc here
        dc = self.mdc
        w, h = dc.GetSize()
        dc.Clear()
        dc.DrawLine(0, 0, w, h)
        self.Refresh()

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = Frame()
    frame.Show()
    app.MainLoop()