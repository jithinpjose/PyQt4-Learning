from PyQt4 import QtGui
from PyQt4 import QtCore
import sys
class MicroHope_Editor(QtGui.QMainWindow):
	
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		self.resize(800,600)
		self.text = QtGui.QTextEdit(self)
		self.setWindowTitle("MicroHOPE ")
		self.show()
		
if __name__ == "__main__":
	app_obj = QtGui.QApplication(sys.argv)
	mh_obj = MicroHope_Editor()
	sys.exit(app_obj.exec_())
	
