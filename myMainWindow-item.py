
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
        
        # plot data item

        # plot item

        # colot bar item

        # P colot mesh Item

        # GraphItem

        # ViewBox

        # LinearRegionItem

        # Infinite Line

       # multiplot item
        layout_item = pg.MultiPlotItem()
        self.graphicLayoutWidget.addItem(layout_item,0, 0, 1, 1)


        # plot curve item

        # scatter plot item

        # isoCureItem

        # AxisItem

        # TextItem

        # ErrorBarItem

        # ArrowItem

        # LabelItem

        # LegendItem

        # GradientEditorItem

        # HistogramLUTItem
        
        # ButtonItem

        # GraphicsItem

        # UIGraphicsItem

        # DeteAxisItem

        # TargetItem




        self.setCentralWidget(self.graphicLayoutWidget)

    def add_plots(self):
        pass

    def add_images(self):
        pass





app = QApplication(sys.argv)
window = myMainWindow()
window.show()
app.exec()