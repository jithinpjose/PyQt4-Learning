from PyQt4 import QtGui
import sys
app=QtGui.QApplication(sys.argv)
window=QtGui.QWidget()
window.resize(10,76)
window.setWindowTitle("window")
window.show()
sys.exit(app.exec_())
