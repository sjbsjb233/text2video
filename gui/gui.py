import sys
from MainWin import Ui_MainWindow
# from gui.MainWin import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from qt_material import apply_stylesheet
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QCoreApplication
from PyQt5.QtGui import QCursor

class MainWin(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        #配置上面三个按钮的点击事件
        self.close_button_clicked()

        #去除边框
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)

        #设置窗体移动

    def close_button_clicked(self):
        '''配置上面三个按钮的点击事件'''
        #关闭按钮
        self.pushButton_3.clicked.connect(self.close)
        #最小化按钮
        self.pushButton.clicked.connect(self.showMinimized)
        #最大化按钮
        self.pushButton_2.clicked.connect(self.max_win)
        
    def max_win(self):
        '''最大化窗口'''
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()
    
    def mousePressEvent(self, event):
        self.m_flag=False
        #鼠标点击事件(鼠标要在y轴45以下才能拖动窗口)
        if event.button()==Qt.LeftButton and event.pos().y()<45:
            self.m_flag=True
            self.m_Position=event.globalPos()-self.pos() #获取鼠标相对窗口的位置
            event.accept()
            # self.setCursor(QCursor(Qt.OpenHandCursor))  #更改鼠标图标
            
    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:  
            self.move(QMouseEvent.globalPos()-self.m_Position)#更改窗口位置
            QMouseEvent.accept()
            
    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag=False
        self.setCursor(QCursor(Qt.ArrowCursor))

        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWin()
    apply_stylesheet(app, theme='dark_teal.xml')
    win.show()
    sys.exit(app.exec_())