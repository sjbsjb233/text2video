import sys
from MainWin import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from qt_material import apply_stylesheet
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QCoreApplication
from PyQt5.QtGui import QCursor
from script.init import insert_dominate
from ui_script import base


class MainWin(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # 创建基础list
        self.program_list = []  # 我的项目的控件列表
        self.my_one_program_list = []  # 我的一个项目的tab标签大控件列表
        self.refresh_dict = {}  # 刷新控件的字典
        self.my_one_program = {}  # 我的一个项目 对应的tabwidget标签对象
        self.start_program = False  # 是否开始运行项目
        # 加载基础窗口控件
        base.init_mainwin(self)

    def mousePressEvent(self, event):
        self.m_flag = False
        # 鼠标点击事件(鼠标要在y轴45以下才能拖动窗口)
        if event.button() == Qt.LeftButton and event.pos().y() < 45:
            self.m_flag = True
            self.m_Position = event.globalPos()-self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            # self.setCursor(QCursor(Qt.OpenHandCursor))  #更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos()-self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWin()
    apply_stylesheet(app, theme='dark_teal.xml')
    win.show()
    sys.exit(app.exec_())
