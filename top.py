from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize, Qt
from PyQt5 import QtGui
from PyQt5.QtWidgets import QHBoxLayout, QPushButton, QAbstractItemView, QTableView, QVBoxLayout, QSplitter, \
    QApplication, QGroupBox, QLabel, QGridLayout, QLineEdit, QComboBox, QTextEdit, QCheckBox
from PyQt5.QtWidgets import QListWidget, QStackedWidget
from PyQt5.QtWidgets import QListWidgetItem, QSizePolicy
from PyQt5.QtWidgets import QWidget, QSpacerItem
from PyQt5.QtGui import QPixmap, QIcon
from png import *
import sys

from Interface import SettingFunc


class Top(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # self.setObjectName("self")
        # self.resize(960, 40)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.widget_2 = QtWidgets.QWidget(self)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_4 = QPushButton(QIcon(':/static/task.png'),' 任务',self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setObjectName("pushButton_4")
        # self.horizontalLayout_3.addWidget(QSplitter(Qt.Vertical))
        self.horizontalLayout_3.addWidget(self.pushButton_4)
        self.pushButton_10 = QPushButton(QIcon(':/static/agent.png'),' 代理',self.widget_2)
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout_3.addWidget(self.pushButton_10)
        self.pushButton_9 = QPushButton(QIcon(':/static/account.png'),' 账号',self.widget_2)
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_3.addWidget(self.pushButton_9)
        self.pushButton_8 = QPushButton(QIcon(':/static/code.png'),' 折扣码',self.widget_2)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_3.addWidget(self.pushButton_8)
        self.pushButton_7 = QPushButton(QIcon(':/static/gift.png'),' 礼品卡',self.widget_2)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_3.addWidget(self.pushButton_7)
        self.pushButton_5 = QPushButton(QIcon(':/static/address.png'),' 地址',self.widget_2)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_3.addWidget(self.pushButton_5)
        self.pushButton_6 = QPushButton(QIcon(':/static/order.png'),' 订单',self.widget_2)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_3.addWidget(self.pushButton_6)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.setStretch(2, 1)
        self.horizontalLayout_3.setStretch(3, 1)
        self.horizontalLayout_3.setStretch(4, 1)
        self.horizontalLayout_3.setStretch(5, 1)
        self.horizontalLayout_3.setStretch(6, 1)
        self.horizontalLayout_3.setStretch(7, 1)
        self.horizontalLayout_2.addWidget(self.widget_2)
        self.widget = QtWidgets.QWidget(self)
        self.widget.setObjectName("widget")
        # self.setAutoFillBackground(False)
        self.pushButton_3 = QPushButton(QIcon(':/static/setting.png'),'',self.widget)
        self.pushButton_3.clicked.connect(self.showSetting)
        self.pushButton = QPushButton(QIcon(':/static/min.png'),'',self.widget)
        self.pushButton.clicked.connect(self.showMinimized)
        self.pushButton_2 = QPushButton(QIcon(':/static/close.png'),'',self.widget)
        self.pushButton_2.clicked.connect(self.close)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        # self.pushButton_3 = QPushButton(self.widget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        # self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        # self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.horizontalLayout_2.addWidget(self.widget)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 7)
        self.horizontalLayout_2.setStretch(2, 1)
        pix = QtGui.QPixmap(':/static/logo.png')
        self.label.setPixmap(pix)
        self.label.setScaledContents(True)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_3.setSpacing(20)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setContentsMargins(25, 0, 0, 0)
        self.setQss()

        self.pushButton_4.setAttribute(Qt.WA_Hover,True)
        self.pushButton_4.installEventFilter(self)
        self.pushButton_10.setAttribute(Qt.WA_Hover,True)
        self.pushButton_10.installEventFilter(self)
        self.pushButton_9.setAttribute(Qt.WA_Hover,True)
        self.pushButton_9.installEventFilter(self)
        self.pushButton_8.setAttribute(Qt.WA_Hover,True)
        self.pushButton_8.installEventFilter(self)
        self.pushButton_7.setAttribute(Qt.WA_Hover,True)
        self.pushButton_7.installEventFilter(self)
        self.pushButton_6.setAttribute(Qt.WA_Hover,True)
        self.pushButton_6.installEventFilter(self)
        self.pushButton_5.setAttribute(Qt.WA_Hover,True)
        self.pushButton_5.installEventFilter(self)
        self.pushButton_4.setMinimumSize(0,40)
        self.pushButton_10.setMinimumSize(0,40)
        self.pushButton_9.setMinimumSize(0,40)
        self.pushButton_8.setMinimumSize(0,40)
        self.pushButton_7.setMinimumSize(0,40)
        self.pushButton_6.setMinimumSize(0,40)
        self.pushButton_5.setMinimumSize(0,40)

    def showSetting(self):
        self.settingWindow = settingWindow()
        self.settingWindow.setWindowModality(Qt.ApplicationModal)
        self.settingWindow.show()


    def eventFilter(self, object, event):
        if object == self.pushButton_4:
            if event.type() == QtCore.QEvent.HoverEnter:
                self.pushButton_4.setIcon(QIcon(':/static/taskh.png'))
                return True
            if event.type() == QtCore.QEvent.HoverLeave and not self.pushButton_4.isChecked():
                self.pushButton_4.setIcon(QIcon(':/static/task.png'))
                return True
        if object == self.pushButton_10:
            if event.type() == QtCore.QEvent.HoverEnter:
                self.pushButton_10.setIcon(QIcon(':/static/agenth.png'))
                return True
            if event.type() == QtCore.QEvent.HoverLeave and not self.pushButton_10.isChecked():
                self.pushButton_10.setIcon(QIcon(':/static/agent.png'))
                return True
        if object == self.pushButton_9:
            if event.type() == QtCore.QEvent.HoverEnter:
                self.pushButton_9.setIcon(QIcon(':/static/accounth.png'))
                return True
            if event.type() == QtCore.QEvent.HoverLeave and not self.pushButton_9.isChecked():
                self.pushButton_9.setIcon(QIcon(':/static/account.png'))
                return True
        if object == self.pushButton_8:
            if event.type() == QtCore.QEvent.HoverEnter:
                self.pushButton_8.setIcon(QIcon(':/static/codeh.png'))
                return True
            if event.type() == QtCore.QEvent.HoverLeave and not self.pushButton_8.isChecked():
                self.pushButton_8.setIcon(QIcon(':/static/code.png'))
                return True
        if object == self.pushButton_7:
            if event.type() == QtCore.QEvent.HoverEnter:
                self.pushButton_7.setIcon(QIcon(':/static/gifth.png'))
                return True
            if event.type() == QtCore.QEvent.HoverLeave and not self.pushButton_7.isChecked():
                self.pushButton_7.setIcon(QIcon(':/static/gift.png'))
                return True
        if object == self.pushButton_5:
            if event.type() == QtCore.QEvent.HoverEnter:
                self.pushButton_5.setIcon(QIcon(':/static/addressh.png'))
                return True
            if event.type() == QtCore.QEvent.HoverLeave and not self.pushButton_5.isChecked():
                self.pushButton_5.setIcon(QIcon(':/static/address.png'))
                return True
        if object == self.pushButton_6:
            if event.type() == QtCore.QEvent.HoverEnter:
                self.pushButton_6.setIcon(QIcon(':/static/orderh.png'))
                return True
            if event.type() == QtCore.QEvent.HoverLeave and not self.pushButton_6.isChecked():
                self.pushButton_6.setIcon(QIcon(':/static/order.png'))
                return True
        return False


    def setQss(self):
        self.setStyleSheet('''
        QWidget{background : #1e1f29;}

        QListWidget{

        background: #1e1f29;

        outline:0px;}

        QListWidget::Item{

        border:none;

        outline:0px;}

        QPushButton{border:none;font-size:16px;font-family:"PingFangSC-Regular";color: #606060;font-weight: 400;line-height: 16px;}

        QPushButton:hover{

        border:none;

        border-width:1px;

        border-style:none none solid none;

        border-color:#1FBC6F;

        font-size:16px;

        font-family:"PingFangSC-Regular";

        color: #ffffff;

        font-weight: 400;

        line-height: 16px;}

        QPushButton:pressed{

        border:none;

        border-width:1px;

        border-style:none none solid none;

        border-color:#1FBC6F;

        font-size:16px;

        font-family:"PingFangSC-Regular";

        color: #ffffff;

        font-weight: 400;

        line-height: 16px;}

        QPushButton:checked{

        border:none;

        border-width:1px;

        border-style:none none solid none;

        border-color:#1FBC6F;

        font-size:16px;

        font-family:"PingFangSC-Regular";

        color: #ffffff;

        font-weight: 400;

        line-height: 16px;}''')

class settingWindow(QWidget):
    """设置窗口"""

    def __init__(self):
        super().__init__()
        self.resize(520,380)
        self.setFixedSize(self.width(), self.height())

        # self.cookieset = QLabel('cookie设置:')  # cookie设置: 标签
        self.wxset = QLabel('微信通知设置')  # 微信通知设置：标签
        self.language_label = QLabel('语言设置')
        self.webhook = QLabel('WebHook:')  # webhook:标签
        self.wxset.setObjectName('wxset')
        self.language_label.setObjectName('language_label')
        self.webhook.setObjectName('webhook')

        self.uid_label = QLabel('UID:')  # uid:标签
        self.app_token = QLabel('APP_token:')  # APP_token:标签
        self.label = QLabel('   设置')

        self.language_combobox = QQComboBox()

        # self.local_btn = QPushButton('本地模式')  # 本地模式按钮
        # self.local_btn.setCheckable(True)
        # self.bp_btn = QPushButton('BP模式')  # BP模式按钮
        # self.bp_btn.setCheckable(True)
        self.gift_change = QPushButton('礼品卡余额变动')  # 礼品卡余额变动按钮
        self.gift_change.setCheckable(True)
        self.order_btn = QPushButton('成功订单')  # 成功订单按钮
        self.order_btn.setCheckable(True)
        self.cancel_btn = QPushButton('确定')
        self.cancel_btn.clicked.connect(self.close)
        # self.local_btn.clicked[bool].connect(self.cookie_setting_Action)
        # self.bp_btn.clicked[bool].connect(self.cookie_setting_Action)
        self.gift_change.clicked[bool].connect(self.gift_order_Action)
        self.order_btn.clicked[bool].connect(self.gift_order_Action)
        # self.local_btn.toggled.connect(self.cookie_setting_Action)
        # self.bp_btn.toggled.connect(self.cookie_setting_Action)
        # self.gift_change.toggled.connect(self.gift_order_Action)
        # self.order_btn.toggled.connect(self.gift_order_Action)

        self.test_btn = QPushButton('测试')  # 测试按钮
        self.test_btn.clicked.connect(self.test_action)
        self.unbound_machine = QPushButton('解绑机器')  # 解绑机器按钮
        self.unbound_machine.clicked.connect(self.unbound_machine_action)

        # self.open_btn = QPushButton('打开生产')  # 打开生产按钮
        # self.open_btn.clicked.connect(self.open_btn_action)
        # self.close_btn = QPushButton('关闭生产')  # 关闭生产按钮
        # self.close_btn.clicked.connect(self.close_btn_action)
        # self.delete_cookie = QPushButton('删除Cookie')  # 删除Cookie按钮
        # self.delete_cookie.clicked.connect(self.delete_cookie_action)

        self.line1 = QLineEdit()  # uid:标签后面的输入框
        self.line1.setPlaceholderText(' 请输入UID')
        self.line2 = QLineEdit()  # APP_token:标签后面的输入框
        self.line2.setPlaceholderText(' 请输入APP_ToKen')
        self.line3 = QLineEdit()  # webhook:标签后面的输入框
        self.line3.setPlaceholderText(' 请输入WebHook')

        self.chekbox1 = QCheckBox()
        self.chekbox2 = QCheckBox()
        self.chekbox1.setCursor(Qt.PointingHandCursor)
        self.chekbox2.setCursor(Qt.PointingHandCursor)
        self.chekboxl1 = QLabel('成功订单  ')
        self.chekboxl2 = QLabel('GC余额变动')
        # self.chekbox1.setLayoutDirection(Qt.RightToLeft)
        # self.chekbox2.setLayoutDirection(Qt.RightToLeft)

        # self.groupBox = QGroupBox()
        # self.groupBox1 = QGroupBox()

        h1 = QVBoxLayout()
        h2 = QVBoxLayout()
        h3 = QHBoxLayout()
        h4 = QVBoxLayout()
        layout = QVBoxLayout()
        layout1 = QHBoxLayout()
        layout2 = QHBoxLayout()
        layout3 = QHBoxLayout()
        layout4 = QHBoxLayout()
        layout5 = QHBoxLayout()
        layout6 = QHBoxLayout()
        layout7 = QHBoxLayout()
        layout8 = QHBoxLayout()
        layout9 = QVBoxLayout()

        # layout1.addWidget(self.open_btn)
        # layout1.addWidget(self.close_btn)
        # layout1.addWidget(self.delete_cookie)
        # self.groupBox1.setLayout(layout1)

        # layout2.addWidget(self.cookieset)
        # layout2.addWidget(self.local_btn)
        # layout2.addWidget(self.bp_btn)

        # layout3.addWidget(self.wxset)
        h2.addWidget(self.language_label)
        h3.addWidget(self.language_combobox)
        h3.addWidget(QSplitter())
        h2.addLayout(h3)
        layout3.addWidget(self.line1)
        # layout3.addWidget(QSplitter())
        layout3.addWidget(self.chekboxl1)
        layout3.addWidget(self.chekbox1)
        h1.addWidget(self.wxset)

        # layout4.addWidget(QSplitter())
        layout4.addWidget(self.line2)
        # layout4.addWidget(QSplitter())
        layout4.addWidget(self.chekboxl2)
        layout4.addWidget(self.chekbox2)
        h1.addLayout(layout3)
        h1.addLayout(layout4)

        # layout5.addWidget(QSplitter())
        # layout5.addWidget(self.gift_change)
        # layout5.addWidget(self.order_btn)

        layout6.addWidget(self.line3)
        layout6.addWidget(self.test_btn)
        layout6.setSpacing(0)

        layout7.addWidget(QSplitter())
        layout7.addWidget(self.unbound_machine)
        layout7.addWidget(self.cancel_btn)
        layout7.addWidget(QSplitter())

        # layout.addLayout(layout2)
        # layout.addWidget(self.groupBox1)
        layout.addLayout(h2)
        layout.addLayout(h1)
        # layout.addLayout(layout4)
        # layout.addLayout(layout5)
        layout.addWidget(self.webhook)
        layout.addLayout(layout6)
        layout.addLayout(layout7)
        layout.setSpacing(15)
        layout.setContentsMargins(80,15,80,15)
        h4.addWidget(self.label)
        h4.addLayout(layout)
        # self.groupBox.setLayout(layout)

        # layout8.addWidget(QSplitter())
        # layout8.addLayout(lay)
        # layout8.addWidget(QSplitter())

        # layout9.addWidget(QSplitter())
        # layout9.addLayout(layout8)
        # layout9.addWidget(QSplitter())

        self.setWindowFlag(Qt.FramelessWindowHint)

        self.setLayout(h4)

        self.setStyleSheet('''

                            QCheckBox::indicator { 

                            width: 38px;

                            height: 20px;

                            color: #5b5d6a;

                            font-family: "PingFangSC-Regular";

                            font-size: 10px;

                            font-weight: 400;

                            line-height: 13px;

                            text-align:left;

                            }

                            QCheckBox::indicator::unchecked {  

                            image: url(:/static/checkoff.png);

                            }

                            QCheckBox::indicator::checked { 

                            image: url(:/static/checkon.png);

                            }

                            QWidget{

                            background: #1e1f29;

                            }

                            QLabel{font-family: "PingFangSC-Regular";

                            font-size: 15px;

                            font-weight: 400;

                            line-height: 15px;

                            text-align: center;

                            color: #5b5d6a;}

                            QLabel#wxset{color: #a9aab2;}

                            QLabel#language_label{color: #a9aab2;}

                            QLabel#webhook{color: #a9aab2;}

                            
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

                            background:#5b5d6a;

                            border : none;

                            }

                            QComboBox::drop-down{

                            border:none;

                            image: url(:/static/down.png);

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

                            font-size: 14px;

                            font-weight: 400;

                            line-height: 13px;

                            }''')
        
        self.label.setStyleSheet('''width: 48px;

                            height: 19px;

                            color: #ffffff;

                            font-family: "PingFangSC-Medium";

                            font-size: 15px;

                            font-weight: 400;

                            line-height: 16px;''')
        

        self.gift_change.setStyleSheet('''QPushButton{width: 90px;

                height: 25px; 

                border-radius: 6px;

                color: #ffffff;

                font-family: "PingFangSC-Medium";

                font-size: 12px;

                font-weight: 400;

                line-height: 16px;

                background: #5c5858;}

                QPushButton:checked{

                background: qlineargradient(x1:0, y1:1, x2:0, y2:1,stop:0 #3EC169,stop:1 #1BBB70);

                }''')

        self.order_btn.setStyleSheet('''QPushButton{width: 90px;

                height: 25px; 

                border-radius: 6px;

                color: #ffffff;

                font-family: "PingFangSC-Medium";

                font-size: 12px;

                font-weight: 400;

                line-height: 16px;

                background: #5c5858;}

                QPushButton:checked{

                background: qlineargradient(x1:0, y1:1, x2:0, y2:1,stop:0 #3EC169,stop:1 #1BBB70);

                }''')

        self.line3.setStyleSheet('''

            width: 160px;

            height: 30px;

            border-radius: 0px;

            background: #181922;

            color: #5b5d6a;

            font-family: "PingFangSC-Regular";

            font-size: 12px;

            font-weight: 400;

            line-height: 13px;

            border-top-left-radius:8px;

            border-bottom-left-radius:8px;

            ''')

        self.test_btn.setStyleSheet('''

                color: #5b5d6a;

                font-family: "PingFangSC-Regular";

                font-size: 13px;

                font-weight: 400;

                line-height: 13px;

                text-align: center;

                border:none;

                width: 30px;

                height: 30px;

                background: #12131b;

                border-top-right-radius:8px;

                border-bottom-right-radius:8px;''')

        self.unbound_machine.setStyleSheet('''width: 100px;

            height: 30px; 

            border-radius: 6px;

            color: #ffffff;

            font-family: "PingFangSC-Medium";

            font-size: 12px;

            font-weight: 400;

            line-height: 16px;

            background: #5c5858;''')

        self.cancel_btn.setStyleSheet('''width: 100px;

                height: 30px; 

                border-radius: 6px;

                color: #ffffff;

                font-family: "PingFangSC-Medium";

                font-size: 12px;

                font-weight: 400;

                line-height: 16px;

                background: qlineargradient(x1:0, y1:1, x2:0, y2:1,stop:0 #3EC169,stop:1 #1BBB70);''')

    def cookie_setting_Action(self):
        source = self.sender()
        if source.text() == '本地模式':
            self.local_btn.setChecked(True)
            self.bp_btn.setChecked(False)
        if source.text() == 'BP模式':
            self.local_btn.setChecked(False)
            self.bp_btn.setChecked(True)

    def gift_order_Action(self):
        source = self.sender()
        if source.text() == '礼品卡余额变动':
            self.gift_change.setChecked(True)
            self.order_btn.setChecked(False)
        if source.text() == '成功订单':
            self.gift_change.setChecked(False)
            self.order_btn.setChecked(True)

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

    def test_action(self):
        SettingFunc.test_action(self)

    def unbound_machine_action(self):
        SettingFunc.unbound_machine_action(self)

    # def open_btn_action(self):
    #     pass

    # def close_btn_action(self):
    #     pass

    # def delete_cookie_action(self):
    #     pass
class QPushButton(QPushButton):
    def __init__(self, *__args: any,clicked = None):
        super(QPushButton,self).__init__(*__args)
        self.setCursor(Qt.PointingHandCursor)
        self.setIconSize(QSize(20, 20))

class QQComboBox(QComboBox):
    def __init__(self):
        super(QQComboBox, self).__init__()
        self.setCursor(Qt.PointingHandCursor)

    def mousePressEvent(self, QMouseEvent):
        self.showPopup()
        

    def showPopup(self):
        QComboBox.showPopup(self)
        pop = self.children()[1]
        pop.setStyleSheet('''border-radius: 8px;background: #181922''')
        pop.move(pop.x(), pop.y() + 5)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = Top()
    gui.show()
    sys.exit(app.exec_())