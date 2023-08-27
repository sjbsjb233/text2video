# -*- coding: utf-8 -*-
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from script import init
from script import cut_novel


def view_my_program(mainwin: object):
    '''查看我的项目'''
    # 清空verticalLayout_3中的所有控件
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


def my_one_program(mainwin: object, dominate_id: int):
    '''点击我的项目中的操作按钮后触发显示我的项目具体的一个'''
    tab = mainwin.my_one_program.get(dominate_id)
    if tab:
        # 如果tab存在
        mainwin.tabWidget.setCurrentWidget(tab)
        return
    # 如果tab不存在
    # 创建一个tab
    new_tab = My_one_program(mainwin, dominate_id)
    # 将tab添加到tabWidget中
    mainwin.tabWidget.addTab(new_tab.tab_6, "")
    # 获取new_tab的index
    index = mainwin.tabWidget.indexOf(new_tab.tab_6)
    # 隐藏当前的new_tab
    mainwin.tabWidget.setTabVisible(index, False)
    # tabWidget切换到new_tab
    mainwin.tabWidget.setCurrentWidget(new_tab.tab_6)
    # 将new_tab添加到my_one_program字典中
    mainwin.my_one_program[dominate_id] = new_tab
    # 初始化new_tab
    new_tab.init_new_tab()


class My_program(QFrame):
    '''我的项目操作条子'''

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

        self.dominat_id = dominate_id  # 项目的dominate_id


class My_one_program():
    def init_new_tab(self):
        '''初始化new_tab,附加内容'''
        self.part = {}  # 每一个部分的控件存储
        self.mainwin.refresh_dict[self.dominate_id] = [
            self.refresh]  # 刷新控件的字典加入本项目
        # 主信息页面
        # 获取dominate表中的指定id数据
        data = init.get_program_info(self.dominate_id)
        self.path = data[5]  # 项目路径

        self.if_start_ai_screenshot = False  # 是否开始AI分镜

        # 显示项目名称
        self.label_3.setText(data[1])
        # 显示花费的tokens
        self.label_5.setText(str(data[3]))
        # 恢复按钮状态
        self.pushButton_17.setEnabled(True)
        self.pushButton_18.setEnabled(True)
        self.pushButton_21.setEnabled(False)  # 切分镜--AI分镜--提交按钮
        # 删除项目按钮事件
        self.pushButton_15.clicked.connect(self.delete_program)
        # 重命名项目按钮事件
        self.pushButton_19.clicked.connect(self.rename_program)
        # 人物固定按钮事件
        self.pushButton_4.clicked.connect(self.loro_figure)
        # 插图审核按钮事件
        self.pushButton_6.clicked.connect(self.pic_review)

        # 加载主信息--分镜信息内容
        self.load_part_info()

    def start_ai_screenshot(self, chapter):
        '''开始AI分镜按钮点击事件'''
        # 禁用按钮
        self.pushButton_20.setEnabled(False)
        self.label_8.setText('AI分镜处理中(等待ChatGPT响应)')
        # 多线程执行AI分镜
        self.ai_screenshot_thread = QThread()
        self.ai_screenshot_thread.run(lambda: cut_novel.gpt_split(
            self.path, chapter, self.progressBar_2, self.textEdit))
        self.ai_screenshot_thread.finished.connect(
            self.ai_screenshot_thread_over)
        self.ai_screenshot_thread.start()
        self.if_start_ai_screenshot = True

    def ai_screenshot_thread_over(self):
        '''AI分镜线程结束后执行'''
        # 启用按钮
        self.pushButton_21.setEnabled(True)  # 提交按钮
        # 更新状态
        self.label_8.setText('AI分镜处理完成,请人工审核后点击提交按钮')

        self.if_start_ai_screenshot = False

    def add_chapter(self):
        '''添加章节'''
        # 弹出对话框
        text, ok = QInputDialog.getText(
            self.tab_6, '添加章节', '请输入章节内容:')
        if ok:
            pass

    def load_part_info(self):
        '''加载主信息--分镜信息内容'''
        # 获取章节数量
        chapter_num = init.get_chapter_num(self.path)
        # 向listView中添加item
        chapter = []
        for i in range(chapter_num):
            chapter.append('第%s章' % str(i+1))
        slm = QStringListModel()
        slm.setStringList(chapter)
        self.listView.setModel(slm)
        # 设置listView的点击事件
        # ???

        part_list = init.get_part_list(self.path)
        for i in part_list:
            state, persent = init.get_state(self.path, i[0])
            self.part[(i[1], i[2])] = Part_info(self.mainwin, self, i[1], i[2])
            self.part[(i[1], i[2])].label_4.setText(state)
            self.part[(i[1], i[2])].progressBar.setValue(persent)

    def loro_figure(self):
        '''人物固定按钮点击事件'''
        # tabWidget_2切换到index=2的页面
        self.tabWidget_2.setCurrentIndex(2)
        # tabWidget_5切换到index=3的页面
        self.tabWidget_5.setCurrentIndex(3)

    def pic_review(self):
        '''插图审核按钮点击事件'''
        # tabWidget_2切换到index=2的页面
        self.tabWidget_2.setCurrentIndex(2)
        # tabWidget_5切换到index=1的页面
        self.tabWidget_5.setCurrentIndex(1)

    def rename_program(self):
        '''重命名项目按钮点击事件'''
        # 弹出重命名对话框
        text, ok = QInputDialog.getText(
            self.tab_6, '重命名项目', '请输入新的项目名称:')
        if ok:
            # 判断项目名称是否已存在
            if init.if_project_name_exist(text):
                QMessageBox.warning(
                    self.tab_6, '重命名项目', '项目名称已存在!', QMessageBox.Yes, QMessageBox.Yes)
                return
            # 更新dominate表中的项目名称
            init.update_dominate_name(self.dominate_id, text)
            # 更新项目名称
            self.label_3.setText(text)

    def delete_program(self):
        '''删除项目按钮点击事件'''
        # 弹出确认框
        reply = QMessageBox.question(
            self.tab_6, '删除项目', '确认删除项目?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.No:
            return
        init.delete_program_dir(self.dominate_id)

    def refresh(self):
        '''实时刷新的内容(多项条列)'''
        # 累计消耗的tokens
        data = init.get_program_info(self.dominate_id)
        self.label_5.setText(str(data[3]))

    def __init__(self, mainwin, dominate_id):
        self.dominate_id = dominate_id
        self.mainwin = mainwin

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
        self.verticalLayout_21 = QVBoxLayout(self.tab_7)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
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

        self.horizontalSpacer_3 = QSpacerItem(
            865, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.label_4 = QLabel(self.widget_3)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_5.addWidget(self.label_4)

        self.label_5 = QLabel(self.widget_3)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.verticalLayout_21.addWidget(self.widget_3)

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
        self.pushButton_17.setEnabled(True)

        self.horizontalLayout_6.addWidget(self.pushButton_17)

        self.pushButton_18 = QPushButton(self.widget_4)
        self.pushButton_18.setObjectName(u"pushButton_18")

        self.horizontalLayout_6.addWidget(self.pushButton_18)

        self.pushButton_19 = QPushButton(self.widget_4)
        self.pushButton_19.setObjectName(u"pushButton_19")

        self.horizontalLayout_6.addWidget(self.pushButton_19)

        self.horizontalSpacer_4 = QSpacerItem(
            562, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)

        self.pushButton_4 = QPushButton(self.widget_4)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_6.addWidget(self.pushButton_4)

        self.pushButton_6 = QPushButton(self.widget_4)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.horizontalLayout_6.addWidget(self.pushButton_6)

        self.verticalLayout_21.addWidget(self.widget_4)

        self.groupBox_5 = QGroupBox(self.tab_7)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.widget_5 = QWidget(self.groupBox_5)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.listView = QListView(self.widget_5)
        self.listView.setObjectName(u"listView")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(2)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(
            self.listView.sizePolicy().hasHeightForWidth())
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
        sizePolicy4.setHeightForWidth(
            self.frame_4.sizePolicy().hasHeightForWidth())
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
        sizePolicy5.setHeightForWidth(
            self.scrollArea_2.sizePolicy().hasHeightForWidth())
        self.scrollArea_2.setSizePolicy(sizePolicy5)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(
            u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 888, 381))
        self.verticalLayout_20 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_5.addWidget(self.scrollArea_2)

        self.horizontalLayout_7.addWidget(self.frame_4)

        self.verticalLayout_6.addWidget(self.widget_5)

        self.verticalLayout_21.addWidget(self.groupBox_5)

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
        self.scrollAreaWidgetContents_3.setObjectName(
            u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 1124, 487))
        self.verticalLayout_22 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
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
        self.scrollAreaWidgetContents_4.setObjectName(
            u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 1124, 487))
        self.verticalLayout_23 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)

        self.horizontalLayout_18.addWidget(self.scrollArea_4)

        self.tabWidget_3.addTab(self.tab_13, "")
        self.tab_14 = QWidget()
        self.tab_14.setObjectName(u"tab_14")
        self.verticalLayout_7 = QVBoxLayout(self.tab_14)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_6 = QLabel(self.tab_14)
        self.label_6.setObjectName(u"label_6")

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

        self.horizontalSpacer_5 = QSpacerItem(
            883, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

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
        self.horizontalSpacer_7 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_7)

        self.pushButton_20 = QPushButton(self.widget_7)
        self.pushButton_20.setObjectName(u"pushButton_20")

        self.horizontalLayout_10.addWidget(self.pushButton_20)

        self.horizontalSpacer_6 = QSpacerItem(
            301, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_6)

        self.pushButton_21 = QPushButton(self.widget_7)
        self.pushButton_21.setObjectName(u"pushButton_21")

        self.horizontalLayout_10.addWidget(self.pushButton_21)

        self.horizontalSpacer_8 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

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
        self.horizontalSpacer_9 = QSpacerItem(
            401, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_9)

        self.pushButton_22 = QPushButton(self.widget_8)
        self.pushButton_22.setObjectName(u"pushButton_22")

        self.horizontalLayout_11.addWidget(self.pushButton_22)

        self.horizontalSpacer_10 = QSpacerItem(
            401, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

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
        self.scrollAreaWidgetContents_5.setObjectName(
            u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 1124, 487))
        self.verticalLayout_24 = QVBoxLayout(self.scrollAreaWidgetContents_5)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
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
        self.horizontalSpacer_17 = QSpacerItem(
            208, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_17)

        self.label_18 = QLabel(self.widget_14)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_21.addWidget(self.label_18)

        self.label_19 = QLabel(self.widget_14)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_21.addWidget(self.label_19)

        self.horizontalSpacer_16 = QSpacerItem(
            209, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_16)

        self.label_16 = QLabel(self.widget_14)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_21.addWidget(self.label_16)

        self.label_17 = QLabel(self.widget_14)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_21.addWidget(self.label_17)

        self.horizontalSpacer_15 = QSpacerItem(
            208, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_15)

        self.checkBox_2 = QCheckBox(self.widget_14)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.horizontalLayout_21.addWidget(self.checkBox_2)

        self.horizontalSpacer_14 = QSpacerItem(
            208, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

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

        self.horizontalSpacer_18 = QSpacerItem(
            1021, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

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

        self.horizontalSpacer_19 = QSpacerItem(
            1009, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_19)

        self.verticalLayout_11.addWidget(self.widget_16)

        self.widget_17 = QWidget(self.frame_5)
        self.widget_17.setObjectName(u"widget_17")
        self.horizontalLayout_24 = QHBoxLayout(self.widget_17)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_24 = QLabel(self.widget_17)
        self.label_24.setObjectName(u"label_24")

        self.horizontalLayout_24.addWidget(self.label_24)

        self.horizontalSpacer_20 = QSpacerItem(
            1009, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_20)

        self.verticalLayout_11.addWidget(self.widget_17)

        self.label_25 = QLabel(self.frame_5)
        self.label_25.setObjectName(u"label_25")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(
            self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy6)

        self.verticalLayout_11.addWidget(self.label_25)

        self.widget_18 = QWidget(self.frame_5)
        self.widget_18.setObjectName(u"widget_18")
        self.horizontalLayout_25 = QHBoxLayout(self.widget_18)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalSpacer_21 = QSpacerItem(
            304, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_21)

        self.pushButton_25 = QPushButton(self.widget_18)
        self.pushButton_25.setObjectName(u"pushButton_25")

        self.horizontalLayout_25.addWidget(self.pushButton_25)

        self.horizontalSpacer_22 = QSpacerItem(
            305, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_22)

        self.pushButton_26 = QPushButton(self.widget_18)
        self.pushButton_26.setObjectName(u"pushButton_26")
        self.pushButton_26.setCursor(QCursor(Qt.ArrowCursor))

        self.horizontalLayout_25.addWidget(self.pushButton_26)

        self.horizontalSpacer_23 = QSpacerItem(
            304, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

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
        self.scrollAreaWidgetContents_6.setObjectName(
            u"scrollAreaWidgetContents_6")
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, 0, 1124, 487))
        self.verticalLayout_25 = QVBoxLayout(self.scrollAreaWidgetContents_6)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
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

        self.horizontalSpacer_39 = QSpacerItem(
            1024, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_50.addItem(self.horizontalSpacer_39)

        self.verticalLayout_19.addWidget(self.widget_39)

        self.scrollArea_10 = QScrollArea(self.tab_23)
        self.scrollArea_10.setObjectName(u"scrollArea_10")
        self.scrollArea_10.setWidgetResizable(True)
        self.scrollAreaWidgetContents_10 = QWidget()
        self.scrollAreaWidgetContents_10.setObjectName(
            u"scrollAreaWidgetContents_10")
        self.scrollAreaWidgetContents_10.setGeometry(QRect(0, 0, 1124, 440))
        self.verticalLayout_26 = QVBoxLayout(self.scrollAreaWidgetContents_10)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
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
        self.scrollAreaWidgetContents_7.setObjectName(
            u"scrollAreaWidgetContents_7")
        self.scrollAreaWidgetContents_7.setGeometry(QRect(0, 0, 1124, 487))
        self.verticalLayout_27 = QVBoxLayout(self.scrollAreaWidgetContents_7)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
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
        self.scrollAreaWidgetContents_8.setObjectName(
            u"scrollAreaWidgetContents_8")
        self.scrollAreaWidgetContents_8.setGeometry(QRect(0, 0, 1124, 487))
        self.verticalLayout_28 = QVBoxLayout(self.scrollAreaWidgetContents_8)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.scrollArea_8.setWidget(self.scrollAreaWidgetContents_8)

        self.horizontalLayout_29.addWidget(self.scrollArea_8)

        self.tabWidget_6.addTab(self.tab_22, "")

        self.horizontalLayout_27.addWidget(self.tabWidget_6)

        self.tabWidget_2.addTab(self.tab_10, "")
        self.widget1 = QWidget()
        self.widget1.setObjectName(u"widget1")
        self.verticalLayout_29 = QVBoxLayout(self.widget1)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.tabWidget_7 = QTabWidget(self.widget1)
        self.tabWidget_7.setObjectName(u"tabWidget_7")
        self.tab_24 = QWidget()
        self.tab_24.setObjectName(u"tab_24")
        self.verticalLayout_31 = QVBoxLayout(self.tab_24)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.scrollArea_12 = QScrollArea(self.tab_24)
        self.scrollArea_12.setObjectName(u"scrollArea_12")
        self.scrollArea_12.setWidgetResizable(True)
        self.scrollAreaWidgetContents_12 = QWidget()
        self.scrollAreaWidgetContents_12.setObjectName(
            u"scrollAreaWidgetContents_12")
        self.scrollAreaWidgetContents_12.setGeometry(QRect(0, 0, 1124, 487))
        self.verticalLayout_32 = QVBoxLayout(self.scrollAreaWidgetContents_12)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.scrollArea_12.setWidget(self.scrollAreaWidgetContents_12)

        self.verticalLayout_31.addWidget(self.scrollArea_12)

        self.tabWidget_7.addTab(self.tab_24, "")
        self.tab_25 = QWidget()
        self.tab_25.setObjectName(u"tab_25")
        self.verticalLayout_30 = QVBoxLayout(self.tab_25)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.scrollArea_11 = QScrollArea(self.tab_25)
        self.scrollArea_11.setObjectName(u"scrollArea_11")
        self.scrollArea_11.setWidgetResizable(True)
        self.scrollAreaWidgetContents_11 = QWidget()
        self.scrollAreaWidgetContents_11.setObjectName(
            u"scrollAreaWidgetContents_11")
        self.scrollAreaWidgetContents_11.setGeometry(QRect(0, 0, 1124, 487))
        self.verticalLayout_33 = QVBoxLayout(self.scrollAreaWidgetContents_11)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.scrollArea_11.setWidget(self.scrollAreaWidgetContents_11)

        self.verticalLayout_30.addWidget(self.scrollArea_11)

        self.tabWidget_7.addTab(self.tab_25, "")

        self.verticalLayout_29.addWidget(self.tabWidget_7)

        self.tabWidget_2.addTab(self.widget1, "")

        self.horizontalLayout_4.addWidget(self.tabWidget_2)

        mainwin.tabWidget.addTab(self.tab_6, "")

        # 设置文字
        self.label_2.setText(QCoreApplication.translate(
            "MainWindow", u"\u9879\u76ee\u540d\u79f0\uff1a", None))
        self.label_3.setText(QCoreApplication.translate(
            "MainWindow", u"????", None))
        self.label_4.setText(QCoreApplication.translate(
            "MainWindow", u"\u7d2f\u8ba1\u6d88\u8017ChatGPT Tokens:", None))
        self.label_5.setText(
            QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_15.setText(QCoreApplication.translate(
            "MainWindow", u"\u5220\u9664\u9879\u76ee", None))
        self.pushButton_16.setText(QCoreApplication.translate(
            "MainWindow", u"\u65b0\u589e\u7ae0\u8282", None))
        self.pushButton_17.setText(QCoreApplication.translate(
            "MainWindow", u"\u6682\u505c\u6240\u6709", None))
        self.pushButton_18.setText(QCoreApplication.translate(
            "MainWindow", u"\u7ee7\u7eed\u6240\u6709", None))
        self.pushButton_19.setText(QCoreApplication.translate(
            "MainWindow", u"\u91cd\u547d\u540d", None))
        self.pushButton_4.setText(QCoreApplication.translate(
            "MainWindow", u"\u4eba\u7269\u56fa\u5b9a", None))
        self.pushButton_6.setText(QCoreApplication.translate(
            "MainWindow", u"\u63d2\u56fe\u5ba1\u6838", None))
        self.groupBox_5.setTitle(QCoreApplication.translate(
            "MainWindow", u"\u5206\u955c\u4fe1\u606f(\u82e5\u65e0\u5185\u5bb9\u8bf7\u5148\u5207\u5206\u955c)", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(
            self.tab_7), QCoreApplication.translate("MainWindow", u"\u4e3b\u4fe1\u606f", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(
            self.tab_12), QCoreApplication.translate("MainWindow", u"\u672a\u5b8c\u6210", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(
            self.tab_13), QCoreApplication.translate("MainWindow", u"\u5df2\u5b8c\u6210", None))
        self.label_6.setText(QCoreApplication.translate(
            "MainWindow", u"\u521b\u5efa\u5206\u955c", None))
        self.label_7.setText(QCoreApplication.translate(
            "MainWindow", u"\u72b6\u6001:", None))
        self.label_8.setText(QCoreApplication.translate(
            "MainWindow", u"\u672a\u5f00\u59cb", None))
        self.label_9.setText(QCoreApplication.translate(
            "MainWindow", u"(\u6e29\u99a8\u63d0\u9192:\u4e00\u884c\u4e00\u955c)", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                         "p, li { white-space: pre-wrap; }\n"
                                                         "</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u5206\u955c\u5185\u5bb9\u4e8e\u6b64\u663e\u793a\u6216\u4fee\u6539</p></body></html>", None))
        self.pushButton_20.setText(QCoreApplication.translate(
            "MainWindow", u"\u5f00\u59cbAI\u5206\u955c", None))
        self.pushButton_21.setText(QCoreApplication.translate(
            "MainWindow", u"\u63d0\u4ea4", None))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(
            self.tab_15), QCoreApplication.translate("MainWindow", u"AI\u5206\u955c", None))
        self.label_10.setText(QCoreApplication.translate(
            "MainWindow", u"\u6e29\u99a8\u63d0\u9192:\u4e00\u884c\u4e00\u955c", None))
        self.pushButton_22.setText(QCoreApplication.translate(
            "MainWindow", u"\u63d0\u4ea4", None))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(
            self.tab_16), QCoreApplication.translate("MainWindow", u"\u4eba\u5de5\u5206\u955c", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_14), QCoreApplication.translate(
            "MainWindow", u"\u9009\u62e9\u9875(\u9690\u85cf)", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(
            self.tab_8), QCoreApplication.translate("MainWindow", u"\u5207\u5206\u955c", None))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(
            self.tab_18), QCoreApplication.translate("MainWindow", u"\u672a\u5b8c\u6210", None))
        self.label_18.setText(QCoreApplication.translate(
            "MainWindow", u"\u5171\u9700\u5ba1\u6838:", None))
        self.label_19.setText(
            QCoreApplication.translate("MainWindow", u"0", None))
        self.label_16.setText(QCoreApplication.translate(
            "MainWindow", u"\u672c\u6b21\u5269\u4f59\u5ba1\u6838:", None))
        self.label_17.setText(
            QCoreApplication.translate("MainWindow", u"0", None))
        self.checkBox_2.setText(QCoreApplication.translate(
            "MainWindow", u"\u65e0\u9700\u5ba1\u6838", None))
        self.label_20.setText(QCoreApplication.translate(
            "MainWindow", u"\u63d0\u793a\u8bcd:", None))
        self.label_21.setText(
            QCoreApplication.translate("MainWindow", u"???", None))
        self.label_22.setText(QCoreApplication.translate(
            "MainWindow", u"\u5206\u955c\u539f\u6587:", None))
        self.label_23.setText(
            QCoreApplication.translate("MainWindow", u"???", None))
        self.label_24.setText(QCoreApplication.translate(
            "MainWindow", u"\u7b2cx\u7ae0 \u7b2cx\u90e8\u5206", None))
        self.label_25.setText(
            QCoreApplication.translate("MainWindow", u"PIC", None))
        self.pushButton_25.setText(QCoreApplication.translate(
            "MainWindow", u"\u901a\u8fc7(Space)", None))
        self.pushButton_26.setText(QCoreApplication.translate(
            "MainWindow", u"\u4e0d\u901a\u8fc7(F)", None))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(
            self.tab_19), QCoreApplication.translate("MainWindow", u"\u5f85\u5ba1\u6838", None))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(
            self.tab_20), QCoreApplication.translate("MainWindow", u"\u5df2\u5b8c\u6210", None))
        self.pushButton_5.setText(QCoreApplication.translate(
            "MainWindow", u"\u6dfb\u52a0", None))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(
            self.tab_23), QCoreApplication.translate("MainWindow", u"\u4eba\u7269\u56fa\u5b9a", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(
            self.tab_9), QCoreApplication.translate("MainWindow", u"\u63d2\u56fe\u751f\u6210", None))
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(
            self.tab_21), QCoreApplication.translate("MainWindow", u"\u672a\u5b8c\u6210", None))
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(
            self.tab_22), QCoreApplication.translate("MainWindow", u"\u5df2\u5b8c\u6210", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(
            self.tab_10), QCoreApplication.translate("MainWindow", u"\u914d\u97f3\u751f\u6210", None))
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(
            self.tab_24), QCoreApplication.translate("MainWindow", u"\u672a\u5b8c\u6210", None))
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(
            self.tab_25), QCoreApplication.translate("MainWindow", u"\u5df2\u5b8c\u6210", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(
            self.widget1), QCoreApplication.translate("MainWindow", u"\u89c6\u9891\u751f\u6210", None))


class Part_info(QFrame):
    '''主信息--分镜信息'''

    def __init__(self, mainwin: object, my_one_program: object, chapter: int, part: int):
        super().__init__()
        self.chapter = chapter
        self.part = part
        self.mainwin = mainwin
        self.my_one_program = my_one_program

        self.setObjectName(u"frame")
        self.setMaximumSize(QSize(16777215, 121))
        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(self)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.horizontalSpacer = QSpacerItem(
            658, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4)

        self.verticalLayout.addWidget(self.widget)

        self.progressBar = QProgressBar(self.frame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.verticalLayout.addWidget(self.progressBar)

        self.label.setText(QCoreApplication.translate(
            "Form", u"\u5206\u955c", None))
        self.label_2.setText(QCoreApplication.translate(
            "Form", str(self.part), None))
        self.label_3.setText(QCoreApplication.translate(
            "Form", u"\u6b63\u5728\u8fdb\u884c\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"???", None))


class part_undone(QFrame):
    '''切分镜--未完成'''

    def init_other(self):
        '''初始化其他'''
        self.pushButton.clicked.connect(self.create_part)

    def create_part(self):
        '''创建分镜,开始按钮点击事件'''
        #确认AI分镜是否启动
        if self.my_one_program.if_ai_screenshot:
            # 将页面切换到index=2
            self.my_one_program.tabWidget_3.setCurrentIndex(2)
            QMessageBox.information(self, '提示', 'AI智能分镜已经在运行中,请等待上个AI智能分镜结束后才能进行新的分镜任务', QMessageBox.Ok)
            return
        # 将页面切换到index=2
        self.my_one_program.tabWidget_3.setCurrentIndex(2)
        # 设置AI分镜开始按钮点击事件
        self.my_one_program.pushButton_20.clicked.connect(
            lambda: self.my_one_program.start_ai_screenshot(self.chapter))

        origin_text = init.get_original_content(self.my_one_program.path, self.chapter)
        #人工分镜中显示原文内容
        self.my_one_program.textEdit_2.setPlainText(origin_text)

    def __init__(self, mainwin: object, my_one_program: object, chapter: int):
        self.mainwin = mainwin
        self.my_one_program = my_one_program
        self.chapter = chapter

        super().__init__()
        self.setObjectName(u"frame")
        self.setMaximumSize(QSize(16777215, 81))
        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(
            469, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_2 = QLabel(self)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.pushButton = QPushButton(self)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.label.setText(QCoreApplication.translate(
            "Form", u"\u7b2cN\u7ae0", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"???", None))
        self.label_3.setText(
            QCoreApplication.translate("Form", u"\u5b57", None))
        self.pushButton.setText(QCoreApplication.translate(
            "Form", u"\u5f00\u59cb", None))


class part_done(QFrame):
    '''切分镜--已完成'''

    def __init__(self, mainwin: object, my_one_program: object, chapter: int):
        self.mainwin = mainwin
        self.my_one_program = my_one_program
        self.chapter = chapter

        super().__init__()
        self.setObjectName(u"frame")
        self.setMaximumSize(QSize(16777215, 81))
        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(
            213, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_2 = QLabel(self)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(self)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4)

        self.label_5 = QLabel(self)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout.addWidget(self.label_5)

        self.pushButton = QPushButton(self)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.label.setText(QCoreApplication.translate(
            "Form", u"\u7b2cN\u7ae0", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"???", None))
        self.label_3.setText(
            QCoreApplication.translate("Form", u"\u5b57", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"???", None))
        self.label_5.setText(QCoreApplication.translate(
            "Form", u"\u4e2a\u5206\u955c", None))
        self.pushButton.setText(QCoreApplication.translate(
            "Form", u"\u91cd\u65b0\u5206\u955c", None))
