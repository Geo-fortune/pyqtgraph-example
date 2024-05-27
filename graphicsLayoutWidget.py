
import pyqtgraph as pg
import numpy as np
import pyqtgraph.examples
 

# image show 
# frame-objects show 
# plot object property show 

# pyqtgraph.examples.run()

class MyGraphicsLayoutWidget(pg.GraphicsLayoutWidget):

    def __init__(self, parent=None, show=False, size=None, title=None, **kargs):
        super().__init__(parent, show, size, title, **kargs)

    
