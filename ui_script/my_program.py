# -*- coding: utf-8 -*-
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from script import init


class My_program(QFrame):
    def __init__(self, dominate_id: int, name: str, mainwin: object, parent=None):
        super(My_program, self).__init__(parent)

        # self.setGeometry(QRect(80, 89, 871, 91))
        self.setMaximumSize(QSize(16777215, 81))
        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget = QWidget(self)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.progressBar = QProgressBar(self.widget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.verticalLayout.addWidget(self.progressBar)

        self.horizontalLayout.addWidget(self.widget)

        self.pushButton = QPushButton(self)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.label.setText(name)
        self.pushButton.setText(QCoreApplication.translate(
            "Form", u"\u64cd\u4f5c", None))
        self.pushButton.clicked.connect(
            lambda: my_one_program(mainwin, dominate_id))

def view_my_program(mainwin: object):
    '''查看我的项目'''
    #清空verticalLayout_3中的所有控件
    for i in range(mainwin.verticalLayout_3.count()):
        mainwin.verticalLayout_3.itemAt(i).widget().deleteLater()

    # 获取dominate表中的所有数据
    data = init.get_dominate()
    for i in data:
        # 创建一个My_program对象
        my_program = My_program(i[0], i[1], mainwin)
        # 将my_program添加到mainwin中
        mainwin.verticalLayout_3.addWidget(my_program)
        mainwin.program_list.append(my_program)


def my_one_program(mainwin:object, dominate_id: int):
    '''点击我的项目中的操作按钮后触发显示我的项目具体的一个'''
