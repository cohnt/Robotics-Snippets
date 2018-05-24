#!/usr/bin/env python2

import numpy as np
import matplotlib.pyplot as plt 

class MouseCross(object):
	def __init__(self, ax, **kwargs):
		self.ax = ax
		self.line, = self.ax.plot([0], [0], visible=False, **kwargs)
	def show_cross(self, event):
		if event.inaxes == self.ax:
			self.line.set_data([event.xdata], [event.ydata])
			self.line.set_visible(True)
		else:
			self.line.set_visible(False)
		plt.draw()

if __name__ == '__main__':
	fig, ax = plt.subplots()
	ax.plot(np.random.random(100) * 10.0)
	# note that not every "normal" matplotlib marker will work
	# math symbols work fine
	cross = MouseCross(ax, marker=r'$\bigoplus$', markersize=30, color='red',)
	fig.canvas.mpl_connect('motion_notify_event', cross.show_cross)
	plt.tight_layout()
	plt.show()