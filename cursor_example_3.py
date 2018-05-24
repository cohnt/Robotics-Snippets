#!/usr/bin/env python2

import matplotlib.pyplot as plt
import matplotlib.widgets as widgets
import numpy as np

class SnaptoCursor(object):
    def __init__(self, ax):
        self.ax = ax
        self.vl1 = ax.axvline(color='red', alpha=0.75)
        self.vl2 = ax.axvline(color='red', alpha=0.75)
        self.hl1 = ax.axhline(color='red', alpha=0.75)
        self.hl2 = ax.axhline(color='red', alpha=0.75)
        self.x = 0
        self.y = 0
    
    def mouse_move(self, event):
        if not event.inaxes: return
        x, y = event.xdata, event.ydata
        self.vl1.set_xdata(x)
        self.vl2.set_xdata(x+0.1)
        self.hl1.set_ydata(y)
        self.hl2.set_ydata(y+0.1)
        self.ax.figure.canvas.draw_idle()

t = np.arange(0.0, 1.0, 0.01)
s = np.sin(2*2*np.pi*t)
fig, ax = plt.subplots()

#cursor = Cursor(ax)
cursor = SnaptoCursor(ax)
cid =  plt.connect('motion_notify_event', cursor.mouse_move)

ax.plot(t, s,)
plt.axis([0, 1, -1, 1])
plt.show()