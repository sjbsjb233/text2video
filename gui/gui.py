import sys
from MainWin import Ui_MainWindow
# from gui.MainWin import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from qt_material import apply_stylesheet

class MainWin(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWin()
    apply_stylesheet(app, theme='dark_teal.xml')
    win.show()
    sys.exit(app.exec_())