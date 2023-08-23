# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainUinXHKac.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 700)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(16777215, 35))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(11)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 5, -1, 5)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        font.setPointSize(12)
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(982, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(15)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMaximumSize(QSize(24, 24))
        self.pushButton.setStyleSheet(u"QPushButton{background:#6DDF6D;border-radius:5px;border:none}QPushButton:hover{background:green;}")

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMaximumSize(QSize(24, 24))
        self.pushButton_2.setStyleSheet(u"QPushButton{background:#F7D674;border-radius:5px;border:none}QPushButton:hover{background:yellow;}")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.widget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMaximumSize(QSize(24, 24))
        self.pushButton_3.setStyleSheet(u"QPushButton{background:#F76677;border-radius:5px;border:none}QPushButton:hover{background:red;}")

        self.horizontalLayout.addWidget(self.pushButton_3)


        self.verticalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.widget_2)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setElideMode(Qt.ElideNone)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_4 = QVBoxLayout(self.tab_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_2 = QFrame(self.tab_2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_8 = QPushButton(self.frame_2)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.horizontalLayout_3.addWidget(self.pushButton_8)

        self.pushButton_9 = QPushButton(self.frame_2)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.horizontalLayout_3.addWidget(self.pushButton_9)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout_4.addWidget(self.frame_2)

        self.frame = QFrame(self.tab_2)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(4, 4, 4, 4)
        self.scrollArea = QScrollArea(self.frame)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1154, 504))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)


        self.verticalLayout_4.addWidget(self.frame)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_18 = QVBoxLayout(self.tab_3)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.scrollArea_9 = QScrollArea(self.tab_3)
        self.scrollArea_9.setObjectName(u"scrollArea_9")
        self.scrollArea_9.setWidgetResizable(True)
        self.scrollAreaWidgetContents_9 = QWidget()
        self.scrollAreaWidgetContents_9.setObjectName(u"scrollAreaWidgetContents_9")
        self.scrollAreaWidgetContents_9.setGeometry(QRect(0, 0, 1147, 990))
        self.verticalLayout_13 = QVBoxLayout(self.scrollAreaWidgetContents_9)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.groupBox = QGroupBox(self.scrollAreaWidgetContents_9)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_14 = QVBoxLayout(self.groupBox)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.widget_19 = QWidget(self.groupBox)
        self.widget_19.setObjectName(u"widget_19")
        self.horizontalLayout_30 = QHBoxLayout(self.widget_19)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_26 = QLabel(self.widget_19)
        self.label_26.setObjectName(u"label_26")

        self.horizontalLayout_30.addWidget(self.label_26)

        self.label_27 = QLabel(self.widget_19)
        self.label_27.setObjectName(u"label_27")

        self.horizontalLayout_30.addWidget(self.label_27)

        self.horizontalSpacer_24 = QSpacerItem(923, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_24)

        self.pushButton_27 = QPushButton(self.widget_19)
        self.pushButton_27.setObjectName(u"pushButton_27")

        self.horizontalLayout_30.addWidget(self.pushButton_27)


        self.verticalLayout_14.addWidget(self.widget_19)


        self.verticalLayout_13.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.scrollAreaWidgetContents_9)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_15 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.widget_20 = QWidget(self.groupBox_2)
        self.widget_20.setObjectName(u"widget_20")
        self.horizontalLayout_31 = QHBoxLayout(self.widget_20)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label_28 = QLabel(self.widget_20)
        self.label_28.setObjectName(u"label_28")

        self.horizontalLayout_31.addWidget(self.label_28)

        self.lineEdit_4 = QLineEdit(self.widget_20)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.horizontalLayout_31.addWidget(self.lineEdit_4)

        self.pushButton_28 = QPushButton(self.widget_20)
        self.pushButton_28.setObjectName(u"pushButton_28")

        self.horizontalLayout_31.addWidget(self.pushButton_28)


        self.verticalLayout_15.addWidget(self.widget_20)

        self.widget_21 = QWidget(self.groupBox_2)
        self.widget_21.setObjectName(u"widget_21")
        self.horizontalLayout_32 = QHBoxLayout(self.widget_21)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.label_29 = QLabel(self.widget_21)
        self.label_29.setObjectName(u"label_29")

        self.horizontalLayout_32.addWidget(self.label_29)

        self.lineEdit_5 = QLineEdit(self.widget_21)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit_5.sizePolicy().hasHeightForWidth())
        self.lineEdit_5.setSizePolicy(sizePolicy1)

        self.horizontalLayout_32.addWidget(self.lineEdit_5)

        self.horizontalSpacer_25 = QSpacerItem(823, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_32.addItem(self.horizontalSpacer_25)


        self.verticalLayout_15.addWidget(self.widget_21)

        self.widget_22 = QWidget(self.groupBox_2)
        self.widget_22.setObjectName(u"widget_22")
        self.horizontalLayout_34 = QHBoxLayout(self.widget_22)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.label_30 = QLabel(self.widget_22)
        self.label_30.setObjectName(u"label_30")

        self.horizontalLayout_34.addWidget(self.label_30)

        self.lineEdit_6 = QLineEdit(self.widget_22)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        sizePolicy1.setHeightForWidth(self.lineEdit_6.sizePolicy().hasHeightForWidth())
        self.lineEdit_6.setSizePolicy(sizePolicy1)

        self.horizontalLayout_34.addWidget(self.lineEdit_6)

        self.horizontalSpacer_26 = QSpacerItem(829, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_34.addItem(self.horizontalSpacer_26)


        self.verticalLayout_15.addWidget(self.widget_22)

        self.widget_23 = QWidget(self.groupBox_2)
        self.widget_23.setObjectName(u"widget_23")
        self.horizontalLayout_35 = QHBoxLayout(self.widget_23)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.label_31 = QLabel(self.widget_23)
        self.label_31.setObjectName(u"label_31")

        self.horizontalLayout_35.addWidget(self.label_31)

        self.lineEdit_7 = QLineEdit(self.widget_23)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.horizontalLayout_35.addWidget(self.lineEdit_7)


        self.verticalLayout_15.addWidget(self.widget_23)

        self.widget_24 = QWidget(self.groupBox_2)
        self.widget_24.setObjectName(u"widget_24")
        self.horizontalLayout_36 = QHBoxLayout(self.widget_24)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.label_32 = QLabel(self.widget_24)
        self.label_32.setObjectName(u"label_32")

        self.horizontalLayout_36.addWidget(self.label_32)

        self.lineEdit_8 = QLineEdit(self.widget_24)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.horizontalLayout_36.addWidget(self.lineEdit_8)


        self.verticalLayout_15.addWidget(self.widget_24)

        self.widget_25 = QWidget(self.groupBox_2)
        self.widget_25.setObjectName(u"widget_25")
        self.horizontalLayout_37 = QHBoxLayout(self.widget_25)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.label_33 = QLabel(self.widget_25)
        self.label_33.setObjectName(u"label_33")

        self.horizontalLayout_37.addWidget(self.label_33)

        self.lineEdit_9 = QLineEdit(self.widget_25)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        sizePolicy1.setHeightForWidth(self.lineEdit_9.sizePolicy().hasHeightForWidth())
        self.lineEdit_9.setSizePolicy(sizePolicy1)

        self.horizontalLayout_37.addWidget(self.lineEdit_9)

        self.horizontalSpacer_27 = QSpacerItem(757, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_37.addItem(self.horizontalSpacer_27)


        self.verticalLayout_15.addWidget(self.widget_25)


        self.verticalLayout_13.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.scrollAreaWidgetContents_9)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_16 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.widget_26 = QWidget(self.groupBox_3)
        self.widget_26.setObjectName(u"widget_26")
        self.horizontalLayout_38 = QHBoxLayout(self.widget_26)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.label_34 = QLabel(self.widget_26)
        self.label_34.setObjectName(u"label_34")

        self.horizontalLayout_38.addWidget(self.label_34)

        self.comboBox = QComboBox(self.widget_26)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy2)

        self.horizontalLayout_38.addWidget(self.comboBox)

        self.horizontalSpacer_28 = QSpacerItem(473, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_38.addItem(self.horizontalSpacer_28)


        self.verticalLayout_16.addWidget(self.widget_26)


        self.verticalLayout_13.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(self.scrollAreaWidgetContents_9)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_17 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.widget_27 = QWidget(self.groupBox_4)
        self.widget_27.setObjectName(u"widget_27")
        self.horizontalLayout_39 = QHBoxLayout(self.widget_27)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.label_35 = QLabel(self.widget_27)
        self.label_35.setObjectName(u"label_35")

        self.horizontalLayout_39.addWidget(self.label_35)

        self.lineEdit_10 = QLineEdit(self.widget_27)
        self.lineEdit_10.setObjectName(u"lineEdit_10")

        self.horizontalLayout_39.addWidget(self.lineEdit_10)


        self.verticalLayout_17.addWidget(self.widget_27)

        self.widget_28 = QWidget(self.groupBox_4)
        self.widget_28.setObjectName(u"widget_28")
        self.horizontalLayout_40 = QHBoxLayout(self.widget_28)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.label_36 = QLabel(self.widget_28)
        self.label_36.setObjectName(u"label_36")

        self.horizontalLayout_40.addWidget(self.label_36)

        self.lineEdit_11 = QLineEdit(self.widget_28)
        self.lineEdit_11.setObjectName(u"lineEdit_11")

        self.horizontalLayout_40.addWidget(self.lineEdit_11)


        self.verticalLayout_17.addWidget(self.widget_28)

        self.widget_29 = QWidget(self.groupBox_4)
        self.widget_29.setObjectName(u"widget_29")
        self.horizontalLayout_41 = QHBoxLayout(self.widget_29)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.label_37 = QLabel(self.widget_29)
        self.label_37.setObjectName(u"label_37")

        self.horizontalLayout_41.addWidget(self.label_37)

        self.lineEdit_12 = QLineEdit(self.widget_29)
        self.lineEdit_12.setObjectName(u"lineEdit_12")

        self.horizontalLayout_41.addWidget(self.lineEdit_12)


        self.verticalLayout_17.addWidget(self.widget_29)

        self.widget_32 = QWidget(self.groupBox_4)
        self.widget_32.setObjectName(u"widget_32")
        self.horizontalLayout_42 = QHBoxLayout(self.widget_32)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.label_38 = QLabel(self.widget_32)
        self.label_38.setObjectName(u"label_38")

        self.horizontalLayout_42.addWidget(self.label_38)

        self.lineEdit_13 = QLineEdit(self.widget_32)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        sizePolicy1.setHeightForWidth(self.lineEdit_13.sizePolicy().hasHeightForWidth())
        self.lineEdit_13.setSizePolicy(sizePolicy1)

        self.horizontalLayout_42.addWidget(self.lineEdit_13)

        self.horizontalSpacer_32 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_42.addItem(self.horizontalSpacer_32)


        self.verticalLayout_17.addWidget(self.widget_32)

        self.widget_30 = QWidget(self.groupBox_4)
        self.widget_30.setObjectName(u"widget_30")
        self.horizontalLayout_43 = QHBoxLayout(self.widget_30)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.label_39 = QLabel(self.widget_30)
        self.label_39.setObjectName(u"label_39")

        self.horizontalLayout_43.addWidget(self.label_39)

        self.lineEdit_14 = QLineEdit(self.widget_30)
        self.lineEdit_14.setObjectName(u"lineEdit_14")

        self.horizontalLayout_43.addWidget(self.lineEdit_14)

        self.horizontalSpacer_33 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_43.addItem(self.horizontalSpacer_33)


        self.verticalLayout_17.addWidget(self.widget_30)

        self.widget_33 = QWidget(self.groupBox_4)
        self.widget_33.setObjectName(u"widget_33")
        self.horizontalLayout_44 = QHBoxLayout(self.widget_33)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.label_40 = QLabel(self.widget_33)
        self.label_40.setObjectName(u"label_40")

        self.horizontalLayout_44.addWidget(self.label_40)

        self.lineEdit_15 = QLineEdit(self.widget_33)
        self.lineEdit_15.setObjectName(u"lineEdit_15")
        sizePolicy1.setHeightForWidth(self.lineEdit_15.sizePolicy().hasHeightForWidth())
        self.lineEdit_15.setSizePolicy(sizePolicy1)

        self.horizontalLayout_44.addWidget(self.lineEdit_15)

        self.horizontalSpacer_34 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_44.addItem(self.horizontalSpacer_34)


        self.verticalLayout_17.addWidget(self.widget_33)

        self.widget_34 = QWidget(self.groupBox_4)
        self.widget_34.setObjectName(u"widget_34")
        self.horizontalLayout_45 = QHBoxLayout(self.widget_34)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.label_41 = QLabel(self.widget_34)
        self.label_41.setObjectName(u"label_41")

        self.horizontalLayout_45.addWidget(self.label_41)

        self.lineEdit_16 = QLineEdit(self.widget_34)
        self.lineEdit_16.setObjectName(u"lineEdit_16")
        sizePolicy1.setHeightForWidth(self.lineEdit_16.sizePolicy().hasHeightForWidth())
        self.lineEdit_16.setSizePolicy(sizePolicy1)

        self.horizontalLayout_45.addWidget(self.lineEdit_16)

        self.horizontalSpacer_35 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_45.addItem(self.horizontalSpacer_35)


        self.verticalLayout_17.addWidget(self.widget_34)

        self.widget_35 = QWidget(self.groupBox_4)
        self.widget_35.setObjectName(u"widget_35")
        self.horizontalLayout_46 = QHBoxLayout(self.widget_35)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.label_42 = QLabel(self.widget_35)
        self.label_42.setObjectName(u"label_42")

        self.horizontalLayout_46.addWidget(self.label_42)

        self.lineEdit_17 = QLineEdit(self.widget_35)
        self.lineEdit_17.setObjectName(u"lineEdit_17")
        sizePolicy1.setHeightForWidth(self.lineEdit_17.sizePolicy().hasHeightForWidth())
        self.lineEdit_17.setSizePolicy(sizePolicy1)

        self.horizontalLayout_46.addWidget(self.lineEdit_17)

        self.horizontalSpacer_36 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_46.addItem(self.horizontalSpacer_36)


        self.verticalLayout_17.addWidget(self.widget_35)

        self.widget_36 = QWidget(self.groupBox_4)
        self.widget_36.setObjectName(u"widget_36")
        self.horizontalLayout_47 = QHBoxLayout(self.widget_36)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.checkBox_3 = QCheckBox(self.widget_36)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.horizontalLayout_47.addWidget(self.checkBox_3)


        self.verticalLayout_17.addWidget(self.widget_36)

        self.widget_37 = QWidget(self.groupBox_4)
        self.widget_37.setObjectName(u"widget_37")
        self.horizontalLayout_48 = QHBoxLayout(self.widget_37)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.label_43 = QLabel(self.widget_37)
        self.label_43.setObjectName(u"label_43")

        self.horizontalLayout_48.addWidget(self.label_43)

        self.lineEdit_18 = QLineEdit(self.widget_37)
        self.lineEdit_18.setObjectName(u"lineEdit_18")

        self.horizontalLayout_48.addWidget(self.lineEdit_18)

        self.horizontalSpacer_37 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_48.addItem(self.horizontalSpacer_37)


        self.verticalLayout_17.addWidget(self.widget_37)

        self.widget_38 = QWidget(self.groupBox_4)
        self.widget_38.setObjectName(u"widget_38")
        self.horizontalLayout_49 = QHBoxLayout(self.widget_38)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.label_44 = QLabel(self.widget_38)
        self.label_44.setObjectName(u"label_44")

        self.horizontalLayout_49.addWidget(self.label_44)

        self.lineEdit_19 = QLineEdit(self.widget_38)
        self.lineEdit_19.setObjectName(u"lineEdit_19")
        sizePolicy1.setHeightForWidth(self.lineEdit_19.sizePolicy().hasHeightForWidth())
        self.lineEdit_19.setSizePolicy(sizePolicy1)

        self.horizontalLayout_49.addWidget(self.lineEdit_19)

        self.horizontalSpacer_38 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_49.addItem(self.horizontalSpacer_38)


        self.verticalLayout_17.addWidget(self.widget_38)


        self.verticalLayout_13.addWidget(self.groupBox_4)

        self.scrollArea_9.setWidget(self.scrollAreaWidgetContents_9)

        self.verticalLayout_18.addWidget(self.scrollArea_9)

        self.widget_31 = QWidget(self.tab_3)
        self.widget_31.setObjectName(u"widget_31")
        self.horizontalLayout_33 = QHBoxLayout(self.widget_31)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalSpacer_29 = QSpacerItem(322, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_33.addItem(self.horizontalSpacer_29)

        self.pushButton_30 = QPushButton(self.widget_31)
        self.pushButton_30.setObjectName(u"pushButton_30")

        self.horizontalLayout_33.addWidget(self.pushButton_30)

        self.horizontalSpacer_30 = QSpacerItem(321, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_33.addItem(self.horizontalSpacer_30)

        self.pushButton_29 = QPushButton(self.widget_31)
        self.pushButton_29.setObjectName(u"pushButton_29")

        self.horizontalLayout_33.addWidget(self.pushButton_29)

        self.horizontalSpacer_31 = QSpacerItem(322, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_33.addItem(self.horizontalSpacer_31)


        self.verticalLayout_18.addWidget(self.widget_31)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.horizontalLayout_4 = QHBoxLayout(self.tab_6)
        self.horizontalLayout_4.setSpacing(4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.tabWidget_2 = QTabWidget(self.tab_6)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.verticalLayout_6 = QVBoxLayout(self.tab_7)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.widget_3 = QWidget(self.tab_7)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_2 = QLabel(self.widget_3)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_5.addWidget(self.label_2)

        self.label_3 = QLabel(self.widget_3)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_5.addWidget(self.label_3)

        self.horizontalSpacer_3 = QSpacerItem(865, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.label_4 = QLabel(self.widget_3)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_5.addWidget(self.label_4)

        self.label_5 = QLabel(self.widget_3)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)


        self.verticalLayout_6.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.tab_7)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.pushButton_15 = QPushButton(self.widget_4)
        self.pushButton_15.setObjectName(u"pushButton_15")

        self.horizontalLayout_6.addWidget(self.pushButton_15)

        self.pushButton_16 = QPushButton(self.widget_4)
        self.pushButton_16.setObjectName(u"pushButton_16")

        self.horizontalLayout_6.addWidget(self.pushButton_16)

        self.pushButton_17 = QPushButton(self.widget_4)
        self.pushButton_17.setObjectName(u"pushButton_17")

        self.horizontalLayout_6.addWidget(self.pushButton_17)

        self.pushButton_18 = QPushButton(self.widget_4)
        self.pushButton_18.setObjectName(u"pushButton_18")

        self.horizontalLayout_6.addWidget(self.pushButton_18)

        self.pushButton_19 = QPushButton(self.widget_4)
        self.pushButton_19.setObjectName(u"pushButton_19")

        self.horizontalLayout_6.addWidget(self.pushButton_19)

        self.horizontalSpacer_4 = QSpacerItem(562, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)

        self.pushButton_4 = QPushButton(self.widget_4)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_6.addWidget(self.pushButton_4)

        self.pushButton_6 = QPushButton(self.widget_4)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.horizontalLayout_6.addWidget(self.pushButton_6)


        self.verticalLayout_6.addWidget(self.widget_4)

        self.widget_5 = QWidget(self.tab_7)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.listView = QListView(self.widget_5)
        self.listView.setObjectName(u"listView")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(2)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.listView.sizePolicy().hasHeightForWidth())
        self.listView.setSizePolicy(sizePolicy3)

        self.horizontalLayout_7.addWidget(self.listView)

        self.line_2 = QFrame(self.widget_5)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_7.addWidget(self.line_2)

        self.frame_4 = QFrame(self.widget_5)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(9)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy4)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(3, 3, 3, 3)
        self.scrollArea_2 = QScrollArea(self.frame_4)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(9)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.scrollArea_2.sizePolicy().hasHeightForWidth())
        self.scrollArea_2.setSizePolicy(sizePolicy5)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 904, 408))
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_5.addWidget(self.scrollArea_2)


        self.horizontalLayout_7.addWidget(self.frame_4)


        self.verticalLayout_6.addWidget(self.widget_5)

        self.tabWidget_2.addTab(self.tab_7, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.horizontalLayout_8 = QHBoxLayout(self.tab_8)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.tabWidget_3 = QTabWidget(self.tab_8)
        self.tabWidget_3.setObjectName(u"tabWidget_3")
        self.tab_12 = QWidget()
        self.tab_12.setObjectName(u"tab_12")
        self.horizontalLayout_17 = QHBoxLayout(self.tab_12)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.scrollArea_3 = QScrollArea(self.tab_12)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 1124, 485))
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.horizontalLayout_17.addWidget(self.scrollArea_3)

        self.tabWidget_3.addTab(self.tab_12, "")
        self.tab_13 = QWidget()
        self.tab_13.setObjectName(u"tab_13")
        self.horizontalLayout_18 = QHBoxLayout(self.tab_13)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.scrollArea_4 = QScrollArea(self.tab_13)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 1124, 485))
        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)

        self.horizontalLayout_18.addWidget(self.scrollArea_4)

        self.tabWidget_3.addTab(self.tab_13, "")
        self.tab_14 = QWidget()
        self.tab_14.setObjectName(u"tab_14")
        self.verticalLayout_7 = QVBoxLayout(self.tab_14)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_6 = QLabel(self.tab_14)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.verticalLayout_7.addWidget(self.label_6)

        self.tabWidget_4 = QTabWidget(self.tab_14)
        self.tabWidget_4.setObjectName(u"tabWidget_4")
        self.tab_15 = QWidget()
        self.tab_15.setObjectName(u"tab_15")
        self.verticalLayout_8 = QVBoxLayout(self.tab_15)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.widget_6 = QWidget(self.tab_15)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_7 = QLabel(self.widget_6)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_9.addWidget(self.label_7)

        self.label_8 = QLabel(self.widget_6)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_9.addWidget(self.label_8)

        self.horizontalSpacer_5 = QSpacerItem(883, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_5)

        self.label_9 = QLabel(self.widget_6)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_9.addWidget(self.label_9)


        self.verticalLayout_8.addWidget(self.widget_6)

        self.textEdit = QTextEdit(self.tab_15)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout_8.addWidget(self.textEdit)

        self.progressBar_2 = QProgressBar(self.tab_15)
        self.progressBar_2.setObjectName(u"progressBar_2")
        self.progressBar_2.setValue(0)

        self.verticalLayout_8.addWidget(self.progressBar_2)

        self.widget_7 = QWidget(self.tab_15)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_10 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_7)

        self.pushButton_20 = QPushButton(self.widget_7)
        self.pushButton_20.setObjectName(u"pushButton_20")

        self.horizontalLayout_10.addWidget(self.pushButton_20)

        self.horizontalSpacer_6 = QSpacerItem(301, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_6)

        self.pushButton_21 = QPushButton(self.widget_7)
        self.pushButton_21.setObjectName(u"pushButton_21")

        self.horizontalLayout_10.addWidget(self.pushButton_21)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_8)


        self.verticalLayout_8.addWidget(self.widget_7)

        self.tabWidget_4.addTab(self.tab_15, "")
        self.tab_16 = QWidget()
        self.tab_16.setObjectName(u"tab_16")
        self.verticalLayout_9 = QVBoxLayout(self.tab_16)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_10 = QLabel(self.tab_16)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_9.addWidget(self.label_10)

        self.textEdit_2 = QTextEdit(self.tab_16)
        self.textEdit_2.setObjectName(u"textEdit_2")

        self.verticalLayout_9.addWidget(self.textEdit_2)

        self.widget_8 = QWidget(self.tab_16)
        self.widget_8.setObjectName(u"widget_8")
        self.horizontalLayout_11 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer_9 = QSpacerItem(401, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_9)

        self.pushButton_22 = QPushButton(self.widget_8)
        self.pushButton_22.setObjectName(u"pushButton_22")

        self.horizontalLayout_11.addWidget(self.pushButton_22)

        self.horizontalSpacer_10 = QSpacerItem(401, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_10)


        self.verticalLayout_9.addWidget(self.widget_8)

        self.tabWidget_4.addTab(self.tab_16, "")

        self.verticalLayout_7.addWidget(self.tabWidget_4)

        self.tabWidget_3.addTab(self.tab_14, "")

        self.horizontalLayout_8.addWidget(self.tabWidget_3)

        self.tabWidget_2.addTab(self.tab_8, "")
        self.tab_9 = QWidget()
        self.tab_9.setObjectName(u"tab_9")
        self.horizontalLayout_19 = QHBoxLayout(self.tab_9)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.tabWidget_5 = QTabWidget(self.tab_9)
        self.tabWidget_5.setObjectName(u"tabWidget_5")
        self.tab_18 = QWidget()
        self.tab_18.setObjectName(u"tab_18")
        self.horizontalLayout_20 = QHBoxLayout(self.tab_18)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.scrollArea_5 = QScrollArea(self.tab_18)
        self.scrollArea_5.setObjectName(u"scrollArea_5")
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 1124, 485))
        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_5)

        self.horizontalLayout_20.addWidget(self.scrollArea_5)

        self.tabWidget_5.addTab(self.tab_18, "")
        self.tab_19 = QWidget()
        self.tab_19.setObjectName(u"tab_19")
        self.verticalLayout_12 = QVBoxLayout(self.tab_19)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.widget_14 = QWidget(self.tab_19)
        self.widget_14.setObjectName(u"widget_14")
        self.horizontalLayout_21 = QHBoxLayout(self.widget_14)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalSpacer_17 = QSpacerItem(208, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_17)

        self.label_18 = QLabel(self.widget_14)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_21.addWidget(self.label_18)

        self.label_19 = QLabel(self.widget_14)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_21.addWidget(self.label_19)

        self.horizontalSpacer_16 = QSpacerItem(209, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_16)

        self.label_16 = QLabel(self.widget_14)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_21.addWidget(self.label_16)

        self.label_17 = QLabel(self.widget_14)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_21.addWidget(self.label_17)

        self.horizontalSpacer_15 = QSpacerItem(208, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_15)

        self.checkBox_2 = QCheckBox(self.widget_14)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.horizontalLayout_21.addWidget(self.checkBox_2)

        self.horizontalSpacer_14 = QSpacerItem(208, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_14)


        self.verticalLayout_12.addWidget(self.widget_14)

        self.frame_5 = QFrame(self.tab_19)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_5)
        self.verticalLayout_11.setSpacing(4)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(5, 5, 5, 5)
        self.widget_15 = QWidget(self.frame_5)
        self.widget_15.setObjectName(u"widget_15")
        self.horizontalLayout_23 = QHBoxLayout(self.widget_15)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_20 = QLabel(self.widget_15)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_23.addWidget(self.label_20)

        self.label_21 = QLabel(self.widget_15)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_23.addWidget(self.label_21)

        self.horizontalSpacer_18 = QSpacerItem(1021, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_18)


        self.verticalLayout_11.addWidget(self.widget_15)

        self.widget_16 = QWidget(self.frame_5)
        self.widget_16.setObjectName(u"widget_16")
        self.horizontalLayout_22 = QHBoxLayout(self.widget_16)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_22 = QLabel(self.widget_16)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_22.addWidget(self.label_22)

        self.label_23 = QLabel(self.widget_16)
        self.label_23.setObjectName(u"label_23")

        self.horizontalLayout_22.addWidget(self.label_23)

        self.horizontalSpacer_19 = QSpacerItem(1009, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_19)


        self.verticalLayout_11.addWidget(self.widget_16)

        self.widget_17 = QWidget(self.frame_5)
        self.widget_17.setObjectName(u"widget_17")
        self.horizontalLayout_24 = QHBoxLayout(self.widget_17)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_24 = QLabel(self.widget_17)
        self.label_24.setObjectName(u"label_24")

        self.horizontalLayout_24.addWidget(self.label_24)

        self.horizontalSpacer_20 = QSpacerItem(1009, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_20)


        self.verticalLayout_11.addWidget(self.widget_17)

        self.label_25 = QLabel(self.frame_5)
        self.label_25.setObjectName(u"label_25")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy6)

        self.verticalLayout_11.addWidget(self.label_25)

        self.widget_18 = QWidget(self.frame_5)
        self.widget_18.setObjectName(u"widget_18")
        self.horizontalLayout_25 = QHBoxLayout(self.widget_18)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalSpacer_21 = QSpacerItem(304, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_21)

        self.pushButton_25 = QPushButton(self.widget_18)
        self.pushButton_25.setObjectName(u"pushButton_25")

        self.horizontalLayout_25.addWidget(self.pushButton_25)

        self.horizontalSpacer_22 = QSpacerItem(305, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_22)

        self.pushButton_26 = QPushButton(self.widget_18)
        self.pushButton_26.setObjectName(u"pushButton_26")
        self.pushButton_26.setCursor(QCursor(Qt.ArrowCursor))

        self.horizontalLayout_25.addWidget(self.pushButton_26)

        self.horizontalSpacer_23 = QSpacerItem(304, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_23)


        self.verticalLayout_11.addWidget(self.widget_18)


        self.verticalLayout_12.addWidget(self.frame_5)

        self.tabWidget_5.addTab(self.tab_19, "")
        self.tab_20 = QWidget()
        self.tab_20.setObjectName(u"tab_20")
        self.horizontalLayout_26 = QHBoxLayout(self.tab_20)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.scrollArea_6 = QScrollArea(self.tab_20)
        self.scrollArea_6.setObjectName(u"scrollArea_6")
        self.scrollArea_6.setWidgetResizable(True)
        self.scrollAreaWidgetContents_6 = QWidget()
        self.scrollAreaWidgetContents_6.setObjectName(u"scrollAreaWidgetContents_6")
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, 0, 1124, 485))
        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_6)

        self.horizontalLayout_26.addWidget(self.scrollArea_6)

        self.tabWidget_5.addTab(self.tab_20, "")
        self.tab_23 = QWidget()
        self.tab_23.setObjectName(u"tab_23")
        self.verticalLayout_19 = QVBoxLayout(self.tab_23)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.widget_39 = QWidget(self.tab_23)
        self.widget_39.setObjectName(u"widget_39")
        self.horizontalLayout_50 = QHBoxLayout(self.widget_39)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.pushButton_5 = QPushButton(self.widget_39)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.horizontalLayout_50.addWidget(self.pushButton_5)

        self.horizontalSpacer_39 = QSpacerItem(1024, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_50.addItem(self.horizontalSpacer_39)


        self.verticalLayout_19.addWidget(self.widget_39)

        self.scrollArea_10 = QScrollArea(self.tab_23)
        self.scrollArea_10.setObjectName(u"scrollArea_10")
        self.scrollArea_10.setWidgetResizable(True)
        self.scrollAreaWidgetContents_10 = QWidget()
        self.scrollAreaWidgetContents_10.setObjectName(u"scrollAreaWidgetContents_10")
        self.scrollAreaWidgetContents_10.setGeometry(QRect(0, 0, 1124, 438))
        self.scrollArea_10.setWidget(self.scrollAreaWidgetContents_10)

        self.verticalLayout_19.addWidget(self.scrollArea_10)

        self.tabWidget_5.addTab(self.tab_23, "")

        self.horizontalLayout_19.addWidget(self.tabWidget_5)

        self.tabWidget_2.addTab(self.tab_9, "")
        self.tab_10 = QWidget()
        self.tab_10.setObjectName(u"tab_10")
        self.horizontalLayout_27 = QHBoxLayout(self.tab_10)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.tabWidget_6 = QTabWidget(self.tab_10)
        self.tabWidget_6.setObjectName(u"tabWidget_6")
        self.tab_21 = QWidget()
        self.tab_21.setObjectName(u"tab_21")
        self.horizontalLayout_28 = QHBoxLayout(self.tab_21)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.scrollArea_7 = QScrollArea(self.tab_21)
        self.scrollArea_7.setObjectName(u"scrollArea_7")
        self.scrollArea_7.setWidgetResizable(True)
        self.scrollAreaWidgetContents_7 = QWidget()
        self.scrollAreaWidgetContents_7.setObjectName(u"scrollAreaWidgetContents_7")
        self.scrollAreaWidgetContents_7.setGeometry(QRect(0, 0, 1124, 485))
        self.scrollArea_7.setWidget(self.scrollAreaWidgetContents_7)

        self.horizontalLayout_28.addWidget(self.scrollArea_7)

        self.tabWidget_6.addTab(self.tab_21, "")
        self.tab_22 = QWidget()
        self.tab_22.setObjectName(u"tab_22")
        self.horizontalLayout_29 = QHBoxLayout(self.tab_22)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.scrollArea_8 = QScrollArea(self.tab_22)
        self.scrollArea_8.setObjectName(u"scrollArea_8")
        self.scrollArea_8.setWidgetResizable(True)
        self.scrollAreaWidgetContents_8 = QWidget()
        self.scrollAreaWidgetContents_8.setObjectName(u"scrollAreaWidgetContents_8")
        self.scrollAreaWidgetContents_8.setGeometry(QRect(0, 0, 935, 485))
        self.scrollArea_8.setWidget(self.scrollAreaWidgetContents_8)

        self.horizontalLayout_29.addWidget(self.scrollArea_8)

        self.tabWidget_6.addTab(self.tab_22, "")

        self.horizontalLayout_27.addWidget(self.tabWidget_6)

        self.tabWidget_2.addTab(self.tab_10, "")
        self.tab_11 = QWidget()
        self.tab_11.setObjectName(u"tab_11")
        self.tabWidget_2.addTab(self.tab_11, "")

        self.horizontalLayout_4.addWidget(self.tabWidget_2)

        self.tabWidget.addTab(self.tab_6, "")
        self.tab_17 = QWidget()
        self.tab_17.setObjectName(u"tab_17")
        self.verticalLayout_10 = QVBoxLayout(self.tab_17)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_11 = QLabel(self.tab_17)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)

        self.verticalLayout_10.addWidget(self.label_11)

        self.widget_9 = QWidget(self.tab_17)
        self.widget_9.setObjectName(u"widget_9")
        self.horizontalLayout_12 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_12 = QLabel(self.widget_9)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_12.addWidget(self.label_12)

        self.lineEdit = QLineEdit(self.widget_9)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_12.addWidget(self.lineEdit)


        self.verticalLayout_10.addWidget(self.widget_9)

        self.widget_10 = QWidget(self.tab_17)
        self.widget_10.setObjectName(u"widget_10")
        self.horizontalLayout_13 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_13 = QLabel(self.widget_10)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_13.addWidget(self.label_13)

        self.lineEdit_2 = QLineEdit(self.widget_10)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_13.addWidget(self.lineEdit_2)

        self.pushButton_23 = QPushButton(self.widget_10)
        self.pushButton_23.setObjectName(u"pushButton_23")
        sizePolicy7 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.pushButton_23.sizePolicy().hasHeightForWidth())
        self.pushButton_23.setSizePolicy(sizePolicy7)

        self.horizontalLayout_13.addWidget(self.pushButton_23)


        self.verticalLayout_10.addWidget(self.widget_10)

        self.widget_11 = QWidget(self.tab_17)
        self.widget_11.setObjectName(u"widget_11")
        self.horizontalLayout_15 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_14 = QLabel(self.widget_11)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_15.addWidget(self.label_14)

        self.checkBox = QCheckBox(self.widget_11)
        self.checkBox.setObjectName(u"checkBox")

        self.horizontalLayout_15.addWidget(self.checkBox)

        self.horizontalSpacer_11 = QSpacerItem(499, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_11)

        self.widget_12 = QWidget(self.widget_11)
        self.widget_12.setObjectName(u"widget_12")
        self.horizontalLayout_14 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_15 = QLabel(self.widget_12)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_14.addWidget(self.label_15)

        self.lineEdit_3 = QLineEdit(self.widget_12)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.horizontalLayout_14.addWidget(self.lineEdit_3)


        self.horizontalLayout_15.addWidget(self.widget_12)


        self.verticalLayout_10.addWidget(self.widget_11)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_3)

        self.progressBar = QProgressBar(self.tab_17)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setEnabled(True)
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setInvertedAppearance(False)

        self.verticalLayout_10.addWidget(self.progressBar)

        self.widget_13 = QWidget(self.tab_17)
        self.widget_13.setObjectName(u"widget_13")
        self.horizontalLayout_16 = QHBoxLayout(self.widget_13)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalSpacer_12 = QSpacerItem(528, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_12)

        self.pushButton_24 = QPushButton(self.widget_13)
        self.pushButton_24.setObjectName(u"pushButton_24")

        self.horizontalLayout_16.addWidget(self.pushButton_24)

        self.horizontalSpacer_13 = QSpacerItem(527, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_13)


        self.verticalLayout_10.addWidget(self.widget_13)

        self.tabWidget.addTab(self.tab_17, "")

        self.horizontalLayout_2.addWidget(self.tabWidget)


        self.verticalLayout.addWidget(self.widget_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1200, 23))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(0)
        self.tabWidget_4.setCurrentIndex(0)
        self.tabWidget_5.setCurrentIndex(0)
        self.tabWidget_6.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Text2Img", None))
        self.pushButton.setText("")
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u4e3b\u9875", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"\u521b\u5efa", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u6211\u7684\u9879\u76ee", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Text2Img", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u7248\u672c:", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"1.0", None))
        self.pushButton_27.setText(QCoreApplication.translate("MainWindow", u"\u68c0\u67e5\u66f4\u65b0", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"ChatGPT(\u667a\u80fd\u5206\u955c/\u63d2\u56fe\u751f\u6210)", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"OpenAI\u5bc6\u94a5Key:", None))
        self.pushButton_28.setText(QCoreApplication.translate("MainWindow", u"\u663e\u793a", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"\u5bc6\u94a5\u8d26\u6237\u4f59\u989d(\u7f8e\u5143$):", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"1\u5343Token\u6240\u9700\u7684\u7f8e\u5143:", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"ChatGPT\u751f\u6210Prompt\u7684System\u9884\u8bbe:", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"ChatGPT\u667a\u80fd\u5206\u955c\u7684System\u9884\u8bbe:", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"\u8c03\u7528ChatGPT API\u82b1\u8d39\u7684\u6700\u5927Token:", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Edge-tts(\u914d\u97f3\u751f\u6210)", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Edge-tts\u914d\u97f3\u4e3b\u64ad\u9009\u62e9:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"zh-CN-YunxiNeural", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"zh-CN-XiaoxiaoNeural", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"zh-CN-XiaoyiNeural", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"zh-CN-YunjianNeural", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"zh-CN-YunxiaNeural", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"zh-CN-YunyangNeural", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"zh-CN-liaoning-XiaobeiNeural", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"zh-CN-shaanxi-XiaoniNeural", None))
        self.comboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"zh-HK-HiuGaaiNeural", None))
        self.comboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"zh-HK-HiuMaanNeural", None))
        self.comboBox.setItemText(10, QCoreApplication.translate("MainWindow", u"zh-HK-WanLungNeural", None))
        self.comboBox.setItemText(11, QCoreApplication.translate("MainWindow", u"zh-TW-HsiaoChenNeural", None))
        self.comboBox.setItemText(12, QCoreApplication.translate("MainWindow", u"zh-TW-HsiaoYuNeural", None))
        self.comboBox.setItemText(13, QCoreApplication.translate("MainWindow", u"zh-TW-YunJheNeural", None))

        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Stable Diffusion(\u63d2\u56fe\u751f\u6210/\u9ad8\u6e05\u4fee\u590d)", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Stable Diffusion\u56fa\u5b9a\u6b63\u5411Prompt:", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Stable Diffusion\u56fa\u5b9a\u53cd\u5411Prompt:", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Stable Diffusion\u79cd\u5b50(seed):", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Stable Diffusion\u63d0\u793a\u8bcd\u76f8\u5173\u5ea6(cfg scale):", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Stable Diffusion\u91c7\u6837\u65b9\u6cd5(sampler):", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Stable Diffusion\u63d2\u56fe\u751f\u6210\u5bbd\u5ea6(width):", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Stable Diffusion\u63d2\u56fe\u751f\u6210\u9ad8\u5ea6(height):", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Stable Diffusion\u91c7\u6837\u6b65\u6570(step):", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"Stable Diffusion\u9762\u90e8\u4fee\u590d(restore face)", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Stable Diffusion\u9ad8\u6e05\u4fee\u590d\u7b97\u6cd5:", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Stable Diffusion\u9ad8\u6e05\u4fee\u590d\u653e\u5927\u500d\u6570(upscaling resize):", None))
        self.pushButton_30.setText(QCoreApplication.translate("MainWindow", u"\u6062\u590d\u9ed8\u8ba4", None))
        self.pushButton_29.setText(QCoreApplication.translate("MainWindow", u"\u5e94\u7528", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"\u4e91\u8ba1\u7b97", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u9879\u76ee\u540d\u79f0\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\uff1f\uff1f\uff1f", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u7d2f\u8ba1\u6d88\u8017ChatGPT Tokens:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664\u9879\u76ee", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u589e\u7ae0\u8282", None))
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"\u6682\u505c\u6240\u6709", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"\u7ee7\u7eed\u6240\u6709", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u547d\u540d", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u4eba\u7269\u56fa\u5b9a", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"\u63d2\u56fe\u5ba1\u6838", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", u"\u4e3b\u4fe1\u606f", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_12), QCoreApplication.translate("MainWindow", u"\u672a\u5b8c\u6210", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_13), QCoreApplication.translate("MainWindow", u"\u5df2\u5b8c\u6210", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u521b\u5efa\u5206\u955c", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u72b6\u6001:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u672a\u5f00\u59cb", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"(\u6e29\u99a8\u63d0\u9192:\u4e00\u884c\u4e00\u955c)", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u5206\u955c\u5185\u5bb9\u4e8e\u6b64\u663e\u793a\u6216\u4fee\u6539</p></body></html>", None))
        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cbAI\u5206\u955c", None))
        self.pushButton_21.setText(QCoreApplication.translate("MainWindow", u"\u63d0\u4ea4", None))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_15), QCoreApplication.translate("MainWindow", u"AI\u5206\u955c", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u6e29\u99a8\u63d0\u9192:\u4e00\u884c\u4e00\u955c", None))
        self.pushButton_22.setText(QCoreApplication.translate("MainWindow", u"\u63d0\u4ea4", None))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_16), QCoreApplication.translate("MainWindow", u"\u4eba\u5de5\u5206\u955c", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_14), QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u9875(\u9690\u85cf)", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_8), QCoreApplication.translate("MainWindow", u"\u5207\u5206\u955c", None))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_18), QCoreApplication.translate("MainWindow", u"\u672a\u5b8c\u6210", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u5171\u9700\u5ba1\u6838:", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u672c\u6b21\u5269\u4f59\u5ba1\u6838:", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"\u65e0\u9700\u5ba1\u6838", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u63d0\u793a\u8bcd:", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"???", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"\u5206\u955c\u539f\u6587:", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"???", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"\u7b2cx\u7ae0 \u7b2cx\u90e8\u5206", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"PIC", None))
        self.pushButton_25.setText(QCoreApplication.translate("MainWindow", u"\u901a\u8fc7(Space)", None))
        self.pushButton_26.setText(QCoreApplication.translate("MainWindow", u"\u4e0d\u901a\u8fc7(F)", None))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_19), QCoreApplication.translate("MainWindow", u"\u5f85\u5ba1\u6838", None))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_20), QCoreApplication.translate("MainWindow", u"\u5df2\u5b8c\u6210", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0", None))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_23), QCoreApplication.translate("MainWindow", u"\u4eba\u7269\u56fa\u5b9a", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_9), QCoreApplication.translate("MainWindow", u"\u63d2\u56fe\u751f\u6210", None))
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(self.tab_21), QCoreApplication.translate("MainWindow", u"\u672a\u5b8c\u6210", None))
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(self.tab_22), QCoreApplication.translate("MainWindow", u"\u5df2\u5b8c\u6210", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_10), QCoreApplication.translate("MainWindow", u"\u914d\u97f3\u751f\u6210", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_11), QCoreApplication.translate("MainWindow", u"\u89c6\u9891\u751f\u6210", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"\u6211\u7684\u9879\u76ee\u5177\u4f53\u7684\u4e00\u4e2a(\u9690\u85cf)", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u521b\u5efa\u9879\u76ee:", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u9879\u76ee\u540d\u79f0:", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u6587\u672c\u8def\u5f84:", None))
        self.pushButton_23.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u662f\u5426\u9700\u8981\u6309\u7ae0\u8282\u5207\u5206:", None))
        self.checkBox.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u7ae0\u8282\u6b63\u5219\u8868\u8fbe\u5f0f:", None))
        self.pushButton_24.setText(QCoreApplication.translate("MainWindow", u"\u521b\u5efa", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_17), QCoreApplication.translate("MainWindow", u"\u521b\u5efa\u9879\u76ee(\u9690\u85cf)", None))
    # retranslateUi

