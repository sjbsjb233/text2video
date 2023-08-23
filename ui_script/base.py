#主窗口基本功能初始化
from PyQt5 import QtCore, QtGui, QtWidgets
from script.init import insert_dominate
from ui_script import my_program

def init_mainwin(self):
    '''初始化mainwin'''
    # 配置上面三个按钮的点击事件 
    # 关闭按钮
    self.pushButton_3.clicked.connect(self.close)
    # 最小化按钮
    self.pushButton.clicked.connect(self.showMinimized)
    # 最大化按钮
    self.pushButton_2.clicked.connect(lambda: max_win(self))

    # 去除边框
    self.setWindowFlag(QtCore.Qt.FramelessWindowHint)

    #隐藏tab_widget
    self.tabWidget.setTabVisible(5, False)
    self.tabWidget.setTabVisible(6, False)
    self.tabWidget_3.setTabVisible(2, False)

    # 点击pushButton_8后tab_widget转到index=6的页面
    self.pushButton_8.clicked.connect(
        lambda: self.tabWidget.setCurrentIndex(6))
    # 创建新项目按钮点击事件
    self.pushButton_24.clicked.connect(lambda: create_new_project(self))

    #tab_widget切换时触发
    self.tabWidget.currentChanged.connect(lambda: tab_widget_change(self))

    #重写comboBox鼠标滚轮事件
    self.comboBox.wheelEvent = lambda _: None


def tab_widget_change(self):
    #获取当前tab_widget的index
    index = self.tabWidget.currentIndex()
    if index == 1:
        #显示我的项目
        my_program.view_my_program(self)


def create_new_project(self):
    '''创建新项目按钮点击事件'''
    # 获取项目名称
    project_name = self.lineEdit.text()
    # 获取项目路径
    project_path = self.lineEdit_2.text()
    # 获取项目是否需要按章节切分
    chapter_regex = ''
    if self.checkBox.isChecked():
        split = 1
        # 获取章节切分正则表达式
        chapter_regex = self.lineEdit_3.text()
    else:
        split = 0
    
    #显示进度条
    self.progressBar.setVisible(True)
    # 多线程将项目信息写入dominate表
    self.thread = QtCore.QThread()
    self.thread.run = lambda: insert_dominate(
        project_name, split, chapter_regex, project_path,self.progressBar)
    self.thread.finished.connect(lambda: clear_create_new_project(self))
    self.thread.start()

def clear_create_new_project(self):
    '''清空创建新项目界面'''
    self.lineEdit.setText('')
    self.lineEdit_2.setText('')
    self.checkBox.setChecked(False)
    self.lineEdit_3.setText('')
    self.progressBar.setVisible(False)
    self.progressBar.setValue(0)
    self.tabWidget.setCurrentIndex(1)


def max_win(self):
    '''最大化窗口'''
    if self.isMaximized():
        self.showNormal()
    else:
        self.showMaximized()
