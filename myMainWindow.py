
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton
import sys
# from pyqtgraph import plot
import pyqtgraph as pg
import numpy as np

from graphicsLayoutWidget import MyGraphicsLayoutWidget

class myMainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("XPeng Analysis")
        self.graphicLayoutWidget = pg.GraphicsLayoutWidget(show=True)

        p = self.graphicLayoutWidget.addPlot(title= "MultiLine")
        
        p.plot(np.random.normal(size=100), pen=(255,0,0), name="红色")
# 显示第二波形
        p.plot(np.random.normal(size=110)+5, pen=(0,255,0), name="绿色")
# 显示第三波形
        p.plot(np.random.normal(size=120)+10, pen=(0,0,255), name="蓝色")

        # p.setLogMode(x=True, y=False)
        # self.plot_widget = pg.PlotWidget()
        # self.graphicLayoutWidget.addItem(self.plot_widget)
        
        self.setCentralWidget(self.graphicLayoutWidget)

    def add_plots(self):
        pass

    def add_images(self):
        pass





app = QApplication(sys.argv)
window = myMainWindow()
window.show()
app.exec()