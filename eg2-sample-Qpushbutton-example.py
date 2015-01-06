from PyQt4 import QtGui
from PyQt4 import QtCore
import sys

class sampleWindow(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)

        self.resize(500,600)
        #set the size of window
        self.helloBuitton = QtGui.QPushButton("Hello",self)
        self.helloBuitton.connect(self,QtCore.SIGNAL("clicked()"),self.printhello)
        self.show()
    def printhello(self,event):
        print "hello world:: button pressed"

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = sampleWindow()
    sys.exit(app.exec_())
