import sys

from Interface import *
from png import *
from PyQt5.QtCore import QSize, Qt
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QHBoxLayout, QPushButton, QAbstractItemView, QTableView, QVBoxLayout, QSplitter, \
    QApplication, QGroupBox, QLabel, QGridLayout, QLineEdit, QComboBox, QTextEdit, QCheckBox,QVBoxLayout,QListView
from PyQt5.QtWidgets import QListWidget, QStackedWidget, QFrame
from PyQt5.QtWidgets import QListWidgetItem, QSizePolicy
from PyQt5.QtWidgets import QWidget, QSpacerItem, QHeaderView
from top import Top
import qtawesome




class magicPillWindow(QWidget):
    '''左侧选项栏'''

    def __init__(self):
        super(magicPillWindow, self).__init__()
        self.screenRect = QApplication.desktop().screenGeometry()
        self.width = self.screenRect.width()
        self.height = self.screenRect.height()
        if self.width == 2560 and self.height == 1440:
            self.resize(960, 640)
        elif self.width == 1920 and self.height == 1080:
            self.resize(960, 640)
        elif self.width == 1440 and self.height == 900:
            self.resize(860, 540)
        elif self.width == 1024 and self.height == 768:
            self.resize(800, 520)
        else:
            self.resize(960, 640)
        self.lis_name = ['任务', '代理', '账号', '折扣码', '礼品卡', '地址', '订单']

        self.lis_win = [taskWindow(), agentWindow(), accountWindow(), discountWindow(), giftWindow(), addressWindow(),
                        orderWindow()]

        # self.setFixedSize(self.width(), self.height())

        self.main_layout = QVBoxLayout(self, spacing = 0)  # 窗口的整体布局

        self.left_widget_ = Top()  # 左侧选项列表
        self.left_widget_.pushButton_2.clicked.connect(self.close)
        self.left_widget_.pushButton.clicked.connect(self.showMinimized)
        # self.verticalLayout = QHBoxLayout(self.left_widget_)
        # spacerItem = QSpacerItem(20, 125, QSizePolicy.Minimum, QSizePolicy.Expanding)
        # self.verticalLayout.addItem(spacerItem)
        # self.left_widget = self.left_widget_.listWidget
        self.setAttribute(Qt.WA_TranslucentBackground) # 设置窗口背景透明
        self.setWindowFlag(Qt.FramelessWindowHint)
        # font = QtGui.QFont()
        # font.setFamily("Microsoft YaHei") #括号里可以设置成自己想要的其它字体
        # font.setPointSize(10)   #括号里的数字可以设置成自己想要的字体大小
        # self.left_widget.setFont(font)
        self.main_layout.addWidget(self.left_widget_)

        self.right_widget = QStackedWidget()
        self.main_layout.addWidget(self.right_widget)

        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.right_widget.layout().setSpacing(0)
        self.right_widget.layout().setContentsMargins(0, 0, 0, 0)

        self.main_layout.setStretch(0,1)
        self.main_layout.setStretch(1,14)

        minimizeAction = QtWidgets.QAction("最小化至托盘", self, triggered=self.hide)
        restoreAction = QtWidgets.QAction("还原", self,
                                triggered=self.showNormal)
        quitAction = QtWidgets.QAction("退出", self,
                                triggered=self.close)
        self.trayIconMenu = QtWidgets.QMenu(self)
        self.trayIconMenu.addAction(minimizeAction)
        self.trayIconMenu.addAction(restoreAction)
        self.trayIconMenu.addSeparator()
        self.trayIconMenu.addAction(quitAction)
        self.trayIcon = QtWidgets.QSystemTrayIcon(self)
        self.trayIcon.setIcon(QtGui.QIcon(":/static/2.jpg"))
        self.trayIcon.setContextMenu(self.trayIconMenu)
        self.trayIcon.show()

        self._setup_ui()
        self.setQss()

    def mouseMoveEvent(self, e: QtGui.QMouseEvent):  # 重写移动事件
        try:
            self._endPos = e.pos() - self._startPos
            self.move(self.pos() + self._endPos)
        except:
            pass

    def mousePressEvent(self, e: QtGui.QMouseEvent):
        if e.button() == QtCore.Qt.LeftButton:
            self._isTracking = True
            self._startPos = QtCore.QPoint(e.x(), e.y())

    def mouseReleaseEvent(self, e: QtGui.QMouseEvent):
        if e.button() == QtCore.Qt.LeftButton:
            self._isTracking = False
            self._startPos = None
            self._endPos = None

    def clearButton(self):
        self.left_widget_.pushButton_4.setChecked(False)
        self.left_widget_.pushButton_10.setChecked(False)
        self.left_widget_.pushButton_9.setChecked(False)
        self.left_widget_.pushButton_8.setChecked(False)
        self.left_widget_.pushButton_7.setChecked(False)
        self.left_widget_.pushButton_6.setChecked(False)
        self.left_widget_.pushButton_5.setChecked(False)
        self.left_widget_.pushButton_4.setDown(False)
        self.left_widget_.pushButton_10.setDown(False)
        self.left_widget_.pushButton_9.setDown(False)
        self.left_widget_.pushButton_8.setDown(False)
        self.left_widget_.pushButton_7.setDown(False)
        self.left_widget_.pushButton_6.setDown(False)
        self.left_widget_.pushButton_5.setDown(False)
        # self.left_widget_.pushButton_4.clicked.connect(lambda:self.left_widget_.pushButton_4.setDown(True))
        self.left_widget_.pushButton_4.setIcon(QIcon(':/static/task.png'))
        # self.left_widget_.pushButton_10.clicked.connect(lambda:self.left_widget_.pushButton_10.setDown(True))
        self.left_widget_.pushButton_10.setIcon(QIcon(':/static/agent.png'))
        # self.left_widget_.pushButton_9.clicked.connect(lambda:self.left_widget_.pushButton_9.setDown(True))
        self.left_widget_.pushButton_9.setIcon(QIcon(':/static/account.png'))
        # self.left_widget_.pushButton_8.clicked.connect(lambda:self.left_widget_.pushButton_8.setDown(True))
        self.left_widget_.pushButton_8.setIcon(QIcon(':/static/code.png'))
        # self.left_widget_.pushButton_7.clicked.connect(lambda:self.left_widget_.pushButton_7.setDown(True))
        self.left_widget_.pushButton_7.setIcon(QIcon(':/static/gift.png'))
        # self.left_widget_.pushButton_6.clicked.connect(lambda:self.left_widget_.pushButton_6.setDown(True))
        self.left_widget_.pushButton_6.setIcon(QIcon(':/static/order.png'))
        # self.left_widget_.pushButton_5.clicked.connect(lambda:self.left_widget_.pushButton_5.setDown(True))
        self.left_widget_.pushButton_5.setIcon(QIcon(':/static/address.png'))


    def _setup_ui(self):
        '''加载界面ui'''

        self.left_widget_.pushButton_4.clicked.connect(lambda:self.right_widget.setCurrentIndex(0))  # list和右侧窗口的index对应绑定
        self.left_widget_.pushButton_10.clicked.connect(lambda:self.right_widget.setCurrentIndex(1))
        self.left_widget_.pushButton_9.clicked.connect(lambda:self.right_widget.setCurrentIndex(2))
        self.left_widget_.pushButton_8.clicked.connect(lambda:self.right_widget.setCurrentIndex(3))
        self.left_widget_.pushButton_7.clicked.connect(lambda:self.right_widget.setCurrentIndex(4))
        self.left_widget_.pushButton_5.clicked.connect(lambda:self.right_widget.setCurrentIndex(5))
        self.left_widget_.pushButton_6.clicked.connect(lambda:self.right_widget.setCurrentIndex(6))

        self.left_widget_.pushButton_4.clicked.connect(self.clearButton)
        self.left_widget_.pushButton_10.clicked.connect(self.clearButton)
        self.left_widget_.pushButton_9.clicked.connect(self.clearButton)
        self.left_widget_.pushButton_8.clicked.connect(self.clearButton)
        self.left_widget_.pushButton_7.clicked.connect(self.clearButton)
        self.left_widget_.pushButton_6.clicked.connect(self.clearButton)
        self.left_widget_.pushButton_5.clicked.connect(self.clearButton)

        self.left_widget_.pushButton_4.setCheckable(True)
        self.left_widget_.pushButton_10.setCheckable(True)
        self.left_widget_.pushButton_9.setCheckable(True)
        self.left_widget_.pushButton_8.setCheckable(True)
        self.left_widget_.pushButton_7.setCheckable(True)
        self.left_widget_.pushButton_6.setCheckable(True)
        self.left_widget_.pushButton_5.setCheckable(True)

        self.left_widget_.pushButton_4.setChecked(True)
        self.left_widget_.pushButton_4.setDown(True)
        self.left_widget_.pushButton_4.setIcon(QIcon(':/static/taskh.png'))

        self.left_widget_.pushButton_4.setAutoExclusive(True)
        self.left_widget_.pushButton_10.setAutoExclusive(True)
        self.left_widget_.pushButton_9.setAutoExclusive(True)
        self.left_widget_.pushButton_8.setAutoExclusive(True)
        self.left_widget_.pushButton_7.setAutoExclusive(True)
        self.left_widget_.pushButton_6.setAutoExclusive(True)
        self.left_widget_.pushButton_5.setAutoExclusive(True)

        self.left_widget_.pushButton_4.clicked.connect(lambda:self.left_widget_.pushButton_4.setChecked(True))
        self.left_widget_.pushButton_10.clicked.connect(lambda:self.left_widget_.pushButton_10.setChecked(True))
        self.left_widget_.pushButton_9.clicked.connect(lambda:self.left_widget_.pushButton_9.setChecked(True))
        self.left_widget_.pushButton_8.clicked.connect(lambda:self.left_widget_.pushButton_8.setChecked(True))
        self.left_widget_.pushButton_7.clicked.connect(lambda:self.left_widget_.pushButton_7.setChecked(True))
        self.left_widget_.pushButton_6.clicked.connect(lambda:self.left_widget_.pushButton_6.setChecked(True))
        self.left_widget_.pushButton_5.clicked.connect(lambda:self.left_widget_.pushButton_5.setChecked(True))

        self.left_widget_.pushButton_4.clicked.connect(lambda:self.left_widget_.pushButton_4.setDown(True))
        self.left_widget_.pushButton_4.clicked.connect(lambda:self.left_widget_.pushButton_4.setIcon(QIcon(':/static/taskh.png')))
        self.left_widget_.pushButton_10.clicked.connect(lambda:self.left_widget_.pushButton_10.setDown(True))
        self.left_widget_.pushButton_10.clicked.connect(lambda:self.left_widget_.pushButton_10.setIcon(QIcon(':/static/agenth.png')))
        self.left_widget_.pushButton_9.clicked.connect(lambda:self.left_widget_.pushButton_9.setDown(True))
        self.left_widget_.pushButton_9.clicked.connect(lambda:self.left_widget_.pushButton_9.setIcon(QIcon(':/static/accounth.png')))
        self.left_widget_.pushButton_8.clicked.connect(lambda:self.left_widget_.pushButton_8.setDown(True))
        self.left_widget_.pushButton_8.clicked.connect(lambda:self.left_widget_.pushButton_8.setIcon(QIcon(':/static/codeh.png')))
        self.left_widget_.pushButton_7.clicked.connect(lambda:self.left_widget_.pushButton_7.setDown(True))
        self.left_widget_.pushButton_7.clicked.connect(lambda:self.left_widget_.pushButton_7.setIcon(QIcon(':/static/gifth.png')))
        self.left_widget_.pushButton_6.clicked.connect(lambda:self.left_widget_.pushButton_6.setDown(True))
        self.left_widget_.pushButton_6.clicked.connect(lambda:self.left_widget_.pushButton_6.setIcon(QIcon(':/static/orderh.png')))
        self.left_widget_.pushButton_5.clicked.connect(lambda:self.left_widget_.pushButton_5.setDown(True))
        self.left_widget_.pushButton_5.clicked.connect(lambda:self.left_widget_.pushButton_5.setIcon(QIcon(':/static/addressh.png')))


        # self.left_widget.setFrameShape(QListWidget.NoFrame)  # 去掉边框

        # self.left_widget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)  # 隐藏滚动条
        # self.left_widget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        for i in range(len(self.lis_name)):
            # print(self.lis_name[i])
            # self.item = QListWidgetItem(
            #     self.lis_name[i],
            #     self.left_widget
            # )  # 左侧选项的添加
            # self.item.setSizeHint(QSize(30, 60))
            # self.item.setTextAlignment(Qt.AlignCenter)  # 居中显示
            self.right_widget.addWidget(self.lis_win[i])

    def setQss(self):
        self.setStyleSheet('''QStackedWidget{background : #181922;}



        QTableView{

        border:none;

        background-color: #181922; 

        alternate-background-color:#e3edf9;

        font:14px "PingFangSC-Regular";

        color:#677483;}

        QHeaderView::section{

        color: #777777;

        font-size: 16px;

        font-family: "PingFangSC-Regular";

        font-weight: 400;

        text-align:center;

        height:32px;

        background-color: #181922;

        border:none;

        outline:none} 

        QTableView::item{

        border : none;

        margin-bottom:4px;

        margin-top:4px;

        background: #21232f;

        font-family: "PingFangSC-Regular";

        }''')


class taskWindow(QWidget):
    """任务窗口"""

    def __init__(self):
        super().__init__()
        # self.resize(960, 400)
        # self.setFixedSize(self.width(), self.height())


        # 表模型
        self.queryModel = None

        # 数据表
        self.tableView = None

        self.dic = {
            'header': ['ID', '地区', '货号', '尺码', '数量', '账户', '代理','状态','操作'],
            'data': [[1,1,1,1,1,1,1,1,1], [2,2,2,2,2,2,2,2,2]]
        }

        self.add_btn = QPushButton(QIcon(':/static/add.png'),'添加任务',self)  # 添加任务按钮
        self.add_btn.setIconSize(QSize(10, 10))
        self.add_btn.setStyleSheet('''width: 100px;

            height: 30px; 

            border-radius: 6px;

            color: #ffffff;

            font-family: "PingFangSC-Medium";

            font-size: 12px;

            font-weight: 400;

            line-height: 16px;

            background: qlineargradient(x1:0, y1:1, x2:0, y2:1,stop:0 #3EC169,stop:1 #1BBB70);''')
        self.start_btn = QPushButton(QIcon(':/static/start.png'),'开始所有',self)  # 开始所有按钮

        # self.start_btn.setIconSize(QSize(13, 13))
        self.start_btn.setStyleSheet('''width: 100px;

            height: 30px; 

            border-radius: 6px;

            color: #ffffff;

            font-family: "PingFangSC-Medium";

            font-size: 12px;

            font-weight: 400;

            line-height: 16px;

            background: qlineargradient(x1:0, y1:1, x2:0, y2:1,stop:0 #3EC169,stop:1 #1BBB70);''')
        self.stop_btn = QPushButton(QIcon(':/static/pause.png'),'停止所有',self)  # 停止所有按钮
        self.stop_btn.setStyleSheet('''width: 100px;

            height: 30px; 

            border-radius: 6px;

            color: #ffffff;

            font-family: "PingFangSC-Medium";

            font-size: 12px;

            font-weight: 400;

            line-height: 16px;

            background: #5c5858;''')
        self.delete_btn = QPushButton(QIcon(':/static/delete.png'),'删除所有',self)  # 删除所有按钮
        self.delete_btn.setStyleSheet('''width: 100px;

            height: 30px; 

            border-radius: 6px;

            color: #ffffff;

            font-family: "PingFangSC-Medium";

            font-size: 12px;

            font-weight: 400;

            line-height: 16px;

            background: #ff6d6d;''')
        # self.btn = QPushButton('+')  # +按钮

        self.add_btn.clicked.connect(self.add_action)
        self.start_btn.clicked.connect(self.start_action)
        self.stop_btn.clicked.connect(self.stop_action)
        self.delete_btn.clicked.connect(self.delete_action)
        # self.btn.clicked.connect(self.add_action)

        # 软件中的表
        self.tableView = MyTableView()  # 用的是自己重写的tableview，在querymodel中查看,这里被改动
        self.tableView.verticalHeader().setDefaultSectionSize(40)
        self.tableView.setShowGrid(False)
        self.tableView.verticalHeader().hide()
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.queryModel = myTableModel(self.dic['header'], self.dic['data'])
        self.tableView.setModel(self.queryModel)

        # self.tableView.ColumnWidth()

        self.tableView.setColumnWidth(0, 77)
        self.tableView.setColumnWidth(1, 77)
        self.tableView.setColumnWidth(2, 255)
        self.tableView.setColumnWidth(3, 60)
        self.tableView.setColumnWidth(4, 77)
        self.tableView.setColumnWidth(5, 77)
        self.tableView.setColumnWidth(6, 90)
        self.tableView.setColumnWidth(7, 90)
        self.tableView.setColumnWidth(8, 111)


        self.layout = QVBoxLayout(self)
        self.h1 = QHBoxLayout()
        self.h1.addWidget(self.add_btn)
        # self.h1.addWidget(self.btn)
        self.h1.addWidget(QSplitter())
        self.h1.addWidget(self.start_btn)
        self.h1.addWidget(self.stop_btn)
        self.h1.addWidget(self.delete_btn)
        # self.layout.addWidget(QSplitter())
        # self.setLayout(self.layout)
        self.widget = QWidget()
        self.widget.setLayout(self.h1)
        self.widget.setStyleSheet('''background : #1e1f29;''')
        self.layout.addWidget(QSplitter())
        self.h2 = QVBoxLayout()
        self.h2.addWidget(self.tableView)
        self.layout.addLayout(self.h2)
        self.layout.addWidget(self.widget)
        self.layout.setStretch(0,1)
        self.layout.setStretch(1,9)
        self.layout.setStretch(2,1)
        self.layout.setStretch(3,3)
        self.layout.setContentsMargins(0, 0, 0, 0)
        # self.h1.setSpacing(8)
        self.h1.setContentsMargins(10, 10, 10, 10)
        self.h2.setContentsMargins(15, 15, 15, 15)

    def add_action(self):
        self.win = addTaskWindow()
        self.win.setWindowModality(Qt.ApplicationModal)
        self.win.show()

    def start_action(self):
        TaskFunc.start_action(self)

    def stop_action(self):
        TaskFunc.stop_action(self)

    def delete_action(self):
        TaskFunc.delete_action(self)


class agentWindow(QWidget):
    """代理窗口"""

    def __init__(self):
        super().__init__()
        # self.resize(960, 540)
        # self.setFixedSize(self.width(), self.height())

        # 表模型
        self.queryModel = None

        # 数据表
        self.tableView = None

        self.dic = {
            'header': ['ID', '名称', '数量', '操作'],
            'data': [[1,1,1,1], [2,2,2,2],[2,2,2,2],[2,2,2,2],[2,2,2,2],[2,2,2,2],[2,2,2,2],[2,2,2,2],[2,2,2,2],[2,2,2,2],[2,2,2,2],[2,2,2,2]]
        }

        self.add_btn = QPushButton(QIcon(':/static/add.png'),'添加代理')  # 添加代理按钮
        self.add_btn.setIconSize(QSize(10, 10))
        self.delete_btn = QPushButton(QIcon(':/static/delete.png'),'删除所有')  # 删除所有按钮
        # self.btn = QPushButton('+')  # +按钮

        self.add_btn.clicked.connect(self.add_action)
        self.delete_btn.clicked.connect(self.delete_action)
        # self.btn.clicked.connect(self.add_action)

        # 软件中的表
        self.tableView = MyTableView1()  # 用的是自己重写的tableview，在querymodel中查看,这里被改动
        self.tableView.setShowGrid(False)
        self.tableView.verticalHeader().hide()
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.queryModel = myTableModel(self.dic['header'], self.dic['data'])
        self.tableView.setModel(self.queryModel)


        layout = QVBoxLayout(self)
        h1 = QHBoxLayout(self)
        h1.addWidget(self.add_btn)
        # h1.addWidget(self.btn)
        h1.addWidget(QSplitter())
        h1.addWidget(self.delete_btn)

        self.widget = QWidget()
        self.widget.setLayout(h1)
        self.widget.setStyleSheet('''background : #1e1f29;''')
        layout.addWidget(QSplitter())
        self.h2 = QVBoxLayout()
        self.h2.addWidget(self.tableView)
        layout.addLayout(self.h2)
        layout.addWidget(self.widget)
        layout.setStretch(0,1)
        layout.setStretch(1,9)
        layout.setStretch(2,1)
        layout.setStretch(3,3)
        layout.setContentsMargins(0, 0, 0, 0)
        # self.h1.setSpacing(8)
        h1.setContentsMargins(10, 10, 10, 10)
        self.h2.setContentsMargins(15, 15, 15, 15)

        self.add_btn.setStyleSheet('''width: 100px;

            height: 30px; 

            border-radius: 6px;

            color: #ffffff;

            font-family: "PingFangSC-Medium";

            font-size: 12px;

            font-weight: 400;

            line-height: 16px;

            background: qlineargradient(x1:0, y1:1, x2:0, y2:1,stop:0 #3EC169,stop:1 #1BBB70);''')

        self.delete_btn.setStyleSheet('''width: 100px;

            height: 30px; 

            border-radius: 6px;

            color: #ffffff;

            font-family: "PingFangSC-Medium";

            font-size: 12px;

            font-weight: 400;

            line-height: 16px;

            background: #ff6d6d;''')

    def add_action(self):
        self.win = addAgentWindow()
        self.win.setWindowModality(Qt.ApplicationModal)
        self.win.show()

    def delete_action(self):
        AgentFunc.delete_action(self)


class accountWindow(QWidget):
    """账号窗口"""

    def __init__(self):
        super().__init__()
        # self.resize(960, 540)
        # self.setFixedSize(self.width(), self.height())

        # 表模型
        self.queryModel = None

        # 数据表
        self.tableView = None

        self.dic = {
            'header': ['ID', '账号', '密码', '状态', '操作'],
            'data': [[1,1,1,1,1], [2,2,2,2,2]]
        }

        self.add_btn = QPushButton(QIcon(':/static/add.png'),'添加账号')  # 添加账号按钮
        self.add_btn.setIconSize(QSize(10, 10))
        self.logging = QPushButton(QIcon(':/static/start.png'),'登录所有')  # 登录所有按钮
        self.logging.setIconSize(QSize(12, 12))
        self.delete_btn = QPushButton(QIcon(':/static/delete.png'),'删除所有')  # 删除所有按钮
        # self.btn = QPushButton('+')  # +按钮

        self.add_btn.clicked.connect(self.add_action)
        self.logging.clicked.connect(self.logging_action)
        self.delete_btn.clicked.connect(self.delete_action)
        # self.btn.clicked.connect(self.add_action)

        # 软件中的表
        self.tableView = MyTableView2()  # 用的是自己重写的tableview，在querymodel中查看,这里被改动
        self.tableView.setShowGrid(False)
        self.tableView.verticalHeader().hide()
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.queryModel = myTableModel(self.dic['header'], self.dic['data'])
        self.tableView.setModel(self.queryModel)

        layout = QVBoxLayout(self)
        h1 = QHBoxLayout(self)
        h1.addWidget(self.add_btn)
        # h1.addWidget(self.btn)
        h1.addWidget(QSplitter())
        h1.addWidget(self.logging)
        h1.addWidget(self.delete_btn)
        
        self.widget = QWidget()
        self.widget.setLayout(h1)
        self.widget.setStyleSheet('''background : #1e1f29;''')
        layout.addWidget(QSplitter())
        self.h2 = QVBoxLayout()
        self.h2.addWidget(self.tableView)
        layout.addLayout(self.h2)
        layout.addWidget(self.widget)
        layout.setStretch(0,1)
        layout.setStretch(1,9)
        layout.setStretch(2,1)
        layout.setStretch(3,3)
        layout.setContentsMargins(0, 0, 0, 0)
        # self.h1.setSpacing(8)
        h1.setContentsMargins(10, 10, 10, 10)
        self.h2.setContentsMargins(15, 15, 15, 15)

        self.add_btn.setStyleSheet('''width: 100px;

            height: 30px; 

            border-radius: 6px;

            color: #ffffff;

            font-family: "PingFangSC-Medium";

            font-size: 12px;

            font-weight: 400;

            line-height: 16px;

            background: qlineargradient(x1:0, y1:1, x2:0, y2:1,stop:0 #3EC169,stop:1 #1BBB70);''')

        self.logging.setStyleSheet('''width: 100px;

            height: 30px; 

            border-radius: 6px;

            color: #ffffff;

            font-family: "PingFangSC-Medium";

            font-size: 12px;

            font-weight: 400;

            line-height: 16px;

            background: qlineargradient(x1:0, y1:1, x2:0, y2:1,stop:0 #3EC169,stop:1 #1BBB70);''')

        self.delete_btn.setStyleSheet('''width: 100px;

            height: 30px; 

            border-radius: 6px;

            color: #ffffff;

            font-family: "PingFangSC-Medium";

            font-size: 12px;

            font-weight: 400;

            line-height: 16px;

            background: #ff6d6d;''')

    def add_action(self):
        self.win = addUserWindow()
        self.win.setWindowModality(Qt.ApplicationModal)
        self.win.show()

    def delete_action(self):
        AccountFunc.delete_action(self)

    def logging_action(self):
        AccountFunc.logging_action(self)


class discountWindow(QWidget):
    """折扣码窗口"""


    def __init__(self):
        super().__init__()
        # self.resize(960, 540)
        # self.setFixedSize(self.width(), self.height())

        # 表模型
        self.queryModel = None

        # 数据表
        self.tableView = None

        self.dic = {
            'header': ['ID', '折扣码', '状态', '操作'],
            'data': [[1,1,1,1,1], [2,2,2,2,2]]
        }

        self.add_btn = QPushButton(QIcon(':/static/add.png'),'添加折扣码')  # 添加折扣码按钮
        self.add_btn.setIconSize(QSize(10, 10))
        self.select = QPushButton(qtawesome.icon('fa.repeat', color='white'),'查询所有')  # 查询所有按钮
        self.delete_btn = QPushButton(QIcon(':/static/delete.png'),'删除所有')  # 删除所有按钮
        # self.btn = QPushButton('+')  # +按钮

        self.add_btn.clicked.connect(self.add_action)
        self.select.clicked.connect(self.select_action)
        self.delete_btn.clicked.connect(self.delete_action)
        # self.btn.clicked.connect(self.add_action)

        # 软件中的表
        self.tableView = MyTableView3(self)  # 用的是自己重写的tableview，在querymodel中查看,这里被改动
        self.tableView.setShowGrid(False)
        self.tableView.verticalHeader().hide()
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.queryModel = myTableModel(self.dic['header'], self.dic['data'])
        self.tableView.setModel(self.queryModel)

        layout = QVBoxLayout(self)
        h1 = QHBoxLayout(self)
        h1.addWidget(self.add_btn)
        # h1.addWidget(self.btn)
        h1.addWidget(QSplitter())
        h1.addWidget(self.select)
        h1.addWidget(self.delete_btn)
        

        self.widget = QWidget()
        self.widget.setLayout(h1)
        self.widget.setStyleSheet('''background : #1e1f29;''')
        layout.addWidget(QSplitter())
        self.h2 = QVBoxLayout()
        self.h2.addWidget(self.tableView)
        layout.addLayout(self.h2)
        layout.addWidget(self.widget)
        layout.setStretch(0,1)
        layout.setStretch(1,9)
        layout.setStretch(2,1)
        layout.setStretch(3,3)
        layout.setContentsMargins(0, 0, 0, 0)
        # self.h1.setSpacing(8)
        h1.setContentsMargins(10, 10, 10, 10)
        self.h2.setContentsMargins(15, 15, 15, 15)

        self.add_btn.setStyleSheet('''width: 100px;

            height: 30px; 

            border-radius: 6px;

            color: #ffffff;

            font-family: "PingFangSC-Medium";

            font-size: 12px;

            font-weight: 400;

            line-height: 16px;

            background: qlineargradient(x1:0, y1:1, x2:0, y2:1,stop:0 #3EC169,stop:1 #1BBB70);''')

        self.select.setStyleSheet('''width: 100px;

            height: 30px; 

            border-radius: 6px;

            color: #ffffff;

            font-family: "PingFangSC-Medium";

            font-size: 12px;

            font-weight: 400;

            line-height: 16px;

            background: qlineargradient(x1:0, y1:1, x2:0, y2:1,stop:0 #3EC169,stop:1 #1BBB70);''')

        self.delete_btn.setStyleSheet('''width: 100px;

            height: 30px; 

            border-radius: 6px;

            color: #ffffff;

            font-family: "PingFangSC-Medium";

            font-size: 12px;

            font-weight: 400;

            line-height: 16px;

            background: #ff6d6d;''')

    def add_action(self):
        self.win = addDiscountWindow()
        self.win.setWindowModality(Qt.ApplicationModal)
        self.win.show()

    def delete_action(self):
        DiscountFunc.delete_action(self)

    def select_action(self):
        DiscountFunc.select_action(self)


class giftWindow(QWidget):
    """礼品卡窗口"""

    def __init__(self):
        super().__init__()
        # self.resize(960, 540)
        # self.setFixedSize(self.width(), self.height())

        # 表模型
        self.queryModel = None

        # 数据表
        self.tableView = None

        self.dic = {
            'header': ['ID', '名称', '地区', '卡号', 'PIN', '余额', '操作'],
            'data': [[1,1,1,1,1,1,1,1,1], [2,2,2,2,2,2,2,2,2,2]]
        }

        self.add_btn = QPushButton(QIcon(':/static/add.png'),'添加礼品卡')  # 添加礼品卡按钮
        self.add_btn.setIconSize(QSize(10, 10))
        self.select = QPushButton(qtawesome.icon('fa.repeat', color='white'),'查询所有')  # 查询所有按钮
        self.delete_btn = QPushButton(QIcon(':/static/delete.png'),'删除所有')  # 删除所有按钮
        # self.btn = QPushButton('+')  # +按钮

        self.add_btn.clicked.connect(self.add_action)
        self.select.clicked.connect(self.select_action)
        self.delete_btn.clicked.connect(self.delete_action)
        # self.btn.clicked.connect(self.add_action)

        self.tableView = MyTableView4(self)  # 用的是自己重写的tableview，在querymodel中查看,这里被改动
        self.tableView.setShowGrid(False)
        self.tableView.verticalHeader().hide()
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.queryModel = myTableModel(self.dic['header'], self.dic['data'])
        self.tableView.setModel(self.queryModel)

        layout = QVBoxLayout(self)
        h1 = QHBoxLayout(self)
        h1.addWidget(self.add_btn)
        # h1.addWidget(self.btn)
        h1.addWidget(QSplitter())
        h1.addWidget(self.select)
        h1.addWidget(self.delete_btn)

        self.widget = QWidget()
        self.widget.setLayout(h1)
        self.widget.setStyleSheet('''background : #1e1f29;''')
        layout.addWidget(QSplitter())
        self.h2 = QVBoxLayout()
        self.h2.addWidget(self.tableView)
        layout.addLayout(self.h2)
        layout.addWidget(self.widget)
        layout.setStretch(0,1)
        layout.setStretch(1,9)
        layout.setStretch(2,1)
        layout.setStretch(3,3)
        layout.setContentsMargins(0, 0, 0, 0)
        # self.h1.setSpacing(8)
        h1.setContentsMargins(10, 10, 10, 10)
        self.h2.setContentsMargins(15, 15, 15, 15)

        self.add_btn.setStyleSheet('''width: 100px;

            height: 30px; 

            border-radius: 6px;

            color: #ffffff;

            font-family: "PingFangSC-Medium";

            font-size: 12px;

            font-weight: 400;

            line-height: 16px;

            background: qlineargradient(x1:0, y1:1, x2:0, y2:1,stop:0 #3EC169,stop:1 #1BBB70);''')

        self.select.setStyleSheet('''width: 100px;

            height: 30px; 

            border-radius: 6px;

            color: #ffffff;

            font-family: "PingFangSC-Medium";

            font-size: 12px;

            font-weight: 400;

            line-height: 16px;

            background: qlineargradient(x1:0, y1:1, x2:0, y2:1,stop:0 #3EC169,stop:1 #1BBB70);''')

        self.delete_btn.setStyleSheet('''width: 100px;

            height: 30px; 

            border-radius: 6px;

            color: #ffffff;

            font-family: "PingFangSC-Medium";

            font-size: 12px;

            font-weight: 400;

            line-height: 16px;

            background: #ff6d6d;''')

    def add_action(self):
        self.win = addGiftWindow()
        self.win.setWindowModality(Qt.ApplicationModal)
        self.win.show()

    def delete_action(self):
        GiftFunc.delete_action(self)

    def select_action(self):
        GiftFunc.select_action(self)


class addressWindow(QWidget):
    """地址窗口"""

    def __init__(self):
        super().__init__()
        # self.resize(960, 540)
        # self.setFixedSize(self.width(), self.height())

        # 表模型
        self.queryModel = None

        # 数据表
        self.tableView = None

        self.dic = {
            'header': ['ID', '名称', '地区', '邮箱', '付款方式', '操作'],
            'data': [[1,1,1,1,1,1,1,1,1], [2,2,2,2,2,2,2,2,2,2]]
        }

        self.add_btn = QPushButton(QIcon(':/static/add.png'),'添加地址')  # 添加地址按钮
        self.add_btn.setIconSize(QSize(10, 10))
        self.delete_btn = QPushButton(QIcon(':/static/delete.png'),'删除所有')  # 删除所有按钮
        # self.btn = QPushButton('+')  # +按钮

        self.add_btn.clicked.connect(self.add_action)
        self.delete_btn.clicked.connect(self.delete_action)
        # self.btn.clicked.connect(self.add_action)

        self.tableView = MyTableView5()  # 用的是自己重写的tableview，在querymodel中查看,这里被改动
        self.tableView.setShowGrid(False)
        self.tableView.verticalHeader().hide()
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.queryModel = myTableModel(self.dic['header'], self.dic['data'])
        self.tableView.setModel(self.queryModel)

        layout = QVBoxLayout(self)
        h1 = QHBoxLayout(self)
        h1.addWidget(self.add_btn)
        # h1.addWidget(self.btn)
        h1.addWidget(QSplitter())
        h1.addWidget(self.delete_btn)
        
        self.widget = QWidget()
        self.widget.setLayout(h1)
        self.widget.setStyleSheet('''background : #1e1f29;''')
        layout.addWidget(QSplitter())
        self.h2 = QVBoxLayout()
        self.h2.addWidget(self.tableView)
        layout.addLayout(self.h2)
        layout.addWidget(self.widget)
        layout.setStretch(0,1)
        layout.setStretch(1,9)
        layout.setStretch(2,1)
        layout.setStretch(3,3)
        layout.setContentsMargins(0, 0, 0, 0)
        # self.h1.setSpacing(8)
        h1.setContentsMargins(10, 10, 10, 10)
        self.h2.setContentsMargins(15, 15, 15, 15)

        self.add_btn.setStyleSheet('''width: 100px;

            height: 30px; 

            border-radius: 6px;

            color: #ffffff;

            font-family: "PingFangSC-Medium";

            font-size: 12px;

            font-weight: 400;

            line-height: 16px;

            background: qlineargradient(x1:0, y1:1, x2:0, y2:1,stop:0 #3EC169,stop:1 #1BBB70);''')

        self.delete_btn.setStyleSheet('''width: 100px;

            height: 30px; 

            border-radius: 6px;

            color: #ffffff;

            font-family: "PingFangSC-Medium";

            font-size: 12px;

            font-weight: 400;

            line-height: 16px;

            background: #ff6d6d;''')

    def add_action(self):
        self.win = addAddressWindow()
        self.win.setWindowModality(Qt.ApplicationModal)
        self.win.show()

    def delete_action(self):
        AddressFunc.delete_action(self)


class orderWindow(QWidget):
    """订单窗口"""

    def __init__(self):
        super().__init__()
        # self.resize(960, 540)
        # self.setFixedSize(self.width(), self.height())

        # 表模型
        self.queryModel = None

        # 数据表
        self.tableView = None

        self.dic = {
            'header': ['ID', '时间', '地区', '订单号', '账户', '货号', '尺码', '数量', '单价', '折扣码', '付款', '总金额'],
            'data': []
        }

        self.export_btn = QPushButton(qtawesome.icon('fa.download', color='white'),'导出所有')  # 导出所有按钮
        self.delete_btn = QPushButton(QIcon(':/static/delete.png'),'删除所有')  # 删除所有按钮

        self.export_btn.clicked.connect(self.export_action)
        self.delete_btn.clicked.connect(self.delete_action)

        self.tableView = MyTableView6()
        self.tableView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.tableView.setShowGrid(False)
        self.tableView.verticalHeader().hide()
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.queryModel = myTableModel(self.dic['header'], self.dic['data'])
        self.tableView.setModel(self.queryModel)
        self.tableView.setColumnWidth(0, 60)
        self.tableView.setColumnWidth(1, 60)
        self.tableView.setColumnWidth(2, 71)
        self.tableView.setColumnWidth(3, 120)
        self.tableView.setColumnWidth(4, 60)
        self.tableView.setColumnWidth(5, 60)
        self.tableView.setColumnWidth(6, 60)
        self.tableView.setColumnWidth(7, 60)
        self.tableView.setColumnWidth(8, 60)
        self.tableView.setColumnWidth(9, 140)
        self.tableView.setColumnWidth(10, 60)
        self.tableView.setColumnWidth(11, 60)
        self.tableView.setColumnWidth(12, 70)
        # self.tableView.setColumnWidth(13, 45)
        # self.tableView.setColumnWidth(14, 45)

        layout = QVBoxLayout(self)
        h1 = QHBoxLayout(self)
        h1.addWidget(QSplitter())
        h1.addWidget(self.export_btn)
        h1.addWidget(self.delete_btn)
        

        self.widget = QWidget()
        self.widget.setLayout(h1)
        self.widget.setStyleSheet('''background : #1e1f29;''')
        layout.addWidget(QSplitter())
        self.h2 = QVBoxLayout()
        self.h2.addWidget(self.tableView)
        layout.addLayout(self.h2)
        layout.addWidget(self.widget)
        layout.setStretch(0,1)
        layout.setStretch(1,9)
        layout.setStretch(2,1)
        layout.setStretch(3,3)
        layout.setContentsMargins(0, 0, 0, 0)
        # self.h1.setSpacing(8)
        h1.setContentsMargins(10, 10, 10, 10)
        self.h2.setContentsMargins(15, 15, 15, 15)

        self.export_btn.setStyleSheet('''width: 100px;

            height: 30px; 

            border-radius: 6px;

            color: #ffffff;

            font-family: "PingFangSC-Medium";

            font-size: 12px;

            font-weight: 400;

            line-height: 16px;

            background: qlineargradient(x1:0, y1:1, x2:0, y2:1,stop:0 #3EC169,stop:1 #1BBB70);''')

        self.delete_btn.setStyleSheet('''width: 100px;

            height: 30px; 

            border-radius: 6px;

            color: #ffffff;

            font-family: "PingFangSC-Medium";

            font-size: 12px;

            font-weight: 400;

            line-height: 16px;

            background: #ff6d6d;''')

    def export_action(self):
        OrderFunc.export_action(self)

    def delete_action(self):
        OrderFunc.delete_action(self)


		
		

class addTaskWindow(QFrame):
    """添加任务窗口"""

    def __init__(self):
        super().__init__()
        self.resize(520, 330)  # 这里被改动
        self.setFixedSize(self.width(), self.height())

        self.confirm_btn = QPushButton('确定')  # 确定按钮
        self.cancel_btn = QPushButton('取消')  # 取消按钮

        self.confirm_btn.clicked.connect(self.confirm_btn_action)
        self.cancel_btn.clicked.connect(self.cancel_btn_action)

        # self.region = QLabel('       地区：')  # 地区标签
        # self.agent = QLabel('       代理：')  # 代理标签
        # self.article = QLabel('       货号：')  # 货号标签
        # self.size = QLabel('       尺码：')  # 尺码标签
        # self.number = QLabel('       数量：')  # 数量标签
        # self.account = QLabel('       账号：')  # 账号标签
        # self.discount = QLabel('       折扣码：')  # 折扣码标签
        # self.adderss = QLabel('       地址：')  # 地址标签

        # self.line1 = QLineEdit()  # 货号标签后的输入框
        # self.line2 = QLineEdit()  # 尺码标签后的输入框

        # self.ComboBox1 = QComboBox()  # 地区标签后的下拉列表
        # self.ComboBox2 = QComboBox()  # 代理标签后的下拉列表
        # self.ComboBox3 = QComboBox()  # 数量标签后的下拉列表
        # self.ComboBox4 = QComboBox()  # 账号标签后的下拉列表
        # self.ComboBox5 = QComboBox()  # 折扣码标签后的下拉列表
        # self.ComboBox6 = QComboBox()  # 地址标签后的下拉列表

        

        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(19, -1, 19, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.ComboBox1 = QQComboBox()
        self.ComboBox1.setObjectName("ComboBox1")
        self.gridLayout.addWidget(self.ComboBox1, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 1, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 2, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 3, 1, 1)
        self.ComboBox2 = QQComboBox()
        self.ComboBox2.setObjectName("ComboBox2")
        self.gridLayout.addWidget(self.ComboBox2, 1, 1, 1, 1)
        self.line1 = QtWidgets.QLineEdit(self)
        self.line1.setObjectName("line1")
        self.gridLayout.addWidget(self.line1, 2, 1, 1, 1)
        self.line2 = QtWidgets.QLineEdit(self)
        self.line2.setObjectName("line2")
        self.gridLayout.addWidget(self.line2, 3, 1, 1, 1)
        self.ComboBox3 = QQComboBox()
        self.ComboBox3.setObjectName("ComboBox3")
        self.gridLayout.addWidget(self.ComboBox3, 4, 1, 1, 1)
        self.ComboBox5 = QQComboBox()
        self.ComboBox5.setObjectName("ComboBox5")
        self.gridLayout.addWidget(self.ComboBox5, 1, 4, 1, 1)
        self.ComboBox4 = QQComboBox()
        self.ComboBox4.setObjectName("ComboBox4")
        self.gridLayout.addWidget(self.ComboBox4, 0, 4, 1, 1)
        self.ComboBox6 = QQComboBox()
        self.ComboBox6.setObjectName("ComboBox6")
        self.gridLayout.addWidget(self.ComboBox6, 2, 4, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 3)
        self.gridLayout.setColumnStretch(2, 1)
        self.gridLayout.setColumnStretch(3, 1)
        self.gridLayout.setColumnStretch(4, 3)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        # self.confirm_btn = QPushButton(self)
        self.confirm_btn.setObjectName("confirm_btn")
        self.horizontalLayout_2.addWidget(self.confirm_btn)
        # self.cancel_btn = QPushButton(self)
        self.cancel_btn.setObjectName("cancel_btn")
        self.horizontalLayout_2.addWidget(self.cancel_btn)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addWidget(QSplitter())
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 9)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 1)

        self.label.setText("   添加任务")
        self.label_2.setText("地区")
        self.label_6.setText("数量")
        self.label_8.setText("折扣码")
        self.label_3.setText("代理")
        self.label_9.setText("地址")
        self.label_5.setText("尺码")
        self.label_4.setText("货号")
        self.label_7.setText("账号")

        self.line1.setPlaceholderText(' 请输入货号')  # 地区标签后的下拉列表
        self.line2.setPlaceholderText(' 请输入尺码')  # 代理标签后的下拉列表
        # self.ComboBox3.setPlaceholderText('请选择数量')  # 数量标签后的下拉列表
        # self.ComboBox4.setPlaceholderText('请选择账号')  # 账号标签后的下拉列表
        # self.ComboBox5.setPlaceholderText('请选择折扣码')  # 折扣码标签后的下拉列表
        # self.ComboBox6.setPlaceholderText('请选择地区')  # 地址标签后的下拉列表

        self.ComboBox1.addItem(' 请选择地区')  # 地区标签后的下拉列表
        self.ComboBox1.addItem(' 请选择')
        self.ComboBox2.addItem(' 请选择代理')  # 代理标签后的下拉列表
        self.ComboBox3.addItem(' 请选择数量')  # 数量标签后的下拉列表
        self.ComboBox4.addItem(' 请选择账号')  # 账号标签后的下拉列表
        self.ComboBox5.addItem(' 请选择折扣码')  # 折扣码标签后的下拉列表
        self.ComboBox6.addItem(' 请选择地区')

        self.ComboBox1.setView(QListView())
        self.ComboBox2.setView(QListView())  # 代理标签后的下拉列表
        self.ComboBox3.setView(QListView())  # 数量标签后的下拉列表
        self.ComboBox4.setView(QListView())  # 账号标签后的下拉列表
        self.ComboBox5.setView(QListView())  # 折扣码标签后的下拉列表
        self.ComboBox6.setView(QListView()) 

        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setContentsMargins(19, 19, 19, 19)
        # self.groupBox = QGroupBox()  # 最外面的方框
        # layout2 = QHBoxLayout()
        # layout = QGridLayout()
        # h1 = QHBoxLayout()
        # h2 = QHBoxLayout()

        # h1.addWidget(QSplitter())
        # h1.addWidget(self.confirm_btn)
        # h2.addWidget(QSplitter())
        # h2.addWidget(self.cancel_btn)
        # h2.addWidget(QSplitter())

        # names = [
        #     self.article, self.line1,
        #     self.size, self.line2,
        #     self.region, self.ComboBox1,
        #     self.agent, self.ComboBox2,
        #     self.number, self.ComboBox3,
        #     self.account, self.ComboBox4,
        #     self.discount, self.ComboBox5,
        #     self.adderss, self.ComboBox6,
        # ]
        # positions = [(i, j) for i in range(8) for j in range(2)]

        # for position, name in zip(positions, names):
        #     layout.addWidget(name, *position)
        # layout.addLayout(h1, 9, 0)
        # layout.addLayout(h2, 9, 1)
        # # self.groupBox.setLayout(layout)
        # layout2.addWidget(QSplitter())
        # # layout2.addWidget(self.groupBox)
        # layout2.addWidget(QSplitter())
        # self.setLayout(layout2)

        # layout2.layout().setContentsMargins(0, 0, 0, 0)

        # self.setAttribute(Qt.WA_TranslucentBackground) # 设置窗口背景透明
        self.setWindowFlag(Qt.FramelessWindowHint)

        # self.setStyleSheet('''''')
        self.setStyleSheet('''QLabel{width: 24px;

							height: 16px;

							color: #5b5d6a;

							font-family: "PingFangSC-Regular";

							font-size: 12px;

							font-weight: 400;

							line-height: 16px;}

                            QFrame{

							border-radius: 6px;

							background: #1e1f29;

                            }
                            QComboBox{

                            width: 160px;

							height: 32px;

							border-radius: 8px;

							background: #181922;

							color: #5b5d6a;

							font-family: "PingFangSC-Regular";

							font-size: 12px;

							font-weight: 400;

							line-height: 13px;

                            }

                            QComboBox::on{

                            border: 1px solid  #1fbc6f;

                            }


							QComboBox QAbstractItemView{border-radius: 8px;background: #181922;outline:0px;}

							QComboBox QAbstractItemView::item {

							border-radius: 8px;

							width: 160px;

							height: 28px;

							background: #181922;

							color: #5b5d6a;

							font-family: "PingFangSC-Regular";

							font-size: 15px;

							font-weight: 400;

							line-height: 13px;

							}






							QComboBox QAbstractItemView::item:hover{

							background:gray;

							color:white;

							}

                            QComboBox::drop-down{

                            border:none;

                            image: url(:/static/xiala.png);

                            }

                            QGroupBox{

                            background: #1e1f29;

                            border:none;

                            }

                            QLineEdit{

                            width: 160px;

							height: 30px;

							border-radius: 8px;

							background: #181922;

							color: #5b5d6a;

							font-family: "PingFangSC-Regular";

							font-size: 12px;

							font-weight: 400;

							line-height: 13px;

                            }''')
       # QComboBox:hover{

							# color: white;

							# background-color: gray;

							# }

       #                      QComboBox::selected{

       #                      color: white;

       #                      background:gray;

       #                      }

       	self.label.setStyleSheet('''width: 48px;

							height: 19px;

							color: #ffffff;

							font-family: "PingFangSC-Medium";

							font-size: 12px;

							font-weight: 400;

							line-height: 16px;''')

        self.confirm_btn.setStyleSheet('''width: 100px;

            height: 30px; 

            border-radius: 6px;

            color: #ffffff;

            font-family: "PingFangSC-Medium";

            font-size: 12px;

            font-weight: 400;

            line-height: 16px;

            background: qlineargradient(x1:0, y1:1, x2:0, y2:1,stop:0 #3EC169,stop:1 #1BBB70);''')

        self.cancel_btn.setStyleSheet('''width: 100px;

            height: 30px; 

            border-radius: 6px;

            color: #ffffff;

            font-family: "PingFangSC-Medium";

            font-size: 12px;

            font-weight: 400;

            line-height: 16px;

            background: #5c5858;''')
        
  


    

    def confirm_btn_action(self):
        TaskFunc.confirm_btn_action(self)
        self.close()

    def cancel_btn_action(self):
        self.close()


class addAgentWindow(QFrame):
    '''添加代理窗口'''

    def __init__(self):
        super().__init__()
        self.resize(600, 322)  # 这里被改动
        from querymodel import myTableModel, MyTableView
        # self.setFixedSize(self.width(), self.height())

        # 表模型
        self.queryModel = None

        # 数据表
        self.tableView = None

        self.dic = {
            'header': ['Ping'],
            'data': []
        }

        self.name = QLabel('名称')  # 名称标签
        self.speed = QLabel('速度')  # 速度标签
        self.label = QLabel(' 添加代理')
        self.pingL = QLabel('Ping')

        self.ping = QPushButton('Ping')  # ping标签
        self.confirm_btn = QPushButton('确定')  # 确定按钮
        self.cancel_btn = QPushButton('取消')  # 取消按钮

        self.confirm_btn.clicked.connect(self.confirm_btn_action)
        self.cancel_btn.clicked.connect(self.cancel_btn_action)
        self.cancel_btn.clicked.connect(self.ping_btn_action)
        # self.ping.setAlignment(QtCore.Qt.AlignCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignVCenter)

        self.line = QLineEdit()  # 名称标签下面的输入框

        self.comboBox = QQComboBox()  # 速度下面的下拉列表
        self.comboBox.setView(QListView())

        self.groupBox = QGroupBox()  # 表格外围的框

        self.edit = QTextEdit() # 代理信息输入框
        self.edit.setPlaceholderText(' IP|端口|账号|密码')
        self.edit.setLineWrapMode(QTextEdit.NoWrap)

        self.tableView = QTableView() # Ping列表
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.horizontalHeader().setVisible(False)
        self.tableView.verticalHeader().setVisible(False)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.queryModel = myTableModel(self.dic['header'], self.dic['data'])
        self.tableView.setModel(self.queryModel)
        self.tableView.setColumnWidth(0, 10)
        # self.tableView.setColumnWidth(1, 40)
        # self.tableView.setColumnWidth(2, 40)
        # self.tableView.setColumnWidth(3, 40)
        # self.tableView.setColumnWidth(4, 40)

        layout = QVBoxLayout()
        layout1 = QVBoxLayout()
        layout2 = QHBoxLayout()
        h1 = QHBoxLayout()
        h2 = QHBoxLayout()
        h3 = QHBoxLayout()
        h4 = QHBoxLayout()
        h5 = QHBoxLayout()
        h = QHBoxLayout()

        h6 = QHBoxLayout()
        h6.addWidget(self.edit)
        h6.addWidget(self.tableView)
        h6.setSpacing(0)
        h6.setContentsMargins(0, 0, 0, 0)
        h6.setStretch(0,8)
        h6.setStretch(1,1)

        layout1.addLayout(h6)

        self.groupBox.setLayout(layout1)

        h1.addWidget(self.name)
        h1.addWidget(self.line)
        # h2.addWidget(self.line)
        # h2.addWidget(QSplitter())
        h3.addWidget(self.speed)
        h3.addWidget(self.comboBox)
        # h4.addWidget(self.comboBox)
        h4.addWidget(self.ping)
        # h5.addWidget(QSplitter())
        h5.addWidget(self.confirm_btn)
        h5.addWidget(QSplitter())
        h5.addWidget(self.cancel_btn)
        h5.addWidget(QSplitter())

        layout.addLayout(h1)
        # layout.addLayout(h2)
        # layout.addWidget(QSplitter())
        layout.addLayout(h3)
        layout.addLayout(h4)
        layout.addWidget(QSplitter())
        layout.addWidget(QSplitter())
        layout.addWidget(QSplitter())
        layout.addLayout(h5)
        # layout.addWidget(QSplitter())

        layout2.addWidget(self.groupBox)
        layout2.addWidget(QSplitter())
        layout2.addLayout(layout)
        layout2.setStretch(0,8)
        layout2.setStretch(1,1)
        layout2.setStretch(1,1)
        
        self.layout_ = QVBoxLayout()
        h.addWidget(self.label)
        h.addWidget(QSplitter())
        h.addWidget(self.pingL)
        h.addWidget(QSplitter())
        h.addWidget(QSplitter())
        self.layout_.addLayout(h)
        self.layout_.addLayout(layout2)
        self.setLayout(self.layout_)

        # layout2.setSpacing(40)
        layout.setSpacing(10)
        self.layout_.setSpacing(10)
        self.layout_.setContentsMargins(25, 15, 25, 15)
        # layout1.setSpacing(0)
        layout1.setContentsMargins(0, 0, 0, 0)

        # layout2.setSpacing(0)
        # layout2.setContentsMargins(0, 0, 0, 0)
        # h1.setSpacing(0)
        h1.setContentsMargins(0, 0, 0, 0)
        # h2.setContentsMargins(0, 0, 0, 0)
        # h3.setSpacing(0)
        h3.setContentsMargins(0, 0, 0, 0)
        # h4.setSpacing(0)
        h4.setContentsMargins(0, 0, 0, 0)
        # h5.setSpacing(10)
        h5.setContentsMargins(0, 0, 0, 0)

        # self.setAttribute(Qt.WA_TranslucentBackground) # 设置窗口背景透明
        self.setWindowFlag(Qt.FramelessWindowHint)

        self.setStyleSheet('''

                            QVBoxLayout{

                            background: #1e1f29;

                            }
                            QHBoxLayout{

                            background: #1e1f29;

                            }

                            QFrame{

                            border-radius: 6px;

                            background: #1e1f29;

                            }


                            QWidget{

                            background: #1e1f29;

                            }

                            QLabel{font-family: "PingFangSC-Regular";

                            font-size: 16px;

                            font-weight: 400;

                            line-height: 16px;

                            text-align: center;

                            color: #5b5d6a;}

                            QTextEdit{background-color: #181922;

                            border-radius: 0px;

                            border:none;

                            border-top-left-radius:8px;

                            alternate-background-color:#181922;;

                            font:14px "PingFangSC-Regular";

                            color:#677483;}

                            QTableView{

                            background-color: #181922;

                            border-radius: 0px;

                            border:none;

                            border-bottom-right-radius:8px;

                            alternate-background-color:#181922;;

                            font:14px "PingFangSC-Regular";

                            color:#677483;}

                            QHeaderView::section{

                            color: #777777;

                            font-size: 16px;

                            font-family: "PingFangSC-Regular";

                            font-weight: 400;

                            text-align:center;

                            height:32px;

                            background-color: #181922;

                            border:none;

                            border-top-right-radius:8px;}

                            QTableView::item{

                            margin-bottom:4px;

                            margin-top:4px;

                            background: #21232f;

                            font-family: "PingFangSC-Regular";

                            }

                            
                            QSplitter{

                            background-color: #1e1f29;

                            }

                            QComboBox{

                            width: 160px;

							height: 32px;

							border-radius: 8px;

							background: #181922;

							color: #5b5d6a;

							font-family: "PingFangSC-Regular";

							font-size: 12px;

							font-weight: 400;

							line-height: 13px;

                            }

                            QComboBox::on{

                            border: 1px solid  #1fbc6f;

                            }


							QComboBox QAbstractItemView{border-radius: 8px;background: #181922;outline:0px;}

							QComboBox QAbstractItemView::item {

							border-radius: 8px;

							width: 160px;

							height: 28px;

							background: #181922;

							color: #5b5d6a;

							font-family: "PingFangSC-Regular";

							font-size: 15px;

							font-weight: 400;

							line-height: 13px;

							}






							QComboBox QAbstractItemView::item:hover{

							background:gray;

							color:white;

							}

                            QComboBox::drop-down{

                            border:none;

                            image: url(:/static/xiala.png);

                            }

                            QGroupBox{

                            background: #1e1f29;

                            border:none;

                            }

                            QLineEdit{

                            width: 160px;

							height: 30px;

							border-radius: 8px;

							background: #181922;

							color: #5b5d6a;

							font-family: "PingFangSC-Regular";

							font-size: 12px;

							font-weight: 400;

							line-height: 13px;

                            }''')

        # 
        self.ping.setStyleSheet('''width: 194px;

							height: 30px;

							border-radius: 8px;

							background: #5c5858;

							color: #ffffff;

							font-family: "PingFangSC-Regular";

							font-size: 12px;

							font-weight: 400;

							line-height: 16px;

							text-align: center;

        					''')

       	self.label.setStyleSheet('''width: 48px;

							height: 19px;

							color: #ffffff;

							font-family: "PingFangSC-Medium";

							font-size: 14px;

							font-weight: 400;

							line-height: 16px;''')

        self.confirm_btn.setStyleSheet('''width: 100px;

                height: 30px; 

                border-radius: 6px;

                color: #ffffff;

                font-family: "PingFangSC-Medium";

                font-size: 12px;

                font-weight: 400;

                line-height: 16px;

                background: qlineargradient(x1:0, y1:1, x2:0, y2:1,stop:0 #3EC169,stop:1 #1BBB70);''')

        self.cancel_btn.setStyleSheet('''width: 100px;

            height: 30px; 

            border-radius: 6px;

            color: #ffffff;

            font-family: "PingFangSC-Medium";

            font-size: 12px;

            font-weight: 400;

            line-height: 16px;

            background: #5c5858;''')
        


    def confirm_btn_action(self):
        AgentFunc.confirm_btn_action(self)
        self.close()

    def cancel_btn_action(self):
        self.close()

    def ping_btn_action(self):
        AgentFunc.ping_btn_action(self)


class addUserWindow(QWidget):
    '''添加账号窗口'''

    def __init__(self):
        super().__init__()
        self.resize(520, 322)  # 这里被改动
        # self.setFixedSize(self.width(), self.height())

        self.confirm_btn = QPushButton('确定')  # 确定按钮
        self.cancel_btn = QPushButton('取消')  # 取消按钮
        self.label = QLabel('添加账号')

        self.confirm_btn.clicked.connect(self.confirm_btn_action)
        self.cancel_btn.clicked.connect(self.cancel_btn_action)

        self.text_line = QTextEdit()  # 大文本输入框
        self.text_line.setPlaceholderText(' 请输入账号信息:账号|密码')

        self.groupBox = QGroupBox()  # 最外围的框

        layout = QVBoxLayout()
        layout2 = QHBoxLayout()
        layout3 = QVBoxLayout()
        layout2.addWidget(QSplitter())
        layout2.addWidget(self.confirm_btn)
        # layout2.addWidget(QSplitter())
        layout2.addWidget(self.cancel_btn)
        layout2.addWidget(QSplitter())

        # layout.addWidget(self.text_line)
        # layout.addLayout(layout2)
        # self.groupBox.setLayout(layout)
        # layout3.addWidget(QSplitter(Qt.Horizontal))
        layout3.addWidget(self.label)
        layout3.addWidget(self.text_line)
        # layout3.addWidget(QSplitter(Qt.Horizontal))
        layout3.addLayout(layout2)
        layout.setSpacing(15)
        layout3.setContentsMargins(30,15,30,15)
        layout3.setSpacing(15)
        self.setLayout(layout3)

        self.setWindowFlag(Qt.FramelessWindowHint)

        self.setStyleSheet('''

                            QWidget{

                            background: #1e1f29;

                            }

                            QLabel{font-family: "PingFangSC-Regular";

                            font-size: 16px;

                            font-weight: 400;

                            line-height: 16px;

                            text-align: center;

                            color: #5b5d6a;}

                            QFrame{

                            border-radius: 6px;

                            background: #1e1f29;

                            }

                            QGroupBox{

                            background: #1e1f29;

                            border:none;

                            }

                            QTextEdit{

                            border:0px;    

                            background:#181922;

                            border-radius: 8px;

                            color : white;

                            font-family: "PingFangSC-Regular";

                            font-size:16px;

                            }

                            QSplitter{

                            background-color: #1e1f29;

                            }''')

       	self.label.setStyleSheet('''width: 48px;

							height: 19px;

							color: #ffffff;

							font-family: "PingFangSC-Medium";

							font-size: 15px;

							font-weight: 400;

							line-height: 16px;''')

        self.confirm_btn.setStyleSheet('''width: 100px;

                height: 30px; 

                border-radius: 6px;

                color: #ffffff;

                font-family: "PingFangSC-Medium";

                font-size: 12px;

                font-weight: 400;

                line-height: 16px;

                background: qlineargradient(x1:0, y1:1, x2:0, y2:1,stop:0 #3EC169,stop:1 #1BBB70);''')

        self.cancel_btn.setStyleSheet('''width: 100px;

            height: 30px; 

            border-radius: 6px;

            color: #ffffff;

            font-family: "PingFangSC-Medium";

            font-size: 12px;

            font-weight: 400;

            line-height: 16px;

            background: #5c5858;''')

    def confirm_btn_action(self):
        AccountFunc.confirm_btn_action(self)
        self.close()

    def cancel_btn_action(self):
        self.close()


class addDiscountWindow(QWidget):
    '''添加折扣码窗口'''

    def __init__(self):
        super().__init__()

        self.resize(520, 322)  # 这里被改动
        # self.setFixedSize(self.width(), self.height())

        self.confirm_btn = QPushButton('确定')  # 确定按钮
        self.cancel_btn = QPushButton('取消')  # 取消按钮

        self.label = QLabel('添加折扣码')

        self.confirm_btn.clicked.connect(self.confirm_btn_action)
        self.cancel_btn.clicked.connect(self.cancel_btn_action)

        self.text_line = QTextEdit()  # 大文本输入框
        self.text_line.setPlaceholderText('请输入折扣码')

        # self.groupBox = QGroupBox()  # 最外围的框

        layout = QVBoxLayout()
        layout2 = QHBoxLayout()
        layout3 = QHBoxLayout()
        layout2.addWidget(QSplitter())
        layout2.addWidget(self.confirm_btn)
        # layout2.addWidget(QSplitter())
        layout2.addWidget(self.cancel_btn)
        layout2.addWidget(QSplitter())

        layout.addWidget(self.label)
        layout.addWidget(self.text_line)
        layout.addLayout(layout2)
        # self.groupBox.setLayout(layout)
        # layout3.addWidget(QSplitter())
        # layout3.addWidget(self.text_line)
        # layout3.addWidget(QSplitter())
        # layout.setSpacing(15)
        layout.setContentsMargins(30,15,30,15)
        layout.setSpacing(15)
        self.setLayout(layout)

        self.setWindowFlag(Qt.FramelessWindowHint)

        self.setStyleSheet('''

                            QWidget{

                            background: #1e1f29;

                            border-radius: 8px;

                            }

                            QLabel{font-family: "PingFangSC-Regular";

                            font-size: 16px;

                            font-weight: 400;

                            line-height: 16px;

                            text-align: center;

                            color: #5b5d6a;}

                            QFrame{

                            border-radius: 6px;

                            background: #1e1f29;

                            }

                            QGroupBox{

                            background: #1e1f29;

                            border:none;

                            }

                            QTextEdit{

                            border:0px;    

                            background:#181922;

                            border-radius: 8px;

                            color : white;

                            font-family: "PingFangSC-Regular";

                            font-size:16px;

                            }

                            QSplitter{

                            background-color: #1e1f29;

                            }''')

       	self.label.setStyleSheet('''width: 48px;

							height: 19px;

							color: #ffffff;

							font-family: "PingFangSC-Medium";

							font-size: 15px;

							font-weight: 400;

							line-height: 16px;''')

        self.confirm_btn.setStyleSheet('''width: 100px;

                height: 30px; 

                border-radius: 6px;

                color: #ffffff;

                font-family: "PingFangSC-Medium";

                font-size: 12px;

                font-weight: 400;

                line-height: 16px;

                background: qlineargradient(x1:0, y1:1, x2:0, y2:1,stop:0 #3EC169,stop:1 #1BBB70);''')

        self.cancel_btn.setStyleSheet('''width: 100px;

            height: 30px; 

            border-radius: 6px;

            color: #ffffff;

            font-family: "PingFangSC-Medium";

            font-size: 12px;

            font-weight: 400;

            line-height: 16px;

            background: #5c5858;''')

    def confirm_btn_action(self):
        DiscountFunc.confirm_btn_action(self)
        self.close()

    def cancel_btn_action(self):
        self.close()


class addGiftWindow(QWidget):
    '''添加礼品卡窗口'''

    def __init__(self):
        super().__init__()
        self.resize(800, 322)  # 这里被改动
        # self.setFixedSize(self.width(), self.height())


        self.confirm_btn = QPushButton('确定')  # 确定按钮
        self.cancel_btn = QPushButton('取消')  # 取消按钮

        self.confirm_btn.clicked.connect(self.confirm_btn_action)
        self.cancel_btn.clicked.connect(self.cancel_btn_action)

        self.name = QLabel('名称')  # 名称标签
        self.country = QLabel('国家')  # 国家标签
        self.label = QLabel('添加礼品卡')

        self.line = QLineEdit()  # 名称标签后的输入框
        self.line.setPlaceholderText('请输入名称')

        self.textline = QTextEdit()  # 文本输入框
        self.textline.setPlaceholderText('请输入礼品卡')

        self.comboBox = QQComboBox()  # 国家标签后的下拉列表
        self.comboBox.setView(QListView())

        # self.groupBox = QGroupBox()  # 最外围的框

        layout = QVBoxLayout()
        layout2 = QHBoxLayout()
        h1 = QGridLayout()
        h2 = QHBoxLayout()
        h3 = QVBoxLayout()

        h1.addWidget(self.name, 0, 0)
        h1.addWidget(self.line, 0, 1)
        h1.addWidget(self.country, 1, 0)
        h1.addWidget(self.comboBox, 1, 1)

        h2.addWidget(QSplitter())
        h2.addWidget(self.confirm_btn)
        # h2.addWidget(QSplitter())
        h2.addWidget(self.cancel_btn)
        h2.addWidget(QSplitter())

        # layout.addLayout(h1)
        # layout.addWidget(self.textline)
        # layout.addLayout(h2)
        # self.groupBox.setLayout(layout)
        h3.addLayout(h1)
        h3.addWidget(QSplitter())
        h3.addWidget(QSplitter())
        h3.addLayout(h2)
        h3.setStretch(0,2)
        h3.setStretch(0,1)
        h3.setStretch(0,1)
        h3.setStretch(0,1)

        # layout2.addWidget(QSplitter())
        h1.setContentsMargins(0,0,0,0)
        h3.setContentsMargins(0,0,0,0)
        layout2.addWidget(self.textline)
        layout2.addLayout(h3)
        layout2.setContentsMargins(0,0,0,0)
        layout2.setStretch(0,6)
        layout2.setStretch(1,1)
        layout.setSpacing(15)
        layout.addWidget(self.label)
        layout.addLayout(layout2)
        layout.setContentsMargins(30,15,30,15)
        # layout.setSpacing(15)
        self.setLayout(layout)


        self.setWindowFlag(Qt.FramelessWindowHint)

        self.setStyleSheet('''

                            QWidget{

                            background: #1e1f29;

                            border-radius: 8px;

                            }

                            QLabel{font-family: "PingFangSC-Regular";

                            font-size: 16px;

                            font-weight: 400;

                            line-height: 16px;

                            text-align: center;

                            color: #5b5d6a;}

                            QFrame{

                            border-radius: 8px;

                            background: #1e1f29;

                            }

                            QGroupBox{

                            background: #1e1f29;

                            border:none;

                            }

                            QTextEdit{

                            border:0px;    

                            background:#181922;

                            border-radius: 8px;

                            color : white;

                            font-family: "PingFangSC-Regular";

                            font-size:16px;

                            }

                            QSplitter{

                            background-color: #1e1f29;

                            }

                            QComboBox{

                            width: 160px;

							height: 32px;

							border-radius: 8px;

							background: #181922;

							color: #5b5d6a;

							font-family: "PingFangSC-Regular";

							font-size: 12px;

							font-weight: 400;

							line-height: 13px;

                            }

                            QComboBox::on{

                            border: 1px solid  #1fbc6f;

                            }


							QComboBox QAbstractItemView{border-radius: 8px;background: #181922;outline:0px;}

							QComboBox QAbstractItemView::item {

							border-radius: 8px;

							width: 160px;

							height: 28px;

							background: #181922;

							color: #5b5d6a;

							font-family: "PingFangSC-Regular";

							font-size: 15px;

							font-weight: 400;

							line-height: 13px;

							}






							QComboBox QAbstractItemView::item:hover{

							background:gray;

							color:white;

							}

                            QComboBox::drop-down{

                            border:none;

                            image: url(:/static/xiala.png);

                            }

                            QGroupBox{

                            background: #1e1f29;

                            border:none;

                            }

                            QLineEdit{

                            width: 160px;

							height: 30px;

							border-radius: 8px;

							background: #181922;

							color: #5b5d6a;

							font-family: "PingFangSC-Regular";

							font-size: 15px;

							font-weight: 400;

							line-height: 13px;

                            }''')

       	self.label.setStyleSheet('''width: 48px;

							height: 19px;

							color: #ffffff;

							font-family: "PingFangSC-Medium";

							font-size: 14px;

							font-weight: 400;

							line-height: 16px;''')


        self.confirm_btn.setStyleSheet('''width: 100px;

                height: 30px; 

                border-radius: 6px;

                color: #ffffff;

                font-family: "PingFangSC-Medium";

                font-size: 12px;

                font-weight: 400;

                line-height: 16px;

                background: qlineargradient(x1:0, y1:1, x2:0, y2:1,stop:0 #3EC169,stop:1 #1BBB70);''')

        self.cancel_btn.setStyleSheet('''width: 100px;

            height: 30px; 

            border-radius: 6px;

            color: #ffffff;

            font-family: "PingFangSC-Medium";

            font-size: 12px;

            font-weight: 400;

            line-height: 16px;

            background: #5c5858;''')

    def confirm_btn_action(self):
        GiftFunc.confirm_btn_action(self)
        self.close()

    def cancel_btn_action(self):
        self.close()


class addAddressWindow(QWidget):
    '''添加地址窗口'''

    def __init__(self):
        super().__init__()
        self.resize(600, 450)  # 这里被改动
        # self.setFixedSize(self.width(), self.height())

        



        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.comboBox = QQComboBox()
        self.comboBox.setView(QListView())
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_3.addWidget(self.lineEdit)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton = QPushButton(self)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.pushButton_2 = QPushButton(self)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.pushButton_3 = QPushButton(self)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.horizontalLayout_2.addWidget(QSplitter())
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.mid_widget = QStackedWidget()
        self.mid_widget.setObjectName("widget")
        self.verticalLayout.addWidget(self.mid_widget)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.submit = QPushButton(self)
        self.submit.setObjectName("pushButton_4")
        self.horizontalLayout_4.addWidget(self.submit)
        self.exit_close = QPushButton(self)
        self.exit_close.setObjectName("pushButton_5")
        self.horizontalLayout_4.addWidget(self.exit_close)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 5)
        self.verticalLayout.setStretch(4, 1)

        self.horizontalLayout.setContentsMargins(15,-1,15,-1)
        self.horizontalLayout_2.setContentsMargins(15,-1,15,-1)
        self.horizontalLayout_3.setContentsMargins(15,-1,15,-1)

        self.pushButton.setMinimumSize(0,40)
        self.pushButton_2.setMinimumSize(0,40)
        self.pushButton_3.setMinimumSize(0,40)



        self.label.setText("添加地址")
        self.label.setAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop|QtCore.Qt.AlignTop)
        self.pushButton.setText("Shipping address")
        self.pushButton_2.setText("Billing address")
        self.pushButton_3.setText("Payment")
        self.submit.setText("确认")
        self.exit_close.setText("取消")
        self.lineEdit.setPlaceholderText(' 名称')
        self.comboBox.addItem(' Country')

        self.mid_widget.addWidget(ShippingWidget())
        self.mid_widget.addWidget(BillingWidget())
        self.mid_widget.addWidget(PaymentWidget())

        self.pushButton.setCheckable(True)
        self.pushButton.setChecked(True)
        self.pushButton_2.setCheckable(True)
        self.pushButton_3.setCheckable(True)

        self.pushButton.clicked.connect(lambda:self.mid_widget.setCurrentIndex(0))  # list和右侧窗口的index对应绑定
        self.pushButton_2.clicked.connect(lambda:self.mid_widget.setCurrentIndex(1))
        self.pushButton_3.clicked.connect(lambda:self.mid_widget.setCurrentIndex(2))
        self.pushButton_3.clicked.connect(self.setQss)



        self.pushButton.setAutoExclusive(True)
        self.pushButton_2.setAutoExclusive(True)
        self.pushButton_3.setAutoExclusive(True)


        self.pushButton.clicked.connect(lambda:self.pushButton.setChecked(True))
        self.pushButton_2.clicked.connect(lambda:self.pushButton_2.setChecked(True))
        self.pushButton_3.clicked.connect(lambda:self.pushButton_3.setChecked(True))
    

        # self.title = QLabel('Add New Profile')  # Add New Profile大标签，在最上方
        # self.shopping_address = QLabel('Shipping Address')  # Shipping Address标签
        # self.billing_Address = QLabel('Billing Address')  # Billing Address标签
        # self.Payment_type = QLabel('Payment Type')  # Payment Type标签

        # self.first_name1 = QLineEdit()  # Shipping Address下的First Name输入框
        # self.first_name1.setPlaceholderText('First Name')
        # self.first_name2 = QLineEdit()  # Billing Address 下的First Name输入框
        # self.first_name2.setPlaceholderText('First Name')
        # self.profile_name = QLineEdit()  # Profile Name 输入框
        # self.profile_name.setPlaceholderText('Profile Name')

        # self.last_name1 = QLineEdit()  # Shipping Address下的Last Name输入框
        # self.last_name1.setPlaceholderText('Last Name')
        # self.last_name2 = QLineEdit()  # Billing Address下的Last Name输入框
        # self.last_name2.setPlaceholderText('Last Name')
        # self.email = QLineEdit()  # Email输入框
        # self.email.setPlaceholderText('Email')

        # self.country1 = QQComboBox()  # Shipping Address下的国家下拉列表
        # self.country2 = QQComboBox()  # Billing Address下的国家下拉列表
        # self.card_type = QQComboBox()  # Card Type 下拉列表
        # self.month = QQComboBox()  # 月下拉列表
        # self.year = QQComboBox()  # 年下拉列表

        # self.address1 = QLineEdit()  # Shipping Address下的Address 1输入框
        # self.address1.setPlaceholderText('Address 1')
        # self.address2 = QLineEdit()  # Billing Address下的Address 1输入框
        # self.address2.setPlaceholderText('Address 1')
        # self.address3 = QLineEdit()  # Shipping Address下的Address 2输入框
        # self.address3.setPlaceholderText('Address 2')
        # self.address4 = QLineEdit()  # Billing Address下的Address 2输入框
        # self.address4.setPlaceholderText('Address 2')

        # self.card_number = QLineEdit()  # Card Number输入框
        # self.card_number.setPlaceholderText('Card Number')
        # self.cvv = QLineEdit()  # CVV输入框
        # self.cvv.setPlaceholderText('CVV')

        # self.county3 = QLineEdit()  # Shipping Address下的County输入框
        # self.county3.setPlaceholderText('County')
        # self.county4 = QLineEdit()  # Billing Address下的County输入框
        # self.county4.setPlaceholderText('County')

        # self.city1 = QLineEdit()  # Shipping Address下的City输入框
        # self.city1.setPlaceholderText('City')
        # self.city2 = QLineEdit()  # Billing Address下的City输入框
        # self.city2.setPlaceholderText('City')

        # self.state1 = QLineEdit()  # Shipping Address下的State输入框
        # self.state1.setPlaceholderText('State')
        # self.state2 = QLineEdit()  # Billing Address下的State输入框
        # self.state2.setPlaceholderText('State')

        # self.zip_code1 = QLineEdit()  # Shipping Address下的Zip Code输入框
        # self.zip_code1.setPlaceholderText('Zip Code')
        # self.zip_code2 = QLineEdit()  # Billing Address下的Zip Code输入框
        # self.zip_code2.setPlaceholderText('Zip Code')

        # self.phone_number1 = QLineEdit()  # Shipping Address下的Phone Number输入框
        # self.phone_number1.setPlaceholderText('Phone Number')
        # self.phone_number2 = QLineEdit()  # Billing Address下的Phone Number输入框
        # self.phone_number2.setPlaceholderText('Phone Number')

        # self.checkbox = QCheckBox('Same with shipping')  # Same with shipping 复选框

        # self.submit = QPushButton('SUBMIT')  # SUBMIT按钮
        # self.exit_close = QPushButton('CLOSE')  # CLOSE按钮

        self.submit.clicked.connect(self.submit_action)
        self.exit_close.clicked.connect(self.exit_action)

        # layout = QGridLayout()
        # h2 = QHBoxLayout()
        # h3 = QHBoxLayout()
        # h4 = QHBoxLayout()
        # h5 = QHBoxLayout()

        # # names 列表是根据图片上控件顺序来排列的
        # names = [
        #     '', '', '',
        #     self.shopping_address, self.billing_Address, self.Payment_type,
        #     self.first_name1, self.first_name2, self.profile_name,
        #     self.last_name1, self.last_name2, self.email,
        #     self.country1, self.country2, self.card_type,
        #     self.address1, self.address2, self.card_number,
        #     self.address3, self.address4, '',
        #     self.county3, self.county4, self.cvv,
        #     self.city1, self.city2, '',
        #     self.state1, self.state2, '',
        #     self.zip_code1, self.zip_code2, '',
        #     self.phone_number1, self.phone_number2, ''
        # ]

        # positions = [(i, j) for i in range(12) for j in range(3)]

        # for position, name in zip(positions, names):
        #     if name == '':
        #         continue
        #     layout.addWidget(name, *position)

        # h2.addWidget(QSplitter())
        # h2.addWidget(self.title)
        # h2.addWidget(QSplitter())

        # h3.addWidget(self.month)
        # h3.addWidget(self.year)

        # h4.addWidget(QSplitter())
        # h4.addWidget(self.checkbox)
        # h4.addWidget(QSplitter())

        # h5.addWidget(self.submit)
        # h5.addWidget(QSplitter())
        # h5.addWidget(self.exit_close)

        # layout.addLayout(h2, 0, 1)
        # layout.addLayout(h3, 6, 2)
        # layout.addLayout(h4, 12, 1)
        # layout.addLayout(h5, 13, 1)

        # self.setLayout(layout)

        self.setWindowFlag(Qt.FramelessWindowHint)

        self.setStyleSheet('''

                            QWidget{

                            background: #1e1f29;

                            }

                            QLabel{font-family: "PingFangSC-Regular";

                            font-size: 16px;

                            font-weight: 400;

                            line-height: 16px;

                            text-align: center;

                            color: #5b5d6a;}

                            QFrame{

                            border-radius: 6px;

                            background: #1e1f29;

                            }

                            QGroupBox{

                            background: #1e1f29;

                            border:none;

                            }

                            QTextEdit{

                            border:0px;    

                            background:#181922;

                            border-radius: 8px;

                            color : white;

                            font-family: "PingFangSC-Regular";

                            font-size:16px;

                            }

                            

                            QCheckBox{color:#5b5d6a;}

                            QComboBox{

                            width: 160px;

							height: 32px;

							border-radius: 8px;

							background: #181922;

							color: #5b5d6a;

							font-family: "PingFangSC-Regular";

							font-size: 15px;

							font-weight: 400;

							line-height: 13px;

                            }

                            QComboBox::on{

                            border: 1px solid  #1fbc6f;

                            }


							QComboBox QAbstractItemView{border-radius: 8px;background: #181922;outline:0px;}

							QComboBox QAbstractItemView::item {

							border-radius: 8px;

							width: 160px;

							height: 28px;

							background: #181922;

							color: #5b5d6a;

							font-family: "PingFangSC-Regular";

							font-size: 15px;

							font-weight: 400;

							line-height: 13px;

							}


							QPushButton{border:none;font-size:13px;font-family:"PingFangSC-Medium";color: white;font-weight: 400;line-height: 16px;}

					        QPushButton:hover{

					        border:none;

					        border-width:1px;

					        border-style:none none solid none;

					        border-color:#1FBC6F;

					        font-size:13px;

					        font-family:"PingFangSC-Medium";

					        color: #ffffff;

					        font-weight: 400;

					        line-height: 16px;}

					        QPushButton:pressed{

					        border:none;

					        border-width:1px;

					        border-style:none none solid none;

					        border-color:#1FBC6F;

					        color: #ffffff;

							font-family: "PingFangSC-Medium";

							font-size: 13px;

							font-weight: 400;

							line-height: 16px;}

					        QPushButton:checked{

					        border:none;

					        border-width:1px;

					        border-style:none none solid none;

					        border-color:#1FBC6F;

					        font-size:13px;

					        font-family:"PingFangSC-Medium";

					        color: #ffffff;

					        font-weight: 400;

					        line-height: 16px;}



							QComboBox QAbstractItemView::item:hover{

							background:gray;

							color:white;

							}

                            QComboBox::drop-down{

                            border:none;

                            image: url(:/static/xiala.png);

                            }

                            QGroupBox{

                            background: #1e1f29;

                            border:none;

                            }

                            QLineEdit{

                            width: 160px;

							height: 30px;

							border-radius: 8px;

							background: #181922;

							color: #5b5d6a;

							font-family: "PingFangSC-Regular";

							font-size: 15px;

							font-weight: 400;

							line-height: 13px;

                            }

                            QSplitter{

                            background-color: #1e1f29;

                            }

                            QCheckBox::indicator:checked{

							    image:url(:/static/check.png);
							}
							QCheckBox::indicator:unchecked{

							    image:url(:/static/uncheck.png);
							}

							QCheckBox{color: #5c5858;

							font-family: "PingFangSC-Regular";

							font-size: 11px;

							font-weight: 400;

							line-height: 13px;}''')

        self.submit.setStyleSheet('''width: 100px;

                height: 30px; 

                border-radius: 6px;

                color: #ffffff;

                font-family: "PingFangSC-Medium";

                font-size: 12px;

                font-weight: 400;

                line-height: 16px;

                background: qlineargradient(x1:0, y1:1, x2:0, y2:1,stop:0 #3EC169,stop:1 #1BBB70);''')

        self.exit_close.setStyleSheet('''width: 100px;

            height: 30px; 

            border-radius: 6px;

            color: #ffffff;

            font-family: "PingFangSC-Medium";

            font-size: 12px;

            font-weight: 400;

            line-height: 16px;

            border-style:none none none none;

            background: #5c5858;''')

        self.label.setStyleSheet('''width: 48px;

							height: 19px;

							color: #ffffff;

							font-family: "PingFangSC-Medium";

							font-size: 14px;

							font-weight: 400;

							line-height: 13px;''')

    def setQss(self):
        self.mid_widget.currentWidget().pushButton.setStyleSheet('''
    		QPushButton{width: 110px;

			height: 30px;

			border-radius: 8px;

			background: #181922;

			color: #5b5d6a;

			font-family: "PingFangSC-Regular";

			font-size: 15px;

			font-weight: 400;

			line-height: 15px;

            }

            QPushButton:hover{

	        border:1px solid  #1fbc6f;

	        font-size:16px;

	        font-family:"PingFangSC-Regular";

	        color: #ffffff;

	        font-weight: 400;

	        line-height: 16px;}

	        QPushButton:pressed{

	        border:1px solid  #1fbc6f;

	        font-size:16px;

	        font-family:"PingFangSC-Regular";

	        color: #ffffff;

	        font-weight: 400;

	        line-height: 16px;}

	        QPushButton:checked{

	        border:1px solid  #1fbc6f;

	        font-size:16px;

	        font-family:"PingFangSC-Regular";

	        color: #ffffff;

	        font-weight: 400;

	        line-height: 16px;}
        ''')

        self.mid_widget.currentWidget().comboBox.setStyleSheet('''
    		QComboBox{

            width: 110px;

			height: 32px;

			border-radius: 8px;

			background: #181922;

			color: #5b5d6a;

			font-family: "PingFangSC-Regular";

			font-size: 15px;

			font-weight: 400;

			line-height: 13px;

            }''')

    def submit_action(self):
        AddressFunc.confirm_btn_action(self)
        self.close()
        

    def exit_action(self):
        self.close()

class ShippingWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout.addWidget(self.lineEdit_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout.addWidget(self.lineEdit_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEdit_5 = QtWidgets.QLineEdit(self)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout_3.addWidget(self.lineEdit_5)
        self.comboBox = QQComboBox()
        self.comboBox.setView(QListView())
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_3.addWidget(self.comboBox)
        self.lineEdit_7 = QtWidgets.QLineEdit(self)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.horizontalLayout_3.addWidget(self.lineEdit_7)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.setStretch(2, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lineEdit_8 = QtWidgets.QLineEdit(self)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.horizontalLayout_4.addWidget(self.lineEdit_8)
        self.lineEdit_9 = QtWidgets.QLineEdit(self)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.horizontalLayout_4.addWidget(self.lineEdit_9)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(4, 1)

        self.lineEdit.setPlaceholderText(' First Name')
        self.lineEdit_2.setPlaceholderText(' Last Name')
        self.lineEdit_3.setPlaceholderText(' Address1')
        self.lineEdit_4.setPlaceholderText(' Address2')
        self.lineEdit_5.setPlaceholderText(' City')
        self.lineEdit_7.setPlaceholderText(' Postal Code')
        self.lineEdit_8.setPlaceholderText(' Email')

        self.lineEdit_9.setPlaceholderText(' Phone Number')

        self.comboBox.addItem(' State')

class BillingWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.checkBox = QtWidgets.QCheckBox(self)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_6.addWidget(self.checkBox)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout.addWidget(self.lineEdit_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout.addWidget(self.lineEdit_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEdit_5 = QtWidgets.QLineEdit(self)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout_3.addWidget(self.lineEdit_5)
        self.comboBox = QQComboBox()
        self.comboBox.setView(QListView())
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_3.addWidget(self.comboBox)
        self.lineEdit_7 = QtWidgets.QLineEdit(self)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.horizontalLayout_3.addWidget(self.lineEdit_7)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.setStretch(2, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lineEdit_8 = QtWidgets.QLineEdit(self)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.horizontalLayout_4.addWidget(self.lineEdit_8)
        self.lineEdit_9 = QtWidgets.QLineEdit(self)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.horizontalLayout_4.addWidget(self.lineEdit_9)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(4, 1)


        self.lineEdit.setPlaceholderText(' First Name')
        self.lineEdit_2.setPlaceholderText(' Last Name')
        self.lineEdit_3.setPlaceholderText(' Address1')
        self.lineEdit_4.setPlaceholderText(' Address2')
        self.lineEdit_5.setPlaceholderText(' City')
        self.lineEdit_7.setPlaceholderText(' Postal Code')
        self.lineEdit_8.setPlaceholderText(' Email')
        self.lineEdit_8.setReadOnly(True)
        self.lineEdit_8.setStyleSheet('''background: rgba(24,25,34,50);''')
        self.lineEdit_9.setPlaceholderText(' Phone Number')
        self.checkBox.setText("Same With Shipping")
        self.comboBox.addItem(' State')


class PaymentWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.comboBox = QQQComboBox(parent = self)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        self.pushButton = QPushButton(self)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 96, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_2.addWidget(self.lineEdit_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_2.addWidget(self.lineEdit_4)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 2)
        self.verticalLayout.setContentsMargins(-1,50,-1,-1)

        self.pushButton.setText("Bank Card")
        self.lineEdit_2.setPlaceholderText(' Card Number')
        self.lineEdit_3.setPlaceholderText(' MM/YY')
        self.lineEdit_4.setPlaceholderText(' XXX')

        self.pushButton.setCheckable(True)

        self.pushButton.setAutoExclusive(True)
        self.pushButton.clicked.connect(self.buttonClicked)

        self.comboBox.setView(QListView())

        self.comboBox.addItem(' Gift Card')
        self.comboBox.addItem(' 美 国')
        self.comboBox.addItem(' 英 国')

        # self.comboBox.clicked.connect(self.boxClicked)

        # self.pushButton.clicked.connect(lambda:self.pushButton.setChecked(True))

    def boxClicked(self):
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_2.setStyleSheet('''background: rgba(24,25,34,50);''')
        self.lineEdit_3.setStyleSheet('''background: rgba(24,25,34,50);''')
        self.lineEdit_4.setStyleSheet('''background: rgba(24,25,34,50);''')
        self.comboBox.setStyleSheet('''QComboBox{

                            border: 1px solid  #1fbc6f;

                            width: 110px;

							height: 32px;

                            }''')
        self.pushButton.setChecked(False)

    def buttonClicked(self):
        self.lineEdit_2.setReadOnly(False)
        self.lineEdit_3.setReadOnly(False)
        self.lineEdit_4.setReadOnly(False)
        self.lineEdit_2.setStyleSheet('''background: rgba(24,25,34);''')
        self.lineEdit_3.setStyleSheet('''background: rgba(24,25,34);''')
        self.lineEdit_4.setStyleSheet('''background: rgba(24,25,34);''')
        self.comboBox.setStyleSheet('''QComboBox{

        					width: 110px;

							height: 32px;

                            border: none;

                            }''')

        

        






class QPushButton(QPushButton):
    def __init__(self, *__args: any,clicked = None):
        super(QPushButton,self).__init__(*__args)
        self.setCursor(Qt.PointingHandCursor)
        self.setIconSize(QSize(14, 14))

class QQComboBox(QComboBox):
	def __init__(self):
		super(QQComboBox, self).__init__()

	def mousePressEvent(self, QMouseEvent):
		self.showPopup()
		

	def showPopup(self):
		QComboBox.showPopup(self)
		pop = self.children()[1]
		pop.setStyleSheet('''border-radius: 8px;background: #181922''')
		pop.move(pop.x(), pop.y() + 5)

class QQQComboBox(QComboBox):
	def __init__(self, parent = None):
		super(QQQComboBox, self).__init__(parent)
		self.parent = parent
		self.checked = 0

	def mousePressEvent(self, QMouseEvent):
		self.checked = 1
		self.parent.boxClicked()
		self.showPopup()

	def showPopup(self):
		QComboBox.showPopup(self)
		pop = self.children()[1]
		pop.setStyleSheet('''border-radius: 8px;background: #181922''')
		pop.move(pop.x(), pop.y() + 5)

if __name__ == '__main__':
    from querymodel import myTableModel, MyTableView, MyTableView1, MyTableView2, MyTableView3, MyTableView4, MyTableView5,MyTableView6
    app = QApplication(sys.argv)
    ex = magicPillWindow()
    # ex = settingWindow()
    ex.show()
    sys.exit(app.exec_())
